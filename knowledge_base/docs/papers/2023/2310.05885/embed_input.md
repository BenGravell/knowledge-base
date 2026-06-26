<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DTPP: Differentiable Joint Conditional Prediction and Cost Evaluation for Tree Policy Planning in Autonomous Driving

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motion prediction and cost evaluation are vital components in the decision-making system of autonomous vehicles. However, existing methods often ignore the importance of cost learning and treat them as separate modules. In this study, we employ a tree-structured policy planner and propose a differentiable joint training framework for both ego-conditioned prediction and cost models, resulting in a direct improvement of the final planning performance. For conditional prediction, we introduce a query-centric Transformer model that performs efficient ego-conditioned motion prediction. For planning cost, we propose a learnable context-aware cost function with latent interaction features, facilitating differentiable joint learning. We validate our proposed approach using the real-world nuPlan dataset and its associated planning test platform. Our framework not only matches state-of-the-art planning methods but outperforms other learning-based methods in planning quality, while operating more efficiently in terms of runtime. We show that joint training delivers significantly better performance than separate training of the two modules. Additionally, we find that tree-structured policy planning outperforms the conventional single-stage planning approach.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A fundamental requirement for autonomous vehicles is the ability to make decisions that are safe, informed, and human-like. Achieving this involves accurate prediction of the future behavior of traffic participants and planning that ensures safety, comfort, and adherence to traffic norms. Due to inherent uncertainties in the real world, the decision-making system should be capable of *policy planning* that accounts for different futures and options for the ego vehicle to react. To tackle this intractable continuous-space planning problem, tree-structured policy planners, such as Tree Policy Planning (TPP) and Monte-Carlo Tree Search (MCTS), employ a tree policy where the optimal action can be found by solving a discrete Markov Decision Process (MDP). Specifically, the TPP algorithm constructs two trees: a trajectory tree and a scenario tree. Each branch of the trajectory tree represents a candidate (multi-stage) trajectory for the ego agent, and each branch of the scenario tree contains the predicted outcomes of neighboring agents.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

However, tree-structured planners face two significant challenges. First, in contrast to most neural motion prediction models that only predict unconditional future trajectories of other agents (i.e., without considering bi-directional interactions), tree-structured planners require a prediction model capable of efficiently producing ego-conditioned predictions. The prediction model must be able to handle varying search depths (timesteps) within the planning process, maintain causal relationships, and efficiently process multiple branches. Second, evaluating the cost (or reward) of actions in alignment with human decision-making is challenging. Existing approaches often employ a simple linear cost function with a set of manually-crafted features and fixed weights. However, factors related to agent interactions are intricate to design and difficult to quantify manually. Accordingly, a learnable cost function becomes an attractive approach to reflect human driving preferences.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Our key contributions are threefold. First, we present the DTPP framework that integrates efficient ego-conditioned predictions with the learning of a situation-aware cost function (Fig. 1). Our framework can flexibly leverage both learned and handcrafted cost components, is end-to-end differentiable, and enables joint training with human driving data. Second, we present a novel query-centric, Transformer-based prediction model that enables efficient multi-stage motion predictions conditioned on multiple potential future ego trajectories. The key advantage of our prediction model is its use of the ego agent's future branch information (trajectory tree) as a query in its Transformer decoder, in contrast to the conventional approach of incorporating a single ego trajectory plan during context encoding. Finally, we demonstrate that this approach yields strong performance for both closed-loop planning and prediction across a wide array of challenging, interactive scenarios in the large-scale, real-world nuPlan dataset.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Methodology", "weight": 1.0} -->

