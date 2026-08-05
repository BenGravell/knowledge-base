<!-- arxiv-full-text:v1 {"arxiv_id": "1305.6644", "source": "arxiv-pdf"} -->

## INTRODUCTION

There are several curves proposed for Computer Aided Design either [Farin 2002; Baran et al. 2010; De Boor 1978], for trajectories planning of robots and vehicles and for geometric roads layout [De Cecco et al. 2007; Scheuer and Fraichard 1997].

The most important curves are the clothoids (also known as Euler's or Cornu's spirals), the clothoids splines (a planar curve consisting in clothoid segments), circles and straight lines,[Davis 1999; Meek and Walton 1992; Meek and Walton 2004; 2009; Walton and Meek 2009], the generalized clothoids or Bezier spirals [Walton and Meek 1996]. Pythagorean Hodograph [Walton and Meek 2007; Farouki and Neff 1995], bi-arcs and conic curves are also widely used [Pavlidis 1983]. It is well known that clothoids are extremely useful despite their transcendental form.

The procedure that allows a curve to interpolate two given points in a plane with assigned unit tangent vectors is called G 1 Hermite interpolation, while if the curvatures are given at the two points, then this is called G 2 Hermite interpolation [McCrae and Singh 2009]. A single clothoid segment is not enough to ensure G 2 Hermite interpolation, because of the insufficient degrees of freedom. For example the interpolation problem is solved by using composite clothoid segments in [Shin and Singh 1990] and using cubic spirals in [Kanayama and Hartman 1989]. However, in some applications is enough the cost-effectiveness of a G 1 Hermite interpolation [Walton and Meek 2009; Bertolazzi et al. 2006] especially when the discontinuity of the curvature is acceptable.

The purpose of this paper is to describe a new method for G 1 Hermite interpolation with a single clothoid segment; this method, which does not require to split the problem in mutually exclusive cases, is fully effective even in case of Hermite data like straight lines or circles (see Figure 1 - right). These are of course limiting cases but are naturally treated in the present approach. In previous works the limiting cases are treated separately introducing thresholds. The decomposition in mutually exclusive states is just a geometrical fact that helps to understand the problem but introduces instabilities and inaccuracies which are absent in the present formulation, as we show in the section of numerical tests.

Finally, the problem of the G 1 Hermite interpolation is reduced to the computation of a zero of a unique nonlinear equation. The Newton-Rasphson iterative algorithm is used to accurately compute the zero and a good initial guess is also derived so that few iterations (less than four) suffice.

The article is structured as follows. In section 2 we define the interpolation problem, in section 3 we describe the passages to reformulate it such that from three equations in three unknowns it reduces to one nonlinear equation in one unknown. Section 4 describes the theoretical aspects of the present algorithm. Here it is proved the existence of the solution and how to select a valid solution among the infinite possibilities. A bounded range where this solution exists and is unique is provided. Section 5 is devoted to the discussion of a good starting point for the Newton-Raphson method, so that using that guess, quick convergence is achieved. Section 6 introduces the Fresnel related integrals, e.g. the momenta of the Fresnel integrals. Section 6 analyses the stability of the computation of the clothoid and ad hoc expressions for critical cases are provided. Section 7 is devoted to numerical tests and comparisons with other methods present in literature. In the Appendix a pseudo-code complete the presented algorithm for the accurate computation of the Fresnel related integrals.

## THE FITTING PROBLEM

Consider the curve which satisfies the following differential equations: where s is the arc parameter of the curve, ϑ (s) is the direction of the tangent (x ′ (s), y ′ (s)) and K (s) is the curvature at the point (x (s), y (s)). When K (s):= κ ′ s + κ, i.e. when the curvature changes linearly, the curve is called Clothoid. As a special case, when κ ′ = 0 the curve has constant curvature, i.e. is a circle and when both κ = κ ′ = 0 the curve is a straight line. The solution of ODE is given in the next definition: Definition 2.1 Clothoid curve. The general parametric form of a clothoid spiral curve is the following Notice that 1 2 κ ′ s 2 + κs + ϑ 0 and κ ′ s + κ are, respectively, the angle and the curvature at the abscissa s.

