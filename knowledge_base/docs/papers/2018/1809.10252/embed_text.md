## Introduction

Sampling-based Motion Planners (SMPs) have emerged as a promising framework for solving high-dimensional, constrained motion planning problems. SMPs ensure probabilistic completeness, which implies that a probability of finding a feasible path solution, if one exists, approaches to one as the limit of the number of randomly drawn samples from an obstacle-free space increases to infinity. However, despite their ability to compute motion plans irrespective of the obstacles geometry, these methods exhibit slow convergence to computing path solutions due to their reliance on the extensive exploration of a given obstacle-free configuration space. Recent research shows that biasing a sample distribution towards the region with high probability of finding a path solution can considerably enhance the performance of classical single-query SMPs such as RRT and RRT\*. To the best of our knowledge, there does not exist any effective and reliable solution that uses the knowledge from the past planning problems to bias the sample distributions towards the region of the configuration space containing an optimal path solution.

In this paper, we propose a neural network-based adaptive sampler that generates samples in particular regions of a configuration space where there is likely to exist an optimal path solution. Our method consists of two neural models, i.e., an obstacle-space encoder and random samples generator. We use a Contractive AutoEncoder (CAE) for the encoding of an obstacle-space into an invariant, robust feature space. A samples generator that comprises a Dropout-based stochastic Deep Neural Network (DNN) that takes the obstacle-space encoding, start and goal configuration as an input, and generates samples distributing over the region of configuration space containing the path solutions. We evaluate our method on various complex motion planning tasks such as planning of a rigid-body (piano-mover problem) and 6 degree-of-freedom (DOF) robotic arm (UR6), and planning through narrow passages. We also benchmark our method against existing biased-sampling based state-of-the-art SMPs including Informed-RRT\* and Batch Informed Trees (BIT\*). The results show that our algorithm generates samples that enable unbiased SMPs such as RRT\* to compute near-optimal paths in a considerably lesser computational time than BIT\* and Informed-RRT\*.

## Related Work

Many biased-sampling heuristics have been proposed to enhance the computational speed of RRT and its variants. For instance, Rickert et al. used gradient information to balance exploration and exploitation. Urmson and Simmons method heuristically biased samples in RRT while Ferguson and Stentz presented the anytime RRT algorithm by using multiple independent RRTs. Although these methods are useful, they lack asymptotic optimality due to the underlying RRT algorithm.

RRT\* extends RRTs to guarantee asymptotic optimality by incrementally rewiring the RRT graph connections such that the shortest path is asymptotically guaranteed. However, to determine an $\epsilon$-near optimal path in $d \in {\mathbb{N}}$ dimensions, roughly $O{({1/\epsilon^{d}})}$ samples are required, which makes RRT\* no better than grid search methods. Likewise, experiments in also confirmed that RRT\* exhibits slow convergence rates to optimal path solution in higher-dimensional spaces. The following sections discusses various existing biased/adaptive sampling methods to speed up the convergence rate of SMPs to compute optimal/near-optimal path solution.

### II-A Adaptive Sampling Methods

Gammell et al. proposed the Informed-RRT\* algorithm which takes an initial solution from RRT\* algorithm to define an ellipsoidal region from which new samples are drawn to minimize the initial solution for a given cost function. Although Informed-RRT\* demonstrated enhanced convergence towards an optimal solution, this method suffers in situations where finding an initial path solution takes most of the computation time. To address this limitation, Gammell et al. proposed Batch Informed Trees (BIT\*). BIT\* is an incremental graph search technique where an ellipsoidal subset, containing configurations to update the graph, is incrementally enlarged. BIT\* is shown empirically to outperform prior methods such as RRT\* and Informed-RRT\*. However, confining a graph search to ellipsoidal region slows down the performance of an algorithm in maze-like scenarios especially where the start and goal configurations are very close to each other, but the path among them traverses a complicated maze stretching waypoints far away from the goal. Furthermore, such a method would not translate to non-stationary environments or unseen environments.

### II-B Learning-based Search Methods

Many approaches exist that use learning to improve classical SMPs computationally. A recent method called a Lightning Framework stored paths into a lookup table and used a learned heuristic to write new paths as well as to read and repair old paths. Another similar framework by Coleman et al. is an experience-based strategy to cache experiences in a graph instead of individual trajectories. Although these approaches exhibit superior performance in higher-dimensional spaces when compared to conventional planning methods, lookup tables are memory inefficient and incapable of generalizing well to new planning problems. Zucker et al. proposed a reinforcement learning-based method to bias samples in discretized workspaces. However, reinforcement learning-based approaches are known for their slow convergence as they require a large number of interactive experiences.

