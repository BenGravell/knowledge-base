Pseudo-Simulation for Autonomous Driving

Topics include Autonomous driving, Vehicles, Safety, Causal inference, Datasets, Benchmarks.

Existing evaluation paradigms for Autonomous Vehicles (AVs) face critical limitations. Real-world evaluation is often challenging due to safety concerns and a lack of reproducibility, whereas closed-loop simulation can face insufficient realism or high computational costs. Open-loop evaluation, while being efficient and data-driven, relies on metrics that generally overlook compounding errors. In this paper, we propose pseudo-simulation, a novel paradigm that addresses these limitations. Pseudo-simulation operates on real datasets, similar to open-loop evaluation, but augments them with synthetic observations generated prior to evaluation using 3D Gaussian Splatting. Our key idea is to approximate potential future states the AV might encounter by generating a diverse set of observations that vary in position, heading, and speed. Our method then assigns a higher importance to synthetic observations that best match the AV's likely behavior using a novel proximity-based weighting scheme. This enables evaluating error recovery and the mitigation of causal confusion, as in closed-loop benchmarks, without requiring sequential interactive simulation.

## Introduction

Reliable evaluation is essential for developing decision-making systems. In the context of autonomous vehicles (AVs), this means assessing the system's ability to navigate complex traffic scenarios efficiently, comfortably, and safely. Existing evaluation strategies typically fall into two categories: closed-loop and open-loop evaluation.

To address the limitations of existing evaluation protocols, we introduce pseudo-simulation. This new paradigm aims to combine the scalability of open-loop evaluation with a comprehensive assessment traditionally restricted to interactive closed-loop testing. As shown in Fig. 1, our approach evaluates the AV's performance in two stages. Stage 1 uses the originally recorded real-world observations. Stage 2 uses synthetic observations generated based on these original frames. Crucially, these synthetic observations are generated before the evaluation process begins, enabling evaluation in a non-interactive manner.

We evaluate the output trajectories predicted by the AV, considering its performance on both the initial real-world observations (from Stage 1) and the generated synthetic observations (used in Stage 2). Our key idea lies in how we assess performance in Stage 2: we weight the importance of each synthetic observation based on its proximity to the endpoint of the trajectory that the AV initially predicted in Stage 1 (Fig. 1 bottom-right).

## Conclusion

We introduce pseudo-simulation, a new evaluation paradigm which demonstrates a high correlation to computationally expensive closed-loop simulations. Our experiments show how it better captures crucial aspects of AV evaluation like error recovery than open-loop evaluation. Pseudo-simulation offers significant potential impacts for AV development. It enables more efficient iteration cycles, promotes system robustness by rigorously testing sensitivity to perturbations, and ultimately enhances safety through more comprehensive evaluations.

## Limitations and Future Work

While