The computation of the integrals is here recast as a combination (discussed in Section 6) of Fresnel sine S ( t ) and cosine C ( t ) functions. Among the various possible definitions, we choose the following one, Abramowitz and Stegun 1964.

Definition 2.2 Fresnel integral functions.

Remark 2.3. The literature reports different definitions, such as: The identities allow to switch among these definitions: Thus, the problem considered in this paper is stated next.

Problem 1 Clothoid Hermite interpolation. Given two points (x 0, y 0) and (x 1, y 1) and two angles ϑ 0 and ϑ 1, find a clothoid segment of the form which satisfies: where L > 0 is the length of the curve segment.

The general scheme is showed in Figure 1 - left.

Remark 2.4. Notice that Problem 1 admits an infinite number of solutions. In fact, given ϑ ( s ), the angle of a clothoid which solves Problem 1, satisfies ϑ = ϑ 0 + 2 kπ and ϑ ( L ) = ϑ 1 + 2 ℓπ with k, ℓ ∈ Z: different values of k correspond to different interpolant curves that loop around the initial and the final point. Figure 1- right shows possible solutions derived from the same Hermite data.

The solution of Problem 1 is a zero of the following nonlinear system involving the unknowns L, κ, κ ′: Fig. 1. Left: G 1 Hermite interpolation schema and notation. Right: some possible solutions.

In Section 3 the nonlinear system is reduced to a single non linear equation that allows for the efficient solution Problem 1.

## RECASTING THE INTERPOLATION PROBLEM

The nonlinear system is recasted in an equivalent form by introducing the parametrization s = τL so that the involved integrals have extrema which do not dependent on L: where A = 1 2 κ ′ L 2, B = Lκ, ∆ x = x 1 -x 0, ∆ y = y 1 -y 0. It is convenient to introduce the following functions whose properties are studied in Section 6: Combining with becomes: The third equation in is linear so that solve it with respect to B, and the solution of the nonlinear system is reduced to the solution of the nonlinear system of two equations in two unknowns, namely L and A: followed by the computation of B. We can perform one further simplification using polar coordinates to represent (∆ x, ∆ y), namely From and L > 0 we define two nonlinear functions f (L, A) and g (A), where g (A) does not depend on L, as follows: Taking advantage of the trigonometric identities the functions g (A) and f (L, A) are simplified: Supposing to find A such that g (A) = 0, then from f (L, A) = 0 we compute L and B using equations and respectively. This yields Thus, the solutions of the nonlinear system are known if the solutions of the single nonlinear function g (A) of equation are determined. The solution of Problem 1 is recapitulated in the following steps: This algorithm prompts the following issues.

- How to compute the roots of g (A) and to select the one which appropriately solves Problem 1. - Check that the length L is well defined and positive.

These issues are discussed in Section 4. Unlike the work of Meek and Walton 2009, this method does not require to split the problem in mutually exclusive cases, i.e., straight lines and circles are treated naturally.

## THEORETICAL DEVELOPMENT

In this section the existence and selection of the appropriate solution are discussed in detail. The computation of L requires only to verify that for A ⋆ such that g ( A ⋆ ) = 0 then h ( A ⋆ ) = X (2 A ⋆, δ -A ⋆, φ 0 ) = 0. This does not ensure that the computed L is positive; but positivity is obtained by an appropriate choice of A ⋆.

## Symmetries of the roots of g ( A )

The general analysis of the zeros of g (A) requires the angles φ 0 and φ 1 to be in the range (-π, π). It is possible to restrict the domain of search stating the following auxiliary problems: The reversed problem. The clothoid joining (x 1, y 1) to (x 0, y 0) with angles ϑ R 0 = -ϑ 1 and ϑ R 1 = -ϑ 0 is a curve with support a clothoid that solves Problem 1 but running in the opposite direction (with the same length L). Let δ R = ϑ R 1 -ϑ R 0 = -ϑ 0 + ϑ 1 = δ, it follows that g R (A):= Y (2 A,δ -A, -φ 1) is the function whose zeros give the solution of the reversed interpolation problem.

