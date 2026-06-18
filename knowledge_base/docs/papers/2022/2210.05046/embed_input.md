Data-Driven Feedback Linearization Using the Koopman Generator

Topics include Online algorithms, Control, KGFL, Feedback linearization.

This paper contributes a theoretical framework for data-driven feedback linearization of nonlinear control-affine systems. We unify the traditional geometric perspective on feedback linearization with an operator-theoretic perspective involving the Koopman operator. We first show that if the distribution of the control vector field and its repeated Lie brackets with the drift vector field is involutive, then there exists an output and a feedback control law for which the Koopman generator is finite-dimensional and locally nilpotent. We use this connection to propose a data-driven algorithm Koopman Generator-based Feedback Linearization (KGFL) for feedback linearization. Particularly, we use experimental data to identify the state transformation and control feedback from a dictionary of functions for which feedback linearization is achieved in a least-squares sense. We also propose a single-step data-driven formula which can be used to compute the linearizing transformations. When the system is feedback linearizable and the chosen dictionary is complete, our data-driven algorithm provides the same solution as model-based feedback linearization.

## Introduction

Nonlinear control methods rooted in model-based approaches have received considerable attention. Among these techniques, feedback linearization has emerged as a prominent strategy, offering the implementation of straightforward linear control methodologies to nonlinear systems. However, a notable limitation of this approach is its demand for a comprehensive knowledge of the system dynamics. Consequently, inadequate system identification in the context of complex, high-dimensional cyber-physical systems can lead to poor control performance.

Problem setup.

Our objective is to transform system to a target linear system $\overset{˙}{z} = {{Az} + {Bv}}$, where $z$ and $v$ are transformed state and control, respectively. We propose to transform the state as $z = {H{(x)}}$ and the control as $u = {{\alpha{(x)}} + {\beta{(x)}v}}$. We seek to identify the transformations ${H,\alpha},$ and $\beta$ using the data $X,U$.\

Contributions. The main contributions of this paper are as follows. We first bridge the gap between the geometric framework of feedback linearization and the Koopman operator-theoretic framework. In particular, we show that, when the system is involutive to a certain degree, there exists an observable $h$ and a feedback control $\alpha$ such that the Koopman generator for the closed-loop system under the feedback $\alpha$ is nilpotent at the observable $h$. Furthermore, there exists a finite-dimensional Koopman invariant subspace of the same dimension as the involutive distribution for the system.

## Conclusion

We establish a connection between the traditional model-based feedback linearization technique and the Koopman generator. Particularly, we show that here exists an observable and a state feedback control that renders the Koopman-generator finite-dimensional and nilpotent when the system is feedback linearizable. Using this connection, we develop an algorithm called KGFL to feedback linearize a control-affine system using experimental data. We demonstrate the algorithm numerically on complex dynamical systems and discuss tradeoffs related to the size of the dictionaries and the size of the dataset.
