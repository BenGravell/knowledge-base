Universal Manipulation Interface: In-The-Wild Robot Teaching without In-The-Wild Robots

Topics include Robotics, Learning, Interface, Universal, Manipulation, UMI.

We present Universal Manipulation Interface (UMI) - a data collection and policy learning framework that allows direct skill transfer from in-the-wild human demonstrations to deployable robot policies. UMI employs hand-held grippers coupled with careful interface design to enable portable, low-cost, and information-rich data collection for challenging bimanual and dynamic manipulation demonstrations. To facilitate deployable policy learning, UMI incorporates a carefully designed policy interface with inference-time latency matching and a relative-trajectory action representation. The resulting learned policies are hardware-agnostic and deployable across multiple robot platforms. Equipped with these features, UMI framework unlocks new robot manipulation capabilities, allowing zero-shot generalizable dynamic, bimanual, precise, and long-horizon behaviors, by only changing the training data for each task. We demonstrate UMI's versatility and efficacy with comprehensive real-world experiments, where policies learned via UMI zero-shot generalize to novel environments and objects when trained on diverse human demonstrations. UMI's hardware and software system is open-sourced at

## Introduction

How should we demonstrate complex manipulation skills for robots to learn from? Attempts in the field have approached this question primarily from two directions: collecting targeted in-the-lab robot datasets via teleoperation or leveraging unstructured in-the-wild human videos. Unfortunately, neither is sufficient, as teleoperation requires high setup costs for hardware and expert operators, while human videos exhibit a large embodiment gap to robots.

Recently, using sensorized hand-held grippers as a data collection interface has emerged as a promising middle-ground alternative -- simultaneously minimizing the embodiment gap while remaining intuitive and flexible. Despite their potential, these approaches still struggle to balance action diversity with transferability. While users can theoretically collect any actions with these hand-held devices, much of that data can not be transferred to an effective robot policy.

With just a wrist-mounted camera on the hand-held gripper, we show that UMI is capable of achieving a wide range of manipulation tasks that involve dynamic, bimanual, precise and long-horizon actions by only changing the training data for each task. Furthermore, when trained with diverse human demonstrations, the final policy exhibits zero-shot generalization to novel environments and objects, achieving a remarkable $70\%$ success rate in out-of-distribution tests, a level of generalizabilty seldomly observed in other behavior cloning frameworks. We open-source the hardware and software system at

## Limitations and Future Works

While UMI demonstrates policy efficacy across a wide range of tasks and scenarios, a few limitations remain. First, since the kinematics limits of the downstream deployment robots are unknown at the time of data collection, we rely on data filtering to ensure the kinematic feasibility of the resulting policy. Future works could develop an embodiment-aware policy learning framework that can transfer skills from valid but hardware-infeasible actions.

Second, our SLAM-based action recovery system inherits visual SLAM's requirement for sufficient texture in the environment. Future works could leverage static third-person-view cameras, coupled with additional fiducial markers on UMI grippers to recover action even in texture-deficient environments like rooms with pure white walls.
