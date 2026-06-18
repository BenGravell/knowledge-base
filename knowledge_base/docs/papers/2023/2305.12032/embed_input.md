The Waymo Open Sim Agents Challenge

Topics include Autonomous driving, Vehicles, WOSAC.

Simulation with realistic, interactive agents represents a key task for autonomous vehicle software development. In this work, we introduce the Waymo Open Sim Agents Challenge (WOSAC). WOSAC is the first public challenge to tackle this task and propose corresponding metrics. The goal of the challenge is to stimulate the design of realistic simulators that can be used to evaluate and train a behavior model for autonomous driving. We outline our evaluation methodology, present results for a number of different baseline simulation agent methods, and analyze several submissions to the 2023 competition which ran from March 16, 2023 to May 23, 2023. The WOSAC evaluation server remains open for submissions and we discuss open problems for the task.

## Introduction

Simulation environments allow cheap and fast evaluation of autonomous driving behavior systems, while also reducing the need to deploy potentially risky software releases to physical systems. While generation of synthetic sensor data was an early goal Pomerleau; Dosovitskiy et al. of simulation, use cases have evolved as perception systems have matured. Today, one of the most promising use cases for simulation is system safety validation via statistical model checking Corso et al.; Agha and Palmskog with Monte Carlo trials involving realistically modeled traffic participants, i.e., *simulation agents*.

Simulation agents are controlled objects that perform realistic behaviors in a virtual world. In this challenge, in order to reduce the computational burden and complexity of simulation, we focus on simulating agent behavior as captured by the outputs of a perception system, e.g., mid-level object representations Bansal et al.; Zhang et al. such as object trajectories, rather than simulating the underlying sensor data Yang et al.; Manivasagam et al.; Chen et al.; Tancik et al. (see Figure 1).

## Limitations

For our 2023 Challenge, we manually verified the validity of each submission according to factorization and closed-loop requirements discussed in each team's report, and we observed that the technical rules were subtle. Several of the submissions that used open-loop or hybrid open-loop/closed-loop methods may have limited applicability for some simulation applications.

Even if we had instituted a benchmark based on Docker-containerized software submissions instead of uploading output trajectory submissions, enforcing our requirements algorithmically and automatically would still be challenging. Although many properties of function calls to Dockerized software can be measured, e.g. latency, as long as any arbitrary state is maintained by the user, the system could not enforce all details of the closed-loop nature of the function call. As a result, user-submitted simulation agent software would have to adhere to strict stateless input and output data APIs.
