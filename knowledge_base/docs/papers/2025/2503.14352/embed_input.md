<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Flying in Highly Dynamic Environments with End-to-end Learning Approach

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Obstacle avoidance for unmanned aerial vehicles like quadrotors is a popular research topic. Most existing research focuses only on static environments, and obstacle avoidance in environments with multiple dynamic obstacles remains challenging. This paper proposes a novel deep-reinforcement learning-based approach for the quadrotors to navigate through highly dynamic environments. We propose a lidar data encoder to extract obstacle information from the massive point cloud data from the lidar. Multi frames of historical scans will be compressed into a 2-dimension obstacle map while maintaining the obstacle features required. An end-to-end deep neural network is trained to extract the kinematics of dynamic and static obstacles from the obstacle map, and it will generate acceleration commands to the quadrotor to control it to avoid these obstacles. Our approach contains perception and navigating functions in a single neural network, which can change from a navigating state into a hovering state without mode switching. We also present simulations and real-world experiments to show the effectiveness of our approach while navigating in highly dynamic cluttered environments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unmanned Aerial Vehicles (UAVs), particularly quadrotors, have ushered in a new era of possibilities across diverse applications in recent years, such as photography, logistics, and exploration. Quadrotors have emerged as the predominant choice among UAVs owing to their adaptability and agility. Nevertheless, maneuvering quadrotors in cluttered environments typically demands the expertise of a skilled human pilot, leading to additional training requirements. Moreover, human response times can limit the full potential of quadrotors.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these challenges, autonomous obstacle avoidance techniques have been introduced. By integrating sensors like depth cameras or lidar, quadrotors can autonomously navigate through these environments. State-of-the-art obstacle avoidance approaches primarily rely on perception and path planning utilizing optimization algorithms, ensuring performance but often requiring substantial hardware resources for deployment. Furthermore, the latency of perception during high-speed flight can constrain performance.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, learning-based approaches have emerged as an alternative. Unlike optimization algorithms, neural networks are employed for obstacle avoidance, offering reduced latency and enabling faster responses compared to conventional optimization-based approaches.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the majority of current research only focuses on static environments. Obstacle avoidance in highly dynamic settings with fast-moving dynamic obstacles remains a challenge. Navigating through such environments not only poses planning complexities but also demands effective perception techniques.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we introduce a novel end-to-end learning-based approach designed for obstacle avoidance in highly dynamic environments. Leveraging lidar for perception, the point cloud data captured by the lidar system is transformed into an obstacle map. Our approach employs Deep Reinforcement Learning (Deep-RL) to train a neural network specifically tailored for dynamic obstacle evasion.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The observation space of the neural network contains both the obstacle map and the current state of the quadrotor. By sending acceleration commands to the flight controller, the neural network directs the quadrotor to navigate and bypass both dynamic and static obstacles during flight.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, we conduct a series of simulated and real-world experiments to compare our framework against the existing works. Our method showcases reduced response latency in comparison to optimization-based approaches, enabling rapid reactions to swiftly moving obstacles. In contrast to prevailing learning-based techniques, our methodology demonstrates superior performance in navigating through cluttered environments with a higher density of high-speed dynamic obstacles.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The key contributions of this research are outlined as follows: We introduce a novel lidar data encoding methodology. By compressing 3D point cloud data into a 2D obstacle map, our approach encapsulates the contours and dynamics of both static and dynamic obstacles.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our work proposes a deep reinforcement learning framework that incorporates both static and dynamic obstacles during the training phase. Our framework enables quadrotors to navigate through highly dynamic environments.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We first realize the learning-based end-to-end dynamic obstacle avoidance. In contrast to rule-based approaches, our system exhibits obviously reduced latency on mobile computing platforms, enabling the quadrotor to evade high-speed obstacles moving at speeds of up to 6 $m/s$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Static environments navigation", "weight": 1.0} -->

Various approaches have been proposed to tackle the obstacle avoidance problem. In most of the works, real-time obstacle avoidance for mobile robots is realized by a two-piece framework comprised of mapping and planning. first realized optimization-based planning algorithm for trajectory generation of quadrotors. Subsequent research like proposed the integration of grid maps and optimization-based planning algorithms to facilitate real-time trajectory generation using onboard sensors like lidar or depth cameras. The methods enable the UAVs to fly in static cluttered environments robustly and avoid some slow-moving objects. However, the methods could not perform well in cluttered and highly dynamic environments, because their planning process did not include the observation and prediction of the moving objects.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Static environments navigation", "weight": 1.0} -->

Learning-based planners satisfy a faster response compared to conventional methods. applied imitation learning to achieve high-speed flight in cluttered environments with depth cameras. In this work, a stated-based teacher policy was trained to fly in these environments with pre-calculated waypoints and various sensor data. The student policy shared the same action space with the teacher policy, but it only had the observation space containing depth image, velocity, and attitude data, and it would be trained by the teacher policy. This work realized high-agility flight in cluttered environments, but it is not compatible with highly dynamic environments. also applied similar approaches.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Dynamic obstacle avoidance", "weight": 1.0} -->

In order to satisfy the requirements of navigating in environments with dynamic obstacles, researchers have developed some new methods. applied image-based algorithm for dynamic obstacle perception, and added the kinematic of dynamic obstacles into the cost function of the optimization algorithm while planning. Such works perform well on fast-moving small objects, but due to the limit of image recognition algorithms, only specific objects with distinct characteristics can be tracked, which reduces their universality. achieved fast-moving object avoidance based on the low latency of the event camera. However, event cameras are only sensitive to moving objects, making it difficult to fully perceive the information in complex environments. To fill these gaps, made further contributions to dynamic obstacle avoidance. In these works, dynamic obstacles would be segmented from the overall point cloud data by cluster algorithm, and a Kalman Filter was adopted to estimate the velocity of moving objects. The optimization algorithm would then generate the trajectory of the UAV according to the perception result. However, the point cloud-based dynamic perception methods were time-consuming, and the success rate would significantly decrease when dynamic objects move at a high speed.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Dynamic obstacle avoidance", "weight": 1.0} -->

Besides, the classification of the dynamic point cloud was difficult to formulate by conventional methods, and some false detection conditions could not be eliminated. Moreover, solving the model predictive control (MPC) and polynomial optimization problems would be very time-consuming if the problem was very complex.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Dynamic obstacle avoidance", "weight": 1.0} -->

Furthermore, made contributions to learning-based dynamic obstacle avoidance. In this work, a conventional optimization-based planner served as the teacher policy, and imitation learning was applied to train a neural network as a planner, which brought a significant decrease in planning latency. However, it did not consider the perception of dynamic obstacles, and the proposed neural network was designed to avoid only a single dynamic obstacle. tailored a pedestrian avoidance methodology for ground-based robots, leveraging a combination of sensors such as lidar and RGB cameras for perception. This research utilized RGB camera and lidar inputs, enabling the system to monitor pedestrian movements based on a brief historical analysis of lidar data and the kinematic details derived from YOLOv3. While this approach proved effective for navigating congested environments by detecting and avoiding pedestrians, its scope is limited solely to pedestrian avoidance and does not extend to evading other categories of dynamic obstacles. Analogously, designed a learning-based approach for ground-based robot navigation, which also collects multiple historical scans for obstacle identification. In this work, semantic segmentation is applied to separate movable objects from the lidar point cloud.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Dynamic obstacle avoidance", "weight": 1.0} -->

However, this work was designed for ground robots and relatively static environments, and it is not compatible with highly dynamic environments and quadrotors.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Methodology", "weight": 1.0} -->

In this article, we address the problem of planning the motion of a quadrotor to fly safely in highly dynamic environments with lidar sensing.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Method Overview", "weight": 1.0} -->

Our approach to dynamic obstacle avoidance while flying in cluttered environments contains a method for observing static and dynamic obstacle information from point cloud data, and a training strategy to train a neural network with deep reinforcement learning.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Method Overview", "weight": 1.0} -->

The overall architecture of our method is shown in Fig. 2. The input of the system includes point cloud data of the environment, a set of vectors indicating the target position related to the quadrotor, and the state of the quadrotor including its velocity and acceleration command from the network in the last frame. The point cloud data will be encoded to compress obstacle information into a single-dimensional array to reduce data volume. We stack the compressed historical obstacle information in the previous 36 frames into a gray-scale image, and use an image encoder to extract the obstacle outlines and kinematic information of dynamic obstacles. Then, a Multi-Layer Perceptron (MLP) network is applied to generate horizontal accelerations according to the target command, quadrotor state observation, and obstacle information, therefore avoiding dynamic and static obstacles while navigating to the target position.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Lidar Data Encoding", "weight": 1.0} -->

This section introduces a methodology for encoding voluminous point cloud data from lidar into a 2-dimension array obstacle map, encompassing information on static and dynamic obstacles. This encoded data serves as a component of the input of the neural network.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Lidar Data Encoding", "weight": 1.0} -->

The system perceives its surroundings through lidar, which furnishes a point cloud dataset comprising detected point positions. However, directly feeding this data into the neural network is impractical due to its varying size and substantial data volume. Let ${}_{B}^{}P_{k}^{}$ denote the point set obtained from lidar in the $k$th frame. To neutralize the attitude impact of the quadrotor, a ${\mathbb{S}}{\mathbb{O}}{}$ rotation transformation ${}_{B}^{W}T_{k}^{}$ is applied to convert the point cloud data from the body frame $B$ to the horizontal global frame $W$, yielding the transformed point set ${}_{W}^{}P_{k}^{}$, and ${}_{B}^{W}T_{k}^{}$ can be obtained from the onboard attitude estimator.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Lidar Data Encoding", "weight": 1.0} -->

The scanning time of the lidar leads to significant delays when evading fast-moving dynamic obstacles. It usually takes a lidar 0.1 seconds to finish a complete scan, and incomplete scans might overlook smaller objects. Therefore, a sliding window is employed to process the point data. To be specific, a dynamic set of point clouds $\xi$ is defined, where $\xi \subseteq {\{{\underset{i\in{\lbrack{k-j},k\rbrack}}{\bigcup}{{}_{W}^{}P_{i}^{}}}\}}$. This set retains point cloud data received from the lidar in the preceding $j$ frames, ensuring a stable observation of the point cloud while maintaining swift responses to rapidly moving small obstacles.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Lidar Data Encoding", "weight": 1.0} -->

\{{p_{i} \in \xi} \middle| {{{\| p_{i}\|} < d_{max}},{{z_{i} \in {\lbrack z_{min},z_{max}\rbrack}},{\theta_{i} \in {\lbrack\frac{2\pi{({s - 1})}}{n},\frac{2\pi s}{n}\rbrack}}}}\} \right.$, where $n$ is the angular resolution while generating the obstacle map, which is set to 36, and $d_{max}$ is the maximum distance that the obstacle map presents, which is set to 10 during training and real-world deployment. To filter out the points that do not impede flight, like ground and ceiling, only points within the current flight level are kept, where $z_{min} = {z_{q} - h}$, and $z_{max} = {z_{q} + h}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Lidar Data Encoding", "weight": 1.0} -->

$z_{q}$ is the altitude of the quadrotor, and $h$ is the altitude threshold, which is set to 1 $m$ in real-world deployment. With the constant altitude of the quadrotor, the 3-dimension point cloud data can be compressed into a distance vector: Furthermore, if $P_{s} = \varnothing$, we will let ${D_{s}{(k)}} = 1$. The distance vector $O{(k)}$ contains the distances of the nearest point to obstacles in each direction, which are denoted as $D_{s}{(k)}$. This format maintains a constant data size, occupies less storage, and provides adequate information for obstacle avoidance.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Lidar Data Encoding", "weight": 1.0} -->

