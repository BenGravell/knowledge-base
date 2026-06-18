LeARN: Learnable and Adaptive Representations for Nonlinear Dynamics in System Identification

Topics include Robustness, System identification, Neural networks, Attention mechanisms, Meta-learning, Datasets, Online algorithms, Generalization, Learning, LeARN, DNN, Nonlinear systems, Nonlinear system identification.

System identification, the process of deriving mathematical models of dynamical systems from observed input-output data, has undergone a paradigm shift with the advent of learning-based methods. Addressing the intricate challenges of data-driven discovery in nonlinear dynamical systems, these methods have garnered significant attention. Among them, Sparse Identification of Nonlinear Dynamics (SINDy) has emerged as a transformative approach, distilling complex dynamical behaviors into interpretable linear combinations of basis functions. However, SINDy relies on domain-specific expertise to construct its foundational "library" of basis functions, which limits its adaptability and universality. In this work, we introduce a nonlinear system identification framework called LeARN that transcends the need for prior domain knowledge by learning the library of basis functions directly from data. To enhance adaptability to evolving system dynamics under varying noise conditions, we employ a novel meta-learning-based system identification approach that uses a lightweight deep neural network (DNN) to dynamically refine these basis functions.

## INTRODUCTION

Robustness of robotic systems in unstructured environments requires adaptive control laws, yet their efficacy is fundamentally contingent upon the accuracy of the underlying plant model. Historically, these models have relied on physics-based equations to ensure reliability and physical interpretability under ideal conditions.

Complex nonlinear dynamics: Many robotic systems operate in high-dimensional spaces with nonlinear interactions, making precise modeling difficult.

Unknown or un-modeled dynamics: Environmental disturbances and uncertainties often introduce dynamics that are challenging to capture using predefined equations.

High-dimensional inputs: Robots with numerous sensors and actuators generate large-scale data that physics-based models may struggle to incorporate.

Unlike traditional SINDy, our method does not require a predefined function library, thus enhancing flexibility and eliminating the need for domain expertise.

In this paper, we test our approach on the Neural Fly dataset, which provides a challenging benchmark for nonlinear system identification. Therefore, throughout the paper, our principal robotic system of interest for the demonstration of our framework will be a quadrotor.

## Conclusion

In this work, we introduced LeARN, a novel algorithm for meta-learning the basis functions for nonlinear system identification. Our proposed approach demonstrates significant adaptability and generalization capabilities in modeling dynamical systems, as evidenced by its performance on unseen wind conditions in the Neural Fly dataset. Unlike the SINDy algorithm, our approach learns the library of basis functions directly from the data. The proposed algorithm yields a parameterized basis function library optimized for adaptability to new, unseen environments.

Looking ahead, our study sets the groundwork for addressing the broader goal of enabling robots to autonomously model and adapt to dynamic unstructured environments. Furthermore, our approach paves the way for developing robust, versatile, and adaptive robotic systems capable of operating safely and effectively in the real-world where such approaches can be utilized for health monitoring of these systems via data-driven system identification.
