<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Computation of Linear Models by Convex Relaxation

Topics include Robust subspace recovery, Convex relaxation, REAPER, Outlier robustness, Orthogonal projectors, High-dimensional statistics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces REAPER, a convex relaxation for fitting a low-dimensional linear subspace in the presence of many outliers by optimizing over a convex hull of orthogonal projectors. The paper matters because it couples a practical solver with recovery theory for noisy inliers, making robust PCA-style model fitting less dependent on brittle combinatorial inlier selection.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Consider a dataset of vector-valued observations that consists of noisy inliers, which are explained well by a low-dimensional subspace, along with some number of outliers. This work describes a convex optimization problem, called REAPER, that can reliably fit a low-dimensional model to this type of data. This approach parameterizes linear subspaces using orthogonal projectors, and it uses a relaxation of the set of orthogonal projectors to reach the convex formulation. The paper provides an efficient algorithm for solving the REAPER problem, and it documents numerical experiments which confirm that REAPER can dependably find linear structure in synthetic and natural data. In addition, when the inliers lie near a low-dimensional subspace, there is a rigorous theory that describes when REAPER can approximate this subspace.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Low-dimensional linear models have applications in a huge array of data analysis problems. Let us highlight some examples from computer vision, machine learning, and bioinformatics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

: Images of a face---or any Lambertian object---viewed under different illumination conditions lie near a nine-dimensional subspace:5pm2; HYL+03:Clustering-Appearances;:Lambertian-Reflectance.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

: Feature points on a moving rigid body lie on an affine space of dimension three, assuming the affine camera model:Multibody-Factorization. More generally, estimating structure from motion involves estimating low-rank matrices (:Efficient-Computation Sec. 5.2).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

: We can describe a large corpus of documents that concern a small number of topics using a low-dimensional linear model DDL+88:Improving-Information.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

: Low-dimensional models of single nucleotide polymorphism (SNP) data have been used to show that the genotype of an individual is correlated with her geographical ancestry NJB+08:Genes-Mirror. More generally, linear models are used to assess differences in allele frequencies among populations PPP+06:Principal-Components.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In most of these applications, the datasets are noisy, and they contain a substantial number of outliers. Principal component analysis, the standard method for finding a low-dimensional linear model, is sensitive to these non-idealities. As a consequence, good robust modeling techniques would be welcome in a range of scientific and engineering disciplines.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, researchers have started to use convex optimization to develop alternatives to principal component analysis that have more favorable robustness properties. For the most part, these formulations attempt to find a low-rank matrix that approximates the data well. They typically use the Schatten 1-norm as a convex proxy for the rank. See Section 6 for a more complete discussion. Although these ideas are compelling, it remains valuable to explore other methods because of the importance of linear modeling.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper describes a new technique for fitting a low-dimensional linear model to data. Our formulation is based on convex optimization, but it has a different flavor from the earlier techniques. We use a new set of ideas to develop a rigorous analysis of the performance of our method. This theory demonstrates that the approach is robust against noise in the inliers, and it can cope with a large number of adversarial outliers. We describe an efficient numerical algorithm that is guaranteed to solve the optimization problem after a modest number of spectral calculations. We also include some experiments with synthetic and natural data to verify that our technique reliably seeks out linear structure.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Linear Modeling by Principal Component Analysis", "weight": 1.0} -->

To motivate our approach to linear modeling, we summarize a classical line of research in statistics that begins with principal component analysis.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Linear Modeling by Principal Component Analysis", "weight": 1.0} -->

Let $\mathcal{X}$ be a dataset^11^1A dataset is simply a finite multiset, that is, a finite set with repeated elements allowed. consisting of $N$ points in ${\mathbb{R}}^{D}$. Suppose we wish to determine a $d$-dimensional subspace that best explains the data. For each point, we can measure the residual error in the approximation by computing the orthogonal distance from the point to the subspace.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Linear Modeling by Principal Component Analysis", "weight": 1.0} -->

(Here and elsewhere, sums indexed by a dataset repeat each point as many times as it appears in the dataset.) The approach (1.2) is equivalent with the method of *principal component analysis* (PCA) from the statistics literature:Principal-Component and the *total least squares* (TLS) method from the linear algebra community:Total-Least.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Linear Modeling by Principal Component Analysis", "weight": 1.0} -->

The mathematical program (1.2) is not convex because orthoprojectors do not form a convex set, so we have no right to expect that the problem is tractable. Nevertheless, we can compute an analytic solution by means of a singular value decomposition (SVD) of the data:Principal-Axis;:Total-Least. Suppose that $\mathbf{X}$ is a $D \times N$ matrix whose columns are the data points, arranged in fixed order, and let ${\mathbf{X}} = {{\mathbf{U}}\mathbf{\Sigma}{\mathbf{V}}^{\mathsf{t}}}$ be an SVD of this matrix. Form the $D \times d$ matrix ${\mathbf{U}}_{d}$ by extracting the first $d$ columns of $\mathbf{U}$; the columns of ${\mathbf{U}}_{d}$ are often called the *principal components* of the data.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Classical Methods for Achieving Robustness", "weight": 1.0} -->

Imagine now that the dataset $\mathcal{X}$ contains *inliers*, points we hope to explain with a linear model, as well as *outliers*, points that come from another process, such as a different population or noise. The data are not labeled, so it may be challenging to distinguish inliers from outliers. If we apply the PCA formulation (1.2) to fit a subspace to $\mathcal{X}$, the rogue points can interfere with the linear model for the inliers.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Classical Methods for Achieving Robustness", "weight": 1.0} -->

To guard the subspace estimation procedure against outliers, statisticians have proposed to replace the sum of squares in (1.2) with a figure of merit that is less sensitive to outliers. One possibility is to sum the *unsquared* residuals, which reduces the contribution from large residuals that may result from aberrant data points. This idea leads to the following optimization problem.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Classical Methods for Achieving Robustness", "weight": 1.0} -->

In case $d = {D - 1}$, the problem (1.3) is sometimes called *orthogonal $\ell_{1}$ regression*:Orthogonal-Linear or *least orthogonal absolute deviations*:Least-Orthogonal. The extension to general $d$ is apparently more recent:Some-Problems;:R1-PCA. See the books:Robust-Statistics;:Robust-Regression;:Robust-Statistics for an extensive discussion of other ways to combine residuals to obtain robust estimators.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Classical Methods for Achieving Robustness", "weight": 1.0} -->

Unfortunately, the mathematical program (1.3) is not convex, and, in contrast to (1.2), no deus ex machina emerges to make the problem tractable. Although there are many algorithms:Least-Orthogonal;:Iterative-Linear;:Orthogonal-Linear;:Gauss-Newton-Method;:R1-PCA;:Median-k-Flats that attempt (1.3), none is guaranteed to return a global minimum. In fact, most of the classical proposals for robust linear modeling involve intractable optimization problems, which makes them poor options for computation in spite of their theoretical properties:Robust-Statistics.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Convex Program for Robust Linear Modeling", "weight": 1.0} -->

