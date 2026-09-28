<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Motion Memory: Leveraging Past Experiences to Accelerate Future Motion Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

When facing a new motion-planning problem, most motion planners solve it from scratch, e.g., via sampling and exploration or starting optimization from a straight-line path. However, most motion planners have to experience a variety of planning problems throughout their lifetimes, which are yet to be leveraged for future planning. In this paper, we present a simple but efficient method called Motion Memory, which allows different motion planners to accelerate future planning using past experiences. Treating existing motion planners as either a closed or open box, we present a variety of ways that Motion Memory can contribute to reduce the planning time when facing a new planning problem. We provide extensive experiment results with three different motion planners on three classes of planning problems with over 30,000 problem instances and show that planning speed can be significantly reduced by up to 89% with the proposed Motion Memory technique and with increasing past planning experiences.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Motion planning refers to the computational process of determining a sequence of control inputs and actions to move a robot from a given start state to a desired goal location while avoiding obstacles and observing system and environment constraints. Motion planners are essential components for almost all robotic applications, such as autonomous navigation, and manipulation,. Therefore, quick, efficient, and optimal collision-free motion planning is of paramount value to the entire robotics community.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Decades of research into motion planning have made significant progress and are able to find motion-planning solutions for different robot platforms, e.g., using Probabilistic Roadmaps (PRM), Expansive Spaces algorithm, and Rapidly-Exploring Random Trees (RRT) to move mobile robots or manipulator arms. Nevertheless, these planners still face challenges in complex real-world settings when real-time planning is required to assure fast and reliable motion execution. Conventional motion planners need to plan from scratch every time they encounter a new environment. This situation remains true even when robots repeatedly face similar environments, where prior experiences could be beneficial. Such repetitive planning introduces unnecessary planning time and therefore limits the robot performance in real-world environments where fast planning time can benefit the downstream tasks, such as quickly moving through highly constrained obstacle spaces.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

On the other hand, advances in machine learning have demonstrated that robots are capable of learning emergent behaviors in a data-driven manner without depending on heavily engineered attributes and heuristics. One particular benefit of learning methods is the potential to continually improve with increasing real deployment experiences, a capability that the classical motion planners lack.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Fig. 1: Traditional motion planners require significant amount of effort to plan from scratch (left), such as large amount of samples or iterations (illustrated in green); Motion Memory utilizes past planning experiences to accelerate future planning when facing new planing problems (right).

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Considering the limitations of classical motion planners and the potential of learning from experiences, we present Motion Memory, a new paradigm based on past planning experiences to guide traditional motion-planning methods when facing new planning problems in order to reduce computational overhead and therefore improve planning efficiency, as robots gather more and more deployment experiences in the real world. Leveraging machine learning, Motion Memory includes an experience augmentation technique and a representation learning method that enable robots to reflect on prior planning experiences for efficient future planning as shown in Fig. 1. To be specific, the experience augmentation strategy automatically generates new planning problems, for which past motion plans are (or are not) the solutions, and thus provides Motion Memory with an extensive corpus of training data to generalize to future planning problems. Motion Memory also utilizes representation learning to enable autonomous robots to learn from augmented previous planning experiences so that motion planners can identify, store, memorize, and retrieve past planning experiences to facilitate motion planning in unseen future environments. We present different ways to integrate Motion Memory with three existing motion planners in three different categories of environments both in a closed and open box manner to showcase the wide applicability and generalizability of the technique.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Our experiments demonstrate that Motion Memory significantly reduces the motion-planning time in future unseen environments by up to 89% with increasing deployment experiences.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Classical Motion Planning", "weight": 1.0} -->

