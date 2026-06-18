Data-enabled Policy Optimization for the Linear Quadratic Regulator

Policy optimization (PO), an essential approach of reinforcement learning for a broad range of system classes, requires significantly more system data than indirect (identification-followed-by-control) methods or behavioral-based direct methods even in the simplest linear quadratic regulator (LQR) problem. In this paper, we take an initial step towards bridging this gap by proposing the data-enabled policy optimization (DeePO) method, which requires only a finite number of sufficiently exciting data to iteratively solve the LQR problem via PO. Based on a data-driven closed-loop parameterization, we are able to directly compute the policy gradient from a batch of persistently exciting data. Next, we show that the nonconvex PO problem satisfies a projected gradient dominance property by relating it to an equivalent convex program, leading to the global convergence of DeePO. Moreover, we apply regularization methods to enhance certainty-equivalence and robustness of the resulting controller and show an implicit regularization property. Finally, we perform simulations to validate our results.

## Introduction

As a cornerstone of modern control theory, the linear quadratic regulator (LQR) problem has been the benchmark for data-driven control methods that seek to design a controller from raw system data. The manifold approaches to data-driven control can be broadly categorized as indirect (when identifying a dynamical model followed by model-based control design) versus direct (when bypassing the identification step). The use of direct data-driven control is usually motivated when the dynamical model is difficult to establish, or is too complex for model-based control design....

A representative instance of direct data-driven control is policy optimization (PO), an essential approach for applications of reinforcement learning (RL). As an iterative method, PO directly searches over the policy space to optimize a performance metric of interest. Based on zeroth-order optimization techniques, it uses multiple system trajectories to estimate the policy gradient. There has been a resurgent interest in studying theoretical properties of PO on the LQR problem such as convergence and sample complexity; see e.g., and the comprehensive survey....

In this paper, we have proposed the DeePO method that only requires a finite number of PE data to solve the LQR problem. By relating the nonconvex optimization problem to a convex program, we have shown the global convergence of DeePO. Furthermore, we have shown that the regularization method can be applied to enhance certainty-equivalence and robust stability without affecting its convergence. The implicit regularization property has also provided an insightful understanding on the optimization landscape of DeePO.

In future, it would be valuable to discover a strongly convex reparameterization of, which may improve the sublinear convergence rate to linear. It would also be interesting to study DeePO in a more general setting, e.g., the LQR with noisy inputs. Since DeePO is an efficient iterative method, it is expected to be able to applied to online control, where the control performance is constantly improved by collecting more real-time data. We are also hopeful that it can be used to solve the adaptive LQR for time-varying systems.

Those bounds are also true for $L^{\ast},\Sigma^{\ast}$. Furthermore, we can provide an upper bound of $\mu{(a)}$ as

### Lemma 2

### IV-A Certainty-equivalence regularizer