The mirrored problem. The curve obtained connecting ( x 0, y 0 ) to ( x 1, y 1 ) with angle ϑ M 0 = ϕ -φ 0 and ϑ M 1 = ϕ -φ 1 is a curve with support a curve solving the same problem but mirrored along the line connecting the points ( x 0, y 0 ) and ( x 1, y 1 ) (with the same length L ). Let δ M = ϑ M 1 -ϑ M 0 = -φ 1 + φ 0 = -δ, it follows that g M ( A ):= Y (2 A, -δ -A, -φ 0 ) is the function whose zeros are the solution of the mirrored interpolation problem.

Lemma (4.1) shows that it is possible to reduce the search of the roots in the domain | φ 0 | < φ 1 ≤ π. The special cases φ 0 ± φ 1 = 0 are considered separately.

Lemma 4.1. Let g (A):= Y (2 A,δ A,φ) and h (A):= X (2 A,δ A,φ) with Thus, g (A) has the same roots of g R (A), g M (A) with opposite sign.

Using again g (A) with the following manipulation: we have g (A) = -g M (-A). The thesis for h (A) is obtained in the same way.

Figure 2 shows the domain | φ 0 | < φ 1 ≤ π with the mirrored and reversed problem. Reflecting and mirroring allows to assume the constraints for the angles described in Assumption (4.2).

Assumption 4.2 Angle domains. The angles φ 0 and φ 1 satisfy the restriction: | φ 0 | ≤ φ 1 ≤ π with ambiguous cases | φ 0 | = φ 1 = π excluded (see Figure 2).

This ordering ensures that the curvature of the fitting curve is increasing, i.e. κ ′ > 0. Notice that if A is the solution of nonlinear system then κ ′ = 2 A/L 2, i.e. the sign of A is the sign of κ ′ and thus A must be positive. Finally, δ = φ 1 -φ 0 > 0. This assumption is not a limitation because any interpolation problem can be reformulated as a problem satisfying Assumption 4.2 while the analysis for the special case φ 0 + φ 1 = 0 and φ 0 -φ 1 = 0 are performed apart.

Lemma 4.3. The (continuous) functions g (A):= Y (2 A,δ -A,φ 0) and h (A):= X (2 A,δ -A,φ 0) for A > 0, when φ 0 and φ 1 satisfy assumption 4.2, can be written as Fig. 2. Left: the domain φ 1 > | φ 0 | with the special cases φ 1 = φ 0 and φ 1 + φ 0 = 0. Right: the domain mirrored and reversed.

Proof. With standard trigonometric passages and A > 0 we deduce the following expression for g (A) and h (A): Combining equivalence and the parity properties of sin x and cos x, g (A) and h (A) take the form: and ̂ C, ̂ S are defined; moreover By using identities equation becomes: It is recalled that A must be positive, so that when A to 0 < A < δ then σ -= 1, otherwise, when A > δ then σ -= -1. In case A = δ then θ = 0 and the second integral is 0 and thus g (δ) = p = q and h (δ) = p = q.

## Localization of the roots of g ( A )

The problem g ( A ) = 0 has in general infinite solutions. The next Theorems show the existence of a unique solution in a prescribed range, they are in part new and in part taken from [Walton and Meek 2009] here reported without proofs and notation slightly changed to better match the notation. By appropriate transformations we use these Theorems to select the suitable solution and find the interval where the solution is unique. The Theorems characterize the zeros of the functions finding intervals where the solution exists and is unique.

Theorem 4.4 Meek-Walton th.2. Let 0 < -φ 0 < φ 1 < π. If p > 0 then p (θ) = 0 has no root for θ ≥ 0. If p ≤ 0 then p (θ) = 0 has exactly one root for θ ≥ 0. Moreover, the root occurs in the interval [0, θ ⋆] where Theorem 4.5 Meek-Walton th.3. Let -π < -φ 1 < φ 0 < 0 and q > 0 then q (θ) = 0 has exactly one root in the interval [0, π/ 2 + φ 0]. If q < 0 then q (θ) = 0 has no roots in the interval [0, π/ 2 + φ 0].

