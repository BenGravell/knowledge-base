<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SIL-RRT*: Learning Sampling Distribution through Self Imitation Learning

Topics include Imitation learning, Motion planning, Robotics, Safety, Neural networks, Sampling-based methods, Planning, Learning, Sampling.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Efficiently finding safe and feasible trajectories for mobile objects is a critical field in robotics and computer science. In this paper, we propose SIL-RRT*, a novel learning-based motion planning algorithm that extends the RRT* algorithm by using a deep neural network to predict a distribution for sampling at each iteration. We evaluate SIL-RRT* on various 2D and 3D environments and establish that it can efficiently solve high-dimensional motion planning problems with fewer samples than traditional sampling-based algorithms. Moreover, SIL-RRT* is able to scale to more complex environments, making it a promising approach for solving challenging robotic motion planning problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning is a crucial field of study in robotics and computer science that focuses on finding a feasible and safe trajectory for a robot to achieve a desired goal. It involves determining a sequence of actions that will guide the robot from its initial state to the target, while avoiding collisions and satisfying various constraints, such as kinematic limitations, time constraints, and performance criteria. The significance of motion planning lies in its ability to enable robots to interact safely with their environment and carry out various tasks autonomously.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

As robots become more widely used and their applications increasingly complex, the motion planning problem demands algorithms that are both computationally tractable and efficient. This has led to the development of sampling-based algorithms, such as Probabilistic Roadmaps (PRM), Rapidly-exploring Random Trees (RRT), and RRT\*. These algorithms typically employ a uniform sampler, but when the dimension of the environment increases, the number of samples needed to find a feasible solution may also raise. To address this sampling efficiency problem, some researchers have introduced heuristic biased samplers, such as BIT\* and Informed RRT\*.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this study, we introduce SIL-RRT\*, a novel approach that enhances the Rapidly-exploring Random Tree Star (RRT\*) algorithm through the utilization of deep learning techniques. Unlike traditional methods that rely on Convolutional Neural Networks (CNNs) or Graph Neural Networks (GNNs), we adopt a Transformer-based architecture to capture the relationships between the state space and paths. This choice of architecture allows for greater flexibility and extensibility, enabling SIL-RRT\* to handle motion planning tasks across different dimensions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In SIL-RRT\*, the state space is represented by a list of point clouds sampled on the surface of obstacles, providing a comprehensive depiction of the environment, as shown in as Figure 1. Indeed, the technique we employed in SIL-RRT\* for representing obstacles using point clouds sampled from their surfaces is similar to the approach utilized in the work by Strudel et al.. This technique has been shown to be effective in representing obstacles in various dimensions. We trained SIL-RRT\* using a dataset collected within our Unity-based environment, enabling the algorithm to learn from a diverse range of scenarios.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To further enhance SIL-RRT\*, we incorporated a fine-tuning technique called weighted self-imitation learning (WSIL), which dynamically selects high-quality solutions from a fixed-size buffer. This approach eliminates the requirement of collecting near-optimal demonstrations by reusing successful records during the training process. This technique is particularly valuable in high-dimensional environments, where obtaining such demonstrations can be difficult.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In our experiments, extensive evaluations in diverse motion planning scenarios have demonstrated the effectiveness of SIL-RRT\*. The algorithm significantly reduces the number of samples required to solve new planning tasks, effectively leveraging prior experiences for improved performance in both 2D and 3D environments. Overall, our study contributes a cutting-edge motion planning approach, SIL-RRT\*, that combines deep learning, self-imitation learning, and a Transformer-based architecture to enhance the RRT\* algorithm for high-dimensional motion planning problems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The state space, $S$, is defined as a subset of ${\mathbb{R}}^{n}$. The obstacle state space, $S_{obs}$, and free state space, $S_{free}$, are defined as subsets of $S$. The initial state, $S_{init}$, is defined as an element of $S_{free}$, and the goal region, $S_{goal}$, is defined as a subset of $S_{free}$. A collision-free path, $\tau$, is defined as a continuous mapping from $\lbrack 0,1\rbrack$ to $S_{free}$ such that ${\tau{}} = S_{init}$ and ${\tau{}} \in S_{goal}$. The set of all collision-free paths is defined as $T$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The cost function, $c{( \cdot )}$, is used to evaluate paths and the optimal motion planning problem is to find the path, $\tau^{\ast}$, with the minimum cost among all paths in $T$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Transformer", "weight": 1.0} -->

