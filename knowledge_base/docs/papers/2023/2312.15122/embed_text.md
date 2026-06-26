## Introduction

In this paper, we set up a scalable reinforcement learning framework and combine it with an efficient simulator for autonomous driving based on real-world data. We then conduct experiments on billions of agent steps with different model sizes in order to determine if we can overcome the constrained state space of the simulator by using increasingly more real-world data.

The main contributions of our work are: We demonstrate how to use prerecorded real-world driving data in a hardware-accelerated simulator as part of distributed reinforcement learning to achieve improving policy performance with increasing experiment size.

We demonstrate that our largest scale experiments, using a 25M parameter model on 6000 h of human-expert driving from San Francisco training on 2.5 billion agent steps, reduced the failure rate compared to the current state of the art by 64%.

## Related work

In this paper we present a hardware-accelerated autonomous driving simulator for real-world driving scenarios, which is similar to Waymax. Waymax also trains RL agents but only reported results from 30 million agent steps, approximately two orders of magnitude less than our experiments.

Training highly performant policies in complex and continuous real-world domains has mainly been achieved with distributed and scalable reinforcement learning using actor-critic methods. However, most existing results focus not on real-world problems but on video game environments.

Of the techniques that have been used to train autonomous driving policies, the closest to our work is Imitation Is Not Enough which also uses a combination of imitation learning (IL) and RL to train strong driving policies on a large dataset of real-world driving scenarios. That work established two fundamental driving metrics (failure rate and progress ratio) and provides a detailed description of the mining process of their evaluation dataset. The presented policies are state of the art (SOTA) and we will compare our best policy to theirs. Other work focuses on realistic traffic simulation, but also trains policies with a combined IL and RL approach. However, their datasets are approximately 3 orders of magnitude smaller than ours and focus on highway driving, which does not pose as complex challenges as the dense urban driving we focus . Imitation learning approaches in open loop and closed loop have also been proposed for autonomous driving. As argue, IL approaches lack explicit knowledge of unsafe driving and can respond inappropriate in rare, long tail scenarios.

## Large scale RL for autonomous driving

The challenges of using large scale reinforcement learning for autonomous driving are manifold. To achieve scale, the real-world problem must be modeled by a simulator, which requires creating realistic traffic scenes and modeling the interactions between different dynamic agents. The simulator must be sufficiently efficient to generate environment interactions on the order of billions of steps in reasonable time and computational cost. Finally, a distributed learning architecture must be identified that can learn efficiently and scalably. Learners and simulation actors must be created across many machines, each leveraging parallel hardware, i.e. GPUs.

### Scene generation and agent interactions

There are different ways of creating traffic scenes for simulation. Simulations scenarios can be generated entirely synthetically, including the placement of roads, agents, and traffic signals, for example as in the Carla simulator. While entirely synthetic simulation gives very fine grained control over training scenario distribution, this approach raises the challenge of identifying what that scenario distribution should be, and how best to sample training instances from it. A different approach is to create scenes based on real-world data recorded from vehicles equipped with sensors, such as cameras and lidar sensors, driving on public roads. From the recorded sensor data, a 3D-scene can be created that contains, for example, the observed traffic light states and challenging obstacles, such as pedestrians, cyclists, and cars. In this work, we use scenarios that have been created from real-world driving, for the fidelity of their representation of the real world.

### Accelerated autonomous driving simulator

Because our ultimate goal is to run reinforcement learning experiments with billions of agent steps, the simulator must be very efficient. This can be achieved by running the simulation on accelerated hardware, such as GPUs. The parallel computing power of accelerated hardware can lead to massive speed ups compared to CPUs. However, challenges regarding the simulation data structures and control flow need to be addressed to enable large scale parallelism. In particular, all data need to be of the same size and no logical branches depending on the values of the data can be introduced.

### Preparing data for parallel execution

A traffic scene can be described by data that changes over time (dynamic data) and data that is constant throughout the scenario (static data). An example of dynamic data are the agents in the scene --- the number of agents can change during a scenario as well as between scenarios. An example for static data are the road segments, which do not change within a scenario but change across scenarios as different locations require different roads. Furthermore, the number of time steps per scene can vary.

Data segments of different sizes are not suitable for parallel execution on hardware accelerators. To overcome this issue, a common maximum size for each type of data is defined. All data elements in the dynamic data are then padded to the defined maximum size for each time step.

### The accelerated simulation utilizing JAX

Conceptually, the simulation can be divided into a phase of action generation and a phase of advancing the environment state by applying the selected actions to the active agent and updating all other agent positions based on the logged trajectories. From the updated environment state including the recorded data, the required observations can be retrieved and used in the next step of action generation from the learning system as described in Section 3.4. The action generation is well-suited for batched inference, so the primary challenge in simulating on parallel hardware is to implement the environment update function to process batched data in parallel. We used the JAX library to rewrite the update function, so it can be jit-compiled and executed on batches on the GPU. Finally, to maximize the simulation speed, we combine the batched environment call with the batched model call and scan along the time axis of the dynamic data via the jax.lax.scan primitive. The entire simulation is then jit-compiled into a single graph and run in XLA.

### Simulator performance benchmark

To demonstrate the performance of our simulator, we compare the environment step time with Waymax, which is closest to our work. Table 1 reports the step time for different batch sizes on Nvidia v100 GPUs, showing that our simulator runs slightly faster.

Table 1: Runtime comparison for different batch sizes (BS) between Waymax and our simulator for one controlled agent.

### RL problem formulation

For our reinforcement learning approach we need to specify how we retrieve the model inputs (observations) from the state $s$ and how we generate the physical actions from the model outputs. The state $s$ is the state of the simulation described previously, i.e., agents, roads, traffic lights etc. We also need to define the rewards, so the simulated data can be used to calculate the parameter update from an RL method.

### Observation space

The observation space retrieves a subset of the information of the environment state and transforms the fields of the observation vector into an agent-centric coordinate frame.

### Action space

Our model directly controls the longitudinal acceleration as well as the steering angle rate. Using these controls guarantees that the associated dynamic constraints are not violated. We are using discrete actions, which we found to be more stable than continuous actions during reinforcement learning training.

### Rewards

The goal of the policy is to navigate safely through traffic. In particular, the agent should make progress along the desired route while not colliding with other agents and adhering to basic traffic rules. In order to achieve this, we introduce dense rewards as well as done signals that are associated with sparse rewards.

Done signals have been introduced for collisions, off-route driving, as well as running red lights and stop lines and are associated with high negative rewards. Dense rewards are introduced for the progress along the planned route (positive), velocity above the speed limit, as well as on the squared lateral and longitudinal acceleration (all negative).

### Distributed learning system

We can now establish the reinforcement learning approach. Our base reinforcement learner uses actor-critic Proximal Policy Optimization (PPO). However, to achieve scale, we set up an asynchronous reinforcement learning system similar to Dota2. The asynchronous setting allows to run the learners and actors independently avoiding any slow down. This in turn causes the data to be off-policy. We address this challenge for actor-critic methods by using the V-trace off-policy correction algorithm. Furthermore, we pre-train a policy via behavioral cloning, similar to AlphaStar because a good initial policy can speed up the RL training. However, only pre-training the policy and not the value network poses challenges to the stability at the start of RL training. Therefore, we use the discounted return of the expert trajectories as the value target. We calculate the discounted return by replaying the expert trajectories in our simulator and assigning the defined RL rewards.

## Evaluation

This section describes the different metrics and the dataset used for policy evaluation and comparison.

### Metrics

The goal of the metrics are to measure the quality of the trained policy. This is already a complex problem for autonomous driving as the quality of driving comprises many different aspects. For the scope of this paper, we follow the work of who introduced the failure rate and progress ratio as relevant metrics for autonomous driving. The failure rate measures the fundamental safety of the policy. If the agent collides or drives off-road in the simulation the scenario is considered as failed. The progress ratio is the distance traveled by the agent in the simulation divided by the distance traveled of the vehicle in the original log. When the agent travels the same distance as the vehicle in the log, this metric becomes 100 %.

In addition to collisions and off-route failures, we also implemented metrics for stop line and traffic light violations. We did not include these violations in the failure rate to maintain consistency with previously reported results. However, we do report these metrics in Table 2.

### Dataset

As the current state-of-the-art policies are evaluated on proprietary datasets, our goal was to achieve the fairest comparison by following the same dataset mining procedure. A dataset of 10k randomly sampled 10 s segments was created using data collected from human-expert driving in San Francisco. This is comparable to the "All" evaluation dataset .

## Experiments

Combining the real-world driving simulator, the scalable reinforcement learning framework and the described evaluation metrics and dataset, we conduct experiments with different training dataset and model sizes. For all these experiments we keep the hyperparameters the same. In particular we run our experiments for larger models across more GPUs to achieve the same batch size.

(a) Minimum failure rate Figure 1: Results for experiments with different model sizes (rows) and dataset sizes (columns). Colors represent the numerical results on color scales. (a) The performance of the policy improves with increasing model and dataset size. (b) The model size is the major driver of the required GPU time and therefore cost of training. Dataset size has no effect on the training time, but it can affect one time costs during data preprocessing which is not considered here.

Stop Line Violations [%] Traffic Light Violations [%] Table 2: Comparison of our policies with the current SOTA.

We mined three different training datasets of 600 h, 2000 h and 6000 h from human-expert driving in San Francisco. We also created three different model sizes of 0.75M, 2.5M and 25M parameters by increasing the attention dimensions of the network. Each model is trained first by behavior cloning for 20 epochs on the given dataset. The pre-trained policy is then refined by reinforcement learning on 2.5B agent steps. We evaluate the policy during reinforcement learning every 20M agent steps and after training select the checkpoint with the lowest failure rate on the evaluation dataset.

We conduct experiments on all combinations of model size and dataset size, with the exception of the small 600 h dataset in combination with the large 25M parameter model. 1(a) ‣ Figure 1 ‣ 5 Experiments ‣ Scaling Is All You Need: Autonomous Driving with JAX-Accelerated Reinforcement Learning") shows that increasing the dataset size improves the performance of the trained policy in terms of failure rate. Increasing the model size in general also improves the policy performance. The 2.5M model is strictly better than the 0.75M model and the best policy is trained on the 25M model. However, we observe that increasing the model size only helps when sufficient real-world driving data is available. On the 2000 h dataset the 25M performs worse than the 2.5M model and only on the 6000 h dataset it performs better. The largest experiment achieves a failure rate of $0.88\ \%$.

In Table 2 we compare the policy performance of our largest setting after behavioral cloning and after reinforcement learning training with the current SOTA. Our behavioral cloning policy performs quite poorly, achieving a failure rate of 19.85 %. This is much higher than the pure BC failure rate of 3.64 % reported in the current SOTA.

The reinforcement learning training improves the policy and achieves a failure rate of 0.88 % and a progress ratio of 120.8 %. Compared to the best policy of the current SOTA on a similar dataset, the failure rate is reduced by 64% and the progress ratio improved by 25%.

## Conclusions

In this paper we combined an efficient and realistic autonomous driving simulator with a scalable reinforcement learning framework. This allowed us to run large scale reinforcement learning experiments training on billions of agents steps with increasing model size on different dataset sizes of real-world driving.

Our data shows that we can obtain similar scaling behavior as in other reinforcement learning settings when using increasingly large datasets of real-world driving. In particular, we were able to obtain better policies with larger models when using sufficiently large datasets. Our best policy reduces the failure rate compared to the current SOTA by 64% while improving progress by 25%. These results are very encouraging, and motivate further experiments with increasing size. However, to ultimately answer whether the presented approach can be scaled beyond human performance a validation framework that can reliably compare the safety of the policy to human drivers is also required.
