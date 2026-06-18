Regularized Newton Method with Global O(1/k^2) Convergence

Topics include Regularized Newton method, Line search.

We present a Newton-type method that converges fast from any initialization and for arbitrary convex objectives with Lipschitz Hessians. We achieve this by merging the ideas of cubic regularization with a certain adaptive Levenberg-Marquardt penalty. In particular, we show that the iterates given by x^(k)+1 = x^(k) - bigl(nabla^ f(x^(k)) + sqrt(H|nabla f(x^(k))|) Ibigr)^(-1)nabla f(x^(k)), where H > 0 is a constant, converge globally with a O(1/k^) rate. Our method is the first variant of Newton's method that has both cheap iterations and provably fast global convergence. Moreover, we prove that locally our method converges superlinearly when the objective is strongly convex. To boost the method's performance, we present a line search procedure that does not need prior knowledge of H and is provably efficient.

## Introduction

Overview. The history of Newton's method spans over several centuries and the method has become famous for being extremely fast, and infamous for converging only from initialization that is close to a solution. Despite the latter drawback, Newton's method is a cornerstone of convex optimization and it motivated the development of numerous popular algorithms, such as quasi-Newton and trust-region procedures. Its applications and extensions are countless, so we refer to the study in that lists more than 1,000 references in total.

Although widely acknowledged, the extreme behaviour of Newton's method is still startling. Why does it converge so efficiently from one initialization and hopelessly diverge from a tiny perturbation of the same initialization? This oddity encourages us to look for a method with a bit slower but more robust convergence, but the existing theory does not offer any good option. All global variants that we are aware of make iterations more expensive by requiring a line search, solving a subproblem, or solving a series of problems.

The goal of our work is to show that there is, in fact, a simple fix. The core idea of our approach is to employ an adaptive variant of Levenberg--Marquardt regularization to make the update efficient, and to leverage the advanced theory of cubic regularization to find an adaptive rule that would work provably. The rest of our paper is organized as follows. Firstly, we formally state the problem, and expand on the related work and motivating approaches. In Section 2 Convergence \bottomtitlebar"), we give theoretical guarantees of our algorithm and outline the proof.

## Conclusion

In this paper, we presented a proof that a simple gradient-based regularization allows Newton method to converge globally. Our proof relies on new techniques and appears to be less trivial than that of cubic Newton. At the same time, our analysis has a lot in common with that of cubic Newton and the regularization technique has been known in the literature for a long time. We hope that many existing extensions of cubic Newton, such as its acceleration, will become possible with future work. It would be very exciting to see other extensions, for instance, stochastic variants, and quasi-Newton estimation of the Hessian.