Theorem 4.6 Meek-walton th.4. Let φ 0 ∈ [0, π ) and φ 1 ∈ (0, π ], then q ( θ ) = 0 has exactly one root in [0, π/ 2 + φ 0 ], moreover, the root occurs in [ φ 0, π/ 2 + φ 0 ].

The following additional Lemmata are necessary to complete the list of properties of p (θ) and q (θ): Lemma 4.7. Let p (θ) and q (θ) as defined in equation, then

- q (θ) = 0 for θ ∈ [φ 0, π/ 2+ φ 0] and the root is unique in the interval [0, π/ 2+ φ 0]; - if φ 1 > φ 0 then p (θ) > 0 for all θ ≥ 0 otherwise p (θ) = 0 for all θ ≥ 0; - p (θ) = 0 has a unique root θ that satisfies 0 ≤ θ ≤ θ 0 with θ 0 defined. - q (θ) = 0 has no roots in the interval [0, π/ 2 + φ 0]; - q (θ) = 0 has a unique root in the interval [0, π/ 2 + φ 0] Proof. A straightforward application of Theorems 4.4, 4.5 and 4.6. For point (c),: in addiction, since -π ≤ φ 0 ≤ -π/ 2, both sin φ 0 ≤ 0 and cos φ 0 ≤ 0 resulting in p = q < 0.

The combination of Lemma 4.1 together with reversed and mirrored problems, proves that the interpolation problem satisfies Assumption 4.2.

With this Assumption and Lemma 4.3 prove a Theorem that states the existence and uniqueness in a specified range. We show the special case of φ 0 + φ 1 = 0 in a separated Lemma, the case of φ 0 -φ 1 = 0 follows from the application of Theorem 4.6 for positive angles, because Assumption 4.2 forces φ 1 ≥ 0 and excludes the case of equal negative angles.

Lemma 4.8. Let φ 0 + φ 1 = 0 and φ 0 ∈ ( -π, π ), then g ( A ) = 0 has the unique solution A = 0 in the interval ( -2 π, 2 π ).

Using properties of odd and even functions the rightmost integral of the previous line vanishes yielding From this last equality, if A = 0 then g (A) = 0. If 0 < | A | < 4 π, the sign of the quantity sin(A (z 2 -1) / 4) is constant; if | φ 0 | < π/ 2, then cos(zφ 0) > 0 and thus g (A) has no roots. For the remaining values of φ 0, i.e. π/ 2 ≤ | φ 0 | < π, we have: If in addition, 0 < | A | < 2 π then ∣ ∣ sin(A (z 2 -1) / 4) ∣ ∣ is positive and monotone decreasing so that: and thus g (A) = 0 for 0 < | A | < 2 π and | φ 0 | < π.

We state now the main Theorem of this study.

Theorem 4.9 Existence and uniqueness of solution for system. The function g (A), when angles φ 0 and φ 1 satisfy assumption 4.2, admits a unique solution for A ∈ (0, A max], where Proof. The special cases φ 0 + φ 1 = 0 and φ 0 = φ 1 were previously considered and in Lemma 4.8. The other cases are discussed next. From Lemma 4.7 it follows that the two equations Fig. 3. Left: functions g and h, when g vanishes, h is strictly positive. Right: the plot of cos z -w sin z. In both figures φ 0 = -(3 / 4) π and φ 1 = π. cannot be satisfied by the same θ in the specified range, so that they are mutually exclusive although one of the two is satisfied. Thus g (A) = 0 has a unique solution. To find the equivalent range of A we select the correct solution of (δ -A) 2 = 4 Aθ max. The two roots are: and thus A 2 is used to compute A max. We are now interested to check if h (A) > 0 when g (A) = 0. According to Lemma 4.3, Suppose we set the root θ of g (by doing so, we set also the value of A), we have to show that if A ≤ δ then p (θ) > 0 and if A ≥ θ then q (θ) > 0.

