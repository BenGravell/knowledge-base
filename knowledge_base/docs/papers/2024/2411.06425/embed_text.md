<!-- arxiv-full-text:v1 {"arxiv_id": "2411.06425", "source": "arxiv-html"} -->

## Introduction

The CommonRoad Motion Planning Competition was established in 2021, aiming to bring together researchers working on motion planning for autonomous vehicles. This report summarizes the results from the 2023 edition. The main goal of the competition is to provide a fair comparison of different motion planning approaches on a large number of realistic traffic scenarios. To achieve this, all motion planners are executed on the same hardware and consider the same traffic scenarios. Moreover, the benchmark scenarios are realistic since real road networks are used and the behaviors of the traffic participants are either adapted from real-world recordings or simulated by state-of-the-art traffic simulators. Finally, the competition additionally also considers a realistic vehicle model with nonlinear dynamics and parameters taken from a real Ford Escort. In addition to presenting the results of the competition, this report also contains a short description of the motion planners submitted by the participants, which provides some insights into the different motion planning strategies used.

The remainder of this report is organized as follows: First, the format of the competition is described in Sec. 0.2 and the rules for performance evaluation are presented in Sec. 0.3. Afterward, a description of the participating motion planners is provided in Sec. 0.4, before presenting the results of the competition in Sec. 0.5.

## Format of the Competition

Teams participating in the competition solve motion planning problems for autonomous vehicles; an example is shown in Fig. 1. Traffic scenarios covered in the competition contain highway and urban environments, and feature various types of traffic participants, such as passenger cars, buses, and bicycles. The participants are required to solve motion planning problems encoded in the benchmark scenarios, i.e., develop motion planners to generate feasible trajectories that drive the ego vehicle to the predefined goal region. In the 2023 edition, more than $500$ scenarios have been provided to cover many aspects of autonomous driving.

Figure 1: Example for a motion planning problem defined by the CommonRoad scenario DEU_Flensburg-73_1_T-1, where the goal set is depicted in yellow, the initial position and velocity of the ego vehicle in green, and the other traffic participants in blue.

The benchmark problems are provided in the CommonRoad format, and the participants upload Docker images with their motion planners to the servers of the CommonRoad website for evaluation. Apart from the number of solved planning problems, submissions are evaluated considering efficiency, safety, and compliance with a selection of traffic rules. The exact evaluation criteria have been decided by an independent jury and are presented in detail in Sec. 0.3. To support teams without a large software framework for motion planning, we provide useful tools for motion planning within the CommonRoad framework, such as a drivability checker, route planner^11^1 criticality measurement toolbox, etc. The competition provides two types of problems: Non-interactive scenarios in which other traffic participants do not react to the behavior of the ego vehicle with provided predictions.

Interactive scenarios using the SUMO traffic simulator, in which other traffic participants react to the behavior of the ego vehicle.

In order to lower the entry barrier for the competition, the competition is divided into two phases: Phase I is for didactic purposes (results are not considered for the evaluation), where the participants can familiarize themselves with the CommonRoad framework. We use public, known scenarios in this phase. The scenarios are a mix of non-interactive and interactive scenarios.

Phase II: The evaluation is solely performed in Phase II. We use non-public, unknown, and interactive scenarios in this phase. The participants provide Docker images of their motion planners. Submitted solutions will appear in the leaderboard^22^2 of the challenge.

At the end of the competition, the results were presented in a workshop at the IEEE International Conference on Intelligent Transportation Systems.

## Evaluation

In this section, we present the evaluation criteria of the benchmark solutions, which were decided by the jury chair of the competition. We first verify if a planned trajectory is feasible (see Sec. 0.3.1) and reaches the goal region of the benchmark scenario. The feasible trajectories that reach the goal region are then evaluated by a cost function (see Sec. 0.3.2).

### Feasible Trajectories

A trajectory is classified as feasible if it fulfills the following conditions: Collision-free: The occupancy of the ego vehicle does not intersect with other obstacles within the planning horizon.

Kinematically feasible: Trajectories must be feasible regarding the dynamic of a given vehicle model^33^3 In this competition, a kinematic single-track model \[1, Sec. III.B\] configured by the parameters of a real vehicle is employed.

