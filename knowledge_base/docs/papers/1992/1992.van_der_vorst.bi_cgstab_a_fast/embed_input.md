Bi-CGSTAB: A Fast and Smoothly Converging Variant of Bi-CG for the Solution of Nonsymmetric Linear Systems

Topics include Krylov methods, Bi-CGSTAB, Nonsymmetric linear systems, Biconjugate gradient, Iterative solvers, Numerical linear algebra.

Introduces Bi-CGSTAB, a stabilized variant of Bi-CG designed to retain fast convergence while avoiding the irregular convergence and cancellation problems seen in CG-S. It became one of the standard Krylov methods for nonsymmetric linear systems because it offers smoother residual behavior with modest implementation cost.

Recently the Conjugate Gradients-Squared (CG-S) method has been proposed as an attractive variant of the Bi-Conjugate Gradients (Bi-CG) method. However, it has been observed that CG-S may lead to a rather irregular convergence behaviour, so that in some cases rounding errors can even result in severe cancellation effects in the solution. In this paper, another variant of Bi-CG is proposed which does not seem to suffer from these negative effects. Numerical experiments indicate also that the new variant, named Bi-CGSTAB, is often much more efficient than CG-S.
