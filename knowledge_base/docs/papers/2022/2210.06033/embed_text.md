<!-- arxiv-full-text:v1 {"arxiv_id": "2210.06033", "source": "ar5iv"} -->

## INTRODUCTION

Robot motion planning in dynamic environments is fundamentally different from motion generation in static environments because initial plans must be constantly updated in the presence of unforeseen events. Algorithms that aim to adapt global plans according to dynamic changes in the environment and transfer them into actions at runtime fall into the category of local motion planning or reactive motion planning. As the number of applications (e.g. mobile robots, robotic arms, mobile manipulators) is quite diverse, different methods have been presented in the last years showing varying performance depending on the scenarios. These methods can be roughly divided into four categories: (a) geometric approaches, such as the potential field method, reciprocal collision avoidance with velocity obstacles, Riemannian Motion Policies or optimization fabrics, (b) optimization-based approaches, such as STOMP or model predicitive control, (c) compositon of motion primitives, and (d) learning-based approaches. Due to a steady increase in number of methods and a tendency to focus on one of the above approaches, it becomes increasingly difficult and time-consuming to make proper comparisons among methods. Additionally, new methods in the field are often not publicly available so comparisons require re-implementation of these methods. Together with a general bias toward optimizing parameters of a proposed method, fair comparisons become more challenging. To address these issues, we offer localPlannerBench, a bench-marking tool to allow quick and seamless comparison between different local motion planning algorithms. Additionally, we promote extendibility to allow users to modify localPlannerBench according to their setups.

First, we review briefly other benchmarking software with a similar purpose while laying out the differences to our framework (Section II). Then, we state the scope of our framework and introduce the approach. (Section III). We lay out the general structure of localPlannerBench and explain individual components in Section III-E. Lastly, we briefly present a use-case where two different planners are compared (Section IV).

## RELATED WORK

As we propose localPlannerBench for benchmarking local motion planning algorithms, we briefly revise existing benchmarks in robotics to highlight differences. Sampling-based motion planning for global motion planning was first standardized in the Open Motion Planning Library (OMPL). There, many algorithms are implemented and accessible to the user. Today, it is used as the backend planning library for many robotics software. While the benefit of assembling different algorithms in a single library is, still today, highlighted by OMPL, it is not a benchmark suite on its own. Robowflex is a wrapper around various motion planning libraries that can evaluate different global motion planning algorithms in isolation. It also includes standardized motion planning problems to promote comparisons. The goal behind localPlannerBench is to provide a similar framework but instead of focusing on global motion planning methods, which are most valuable in static environments, we focus on dynamic environments and thus on local motion planning methods. Some benchmarking frameworks focus purely on mobile robots and/or autonomous driving and provide benchmarks for local motion planning methods in cluttered and human-shared environments. With localPlannerBench, we generalize this approach beyond mobile robots by including robotic arms and mobile manipulators. To make motion planning methods more reproducible and comparable, all of the mentioned works play a central role and localPlannerBench takes this role for local motion planning.

Figure 1: Examples of environments (pybullet in Figs. 1(a) and 1(b) and simple ODE in Fig. 1(c)) available in localPlannerBench. Goal states are depicted as green circles, and obstacles as either red or black depending on the environment.

## APPROACH

### III-A Scope

We define local motion planning as the problem of computing actions for the robot at runtime, such that the sequence of actions leads to progress in the fulfillment of the goal while avoiding collisions with its environment. From this definition, it follows that interactive motion planning, where the robot is allowed to manipulate objects, is not considered. Moreover, we consider collision avoidance the only safe way of navigating through the environment. While the initial state can be specified by a robot configuration, the goal is a composition of geometric constraints. Some examples that can be stated as geometric constraints are, that the end-effector has to be at a defined position and/or orientation, some joints need to be in a specific position, some links must align or the robot has to follow a certain trajectory. Although not supported in this version, the latter could be generated with global planner. In other words, the meaningful behavior of the robot in the environment is assumed to be parameterizable by these geometric goals.

Furthermore, perception pipelines are outside the scope of this work. At this stage, we assume a working perception pipeline that can detect all obstacles as they move through the environment. In the future, we want to integrate more abstract perception pipelines, e.g. generating occupancy grids based on the obstacles positions and shapes. Low-level control of the joints of the robot is also out of the scope of this work. That means, we provide environments with different control modalities, but the control signal is directly passed to the environment, so a perfect low-level controller is assumed.

### III-B Definitions

An environment refers to the physics simulator (or real world) that produces robot states and obstacle poses and applies actions to the robot. The problem formulation is defined by the geometric parameterization of the goal, the robot, the specifications of the obstacles and additional global environment variables. A planner is a local motion planning method that computes an action based on the current state of the environment. We define a metric as a quantitative measure for the performance evaluation of a planner. A single run of the environment with corresponding problem formulation and planner is referred to as a trial. A study, within localPlannerBench, refers to a series of trials.

### III-C Rational

Our guidelines for developing and maintaining localPlannerBench are the following: Simplicity It should be as simple as possible to run a trial/study.

Modularity It should be straightforward to add a planner, metric or problem formulation.

Specificity It should focus on local motion planning and local motion planning only.

In the following, we derive design choices based on those motivations.

