Pseudo-Simulation for Autonomous Driving

Topics include Autonomous driving, Vehicles, Safety, Causal inference, Datasets, Benchmarks.

Existing evaluation paradigms for Autonomous Vehicles (AVs) face critical limitations. Real-world evaluation is often challenging due to safety concerns and a lack of reproducibility, whereas closed-loop simulation can face insufficient realism or high computational costs. Open-loop evaluation, while being efficient and data-driven, relies on metrics that generally overlook compounding errors. In this paper, we propose pseudo-simulation, a novel paradigm that addresses these limitations. Pseudo-simulation operates on real datasets, similar to open-loop evaluation, but augments them with synthetic observations generated prior to evaluation using 3D Gaussian Splatting. Our key idea is to approximate potential future states the AV might encounter by generating a diverse set of observations that vary in position, heading, and speed. Our method then assigns a higher importance to synthetic observations that best match the AV's likely behavior using a novel proximity-based weighting scheme. This enables evaluating error recovery and the mitigation of causal confusion, as in closed-loop benchmarks, without requiring sequential interactive simulation....

## Introduction

Reliable evaluation is essential for developing decision-making systems. In the context of autonomous vehicles (AVs), this means assessing the system's ability to navigate complex traffic scenarios efficiently, comfortably, and safely. Existing evaluation strategies typically fall into two categories: closed-loop and open-loop evaluation.

Closed-loop evaluation assesses model performance by placing it in an interactive environment. The AV must safely navigate traffic while making progress toward a designated goal. Although real-world closed-loop deployment offers reliable feedback, it is costly, risky, and not reproducible, making it insufficient on its own for benchmarking at the scale needed to demonstrate robustness. As a more reproducible alternative, closed-loop evaluation is often conducted in simulation....

Human Flag Filtering. Our filtering strategy disregards rule violations also committed by human experts. While this helps reduce false positives, it could also risk overlooking important failure and edge cases, since human driving is not always a gold standard for safety. Future work could further refine the human flag filtering and explore this trade-off to ensure more reliable evaluation.

Metric Design Choices. We choose multiplicative aggregation because most sub-scores are binary-valued, and multiplication captures compounding failures, e.g., a collision should significantly impact the final score. Our Gaussian weighting is selected for its strong empirical performance with minimal assumptions. Exploring more principled formulations for aggregation and weighting remains an interesting future direction.

### How well-aligned is pseudo-simulation with closed-loop evaluation?

Here, $\mathcal{M}_{\text{pen}} = {\{\text{NC},\text{DAC},\text{DDC},\text{TLC}\}}$ and $\mathcal{M}_{\text{avg}} = {\{\text{TTC},\text{EP},\text{HC},\text{LK},\text{EC}\}}$ (Table 1). Unlike prior work, to prevent penalizing contextually justified maneuvers, we introduce a novel filtering mechanism ($\text{filter}_{m}$) for the EPDMS. If a rule violation is also committed by the human expert driver in the same scene, the penalty is ignored. This avoids penalizing infractions due to label noise or valid behaviors, such as briefly entering the opposite lane to bypass a static obstacle.

### What new challenges and insights does our leaderboard provide?
