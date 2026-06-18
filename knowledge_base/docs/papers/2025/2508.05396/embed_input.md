Real-Time Iteration Scheme for Diffusion Policy

Topics include Diffusion policy, Real-time iteration, Robotics, Robot manipulation, Diffusion inference, Latency reduction, Discrete actions, Contractivity, Imitation learning, Real-time control.

This preprint transfers the RTI idea from online optimal control to diffusion-policy inference, reusing previous denoising solutions so robots can update actions with less latency. It is conceptually useful in the RTI-MPC cluster because it generalizes the same "one cheap update per cycle" principle to learned policies, including a scaling method for discrete manipulation actions and contractivity conditions for choosing the starting denoising step.

Diffusion Policies have demonstrated impressive performance in robotic manipulation tasks. However, their long inference time, resulting from an extensive iterative denoising process, and the need to execute an action chunk before the next prediction to maintain consistent actions limit their applicability to latency-critical tasks or simple tasks with a short cycle time. While recent methods explored distillation or alternative policy structures to accelerate inference, these often demand additional training, which can be resource-intensive for large robotic models. In this paper, we introduce a novel approach inspired by the Real-Time Iteration (RTI) Scheme, a method from optimal control that accelerates optimization by leveraging solutions from previous time steps as initial guesses for subsequent iterations. We explore the application of this scheme in diffusion inference and propose a scaling-based method to effectively handle discrete actions, such as grasping, in robotic manipulation. The proposed scheme significantly reduces runtime computational costs without the need for distillation or policy redesign.

## INTRODUCTION

Robotic manipulation has seen significant advancements enabled by diffusion models. These models, especially Diffusion Policy (DP), have demonstrated success in a wide range of tasks, improving control, adaptability, and generalization in complex manipulation scenarios.

In this paper, we propose a real-time method, Real-Time Iteration for Diffusion Policy (RTI-DP) that requires neither retraining nor distillation. Our approach is inspired by the Real-Time Iteration Scheme in optimal control, which leverages predictions from previous steps as initialization for the next step, significantly accelerating optimization. Specifically, our method first computes an initial action chunk using the same approach as the standard diffusion policy. For subsequent action chunks, it utilizes the previous one as an initial guess and applies denoising on top of it with a reduced number of time steps.

We propose a real-time inference method that leverages the initial guess from the previous prediction, enabling direct application to pre-trained models.

We show the proposed method can empirically boost the real-time performance in various manipulation tasks through simulation experiments.

## DISCUSSION

RTI-DP offers a clear advantage over existing approaches by achieving substantial speedups without compromising performance, or requiring retraining, making it well-suited for real-time robotic applications. Beyond diffusion models, similar improvements could extend to flow-based models with a denoising component, further reducing computational overhead while maintaining expressive power. Future research could investigate how to integrate optimized initialization techniques with flow-based models, which might achieve even greater speedups than diffusion models, particularly given their inherent smoothness.

While fast inference offers many advantages, some dynamical systems with minimal environmental disturbances---such as static tasks like picking up a cup---do not necessarily benefit from speed improvements, as execution time is not a limiting factor. However, the efficiency of our method creates a larger time budget for prediction with less powerful GPUs. This, in turn, could potentially lower the hardware requirements for visuomotor policies and deployment in edge devices without needing additional training.