Among classical motion planners, sampling-based approaches have shown to be effective in solving challenging problems in complex, unstructured environments. To account for dynamics, sampling-based motion planners often expand a motion tree whose branches correspond to collision-free and dynamically-feasible trajectories. RRT and its variants rely on nearest neighbors to expand the motion tree toward random samples. EST relies on probability distributions to push the tree toward less-explored areas. KPIECE leverages a grid decomposition and interior-exterior cells. GUST introduces a discrete layer based on a roadmap abstraction and relies on discrete search to expand the motion tree along shortest paths in the roadmap. The work in further improves the motion-tree expansion to more aggressively follow the roadmap paths, while also increasing the clearance from the obstacles. When presented with a new planning problem, these approaches, however, have to plan from scratch as they do not learn from prior experiences. This is precisely what our Motion Memory framework addresses, enabling motion planners to leverage prior solutions to similar planning problems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-B Learning Assisted Motion Planning", "weight": 1.0} -->

Throughout the years, the learning and planning communities have investigated a variety of strategies for implementing the concept of machine learning for efficient motion planning. One intuitive approach is to apply machine learning to generate high-quality valid samples in critical regions more efficiently. Some methods produce valid samples in relevant areas by learning the representation of the configuration space, whereas other methods train models to bias sampling over the critical regions of predicted trajectories. Another practical strategy is to minimize the number of collisions by learning Gaussian mixture models, kernel perceptron, and graph neural network to replace the conventional collision checker or using a learned model to determine the order of testing the nodes to identify valid paths.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Learning Assisted Motion Planning", "weight": 1.0} -->

Instead of learning a specific planning operation, other learning-based pipelines learn from prior experience to solve motion planning problems in an end-to-end manner. One strategy is to use similarity function to determine the relevant information and retrieve it from a database in the form of paths or sampling distributions. Another approach is to train a deep neural network for efficient motion planning by using a database of past solved problems. These methods take as input point-cloud representations of a workspace and learn to encode this point-cloud into a latent space. Chamzas et al. and Lien et al. construct a similarity function only over the workspace to extract suitable local representations of planning problems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Learning Assisted Motion Planning", "weight": 1.0} -->

Informed by the aforementioned works, this paper proposes to hallucinate planning problems by experience augmentation, construct a memory of past planning experiences by classifying environments as similar or dissimilar using representation learning, and retrieve relevant planning experience to assist planners in future planning. Compared to all these specific techniques developed for a specific motion planner in an ad hoc manner, our Motion Memory is designed to be a universal technique that is applicable to any motion planner and allows them to improve planning efficiency with increasing planning experiences in a principled manner.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Motion Memory", "weight": 1.0} -->

The key inspiration behind Motion Memory is that most motion planners will encounter many different planning problems and produce different planning solutions throughout their lifetimes. Motion Memory aims to reflect on past planning experiences by generating a set of planning problems that will make the past planning solutions feasible/non-feasible. Then, utilizing representation learning, Motion Memory learns a latent space which contains efficient but also expressive information regarding the feasibility or optimality of the existing problem solutions with respect to any new planning problems in the future.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Motion Memory", "weight": 1.0} -->

Fig. 2: Motion Memory: Using Past Planning Experiences, Environment Generation, and Representation Learning to Accelerate Future Planning.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

We formulate our motion planning problem in the state space (S-space), which represents the universe of all possible robot states. For the scope of this paper, we use a 2D ground mobile robot as an example, but the general paradigm of Motion Memory has the potential to scale up to high-dimensional workspaces. A particular environment's S-space can be decomposed as $S=S_{\textrm{free}}\cup S_{\textrm{obst}}$, where $S_{\textrm{free}}\in\mathcal{S}_{\textrm{free}}$ is the set of reachable states and $S_{\textrm{obst}}\in\mathcal{S}_{\textrm{obst}}$ is the unreachable set due to obstacles, nonholonomic constraints, velocity bounds, etc. The robot state $s\in S$ is defined as in collision with obstacles when $s\in S_{\textrm{obst}}$ and collision free otherwise ($s\in S_{\textrm{free}}$).

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

