Probably Approximately Correct Nonlinear Model Predictive Control (PAC-NMPC)

Topics include Model predictive control, Predictive control, Nonlinear model predictive control, Stochastic model predictive control, Vehicles, Safety, Uncertainty, Real-time systems, Online algorithms, Sampling-based methods, Sample complexity, Control, Sampling, Probably approximately correct, PAC-NMPC, SNMPC, Uncrewed aerial vehicle.

Approaches for stochastic nonlinear model predictive control (SNMPC) typically make restrictive assumptions about the system dynamics and rely on approximations to characterize the evolution of the underlying uncertainty distributions. For this reason, they are often unable to capture more complex distributions (e.g., non-Gaussian or multi-modal) and cannot provide accurate guarantees of performance. In this paper, we present a sampling-based SNMPC approach that leverages recently derived sample complexity bounds to certify the performance of a feedback policy without making assumptions about the system dynamics or underlying uncertainty distributions. By parallelizing our approach, we are able to demonstrate real-time receding-horizon SNMPC with statistical safety guarantees in simulation and on hardware using a 1/10th scale rally car and a 24-inch wingspan fixed-wing unmanned aerial vehicle (UAV).

## Introduction

Nonlinear model predictive control (NMPC) has proven to be a powerful approach for controlling high-dimensional, complex robotic systems (e.g., ). Nevertheless, although these methods can handle large state spaces, nonlinear dynamics, and system constraints, their performance can be adversely affected by the presence of uncertainty even in the context of real-time replanning. A number of approaches have been proposed to compensate for this marginal robustness, the simplest of which is to generate a feedback policy to track the current receding-horizon plan (e.g., ).

In this paper, we present a sampling-based SNMPC algorithm capable of controlling stochastic dynamical systems without applying limiting assumptions to the structure of the stochastic dynamics or underlying uncertainty distributions. In addition, our approach leverages recently derived sample complexity bounds to provide a probabilistic guarantee on system performance. Our algorithm builds on Probably Approximately Correct Robust Policy Search (PROPS) to directly optimize an upper confidence bound on the expected cost and the probability of constraint violation for a receding-horizon feedback policy.

A novel algorithm, PAC-NMPC, for receding horizon SNMPC with probabilistic performance guarantees.

A real-time implementation via GPU acceleration.

Demonstration of our algorithm on complex underactuated systems via simulation and hardware experiments.

## Discussion

In this work, we presented a novel SNMPC method capable of propagating uncertainty through arbitrary nonlinear dynamic systems and of providing statistical guarantees on expected cost and constraint violations. We demonstrated real time performance both in simulation and on-board physical hardware. Further, we show that the algorithm is capable of scaling to more complex systems, like fixed-wing UAVs. Since this algorithm can be used with "black-box" sampling of dynamics (assuming they are continuously differentiable), costs, constraints, and noise, future work can investigate its use with learned dynamics and perception-informed costs.