The goal of this paper is to develop, analyze, and test a rigorous method for fitting robust linear models by means of convex optimization. We propose to *relax* the hard optimization problem (1.3) by replacing the nonconvex constraint set with a larger convex set. The advantage of this approach is that we can solve the resulting convex program completely using a variety of efficient algorithms.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Convex Program for Robust Linear Modeling", "weight": 1.0} -->

The idea behind our relaxation is straightforward. Each eigenvalue of an orthoprojector $\mathbf{\Pi}$ equals zero or one because $\mathbf{\Pi}^{2} = \mathbf{\Pi}$. Although a 0--1 constraint on eigenvalues is hard to enforce, the symmetric matrices whose eigenvalues lie in the interval $\lbrack 0,1\rbrack$ form a convex set. This observation leads us to frame the following convex optimization problem. Given a dataset $\mathcal{X}$ in ${\mathbb{R}}^{D}$ and a target dimension $d \in {\{ 1,2,\ldots,{D - 1}\}}$ for the linear model, we solve

<!-- chunk {"id": "body-0022", "role": "body", "section": "Convex Program for Robust Linear Modeling", "weight": 1.0} -->

We refer to (1.4) as reaper because it attempts to harvest linear structure from data.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Tighter Relaxation?", "weight": 1.0} -->

One may wonder whether it is possible to find a tighter relaxation of (1.3) than our proposed formulation (1.4). If we restrict our attention to convex programs, the answer is negative.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Fact 1.1", "weight": 1.0} -->

To prove this fact, it suffices to apply a diagonalization argument and to check that the set $\{{{\mathbf{λ}} \in {\mathbb{R}}^{D}}:{{\sum_{i = 1}^{D}\lambda_{i}} = {d\text{~and~}0} \leq \lambda_{i} \leq 1}\}$ is the convex hull of the set of vectors that have $d$ ones and $D - d$ zeros. See:Sum-Largest for a discussion of this result.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Fact 1.1", "weight": 1.0} -->

Fact 1.1 gives a geometric indication about why reaper might be effective. Suppose there is a rank-$d$ orthoprojector $\mathbf{\Pi}_{L}$ that provides a good linear model for the inliers. The constraint set in (1.4) is the convex hull of the rank-$d$ orthoprojectors. In high dimensions, convex hulls tend to be very small, so there are relatively few perturbations of $\mathbf{\Pi}_{L}$ that remain feasible for (1.4). At the same time, the objective function in (1.4) is a sort of $\ell_{1}$ norm, so it has relatively few directions of descent at $\mathbf{\Pi}_{L}$. We have the intuition that it is impossible to move far from $\mathbf{\Pi}_{L}$ into the constraint set while simultaneously reducing the objective function. This insight is ultimately the basis for our analysis.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Computing an Orthoprojector from the Solution of reaper", "weight": 1.0} -->

It is easy to see that a solution ${\mathbf{P}}_{\star}$ to the reaper problem has rank $d$ or greater. On the other hand, the matrix ${\mathbf{P}}_{\star}$ does need not to be an orthoprojector, so it is not immediately clear how to obtain a $d$-dimensional linear model from a minimizer of reaper. To accomplish this goal, let us consider the auxiliary problem

<!-- chunk {"id": "body-0027", "role": "body", "section": "Computing an Orthoprojector from the Solution of reaper", "weight": 1.0} -->

In other words, we find a rank-$d$ orthoprojector $\mathbf{\Pi}_{\star}$ that is closest to ${\mathbf{P}}_{\star}$ in Schatten 1-norm. We use the range of $\mathbf{\Pi}_{\star}$ as our linear model.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Computing an Orthoprojector from the Solution of reaper", "weight": 1.0} -->

It is straightforward to compute a solution $\mathbf{\Pi}_{\star}$ to the problem (1.5). We just need to construct an orthogonal projector whose range is a dominant $d$-dimensional invariant subspace of ${\mathbf{P}}_{\star}$. More precisely, we form the spectral factorization ${\mathbf{P}}_{\star} = {{\mathbf{U}}\mathbf{\Lambda}{\mathbf{U}}^{\mathsf{t}}}$ where the entries of the diagonal matrix $\mathbf{\Lambda}$ are listed in weakly decreasing order. Extract the $D \times d$ matrix ${\mathbf{U}}_{d}$ consisting of the first $d$ columns of $\mathbf{U}$. Then an optimal point for (1.5) is given by the formula $\mathbf{\Pi}_{\star} = {{\mathbf{U}}_{d}{}_{}^{}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Computing an Orthoprojector from the Solution of reaper", "weight": 1.0} -->

(This well-known recipe for solving (1.5) can be verified using a straightforward modification of the argument leading to (:Matrix-Analysis Thm. IX.7.2).)

<!-- chunk {"id": "body-0030", "role": "body", "section": "Computing an Orthoprojector from the Solution of reaper", "weight": 1.0} -->

The range of the matrix $\mathbf{\Pi}_{\star}$ often provides a very good fit for the inlying data points, even when there are many outliers. This paper provides theoretical and empirical support for this claim. In Section 4, we present a numerical algorithm for solving (1.4) efficiently. Section 5.1 outlines some practical issues that are important in applications.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

This work partakes in a larger research vision: Given a difficult nonconvex optimization problem, it is often more effective to solve a convex variant than to accept a local minimizer of the original problem.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

We believe that the main point of interest is our application of convex optimization to solve a problem involving subspaces. There are two key observations here. We parameterize subspaces by orthoprojectors, and then we replace the set of rank-$d$ orthoprojectors with its convex hull. This relaxation has a different character from previous approaches to robust linear modeling, so we have found it necessary to develop a new type of analysis to obtain theoretical results for reaper.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

We have also done some numerical work which indicates that reaper can be more effective than its competitors for certain types of robust linear modeling. After the original version:Robust-Computation of this manuscript appeared, our ideas have been applied to a difficult class of problems involving orthogonality constraints, and this approach sometimes outperforms its competitors:Exact-Stable. Together, these papers suggest that relaxations like reaper can be used to address important geometric questions in data analysis.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Roadmap", "weight": 1.0} -->

We close this introduction with an outline of the paper. In Section 2, we develop a deterministic analysis of reaper that describes when it can recover a linear model from a noisy dataset that includes outliers. Section 3 instantiates this result for a simple random data model. In Section 4, we develop an efficient numerical method for solving the reaper problem. Then we describe a numerical example involving an image database in Section 5. We discuss related work in Section 6. The technical details that support our work appear in the appendices.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Theoretical Analysis of the reaper Problem", "weight": 1.0} -->

The goal of this section is to provide theoretical evidence that the reaper problem (1.4) is an effective way to find a robust linear model for a dataset. To do so, we consider a very general deterministic setup where the data consists of inliers that are located near a fixed subspace and outliers that may appear anywhere in the ambient space. We then introduce summary statistics for the data that encapsulate some of its geometric properties. Using these statistics, we state our main result, Theorem 2.1. ‣ 2.3 Performance of reaper with Deterministic Data ‣ 2 Theoretical Analysis of the reaper Problem ‣ Robust computation of linear models by convex relaxationCommunicated by Emmanuel Candès"), which gives a bound on how well reaper is able to approximate the model subspace. This result indicates why reaper may be more effective than PCA for very noisy data. At the end of the section, we summarize the main ideas in the proof of Theorem 2.1. ‣ 2.3 Performance of reaper with Deterministic Data ‣ 2 Theoretical Analysis of the reaper Problem ‣ Robust computation of linear models by convex relaxationCommunicated by Emmanuel Candès"), leaving the remaining details until Appendix A.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Deterministic Data Model", "weight": 1.0} -->

