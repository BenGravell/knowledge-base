LeARN: Learnable and Adaptive Representations for Nonlinear Dynamics in System Identification

Topics include Robustness, System identification, Neural networks, Attention mechanisms, Meta-learning, Datasets, Online algorithms, Generalization, Learning, LeARN, DNN, Nonlinear systems, Nonlinear system identification.

System identification, the process of deriving mathematical models of dynamical systems from observed input-output data, has undergone a paradigm shift with the advent of learning-based methods. Addressing the intricate challenges of data-driven discovery in nonlinear dynamical systems, these methods have garnered significant attention. Among them, Sparse Identification of Nonlinear Dynamics (SINDy) has emerged as a transformative approach, distilling complex dynamical behaviors into interpretable linear combinations of basis functions. However, SINDy relies on domain-specific expertise to construct its foundational "library" of basis functions, which limits its adaptability and universality. In this work, we introduce a nonlinear system identification framework called LeARN that transcends the need for prior domain knowledge by learning the library of basis functions directly from data. To enhance adaptability to evolving system dynamics under varying noise conditions, we employ a novel meta-learning-based system identification approach that uses a lightweight deep neural network (DNN) to dynamically refine these basis functions....

## INTRODUCTION

Robustness of robotic systems in unstructured environments requires adaptive control laws, yet their efficacy is fundamentally contingent upon the accuracy of the underlying plant model. Historically, these models have relied on physics-based equations to ensure reliability and physical interpretability under ideal conditions. However, such models face critical limitations:

Complex nonlinear dynamics: Many robotic systems operate in high-dimensional spaces with nonlinear interactions, making precise modeling difficult.

In this work, we introduced LeARN, a novel algorithm for meta-learning the basis functions for nonlinear system identification. Our proposed approach demonstrates significant adaptability and generalization capabilities in modeling dynamical systems, as evidenced by its performance on unseen wind conditions in the Neural Fly dataset. Unlike the SINDy algorithm, our approach learns the library of basis functions directly from the data. The proposed algorithm yields a parameterized basis function library optimized for adaptability to new, unseen environments....

Looking ahead, our study sets the groundwork for addressing the broader goal of enabling robots to autonomously model and adapt to dynamic unstructured environments. Furthermore, our approach paves the way for developing robust, versatile, and adaptive robotic systems capable of operating safely and effectively in the real-world where such approaches can be utilized for health monitoring of these systems via data-driven system identification.

Figure 1: For a concatenated feature vector X ∈ ℝ1 × (I+U) of the form, $X = \begin{bmatrix}
\end{bmatrix}$, where x ∈ ℝ1 × I is the state feature vector and u ∈ ℝ1 × U is the control input corresponding to x, Θ (X;ψ) ∈ ℝ1 × P (I+U) is the learned basis function library for a total of P basis functions, where mp represents the pt h basis function and ℰ (X;ϕ) ∈ ℝI × P (I+U) is the learned feature selection matrix, for a total of n = I sets of coefficients, ek ∈ ℝ1 × (P+U) is coefficient for kt h state feature in X.

where the global position vector $p \in {\mathbb{R}}^{3}$, velocity vector $v \in {\mathbb{R}}^{3}$, attitude rotation matrix $R \in {{\mathbf{S}\mathbf{O}}{(\mathbf{3})}}$ and body angular velocity $\omega \in {\mathbb{R}}^{3}$ give the states of the quadrotor....