1:Nl expansion stages, fp prediction model, fc cost model, fe node expansion function, s0 initial node. 2:Encode scene context using fp (encoder) 4: Expand the current node(s) si using function fe to obtain the trajectory tree si + 1 5: Query the prediction model fp (decoder) with the trajectory tree to obtain the scenario tree pi + 1 6: Query the cost model fc with the trajectory tree and scenario tree to obtain branch costs ci + 1 7: Prune nodes in si + 1 using ci + 1 9:Compute the optimal first-stage node s1* using dynamic programming Algorithm 1 Tree Policy Planning with Learned Prediction and Cost Models Figure 2: Overview of the DTPP framework with joint learnable prediction and cost evaluation models. The framework encompasses iterative node pruning and expansion, guided by ego-conditioned prediction outcomes and cost evaluations. During training, the loss of cost evaluation can be back-propagated to the prediction module, enabling differentiable and joint optimization of both modules. Figure 2: Overview of the DTPP framework with joint learnable prediction and cost evaluation models.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Methodology", "weight": 1.0} -->

The framework encompasses iterative node pruning and expansion, guided by ego-conditioned prediction outcomes and cost evaluations. During training, the loss of cost evaluation can be back-propagated to the prediction module, enabling differentiable and joint optimization of both modules.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Methodology", "weight": 1.0} -->

The proposed DTPP framework with its associated prediction and cost models are illustrated in Fig. 2 and Algorithm 1. Our planner is based on top of TPP, with the important additions of node pruning enabled by our learned cost model, and integration with our CMP model, which together significantly improve planning performance and efficiency.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Methodology", "weight": 1.0} -->

The key idea behind tree-structured planning is to approximate the intractable continuous-space policy planning problem by sampling a discrete set of ego trajectories in multiple stages, forming a *trajectory tree*, and predicting the motion of other agents conditioned on each ego trajectory segment, forming a *scenario tree*. The optimal ego action is then derived using dynamic programming. Specifically, trajectory tree nodes $s_{i}^{j}$ contain an ego trajectory spanning from $t_{0}^{j}$ to $t_{F}^{j}$, where $t_{0}^{j}$ and $t_{F}^{j}$ indicate the start and end times of the $j$-th stage ($j \geq 1$). Scenario tree nodes $p_{i}^{j}$ contain the state of the environment (predicted states of nearby agents), and we use the same labeling convention.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Methodology", "weight": 1.0} -->

To build the trees, we iteratively sample a set of target states for each $s_{i}^{j}$ and generate trajectories that connect $s_{i}^{j}$ to the respective target states. We then predict environment states $p_{i}^{j}$ with a CMP model. We compute costs with the evaluation model and prune low-scoring nodes. We continue to expand the trees until a specified time limit or depth is reached.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Methodology", "weight": 1.0} -->

Our framework has two key novel model components. First, the query-centric CMP model extracts an environment context with a Transformer encoder, and outputs joint trajectories of other agents (scenario tree) conditioned on possible ego plans with a Transformer decoder. Importantly, the ego trajectories enter the model as part of the decoder query vector, so during planning the encoder is only called once and the decoder is only called once per planning stage. Second, the cost evaluation module takes the trajectory tree and scenario tree as inputs to compute the costs of each branch (plan). To do this, it combines a neural feature extractor (from the joint trajectories of all agents) and a neural weight decoder (from the encoded ego context). The cost model is learned jointly in the context of the planner and prediction model, so it is optimized to capture the desired driving behavior and act as an effective pruning function in testing.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Planning Process", "weight": 1.0} -->

Our proposed planning algorithm is outlined in Algorithm 1. The tree policy planner repeatedly expands the selected nodes guided by the learned prediction and cost models until reaching the maximum expansion stage $N_{l}$. By introducing cost learning as an effective heuristic for expansion, we can ensure that we only expand promising nodes for efficiency. We then use dynamic programming to find the optimal initial stage node for execution. While our framework is extensible to any number of stages, we opt for $N_{l} = 2$ in experiments.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Planning Process", "weight": 1.0} -->

To construct the trajectory tree, we use a lane-centric target sampling process that incorporates mapping and routing information. First, we find multiple reference paths (e.g., lane centerlines) for the ego vehicle. Then, we sample varying target speeds and generate candidate trajectories across different paths based on the target speeds. Note that this is different from TPP, which directly samples target states, because this offers more stable planning performance in various scenarios with complex road networks. Given the current state of the ego vehicle at a node ${s{}} = {\lbrack x_{0},y_{0},v_{0},a_{0},\theta_{0},l_{0}\rbrack}$, representing its coordinates, velocity, acceleration, heading, and position on a reference path, we adopt a third-order polynomial to parameterize the trajectory's velocity $v{(t)}$ concerning the target speed $v_{\text{target}}$: We can directly compute the coefficients of $v{(t)}$ in closed form and determine the velocity of the trajectory.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Planning Process", "weight": 1.0} -->