To analyze the performance of the reaper method, we need to introduce a model for the input data. It is natural to consider the case where the dataset contains inliers that lie on or near a fixed low-dimensional subspace, while the outliers can be arrayed arbitrarily in the ambient space. We formalize this intuition in a set of assumptions that we refer to as the In & Out Model, and we direct the reader to Table 2.1 for a detailed list of the parameters.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Deterministic Data Model", "weight": 1.0} -->

Dataset of Nin inliers, located “near” the subspace L

<!-- chunk {"id": "body-0038", "role": "body", "section": "Deterministic Data Model", "weight": 1.0} -->

Dataset of Nout outliers, at arbitrary locations in ℝD ∖ L

<!-- chunk {"id": "body-0039", "role": "body", "section": "Deterministic Data Model", "weight": 1.0} -->

Dataset 𝒳in ∪ 𝒳out containing all the observations

<!-- chunk {"id": "body-0040", "role": "body", "section": "Deterministic Data Model", "weight": 1.0} -->

D × Nout matrix whose columns are the outliers

<!-- chunk {"id": "body-0041", "role": "body", "section": "Deterministic Data Model", "weight": 1.0} -->

Table 2.1: The In &amp; Out Model. A deterministic model for data with linear structure that is contaminated with outliers.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Deterministic Data Model", "weight": 1.0} -->

The key point about the In & Out Model is that all the inliers are located near a subspace $L$, so it is reasonable for us to investigate when an algorithm can approximate this target subspace $L$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Summary Parameters for the In & Out Model", "weight": 1.0} -->

The In & Out Model is very general, so we cannot hope to approximate the target subspace $L$ without making further assumptions on the data. In this section, we develop some geometric summary statistics that allow us to check when reaper is effective at finding the subspace $L$. Heuristically, we need the inliers to provide a significant amount of evidence for the subspace, while the outliers cannot exhibit too much linear structure. Otherwise, an unsupervised algorithm would be justified in finding a subspace that describes the outliers instead of the inliers!

<!-- chunk {"id": "body-0044", "role": "body", "section": "Summary Parameters for the In & Out Model", "weight": 1.0} -->

Let us begin with a discussion of what it means for the inliers to provide evidence for a specific subspace $M \subset {\mathbb{R}}^{D}$. Imagine that we approximate each inlier $\mathbf{x}$ with the point $\mathbf{\Pi}_{M}{\mathbf{x}}$ in the subspace $M$. These approximations must have two properties. First, we want the approximations of the inliers to corroborate all the directions in the subspace $M$. Second, we need to be sure that the residual error in the approximations is not too large. Our first two summary statistics are designed to address these requirements.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Summary Parameters for the In & Out Model", "weight": 1.0} -->

To quantify how well the inliers fill out a subspace $M \subset {\mathbb{R}}^{D}$, we introduce the *permeance statistic* $\mathcal{P}{(M)}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Summary Parameters for the In & Out Model", "weight": 1.0} -->

If there is a direction in the subspace $M$ that is orthogonal to each inlier, then the permeance statistic $\mathcal{P}{(M)}$ is zero. On the other hand, the permeance statistic is large when every direction $\mathbf{u}$ in $M$ has the property that many inliers have a component along $\mathbf{u}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Summary Parameters for the In & Out Model", "weight": 1.0} -->

Second, we introduce the *total inlier residual* $\mathcal{R}{(M)}$ to measure the total error that we incur by approximating the data using the subspace $M$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Summary Parameters for the In & Out Model", "weight": 1.0} -->

Let us emphasize that the total inlier residual is less sensitive to large errors than the sum of squared residuals that drives the PCA method.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Summary Parameters for the In & Out Model", "weight": 1.0} -->

Next, let us turn to the condition that we require of the outliers. A major challenge for any robust linear modeling procedure is the possibility that both the inliers and the outliers exhibit linear structure. In this case, an algorithm may choose to fit a linear model to the outliers if they have a stronger signature.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Summary Parameters for the In & Out Model", "weight": 1.0} -->

To measure the amount of linear structure in the outliers, we introduce the *alignment statistic* $\mathcal{A}{(M)}$ with respect to a target subspace $M$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Summary Parameters for the In & Out Model", "weight": 1.0} -->

where ${\mathbf{X}}_{out}$ is the matrix whose columns are the outlying data points and the spherization operator $\overset{\sim}{}$ normalizes the columns of a matrix. It is somewhat harder to understand what the alignment statistic $\mathcal{A}{(M)}$ reflects. First, observe that the spectral norm $\left\| {\mathbf{X}}_{out} \right\|$ tends to be large when the outliers are collinear, and it is small when the outliers are weakly correlated. The other term in the alignment statistic asks about the collinearity of the outliers after we have removed their components in the subspace $M$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Summary Parameters for the In & Out Model", "weight": 1.0} -->

Finally, we present one more statistic that weighs the influence of the inliers against the influence of the outliers. The *stability statistic* $\mathcal{S}{(M)}$ of the data with respect to a subspace $M \subset {\mathbb{R}}^{D}$ is the quantity

<!-- chunk {"id": "body-0053", "role": "body", "section": "Summary Parameters for the In & Out Model", "weight": 1.0} -->

The stability statistic tends to be large when the inliers provide a lot of evidence for the subspace $M$ and the outliers contain relatively little distracting linear structure. As we will see, when $\mathcal{S}{(M)}$ is large, the reaper method can be very effective at approximating the subspace $M$, even when the inliers are noisy.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Performance of reaper with Deterministic Data", "weight": 1.0} -->

The main theoretical result in this paper describes the behavior of the reaper method when it is applied to data that meet the assumptions of the In & Out Model from Table 2.1.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Theoretical Example: The Haystack Model", "weight": 1.0} -->