(c) Online: Neural Sampling

Figure 1: DeepSMP consists of two neural models, a Contractive AutoEncoder (CAE), and a stochastic deep feedforward neural network (DeepSampler). These models are trained offline and are used to generate samples during online execution incrementally.

## Problem Definition

This section presents the notations we will be using in this paper, along with the definitions of fundamental motion planning problems addressed by our work.

Let $S$ be a list of finite length $N \in {\mathbb{N}}$ then $S_{i}$ is a mapping from a given index $i \in {\mathbb{N}}$ to an element of $S$ at $i$-th index. For algorithms described in our paper, $S_{0}$ and $S_{T}$ corresponds to the initial and last elements of a list, respectively. Let a given state space be denoted as $X \subset {\mathbb{R}}^{d}$, where $d \in {\mathbb{N}}_{\geq 2}$ denotes the dimension of a state space. The collision and collision-free state spaces are denoted as $X_{obs} \subset X$ and $X_{free} = {X\backslash X_{obs}}$, respectively. Let the initial state and goal region be represented as $x_{init} \in X_{free}$ and $X_{goal} \subset X_{free}$, respectively. Let a trajectory be denoted as a non-empty finite-length list $\sigma:{{\lbrack 0,T\rbrack} \subset X}$. For a given path planning problem, a trajectory $\sigma$ is said to be feasible if it connects $x_{init}$ and $x \in X_{goal}$, i.e. $\sigma_{0} = x_{init}$ and $\sigma_{T} \in X_{goal}$, and a path formed by connecting all consecutive states in $\sigma$ lies entirely in the obstacle-free space $X_{free}$ i.e.,\
Problem 1 (Feasible Path Planning) Given a triplet $\{ X,X_{free},X_{obs}\}$, an initial state $x_{init}$ and a goal region $X_{goal} \subset X_{free}$, find a path $\sigma:{{\lbrack 0,T\rbrack}\rightarrow X_{free}}$ such that $\sigma_{0} = x_{init}$ and $\sigma_{T} \in X_{goal}$.\
Let a cost function $c{( \cdot )}$ computes a cost of a given path $\sigma$ in terms of a summation of Euclidean distances between all the consecutive states in $\sigma$. Let a set of all feasible path solutions to a given planning problem be denoted as $\Pi$. The optimality problem of motion planning is then to find the optimal, feasible, path solution $\sigma^{\ast} \in \Pi$ that has a minimum cost among all other feasible path solutions i.e.,\
Problem 2 (Optimal Path Planning) Assuming that multiple solutions to Problem 1 exists, find a path $\sigma^{\ast} \in \Pi$ such that ${c{(\sigma^{\ast})}} = {\{{\min_{\sigma \in \Pi}c{(\sigma)}}\}}$.\
Let $\Omega \subset X_{free}$ be a potential region containing optimal/near-optimal path solution. The problem of adaptive sampling, also known as biased sampling, is to generate collision-free samples $x \in \Omega$ such that SMPs compute the optimal path $\sigma^{\ast}$ in a least possible time $t \in {\mathbb{R}}$. The problem of adaptive sampling is formalized as follow.\
Problem 3 (Adaptive Sampling) Given a planning problem $\{ x_{init},X_{goal},X\}$, generate samples $x \in \Omega$, where $\Omega \subset X_{free}$, such that the sampling-based motion planning methods compute optimal path solution $\sigma^{\ast}$ in a least-possible time $t \in {\mathbb{R}}$.

## Informed Neural Sampler

This section presents our novel informed neural sampling algorithm called DeepSMP^11^1Supplementary material is available at sites.google.com/view/deepsmp. It comprises two neural modules. The first module is an autoencoder which learns an invariant and robust feature space to embed a point cloud data from obstacle space. The second module is a stochastic DNN which takes obstacles encoding, start and goal configurations to generate samples incrementally for SMPs during online execution. Note that any SMP can utilize these informed samples for rapid convergence to the optimal solution and that the method works for unseen environments via the obstacle space encoding. The following sections describe both neural modules, online sample generation heuristic called DeepSMP, dataset collection, and hyper-parameters initialization.

