The Waymo Open Sim Agents Challenge

Topics include Autonomous driving, Vehicles, WOSAC.

Simulation with realistic, interactive agents represents a key task for autonomous vehicle software development. In this work, we introduce the Waymo Open Sim Agents Challenge (WOSAC). WOSAC is the first public challenge to tackle this task and propose corresponding metrics. The goal of the challenge is to stimulate the design of realistic simulators that can be used to evaluate and train a behavior model for autonomous driving. We outline our evaluation methodology, present results for a number of different baseline simulation agent methods, and analyze several submissions to the 2023 competition which ran from March 16, 2023 to May 23, 2023. The WOSAC evaluation server remains open for submissions and we discuss open problems for the task.

## Introduction

Simulation environments allow cheap and fast evaluation of autonomous driving behavior systems, while also reducing the need to deploy potentially risky software releases to physical systems. While generation of synthetic sensor data was an early goal Pomerleau; Dosovitskiy et al. of simulation, use cases have evolved as perception systems have matured. Today, one of the most promising use cases for simulation is system safety validation via statistical model checking Corso et al.; Agha and Palmskog with Monte Carlo trials involving realistically modeled traffic participants, i.e., *simulation agents*.

Figure 1: WOSAC models the simulation problem as simulation of mid-level object representations, rather than as sensor simulation.

### Conclusion

In this work, we have introduced a new challenge for evaluation of simulation agents, explaining the rationale for the different criteria we require. We invite the research community to continue to participate.

However, there are two problems with trying to minimize Equation 2 exactly in our problem setting. First, $o_{\geq 1}$ is high-dimensional. Instead of trying to parameterize the entire ground truth scenario and compute its NLL under a simulated distribution, we therefore parameterize scenarios with a smaller number of component metrics (see Section 4.2.1) and aggregate them together into a composite NLL metric (see Section 4.2.2). Second, agents may support sampling but not pointwise likelihood estimation Nowozin et al.....

Much of the challenge of modeling $p^{\text{world}}$ lies in the fact that in many situations $s_{t - 1} \in \mathcal{S}$, $p^{\text{world}}$ assigns density to multiple outcomes due to uncertainty from agents in the scene, which means that both $\pi{(\left. o_{t}^{\text{AV}} \middle| o_{< t}^{c} \right.)}$ and $q{(\left. o_{t}^{\text{env}} \middle| o_{< t}^{c} \right.)}$ often must contain multiple modes in order to perform well. We evaluate distribution-matching of $p^{\text{world}}$ relative to a dataset of logged outcomes....

MultiVerse Transformer for Agent simulation (MVTA) Wang et al.: A method inspired by MTR Shi et al. that is trained and executed in closed-loop. MVTA uses a 'receding horizon' policy with a GMM head, and consumes vector inputs.