The In & Out Model is very general, so Theorem 2.1. ‣ 2.3 Performance of reaper with Deterministic Data ‣ 2 Theoretical Analysis of the reaper Problem ‣ Robust computation of linear models by convex relaxationCommunicated by Emmanuel Candès") applies to a wide variety of specific examples. To see the kind of results that are possible, let us apply Theorem 2.1. ‣ 2.3 Performance of reaper with Deterministic Data ‣ 2 Theoretical Analysis of the reaper Problem ‣ Robust computation of linear models by convex relaxationCommunicated by Emmanuel Candès") to study the behavior of reaper for data drawn from a simple random model. We use standard tools from high-dimensional probability to compute the values of the summary statistics.

<!-- chunk {"id": "body-0056", "role": "body", "section": "The Haystack Model", "weight": 1.0} -->

Let us consider a simple generative random model for a dataset. We call this the Haystack Model, and we refer the reader to Table 3.1 for a list of the assumptions and the parameters. The Haystack Model is not intended as a realistic description of data. Instead, the goal is to capture the idea that inliers admit a low-dimensional linear model, while the outliers are totally unstructured.

<!-- chunk {"id": "body-0057", "role": "body", "section": "The Haystack Model", "weight": 1.0} -->

D Dimension of the ambient space L A proper d-dimensional subspace of ℝD containing the inliers Nin Number of inliers Nout Number of outliers ρin Inlier sampling ratio ρin:= Nin/d ρout Outlier sampling ratio ρout:= Nout/D σin2 Variance of the inliers per subspace dimension σout2 Variance of the outliers per ambient dimension
𝒳in Set of Nin inliers, drawn i.i.d. normal (0,(σin2/d) ΠL) 𝒳out Set of Nout outliers, drawn i.i.d. normal (0,(σout2/D) ID) 𝒳 The set 𝒳in ∪ 𝒳out containing all the data points
Table 3.1: The Haystack Model. A generative random model for data with linear structure that is contaminated with outliers. The abbreviation i.i.d. stands for independent and identically distributed.

<!-- chunk {"id": "body-0058", "role": "body", "section": "The Haystack Model", "weight": 1.0} -->

There are a few useful intuitions associated with this model. As the inlier sampling ratio $\rho_{in}$ increases, the inliers fill out the subspace $L$ more completely so the linear structure becomes more evident. As the outlier sampling ratio $\rho_{out}$ increases, the outliers become more distracting and they may even start to exhibit some linear structure due to chance.

<!-- chunk {"id": "body-0059", "role": "body", "section": "The Haystack Model", "weight": 1.0} -->

As a result, when $\sigma_{in}^{2} = \sigma_{out}^{2}$, we cannot screen outliers just by looking at their energy. The sampling ratios and the variances contain most of the information about the behavior of this model.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Analysis of the Haystack Model", "weight": 1.0} -->

Using methods from high-dimensional probability, we can analyze the stability statistic $\mathcal{S}{(L)}$ for a dataset drawn at random from the Haystack Model.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Numerical experiment", "weight": 1.0} -->

We find ${\mathbf{P}}_{\star}$ by solving reaper (1.4) with the algorithm described in Section 4 below, and then determine the orthoprojector $\mathbf{\Pi}_{\star}$ using (1.5). We assess whether this procedure identifies the true subspace $\mathbf{\Pi}_{L}$ subspace by declaring the experiment a success when the error $\left\| {{\mathbf{P}}_{\star} - \mathbf{\Pi}_{L}} \right\|_{S_{1}} < 10^{- 5}$. For each pair $(\rho_{in},\rho_{out})$, we repeat the experiment 25 times and calculate an empirical success probability. For each value of $\rho_{in}$, we find the $50\%$ empirical success $\rho_{out}$ using a logistic fit. We fit a line to these points using standard least-squares.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Numerical experiment", "weight": 1.0} -->

These results indicate that the linear trend suggested by the theoretical bound (3.1) reflects the empirical behavior of reaper.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Noisy inliers", "weight": 1.0} -->

To understand how reaper behaves when the inlying set $\mathcal{X}_{in}$ does not lie precisely within the target subspace, we introduce the *Noisy* Haystack Model. This model expands the standard Haystack Model from Table 3.1 with the additional parameter $\sigma_{noise}^{2}$ that controls the amount of noise present in the inliers. In this extended model, the inlying data $\mathcal{X}_{in}$ is given by

<!-- chunk {"id": "body-0064", "role": "body", "section": "Noisy inliers", "weight": 1.0} -->

All other parameters and data agree with the Haystack Model of Table 3.1.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Noisy inliers", "weight": 1.0} -->

The definition (3.2) of the inlying data ensures that the stability statistic $\mathcal{S}{(L)}$ has the same distribution under the Noisy Haystack Model as under the plain Haystack Model. In particular, the relationship (3.1) holds under the Noisy Haystack Model. On the other hand, the inlier residual statistic $\mathcal{R}{(L)}$ (2.2) is not equal to zero under the noisy model, but rather satisfies

<!-- chunk {"id": "body-0066", "role": "body", "section": "Noisy inliers", "weight": 1.0} -->

where ${\mathbf{g}}_{i} \sim {\text{normal}\left( \mathbf{0},{{({\sigma_{noise}^{2}/{({D - d})}})}\mathbf{\Pi}_{L^{\perp}}} \right)}$. The inequality is Jensen's, and the last expression uses the fact that the squared norm of a Gaussian random variable on the $({D - d})$-dimensional subspace is $D - d$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Noisy inliers", "weight": 1.0} -->

A basic concentration result indicates that the residual statistic will not exceed its mean by more than a factor of, say, two with overwhelming probability. (This claim is easily made precise using the result (Bogachev1998 Thm. 1.7.6).) Combining this observation with (3.1) and Theorem 2.1. ‣ 2.3 Performance of reaper with Deterministic Data ‣ 2 Theoretical Analysis of the reaper Problem ‣ Robust computation of linear models by convex relaxationCommunicated by Emmanuel Candès"), we see that with high probability

<!-- chunk {"id": "body-0068", "role": "body", "section": "Noisy inliers", "weight": 1.0} -->

where we define the signal-to-noise ratio ${SNR}:={\sigma_{in}/\sigma_{noise}}$. This inequality suggests that reaper is stable under the Noisy Haystack Model in the regime where the stability statistic ${\mathcal{S}{(L)}} = {O{}}$ and the signal-to-noise ratio ${SNR} = {O{(N_{in}^{- 1})}}$. Our numerical experience suggests that this SNR restriction is conservative.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Numerical experiment", "weight": 1.0} -->

The heat map in Figure 3.2 shows the mean error $\left\| {\mathbf{\Pi}_{\star} - \mathbf{\Pi}_{L}} \right\|_{S_{1}}$ over these trials for both reaper and PCA. The blue region of the heat map begins where the error is less than $10\%$ of the maximum possible error

<!-- chunk {"id": "body-0070", "role": "body", "section": "Numerical experiment", "weight": 1.0} -->

