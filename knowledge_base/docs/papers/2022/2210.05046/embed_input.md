Data-Driven Feedback Linearization Using the Koopman Generator

Topics include Online algorithms, Control, KGFL, Feedback linearization.

This paper contributes a theoretical framework for data-driven feedback linearization of nonlinear control-affine systems. We unify the traditional geometric perspective on feedback linearization with an operator-theoretic perspective involving the Koopman operator. We first show that if the distribution of the control vector field and its repeated Lie brackets with the drift vector field is involutive, then there exists an output and a feedback control law for which the Koopman generator is finite-dimensional and locally nilpotent. We use this connection to propose a data-driven algorithm Koopman Generator-based Feedback Linearization (KGFL) for feedback linearization. Particularly, we use experimental data to identify the state transformation and control feedback from a dictionary of functions for which feedback linearization is achieved in a least-squares sense. We also propose a single-step data-driven formula which can be used to compute the linearizing transformations. When the system is feedback linearizable and the chosen dictionary is complete, our data-driven algorithm provides the same solution as model-based feedback linearization....

## Introduction

Nonlinear control methods rooted in model-based approaches have received considerable attention. Among these techniques, feedback linearization has emerged as a prominent strategy, offering the implementation of straightforward linear control methodologies to nonlinear systems. However, a notable limitation of this approach is its demand for a comprehensive knowledge of the system dynamics. Consequently, inadequate system identification in the context of complex, high-dimensional cyber-physical systems can lead to poor control performance....

Recently, significant attention has been directed towards the Koopman operator due to its capacity to furnish a global (infinite-dimensional) linear representation of autonomous nonlinear systems. It was shown in that the Koopman operator can be approximated in finite dimensions with data using a dictionary of observables, which has been a notable direction of research for nonlinear systems. However, the commonality between the two aforementioned methodologies pertains to the concept of complete linearization, a dimension of inquiry that has hitherto remained unexplored in the existing literature....

## Conclusion

We establish a connection between the traditional model-based feedback linearization technique and the Koopman generator. Particularly, we show that here exists an observable and a state feedback control that renders the Koopman-generator finite-dimensional and nilpotent when the system is feedback linearizable. Using this connection, we develop an algorithm called KGFL to feedback linearize a control-affine system using experimental data. We demonstrate the algorithm numerically on complex dynamical systems and discuss tradeoffs related to the size of the dictionaries and the size of the dataset....

Here $D{(x)}$ utilizes the structure of $H{(x)}$ as the state transformation $H{(x)}$ contains the observable $h$ and its repeated derivatives. Utilization of this structure for the dictionary is also a novelty of our algorithm. The estimated state transformation $\hat{z}{(x)}$ and control transformations can now be represented as follows:

### III-A Koopman generator-based feedback linearization

### Theorem III.2 (*Full-state and input-output linearizing transformations*)

Problem setup. We consider a continuous-time nonlinear control-affine system, with single input, of the form:
