## Introduction

Recent advances in parallel model-based simulation tools have shown the effectiveness of sampling-based algorithms like predictive sampling, the cross-entropy method (CEM), model predictive path integral control (MPPI), and more for generating rich, dynamic plans for a wide variety of tasks (including contact-rich ones) in real time with limited resources \[(https://arxiv.org/html/2506.17184v1#bib.bib4)\]. Moreover, recent results demonstrate that these strategies can effectively solve real-world tasks, including quadrupedal and bipedal locomotion \[(https://arxiv.org/html/2506.17184v1#bib.bib1), (https://arxiv.org/html/2506.17184v1#bib.bib12), (https://arxiv.org/html/2506.17184v1#bib.bib14)\] as well as dexterous, in-hand object reorientation \[(https://arxiv.org/html/2506.17184v1#bib.bib6)\]. However, if the robotics community wishes to build upon these successes, simple and effective open-source software is critical for further investigating and deploying these methods.

To that end, this work presents `judo`, an open-source library for developing, tuning, and deploying sampling-based MPC algorithms. The aim of `judo` is to provide a user-friendly implementation that is also performant, and enables simple transfer of controllers from simulation to hardware.

## Design Principles

Figure 1: The judo interface. The GUI is interactive, allowing users to tune parameters in real time. Dropdown menus allow switching between different tasks and controllers with ease.

3class CartpoleConfig(TaskConfig):
9class Cartpole(Task[CartpoleConfig]):
10 def __init__(self, model_path=XML_PATH):
11 super().__init__(model_path, sim_model_path=XML_PATH)
14 def reward(self, states, sensors, controls, config, system_metadata=None):
15 x, y, vel = states[..., 0], states[..., 1], states[..., 2:]
16 vertical_rew = -config.w_vert * smooth_l1_norm(np.cos(y) - 1, 0.01).sum(-1)
17 centered_rew = -config.w_ctr * smooth_l1_norm(x, 0.1).sum(-1)
18 velocity_rew = -config.w_vel * quadratic_norm(vel).sum(-1)
19 control_rew = -config.w_ctrl * quadratic_norm(controls).sum(-1)
20 return vertical_rew + centered_rew + velocity_rew + control_rew
22 def reset(self) -&gt; None:
23 self.data.qpos = np.array([1.0, np.pi]) + np.random.randn
24 self.data.qvel = 1e-1 * np.random.randn
25 mujoco.mj_forward(self.model, self.data)
29class PredictiveSamplingConfig(OptimizerConfig):
32class PredictiveSampling(Optimizer[PredictiveSamplingConfig]):
33 def __init__(self, config: PredictiveSamplingConfig, nu: int) -&gt; None:
34 super().__init__(config, nu)
36 def sample_control_knots(self, nominal_knots):
37 nn = self.num_nodes
38 nr = self.num_rollouts
39 sigma = self.config.sigma
40 noised_knots = nominal_knots + sigma * np.random.randn(nr - 1, nn, self.nu)
41 return np.concatenate([nominal_knots, noised_knots])
43 def update_nominal_knots(self, sampled_knots, rewards):
44 i_best = rewards.argmax()
45 return sampled_knots[i_best]
Listing 1: Minimal example implementations of a Task and an Optimizer using the judo API.

The design of `judo` was driven by three core principles:

Maximize Research Velocity. Echoing MJPC \[(https://arxiv.org/html/2506.17184v1#bib.bib4)\], `judo`'s main goal is to accelerate research in sampling-based MPC. To achieve this, `judo` is implemented in Python, offering an effective balance of rapid prototyping and performance suitable for rapid development. Its simple yet extensible interfaces are designed to facilitate extension of (and contribution to) the core codebase. Moreover, an integrated GUI provides real-time visualization and tuning of task and algorithm hyperparameters, significantly shortening the development loop.

Accurate and Fast Simulation. While user-friendliness is a priority, `judo` also requires a high-performance simulation engine for effective controller development and real-time applications. It utilizes MuJoCo as its primary modeling backend, enabling detailed simulation of complex scenes, geometries, and dynamics as defined via MuJoCo XML, and leveraging MuJoCo's highly-optimized, multi-threaded C-based forward dynamics. Crucially, `judo` is designed with a modular simulation backend interface; this allows researchers to integrate alternative physics engines or their own custom dynamics models if their work requires it.

Streamline Sim-to-Real Transfer. Recognizing that discrepancies between simulation and hardware are often major obstacles to hardware deployment, `judo` is engineered to minimize sim-to-real gaps and simplify the transition to hardware. The core application architecture separates control logic from physics simulation, running them in asynchronous threads. This design allows for straightforward hardware deployment: researchers can develop a specific hardware interface and substitute it for the simulation component with minimal changes to their controller code. This maximizes code reuse and provides an accurate preview of the control stack's performance characteristics prior to deployment on physical hardware.

Numerous other open-source libraries exist for developing and deploying sampling-based MPC algorithms (see Table [I](https://arxiv.org/html/2506.17184v1#S2.T1 "TABLE I ‣ II Design Principles ‣ Judo: A User-Friendly Open-Source Package for Sampling-Based Model Predictive Control")).

TABLE I: Comparison of sampling-based MPC libraries

Besides MJPC and hydrax, the majority of these libraries have fairly limited scope, like only supporting one planning algorithm (e.g., MPPI) or only exposing a limited interface for dynamical systems, requiring the user to manually write the dynamics. Thus, most existing software tooling for sampling-based MPC is less extensible towards wider algorithms or systems compared to `judo`. hydrax, an MJPC-inspired toolkit in Python, uses MJX \[(https://arxiv.org/html/2506.17184v1#bib.bib2)\], a `jax`-based re-implementation of MuJoCo as its simulation backend, and does not provide GUI functionality for controller or task tuning. While inspired by MJPC, `judo` is significantly easier to install or use as a dependency downstream. The remainder of this paper will provide detail on some of `judo`'s design decisions. The open-source code is available at [github.com/bdaiinstitute/judo](https://github.com/bdaiinstitute/judo). Of course, nothing replaces simply "playing with" the package:

pip install judo-rai # one-line install
judo # runs the browser-based GUI

## The judo Package

### III-A The Controller Interface

We assume sampling-based MPC controllers to have the structure shown in Alg. (https://arxiv.org/html/2506.17184v1#algorithm1 "In III-A The Controller Interface ‣ III The judo Package ‣ Judo: A User-Friendly Open-Source Package for Sampling-Based Model Predictive Control"). The nominal control signal that is executed on the system is parameterized by the knots $\theta$ of some control spline, which we interpolate at time $t$.

Input: θ, N, planner-specific parameters.
// estimate curr state

Algorithm 1 Sampling-based MPC

At the core of the `judo` API are tasks and optimizers, which are sub-components of the above controller. The task specifies the reward, which allows us to evaluate the rollouts. The optimizer specifies the procedure for sampling new control spline knots as well as how we should update the nominal policy given the samples and their corresponding rewards. Minimal examples of task and optimizer implementations are shown in Listing (https://arxiv.org/html/2506.17184v1#LST1 "Listing 1 ‣ II Design Principles ‣ Judo: A User-Friendly Open-Source Package for Sampling-Based Model Predictive Control").

We provide a number of starter tasks, ranging from low-dimensional examples like the cartpole system to more complex examples, including pick and place and cube rotation. We also supply some initial implementations of canonical sampling-based control algorithms, including predictive sampling, CEM, and MPPI. Lastly, we provide an extensible abstract interface for allowing alternative rollout backends in upcoming releases, such as `mujoco_warp` \[(https://arxiv.org/html/2506.17184v1#bib.bib3)\] or custom dynamics.

### III-B The GUI

The `judo` GUI is built on `viser` \[(https://arxiv.org/html/2506.17184v1#bib.bib10)\], a highly-customizable browser-based visualizer. In `judo`, the fields of registered task or optimizer config objects are automatically parsed into the appropriate GUI elements. For example, consider the dummy optimizer config in Fig. (https://arxiv.org/html/2506.17184v1#S3.F2 "Figure 2 ‣ III-B The GUI ‣ III The judo Package ‣ Judo: A User-Friendly Open-Source Package for Sampling-Based Model Predictive Control"). Integer and float fields are parsed as sliders, booleans as checkboxes, literals as dropdown menus, and numpy arrays as folders with subsliders. Moreover, `judo` provides a flexible decorator-based interface for more finely controlling the range and step size of sliders.

To visualize the optimization iterates, `judo` allows the user to specify traces in the model XML descriptions. To do so, `judo` simply looks for sensors of type `framepos` with the substring "trace" in their name. Then, the nominal and a few of the highest-performing traces (the number of which can be adjusted) are shown in the visualizer over the rollout horizon.

Lastly, `viser` allows active browser sessions to be shared with anyone else. This means that collaborators can view and even interact with a live session from anywhere in the world along with the user.

3class DummyOptimizerConfig(OptimizerConfig):
4 num1: int = 42 # default slider
5 num2: float = 3.14 # custom slider
6 num3: float = 2.71 # default slider
7 checkbox: bool = True
8 options: Literal["opt1", "opt2"] = "opt1"
9 arr: np.ndarray = np_1d_field(
11 names=["field1", "field2"],
Figure 2: A config and the corresponding automatically-generated GUI elements. Note the slider decorator, which allows fine-grained control over slider limits and step size.

### III-C Asynchronous Operation

The `judo` stack is modular, consisting of a "system" node (e.g., the simulator or whatever nodes are required to run a hardware stack), a visualizer node, and a controller node. These nodes all asynchronously communicate with each other, where the interprocess communication is handled by `dora` \[(https://arxiv.org/html/2506.17184v1#bib.bib9)\], a fast robotics-first middleware built on `rust` with a full-featured Python interface.

We find that `dora` is substantially easier to install, set up, and use than other frameworks like ROS2, and the entire communication graph is natively specified in a standardized YAML format. Moreover, `dora` allows zero-copy reads of array data between nodes on the same device, which includes any array built on the `dlpack` specification as well as `pytorch` arrays on both CPU and GPU. If the simulation node is swapped for hardware nodes, then the same visualizer and controller nodes can be used, which facilitates low-friction transfer between simulation and hardware.

### III-D Registration and Configuration Management

1# Example: programmatic registration/overrides
2from judo.cli import app
3from judo.config import set_config_overrides
4from judo.optimizers import register_optimizer
5from judo.tasks import register_task
8 register_optimizer("my_opt", MyOpt, MyOptCfg)
9 register_task("my_task", MyTask, MyTaskCfg)
10 set_config_overrides(
15 set_config_overrides(
22# Example: YAML-based registration/overrides
24 - judo # must use this default!
25task: "my_task" # init task in gui
28 task: module.path.to.MyTask
29 config: module.path.to.MyTaskCfg
32 optimizer: module.path.to.MyOpt
33 config: module.path.to.MyOptCfg
34controller_config_overrides:
37optimizer_config_overrides:
Listing 2: Example of custom registration and task-specific overrides using either a python script or hydra YAML.

There are many parameters to configure in the full `judo` stack, including the parameters of each node, as well as task-specific overrides to controller/optimizer configuration defaults. For example, in Task A, we may want a planning horizon of 1 second, whereas for Task B, we may want to use 0.5 seconds. Both of these may also differ from some default value for the controller of interest, say, 0.75 seconds. Most importantly, when a user writes a custom controller or task, it must be registered into `judo` so that it appears in the interactive dropdown menus in the GUI.

We designed `judo` such that registration and configuration management could occur in one of two ways for most cases: programmatically, by manually defining and registering parameters and/or overrides in Python, and with YAML syntax via `hydra` \[(https://arxiv.org/html/2506.17184v1#bib.bib13)\], where only a single file need be written and passed to the main `judo` executable.

For example, in Listing (https://arxiv.org/html/2506.17184v1#LST2 "Listing 2 ‣ III-D Registration and Configuration Management ‣ III The judo Package ‣ Judo: A User-Friendly Open-Source Package for Sampling-Based Model Predictive Control"), we can register custom tasks/optimizers and specify task-specific optimizer overrides in a python script, or we can identically specify the same changes in a `hydra` YAML file located at `/path/to/folder/example.yaml`, which we can pass to `judo` with the command:

judo -cp /path/to/folder -cn example

## Evaluation

In the sampling-based MPC loop, the computational bottleneck is the nominal control knot update (and in particular, the multi-threaded rollouts). To evaluate whether `judo` is viable for real-time control, we provide speed benchmarks for the control update on a consumer-grade ThinkPad X1 Carbon Gen 11 laptop with a 12-thread 13th generation i7 CPU, as well as a server-grade workstation with an 128-thread Ryzen Threadripper Pro 5995wx CPU.

We test three tasks: the canonical `cartpole` task; the `cylinder_push` task, where an actuated cylinder must push a target cylinder to a goal location; and the `leap_cube` task, where a LEAP hand must rotate a cube to reach as many consecutive goal orientations in a row as possible. For each of these three tasks, we test the speed of three optimizers: predictive sampling, CEM, and MPPI. All benchmark speeds are reported using 10 planning threads, and the threadripper is additionally profiled at 120 threads to show that the speed can be maintained at a high thread count.

Task: cylinder_push

Task: leap_cube

TABLE II: Avg. control update timing (ms).

We observe that the Threadripper computes rollouts about 2.5 times faster than the i7, though both are quick enough to run in real time. The disparity between consumer-grade and server-grade hardware is a limitation of sampling-based MPC, as noted in prior work \[(https://arxiv.org/html/2506.17184v1#bib.bib6)\]. However, as experimental GPU-based parallel simulators like `mujoco_warp` stabilize, we expect that this disparity will shrink.

## Conclusion

We hope that `judo` can facilitate the prototyping and development of sampling-based MPC algorithms in the wider robotics community. By focusing on a feature-rich and user-friendly interface, `judo` provides a hackable, extensible, and expressive framework for the development of new algorithms and investigation of complex tasks. In the future, we have an exciting roadmap of upcoming features, including integration with learned controllers, examples of hardware usage, and adding many more tasks and optimizers to the core library.