We begin analysing A ≤ δ for | φ 0 | < φ 1 ≤ π 2. In this case we have that the cosine in the numerator is always positive, and so is the square root at the denominator, thus the integral p (θ) is strictly positive. When -π < φ 0 < -π 2 then φ 1 ≥ π 2, we can write, for all w ∈ R, In particular we can choose w = cos φ 0 sin φ 0 > 0 positive (which, incidentally is always positive because -π < φ 0 < -π 2) so that the integrand function vanishes for the three values z = φ 0, φ 0 + π, φ 0 +2 π. Moreover cos z -w sin z is strictly positive for z ∈ (φ 0, φ 0 + π), see Figure 3. Thus we can bound integral as The last subcase of A ≤ δ occurs when both φ 0, φ 1 > π 2, but it is not necessary because Lemma 4.7 at point (a) states that p (θ) > 0 does not vanish. We discuss now the second case, when A ≥ δ, it is recalled that from with ∆ ̂ C, ∆ ̂ S > 0 and for θ ∈ [0, π 2 + φ 0] we can write -π 2 ≤ φ 0 -θ ≤ 0, thus the cosine is positive and the sine is negative, hence the whole quantity is strictly positive.

Corollary 4.10. All the solutions of the nonlinear system are given by where A is any root of g (A):= Y (2 A,δ -A,φ 0) provided that the corresponding h (A):= X (2 A,δ -A,φ 0) > 0.

Corollary 4.11. If the angles φ 0 and φ 1 are in the range [-π, π], with the exclusion of the points φ 0 = -φ 1 = ± π, the solution exists and is unique for -A max ≤ A ≤ A max where Notice that the solution of the nonlinear system is reduced to the solution of g (A) = 0. Hence the interpolation problem is reduced to a single nonlinear equation that can be solved numerically with Newton-Raphson Method; also, Corollary 4.11 ensures that L > 0 for A in the specified range. It can also be proved that in general for all A such that g (A) = 0 then h (A) = 0. In the next section, a technique to select a meaningful initial point is described.

## COMPUTING THE INITIAL GUESS FOR ITERATIVE SOLUTION

The zeros of function g ( A ) are used to solve the interpolation problem and are approximated by the Newton-Raphson scheme. This algorithm needs 'a guess point' to converge to the appropriate solution. Notice that there is an infinite number of solutions of Problem 1 and we need criteria for the selection of a solution. By Theorem 4.9 we reduce the problem to standard angles and search the unique solution in the appropriate range.

Denote with A (φ 0, φ 1) the selected zero of g (A):= Y (2 A,δ -A,φ 0) as a function of φ 0 and φ 1. Figure 4 shows that A (φ 0, φ 1) is approximated by a plane. A simple approximation of A (φ 0, φ 1) is obtained by sin x ≈ x in Y (2 A,δ -A,φ 0) and thus, This approximation is a fine initial point for Newton-Raphson, however better approximation for A (φ 0, φ 1) are obtained by least squares method. Invoking reflection and mirroring properties, the functional form of the approximation is simplified and results in the two following expressions for A (φ 0, φ 1): Using, (20a) or (20b) as the starting point for Newton-Raphson, the solution for Problem 1 is found in very few iterations. Computing the solution with NewtonRaphson starting with the proposed guesses in a 1024 × 1024 grid for φ 0 and φ 1 ranging in [-0. 9999 π, 0. 9999 π] with a tolerance of 10 -10, results in the following distribution of iterations: The complete algorithm for the clothoid computation is written in the function buildClothoid of Table I. This function solves equation and builds the coefficients of the interpolating clothoid.

Fig. 4. Left: the function A ( φ 0, φ 1 ). Notice that A ( φ 0, φ 1 ) is approximately a plane. Right: values of the length L of the computed clothoid as a function of φ 0 and φ 1. Notice that when angles satisfy φ 0 = π, φ 1 = -π or φ 0 = -π, φ 1 = π the length goes to infinity. The angles range in [ -π, π ].

## Bertolazzi and M.Frego

