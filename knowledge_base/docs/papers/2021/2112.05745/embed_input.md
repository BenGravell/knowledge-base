A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis

Topics include Model predictive control, Predictive control, Safety, Robustness, Neural networks, Accuracy, Sampling-based methods, Control, Sampling, Convex hull.

In this work, we analyze an efficient sampling-based algorithm for general-purpose reachability analysis, which remains a notoriously challenging problem with applications ranging from neural network verification to safety analysis of dynamical systems. By sampling inputs, evaluating their images in the true reachable set, and taking their epsilon-padded convex hull as a set estimator, this algorithm applies to general problem settings and is simple to implement. Our main contribution is the derivation of asymptotic and finite-sample accuracy guarantees using random set theory. This analysis informs algorithmic design to obtain an epsilon-close reachable set approximation with high probability, provides insights into which reachability problems are most challenging, and motivates safety-critical applications of the technique. On a neural network verification task, we show that this approach is more accurate and significantly faster than prior work. Informed by our analysis, we also design a robust model predictive controller that we demonstrate in hardware experiments.

## Introduction

Forward reachability analysis entails characterizing the reachable set of outputs of a given function corresponding to a set of inputs. This type of analysis underpins a plethora of applications in model predictive control, neural network verification, and safety analysis of dynamical systems. Sampling-based reachability analysis techniques are a particularly simple class of methods to implement; however, conventional wisdom suggests that if insufficient representative samples are considered, these methods may not be robust in that they cannot rule out edge cases missed by the sampling procedure.

it works with any choice of possibly nonlinear reachability maps and non-convex input sets,

its estimate of the reachable set is conservative with high probability and tighter than prior work,

We prove that the set estimator converges to the $\epsilon$-padded convex hull of the true reachable set as the number of samples increases. Our assumption about the sampling distribution is weaker than in related work and implies that sampling the boundary of the input set is sufficient. This asymptotic result justifies using $\epsilon$-RandUP as a thrustworthy baseline for offline validation whenever the reachability map and the input set are complex and no tractable algorithm exists.

We demonstrate $\epsilon$-RandUP on a neural network controller verification task and show that it is highly competitive with prior work. We also embed this algorithm within a robust model predictive controller and present hardware results demonstrating the reliability of the approach.

## Conclusion

We derived new asymptotic and finite-sample statistical guarantees for $\epsilon$-RandUP, a simple yet efficient algorithm for reachability analysis of general systems. We demonstrated its efficacy for a neural network verification task and its applicability to robust model predictive control. In future work, we will investigate tighter finite-sample bounds by leveraging further information about the smoothness of the input set boundary $\partial\mathcal{X}$.
