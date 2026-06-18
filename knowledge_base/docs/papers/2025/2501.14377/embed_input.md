Dream to Fly: Model-Based Reinforcement Learning for Vision-Based Drone Flight

Topics include Model-based reinforcement learning, DreamerV3, Drone racing, Vision-based control, Pixel-to-control, Quadrotors, Robot learning.

Applies DreamerV3 to train a drone-racing policy directly from camera pixels, reducing reliance on hand-crafted intermediate perception or imitation bootstrapping. The key result is that model-based RL can learn visuomotor flight behaviors efficient enough to deploy on real quadrotors through hardware-in-the-loop transfer.

Autonomous drone racing has risen as a challenging robotic benchmark for testing the limits of learning, perception, planning, and control. Expert human pilots are able to fly a drone through a race track by mapping pixels from a single camera directly to control commands. Recent works in autonomous drone racing attempting direct pixel-to-commands control policies have relied on either intermediate representations that simplify the observation space or performed extensive bootstrapping using Imitation Learning (IL). This paper leverages DreamerV3 to train visuomotor policies capable of agile flight through a racetrack using only pixels as observations. In contrast to model-free methods like PPO or SAC, which are sample-inefficient and struggle in this setting, our approach acquires drone racing skills from pixels. Notably, a perception-aware behaviour of actively steering the camera toward texture-rich gate regions emerges without the need of handcrafted reward terms for the viewing direction.

## INTRODUCTION

In recent years, quadrotors have become a central focus of robotics research, emerging as versatile platforms with untapped potential across multiple domains, including search and rescue, inspection, agriculture, cinematography, delivery, passenger air vehicles, space exploration \[22: practical aspects, applications, open challenges, security issues, and future trends")\] and drone racing.

Traditionally, most autonomous drone racing systems have relied on explicit state estimation integrating data from inertial measurement units (IMUs) and other onboard sensors to maintain stability and optimize performance.

However, professional human pilots rely solely on visual feedback from a single onboard camera, showcasing a remarkable ability to navigate complex environments purely from visual inputs. Emulating this human ability to fly based solely on visual information remains a significant challenge for autonomous systems.

Our approach demonstrates that the learned policy effectively controls real-world dynamics directly from rendered pixel observations, and further validates the applicability and potential of MBRL for real-world mobile robotic tasks.

## Conclusion

This paper presented a MBRL approach using DreamerV3 to train end-to-end visuomotor policies for agile drone flight. Our method learns directly from raw pixel inputs, removing the need for intermediate representations or imitation learning bootstrapping. Our experiments demonstrated that this approach is more sample-efficient than model-free baselines like PPO and SAC and results in emergent perception-aware behaviors without explicit reward shaping.

We validated the learned policies in simulation and on a physical quadrotor using a hardware-in-the-loop (HIL) setup. While this confirms the policy's effectiveness on the real quadrotor dynamics, additional challenges remain to transfer to real camera pixel observations. Additionally, the training process is computationally intensive, requiring approximately 240 hours to converge. Future work should focus on using photorealistic simulators or exploring other observation modalities that allow for deployment directly real pixels, and on improving the computational efficiency of the world model.