### IV-A Obstacle Encoding

A Contractive AutoEncoder (CAE) is used to learn a latent-space embedding $Z$ of a raw point cloud data ${\mathbf{x}}_{\mathbf{o}\mathbf{b}\mathbf{s}} \subset X_{obs}$ (see Fig. 1 (a)). The encoder and decoder functions of CAE are denoted as $f{({\mathbf{x}}_{\mathbf{o}\mathbf{b}\mathbf{s}};{\mathbf{θ}}^{e})}$ and $g{({f{({\mathbf{x}}_{\mathbf{o}\mathbf{b}\mathbf{s}})}};{\mathbf{θ}}^{d})}$, respectively, where ${\mathbf{θ}}^{e}$ and ${\mathbf{θ}}^{d}$ are parameters of their corresponding approximating functions. CAE is trained through unsupervised learning using the following objective function.

where ${\|{{\mathbf{x}} - {g{({f{({\mathbf{x}})}})}}}\|}^{2}$ is a reconstruction loss, and $\lambda{\sum_{ij}{(\theta_{ij}^{e})}^{2}}$ is a regularization term with a coefficient $\lambda$. Furthermore, $D_{obs}$ contains a dataset of point clouds ${\mathbf{x}}_{\mathbf{o}\mathbf{b}\mathbf{s}} \subset X_{obs}$ from $N_{obs} \in {\mathbb{N}}$ different workspaces. The regularization term allows the feature space $Z:={f{({\mathbf{x}}_{\mathbf{o}\mathbf{b}\mathbf{s}})}}$ to be contractive in the neighborhood of the training data which results in an invariant and robust feature learning.

### IV-A1 Model Architecture

Since the decoding function $g{({f{({\mathbf{x}}_{\mathbf{o}\mathbf{b}\mathbf{s}})}})}$ is an inverse of encoding function $f{({\mathbf{x}}_{\mathbf{o}\mathbf{b}\mathbf{s}})}$, we present the architectural details of encoding unit only.

The encoding function consists of three fully-connected linear hidden layers followed by an output linear layer. The output from each hidden layer is passed through a Parametric Rectified Linear Unit (PReLU).

For 2D workspaces, the input point cloud is of size $1400 \times 2$ where three hidden layers transform the inputs to 512, 256 and 128 units, respectively. The output layer takes 128 units and transforms them to latent space embedding $Z$ of size 28 units. The decoding function takes the latent space embedding Z to reconstruct the raw point cloud data.

For 3D workspaces, the hidden layers 1, 2 and 3 transform the input point cloud $1400 \times 3$ to 786, 512, and 256 hidden units, respectively. Finally, the output layer transforms the 256 units from preceding hidden layer to a latent space of size 60 units.

### IV-B Deep Sampler

Deep Sampler is a stochastic feedforward deep neural network with parameters $\mathbf{θ}$. It takes obstacles encoding $Z$, robot state $x_{t}$ at step $t$, and goal state $x_{T}$ to produce a next state ${\hat{x}}_{t + 1} \in X_{free}$ that would take a robot closer to the goal region (see Fig. 1(b)) i.e.,

We use RRT\* to produce near-optimal paths to train DeepSMP. The training paths are in the form of a tuple i.e., $\sigma^{\ast} = {\{ x_{0},x_{1},\cdots,x_{T}\}}$, such that the path formed by connecting all following states in $\sigma^{\ast}$ is a feasible solution. The training objective is to minimize mean-squared-error (MSE) between the predicted states ${\hat{x}}_{t + 1}$ and the actual states $x_{t + 1}$ given by RRT\*, i.e.,

where $N_{p} \in {\mathbb{N}}$ corresponds to the total number of paths $\hat{N}$ times their path lengths.

### IV-B1 Model Architecture

Deep Sampler is a twelve-layer deep neural network where each hidden layer is a sandwich of a linear layer, PReLU and Dropout ($p$) with an exception of last hidden layer which does not contain Dropout ($p$). The twelveth layer is an output layer which takes hidden units from preceding layer and transforms them to the desired output size which is equal to the dimension of robot configurations. The configurations for the 2D point-mass robot, 3D point-mass robot, rigid-body and 6 DOF robot have dimensions 2, 3, 3 and 6 respectively. For all presented problems, except planning of 6 DOF robot, the input to Deep Sampler is given by concatenating the obstacles' representation $Z$, robot's current state $x_{t}$ and goal state $x_{T}$. For 6 DOF, we assume a single environment, therefore, the input to Deep Sampler comprises of current state $x_{t}$ and goal state $x_{T}$ only.

