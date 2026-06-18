Can Transformers Learn Optimal Filtering for Unknown Systems?

Topics include Transformers, Kalman filtering, State estimation, Dynamical systems, In-context learning, Unknown systems.

Tests whether transformers trained across families of dynamical systems can perform output estimation on unseen systems, sometimes matching Kalman-filter behavior without explicit model knowledge. The paper is a useful probe of in-context system adaptation and learned filtering rather than a new hand-derived estimator.

Transformer models have shown great success in natural language processing; however, their potential remains mostly unexplored for dynamical systems. In this work, we investigate the optimal output estimation problem using transformers, which generate output predictions using all the past ones. Particularly, we train the transformer using various distinct systems and then evaluate the performance on unseen systems with unknown dynamics. Empirically, the trained transformer adapts exceedingly well to different unseen systems and even matches the optimal performance given by the Kalman filter for linear systems. In more complex settings with non-i.i.d. noise, time-varying dynamics, and nonlinear dynamics like a quadrotor system with unknown parameters, transformers also demonstrate promising results. To support our experimental findings, we provide statistical guarantees that quantify the amount of training data required for the transformer to achieve a desired excess risk. Finally, we point out some limitations by identifying two classes of problems that lead to degraded performance, highlighting the need for caution when using transformers for control and estimation.

## Introduction

Many control problems such as model predictive control and safety analysis are built upon predictions of system's future trajectories. This prediction (or estimation) problem is well studied and dates back to the classical Kalman filter, which is optimal for linear systems with Gaussian noise. Methods are also developed for more complex setups, e.g. extended Kalman filter for nonlinear systems, particle filters when system dynamics can be sampled, and adaptive filters and adaptive filters for unknown systems.

Prediction, on the other hand, in the domain of natural language processing, has witnessed recent success thanks to the transformer models, which are deep learning architectures that can generate text prediction after feeding into an input text sequence. In this work, we investigate the use of transformers in predicting dynamical system's outputs.

To begin , we assume a priori access to a collection of $M$ systems drawn from some distribution $\mathcal{D}_{sys}$ and their respective output trajectories $\{\mathbf{y}_{t}\}$. These are referred to as source systems and trajectories respectively. We then train a transformer using the source trajectories so that after feeding into past outputs $\mathbf{y}_{0:{t - 1}}$, the transformer is able to produce an estimate ${\hat{\mathbf{y}}}_{t}$ of the true output $\mathbf{y}_{t}$.

## Conclusion

In conclusion, this work has demonstrated the potential of transformers in addressing prediction problems for dynamical systems. The proposed MOP exhibits remarkable performance by adapting to unseen settings, non-i.i.d. noise, and time-varying dynamics.

This work motivates new avenues for the application of transformers in continuous control and dynamical systems. Future work could extend the MOP approach to closed-loop control problems to meta-learn policies for problems such as the optimal quadratic control. It is also of interest to explore new training strategies to promote robustness (e.g., against distribution shifts) and safety of this approach in control problems.
