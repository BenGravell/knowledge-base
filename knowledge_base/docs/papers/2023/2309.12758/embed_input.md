Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms

We establish a collection of closed-loop guarantees and propose a scalable optimization algorithm for distributionally robust model predictive control (DRMPC) applied to linear systems, convex constraints, and quadratic costs. Via standard assumptions for the terminal cost and constraint, we establish distribtionally robust long-term and stage-wise performance guarantees for the closed-loop system. We further demonstrate that a common choice of the terminal cost, i.e., via the discrete-algebraic Riccati equation, renders the origin input-to-state stable for the closed-loop system. This choice also ensures that the exact long-term performance of the closed-loop system is independent of the choice of ambiguity set for the DRMPC formulation. Thus, we establish conditions under which DRMPC does not provide a long-term performance benefit relative to stochastic MPC. To solve the DRMPC optimization problem, we propose a Newton-type algorithm that empirically achieves superlinear convergence and guarantees the feasibility of each iterate. We demonstrate the implications of the closed-loop guarantees and the scalability of the proposed algorithm via two examples....

## Introduction

Model predictive control (MPC) defines an implicit control law via a finite horizon optimal control problem. This optimal control problem is defined by the stage cost $\ell{(x,u)}$, state/input constraints, and a linear discrete-time dynamical model

in which $x$ is the state, $u$ is the manipulated input, and $w$ is the disturbance. The primary difference between variants of MPC (e.g., nominal, robust, and stochastic MPC) is their approach to modeling the disturbance $w$ in the optimization problem.

Σ is large, Σ̂ is poor estimate of Σ
SDP (several QPs)

Table 1. Comparison between R/S/DRMPC with Assumption 3.1.

With some manipulation, we can therefore define

If Assumptions 2.1. ‣ 2. Problem Formulation ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), 2.2. ‣ 2. Problem Formulation ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") and 3.1. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") hold, then $\mathcal{X}$ is RPI for and

Lemma 4.3. ‣ 4.3. Pathwise input-to-state stability ‣ 4. Closed-loop guarantees: Technical proofs ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") ensures that within the terminal region, the DRMPC control law is equivalent to the LQR control law defined in Assumption 3.3. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"). Moreover, this controller is the same regardless of the choice of $d \in \mathcal{D}$ and renders the terminal set RPI....

In nominal MPC, the optimization problem uses a nominal dynamical model, i.e., $w = 0$. Nonetheless, feedback affords nominal MPC a nonzero margin of inherent robustness to disturbances. This nonzero margin, however, may be insufficient in certain safety-critical applications with high uncertainty. Robust MPC (RMPC) and stochastic MPC (SMPC) offer a potential means to improve on the inherent robustness of nominal MPC by characterizing the disturbance and including this information in the optimal control problem.