Inspired, we use a 2D array to express multi frames of lidar scan data. The historical distance vectors in the previous $m$ frames can be organized as: where $M{(k)}$ constitutes a 2D obstacle map comprising historical obstacle data from the above-mentioned frames, and $m$ is set to 36 during training and real-world deployment. Fig. 3 (b) illustrates the obstacle map derived directly from the vector ${M{(k)}},$ corresponding to the dynamic obstacles depicted in Fig. 3 (a). The two bands with lower gray levels represent the two dynamic obstacles respectively. Similarly, by analyzing these bands, the kinematics of all dynamic obstacles within the FOV can be observed.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Lidar Data Encoding", "weight": 1.0} -->

In order to validate the effectiveness of our lidar data encoding approach, a control group utilizing raw lidar data as input has been included while training the agent. Fig. 3 (c) illustrates the corresponding learning curve, which indicates that our proposed lidar data encoding approach leads to quicker convergence and achieves significantly higher final reward values compared to the control group.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Learning of dynamic obstacle avoidance", "weight": 1.0} -->

In this subsection, we employ deep reinforcement learning to train a neural network capable of navigating the quadrotor through complex environments replete with dynamic obstacles.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C1 Problem Formulation", "weight": 1.0} -->

The overall strategy involves training a universal policy leveraging deep reinforcement learning to control the acceleration of the quadrotor to fly through the obstacles.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C1 Problem Formulation", "weight": 1.0} -->