Transformer is a powerful neural network architecture that is specially designed to process sequential data, such as text, speech, and time series. The architecture consists of stacks of self-attention layers with residual connections, allowing the model to selectively focus on relevant parts of the input sequence. In a typical Transformer model, the sequence of input vectors $\{ x_{1},x_{2},\ldots,x_{n}\}$ is transformed into key vectors $\{ k_{1},k_{2},\ldots,k_{n}\}$, query vectors $\{ q_{1},q_{2},\ldots,q_{n}\}$, and value vectors $\{ v_{1},v_{2},\ldots,v_{n}\}$ through linear transformations. The weighted sum of value vectors is computed using the self-attention mechanism where $Q$ denotes the query vectors, $K$ the key vectors, and $V$ the value vectors, with $d_{k}$ being the dimensionality of the key vectors.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Transformer", "weight": 1.0} -->

Attention mechanisms have proven to be effective in handling long-range dependencies within input data by dynamically selecting relevant information based on context. As a result, they have been utilized in fields beyond NLP, such as computer vision and reinforcement learning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Transformer", "weight": 1.0} -->

The Transformer architecture's ability to capture global dependencies and establish long-range relationships proves advantageous for managing the complexities inherent in motion planning tasks. SIL-RRT\* utilizes this capability to facilitate efficient and effective tree expansion, resulting in high-quality solutions in challenging environments.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Imitation Learning", "weight": 1.0} -->

Imitation learning is a machine learning technique where an agent learns to perform a task by imitating the actions of an expert. The goal of imitation learning is to enable the agent to learn from a set of expert demonstrations, rather than learning through trial and error in the environment. Imitation learning is particularly useful in cases where defining a reward function for the task is difficult or where direct interaction with the environment during learning is challenging or risky.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Imitation Learning", "weight": 1.0} -->

Imitation learning has been applied to various tasks, such as robotics, autonomous driving, and game playing. Many studies have explored the use of imitation learning to train agents in complex tasks, often with promising results.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Imitation Learning", "weight": 1.0} -->

We enhance our model using self-imitation learning, drawing from solutions created by RRT\* and SIL-RRT\*. These act as 'experts', contributing to the training data, fostering diverse learning experiences. This bolsters the model's robustness and reliability by imitating its effective solutions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Method", "weight": 1.0} -->

Imitation learning is a machine learning technique where an agent learns to perform a task by imitating the actions of an expert. The goal of imitation learning is to enable the agent to learn from a set of expert demonstrations, rather than learning through trial and error in the environment. Imitation learning is particularly useful in cases where defining a reward function for the task is difficult or where direct interaction with the environment during learning is challenging or risky.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Method", "weight": 1.0} -->

Imitation learning has been applied to various tasks, such as robotics, autonomous driving, and game playing. Many studies have explored the use of imitation learning to train agents in complex tasks, often with promising results.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Method", "weight": 1.0} -->

We enhance our model using self-imitation learning, drawing from solutions created by RRT\* and SIL-RRT\*. These act as 'experts', contributing to the training data, fostering diverse learning experiences. This bolsters the model's robustness and reliability by imitating its effective solutions.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Sampler Model Architecture", "weight": 1.0} -->

In the SIL-RRT\* framework, we employ a Transformer architecture to efficiently process point cloud data representing obstacles, subsequently generating a target sequence for navigation, as depicted in Figure 3. This architecture comprises two primary components: the State Space Encoder and the Decoder. The State Space Encoder transforms the raw point cloud data into a fixed-length vector representation, effectively capturing the spatial distribution of obstacles within the environment. The Decoder then uses this representation to methodically encode the tree's growth, enhancing the state space exploration efficiency while considering spatial constraints imposed by obstacles.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Sampler Model Architecture", "weight": 1.0} -->

State Space Encoder: Central to the SIL-RRT\* framework, this encoder processes the point cloud data sequence into a standardized, fixed-length representation. Given the computational intensity associated with traditional transformer architectures, we employ the Perceiver model, which adeptly handles the complexity and scale of input data. When presented with point cloud obstacles, noted as $p = {p_{1},p_{2},\ldots,p_{n}}$, with $n$ indicating the sequence's length, the encoder utilizes a cross-attention mechanism to project $p$ onto a compact, fixed-length latent representation $Z_{p}$. This is subsequently refined via a self-attention layer, enhancing its information content and structural integrity for downstream processing.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Sampler Model Architecture", "weight": 1.0} -->

Node Decoder: Utilizing the Perceiver-IO architecture, the Decoder processes the input sequence of tree nodes, represented as $x = {{goal},x_{1},x_{2},\ldots,x_{t}}$, where $t$ signifies the sequence's total node count. A causal attention mask ensures no future node information is encoded, maintaining the sequence's temporal integrity. Mirroring techniques from Decision Transformers, the model focuses only on the last five nodes of the sequence, balancing computational efficiency with predictive accuracy.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sampler Model Architecture", "weight": 1.0} -->

The decoding phase begins with a cross-attention layer that maps the latent array $Z_{p}$, derived from the State Space Encoder, onto the latent features $Z_{x}$ corresponding to the sequence $x$. This ensures the decoded features faithfully represent the encoded spatial information. A subsequent self-attention layer further refines these features, enhancing their representational utility. The process concludes with two Multilayer Perceptron (MLP) layers that calculate mean( $\mu$) and standard deviation ($\sigma$). These parameters define a multivariate normal distribution, from which samples are drawn to construct the RRT\*, enabling the generation of path samples that are both diverse and contextually informed by the environment's spatial layout.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sampler Model Architecture", "weight": 1.0} -->

In this study, we utilize feasible paths, denoted as $\tau = {x_{0},x_{1},x_{2},\ldots,x_{t}}$, sourced from planning algorithms or expert demonstrations, to guide our model. To enhance the diversity of our dataset, we introduce a novel data augmentation technique that involves random reversals of these paths. This approach substantially increases the variety of training data available. We aim to optimize our model by minimizing the negative log-likelihood loss, employing a multivariate normal distribution to accurately model the underlying data distribution. This precise estimation of data characteristics is critical for effective model training.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Sampler Model Architecture", "weight": 1.0} -->

The SIL-RRT\* algorithm operates through a structured multi-stage process, starting with the encoding of point clouds and goal positions, followed by decoding to form a tree structure, and concluding with the generation of samples essential for constructing the Rapidly-exploring Random Tree (RRT). This method effectively manages the intricate interactions between point cloud data and tree nodes, thus enabling the algorithm to deliver comprehensive navigation solutions for complex environments.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Sampler Model Architecture", "weight": 1.0} -->

During experimental trials, it was observed that the sampling mechanism occasionally struggles near goal states. This results in the generation of excessive samples in these areas and, at times, a failure to identify feasible paths. To address these challenges, we integrated the BiRRT\* algorithm, as detailed by Jordan and Pere, which utilizes alternating forward and backward tree expansions. This strategy has proven effective in overcoming the observed issues, significantly improving the algorithm's ability to find feasible paths through complex spaces.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Weighted Self Imitation Learning", "weight": 1.0} -->

In both supervised and imitation learning frameworks, the quality of expert demonstrations is paramount; however, acquiring optimal or near-optimal demonstrations presents considerable challenges. Within our proposed SIL-RRT\* framework, these challenges are exacerbated due to the inherent properties of Rapidly-exploring Random Trees (RRT), which prioritize solution feasibility over optimality. Consequently, our dataset inevitably comprises a mix of optimal and sub-optimal trajectories. This heterogeneity complicates the task of identifying and filtering out low-quality trajectories, potentially diminishing the performance and efficacy of the trained sampler model.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Weighted Self Imitation Learning", "weight": 1.0} -->

