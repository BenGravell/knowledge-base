A Convex Polynomial That Is Not sos-convex

Topics include Convex polynomials, Sos-convexity, Sum of squares, Semidefinite programming, Polynomial optimization, Counterexamples.

Constructs a convex polynomial that is not Sos-convex, separating ordinary convexity from the Sos-verifiable sufficient condition. The counterexample is important for understanding the conservatism of semidefinite relaxations in polynomial optimization.

A multivariate polynomial p(x)=p(x_1,...,x_n) is sos-convex if its Hessian H(x) can be factored as H(x)=M^T(x)M(x) with a possibly nonsquare polynomial matrix M(x). It is easy to see that sos-convexity is a sufficient condition for convexity of p(x). Moreover, the problem of deciding sos-convexity of a polynomial can be cast as the feasibility of a semidefinite program, which can be solved efficiently. Motivated by this computational tractability, it has been recently speculated whether sos-convexity is also a necessary condition for convexity of polynomials. In this paper, we give a negative answer to this question by presenting an explicit example of a trivariate homogeneous polynomial of degree eight that is convex but not sos-convex. Interestingly, our example is found with software using sum of squares programming techniques and the duality theory of semidefinite optimization. As a byproduct of our numerical procedure, we obtain a simple method for searching over a restricted family of nonnegative polynomials that are not sums of squares.

## Introduction

In many problems in applied and computational mathematics, we would like to *decide* whether a multivariate polynomial is convex or to *parameterize* a family of convex polynomials. Perhaps the most obvious instance appears in optimization. It is well known that in the absence of convexity, global minimization of polynomials is generally NP-hard. However, if we somehow know a priori that the polynomial is convex, nonexistence of local minima is guaranteed, and simple gradient descent methods can find a global minimum....

Over a decade ago, Pardalos and Vavasis put the following question proposed by Shor on the list of seven most important open problems in complexity theory for numerical optimization: "Given a degree-$4$ polynomial in $n$ variables, what is the complexity of determining whether this polynomial describes a convex function?" To the best of our knowledge, the question remains open but the general belief is that the problem should be hard (see the related work in ). Not surprisingly, if testing membership to the set of convex polynomials is hard, searching and optimizing over them also turns out to be a hard problem.

### Remark 4.2

Perhaps of independent interest, the methodology explained in this section can be employed to search or optimize over a restricted family of psd polynomials that are not sos using sos-programming. In particular, we can use this technique to simply find more instances of such polynomials. In order to impose a constraint that some polynomial $q{(x)}$ must belong to $P_{n,d}\backslash\Sigma_{n,d}$, we can use a dual functional $\eta \in \Sigma_{n,d}^{\ast}$ to separate $q{(x)}$ from $\Sigma_{n,d}$, and then require $q{(x)}{({\sum_{i = 1}^{n}x_{i}^{2}})}^{r}$ to be sos, so that $q{(x)}$ stays in $P_{n,d}$.

The converse of Lemma 3.1 does not hold. The Choi matrix serves as a counterexample. It is easy to check that all $7$ principal minors of $C{(x)}$ are sos polynomials and yet it is not an sos-matrix. This is in contrast with the fact that a polynomial matrix is PSD if and only if all its principal minors are psd polynomials. The latter statement follows almost immediately from the well-known fact that a constant matrix is PSD if and only if all its principal minors are nonnegative.