We denote the robot action to be $u\in\mathcal{U}$, e.g., commanded linear and angular velocity $\left(v,\omega\right)$, and define a motion plan $P\in\mathcal{P}$ as a sequence of such actions and resulted states $P=\{u_{i},s_{i}~|~1\leq i\leq t\}$. $\mathcal{P}$ is the space of all motion plans. Notice that some motion planners may produce the resulted states only, i.e., $P=\{s_{i}~|~1\leq i\leq t\}$ and leave the action generation to a low-level controller.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

With the aforementioned notation, any motion planner can be defined as a function $f(\cdot)$ that can be used to produce motion plans, that result in the robot moving from the robot's start state $s_{\textrm{s}}$ to a specified goal state $s_{\textrm{g}}$ without intersecting $S_{\textrm{obst}}$, while observing robot motion constraints and optimizing a particular cost function (e.g. distance, clearance, energy, and combinations thereof).

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

A motion planner $f(\cdot)$ that has been used to solve different motion planning problems in the past will have available a dataset $\mathcal{D}=\{d_{i}\}_{i=1}^{N}=\{S_{i},P_{i}\}_{i=1}^{N}$, where $N$ is the amount of currently available S-space (planning problem) and motion plan (planning solution) pairs. Here, we assume that the start and goal states are a constant distance away from each other and remain the same throughout all planning problems, e.g., by aligning them through rotation and translation of the S-space, a realistic assumption in many real-world motion planning problems where dynamics is primarily considered in the local planner, which is guided by local goals a constant distance away from the robot computed by a global planner. For example, $s_{\textrm{s}}$ can be always expressed as the origin of the S-space, and $s_{\textrm{g}}$ as $$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

The goal of Motion Memory is to utilize the existing $\mathcal{D}$ from past planning experiences to accelerate future planning as shown in Fig. 2.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Augmenting Past Experiences with Hallucination", "weight": 1.0} -->

Although $\mathcal{D}$ may contain a variety of planning problem and solution pairs which have the potential to cover a new planning problem faced in the future, the chance of encountering exactly the same problem is still very low, considering the changing real world, sensory noise, and perceptual imperfectness. Therefore, Motion Memory bootstraps on the existing dataset $\mathcal{D}$ and augments it with hallucinated planning problems.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Augmenting Past Experiences with Hallucination", "weight": 1.0} -->

In contrast to the motion planning problem of finding the optimal motion plan $P$ given a S-space $S$ in Eqn., the hallucination problem is defined as its inverse problem, i.e., given a motion plan $P$, what are the S-spaces $S$ that assure this motion plan is optimal: Notice that $f^{\dagger}(\cdot)$ is not strictly the inverse function of $f(\cdot)$, because $f(\cdot)$ is non-injective, i.e., different S-spaces can map to the same optimal plan. Therefore, instead of one S-space $S$, we need to find the set of all S-spaces $\{S_{i}\}_{i=1}^{\infty}$, where the motion plan $P$ is optimal. In most cases, such a set is an infinity set, except for finitely discretized $S$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Augmenting Past Experiences with Hallucination", "weight": 1.0} -->

Compared to the forward motion planning problem, which needs to run in real time onboard computation-limited robot platforms, the inverse hallucination problem in Eqn. is much easier to solve. Researchers have proposed different ways to approximate the infinity set $\{S_{i}\}_{i=1}^{\infty}$ using representative obstacle states, e.g., the maximal, a minimal, or a learned distribution of obstacle set in the S-space. With these hallucination techniques, each member of the original pairwise motion planning problem-solution dataset can be augmented from $d_{i}=\{S_{i},P_{i}\}$ to $d_{i}^{*}=\{\{S_{i}^{j}\}_{j=1}^{M_{i}},P_{i}\}$, where $M_{i}$ is the number of total generated planning problems for solution $i$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Augmenting Past Experiences with Hallucination", "weight": 1.0} -->

Thus, the original dataset $\mathcal{D}$ is augmented to in which each past planning solution $P_{i}$ is no longer only paired with one original planning problem $S_{i}$, but a set of $M_{i}$ planning problems $\{S_{i}^{j}\}_{j=1}^{M_{i}}$, for which $P_{i}$ is optimal.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Augmenting Past Experiences with Hallucination", "weight": 1.0} -->

