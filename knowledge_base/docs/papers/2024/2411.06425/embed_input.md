Results of the 2023 CommonRoad Motion Planning Competition for Autonomous Vehicles

Topics include Motion planning, Vehicles, Safety, Benchmarks, Planning.

In recent years, different approaches for motion planning of autonomous vehicles have been proposed that can handle complex traffic situations. However, these approaches are rarely compared on the same set of benchmarks. To address this issue, we present the results of a large-scale motion planning competition for autonomous vehicles based on the CommonRoad benchmark suite. The benchmark scenarios contain highway and urban environments featuring various types of traffic participants, such as passengers, cars, buses, etc. The solutions are evaluated considering efficiency, safety, comfort, and compliance with a selection of traffic rules. This report summarizes the main results of the competition.

## Introduction

The CommonRoad Motion Planning Competition was established in 2021, aiming to bring together researchers working on motion planning for autonomous vehicles. This report summarizes the results from the 2023 edition. The main goal of the competition is to provide a fair comparison of different motion planning approaches on a large number of realistic traffic scenarios. To achieve this, all motion planners are executed on the same hardware and consider the same traffic scenarios....

The remainder of this report is organized as follows: First, the format of the competition is described in Sec. [0.2] and the rules for performance evaluation are presented in Sec. [0.3]. Afterward, a description of the participating motion planners is provided in Sec. [0.4], before presenting the results of the competition in Sec. [0.5].

## Conclusion

This report summarizes the results of the 3^rd^ CommonRoad Motion Planning Competition for Autonomous Vehicles held in 2023. Among the participants, two groups from Stony Brook University and Technical University of Munich were awarded for submitting high-performance motion planners which both were able to successfully solve a large number of scenarios....

where $\xi{(t)}$ is the longitudinal position of the vehicle along the lanelet \[\], $v{(t)}$ is the velocity, $a{(t)}$ is the acceleration, $\Delta t$ is the time step size, and $t_{i} = {{i \cdot \Delta}t}$ are the time points for time-discretization. Since the simplified vehicle model is linear and only has two states, the reachable set $\mathcal{R}{(t)}$ for this model can be computed very efficiently using polygons as a set representation:

We perform the evaluation of the three conditions by the CommonRoad drivability checker \[\].

Figure 3: The individual steps during trajectory sampling and trajectory evaluation in the FRENETIX motion planner.

## Format of the Competition

Teams participating in the competition solve motion planning problems for autonomous vehicles; an example is shown in Fig.. Traffic scenarios covered in the competition contain highway and urban environments, and feature various types of traffic participants, such as passenger cars, buses, and bicycles....