Then, we can calculate the positions on the reference path ${l{(t)}} = {l_{0} + {\int_{0}^{t}{v{(t)}{dt}}}}$ and the coordinates $x{(t)}$, $y{(t)}$, $\theta{(t)}$ in Cartesian space. Finally, we drop trajectories that violate dynamic constraints. We set an upper limit on the number of nodes within the trajectory tree and randomly discard nodes if the limit is exceeded.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B Conditional Prediction Model", "weight": 1.0} -->

Transformer encoder. The inputs to the model are the past trajectories of $N_{a} = 10$ nearby agents and the ego vehicle, as well as $N_{m} = 50$ nearby map elements including lanes and crosswalks. Agent trajectories are $T_{h} = 20$ timesteps long with ${\Delta T} = {0.1s}$ resolution. Trajectories are encoded with LSTM networks (with shared weights); map elements are encoded with MLP networks. The encoding vectors are concatenated to form an environment context with shape $\lbrack{1 + N_{a} + N_{m}},D\rbrack$, $D = 256$. To capture inter-dependencies among scene elements, we process the environment context using a self-attention Transformer encoder consisting of $L_{e} = 3$ layers, and output dimension $\lbrack{1 + N_{a} + N_{m}},D\rbrack$. Importantly, this encoder is run only once during the planning process.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Conditional Prediction Model", "weight": 1.0} -->

Transformer decoder. The decoder is designed to efficiently extract information from both the environment context and ego trajectory tree, generating multi-stage predictions for the entire scenario tree in a single forward pass. Ego-conditioning is achieved through two aspects: the query to the attention modules containing the ego's future information, and the ego trajectory tree as information to the attention module. Initially, we encode the ego trajectory tree through an MLP, yielding the ego trajectory tree tensor. To handle the variable-sized trajectory tree, we organize the branches into a fixed-size tensor with a maximum branch size of $M = 30$ and a maximum time step of $T = {8s}$, padding invalid positions with zeros.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Conditional Prediction Model", "weight": 1.0} -->

Fig. 3 illustrates the decoder for a single agent. It consists of two cross-attention Transformer modules that gather information from the environment context and the ego plan, respectively. The query input for the cross-attention module is derived from three sources: an agent history embedding directly retrieved from the corresponding position in the environment encoding, a learnable time embedding (to differentiate between time steps), and the ego plan embedding (target points of the ego agent that correspond to distinct branches). Multi-axis attention is applied to address modal and temporal dimensions in the query. Notably, we employ a time mask to suppress attention from invalid time steps or modalities and a casual mask to maintain the causal relationships among modalities and timesteps. Finally, the outputs from the two attention modules are concatenated and processed through an MLP to decode the future trajectories of the agent. The decoding process is completed in a single shot because of the use of time embeddings. All agents share the same decoder. For different stages, the same decoder is employed to predict time-varying trajectories.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Conditional Prediction Model", "weight": 1.0} -->

Casual masked attention. Fig. 4 shows how we maintain causality in planning and conditional prediction using masked attention. For a given branch $m$, the causal mask excludes any information from other branches. Within each specific branch, predictions up to time step $t$ remain unaffected by any subsequent information beyond that time point. Notably, any invalid branches or time steps in the query or key/value tensors are masked during attention calculations. This masked attention mechanism can efficiently parallelize the predictions for all branches and timesteps in the scenario tree, while also preserving causality.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-C Cost Function", "weight": 1.0} -->

The cost of a candidate trajectory (branch) is the weighted sum of cost features $f^{j}$ over the time horizon: where $s{(t)}$ is the ego state at time $t$, and $p{(t)}$ is the ego-conditional predicted state of other agents, and $\omega_{j}$ are learned context-aware weights. The feature vectors ${f^{j},j} = {\lbrack e,i,c\rbrack}$ consist of ego features $f^{e}$, learned interaction features $f^{i}$, and collision features $f^{c}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-C Cost Function", "weight": 1.0} -->