### IV-C Online Execution of DeepSMP

During the online phase, we use our trained obstacle encoder and DeepSampler to generate random samples for a given SMP. Fig. 1 shows the flow of information between encoder $f{({\mathbf{x}}_{\mathbf{o}\mathbf{b}\mathbf{s}})}$ and DeepSampler. Algorithm 1 outlines DeepSMP which combines our informed neural sampler with any classical SMP such RRT\*.

1 Initialize SMP(xinit, xgoal, X)
7 xrand ← DeepSampler (Z,xrand,xgoal)
15 if xrand ∈ Xgoal then
Algorithm 1 DeepSMP(xinit, xgoal, xobs)

Algorithm 1 starts by initializing a given SMP (Line 1). The obstacles encoder $f{({\mathbf{x}}_{\mathbf{o}\mathbf{b}\mathbf{s}})}$ provides an encoding $Z$ of a raw point cloud data from $X_{obs}$ (Line 3). DeepSMP algorithm runs for $n \in {\mathbb{N}}$ iterations (Line 4). DeepSampler incrementally generates samples between given start and goal configurations until $i < n^{limit}$ (Line 5-6), where $n^{limit} < n$. Upon reaching a given goal configuration, DeepSampler is executed again to produce samples from a given start configuration to the goal configuration by re-initializing random sample $x_{rand}$ to $x_{init}$ (Lines 10-11). After $n^{limit}$ iterations, DeepSMP switches to random sampling (Line 7-8) to ensure completeness guarantees of an underlying SMP. Note that $\sigma$ is a feasible path solution returned by SMP. The path $\sigma$ is continually optimized for a given cost function $c{( \cdot )}$ for a given number of iteration $n$. Finally, after $n$ iterations, a feasible, optimized path solution $\sigma$, if one exists, is returned as a solution to a given planning problem (Lines 12-13).

### IV-D Data Collection

The data collection consists of creating a random set of workspaces, sampling collision-free start and goal configurations in those workspaces, and generating paths using a classical motion planner for every start and goal pair. The following sections describe the procedure to create workspaces, start and goal pairs, and near-optimal paths.

### IV-D1 Workspaces

Many different 2D and 3D workspaces were generated by randomly placing various quadrilateral blocks without repetition in the operating region of $40 \times 40$ and $40 \times 40 \times 40$, respectively. Each random placement of the obstacle blocks led to a different workspace.

### IV-D2 Start and goal configuration

For each generated workspace, a number of start and goal configurations were sampled randomly from its obstacle-free space.

### IV-D3 Near-optimal paths

Finally, for each generated start and goal pair within all workspaces, a feasible, near-optimal path was generated using the RRT\* motion planner.

Complete dataset comprised 110 different workspaces for the presented scenarios in the results section i.e., simple 2D (s2D), complex 2D (c2D), complex 3D (c3D), and rigid-body (rigid). The training dataset contained 100 workspaces with 4000 training paths in every workspace. There were two types of test datasets. The first test dataset comprised already seen 100 workspaces with 200 unseen start and goal configurations in each of the workspaces. The second test dataset comprised entirely unseen 10 workspaces where each contained 2000 unseen start and goal configurations. For rigid-body case, the range of angular configuration was scaled to the range of positional configurations, i.e., $- 20$ to $20$, for training and testing. In case of 6 DOF robot, we consider only a single environment thus no environment encoding is included, and only start and goal configurations are sampled to collect example trajectories from collision-free space to train our feedforward neural network (DeepSampler). The test scenario for 6 DOF robot is to generate paths for unseen start and goal pairs.

### IV-E Hyper-parameters

DeepSMP neural models were trained in mini-batches using Adagrad optimizer with a learning rate of $0.1$. CAE was trained on raw point cloud data from $N_{obs} = {30,000}$ different workspaces which were generated randomly as described earlier. The regularization coefficient $\lambda$ was set to $10^{- 3}$. For DeepSampler, Dropout probability $p$ was kept constant to 0.5 for both training and testing. The number $n^{limit}$ is set to the number of nodes in the longest path available in the training data. For RRT\*, gamma of ball-radius was set to 1.6 whereas tree extension step sizes for point-mass and rigid-body were kept at 0.01 and 0.9, respectively. Finally for the 6-DOF robot, we use OMPL's RRT\* and ROS with their default parameter settings for path generation.