While $P_{1},P_{2},...,P_{N}$ indicate $N$ existing motion plans, $P_{0}$ corresponds to an empty set: It is also possible to produce a set of motion planning problems in which no existing motion planning solutions are feasible or optimal, e.g., by adding obstacles to intersect with at least one robot state in every existing motion plan, which will yield $d_{0}^{*}=\{\{S_{0}^{j}\}_{j=1}^{M_{0}},P_{0}\}$, which is also included in $\mathcal{D}^{*}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Representation Learning", "weight": 1.0} -->

The augmented dataset $\mathcal{D}^{*}$ contains more planning problems for each past planning solution, where the solution is feasible or optimal. Such an augmented dataset is used to learn an efficient latent representation space, which contains critical information regarding the feasibility or optimality of each existing motion plan solution with respect to any motion planning problem. Specifically, we adopt a triplet loss to enforce solution invariance in the learned latent space so that all environments where solution $P_{i}$ is feasible or optimal stay close to each other in the learned embedding space.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Representation Learning", "weight": 1.0} -->

We generate triplet training data of anchor, similar, and dissimilar planning problems $\langle S^{a},S^{s},S^{d}\rangle$ by sampling $S^{a}$ and $S^{s}$ from the same set of planning problems where solution $P_{i}$ is feasible or optimal, i.e., $\{S_{i}^{j}\}_{j=1}^{M_{i}}$, and sample $S^{d}$ from other problem sets and assure $P_{i}$ is not feasible or optimal for $S^{d}$. The planning problem (S-space) encoder $e_{\theta}(\cdot)$ is then trained to minimize a triplet loss, with $\theta$ as the learnable parameters.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Representation Learning", "weight": 1.0} -->

The representation space will contain data points from $N$ different latent clusters corresponding to the $N$ existing motion plans $\{P_{i}\}_{i=0}^{N}$, including a cluster for S-spaces where none of the $N$ plans are feasible or optimal. The cluster centroids are computed as

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-D Accelerating Future Planning", "weight": 1.0} -->

Using representation learning, the planning problem encoder is able to project any new motion planning problem $S_{N+1}$ into the latent space, i.e., $l_{N+1}=e_{\theta}(S_{N+1})$. The existing motion plan associated with the closest cluster centroid $P_{i^{*}}$ is likely the closest to the actual motion planning solution of the problem $S_{n+1}$: For existing motion planners, a motion plan $P_{i^{*}}$ potentially very close to the actual solution can be used to accelerate planning in different ways. For example, for sampling-based motion planners, the states in $P_{i^{*}}$ can be used to bias sampling. For optimization-based approaches, both the actions and states can be used as an initial guess, highlighting the potential of Motion Memory to serve as an effective seed, although this specific application is not demonstrated in our experiments.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D Accelerating Future Planning", "weight": 1.0} -->

For motion planners treated as a closed-box or an open-box, $P_{i^{*}}$ can be collision checked and be used as the final solution if no collisions are detected, or utilize the closed-box planner to only fix the plan segments which are in collision. In cases where $P_{0}$ is the closest in the representation space, the motion planner can start planning from scratch.