Addressing the need for high-quality demonstrations in imitation learning, several innovative methodologies have been developed. Self-Imitation Learning (SIL) as proposed by Oh et al., focuses on replicating an agent's past successful actions, effectively ignoring less successful ones. Complementary strategies such as 2IWIL and SAIL incorporate a quality weighting mechanism into Generative Adversarial Imitation Learning (GAIL), enhancing the learning process from a diverse array of expert demonstrations. Additionally, T-REX develops a reward function that evaluates demonstrations based on their quality and informativeness, prioritizing the most valuable examples.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Weighted Self Imitation Learning", "weight": 1.0} -->

To discern high-quality demonstrations within the SIL-RRT\* framework, we adopt a similar approach by using the length of each trajectory as a measure of its quality. We deploy a Deep Neural Network (DNN) as a predictive estimator to forecast the path length produced by the SIL-RRT\* using the current sampler model, as illustrated in Fig. 3. We introduce a threshold, denoted as $K$, to distinguish between superior and inferior demonstrations, based on the discrepancy between the actual and predicted path lengths. Each solution in our dataset is then weighted according to this measure, as specified by Equation: This methodological innovation aims to enhance the fidelity and utility of our dataset, thereby improving the overall performance of the training model.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Weighted Self Imitation Learning", "weight": 1.0} -->

SIL-RRT* with WSIL Average Samples Generated Average Path Length Average Samples Generated Average Path Length Average Samples Generated Average Path Length Table 1: Comparison of SIL-RRT* with RRT* and MPNetNR with the simple scenarios.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Weighted Self Imitation Learning", "weight": 1.0} -->

During the initial phase of training, because estimator is not well-trained; thus, we set $K$ to a large value to include more training samples. As the training progresses, we gradually decrease the value of $K$ to prioritize higher-quality demonstrations. We update $K$ in fixed steps by dividing it by $\mu$. This weight takes into account the difference between the length of the real path and the estimated path, with solutions that are shorter than predicted having a larger impact on our sampler model. During training, we update the parameters of our length estimator using the MSE loss function: {dmath} L_estimator = 12 ------ C_real-C_est ------ \^2 To fine-tuning our sampler model, we updated the negative log-likelihood loss loss function that takes into account both the weight of each solution. The loss function is defined as follows: Here, $B$ represents the batch size, $N$ denotes the number of nodes within a solution, $g$ is the goal state, and $p$ and $x$ correspond to the point cloud vectors and tree nodes, respectively.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Weighted Self Imitation Learning", "weight": 1.0} -->

To foster the exploration of novel paths by our sampler model, we focus on minimizing the Shannon entropy of the model's predicted distribution, symbolized as $H_{\theta}^{T}$. This loss function is pivotal for learning from high-quality demonstrations, as it aids in preventing the model from overfitting to solutions of inferior quality. The description of the algorithm can be found at reference 1.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Weighted Self Imitation Learning", "weight": 1.0} -->

Initialize S = {Scenario1, Scenario2, …, Scenarion} xinit, xgoal, xobs ← Sample(S) τ ← SIL-RRT*(xinit, xgoal, xobs) τ ← RRT(xinit, xgoal, xobs) Sample (τ, xinit, xgoal, xobs) from D Cest ← Estimator(xobs, xinit, xgoal) $w\leftarrow\frac{1}{\left({1 + e^{({C_{real} - C_{est} - K})}} \right)}$ θpolicy ← θpolicy − η∇θpolicyLpolicy θestimator ← θestimator − η∇θestimatorLestimator Algorithm 1 Weighted Self Imitation Learning

<!-- chunk {"id": "body-0034", "role": "body", "section": "Data Collection", "weight": 1.0} -->

We^11^1Refer to the supplementary material accompanying this paper for videos and more in-depth studies. utilized Unity to enhance the visualization and in- teraction of SIL-RRT\*. To enable a smooth data exchange between Unity and external processes, we implemented a socket communicator on both the Unity and Python sides, allowing an effective training of SIL-RRT\* through the exposure of registered functions. To ensure the versatility and robustness of SIL-RRT\*, we have designed and generated three distinct environments: 2D, rigid body, and 3D. Each environment consists of 100 unique workspaces, and within each workspace, we have created 50 different scenarios.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Data Collection", "weight": 1.0} -->

SIL-RRT* with WSIL Average Samples Generated Average Path Length Complex Rigid Body Average Samples Generated Average Path Length Average Samples Generated Average Path Length Average Samples Generated Average Path Length Table 2: Comparison of SIL-RRT* with the complex scenarios.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Data Collection", "weight": 1.0} -->

In each workspace, we positioned 10 randomly placed obstacles of varying sizes to increase the complexity of the environments and to pose challenges to the SIL-RRT\* algorithm.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Data Collection", "weight": 1.0} -->

For our training dataset, we employed the RRT\* algorithm to collect feasible paths across various scenarios, amassing a total of 5000 data samples. Each sample represents a viable path in the designated environment.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Data Collection", "weight": 1.0} -->

To evaluate the effectiveness and generalization capabilities of SIL-RRT\*, we created a comprehensive test dataset consisting of 100 workspaces, with each workspace featuring 10 unique scenarios. This dataset allows us to test SIL-RRT\* on unseen scenarios, assessing its performance relative to other methodologies. The complex structure of the test dataset, including environments with an increased number of obstacles, serves to examine the scalability of SIL-RRT\*.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Data Collection", "weight": 1.0} -->

In the test scenarios involving three distinct complex environments---2D, rigid body, and 3D---the number of obstacles was consistently set at 15. By subjecting SIL-RRT\* to these enhanced obstacle conditions, we aim to evaluate its performance and gather insights into its ability to scale and effectively navigate through more challenging environments.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Data Collection", "weight": 1.0} -->

To further test SIL-RRT\* in high-dimension scenarios, we designed a 2D space featuring a snake-shaped agent. This agent is composed of three links connected by two joints, creating a system with 5 degrees of freedom (DoF): the x and y positions of the first link, the rotation of the first link, and the angles of the two joints. To ensure the structural integrity of the agent, we restricted the joint angles to a range between -45 and 45 degrees, preventing the agent from folding upon itself. This setup allows us to explore the algorithm's capacity to handle high-dimensional movement and constraint scenarios effectively.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Results", "weight": 1.0} -->

In this study, we conducted a comprehensive performance benchmarking of SIL-RRT\* against two well-known motion planning algorithms: RRT\* and Motion Planning Networks with Neural Replanning (MPNetNR). Additionally, we compared the standard SIL-RRT\* with an augmented version incorporating Weighted Self-Imitation Learning (WSIL) to assess the impact of WSIL on algorithmic performance. All algorithms were implemented in Python and evaluated using a specially curated dataset. Notably, the Deep Neural Network (DNN) used in the experiments was executed on a CPU.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results", "weight": 1.0} -->

The experimental suite, including training phases, was conducted on a high-performance computing system equipped with a 3.60 GHz Intel Core i9 processor and a NVIDIA GeForce RTX 3090 GPU. Both SIL-RRT\* and MPNetNR were trained over 5000 iterations using a dataset where the number of point clouds representing obstacles was fixed at 1000. A distinction was made in the sampling method of the point clouds: SIL-RRT\* samples were taken from the surfaces of obstacles, whereas MPNetNR samples were sourced from their interiors.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Results", "weight": 1.0} -->

For testing in 2D and rigid body environments, the maximum number of samples per algorithm (RRT\*, SIL-RRT\*, MPNetNR) was set to 200. In contrast, for the 3D environments, which present increased complexity, the sample limit for RRT\* was raised to 400, while SIL-RRT\* and MPNetNR maintained a cap of 200 samples.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results", "weight": 1.0} -->

The goal region for all tested scenarios was uniformly set to 1. Importantly, the paths generated by these algorithms underwent no additional post-processing techniques such as path smoothing or lazy state contraction. This decision was made to ensure the evaluation of the algorithms' raw performance and facilitate a direct comparison in their original operational state.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Results", "weight": 1.0} -->

Fig. 4 presents search trees by SIL-RRT\* and other planners for a selection of scenarios from the test dataset. As demonstrated, SIL-RRT\* is capable of identifying near-optimal solutions across various environments with fewer nodes expanded.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Results", "weight": 1.0} -->