The ego features $f^{e}$ consists of normalized ego jerk, acceleration, speed, and lateral acceleration. Through learned weights, ego features can balance comfort and progress.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-C Cost Function", "weight": 1.0} -->

The learned interaction features $f^{i}$ capture interaction between the ego and other agents. We employ an MLP to encode the relative attributes of the ego and other agents (relative position, heading, and velocity) into a higher-dimensional space, followed by max-pooling along the agent dimension. From this latent vector, we decode low-dimensional latent features using another MLP: The collision feature $f^{c}$ is computed with a handcrafted function that explicitly captures safety. Specifically, we apply a Gaussian radial basis function to the distances between the ego and other agents: The cost features are summed with learned context-aware weights $\omega_{j}$. Specifically, they are decoded with an MLP from the ego's encoding feature in the Transformer encoder model. The weights comprise 10 dimensions, encompassing ego, interaction, and collision features.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Cost Function", "weight": 1.0} -->

Note that one could add additional cost terms, e.g., for lane keeping and route following. We did not find this necessary as our planner is constrained to follow a target lane through its trajectory generator (see Section III-A).

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-D Model Training", "weight": 1.0} -->

For training the conditional prediction task, we select the situation that most closely matches the ground-truth ego trajectory and then apply the smooth L1 loss to the predicted trajectories of the surrounding agents. where $p^{*}$ is the prediction branch linked to the ego plan that is closest to the ground truth, and $p^{gt}$ represents the ground-truth trajectories of other agents.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-D Model Training", "weight": 1.0} -->

Notably, our approach captures the multi-modality of the prediction outcomes by learning agent responses to different ego plans. Regarding the cost function, we employ maximum entropy IRL, which sets the probability of a plan to be ${P{(s_{m})}} = \frac{e^{- {c{(s_{m})}}}}{\sum_{n}e^{- {c{(s_{n})}}}}$. Accordingly, we implement cross-entropy loss by comparing the softmax-normalized scores of each planned trajectory with the ground-truth label $y_{m}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-D Model Training", "weight": 1.0} -->

This approach enables the prediction-planning structure to be differentiable, directly linking agent predictions to overall planning performance. The total loss is then: where $\mathcal{L}_{p}^{j}$ and $\mathcal{L}_{c}^{j}$ are losses for planning stage $j$; $\alpha = 0.1$ is the weight assigned to the IRL loss; and $\beta^{j}$ is the weight associated with stage $j$. Given our priority on closed-loop planning, we assign a higher weight to the loss in the first stage, with $\beta^{1} = 1.0$ and $\beta^{2} = 0.2$. This setting enables the model to identify promising actions in the initial stage, which helps guide the tree expansion.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A Experimental setup", "weight": 1.0} -->

We experimentally verify our proposed method using the nuPlan dataset and its associated simulator. The training and testing phases involve a set of labeled scenario types from the nuPlan competition, but we excluded certain static scenario types, resulting in 10 dynamic scenario types. For training, we extract a total of 100k scenarios from the validation subset regarding the mentioned scenario types, and each scenario has a future time horizon of 8 seconds. For testing, we select 20 scenarios (each lasting 15 seconds) from the test subset for each scenario type, leading to a total of 200 scenarios.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A Experimental setup", "weight": 1.0} -->

Our evaluation covers both prediction and planning aspects. The planning test encompasses three tasks: open-loop (OL), closed-loop with non-reactive agents (CL-NR), and closed-loop with reactive agents (CL-R). We report the average *planning score* defined by the nuPlan simulator. The score captures safety, efficiency, and comfort for CL-NR and CL-R, and similarity to human driving for OL. We also evaluate prediction metrics, specifically, average and final displacement error (ADE and FDE) for non-ego agents conditioned on the selected ego trajectory plan.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