Figure 2: DeepSMP in simple 2D environments (s2D).

Figure 3: DeepSMP in complex 2D environments (c2D). The path and goal are indicated in red and blue colors, respectively.

## Results

This section presents the results of DeepSMP for the motion planning of a point-mass robot, rigid-body, and Universal 6 DOF robot (UR6) in both 2D and 3D environments. All experiments were carried out on a computer with 3.40GHz$\times$ 8 Intel Core i7 processor with a 16 GB RAM and GeForce GTX 1080 GPU. DeepSMP, implemented in PyTorch, was compared against Informed-RRT\* and BIT\* implemented in Python. In the following results, the datasets $seen$-$X_{obs}$ and $unseen$-$X_{obs}$ comprised 100 workspaces seen by DeepSMP during training and 10 workspaces not seen by DeepSMP during training, respectively. Both test datasets $seen$-$X_{obs}$ and $unseen$-$X_{obs}$ contained 200 and 2000 unseen start and goal configurations, respectively, for every workspace. Note that every combination of either seen or unseen environment with unseen start and goal pair constitutes a new planning problem, i.e., not seen by DeepSMP during training. For each planning problem, we ran 20 trials of all presented SMPs to calculate the mean computational time.

Figure 4: DeepSMP generating samples in complex 3D environments (c3D). The obstacles, indicated as blocks in beige color, are made slightly transparent to display path profiles behind them.

Figs. 2-5 show different example scenarios named as simple 2D (s2D), complex 2D (c2D), complex 3D (c3D) and rigid-body (rigid) where DeepSMP with underling RRT\* method is planning motions. The mean computational time (in seconds) and iterations took by DeepSMP for each scenario are denoted as $t$ and $n$, respectively.

Table I presents the mean computational time comparison of DeepSMP with an underlying RRT\* SMP against Informed-RRT\* and BIT\* for computing near-optimal paths in different environments s2D, c2D, c3D and rigid. Note that, unbiased RRT\* method is not included in the comparison as the computation time of RRT\*, for computing near-optimal paths, is much higher than all presented algorithms. We report the mean ($t_{mean}$), maximum ($t_{\max}$), and minimum ($t_{\min}$) time taken by an algorithm in every environment. It can be seen that in all test cases, the mean computation time of DeepSMP:RRT\* remained consistently around 2 seconds. However, the mean computation time of Informed-RRT\* and BIT\* increases significantly as the dimensionality of the planning problem increases slightly. Furthermore, the rightmost column presents the ratio of mean computational time of BIT\* to DeepSMP, and it is observed that on average, our method is at least 7 times faster than BIT\*, the current state-of-art motion planner.

From experiments presented so far, it is evident that BIT\* outperforms Informed-RRT\*, therefore, in the following experiments only DeepSMP and BIT\* are compared. Fig. 6 compares the mean computation time of DeepSMP: RRT\* and BIT\* in two test cases, i.e., $seen$-$X_{obs}$ and $unseen$-$X_{obs}$. It can be observed that the mean computation time of DeepSMP stays around 2 seconds irrespective of the given problem's dimensionality. Furthermore, the mean computational time of BIT\* not only fluctuates but also increases significantly as the dimensionality of the planning problem increases slightly.

Figure 5: DeepSMP computed optimal path for a rigid body in 1.12 seconds.

Finally, Fig. 7 shows DeepSMP planning motions for a Universal 6-DOF robot. In Fig. 7 (a), the robotic manipulator is at the start configuration whereas its target configuration is symbolized as a shadowed region. Fig. 7 (b) shows the traces of a path planned by DeepSMP for the given start and goal pair. In this problem, the mean computational times taken by DeepSMP and BIT\* are 1.7 and 48.8 seconds, respectively, which makes DeepSMP around 28 times faster than BIT\*.

$\frac{{BIT}:t_{mean}}{{DeepSMP}:t_{mean}}$

TABLE I: Time comparison (in seconds) of DeepSMP against Informed-RRT* and BIT* on two test datasets.

## Discussion

### VI-A Stochasticity through Dropout