Table 1 presents the performance of SIL-RRT\* in scenarios across different environments, including 2D, rigid body, and 3D. The results are evaluated based on success rate, number of samples, path length, and computation time. To minimize the impact of probabilistic factors, we executed tree trials for each environment and calculated the mean and standard deviation of each property. The results demonstrate that SIL- RRT\* outperforms RRT\* and MPNetNR in terms of iden- tifying feasible solutions with reduced sample requirements and computation time across all environments. Furthermore, SIL-RRT\* produces high-quality paths compared to the other algorithms.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Results", "weight": 1.0} -->

We also conducted a comparison between SIL-RRT\* using a pretrained model and one that underwent fine-tuning by WSIL. The results revealed that WSIL improved the quality of paths generated by SIL-RRT\*, although it slightly in- creased the number of samples required.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Results", "weight": 1.0} -->

MPNetNR showed a poor performance in the 2D and rigid body scenarios. This discrepancy is attributed to the size of our dataset, which is smaller than the dataset used. Additionally, the density of obstacles in our scenarios may have posed additional challenges for MPNetNR.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Results", "weight": 1.0} -->

These findings highlight the effectiveness of SIL-RRT\* in generating high-quality paths while considering computational efficiency. The comparison with RRT\* and MPNetNR underscores the advantages of our approach in scenarios with dense obstacles and limited dataset sizes.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results", "weight": 1.0} -->

To evaluate the scalability of SIL-RRT\*, we conducted 4 additional trials on a more complex dataset. We utilized the same evaluation metrics as in the 10-obstacle dataset. The results of these trials are summarized in Table 2 showing that our algorithm successfully handles more complex environments than those encountered during training. This finding highlights the adaptability and robustness of our method, as it performs well even in scenarios with increased environmental complexity.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion and Limitation", "weight": 1.5} -->

This study introduces SIL-RRT\*, an innovative sampling-based algorithm developed to augment the efficiency of the Rapidly-exploring Random Tree (RRT) algorithm. Central to SIL-RRT\* are two transformer architecture neural networks, serving as the sampler and estimator networks. These networks are responsible for generating samples and forecasting the length of solutions, respectively. To enhance SIL-RRT\*'s performance, we implement a weighting mechanism that assigns values to each solution, predicated on the deviation between the actual solution length and its predicted counterpart. This weighting system is instrumental in assessing solution quality and mitigating the influence of suboptimal solutions within the framework of self-imitation learning.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion and Limitation", "weight": 1.5} -->

The empirical investigations conducted across diverse environments and configurations unequivocally demonstrate SIL-RRT\*'s superior performance relative to competing methodologies. The findings reveal that SIL-RRT\* markedly enhances the convergence rate, diminishes the requisite number of samples, and facilitates the generation of solutions of superior quality. Collectively, these results position our proposed method as a notably promising solution to the motion planning quandary in robotics.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion and Limitation", "weight": 1.5} -->

While SIL-RRT\* has exhibited commendable performance using a constrained dataset and demonstrated the capacity to learn from generated paths, its dependency on substantial datasets for training remains a notable limitation. Procuring such extensive datasets becomes increasingly difficult in complex scenarios. As a prospective avenue for research, we propose exploring the integration of adaptive reinforcement learning (RL) techniques with the RRT\* framework. This innovative approach would empower the algorithm to autonomously learn optimal paths, thereby obviating the need for extensive pre-collected datasets and potentially enhancing its applicability in diverse and intricate environments.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion and Limitation", "weight": 1.5} -->

A notable limitation of SIL-RRT\* lies in its presupposition of uniformity in the size and form of point-mass and rigid-body objects, a constraint that complicates applications involving robots of varying sizes or shapes. The algorithm's ability to generalize its learned knowledge to larger robots is, consequently, hindered. To surmount this challenge, our forthcoming research endeavors will involve the integration of robot size and shape considerations into our models. By incorporating these specific robot characteristics, we aim to significantly improve SIL-RRT\*'s versatility in accommodating diverse robot configurations, thereby expanding its applicability in robotics.
