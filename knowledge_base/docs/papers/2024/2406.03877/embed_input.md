Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving

In an era marked by the rapid scaling of foundation models, autonomous driving technologies are approaching a transformative threshold where end-to-end autonomous driving (E2E-AD) emerges due to its potential of scaling up in the data-driven manner. However, existing E2E-AD methods are mostly evaluated under the open-loop log-replay manner with L2 errors and collision rate as metrics (e.g., in nuScenes), which could not fully reflect the driving performance of algorithms as recently acknowledged in the community. For those E2E-AD methods evaluated under the closed-loop protocol, they are tested in fixed routes (e.g., Town05Long and Longest6 in CARLA) with the driving score as metrics, which is known for high variance due to the unsmoothed metric function and large randomness in the long route. Besides, these methods usually collect their own data for training, which makes algorithm-level fair comparison infeasible. To fulfill the paramount need of comprehensive, realistic, and fair testing environments for Full Self-Driving (FSD), we present Bench2Drive, the first benchmark for evaluating E2E-AD systems' multiple abilities in a closed-loop manner....

## Introduction

^††^footnotetext: This work was in part supported by by NSFC and Shanghai Municipal Science and Technology Major Project under Grant 2021SHZDZX0102.

In recent years, the field of autonomous driving has witnessed tremendous growth, fueled by the rapid advancement and scaling of foundation models. These developments have ushered in a new era of end-to-end autonomous driving (E2E-AD) systems, which promise a scalable, data-driven approach to vehicle automation, opposed to traditional module-based perception, prediction, planning pipeline. Such systems are designed to be capable of learning from vast amounts of data, potentially transforming the landscape of vehicle intelligence.

Generative models like diffusion models \[\] might have the potential to provide realistic and reactive rendering, with some pioneering works in the field. However, the illusion and artifact issue of diffusion requires further exploration.

Social Impact: The deployment of AD systems holds immense potential to revolutionize transportation, but it also brings significant ethical and safety concerns. Bench2Drive could serve as a platform for rigorously validating the capabilities of AD systems in a controlled and simulated environment, helping to identify potential flaws before real-world deployment. One of the primary risks is the simulation-reality gap---the difference between how an AD system performs in simulation versus in the real world. Simulations have the difficulties to fully replicate the complexities and unpredictability of real-world driving conditions....

### Multi-Ability Evaluation

6x Camera: Surround coverage, 900x1600 resolution, JPEG compression (quality-level 20)

In nuPlan, smoothness is determined by frame-by-frame evaluation of these variables over the entire trajectory, which makes it susceptible to local driving behaviors. For example, if a vehicle ahead suddenly brakes, the ego vehicle must also brake abruptly to avoid a collision. Even if the ego's hard brake behavior is appropriate in this case and its driving is smooth at other times, the entire trajectory could still be judged as unsmooth, leading to unreasonable evaluation results. To mitigate this issue, we segment the entire trajectory at a timestep interval $n = 20$ for evaluation.
