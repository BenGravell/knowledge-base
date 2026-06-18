Geometric Median in Nearly Linear Time

Topics include Geometric median, Gradient descent, Optimization, Nearly linear time, Computational geometry, Running time.

In this paper we provide faster algorithms for solving the geometric median problem: given n points in R^(d) compute a point that minimizes the sum of Euclidean distances to the points. This is one of the oldest non-trivial problems in computational geometry yet despite an abundance of research the previous fastest algorithms for computing a (1+epsilon)-approximate geometric median were O(d* n^(4/3)epsilon^(-8/3)) by Chin et. al, tildeO(dexp{epsilon^(-4)logepsilon^(-1)}) by Badoiu et. al, O(nd+poly(d, epsilon^(-1)) by Feldman and Langberg, and O((nd)^(O)logfrac1epsilon) by Parrilo and Sturmfels and Xue and Ye. In this paper we show how to compute a (1+epsilon)-approximate geometric median in time O(ndlog^frac1epsilon) and O(depsilon^(-2)). While our O(depsilon^(-2)) is a fairly straightforward application of stochastic subgradient descent, our O(ndlog^frac1epsilon) time algorithm is a novel long step interior point method. To achieve this running time we start with a simple O((nd)^(O)logfrac1epsilon) time interior point method and show how to improve it, ultimately building an algorithm that is quite non-standard from the perspective of interior point literature....

## Introduction

One of the oldest easily-stated nontrivial problems in computational geometry is the Fermat-Weber problem: given a set of $n$ points in $d$ dimensions ${a^{},\ldots,a^{(n)}} \in {\mathbb{R}}^{d}$, find a point $x_{\ast} \in {\mathbb{R}}^{d}$ that minimizes the sum of Euclidean distances to them:

This problem, also known as the *geometric median problem,* is well studied and has numerous applications. It is often considered over low dimensional spaces in the context of the facility location problem and over higher dimensional spaces it has applications to clustering in machine learning and data analysis. For example, computing the geometric median is a subroutine in popular expectation maximization heuristics for $k$-medians clustering.

### Theorem 1

In $O{({nd{\log^{3}{(\frac{n}{\epsilon})}}})}$ time, Algorithm 1 outputs an $({1 + \epsilon})$-approximate geometric median with constant probability.

## Properties of the Central Path

\(3\) Show how to find the bad direction

### Lemma 5 (The Central Path is Almost Straight)

The problem is also important to robust estimation, where we like to find a point representative of given set of points that is resistant to outliers. The geometric median is a rotation and translation invariant estimator that achieves the optimal *breakdown point* of 0.5, i.e. it is a good estimator even when up to half of the input data is arbitrarily corrupted. Moreover, if a large constant fraction of the points lie in a ball of diameter $\epsilon$ then the geometric median lies in that ball with diameter $O{(\epsilon}$) (see Lemma 23)....

Despite the ancient nature of the Fermat-Weber problem and its many uses there are relatively few theoretical guarantees for solving it (see Table 1). To compute a $({1 + \epsilon})$-approximate solution, i.e. $x \in {\mathbb{R}}^{d}$ with ${f{(x)}} \leq {{({1 + \epsilon})}f{(x_{\ast})}}$, the previous fastest running times were either $O{({{d \cdot n^{4/3}}\epsilon^{- {8/3}}})}$ by, $\overset{\sim}{O}{({d{\exp{\epsilon^{- 4}{\log\epsilon^{- 1}}}}})}$ by, $\overset{\sim}{O}\left( {{nd} + {\text{poly}\left( d,\epsilon^{- 1} \right)}} \right)$ by, or $O{({{({nd})}^{O{}}{\log\frac{1}{\epsilon}}})}$ time by....

Our $O{({nd{\log^{3}\frac{n}{\epsilon}}})}$ time algorithm is a careful modification of standard interior point methods for solving the geometric median problem....