Road-compliance: The ego vehicle must stay within the road network and must not occupy walkways and bicycle paths.

We perform the evaluation of the three conditions by the CommonRoad drivability checker.

### Cost Function

We evaluate the optimality of feasible trajectories by the following cost function: where the individual cost terms are defined as follows: Jerk: $J_{J}^{lon} = {\int_{t_{0}}^{t_{f}}{\overset{˙˙˙}{s}{(t)}^{2}{\mathtt{d}t}}}$, using longitudinal jerk $\overset{˙˙˙}{s}{(t)}$.

Steering rate: $J_{SR} = {\int_{t_{0}}^{t_{f}}{v_{\delta}{(t)}^{2}{\mathtt{d}t}}}$, using steering velocity $v_{\delta}{(t)}$.

Lane center offset: $J_{LC} = {\int_{t_{0}}^{t_{f}}{d{(t)}^{2}{\mathtt{d}t}}}$, where $d{(t)}$ is the distance to the lane center.

Distance to obstacles: $J_{D} = {\int_{t_{0}}^{t_{f}}{{\max{(\xi_{1},\ldots,\xi_{o})}}{\mathtt{d}t}}}$, where $o$ is the number of surrounding obstacles in front of the ego vehicle, $\xi_{i} = e^{- {w_{\mathtt{d}\mathtt{i}\mathtt{s}\mathtt{t}}d_{i}}}$, $d_{i}$ is the distance of the ego vehicle to an obstacle, and $w_{\mathtt{d}\mathtt{i}\mathtt{s}\mathtt{t}}$ is an additional required weight.

The weighting factors are ${\mathbf{w}} = {\lbrack 0.01,22,8,5\rbrack}$ and $w_{\mathtt{d}\mathtt{i}\mathtt{s}\mathtt{t}} = 0.2$. The cost function is implemented in the drivability checker with the ID TR1.

## Participants

The universities that participated in the competition are subsequently introduced in alphabetical order, where each participant provides a short description of the motion planner that was used for the competition.

### Stony Brook University

Niklas Kochdumper and Stanley Bak formed the team of the Reliable Systems Laboratory from the Department of Computer Science at Stony Brook University. This group mainly researches the verification of autonomy, cyber-physical systems, and neural networks.

The core element of the developed motion planner is a reachability-based decision module, which uses reachable sets to identify the most suitable driving corridor for the ego vehicle. This module uses the following simplified vehicle model for decision making: where $\xi{(t)}$ is the longitudinal position of the vehicle along the lanelet, $v{(t)}$ is the velocity, $a{(t)}$ is the acceleration, $\Delta t$ is the time step size, and $t_{i} = {{i \cdot \Delta}t}$ are the time points for time-discretization. Since the simplified vehicle model is linear and only has two states, the reachable set $\mathcal{R}{(t)}$ for this model can be computed very efficiently using polygons as a set representation: where $a_{\text{max}}$ is the maximum acceleration of the vehicle.

The overall process for constructing all possible driving corridors is visualized in Fig. 2: The procedure starts by computing the reachable set for the current lanelet. Next, the computed reachable set is used to check if any neighboring or successor lanelets are reachable. If this is the case, the reachable sets for all reachable lanelets are computed, and it is again checked if any additional lanelets are reachable. This procedure is repeated until all possible driving corridors have been identified. Finally, the most suitable driving corridor is selected from all driving corridors reaching the goal set based on a cost function that penalizes the number of lane changes as well as deviations from a desired velocity profile. Improvements and extensions for this basic procedure consist in applying criteria based on the friction circle to ensure that the selected driving corridor is also driveable by the real vehicle, and considering traffic rules like speed limits by removing regions from the driving corridor that violate the rules.

