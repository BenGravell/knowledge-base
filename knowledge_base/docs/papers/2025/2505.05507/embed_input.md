VIMPPI: Enhancing Model Predictive Path Integral Control with Variational Integration for Underactuated Systems

Topics include Model predictive path integral control, Trajectory optimization, Sampling-based control, Variational integration, Underactuated systems.

Enhances MPPI with variational integration (VI) to accurately simulate the system evolution inside an MPPI over long planning horizons.

This paper presents VIMPPI, a novel control approach for underactuated double pendulum systems developed for the AI Olympics competition. We enhance the Model Predictive Path Integral framework by incorporating variational integration techniques, enabling longer planning horizons without additional computational cost. Operating at 500-700 Hz with control interpolation and disturbance detection mechanisms, VIMPPI substantially outperforms both baseline methods and alternative MPPI implementations.

## Introduction

The AI Olympics with RealAIGym competition challenges participants to develop controllers for complex robotic systems. This year's task focused on designing controllers for underactuated double pendulum systems --- the pendubot and acrobot --- with emphasis on maintaining the upper equilibrium position from various initial states.

Underactuated systems, characterized by fewer control inputs than degrees of freedom, present significant challenges in control engineering. The double pendulum, with its highly nonlinear and chaotic dynamics, serves as an excellent benchmark for evaluating control strategies. Controlling such systems requires balancing computational efficiency with planning accuracy, particularly when dealing with the complex dynamics that emerge from their underactuated nature.

Among sampling-based methods, Model Predictive Path Integral (MPPI) control has emerged as a powerful technique, with successful applications ranging from aggressive vehicle control to various robotic systems. However, computational constraints typically limit the planning horizon in traditional MPPI implementations. Our approach addresses this fundamental limitation by incorporating a variational integrator into the rollout computations, enabling a substantially longer planning horizon without additional computational cost.

## Conclusion

Our VIMPPI controller demonstrated significant performance improvements in the AI Olympics competition. By incorporating a variational integrator into the MPPI framework, we achieved a 4-20x increase in effective planning horizon without additional computational cost. This approach consistently outperformed both alternative MPPI implementations and baseline controllers for both the acrobot and pendubot configurations.

The key innovation --- replacing standard numerical integration with variational integration in the MPPI rollout --- offers an efficient solution for controlling highly dynamic systems without requiring complex reward engineering or system identification. The results highlight the importance of numerical integration methods in sampling-based control approaches, an aspect that has received relatively little attention in the literature.