Our stochastic feedforward DeepSampler uses Dropout in every layer except the last two layers during both offline and online execution. Dropout is applied layer-wise to a neural network, and it drops each unit in the hidden layer with a probability $p \in {\lbrack 0,1\rbrack}$. In our models, the dropped out units are indicated as dotted circles in Fig. 1. Thus, the resulting neural network is a sliced version of the original deep model, and in every iteration during online execution, a different model emerges through randomly dropping some hidden units. These perturbations in DeepSampler through Dropout enables DeepSMP to generate different samples in the region likely to contain path solutions.

Figure 6: Computational time comparison of DeepSMP:RRT* and BIT* on test datasets. The plots show DeepSMP is more consistent and faster than BIT* in all test cases.

### VI-B Bidirectional Sampling

Since our method incrementally generates samples, it can be easily extended to produce samples for bidirectional SMPs such as IB-RRT\*. To do so, treat both start and goal configuration as random variables $x_{rand1}$ and $x_{rand2}$, respectively, and swap their roles by the end of every iteration in Algorithm 1. This way, two trees in bidirectional SMPs can be made to march towards each other to rapidly compute end-to-end collision-free paths.

### VI-C Completeness

SMPs ensure probabilistic completeness. Let $V_{n}^{SMP}$ denotes the tree vertices of SMP after $n \in {\mathbb{N}}$ iterations. Since all SMPs begin to build a tree from initial robot state $x_{init}$ i.e., $V_{0}^{SMP} = x_{init}$, and randomly explore the entire configuration space by forming a connected tree as $n$ approaches to infinity, they guarantee probabilistic completeness i.e.,

DeepSMP also starts generating a connected tree from $x_{init}$ and after exploring a region that most likely contains a path solution for $n^{limit}$ iteration, it switches to uniform random sampling (see Algorithm 1). Therefore, if $n^{limit} \ll n$, DeepSMP also ensures probabilistic completeness i.e., as the number of iterations $n$ approach to infinity, the probability of DeepSMP finding a path solution, if one exists, approaches to one:

### VI-D Asymptotic Optimality

RRT\* and its variants are known to ensure asymptotic optimality i.e., as the number of iterations $n$ approaches to infinity/large-number, the probability of finding a minimum cost path solution reaches to one. This property comes from incrementally rewiring the RRT graph connections such that the shortest path is asymptotically guaranteed in RRT\*. It is proposed that if the underlying SMP of DeepSMP is RRT\* or any optimal variant of RRTs, DeepSMP is guaranteed to be asymptotic optimal. This follows from the fact that DeepSMP samples a selective region for fixed number of iterations and switches to uniform randoms sampling afterwards. Thus if the number of iterations goes infinity, through incremental rewiring of DeepSMP graph, the asymptotic optimality is also guaranteed.

Figure 7: DeepSMP with RRT* planning motions for a 6 DOF manipulator. Fig (a) indicates the robot at start configuration and the goal configuration is indicated as a shadowed region. Fig (b) shows the path traces followed by the robot. In this problem, the mean computational times of DeepSMP and BIT* are 1.7 and 48.8 seconds, respectively, which makes DeepSMP about 28 times faster than BIT*.

### VI-E Computational Complexity

A forward pass through a deep neural network is known to exhibit $O{}$ complexity. It can be seen in Algorithm 1 that adaptive samples are generated incrementally by forward passing through our stochastic DeepSampler. Hence, the proposed neural sampling method does not add any extra computational overhead to any underlying SMP for path generation. Thus, the computational complexity of DeepSMP method will essentially be the same as underlying SMP in Algorithm 1. For instance, as in our case, RRT\* is an underlying SMP method, therefore, in presented experiments, the computational complexity of DeepSMP is $O{({nlogn})}$, where $n$ is the number of nodes in the tree.

## Conclusions and Future work

In this paper, we present a deep neural network based sampling method called DeepSMP which generates samples for Sampling-based Motion Planning algorithms to compute optimal paths rapidly and efficiently. The proposed method 1) adaptively samples a selective region of a configuration space that most likely contains an optimal path solution, 2) combined with SMP methods consistently demonstrate mean execution time of about 2 second in all presented experiments, and 3) generalizes to new unseen environments.

In our future work, we plan to propose an incremental online learning method that begins with an SMP method, and trains DeepSMP simultaneously to gradually switch from uniform sampling to adaptive sampling. To speed up the incremental online learning process, we plan to propose a method that prioritizes experiences to learn from selectively fewer training examples.