Table I. The fitting algorithm The algorithm is extremely compact and was successfully tested in any possible situation. The accurate computation of the clothoid needs an equally accurate computation of g (A) and g ′ (A) and thus the accurate computation of Fresnel related functions X (a, b, c) and Y (a, b, c) with associated derivatives. These functions are a combination of Fresnel and Fresnel momenta integrals which are precise for large a and small momenta. For the computation, only the first two momenta are necessary so that the inaccuracy for large momenta does not pose any problem. A different problem is the computation of these integrals for small values of | a |. In this case, laborious expansion are used to compute the integrals with high accuracy. The expansions are discussed in section 6.

## ACCURATE COMPUTATION OF FRESNEL MOMENTA

Here it is assumed that the standard Fresnel integrals can be computed with high accuracy. For this task one can use algorithms described in Snyder 1993, Smith 2011 and Thompson 1997 or using continued fraction expansion as in Backeljauw and Cuyt 2009 or simply use the available software [Press et al. 2002]. It is possible to reduce the integrals to a linear combination of this standard Fresnel integrals. However simpler expressions are obtained using also the momenta of the Fresnel integrals: Notice that C (t):= C 0 (t) and S (t):= S 0 (t). Closed forms via the exponential integral or the Gamma function are also possible, however we prefer to express them as a recurrence. Integrating by parts, the following recurrence is obtained: Recurrence is started by computing standard Fresnel integrals and (changing z = τ 2) the following values are obtained: Also C 2 (t) and S 2 (t) are readily obtained: Notice that from recurrence it follows that C k (t) and S k (t) with k odd do not contain Fresnel integrals and are combination of elementary functions.

The computation of clothoids relies most on the evaluation of integrals of kind with their derivatives. The reduction is possible via a change of variable and integration by parts. It is sufficient to consider two integrals, that cover all possible cases: and finally, equation can be evaluated as From the trigonometric identities, integrals are rewritten as Defining X k (a, b):= X k (a, b, 0) and Y k (a, b):= Y k (a, b, 0) the computation of is reduced to the computation of X k (a, b) and Y k (a, b). It is convenient to introduce the following quantities so that it is possible to rewrite the argument of the trigonometric functions of X k (a, b) and Y k (a, b) as By using the change of variable ξ = τ z + ω -with inverse τ = z -1 (ξ -ω -) for

## · E.Bertolazzi and M.Frego

X k (a, b) and the identity we have: are the evaluation of the momenta of the Fresnel integrals as defined. Analogously for Y k (a, b) we have: This computation is inaccurate when | a | is small: in fact z appears in the denominator of several fractions. For this reason, for small values of | a | we substitute and with asymptotic expansions. Notice that the recurrence is unstable so that it produces inaccurate results for large k, but we need only the first two terms so this is not a problem for the computation of g (A) and g ′ (A).

## Accurate computation with small parameters

When the parameter a is small, we use identity to derive series expansion: and analogously using again identity we have the series expansion From the inequalities: we estimate the remainder for the series of X k: The same estimate is obtained for the series of Y k Remark 6.1. Both series and converge fast. For example, if | a | < 10 -4 and p = 2, the error is less than 6. 26 · 10 -18 while if p = 3 the error is less than 1. 6 · 10 -26.

It is possible to compute X k (0, b) and Y k (0, b) as follows: This recurrence permits the computation of X k (0, b) and Y k (0, b) when b = 0, however, it is readily seen that this recurrence formula is not stable. As an alternative, an explicit formula based on Lommel function s µ,ν (z) can be used [Shirley and Chang 2003]. The explicit formula is, for k = 1, 2, 3,...: where f (b) = b -1 sin b -cos b and g (b) = f (b)(2 + k). The Lommel function has the following expansion and using this expansion in results in the following explicit formula for k = 1, 2, 3,...:

## · E.Bertolazzi and M.Frego

## NUMERICAL TESTS

The algorithm was implemented and tested in MATLAB. For the Fresnel integrals computation we use the script of Telasula. The first six tests are taken form Walton and Meek and a MATLAB implementation of the algorithm described in the reference is used for comparison.

