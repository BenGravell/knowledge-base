FlowMP: Learning Motion Fields for Robot Planning with Conditional Flow Matching

Topics include Motion planning, Robotics, Diffusion models, Benchmarks, Planning, Learning, FlowMP.

Prior flow matching methods in robotics have primarily learned velocity fields to morph one distribution of trajectories into another. In this work, we extend flow matching to capture second-order trajectory dynamics, incorporating acceleration effects either explicitly in the model or implicitly through the learning objective. Unlike diffusion models, which rely on a noisy forward process and iterative denoising steps, flow matching trains a continuous transformation (flow) that directly maps a simple prior distribution to the target trajectory distribution without any denoising procedure. By modeling trajectories with second-order dynamics, our approach ensures that generated robot motions are smooth and physically executable, avoiding the jerky or dynamically infeasible trajectories that first-order models might produce. We empirically demonstrate that this second-order conditional flow matching yields superior performance on motion planning benchmarks, achieving smoother trajectories and higher success rates than baseline planners....

## Introduction

Motion planning is a fundamental problem in robotics, and its applications range from autonomous navigation to robotic manipulation. As robots are deployed in increasingly complex and dynamic environments, generating collision-free, smooth, and dynamically feasible trajectories is crucial for reliable operation. Traditional motion planning methods can be broadly classified into sampling-based and optimization-based approaches....

Figure 1: Executions of a smooth, dynamically feasible motion on a Kinova Gen3 manipulator. The same start and goal configurations can yield multiple valid solutions when sampling from our flow matching framework, demonstrating its ability to capture different modes of the trajectory distribution.

## Conclusions

We introduced FlowMP---a framework that leverages conditional flow matching to learn motion fields for generating smooth and dynamically feasible trajectories. Using flow matching to encode trajectory distribution and capture second-order trajectory dynamics, our approach directly models acceleration profiles alongside velocity, ensuring physically executable trajectories without requiring iterative denoising steps. Through evaluations, FlowMP demonstrated superior performance over MPD and bare trajectory optimizer in terms of trajectory quality, inference speed, and planning feasibility across both planar and robot environments....

With the jerk field $\mathbf{w} = {{6{({\mathbf{q}_{1} - \varepsilon_{\mathbf{q}}})}} - {6\varepsilon_{\overset{˙}{\mathbf{q}}}} - {3\varepsilon_{\overset{¨}{\mathbf{q}}}}}$ that learns the path acceleration is derived, the time-differentiable interpolation is, therefore, given as:

The optimal via-points $\mathbf{q}_{\text{via}}$ for smooth and task-specific trajectories are optimized via the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) algorithm \[\] by searching the via-point space and iteratively sampling candidate via-points from a Gaussian distribution $\mathcal{N}{(\mu_{\text{via}},\mathbf{\Sigma}_{\text{via}})}$, where $\mu_{\text{via}}$ is the mean and $\mathbf{\Sigma}_{\text{via}}$ is the covariance matrix. Each sampled set of via-points generates a trajectory through the parameterization in Eq. and is evaluated using the cost function in Eq.....

TABLE I: Planning feasibility of FlowMP, Stoch-GPMP, and MPD in RobotPointMass environments.
