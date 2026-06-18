Universal Manipulation Interface: In-The-Wild Robot Teaching without In-The-Wild Robots

Topics include Robotics, Learning, Interface, Universal, Manipulation, UMI.

We present Universal Manipulation Interface (UMI) - a data collection and policy learning framework that allows direct skill transfer from in-the-wild human demonstrations to deployable robot policies. UMI employs hand-held grippers coupled with careful interface design to enable portable, low-cost, and information-rich data collection for challenging bimanual and dynamic manipulation demonstrations. To facilitate deployable policy learning, UMI incorporates a carefully designed policy interface with inference-time latency matching and a relative-trajectory action representation. The resulting learned policies are hardware-agnostic and deployable across multiple robot platforms. Equipped with these features, UMI framework unlocks new robot manipulation capabilities, allowing zero-shot generalizable dynamic, bimanual, precise, and long-horizon behaviors, by only changing the training data for each task. We demonstrate UMI's versatility and efficacy with comprehensive real-world experiments, where policies learned via UMI zero-shot generalize to novel environments and objects when trained on diverse human demonstrations. UMI's hardware and software system is open-sourced at

## Introduction

How should we demonstrate complex manipulation skills for robots to learn from? Attempts in the field have approached this question primarily from two directions: collecting targeted in-the-lab robot datasets via teleoperation or leveraging unstructured in-the-wild human videos. Unfortunately, neither is sufficient, as teleoperation requires high setup costs for hardware and expert operators, while human videos exhibit a large embodiment gap to robots.

Recently, using sensorized hand-held grippers as a data collection interface has emerged as a promising middle-ground alternative -- simultaneously minimizing the embodiment gap while remaining intuitive and flexible. Despite their potential, these approaches still struggle to balance action diversity with transferability. While users can theoretically collect any actions with these hand-held devices, much of that data can not be transferred to an effective robot policy....

## Conclusion

We present Universal Manipulation Interface (UMI), a framework that enables learning capable and generalizable manipulation policies directly from in-the-wild human demonstrations. The UMI gripper, a hand-held demonstration interface, captures sufficient information to learn some challenging manipulation tasks, including washing a dirty dish, bimanual sweater folding, and dynamic object tossing and sorting. At the same time, UMI remains highly scalable for in-the-wild data collection with its portability, cost-effectiveness, and operational simplicity....

During execution, the UMI policy predicts the action sequence starting at the last step of observation $t_{obs}$. The first few actions predicted are immediately outdated due to observation latency $t_{input} - t_{obs}$, policy inference latency $t_{output} - t_{input}$ and execution latency $t_{act} - t_{output}$. We simply discard the outdated actions and only execute actions with the desired timestamp after $t_{act}$ for each hardware.

Mechanical robustness. Because the camera is mechanically fixed relative to the fingers, mounting UMI on robots does not require camera-robot-world calibration. Hence, the system is much more robust to mechanical shocks, making it easy to deploy.

No Fisheye lens [\[HD2\]]: To ablate the importance of having a wide field-of-view (FoV) Fisheye lens, we post-processed the dataset by rectifying and cropping each image...