In addition to the most suitable driving corridor, the decision module described above also provides a reference trajectory inside this corridor. However, since this reference trajectory is constructed using the simplified vehicle model, it might not be driveable by the nonlinear kinematic single track model $\overset{˙}{x} = {f{(x,u)}}$ with state vector $x \in {\mathbb{R}}^{5}$ and control input vector $u \in {\mathbb{R}}^{2}$ used in the CommonRoad competition. Therefore, we solve the following optimal control problem to obtain a trajectory that is consistent with the dynamics of the nonlinear vehicle model and close to the reference trajectory $z_{\text{ref}}{(t)}$ provided by the decision module: where $N$ is the number of discrete time steps, $Q \in {\mathbb{R}}^{2 \times 2}$ and $R \in {\mathbb{R}}^{2 \times 2}$ are user-defined weighting matrices, $u_{\text{max}} \in {\mathbb{R}}^{2}$ is the limit for the control inputs, and $C \in {\mathbb{R}}^{2 \times 5}$ is a matrix that selects the x- and y-position of the vehicle from the state vector $x{(t)}$ of the vehicle model.

For the implementation of the motion planner, we used the code for the decision module available on GitHub^44^4 and applied CasADi^55^5 to solve the optimal control problem. Moreover, the parameter values we used are ${\Delta t} = 0.1$s, $Q = I_{2}$, $R = {0.01 \cdot I_{2}}$, where $I_{n} \in {\mathbb{R}}^{n \times n}$ denotes the identity matrix.

Figure 2: Visualization of the single steps for the reachability-based decision module used by the motion planner from Stony Brook University, where the goal set is depicted in yellow, the space occupied by other traffic participants in blue, the drivable area for the ego vehicle in red, and the provided reference trajectory in black.

### Technical University of Munich

Our motion planner FRENETIX was developed by the Autonomous Vehicle Systems (AVS) Laboratory from the Technical University of Munich. The research of the AVS Lab focuses on the development of new algorithms that enable trajectory and behavior planning, adaptive control, and continuous learning of the systems. The team participating in the competition consists of Alexander Hobmaier, Rainer Trauth, and Johannes Betz.

FRENETIX offers a high-performance, modular solution that integrates various aspects of motion planning, ensuring comfort, safety, and precision in complex urban scenarios. A significant contribution of FRENETIX is its modular design, which realizes easy adaptability and scalability, making it possible to integrate new features or updates without requiring a complete overhaul of the system. Moreover, the FRENETIX algorithm is implemented in both Python and C++, offering flexibility while ensuring real-time capability.

Figure 3: The individual steps during trajectory sampling and trajectory evaluation in the FRENETIX motion planner.

### FRENETIX Architecture

FRENETIX is based on a sampling-based method, which is effective in high-dimensional spaces, searching for free space and target states. The first step in the planning process is to calculate the reference path through global planning, setting the stage for more detailed planning at a local level. The motion planning cycle in FRENETIX involves several critical steps: Trajectory sampling: Trajectory sampling (Figure 3) is the first component of the FRENETIX planning process. Potential final states of the ego vehicle are generated based on a predetermined discretization scheme as in \[10, Table 1\]. By connecting the current state of the ego vehicle and the potential terminal states with polynomial functions, multiple trajectory samples are produced. These samples are initially represented in curvilinear coordinates, which align with the road geometry and realize efficient sampling. Subsequently, the samples are converted to Cartesian coordinates, facilitating their use in trajectory evaluation and further processing.

Trajectory evaluation: In the second component, the sampled trajectories undergo various trajectory evaluation steps (Figure 3) to determine their feasibility. These include kinematic and dynamic feasibility checks, as well as collision avoidance and road compliance checks. Additionally, the trajectories are evaluated based on cost functions that account for efficiency, safety, and comfort.

Scenario update and iteration: After evaluation, the best trajectory is selected. If the goal has not been reached, the scenario is updated, and the planning cycle iterates, refining the trajectory until the vehicle successfully reaches its destination.

Figure 4: One of the scenarios in which FRENETIX was tested involves dynamic overtaking, a complex maneuver that requires precise trajectory planning and real-time adjustments. FRENETIX successfully navigated this scenario, demonstrating its capability to handle high-stakes driving situations where safety and accuracy are paramount.

### FRENTIX Performance

The effectiveness of the FRENETIX motion planner is demonstrated by its performance in various scenarios and its runtime efficiency. Besides the competition, FRENETIX was tested on 1,750 scenarios from the CommonRoad database. FRENETIX successfully solved 1,539 scenarios, representing an 88% success rate. The remaining scenarios were either infeasible, resulted in collisions, or exceeded the time limit. These results highlight the robustness of the planner in handling a wide range of driving situations (Figure 4).

