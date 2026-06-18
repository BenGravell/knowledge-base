Data-driven Discovery of Koopman Eigenfunctions for Control

Topics include Predictive control, Regression, Online algorithms, Control, KRONIC, Nonlinear systems.

Data-driven transformations that reformulate nonlinear systems in a linear framework have the potential to enable the prediction, estimation, and control of strongly nonlinear dynamics using linear systems theory. The Koopman operator has emerged as a principled linear embedding of nonlinear dynamics, and its eigenfunctions establish intrinsic coordinates along which the dynamics behave linearly. Previous studies have used finite-dimensional approximations of the Koopman operator for model-predictive control approaches. In this work, we illustrate a fundamental closure issue of this approach and argue that it is beneficial to first validate eigenfunctions and then construct reduced-order models in these validated eigenfunctions. These coordinates form a Koopman-invariant subspace by design and, thus, have improved predictive power. We show then how the control can be formulated directly in these intrinsic coordinates and discuss potential benefits and caveats of this perspective. The resulting control architecture is termed Koopman Reduced Order Nonlinear Identification and Control (KRONIC).

## Introduction

In contrast to linear systems, a generally applicable and scalable framework for the control of nonlinear systems remains an engineering grand challenge. Improved nonlinear control has the potential to transform our ability to interact with and manipulate complex systems across broad scientific, technological, and industrial domains. From turbulence control to brain-machine interfaces, emerging technologies are characterized by high-dimensional, strongly nonlinear, and multiscale phenomena that lack simple models suitable for control design.

Smooth eigenfunctions in the point spectrum of the Koopman operator can be discovered from given data using sparse regression providing interpretable representations. We propose sparsity-promoting algorithms to regularize EDMD or to discover eigenfunctions directly in an implicit formulation.

The present work is outlined as follows: In Sec. 2, we demonstrate the importance of eigenfunction validation and motivate the use of sparse regression for their discovery. In Sec. 3, key results in Koopman spectral theory and corresponding data-driven approaches are summarized, and a brief background on optimal control is provided. The approach for identifying of Koopman eigenfunctions from data using sparse regression is outlined in Sec. 5. In Sec. 4, it is shown how control can be incorporated in the eigenfunction formulation.

## Discussion and conclusions

In summary, we extend the Koopman operator formalism to include actuation, and demonstrate how a nonlinear control problem may be converted into a bilinear control problem in eigenfunction coordinates. Next, we have presented a data-driven framework to identify leading eigenfunctions of the Koopman operator and sparsity-promoting extensions to EDMD. We find that lightly damped or undamped eigenfunctions may be accurately approximated from data via regression, as these eigenfunctions correspond to persistent phenomena, such as conserved quantities.