### III-D Environment

The environment in localPlannerBench is not specific to a single physics simulator and should even be compatible with the real world through e.g. a ROS bridge (modularity). However, at the time of writing, two physics simulators are officially supported (see Fig. 1), planar environments are based on a simple ODE-simulation and pybullet is used for more complex 3D environments. In the pybullet environments we use the unified robot description format (URDF) that allows to import new robots simply by this robot description. To achieve a clean separation between the simulation environment and planning algorithm, we opted to design an Open-AI gym environment wrapper for the different robot types and control modalities that we support (Simplicity, Modularity). Pybullet is not considered the most accurate physics engine, but it is much easier to install compared to competing simulators like ISAAC-Gym or MuJoCo (Simplicity). Besides, as low-level control and interactive motion planning are outside of our scope, the accuracy of PyBullet is considered sufficient (Specificity).

Figure 2: Code structure of localPlannerBench. Blue components are provided, while the orange components should be passed along at run-time. A specific planner (green) could be implemented by the user, and the outputs are shown as yellow blocks.

### III-E Code structure

The code in localPlannerBench is split up into components as can be seen in Fig. 2. Each component has a unique and clearly defined responsibility (Modularity). The parameters specifying specific configurations of these components are as much as possible defined outside of the code itself using yaml-files. When possible, the code structure reflects the definitions proposed in Section III-B: The Problem class corresponds to the problem formulation and requires its own configuration file to read in the requested problem formulation. Additionally, the component supports randomization of the initial configuration, goal state, and obstacle states. The limits of the randomization should also be defined within the configuration file.

The AbstractPlanner is a blueprint for a planner class. When a user creates a new planner, she should derive from this provided base class, so that the planner will automatically be registered as a valid planner to the rest of the package. A planner created using this component is parameterized by the corresponding configuration file.

The runner executable is the entry point when running a trial or study i.e. it is the executable that the user interacts . The component contains the code for the actual execution loops over the Open-AI gym simulation environments and saves the results afterward.

The post-processor executable processes the results based on user specified metrics and plot characteristics. Like the runner, it is an executable that the user interacts .

### III-F Usage

There are currently two general possible usages of localPlannerBench: (a) access an open implementation of a local motion planner and its tuned parameters by an expert or (b) compare your own local motion planner against baselines that are already implemented in localPlannerBench

### III-G Running a study

localPlannerBench provides a minimal command-line interface (CLI) that processes the configuration files described in the previous section. The CLI calls the runner that runs a study with the given parameters. Specifically, the user specifies the location of the configurations files for the problem formulation and the planner. Additionally, flags and arguments for the study can be speficied through the CLI. For example, the user could specify the location of the output files, whether the simulation should be rendered or not, how many trials should be run, etc. Finally, all relevant information to reproduce a study is saved in a time-stamped results folder. An overview of arguments can be found in Table I.

Path to problem formulation file.

List of paths to planner configuration files.

Path to store the result data.

How many trials to run.

Should the goal be random?

Should the initial configuration be random?

Should the obstacles be random?

TABLE I: List of CLI arguments for the runner executable

### III-H Postprocessing a study

To promote better reproducibility, running, and post-processing a study is completely separated. Specifically, the output of a study is the raw data that was directly accessible during the execution. That is: the joint position, the joint velocities, the taken actions, the positions of the links of the robot, the position of obstacles, and the goal at each time step. During post-processing, the raw data is evaluated according to user metrics and is potentially plotted. Several performance metrics are implemented, see the repository for a full list. However, additional metrics could be added using a similar approach as for the planner. An overview of post-processor arguments can be found in Table II.

Path to the results of a study.

List of all kpis/metrics to be evaluated.

Auto-generate plot from results.

Are you evaluating a single trial or multiple?

Are you comparing planners?

TABLE II: CLI arguments for the post_processor executable

## EXAMPLE: Optimization fabrics vs MPC

An example of how localPlannerBench can be used to compare the two methods, Static Fabrics and Model Predictive Control (MPC), is found . The goal of the comparison was to investigate if the significant reduction in solver time of Static Fabrics impacts other metrics like path length, clearance or time to goal. Using the runner, a study was run for a hundred trials, including both planners. Afterwards, the plots in Figure 3 were generated using the post-processor.

Figure 3: Exemplary comparison between two different local motion planning algorithms in localPlannerBench.

## CONCLUSION

As the field of local motion planning matures, the need for standardized reproducible benchmarks increases. To make the life of a researcher a little easier, we've created localPlannerBench. This framework is capable of simulating local motion planning problems, for many different robots, modalities, and environments. Furthermore, localPlannerBench is fully open source and designed with simplicity, modularity, and specificacy in mind, enabling users to easily modify localPlannerBench to fit their unique use cases as long as they fit within the scope as what we define as local motion planning. In the future, we hope to extend localPlannerBench in several ways: integrating basic global planning methods to provide reference trajectories for local planning, adding artificial uncertainty to the states and observations to help make the studies more representative of real scenarios, adding support for observations in the form of occupancy maps, semantic maps, or even direct camera or lidar data to accommodate new directions in local motion planning. localPlannerBench has already been proven to be useful for academic comparison and evaluations, and we hope it will gain futher attention in this field of local motion planning.