The runtime analysis provides insight into the computational efficiency of FRENETIX, which was evaluated using both single-core and multi-core implementations in C++ and Python. The results indicate that the C++ implementation, particularly in a multi-core setup, significantly outperforms the Python version, especially as the number of trajectories increases. For instance, when processing 90,000 trajectories, the multi-core C++ implementation achieved a runtime of 717 ms, compared to 10,986 ms for the Python multi-core implementation.

### FRENETIX Enhancements with Modules

The modular architecture of FRENETIX makes it possible to integrate additional modules that enhance its functionality. Among these, the motion prediction module plays a pivotal role by enabling the planner to anticipate the movements of other vehicles and objects in the environment, thereby improving its decision-making process in dynamic and fast-changing scenarios. Equally important is the occlusion-aware planning module, which enables FRENETIX to consider hidden areas that might conceal obstacles, further increasing the safety and reliability of its planned trajectories. The architecture also supports reinforcement learning optimization, allowing the system to learn from past experiences and refine its decision-making algorithms. Coupled with an additional risk assessment, these advancements empower FRENETIX to tackle increasingly complex and unpredictable driving environments.

Technical University of Munich (Sec. 0.4.2) Stony Brook University (Sec. 0.4.1) Multiple submitted planners might be able to solve a particular scenario. The solution with the lowest cost according to function is referred to as the top 1 solution to the scenario.

Table 1: Results of the motion planners introduced in Sec. 0.4.

## Results

The submitted motion planners are evaluated on $230$ interactive CommonRoad benchmark scenarios that are unknow to the participants. The evaluation is timed out after 6 hours, and at most two cores can be used. Note that the time limit aims at penalizing computation time, since motion planners that are faster will be able to solve more scenarios within the given time frame. All computations are carried out on a server with two AMD EPYC 7763 processors with $2$ TB memory.

For each submission in Sec. 0.4, the number of solved scenarios and the number of best solutions are presented in Tab. 1. Both motion planners were able to successfully solve a large number of scenarios within the given time frame. Consequently, both planners overall have a quite similar performance, and the victory in the competition was very close. The winner of the competition is the team of Alexander Hobmaier, Rainer Trauth, and Johannes Betz from Technical University of Munich, whose planner results in the most solutions with the lowest costs. Niklas Kochdumper and Stanley Bak from Stony Brook University won the second place in the competition.

For a more detailed comparison of the two participating motion planners, Fig. 5 displays the value of the cost function in for some exemplary scenarios that could be successfully solved by both motion planners. In many scenarios, both planners provide solutions with very similar and quite low overall costs. Exceptions are the scenarios DEU_Frankfurt-3_50_I-1, DEU_Frankfurt-3_50_I-1, and DEU_Frankfurt-3_38_I-1, where the motion planner from Stony Brook University performs significantly better than the one from Technical University of Munich, as well as the scenarios DEU_Frankfurt-3_40_I-1, DEU_Aachen-9_56_I-1, DEU_Frankfurt-3_10_I-1, and DEU_Frankfurt-3_10_I-1, where the motion planner from Technical University of Munich performs much better than the one from Stony Brook University. The results shown in Fig. 5 also demonstrate the different degrees of difficulty for the scenarios considered in the competition, since some scenarios are easily solvable by both planners with very low cost, while other scenarios can only be solved with very high cost by both participants.

Figure 5: Performance comparison on benchmark scenarios that are solved by both planners.

## Conclusion

This report summarizes the results of the 3^rd^ CommonRoad Motion Planning Competition for Autonomous Vehicles held in 2023. Among the participants, two groups from Stony Brook University and Technical University of Munich were awarded for submitting high-performance motion planners which both were able to successfully solve a large number of scenarios. Interestingly, the planners from these two groups apply very different strategies for motion planning, which makes the performance comparison very exciting: While the motion planner from Stony Brook University combines a high-level decision making module with an optimization-based trajectory planner, the motion planner from Technical University of Munich is sampling-based. Despite the very different motion planning strategies used by the participants, their motion planners result in a very similar overall performance in the competition.
