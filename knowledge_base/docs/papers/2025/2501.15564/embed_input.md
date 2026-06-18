Diffusion-Based Planning for Autonomous Driving with Flexible Guidance

Achieving human-like driving behaviors in complex open-world environments is a critical challenge in autonomous driving. Contemporary learning-based planning approaches such as imitation learning methods often struggle to balance competing objectives and lack of safety assurance,due to limited adaptability and inadequacy in learning complex multi-modal behaviors commonly exhibited in human planning, not to mention their strong reliance on the fallback strategy with predefined rules. We propose a novel transformer-based Diffusion Planner for closed-loop planning, which can effectively model multi-modal driving behavior and ensure trajectory quality without any rule-based refinement. Our model supports joint modeling of both prediction and planning tasks under the same architecture, enabling cooperative behaviors between vehicles. Moreover, by learning the gradient of the trajectory score function and employing a flexible classifier guidance mechanism, Diffusion Planner effectively achieves safe and adaptable planning behaviors.

## Introduction

Autonomous driving as a cornerstone technology, is poised to usher transportation into a safer and more efficient era of mobility. The key challenge is achieving human-like driving behaviors in complex open-world environment, while ensuring safety, efficiency, and comfort. Rule-based planning methods have demonstrated initial success in industrial applications, by defining driving behaviors and establishing boundaries derived from human knowledge. However, their reliance on predefined rules limits adaptability to new traffic situations, and modifying rules demands extensive engineering effort.

Though promising, current learning-based planning methods still face several limitations. Firstly, human drivers often exhibit multi-modal behaviors in planning scenarios. Existing methods that rely on behavior cloning lack a guarantee of fitting such complex data distributions, even when utilizing large transformer-based model architecture or sampling multiple trajectories.

In this study, we discover that diffusion model possesses huge potential to address the aforementioned issues. Its ability to model complex data distributions allows for effective capturing of multi-modal human driving behavior. Additionally, the high-quality generation capability of the diffusion model also provides opportunities for improving the output trajectory quality through appropriate structural design, removing the reliance on rule-based refinement. The best part of diffusion lies in its flexible guidance mechanism, which allows adaptation to various planning behavioral needs without additional training.

We demonstrate that our model can achieve personalized driving behavior at runtime by utilizing a flexible guidance mechanism, which is a desirable feature for real-world applications.

## Conclusion

We propose Diffusion Planner, a learning-based approach that fully exploits the expressive power and flexible guidance mechanism of diffusion models for high-quality autonomous planning. A transformer-based architecture is introduced to jointly model the multi-modal data distribution in motion prediction and planning tasks through a diffusion objective. Classifier guidance is employed to align planning behavior with safe or user preferred driving styles.