The accuracy of fit as in Walton and Meek is determined by comparing the ending point as computed by both methods, with the given ending point. For all the tests, both methods have an error which does not exceed 10 -15 or less. Also iterations are comparable and are reported in the following table.

The difference of the present method compared with the algorithm of Walton and Meek are in the transition zone where the solution is close to be a circle arc or a segment. In fact in this situation the present method performs better without loosing accuracy or increasing in iterations as for the Meek and Walton algorithm. The following tests highlight the differences: Table II collects the results. The error is computed as the maximum of the norm of the differences at the ending point as computed by the algorithm with the given ending point. The tolerance used for the Newton iterative solver for both the algorithms is 1 · 10 -12. Improving the tolerance does not improve the error for both the methods. Notice that the proposed algorithm computes the solution with constant accuracy and few iterations while Meek and Walton algorithm loose precision and uses more iterations. The ∞ symbol for iterations in Table II means that Newton method do not reach the required accuracy and the solution is computed using the last computed values. The iteration limit used was 100, increasing this limit to 1000 Table II. Test #7 and #8 results | | Test #7 | Test #7 | Test #7 | Test #7 | Test #8 | Test #8 | Test #8 | Test #8 | did not change the results. In Table II, the algorithm of Walton and Meek has a large number of iteration respect to the proposed method. To understand this behavior, it is recalled that in solving a general nonlinear function f (θ) = 0 Fig. 5. Results of test N.1 up to test N.6. using Newton-Raphson method, the error ϵ k = θ k -α near the root θ = α satisfies: showing the quadratic behavior of Newton-Raphson method; large values of C reflects a slow convergence. If f (θ) is the function used by Walton and Meek for computing the clothoid curve and g (A) is the function of the proposed method then and the error e k = A k -A ⋆ near the root θ (A ⋆) = α satisfy: If g (A ⋆) = 0 and A ⋆ > 0 but small (i.e. A ⋆ ≈ 0) then θ (A) ≈ δ 2 / (4 A) near A ⋆, moreover thus if the ratio δ/A ⋆ is large then | C | ≫ | C ⋆ | and thus Walton and Meek algorithm is slower than the proposed one. This is verified in Table II. Notice that Test #7 has constant C lower than Test #7 and this is reflected in the iteration counts. When the ratio δ/A ⋆ is small then | C | ≪| C ⋆ | and the algorithm of Meek & Walton should be faster. An estimation based on Taylor expansion shows that when δ/A ⋆ is small then C ⋆ is small too. Thus the proposed algorithm do not suffer of slow convergence as verified experimentally.

## CONCLUSIONS

An effective solution to the problem of Hermite G 1 interpolation with a clothoid curve was presented. We solve the G 1 Hermite interpolation problem in a new and complete way.

In our approach we do not need the decomposition in mutually exclusive states, that, numerically, introduces instabilities and inaccuracies as showed in section 7. The solution of the interpolation problem is uniformly accurate even when close to a straight line or an arc of circle, as pointed out in section 7, this was not the case of algorithms found in literature. In fact, even in domains where other algorithms solve the problem, we perform better in terms of accuracy and number of iterations. The interpolation problem was reduced to one single function in one variable making the present algorithm fast and robust. Existence and uniqueness of the problem was discussed and proved in section 4. A guess functions which allows to find that zero with very few iterations in all possible configurations was provided. Asymptotic expansions near critical values for Fresnel related integrals are provided to keep uniform accuracy. Implementation details of the proposed algorithm are given in the appendix using pseudocode and can be easily translated in any programming language.

## ALGORITHMS FOR THE COMPUTATION OF FRESNEL RELATED INTEGRALS