The problem is formulated as a Markov Decision Process (MDP), which is a discrete-time stochastic control process. The process can be formulated as a quadruple $M = {(\mathcal{S},\mathcal{A},\mathcal{P},\mathcal{R})}$, where $\mathcal{S}$ is the state space, $\mathcal{A}$ is the action space, $P{(\mathcal{S},\mathcal{S}')}$ is the probability that the action of the agent causes the state to transform from $S$ to $S'$, and $\mathcal{R}{(\mathcal{S},\mathcal{S}')}$ is the reward that the agent received after the state to transform from $\mathcal{S}$ to $\mathcal{S}'$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-C1 Problem Formulation", "weight": 1.0} -->

The reinforcement learning problem aims to adjust the policy $\pi$, in order to maximize the accumulated reward of the MDP $M$ with a discount ratio $\gamma$: The state $S$ is the combination of the observation $\mathcal{O}$ and the environment parameters. The observation $\mathcal{O} \in {\lbrack{M{(t)}},{S{(t)}},{C{(t)}}\rbrack}$ contains the obstacle map ${M{(t)}} \in {\mathbb{R}}^{36 \times 36}$, the state of the quadrotor ${S{(t)}} \in {\mathbb{R}}^{1 \times 4}$, and the command input ${C{(t)}} \in {\mathbb{R}}^{1 \times 2}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-C1 Problem Formulation", "weight": 1.0} -->

The obstacle map ${M{(t)}} \in {\mathbb{R}}^{36 \times 36}$ is constructed with multiple historical lidar scan results, processed through a Residual Network (ResNet) encoder to extract low-dimensional features. The state of the quadrotor ${S{(t)}} \in {\mathbb{R}}^{4}$ contains the current velocity and the acceleration output in the previous frame. Velocity data is acquired directly from the Unity environment during training and from the velocity estimator of the PX4 flight controller in real-world quadrotor deployment. The command input ${C{(t)}} \in {\mathbb{R}}^{2}$ comes from the user or the higher-level planner, representing the horizontal target position relative to the quadrotor. The action $\mathcal{A} \in {\mathbb{R}}^{2}$ comprises acceleration commands in the horizontal axes, executed by PX4 to adjust the attitude and thrust of the quadrotor during real-world deployment.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-C1 Problem Formulation", "weight": 1.0} -->

The reward $\mathcal{R}$ is computed through a series of reward functions based on the state of the quadrotor. Detailed information on the design of the reward functions will be stated in the subsequent subsection.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-C2 Reward Function Design", "weight": 1.0} -->

The reward function is designed to assess the actions of the quadrotor and provide the agent with feedback. Each component of the state contributes uniquely to the overall reward, influencing it in distinct ways.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-C2 Reward Function Design", "weight": 1.0} -->

The velocity reward, denoted as $r_{v}{(t)}$, serves to constrain the velocity of the quadrotor $v{(t)}$ within a specified range between the maximum velocity $v_{max}$ and the minimum velocity $v_{min}$. The computation of the velocity reward can be formulated as: The progress reward, denoted as $r_{p}{(t)}$, prompts the quadrotor to navigate towards the designated goal position $p_{goal}$. The computation of the progress reward can be expressed as: where $p{(t)}$ is the position of the quadrotor.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-C2 Reward Function Design", "weight": 1.0} -->

The jerk reward, denoted as $r_{j}{(t)}$, acts as a punishment against impractical maneuvers resulting from sudden changes in acceleration $a{(t)}$ of the simulated quadrotor. The computation of the jerk reward can be formulated as: The obstacle avoidance reward, denoted as $r_{o}{(t)}$, plays a crucial role in penalizing the proximity of the quadrotor to static obstacles. Introducing a safety distance $d_{s}$, we utilize a distance function to assess the distance from the quadrotor to obstacles at a given position. The computation of the obstacle avoidance reward can be expressed as: where $d{(t)}$ is the distance from the quadrotor to the closest point on the closest obstacle.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-C2 Reward Function Design", "weight": 1.0} -->

The dynamic obstacle reward, denoted as $r_{d}{(t)}$, aims to prompt the quadrotor to keep out from the future trajectory of dynamic obstacles. A dilation ratio $k^{i}{(t)}$ is employed to amplify the distance reward in the direction of movement of the dynamic obstacle. Assuming there are $n$ dynamic obstacles within the training environment, the dilation ratio for dynamic obstacle $i$ can be calculated: where $v^{i}{(t)}$ represents the linear velocity of dynamic obstacle $i$ under the global coordinate frame, $c^{i}{(t)}$ indicates the clearance distance from the quadrotor to the extended line of the velocity vector of this dynamic obstacle, and $\theta^{i}{(t)}$ denotes the included angle between the velocity vector of the obstacle and the vector from the obstacle to the quadrotor (see Fig. 4 (b)). Fig. 4 (c) illustrates the curve of the dilation ratio when ${v^{i}{(t)}} = 5$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C2 Reward Function Design", "weight": 1.0} -->

The overall dynamic obstacle reward $r_{d}{(t)}$ can be computed as: where $d^{i}{(t)}$ indicates the distance from the quadrotor to dynamic obstacle $i$. Fig. 4 (b) illustrates an instance of dynamic obstacle reward.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C2 Reward Function Design", "weight": 1.0} -->

The hovering reward, denoted as $r_{h}{(t)}$, gives additional rewards to the agent as the quadrotor approaches the goal point and its distance to the goal point is within a threshold distance $g_{h}$. It encourages the quadrotor to sustain a stable hover over the goal point until a new goal is designated. The computation of the hovering reward can be expressed as: The total reward $\mathcal{R}$ at time $t$ is given: where $k_{a}$, $k_{v}$, $k_{g}$, $k_{p}$, $k_{j}$, $k_{o}$, and $k_{h}$ represent the weights assigned to each component of the reward function, $a{(t)}$ is the acceleration of the quadrotor. Additionally, $r_{b}$ denotes the fundamental reward value the agent receives in each step if the quadrotor has not collided with any obstacles.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-C3 Policy Training", "weight": 1.0} -->

Unity is a powerful engine that facilitates kinematics simulation and provides relevant interfaces. With the Unity Machine Learning Agents Toolkit (ML-Agents), it is very convenient to build up a reinforcement learning environment by calling the related APIs, so we choose it as the training platform. The policy is trained with the Proximal Policy Optimization algorithm (PPO), where the Actor network is defined as Fig. 2, and the Critic network is embedded in ML-Agents. We employ 4 parallel agents to train the policy, and the training timescale has been set to 10.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-C3 Policy Training", "weight": 1.0} -->

In Fig. 4 (a), the training environment is depicted, where each quadrotor operates within a square arena. At the beginning of every training episode, the side length of the arena is randomly set between 10 $m$ to 20 $m$. Simultaneously, static obstacles with randomized positions, rotations, and scales are generated. Additionally, a random goal position, maintaining a safe distance of 1 $m$ from any of the static obstacles, is specified. 5 dynamic obstacles, ranging in scale from 0.1 $m$ to 1 $m$, appear randomly at the edges of the arena. These dynamic obstacles move at random speeds from 1 $m/s$ to 6 $m/s$, and will be reset if collide with the edges of the arena. When a dynamic obstacle has been reset, it possesses a $50\%$ probability of moving towards the position of the quadrotor or moving in a random direction otherwise.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-C3 Policy Training", "weight": 1.0} -->

Each training episode has a step limit of 2000. If this limit is reached, the current episode concludes. In the event that a collision occurs before reaching the step limit, an additional punishment will be applied to the reward function, and the training episode will be terminated earlier.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we showcase our simulation tests and real-world experiments aimed at validating the effectiveness of the method proposed in this paper.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A Evaluations in Simulation", "weight": 1.0} -->

To evaluate and compare the performance of our methodology against existing approaches, we design 5 distinct simulation environments for benchmarking purposes. Each environment is confined within a ${{20m} \times 20}m$ test ground enclosed by walls. Dynamic obstacles within these test grounds are characterized by random velocities ranging from 0 $m/s$ to 4 $m/s$, moving in random directions. In addition, the movement direction and velocity of dynamic obstacles underwent continual changes.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Evaluations in Simulation", "weight": 1.0} -->

Illustrations of the simulation environments are shown in Fig. 5. We execute the simulations on a desktop system featuring an i5-13600KF CPU and an RTX 4060 Ti GPU, operating on Ubuntu 20.04. For each scenario, we designate 10 random target points and assess the success rate of reaching these points without colliding with obstacles. Additionally, we record the average processing time, indicating the inference time for learning-based approaches or the combined perception and planning duration for optimization-based methods.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-A Evaluations in Simulation", "weight": 1.0} -->

In our comparative analysis, we establish control groups, which include a traditional optimization-based method outlined, as well as learning-based methods detailed in and. was initially developed for unmanned ground vehicles (UGVs) and features a distinct action space compared to quadrotors. Moreover, incorporates both lidar and RGB image data as input, which may not seamlessly align with our quadrotor application scenario. On the other hand, leverages the global map of the environment as input, disregarding the perception aspect entirely, thereby rendering it incompatible with point cloud data input.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-A Evaluations in Simulation", "weight": 1.0} -->

To ensure a fair and reasonable comparison, we introduce modifications to and, aligning them with our simulation environment. These modifications contain alterations in the observation and action spaces, alongside adjustments to the reward functions to suit these modifications. The adapted reward functions, observation space, and action space utilized are detailed in Tables I and II respectively.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-A Evaluations in Simulation", "weight": 1.0} -->

Table III demonstrates that our proposed approach exhibits superior efficiency and a higher success rate when navigating through environments populated with multiple high-speed dynamic obstacles. $\eta$ presents the success rate of reaching the goal position without collision. $t_{p}$ denotes the processing time per step in learning-based approaches and presents the planning duration in optimization-driven approaches. $v_{a}$ is the average velocity during the flight. $R_{l} = {{10 \ast l}/{\|{P_{g} - P_{s}}\|}}$ signifies the proportion between the path length and the direct path distance to the goal position, where $l$ denotes the path length, and $P_{g}$, $P_{s}$ represent the vectors of the initial and goal positions, respectively. While the above-mentioned methods achieve a decent success rate in environments with relatively low obstacle density, our approach maintains a decent success rate even as obstacle density increases, contrasting with the substantial success rate decline observed in the other methodologies. Our approach additionally attains the maximum average velocity across all five scenarios and attains the shortest path length in two of these scenarios.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-A Evaluations in Simulation", "weight": 1.0} -->

The perception module in experiences noticeable latency when processing point cloud data containing a large number of dynamic obstacles, leading to performance degradation. This latency significantly impacts the ability of the system to respond effectively in dynamic environments. Our processing time is shorter than both conventional and learning-based methods. Furthermore, the reward functions utilized in and are not finely tuned for scenarios involving dynamic obstacles, resulting in a decline in performance in environments with high-speed dynamic obstacles. These reward functions hinder the ability of the agents to navigate efficiently in challenging dynamic environments.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-A Evaluations in Simulation", "weight": 1.0} -->

To assess the impact of the proposed reward function concerning dynamic obstacles, a series of ablation experiments are conducted. The reward function is modified by eliminating the dynamic obstacle reward $r_{d}{(t)}$ and applying the reward function for static obstacles $r_{o}{(t)}$ instead to compute the penalty attributed to dynamic obstacles. Three scenarios are established by varying the average speeds of the dynamic obstacles in the third scenario outlined in Table III.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-A Evaluations in Simulation", "weight": 1.0} -->

Table IV illustrates the efficacy of the dynamic obstacle reward function in enhancing the success rate of navigation in highly dynamic environments. Furthermore, the enhancement in success rate attributed to the dynamic obstacle reward function becomes more pronounced as the average speed of dynamic obstacles increases.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B Implementation of Real-world Experiments", "weight": 1.0} -->

Our quadrotor platform design for real-world experiments features peripheral dimensions of 240 mm. The platform is equipped with propellers with all-around protection, ensuring the safety of experiments. This quadrotor platform is outfitted with a Morefine M6S onboard computer for neural network and odometry deployment, boasting an Intel N100 CPU and 12 GB of RAM. For sensing capabilities, it incorporates a Livox Mid-360 lidar with a wide field of view (FOV) of 360° horizontally and 59° vertically. The onboard computer runs on Ubuntu 20.04, and leverages Fast-Lio for odometry. In terms of flight control, the platform utilizes a mRo Pix-Racer Pro with PX4 firmware. With a total weight of 960 $g$, inclusive of a 1300 mAh battery, the platform offers a flight endurance time of 6.5 minutes.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-C High-speed Obstacle Avoidance", "weight": 1.0} -->

Our methodology showcases a notable advantage in evading high-speed dynamic obstacles. To evaluate its efficacy in such scenarios, we conduct an experiment involving obstacles flying at a high speed. In this experiment, we assign the quadrotor a fixed target position and throw balls toward it while it is hovering. The quadrotor autonomously maneuvers to avoid these incoming balls, and the motion capture system records the positional data of both the quadrotor and the balls.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-C High-speed Obstacle Avoidance", "weight": 1.0} -->

Throughout the experiment, our quadrotor is able to evade the ball flying at a speed up to 6 $m/s$, as illustrated in Fig. 6 (b) and (c). Utilizing a single neural network to handle various situations eliminates the need for the quadrotor to transition from a hovering state to a maneuvering state when faced with approaching obstacles. This reduces reaction times upon detecting dynamic obstacles within the field of view, enhancing performance in similar scenarios.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-C High-speed Obstacle Avoidance", "weight": 1.0} -->

Our system is also able to process scenarios involving multiple high-speed dynamic obstacles. Fig. 6 (a) showcases the quadrotor deftly maneuvering to avoid two balls flying towards it simultaneously while it is hovering.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-C High-speed Obstacle Avoidance", "weight": 1.0} -->

Furthermore, we also demonstrate that our quadrotor can avoid high-speed dynamic obstacles while navigating to a designated goal. Fig. 6 (d) shows that our quadrotor has successfully avoided multiple incoming balls while flying towards a goal at a speed of 2 $m/s$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-D Navigating in Cluttered Environments", "weight": 1.0} -->

To evaluate the practical efficacy of our approach in cluttered dynamic environments, we design five distinctive real-world scenarios.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-D Navigating in Cluttered Environments", "weight": 1.0} -->

Initially, we establish a foundational scenario to validate the core navigation functionality. Diverse boxes of varying shapes and sizes were randomly positioned as obstacles on the test ground. The quadrotor is assigned a target position 10 meters ahead of its takeoff point. Fig. 7 (a) shows the trajectory of the quadrotor as it navigates through the obstacles without collision.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-D Navigating in Cluttered Environments", "weight": 1.0} -->

Subsequently, we heighten the challenge by introducing three additional obstacles to the test ground while maintaining the same target position. The quadrotor successfully maneuvers through these obstacles, but its velocity is reduced due to the increased obstacle density. The trajectory of this scenario is illustrated in Fig. 7 (b).

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-D Navigating in Cluttered Environments", "weight": 1.0} -->

In the third scenario, we integrate three pedestrians into the environment, introducing dynamic obstacles among the static obstacles as the quadrotor flies through the test ground. Fig.7 (c) showcases the trajectory of the quadrotor, and it is able to take evasive maneuvers when a pedestrian obstructs its path.

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-D Navigating in Cluttered Environments", "weight": 1.0} -->

Expanding upon the complexity of the third scenario, pedestrians are tasked with altering the test ground layout by replacing obstacles in the flight path of the quadrotor. The quadrotor adeptly halts when facing an obstructing obstacle, subsequently recalibrating its route to avoid it. The trajectory of this experiment is depicted in Fig. 7 (d).

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-D Navigating in Cluttered Environments", "weight": 1.0} -->

To highlight the efficacy of our methodology under high-speed settings, the fifth scenario involves sparse obstacle placement, challenging the quadrotor to swiftly navigate through them. The quadrotor achieves a notable speed of 6 $m/s$, surpassing the outcomes of 3 $m/s$, and around 5 $m/s$. The trajectory of the quadrotor in this scenario is depicted in Fig. 7 (e).

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-D Navigating in Cluttered Environments", "weight": 1.0} -->

Across all of the scenarios, the quadrotor consistently maintains a hovering position at the designated target point upon arrival, awaiting commands for a new target destination. The series of scenarios demonstrate the adaptability and effectiveness of our navigation approach in maneuvering through dynamic cluttered environments.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we introduced a novel learning-based strategy designed for quadrotors to effectively navigate through highly dynamic and cluttered environments. Our methodology involved utilizing a lidar data processor to encode point cloud data into a range array. By stacking these range arrays into a 2D array, our neural network can discern dynamic obstacle features and execute appropriate evasive actions. We employed an end-to-end neural network for navigation, which controls the quadrotor by giving acceleration commands. A specialized reward function was applied to enhance its reaction against dynamic obstacles.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our approach showcased strong portability and excels across various dynamic environments, particularly in scenarios with high-speed obstacles. However, owing to the nature of end-to-end networks, the acceleration commands generated by the network may exhibit frequent fluctuations, and the current network framework was limited to obstacle avoidance within a horizontal plane. Future works may concentrate on expanding the maneuvering capabilities into three-dimensional space and enhancing overall stability.