The entire planning horizon spans $T = 8$ seconds in $N_{l} = 2$ stages with maximum $M = 30$ branches. In the first stage (short-term, $t_{0}^{1} = {0s}$, $t_{F}^{1} = {3s}$), we consider three reference paths and allow for a maximum of 30 sampled target states. After obtaining the prediction results, we retain only the top 5 nodes and proceed to expand each node with 6 target states for the second stage (long-term, $t_{0}^{2} = {3s}$, $t_{F}^{2} = {8s}$).

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Implementation Details", "weight": 1.0} -->

The model is trained using an NVIDIA RTX 3080 GPU. The batch size is 16 and the total number of training epochs is 20. We use an AdamW optimizer, and the learning rate is initialized at 1e-4 and reduced 50% every 2 epochs after the 10th epoch. The model inference is conducted on the same GPU, while other computations run on an AMD 3900X CPU.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-C Main Results", "weight": 1.0} -->

Closed-loop planning. Table I presents the results of closed-loop planning tests. For a fair comparison, for the imitation learning-based baselines the output trajectories are projected onto the reference path. Our DTPP planner shows significantly better scores compared to learning-based policies, which often face causal confusion issues, as well as the rule-based IDM planner. Our method's performance closely matches that of the PDM(-Closed) method, which is the top-performing planning method on the leaderboard but is highly optimized for the nuPlan challenge metrics. Moreover, our method outperforms the baseline TPP method. For a detailed comparison with TPP, please refer to the following.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-C Main Results", "weight": 1.0} -->

The results of closed-loop planning tests and runtime analysis are shown in Table II. The baseline TPP method, without cost learning, shows subpar performance in closed-loop planning. Node pruning can make performance much worse when cost learning is not included. However, with cost learning, even when done separately, planning performance significantly improves and pruning can be effective without affecting the planning performance. This is because, in the first stage, we can already choose the promising nodes and safely remove the other nodes. Additionally, joint training of prediction and cost evaluation models outperforms separate training, which can lead to suboptimal planning performance. Our DTPP method, which adopts joint learning of prediction and cost evaluation model, yields the best results. Using node pruning does not affect planning performance, but can significantly reduce runtime (by nearly half).

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-C Main Results", "weight": 1.0} -->

Comparison of prediction models. We compare the performance of our prediction model against two other baseline models, while keeping other parts of the planning framework unchanged. No ego-conditioned model (non-EC): information regarding the future trajectories of the ego vehicle is not incorporated into the model. Early fusion model (EF-EC): the ego vehicle's future information is incorporated into the encoder part of the model and thus the model is queried iteratively for different plans. Note that the prediction metrics are derived from the branch selected by the cost evaluation model, and results from the non-EC method are directly employed for calculation. The results in Tables III and IV indicate that ego-conditioned prediction models lag slightly in terms of accuracy compared to the non-EC model. However, they could enhance planning performance for both open-loop and closed-loop testing. Further, our proposed query-centric approach outperforms the early fusion method.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-D Ablation Studies", "weight": 1.0} -->

Influence of cost function learning. We investigate the influence of cost function and report the results in Table VI. The prediction metric and closed-loop planning score are used to evaluate the trained models with different cost-learning settings. The results indicate that the learned latent interaction feature plays a pivotal role in our model, ensuring the superior performance of our method in planning. The inclusion of collision potential in training, as well as the use of context-aware cost weights, proves advantageous for enhancing the final closed-loop planning performance. A noteworthy finding is that better prediction performance may not translate to better closed-loop planning, highlighting the importance of co-designing and joint training.

<!-- chunk {"id": "body-0034", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

We propose DTPP, a differentiable joint learning framework for prediction and cost modeling, specifically designed for a tree policy planner. Our prediction model is a query-centric Transformer network with efficient ego conditioning. The cost model combines learned and handcrafted features with learned context-aware weights. The experimental results for planning and prediction on real-world driving data show that our prediction model yields significantly better performance and efficiency. Joint training is crucial for achieving optimal planning performance, and our tree-based planner significantly outperforms single-stage trajectory planning. Future work may extend our framework to multi-modal probabilistic predictions and perform real-world experiments.