We present here the algorithmic version of the analytical expression we derived in Section 6 and 7. These algorithms are necessary for the computation of the main function buildClothoid of Section 5 which takes the input data ( x 0, y 0, ϑ 0, x 1, y 1, ϑ 1 ) and returns the parameters ( κ, κ ′, L ) that solve the problem as expressed in equation. Function evalXY computes the generalized Fresnel integrals. It distinguishes the cases of a larger or smaller than a threshold ε. The value of ε is discussed in Section 7, see for example Remark 6.1. Formulas, used to compute X k ( a, b ) and Y k ( a, b ) at arbitrary precision when | a | ≥ ε, are implemented in function evalXYaLarge. Formulas -, used to compute X k ( a, b ) and Y k ( a, b ) at arbitrary precision when | a | < ε, are implemented in function evalXYaSmall. This function requires computation of implemented in function evalXYaZero which needs (reduced) Lommel function implemented in function rLommel.

## Function evalXY( a, b, c, k )

- 1 if | a | < ε then ˆ X, ˆ Y ← evalXYaSmall( a, b, k,5) else ˆ X, ˆ Y ← evalXYaLarge( a, b, k ) for j = 0, 1,..., k -1 do X j ← ˆ X j cos c -ˆ Y j sin c; Y j ← ˆ X j sin c + ˆ Y j cos c return X, Y

## Function evalFresnelMomenta( t, k )

## Function evalXYaLarge( a, b, k ) 1 s ← a | a |; z ← √ | a | /π; ℓ ← s b z π; γ ←-sb 2 2 | a |; s γ ← sin γ; c γ ← cos γ; 2 C +, S + ← evalFresnelMomenta( ℓ + z, k ); C -, S -← evalFresnelMomenta( z, k ); 3 ∆ C ← C + -C -; ∆ S ← S + -S -; 4 X 0 ← z -1 ( c γ ∆ C 0 -s s γ ∆ S 0 ); Y 0 ← z -1 ( s γ ∆ C 0 + s c γ ∆ S 0 ); 5 if k > 1 then 6 d c ← ∆ C 1 -ℓ ∆ C 0; d s ← ∆ S 1 -ℓ ∆ S 0; 7 X 1 ← z -2 ( c γ d c -s s γ d s ); Y 1 ← z -2 ( s γ d c + s c γ d s ); 8 end if 9 if k > 1 then 10 d c ← ∆ C 2 + ℓ ( ℓ ∆ C 0 -2∆ C 1 ); d s ← ∆ S 2 + ℓ ( ℓ ∆ S 0 -2∆ S 1 ); 11 X 2 ← z -3 ( c γ d c -s s γ d s ); Y 2 ← z -3 ( s γ d c + s c γ d s ); 12 end if 13 return X, Y

## Function evalXYaZero( b, k ) 1 if | b | < ε then 2 X 0 ← 1 -( b 2 / 6) ( 1 -b 2 / 20 ); Y 0 ← ( b 2 / 2) ( 1 -( b 2 / 6) ( 1 -b 2 / 30 )); 3 else 4 X 0 ← (sin b ) /b; Y 0 ← (1 -cos b ) /b; 5 end if 6 A ← b sin b; D ← sin b -b cos b; B ← bD; C ← -b 2 sin b; 7 for k = 0, 1,..., k -1 do 8 X k +1 ← 1 1 + k ( kA rLommel ( k + 1 2, 3 2, b ) + B rLommel ( k + 3 2, 1 2, b ) +cos b ); 9 Y k +1 ← 1 2 + k ( C rLommel ( k + 3 2, 3 2, b ) +sin b ) + D rLommel ( k + 1 2, 1 2, b ); 10 end for 11 return X, Y

## Function evalXYaSmall( a, b, k, p ) 1 ˆ X, ˆ Y ← evalXYaZero( b, k +4 p +2); t ← 1; 2 for j = 0, 1,..., k -1 do X j ← X 0 j -a 2 Y 0 j +2; Y j ← Y 0 j + a 2 X 0 j +2 for n = 1, 2,..., p do 3 t ← ( -t a 2 ) / (16 n (2 n -1)); s ← a/ (4 n +2); 4 for j = 0, 1,..., k -1 do 5 X j ← X j + t ( ˆ X 4 n + j -s ˆ Y 4 n + j +2 ); 6 Y j ← Y j + t ( ˆ Y 4 n + j + s ˆ X 4 n + j +2 ); 7 end for 8 end for 9 return X, Y

## Function rLommel( µ, ν, b )