We see that reaper is in the blue region over more of the parameter regime than PCA, which indicates that reaper is more stable than PCA under the Noisy Haystack Model.

<!-- chunk {"id": "body-0071", "role": "body", "section": "An Iterative Reweighted Least-Squares Algorithm for reaper", "weight": 1.0} -->

Theorem 2.1. ‣ 2.3 Performance of reaper with Deterministic Data ‣ 2 Theoretical Analysis of the reaper Problem ‣ Robust computation of linear models by convex relaxationCommunicated by Emmanuel Candès") suggests that the reaper problem (1.4) can be a valuable tool for robust linear modeling. On the other hand, reaper is a semidefinite program, so it may be prohibitively expensive to solve using the standard interior-point methods. If we intend reaper to be a viable approach for data analysis problems, it is incumbent that we produce a numerical method with more favorable scaling properties.

<!-- chunk {"id": "body-0072", "role": "body", "section": "An Iterative Reweighted Least-Squares Algorithm for reaper", "weight": 1.0} -->

In this section, we describe a numerical algorithm for solving the reaper problem (1.4). Our approach is based on the iterative reweighted least squares (IRLS) framework (:Numerical-Methods Sec. 4.5.2). At each step of the algorithm, we solve a weighted least-squares problem whose weights evolve as the algorithm proceeds. This subproblem admits a closed-form solution that we can obtain from a single SVD of the (weighted) data. The IRLS method exhibits linear convergence in practice, so it can achieve high accuracy without a substantial number of iterations.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

IRLS is based on the idea that we can solve many types of weighted least-squares problems efficiently. Therefore, instead of solving the reaper problem (1.4) directly, we replace it with a sequence of weighted least-squares problems.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

and so it seems plausible that the minimizer of the following quadratic program is close to ${\mathbf{P}}_{\star}$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

We can efficiently solve problem (4.1) by performing a spectral computation and a water-filling step that ensures $\mathbf{0} \preccurlyeq {\mathbf{P}} \preccurlyeq \mathbf{I}$. The water-filling step differentiates the new algorithm from the earlier work:Novel-M-Estimator. The details appear in a box labeled Algorithm 4.1, and a proof of correctness appears in Appendix C.1.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

A nonnegative weight βx for each x ∈ 𝒳
The dimension parameter d in (4.1), where d ∈ {1,2,…,D − 1}