<!-- chunk {"id": "body-0030", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

Fig. 3: Different Planning Problem Classes: Curves (Left), Random (Middle), Trap (Right) Fig. 4: Different Motion Memory configurations improve three planners in three classes of motion planning problems.

<!-- chunk {"id": "body-0031", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

We present extensive experimental results by integrating our Motion Memory technique with three different motion planners in both a closed-box and an open-box manner to solve three different classes of motion-planning problems. We present detailed results on the three planners' performances with or without Motion Memory for each problem class and for all three classes combined into one. Furthermore, we present evidence demonstrating Motion Memory allows motion planners' planning efficiency to improve with increasing past planning experiences. Finally, we conduct an ablation study to show that the improved planning efficiency is not only due to more past planning experiences, rather the Motion Memory technique itself is an indispensable part.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Experimental Setup", "weight": 1.0} -->

Considering Motion Memory is designed to be a universal paradigm that is agnostic to any underlying planner, we integrate Motion Memory with three different motion planners, in both a closed-box and an open-box manner to show its general applicability (denoted as "C" and "O" in all experiment results). In the closed-box integration, we do not assume any access to or knowledge about the underlying planner, and only interface Motion Memory with it using the Motion Memory output as a potential solution after taking a new planning problem as input. The open-box integration assumes access to and knowledge about the underlying planner and depends on which components can be benefited from the Motion Memory output, e.g., sampling distribution or initial optimization guess. We describe the three underlying planners with their closed-box and open-box Motion Memory integration as follows.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A1 Baseline Planners", "weight": 1.0} -->

We experiment with different sampling-based motion planners. We first use RRT, one of the most popular methods. RRT uses random sampling and nearest neighbors to guide the motion-tree expansion. We also use GUST, which was specifically designed for motion-planning problems for vehicles with dynamics. GUST introduces a discrete layer obtained by building a roadmap to guide the motion-tree expansion. The roadmap is then used to induce a partition of the motion-tree into groups based on their nearest roadmap node. During the motion-tree expansion, priority is given to those groups associated with short paths to the goal. Our third planner, which we refer to as Follow, further improves GUST by more aggressively following the roadmap paths, and dynamically adjusting the weights based on the progress made during the motion-tree expansion.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Closed-box Versions of the Motion Planners", "weight": 1.0} -->

We first use these planners as black boxes in conjunction with the motion-memory framework. Specifically, let $\zeta_{1},\ldots,\zeta_{k}$ be the top $k$-predictions obtained by the motion-memory framework for a new motion-planning problem. Each of these predictions corresponds to a dynamically-feasible trajectory (retrieved from the database). The black-box version, referred to as $\text{MP}_{\text{ClosedBox}}$, first checks these trajectories $\zeta_{1},\ldots,\zeta_{k}$ in order for collisions. If some $\zeta_{i}$ is not in collision, then $\text{MP}_{\text{ClosedBox}}$ returns $\zeta_{i}$ as the solution. Otherwise, $\text{MP}_{\text{ClosedBox}}$ runs MP and returns the solution (if any) found by MP.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Open-box Versions of the Motion Planners", "weight": 1.0} -->

We can better leverage the predictions made by the motion-memory framework by looking inside the motion planners to better leverage the predictions. We refer to these versions as $\text{MP}_{\text{OpenBox}}$. $\text{MP}_{\text{OpenBox}}$, as the closed-box version, starts by checking if any of the predicted trajectories $\zeta_{1},\ldots,\zeta_{k}$ is not in collision. If all of them are in collision, then $\text{MP}_{\text{OpenBox}}$ runs a modified version of MP, as described below. $\text{RRT}_{\text{OpenBox}}$ is obtained by changing the sampling distribution from which the target is drawn. In the original RRT, the target is sampled with probability $b_{\text{goal}}$ (a predetermined probability, usually $b_{\text{goal}}=0.1$) from an area near the goal, and with probability $1-b_{\text{goal}}$ from the entire state space.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Open-box Versions of the Motion Planners", "weight": 1.0} -->

To generate a target along $\zeta_{i}$, we first select an intermediate state in $\zeta_{i}$ and then sample around it. In this way, $\text{RRT}_{\text{OpenBox}}$ biases the exploration toward the predicted trajectories $\zeta_{1},\ldots,\zeta_{k}$. $\text{GUST}_{\text{OpenBox}}$ differs from GUST only in the roadmap construction. Specifically, while GUST generates a roadmap node by sampling from the entire space, $\text{GUST}_{\text{OpenBox}}$ biases the sampling along $\zeta_{1},\ldots,\zeta_{k}$. Specifically, to generate a roadmap node, $\text{GUST}_{\text{OpenBox}}$ selects $\zeta_{i}$ with probability $b_{i}$, selects a state $s$ uniformly at random from $\zeta_{i}$, and generates a roadmap node by sampling near $s$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Open-box Versions of the Motion Planners", "weight": 1.0} -->

This results in a roadmap that captures the connectivity along the predicted trajectories $\zeta_{1},\ldots,\zeta_{k}$. Note that the roadmap is collision free, even if parts of $\zeta_{1},\ldots,\zeta_{k}$ are in collision (since samples that result in collision are discarded during the roadmap construction). This biased roadmap construction allows for a more efficient expansion of the motion tree along the predicted trajectories. $\text{Follow}_{\text{OpenBox}}$ differs from Follow only in the roadmap construction. In fact, $\text{Follow}_{\text{OpenBox}}$ uses the same procedure as $\text{GUST}_{\text{OpenBox}}$ for constructing the roadmap. $\text{Follow}_{\text{OpenBox}}$ then seeks to closely follow the shortest roadmap path from the start to the goal by aggressively expanding the motion tree to follow the nodes in the shortest path in succession.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A2 Planning Problem Classes", "weight": 1.0} -->

Fig. 3 shows the three different classes of planning problems used in our experiments, referred to as "Curves," "Random," and "Trap." These problem classes are parametrized, and the obstacles are procedurally generated. Placement (location and orientation) and size of the obstacles are drawn from a probability distribution so that numerous instances can be generated for each problem class. An instance corresponds to a specific placement of the obstacles, as shown in Fig. 3. For example, for the "Curves" problem class we can vary the number of curves, number of segments per curve, separation among segments, and so. For the "Random" problem class, we can vary the density of the obstacles as well as their shape and placement. For the "Trap" problem class we can perturb the placement of the major obstacles and also of the random obstacles spread throughout the environment.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A3 Motion Memory Implementation", "weight": 1.0} -->

For each of the three motion planning problem classes, we assume our Motion Memory has access to 100 planning problems and their corresponding motion planning solutions as its past planning experiences, i.e., $\mathcal{D}=\{d_{i}\}_{i=1}^{100}=\{S_{i},P_{i}\}_{i=1}^{100}$. We augment each data point in $\mathcal{D}$ with 999 more planning problems and generate an augmented dataset $\mathcal{D}^{*}=\{d_{i}^{*}\}_{i=1}^{100}=\{\{S_{i}^{j}\}_{j=1}^{1000},P_{i}\}_{i=1}^{100}$, a dataset of 100,000 problems per class with 100 solutions, by slightly rearranging obstacles close to the motion plan and randomly shuffling obstacles in other places.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A3 Motion Memory Implementation", "weight": 1.0} -->

For simplicity, we omit the set of problems where no existing motion plan is a solution, i.e., $d_{0}^{*}$. To train the planning problem encoder $e_{\theta}(\cdot)$, we use a Convolutional Neural Network which takes motion planning problems as input and outputs a 30-dimensional latent space. Specifically, the input to our CNN is a discretized version of the workspace, represented as a 2D grid where each cell encodes the presence or absence of an obstacle, and the network architecture comprises sequential layers of convolution and pooling, and the final feature map is processed through fully connected layers to produce the 30-dimensional embedding. For testing, we generate another 10,000 unseen planning problems per class for the motion planners to solve.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A3 Motion Memory Implementation", "weight": 1.0} -->

We present experiments comparing closed-box and open-box integrations with both top-one and top-five predictions for new problems. While top-five predictions provide more information, they also incur additional computational costs due to the need to process multiple predicted solutions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Improvement for Different Planners and Problems", "weight": 1.0} -->

In Fig. 4, we show individual planning performance of the three underlying planners (GUST, Follow, and RRT in row 1, 2, and 3 respectively) in the three classes of motion planning problems (Curves, Random, and Trap in column 1, 2, and 3 respectively). The fourth column is the results of a large Motion Memory which does not distinguish among different motion planning problem classes, with 300,000 training and 30,000 testing data points. In each figure, we show the average planning time of default baseline planner without Motion Memory (Planner_Baseline), the baseline planner assisted by Motion Memory in a closed-box manner with top-one or top-five prediction(s) (MM_Planner_C_1 and MM_Planner_C_5), and also assisted in an open-box manner (MM_Planner_O_1 and MM_Planner_O_5).

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Improvement for Different Planners and Problems", "weight": 1.0} -->

The results show that Motion Memory can significantly reduce planning time compared to all three default baseline planners, with the only exception of using Motion Memory in a closed-box manner with Follow in the Trap environment. In each of the 12 sub-figures in Fig. 4, we can observe increasing performance from left to right. Using Motion Memory in a open-box manner achieves similar or more improvement compared to using it in a closed-box manner. In most cases, using the top-five Motion Memory predictions outperforms using the top-one prediction, despite the potentially more computation to process four extra predictions. Comparing the first three columns, Motion Memory can achieve the most significant improvement for Curves environments with GUST and Follow, while RRT enjoys the most Motion Memory benefits in the Trap environments. In the last column where Motion Memory does not distinguish among the three classes of planning problems, it also outperforms all three baseline planners. Comparing the three rows, Motion Memory is the most helpful for GUST, while the difference made by Motion Memory to RRT is relatively smaller.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Continual Improvement with Increasing Experience", "weight": 1.0} -->

Fig. 5: Improvement with Increasing Experiences.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Continual Improvement with Increasing Experience", "weight": 1.0} -->

Fig. 6: Ablation Study: Random Path Selection.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-C Continual Improvement with Increasing Experience", "weight": 1.0} -->

We also study the performance improvement of Motion Memory with respect to increasing past planning experiences. In Fig. 6, we show how the runtime of the $\text{GUST}_{\text{ClosedBox}}$ planner to solve planning problems in Curves environments changes when having access to more available motion plans. For each bar in Fig. 6, we go through the entire Motion Memory pipeline, including environment generation and representation learning, with a limited number of available motion plans (20, 40, 60, 80, or 100). By integrating the Motion Memory model produced by the corresponding amount of past experiences with $\text{GUST}_{\text{ClosedBox}}$, we test the planner performance on the 10,000 unseen test problems. With only 20 or 40 available past motion plans, Motion Memory underperforms the baseline GUST, because a limited set of available motion plans is not able to sufficiently cover the variety of new planning problems. With increasing experiences, we see a significant reduction in runtime and improvement in planning efficiency. Such experiment results confirm our hypothesis that a motion planner can continually improve when having access to increasing amount of past planning experiences with the assistance of Motion Memory.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-D Ablation Study", "weight": 1.0} -->

Finally, to demonstrate the necessity of the Motion Memory technique, in addition to the access to a large amount of past planning experiences, we conduct an ablation study, in which we do not use the environment generation and representation learning in Motion Memory to decide which past plan may be most helpful for a future planning problem, but randomly pick a past plan to assist the motion planner. Fig. 6 shows that randomly picking one or five past plans to assist GUST in Curves environments in a open-box manner will increase the planning time. Such results indicate it is necessary to use Motion Memory to decide which past planning experience is useful to accelerate future planning.

<!-- chunk {"id": "body-0048", "role": "body", "section": "DISCUSSION", "weight": 1.5} -->

We present Motion Memory, a universal technique which is agnostic to different underlying motion planners but helps them to accelerate their future planning runtime with past planning experiences. By augmenting past experiences and using representation learning, Motion Memory avoids unnecessary and repetitive replanning from scratch when facing similar future planning problems. We demonstrate the efficacy of Motion Memory by integrating it with different planners in a closed-box and open-box fashion, and solving different classes of motion-planning problems more efficiently. One possible direction for future research is to extend Motion Memory for manipulation planning, where the robot interacts with the objects in the environment. Another direction is to consider a heterogeneous team of robots and how Motion Memory can facilitate planning for different types of robot, possibly adpating plans from one robot type to another.
