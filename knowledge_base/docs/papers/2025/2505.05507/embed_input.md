VIMPPI: Enhancing Model Predictive Path Integral Control with Variational Integration for Underactuated Systems

Topics include Model predictive path integral control, Trajectory optimization, Sampling-based control, Variational integration, Underactuated systems.

Enhances MPPI with variational integration (VI) to accurately simulate the system evolution inside an MPPI over long planning horizons.

This paper presents VIMPPI, a novel control approach for underactuated double pendulum systems developed for the AI Olympics competition. We enhance the Model Predictive Path Integral framework by incorporating variational integration techniques, enabling longer planning horizons without additional computational cost. Operating at 500-700 Hz with control interpolation and disturbance detection mechanisms, VIMPPI substantially outperforms both baseline methods and alternative MPPI implementations.

## Introduction

The AI Olympics with RealAIGym \[\] competition challenges participants to develop controllers for complex robotic systems. This year's task focused on designing controllers for underactuated double pendulum systems --- the pendubot and acrobot --- with emphasis on maintaining the upper equilibrium position from various initial states \[\].

Underactuated systems, characterized by fewer control inputs than degrees of freedom, present significant challenges in control engineering. The double pendulum, with its highly nonlinear and chaotic dynamics, serves as an excellent benchmark for evaluating control strategies. Controlling such systems requires balancing computational efficiency with planning accuracy, particularly when dealing with the complex dynamics that emerge from their underactuated nature.

The key innovation --- replacing standard numerical integration with variational integration in the MPPI rollout --- offers an efficient solution for controlling highly dynamic systems without requiring complex reward engineering or system identification. The results highlight the importance of numerical integration methods in sampling-based control approaches, an aspect that has received relatively little attention in the literature.

Future work will focus on applying this technique to more complex robotic systems such as humanoid robots, quadrupeds, and multi-link manipulators, and exploring hybrid approaches that combine our method with learning-based techniques. We believe that the principles demonstrated in this work have broad applicability across robotics and control, particularly for systems where accurate long-term prediction is essential for effective control.

By iterating this process, the initial configuration guess converges to an accurate solution that preserves the system's conservative properties. For our double pendulum system, we found that a single error correction iteration is typically sufficient, as subsequent error magnitudes become negligibly small. This makes the computational overhead of the variational integrator minimal compared to the benefits it provides in simulation accuracy and stability.

In our implementation, we employ the Discrete Euler-Lagrange residual in Momentum form. This formulation allows us to work with momentum equations and accurately estimate the next configuration step in MPPI rollouts....