<!-- chunk {"id": "body-0077", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

Form the D × D weighted covariance matrix

<!-- chunk {"id": "body-0078", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

Compute an eigenvalue decomposition C = U ⋅ diag(λ1,…,λD) ⋅ Ut with eigenvalues in nonincreasing order: λ1 ≥ ⋯ ≥ λD ≥ 0

<!-- chunk {"id": "body-0079", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

Algorithm 4.1 Solving the weighted least-squares problem (4.1)

<!-- chunk {"id": "body-0080", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

The heuristic above motivates an iterative procedure for solving (1.4). Let $\delta$ be a (small) positive regularization parameter. Initialize the iteration counter $k\leftarrow 0$ and the weights $\beta_{\mathbf{x}}\leftarrow 1$ for each ${\mathbf{x}} \in \mathcal{X}$. We solve (4.1) with the weights $\beta_{\mathbf{x}}$ to obtain a matrix ${\mathbf{P}}^{(k)}$, and then we update the weights according to the formula

<!-- chunk {"id": "body-0081", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

In other words, we emphasize the observations that are explained well by the current model. The presence of the regularization parameter $\delta$ ensures that no single point can gain undue influence. We increment $k$, and we repeat the process until it has converged. See the box labeled Algorithm 4.2 for the details.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

The following result shows that Algorithm 4.2 is guaranteed to converge to a point whose value is close to the optimal value of the reaper problem (1.4).

<!-- chunk {"id": "body-0083", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

A D × D matrix P⋆ that satisfies 0 ≼ P⋆ ≼ I and trP⋆ = d

<!-- chunk {"id": "body-0084", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

Set the iteration counter k ← 0
Set the initial error α ← +∞
Set the weight βx ← 1 for each x ∈ 𝒳

<!-- chunk {"id": "body-0085", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

Use Algorithm 4.1 to compute an optimal point P(k) of (4.1) with weights βx
Let α(k) be the optimal value of (4.1)

<!-- chunk {"id": "body-0086", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

until the objective fails to decrease: α(k) ≥ α(k−1) − ε

<!-- chunk {"id": "body-0087", "role": "body", "section": "Solving reaper via IRLS", "weight": 1.0} -->

Algorithm 4.2 IRLS algorithm for solving the reaper problem (1.4)

<!-- chunk {"id": "body-0088", "role": "body", "section": "Computational Costs for Algorithm 4.2", "weight": 1.0} -->

Let us take a moment to summarize the computational costs for the IRLS method, Algorithm 4.2. When reading through this discussion, keep in mind that linear modeling problems typically involve datasets where the number $N$ of data points is somewhat larger than the ambient dimension $D$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Computational Costs for Algorithm 4.2", "weight": 1.0} -->

The bulk of the computation in Algorithm 4.2 occurs when we solve the subproblem in Step 2b using the weighted-least squared method from Algorithm 4.1. The bulk of the computation in Algorithm 4.1 takes place during the spectral calculation in Steps 1 and 2. In general, we need $\mathcal{O}{({ND^{2}})}$ arithmetic operations to form the weighted covariance matrix, and the spectral calculation requires $\mathcal{O}{(D^{3})}$. The remaining steps of both algorithms have lower order.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Computational Costs for Algorithm 4.2", "weight": 1.0} -->

In summary, each iteration of Algorithm 4.2 requires $\mathcal{O}{({ND^{2}})}$ arithmetic operations. The algorithm converges linearly in practice, so we need $\mathcal{O}{({\log{({1/\eta})}})}$ iterations to achieve an error of $\eta$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Computational Costs for Algorithm 4.2", "weight": 1.0} -->

In the statement of Algorithm 4.1, we have presented the weighted least-squared calculation in the most direct way possible. In practice, it is usually more efficient to form a $D \times N$ matrix $\mathbf{W}$ with columns $\sqrt{\beta_{\mathbf{x}}}{\mathbf{x}}$ for ${\mathbf{x}} \in \mathcal{X}$, to compute a thin SVD ${\mathbf{W}} = {{\mathbf{U}}\mathbf{\Sigma}{\mathbf{V}}^{\mathsf{t}}}$, and to set $\mathbf{\Lambda} = \mathbf{\Sigma}^{2}$. This approach is also more stable. In some situations, such as when $\mathbf{C}$ can be guaranteed to be low rank at each iteration, it is possible to accelerate the spectral calculations using randomized dimension reduction as:Finding-Structure.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Empirical Convergence Rate of Algorithm 4.2", "weight": 1.0} -->

Many algorithms based on IRLS exhibit linear convergence:Convergence-Lagged. Under some additional assumptions, we can prove that Algorithm 4.2 generates a sequence $\{{\mathbf{P}}^{(k)}\}$ of iterates that converges linearly to an optimal point ${\mathbf{P}}_{\star}$ of reaper. This argument has a small quotient of novelty relative to the amount of technical maneuver required, so we have chosen to omit the details. Our analysis does not provide a realistic estimate for the rate of convergence, so we have undertaken some numerical investigations to obtain more insight.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Empirical Convergence Rate of Algorithm 4.2", "weight": 1.0} -->

For synthetic data, the number of iterations required for Algorithm 4.2 seems to depend on the difficulty of the problem instance. Indeed, it may take as many as 200 iterations for the method to converge on challenging examples. In experiments with natural data, we usually obtain good performance after 20 iterations or so. In practice, Algorithm 4.2 is also much faster than algorithms:Robust-PCA;:Two-Proposals for solving the low-leverage decomposition problem (6.2).

<!-- chunk {"id": "body-0094", "role": "body", "section": "Empirical Convergence Rate of Algorithm 4.2", "weight": 1.0} -->

The stopping criterion in Algorithm 4.2 is motivated by the fact that the objective value must decrease in each iteration. This result is a consequence of the proof of Theorem 4.1. ‣ 4.1 Solving reaper via IRLS ‣ 4 An Iterative Reweighted Least-Squares Algorithm for reaper ‣ Robust computation of linear models by convex relaxationCommunicated by Emmanuel Candès"); see (C.7). Taking $\varepsilon$ on the order of machine precision ensures that the algorithm terminates when the iterates are dominated by numerical errors. In practice, we achieve very precise results when $\varepsilon = 10^{- 15}$ or even $\varepsilon = 0$. In many applications, this degree of care is excessive, and we can obtain a reasonable solution for much larger values of $\varepsilon$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Numerical Example: reaper Applied to an Image Database", "weight": 1.0} -->

In this section, we present a numerical experiment that describes the performance of reaper for a stylized problem involving natural data.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Some Practical Matters", "weight": 1.0} -->

Although the reaper formulation is effective on its own, we can usually obtain better linear models if we preprocess the data before solving (1.4). Let us summarize the recommended procedure, which appears as Algorithm 5.1.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Some Practical Matters", "weight": 1.0} -->

The target dimension d for the linear model, where d ∈ {1, 2, …, D − 1}

<!-- chunk {"id": "body-0098", "role": "body", "section": "Some Practical Matters", "weight": 1.0} -->

(Optional.) Solve (5.1) to obtain a center c⋆, and center the data: x ← x − c⋆ for each x ∈ 𝒳
(Optional.) Spherize the data: x ← x/∥x∥ for each nonzero x ∈ 𝒳
Solve the reaper problem (1.4) with dataset 𝒳 and parameter d to obtain an optimal point P⋆
Solve (1.5) by finding a dominant d-dimensional invariant subspace of P⋆

<!-- chunk {"id": "body-0099", "role": "body", "section": "Some Practical Matters", "weight": 1.0} -->

Algorithm 5.1 Prototype algorithm for robust computation of a linear model

<!-- chunk {"id": "body-0100", "role": "body", "section": "Some Practical Matters", "weight": 1.0} -->

First, the reaper problem assumes that the inliers are approximately centered. When they are not, it is important to identify a centering point ${\mathbf{c}}_{\star}$ for the dataset and to work with the centered observations.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Some Practical Matters", "weight": 1.0} -->

It is also possible to incorporate centering by modifying the optimization problem (1.4). For brevity, we omit the details.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Some Practical Matters", "weight": 1.0} -->

Second, the reaper formulation can be sensitive to outliers with large magnitude. A simple but powerful method for addressing this challenge is to spherize the data points before solving the optimization problem. For future reference, we write down the resulting convex program.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Some Practical Matters", "weight": 1.0} -->

The tilde denotes the spherization transform (1.1). We refer to (5.2) as the s-reaper problem. In most (but not all) of our experimental work, we have found that s-reaper outperforms reaper. The idea of spherizing data before fitting a subspace was proposed in the paper LMS+99:Robust-Principal, where it is called *spherical PCA*.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Some Practical Matters", "weight": 1.0} -->

Finally, we regard the parameter $d$ in reaper and s-reaper as a proxy for the dimension of the linear model. While the rank of an optimal solution ${\mathbf{P}}_{\star}$ to (1.4) or (5.2) cannot be smaller than $d$ because of the constraints ${{tr}{\mathbf{P}}} = d$ and ${\mathbf{P}} \preccurlyeq \mathbf{I}$, the rank of ${\mathbf{P}}_{\star}$ often exceeds $d$. We recommend solving (1.5) to find a closest projector to ${\mathbf{P}}_{\star}$.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

To solve the reaper problem (1.4) and the s-reaper problem (5.2), we use the IRLS method, Algorithm 4.2. We set the regularization parameter $\delta = 10^{- 10}$ and the stopping tolerance $\varepsilon = 10^{- 15}$. We postprocess the computed optimal point ${\mathbf{P}}_{\star}$ of reaper or s-reaper to obtain a $d$-dimensional linear model by solving (1.5).

<!-- chunk {"id": "body-0106", "role": "body", "section": "Comparisons", "weight": 1.0} -->

By now, there are a huge number of proposals for robust linear modeling, so we have limited our attention to methods that are computationally tractable. That is, we consider only formulations that have a polynomial-time algorithm for constructing a global solution (up to some tolerance). We do not discuss techniques that involve Monte Carlo simulation, nonlinear programming, etc. because the success of these approaches depends largely on parameter settings and providence. As a consequence, it is hard to evaluate their behavior in a consistent way.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Comparisons", "weight": 1.0} -->

We consider two standard approaches, PCA:Principal-Component and spherical PCA LMS+99:Robust-Principal. Spherical PCA rescales each observation so it lies on the Euclidean sphere, and then it applies standard PCA. Simulations performed with several different robust PCA methods in Maronna2005 lead Maronna et al.:Robust-Statistics to recommend spherical PCA as a reliable classical robust PCA algorithm.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Comparisons", "weight": 1.0} -->

We also consider a more recent proposal:Robust-PCA-NIPS;:Robust-PCA;:Two-Proposals, which is called *low-leverage decomposition* (LLD) or *outlier pursuit*. This method decomposes the $D \times N$ matrix $\mathbf{X}$ of observations by solving the optimization problem

<!-- chunk {"id": "body-0109", "role": "body", "section": "Comparisons", "weight": 1.0} -->

where $\left. \parallel \cdot \parallel{}_{S_{1}} \right.$ is the Schatten 1-norm and $\left. \parallel \cdot \parallel_{1\rightarrow 2}^{\ast} \right.$ returns the sum of Euclidean norms of the column. The idea is that the optimizer $({\mathbf{P}}_{\star},{\mathbf{C}}_{\star})$ will consist of a low-rank model ${\mathbf{P}}_{\star}$ for the data along with a column-sparse matrix ${\mathbf{C}}_{\star}$ that identifies the outliers. We always use the parameter choice $\gamma = {0.8\sqrt{D/N}}$, which seems to be effective in practice.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Comparisons", "weight": 1.0} -->

We do not make comparisons with the rank--sparsity decomposition:Rank-Sparsity, which has also been considered for robust linear modeling:Robust-Principal. It is not effective for the problem that we consider here.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Faces in a Crowd", "weight": 1.0} -->

This experiment is designed to test how well several robust methods are able to fit a linear model to face images that are dispersed in a collection of random images. Our setup allows us to study how well the robust model generalizes to faces we have not seen.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Faces in a Crowd", "weight": 1.0} -->

We pull 64 images of a single face under different illuminations from the Extended Yale Face Database B:Acquiring-Linear. We use the first 32 faces for the sample, and we reserve the other 32 for the out-of-sample test. Next, we add all 467 images from the BACKGROUND/Google folder of the Caltech101 database CIT101; Fei-Fei2004. The Caltech101 images are converted to grayscale and downsampled to $192 \times 168$ pixels to match the native resolution of the Yale face images. We center the images by subtracting the Euclidean median (5.1). Then we apply PCA, spherical PCA, LLD, reaper, and s-reaper to fit a nine-dimensional subspace to the data. See:Lambertian-Reflectance for justification of the choice $d = 9$. This experiment is similar to work reported in (LLY+10:Robust-Recovery Sec. VI).

<!-- chunk {"id": "body-0113", "role": "body", "section": "Classical Strategies for Robust Linear Modeling", "weight": 1.0} -->

We begin with an overview of the major techniques that have been proposed in the statistics literature. The theoretical contributions in this area focus on breakdown points and influence functions of estimators. Researchers tend to devote less attention to the computational challenges inherent in these formulations. Moreover, the notion of the breakdown point for quantifying the robustness of estimators for vectors and matrices does not generalize to subspace estimation. We recall that, roughly speaking, the breakdown point measures the proportion of arbitrarily placed outliers an estimator can handle before giving an arbitrarily bad result. However, this idea does not directly extend to subspaces since the set of subspaces is compact. Following instead:Robust-Principal;:Robust-PCA, we quantify robustness of subspace estimation via exact recovery and stability to noise.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Robust Combination of Residuals", "weight": 1.0} -->

Historically, one of the earliest approaches to linear regression is to minimize the sum of (nonorthogonal) residuals. This is the principle of *least absolute deviations* (LAD). Early proponents of this idea include Galileo, Boscovich, Laplace, and Edgeworth. See:Method-Least-I;:Method-Least-II;:Introduction-L1-Norm for some historical discussion. It appears that *orthogonal* regression with LAD was first considered in the late 1980s:Analysis-Total;:Orthogonal-Linear;:Least-Orthogonal; the extension from orthogonal regression to PCA seems to be even more recent:Some-Problems;:R1-PCA. LAD has also been considered as a method for hybrid linear modeling:Median-k-Flats;:Robust-Recovery. We are not aware of a tractable algorithm for these formulations.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Robust Combination of Residuals", "weight": 1.0} -->

There are many other robust methods for combining residuals aside from LAD. An approach that has received wide attention is to minimize the median of the squared residuals:Least-Median;:Robust-Regression. Other methods appear in the books:Robust-Statistics;:Robust-Statistics. These formulations are generally not computationally tractable.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Robust Estimation of Covariance Matrix", "weight": 1.0} -->

Another standard technique for robust PCA is to form a robust estimate of the covariance matrix of the data:Robust-M-Estimators;:Robust-Statistics;:Robust-Statistics;:Robust-Estimation;:Asymptotic-Behavior;:Robust-Principal;:Principal-Component. The classical approaches to robust estimates of covariance are based on maximum likelihood principles that lead to M-estimators. Most often, IRLS algorithms are used to compute these M-estimators of covariance.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Robust Estimation of Covariance Matrix", "weight": 1.0} -->

There are some formal similarities between the minimization program (1.4) and the formulation of classical M-estimators. In particular, the computational complexity of these estimators scales comparably with our own IRLS algorithm. However, there are also important differences between the classical covariance estimators and the subspace estimation procedure we consider here. In particular, the common M-estimators for robust covariance estimation fail for the exact- and near-subspace recovery problems. See (:Novel-M-Estimator Sec. 3.1) for elaboration on these points.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Robust Estimation of Covariance Matrix", "weight": 1.0} -->

In addition to the basic M-estimators computed with IRLS, there are many other covariance estimators, including S-estimators, the minimum covariance determinant (MCD), the minimum volume ellipsoid (MVE), and the Stahel--Donoho estimator. We are not aware of any scalable algorithm with guarantees of correctness for implementing these latter estimators. See (:Robust-Statistics Sec. 6) for a review.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Projection Pursuit PCA", "weight": 1.0} -->

Projection pursuit (often abbreviated PP-PCA) is a procedure that constructs principal components one at a time by finding a direction that maximizes a robust measure of scale, removing the component of the data in this direction, and repeating the process. The initial proposal appears in (:Robust-Statistics 1st edn.), and it has been explored by many other authors:Projection-Pursuit;:Robust-Singular;:Algorithms-Projection;:Principal-Component;:Penalized-Matrix. We are aware of only one formulation that provably (approximately) maximizes a robust measure of scale at each iteration:Two-Proposals, but there are no overall guarantees for PP-PCA algorithms.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Screening for Outliers", "weight": 1.0} -->

Another common approach is to remove possible outliers and then estimate the underlying subspace by PCA:Residuals-Influence;:Robust-Principal;:Framework-Robust. The classical methods offer very limited guarantees. There are some recent algorithms that are provably correct:Robust-PCA;:Principal-Component under some model assumptions and with particular correctness criteria that are tailored to the individual algorithm.

<!-- chunk {"id": "body-0121", "role": "body", "section": "RANSAC", "weight": 1.0} -->

The randomized sample consensus (RANSAC) method is a randomized iterative procedure for fitting models to noisy data consisting of inliers and outliers:Random-Sample. Under some assumptions, RANSAC will eventually identify a linear model for the inliers, but there are no guarantees on the number of iterations required.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Spherical PCA", "weight": 1.0} -->

A useful method for fitting a robust linear model is to center the data robustly, project it onto a sphere, and then apply standard PCA. This approach is due to LMS+99:Robust-Principal. Maronna et al.:Robust-Statistics recommend it as a preferred method for robust PCA. The technique is computationally practical, but it has limited theoretical guarantees.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Approaches Based on Convex Optimization", "weight": 1.0} -->

Recently, researchers have started to develop effective techniques for robust linear modeling that are based on convex optimization. These formulations invite a variety of tractable algorithms, and they have theoretical guarantees under appropriate model assumptions.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Demixing Methods", "weight": 1.0} -->

One class of techniques for robust linear modeling is based on splitting a data matrix into a low-rank model plus a corruption. The first approach of this form is due to Chandrasekaran et al.:Rank-Sparsity. Given an observed matrix $\mathbf{X}$, they solve the semidefinite problem

<!-- chunk {"id": "body-0125", "role": "body", "section": "Demixing Methods", "weight": 1.0} -->

Minimizing the Schatten 1-norm $\left. \parallel \cdot \parallel{}_{S_{1}} \right.$ promotes low rank, while minimizing the vector $\ell_{1}$ norm promotes sparsity. The regularization parameter $\gamma$ negotiates a tradeoff between the two goals. Candès et al.:Robust-Principal study the performance of (6.1) for robust linear modeling in the setting where individual entries of the matrix $\mathbf{X}$ are subject to error.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Demixing Methods", "weight": 1.0} -->

A related proposal is due to Xu et al.:Robust-PCA-NIPS;:Robust-PCA and independently to McCoy & Tropp:Two-Proposals. These authors recommend solving the decomposition problem

<!-- chunk {"id": "body-0127", "role": "body", "section": "Demixing Methods", "weight": 1.0} -->

The norm $\left. \parallel \cdot \parallel_{1\rightarrow 2}^{\ast} \right.$ returns the sum of Euclidean norms of the columns of its argument. This formulation is appropriate for inlier--outlier data models, where entire columns of the data matrix may be corrupted, in contrast to the formulation (6.1) that is used for corruptions of individual matrix elements.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Demixing Methods", "weight": 1.0} -->

Both (6.1) and (6.2) possess some theoretical guarantees under appropriate model assumptions, but we restrict our discussion to (6.2) because it is tuned to the In & Out Model that we consider here. In the noiseless case, Xu et al.:Robust-PCA show that (6.2) will exactly recover the underlying subspace under the In & Out Model so long as the inlier-to-outlier ratio exceeds a constant times the inlier dimension $d$.^44^4More precisely, the inlier-to-outlier ratio must exceed ${({{121\mu}/9})}d$, where $\mu \geq 1$ depends on the data. For the Haystack Model with $\sigma_{in} = \sigma_{out}$ and $d \ll D$, the lower bound (3.1) is positive when the fraction of inliers exceeds a constant times $d/D$. Hence, Theorem 2.1.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Demixing Methods", "weight": 1.0} -->

‣ 2.3 Performance of reaper with Deterministic Data ‣ 2 Theoretical Analysis of the reaper Problem ‣ Robust computation of linear models by convex relaxationCommunicated by Emmanuel Candès") endows reaper with an exact recovery guarantee that is stronger than the results of:Robust-PCA for (6.2) in the $d \ll D$ regime; a similar statement holds for the stability of reaper. Moreover, the work of Coudron & Lerman:Sample-Complexity-RPCA, which appeared after the submission of this work, provides sample-complexity guarantees for reaper that mirrors that of standard PCA when the data $\mathcal{X}$ is drawn i.i.d. from a subgaussian distribution.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Demixing Methods", "weight": 1.0} -->

The most common algorithmic framework for demixing methods of the form (6.1) and (6.2) uses the alternating direction method of multipliers (ADMM):Distributed-Optimization. These algorithms can converge slowly, so it may take excessive computation to obtain a high-accuracy solution. Indeed, our limited numerical experiments indicate that reaper tends to be significantly faster than the ADMM implementation of:Robust-PCA-NIPS;:Robust-PCA and:Two-Proposals.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Demixing Methods", "weight": 1.0} -->

Nevertheless, the demixing strategy readily adapts to different situations such as missing observations or entrywise corruptions:Robust-PCA;:Robust-Principal, while it is not immediately clear how to adapt the reaper framework to these scenarios.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Precedents for the reaper Problem", "weight": 1.0} -->

The reaper problem (1.4) is a semidefinite relaxation of the $\ell_{1}$ orthogonal distance problem (1.3). Our work extends an earlier relaxation of (1.3)

<!-- chunk {"id": "body-0133", "role": "body", "section": "Precedents for the reaper Problem", "weight": 1.0} -->

where the minimum occurs over symmetric $\mathbf{P}$. Although not obvious, the formulation above is equivalent to reaper with the specific choice $d = {D - 1}$. Indeed, any optimal point ${\mathbf{P}}_{\star}$ of (6.3) satisfies ${\mathbf{I} - {\mathbf{P}}_{\star}} \succcurlyeq \mathbf{0}$ (:Novel-M-Estimator Lem. 14), and this fact, together with the trace constraint ${{tr}{({\mathbf{I} - {\mathbf{P}}_{\star}})}} = 1$, implies that ${\mathbf{I} - {\mathbf{P}}_{\star}} \preccurlyeq \mathbf{I}$.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Precedents for the reaper Problem", "weight": 1.0} -->

Thus, the reaper constraints $\mathbf{0} \preccurlyeq {\mathbf{P}} \preccurlyeq \mathbf{I}$ are implicit in (6.3), and so the observation ${{tr}{(\mathbf{I})}} = D$ yields the claimed equivalence.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Precedents for the reaper Problem", "weight": 1.0} -->

The present work extends the earlier formulation by freeing the parameter $d$ to search for subspaces of a specific dimension, which provides a tighter relaxation for finding $d$-dimensional orthoprojectors. In:Novel-M-Estimator, however, the authors show that the optimal point ${\mathbf{P}}_{\star}$ of (6.3) is more analogous to a robust inverse covariance matrix than to an approximate orthoprojector. This allows the determination of the dimension $d$ using the eigenvalues of ${\mathbf{P}}_{\star}$, while in the present work, we treat $d$ as a known parameter.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Precedents for the reaper Problem", "weight": 1.0} -->

Our analysis of reaper builds on the ideas first presented:lp-Recovery;:Novel-M-Estimator, but it incorporates a number of refinements that simplify and improve the theoretical guarantees. In particular, the present results do not require an oracle condition like (:Novel-M-Estimator Eqs. ), and our stability statistic $\mathcal{S}{(L)}$ supersedes the earlier exact recovery and stability requirements (:Novel-M-Estimator Eqs. & ). The exact recovery guarantees under the Haystack Model are somewhat stronger for reaper than the analogous guarantees for (6.3) (:Novel-M-Estimator Sec. 2.6.1). The IRLS algorithm for reaper and the convergence analysis that we present in Section 4 also extend ideas from the earlier work.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Precedents for the reaper Problem", "weight": 1.0} -->

From a broad perspective, the idea of relaxing a difficult nonconvex program like (1.3) to obtain a convex problem is well established in the literature on combinatorial optimization. Research on linear programming relaxations is summarized:Approximation-Algorithms. Some significant works on semidefinite relaxation include:Cones-Matrices;:Improved-Approximation.
