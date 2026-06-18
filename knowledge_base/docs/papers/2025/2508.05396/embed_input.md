Real-Time Iteration Scheme for Diffusion Policy

Topics include Diffusion policy, Real-time iteration, Robotics, Robot manipulation, Diffusion inference, Latency reduction, Discrete actions, Contractivity, Imitation learning, Real-time control.

This preprint transfers the RTI idea from online optimal control to diffusion-policy inference, reusing previous denoising solutions so robots can update actions with less latency. It is conceptually useful in the RTI-MPC cluster because it generalizes the same "one cheap update per cycle" principle to learned policies, including a scaling method for discrete manipulation actions and contractivity conditions for choosing the starting denoising step.

Diffusion Policies have demonstrated impressive performance in robotic manipulation tasks. However, their long inference time, resulting from an extensive iterative denoising process, and the need to execute an action chunk before the next prediction to maintain consistent actions limit their applicability to latency-critical tasks or simple tasks with a short cycle time. While recent methods explored distillation or alternative policy structures to accelerate inference, these often demand additional training, which can be resource-intensive for large robotic models. In this paper, we introduce a novel approach inspired by the Real-Time Iteration (RTI) Scheme, a method from optimal control that accelerates optimization by leveraging solutions from previous time steps as initial guesses for subsequent iterations. We explore the application of this scheme in diffusion inference and propose a scaling-based method to effectively handle discrete actions, such as grasping, in robotic manipulation. The proposed scheme significantly reduces runtime computational costs without the need for distillation or policy redesign....

## INTRODUCTION

Robotic manipulation has seen significant advancements enabled by diffusion models. These models, especially Diffusion Policy (DP) \[\], have demonstrated success in a wide range of tasks, improving control, adaptability, and generalization in complex manipulation scenarios.

However, one main drawback of diffusion models is the slow inference process. Standard diffusion models begin inference from a standard Gaussian distribution and refine it through a denoising process with hundreds of steps. This impedes high-frequency control in demanding tasks, such as contact-rich or high-speed manipulations, which require continuous and timely correction, to prevent irrecoverable errors or even outright failures.

In this paper, we present the Real-Time Iteration Scheme for Diffusion Policy, a simple yet efficient approach to accelerating inference in diffusion-based policies through an informed initialization strategy. Using a reduced number of denoising steps, RTI-DP allows low-latency execution while maintaining good policy performance. Our method can be seamlessly integrated with other pre-trained models, enabling fast inference for large-scale pre-trained robotic models. We provide conditions for the contractivity of denoising dynamics and as potential guidelines for selecting the appropriate number of denoising steps....

Beyond diffusion models, our approach could also benefit flow-based models with denoising components, offering further opportunities to enhance inference speed. Additionally, while our method requires multiple steps for denoising, there remains a potential for one-step denoising without altering the policy structure.

### III-D Local Contractivity of Real-Time Iterations

Formally, let $x_{t}^{\phi} \in \Phi$ denote the trajectory's configuration expressed in a smooth manifold $\Phi$. The consistency constraint is expressed as:

Table II: Image-based Simulation Experiment Results (Max/Average Performance) of DP, SDP, CP, RTI-DP.

The inability to react quickly limits the application of diffusion-based policies in real-world robotics and bottleneck task throughput in repetitive execution. The prolonged waiting time for policies to generate actions results in sluggish, non-smooth robot movements, reducing productivity and making them significantly less responsive compared to human performance....
