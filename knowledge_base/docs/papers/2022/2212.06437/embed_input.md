<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DiffStack: A Differentiable and Modular Control Stack for Autonomous Vehicles

Topics include Differentiable planning, Autonomous driving, Prediction, Motion planning, End-to-end learning, Modular.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents DiffStack, a fully differentiable and modular autonomous driving stack that combines prediction, planning, and control. By making the entire stack differentiable, it enables end-to-end gradient-based optimization across components, improving performance over non-differentiable modular baselines.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous vehicle (AV) stacks are typically built in a modular fashion, with explicit components performing detection, tracking, prediction, planning, control, etc. While modularity improves reusability, interpretability, and generalizability, it also suffers from compounding errors, information bottlenecks, and integration challenges. To overcome these challenges, a prominent approach is to convert the AV stack into an end-to-end neural network and train it with data. While such approaches have achieved impressive results, they typically lack interpretability and reusability, and they eschew principled analytical components, such as planning and control, in favor of deep neural networks. To enable the joint optimization of AV stacks while retaining modularity, we present DiffStack, a differentiable and modular stack for prediction, planning, and control. Crucially, our model-based planning and control algorithms leverage recent advancements in differentiable optimization to produce gradients, enabling optimization of upstream components, such as prediction, via backpropagation through planning and control.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our results on the nuScenes dataset indicate that end-to-end training with DiffStack yields substantial improvements in open-loop and closed-loop planning metrics , e.g., learning to make fewer prediction errors that would affect planning. Beyond these immediate benefits, DiffStack opens up new opportunities for fully data-driven yet modular and interpretable AV architectures.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Intelligent robotic systems, such as autonomous vehicles (AVs), are typically architected in a modular fashion and comprised of modules performing detection, tracking, prediction, planning, and control, among others. Modular architectures are generally desirable because of their verifiability, interpretability and generalization performance; however, they also suffer from compounding errors, information bottlenecks, and integration challenges.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A promising line of work tackling these issues focuses on making AV stacks more integrated (by relaxing inter-module interfaces) and data-driven (by optimizing modules jointly with respect to their downstream task). For example, in the context of AV perception, recent work has achieved substantial performance gains by jointly training tracking models with detection and prediction models. To extend such a joint, data-driven approach to decision making, existing approaches replace hand-engineered components, e.g., planning and control algorithms, with deep neural networks. As neural networks are differentiable, they can be optimized end-to-end for a final control objective; however, they offer weaker generalization, little to no interpretability or safety guarantees.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce DiffStack, a differentiable AV stack with modules for prediction, planning, and control that combines the benefits of modular and data-driven architectures (Fig. 1). The prediction module in DiffStack is a learned neural network that predicts the future motion of agents; the planning and control modules are principled, hand-engineered algorithms that produce AV actions given the current world state and motion predictions. Importantly, our hand-engineered planning and control algorithms are *differentiable*, enabling the training of the upstream prediction module for a downstream control objective by backpropagating gradients *through* the algorithms. In doing so, DiffStack can jointly optimize the entire stack for the final control objective, as in end-to-end neural networks, however it also maintains the interpretability and formal guarantees of standard modular AV architectures.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To make the planner and controller differentiable, we build upon the growing body of work on differentiable algorithm networks. In particular, we leverage the differentiable Model Predictive Control (MPC) algorithm for our controller. While differentiable algorithms show great promise, most prior works consider relatively simple control problems, e.g., pendulum and cartpole. To the best of our knowledge, this is the first work to demonstrate that, through careful design choices and integration, differentiable algorithms can be composed into stacks and trained with real-world data for AV prediction, planning, and control.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate DiffStack in both open-loop and closed-loop simulation settings using the large-scale, real-world nuScenes dataset. Our results show some immediate benefits of differentiable stacks: by training a prediction model with respect to the final control objective, DiffStack increases the effectiveness of predictions for decision making by up to $15\text{\%}$ over a large number of diverse scenarios. DiffStack achieves this, e.g., learning to make fewer prediction errors that would negatively affect planning. Further, DiffStack outperforms alternative handcrafted planning-aware prediction losses; compensates for artificially introduced integration errors; and tunes an interpretable cost function to make resulting plans more similar to human driving. Beyond these immediate benefits, our work demonstrates the feasibility and potential of differentiable AV decision making stacks, making an important step towards a new class of data-driven yet modular AV architectures.

<!-- chunk {"id": "body-0010", "role": "body", "section": "DiffStack: A Differentiable and Modular Autonomous Vehicle Stack", "weight": 1.0} -->

DiffStack is an autonomous driving stack with modules for prediction, planning, and control (Fig. 2). At a high level, DiffStack produces a trajectory for the AV to follow given a goal state, the tracked states of other agents, and a lane graph. To do so, it predicts where non-AV agents could move in the future; uses the predictions to select a safe, low-cost, and dynamically-feasible motion plan from a set of candidates; and finally optimizes the plan to yield a continuous and smooth ego-trajectory.

<!-- chunk {"id": "body-0011", "role": "body", "section": "DiffStack: A Differentiable and Modular Autonomous Vehicle Stack", "weight": 1.0} -->

The key feature of DiffStack is that it is *differentiable*, i.e., we can compute $\partial{\mathcal{L}_{j}/{\partial\theta_{i}}}$, the gradient of the training objective $\mathcal{L}_{j}$ of downstream module $j$ with respect to the parameters $\theta_{i}$ of upstream module $i$. Differentiability enables training all parameters jointly for the overall objective of the stack with a gradient-based optimizer. We can also interpret DiffStack as a neural network with interpretable internal representations and fixed computational blocks for planning and control. Section 3.1 will describe how these components are made differentiable.

<!-- chunk {"id": "body-0012", "role": "body", "section": "DiffStack: A Differentiable and Modular Autonomous Vehicle Stack", "weight": 1.0} -->

The main use case considered in this paper is to train the prediction module with respect to a final control objective. Different agents' predictions have different importance to the ego-vehicle (see examples in Appendix B). Standard metrics used to train prediction models are agnostic to the consequences of downstream planning, treating harmless and dangerous errors equally. By training directly for the end-objective of ego control, we expect DiffStack's prediction module to not only be accurate, but also synergize with planning and yield better overall ego controls.

<!-- chunk {"id": "body-0013", "role": "body", "section": "DiffStack: A Differentiable and Modular Autonomous Vehicle Stack", "weight": 1.0} -->

We consider two open-loop training settings. In reinforcement learning (RL) experiments we optimize a hindsight cost that measures the quality of an ego trajectory in *hindsight*, i.e., after observing the future trajectory of other agents in the scene. The hindsight cost can be viewed as a negative reward for RL. In imitation learning (IL) experiments we compare the planned ego trajectory to the ego-vehicle's enacted motion in the data through a mean-squared-error (MSE) loss. We additionally explore using DiffStack to tune the hand-specified planning and control cost functions. In this section, we describe each module in DiffStack and their respective training setups, with more details in Appendix C.

<!-- chunk {"id": "body-0014", "role": "body", "section": "DiffStack: A Differentiable and Modular Autonomous Vehicle Stack", "weight": 1.0} -->

Nomenclature. *Ego* refers to the AV and *agent* is a non-AV vehicle or pedestrian. States, $s$, consist of 2D position, heading, and longitudinal velocity. Control variables, $u$, are heading rate and longitudinal acceleration. A trajectory is a sequence of states, or states and controls, depending on the context. Distance between states is measured by the 2D Euclidean distance, whereas root-mean-squared state distance over time is used for trajectories. We denote trainable parameters of the prediction module by $\theta$, and trainable parameters of the planning and control cost by $w$. We perform two types of optimization: *training* (also called *learning*) optimizes $\theta$ and $w$ to minimize a loss $\mathcal{L}$ over some data; *planning* and *control* optimizes the ego trajectory to minimize a cost function with $\theta$ and $w$ fixed.

<!-- chunk {"id": "body-0015", "role": "body", "section": "DiffStack modules", "weight": 1.0} -->

Prediction. We employ Trajectron++, a state-of-the art CVAE that takes $H$ seconds of state history for all agents as input, and outputs multimodal trajectory predictions for one agent $a \in A$,

<!-- chunk {"id": "body-0016", "role": "body", "section": "DiffStack modules", "weight": 1.0} -->

where $k \in K$ is the mode of the output distribution. We will use ${\hat{s}}_{a} = {{\hat{s}}_{a}^{({1:T})}{(\theta)}}$ for brevity. The encoder of the CVAE processes agent state histories with recurrent LSTM networks and models inter-agent interactions using graph-based attention. The decoder is a GRU that outputs a Gaussian Mixture Model (GMM) for each future timestep. The GMM modes correspond to the CVAE's $K = 25$ discrete latent states. To ensure predictions are dynamically-feasible, GMMs are defined over controls and then integrated through a known (differentiable) dynamics function to produce a trajectory. We use the default model configuration without map and ego conditioning. We augment the input states with an ego-indicator variable to allow for ego-agent relation reasoning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "DiffStack modules", "weight": 1.0} -->

The raw prediction training objective is the InfoVAE loss, $\mathcal{L}_{pred} = {\mathcal{L}_{InfoVAE}\left( {\hat{s}}_{a},s_{a}^{\text{gt}} \right)}$, the same as for the original Trajectron++.

<!-- chunk {"id": "body-0018", "role": "body", "section": "DiffStack modules", "weight": 1.0} -->

Planning. The planner is a sampling-based algorithm that generates a set of $N$ dynamically-feasible ego trajectory candidates, $\mathcal{P} = {\{ s_{n},u_{n}\}}_{n \in N}$, and selects the candidate with the lowest cost. Namely,

<!-- chunk {"id": "body-0019", "role": "body", "section": "DiffStack modules", "weight": 1.0} -->

where $C$ is the cost function, ${\hat{s}}_{a \in A}$ are multimodal predictions for all agents from the prediction module, $g$ is a given goal, and $m$ is a lane graph. To generate trajectory candidates we sample a set of lane-centric terminal states, fit a cubic spline from the current state to the terminal state, and reject dynamically-infeasible trajectories. The cost function is a weighted sum of handcrafted terms,

<!-- chunk {"id": "body-0020", "role": "body", "section": "DiffStack modules", "weight": 1.0} -->

penalizing collisions, distance to the goal, lateral lane deviation, lane heading deviation, and control effort, respectively. Most notably, the collision term incorporates predictions into planning, ${C_{coll}{(s,{\hat{s}}_{a \in A})}} = {\sum_{a \in A}{\sum_{{t \in 1}:T}{\varphi\left( {\sum_{k \in K}{\pi_{k}{\|{s^{(t)} - {\hat{s}}_{a,k}^{(t)}}\|}^{2}}} \right)}}}$, where ${\hat{s}}_{a,k}$ is the $k$-th mode of the predicted trajectory distribution for agent $a$, $\pi_{k}$ is the probability of the $k$-th mode, $\varphi$ is a Gaussian radial basis function, and $|| \cdot ||$ is the Euclidean norm.

<!-- chunk {"id": "body-0021", "role": "body", "section": "DiffStack modules", "weight": 1.0} -->

Without loss of generality, in experiments we only do prediction for the vehicle closest to ego, and use GT futures for other agents. The remaining terms of are defined in Appendix C.

<!-- chunk {"id": "body-0022", "role": "body", "section": "DiffStack modules", "weight": 1.0} -->

Control. The control module performs MPC over a finite horizon using an iterative box-constrained linear quadratic regulator (LQR) algorithm. Formally, we aim to solve

<!-- chunk {"id": "body-0023", "role": "body", "section": "DiffStack modules", "weight": 1.0} -->

where $C$ denotes the cost function, $f_{d}$ the dynamics, $s^{init}$ the current ego state, and $\underset{¯}{u},\overline{u}$ the control limits. We use the cost defined in for $C$ and the dynamically-extended unicycle for $f_{d}$. We initialize the trajectory with $u_{plan}$ from the planner. The algorithm then iteratively forms and solves a quadratic LQR approximation of around the current solution $s^{(i)},u^{(i)}$ for iteration $i$, using first- and second-order Taylor approximations of $f_{d}$ and $C$, respectively. The trajectory is updated to be close to the LQR optimal control while also decreasing the original non-quadratic cost. We stop iterations upon convergence or a fixed limit.

<!-- chunk {"id": "body-0024", "role": "body", "section": "DiffStack modules", "weight": 1.0} -->

To make the control algorithm differentiable we leverage Amos et al.. The iLQR optimal trajectory, $s_{ctr}$, can be differentiated wrt. $C$ and $f_{d}$ by implicitly differentiating the underlying KKT conditions of the last LQR approximation. The gradients can be analytically computed by one additional backward pass of a modified iterative LQR solver. If iLQR fails to converge, we do not backpropagate gradients. In our setting $f_{d}$ is fixed. We compute gradients wrt. cost parameters, $\frac{\delta\mathcal{L}_{ctr}}{\deltaw} = {\frac{\delta\mathcal{L}_{ctr}}{\deltas_{ctr}}\frac{\deltas_{ctr}}{\deltaC}\frac{\deltaC}{\deltaw}}$, and further wrt.

<!-- chunk {"id": "body-0025", "role": "body", "section": "End-to-end training", "weight": 1.0} -->

An important question for data-driven AV stacks is the training objective and data. Learning in the real world is prohibitively expensive, and building a simulator with realistic traffic agent behavior is an open challenge. Accordingly, standard practice is to perform open-loop training with human driving data. We consider two common types of open-loop training settings: reinforcement learning (RL) and imitation learning (IL).

<!-- chunk {"id": "body-0026", "role": "body", "section": "End-to-end training", "weight": 1.0} -->

In the RL setting, we aim to minimize the (hindsight) cost of output ego trajectories, $s_{ctr},u_{ctr}$, over training examples in the dataset, $\mathcal{L}_{ctr} = \mathcal{L}_{HC} = {C_{H}\left( s_{ctr},u_{ctr};s_{a \in A}^{\text{gt}},g,m;w \right)}$. The hindsight cost $C_{H}$ captures the quality of a trajectory in *hindsight*, i.e., after knowing the future trajectory of non-ego agents $s_{a \in A}^{\text{gt}}$, similar to the concept of rewards in RL. We choose $C_{H}$ identical to the control cost $C$ defined, but with GT future trajectory inputs instead of predictions, and fixed $w$ parameters.

<!-- chunk {"id": "body-0027", "role": "body", "section": "End-to-end training", "weight": 1.0} -->

Note that our open-loop training setup does not account for the effect of ego actions on other agents; nevertheless, we treat recorded trajectories as GT futures, as in the prediction literature. In this setting we only train the prediction model. Given GT futures $\frac{\delta\mathcal{L}_{HC}}{\delta\theta} = {\frac{\delta\mathcal{L}_{HC}}{\delta{\{ s_{ctr},u_{ctr}\}}}\frac{\delta{\{ s_{ctr},u_{ctr}\}}}{\delta\theta}}$ where both terms exists given our differentiable controller. For the planner's target we choose the trajectory candidate with the lowest hindsight cost, $s^{\ast} = {{{\arg\min}_{{s_{n},u_{n}} \in \mathcal{P}}C_{H}}{(s_{n},u_{n}; \cdot )}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "End-to-end training", "weight": 1.0} -->

The total loss for training DiffStack is a linear combination of module-wise objectives, $\mathcal{L} = {{\alpha_{1}\mathcal{L}_{pred}} + {\alpha_{2}\mathcal{L}_{plan}} + {\alpha_{3}\mathcal{L}_{ctr}}}$. We experiment with different $\alpha_{i}$ values, including setting each $\alpha_{i}$ to zero. In the following we omit $\alpha_{i}$ for brevity.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our experiments investigate the following questions: 1) can DiffStack learn predictions that lead to better plans? 2) how does DiffStack compare to alternative planning-aware training techniques? 3) can DiffStack correct systematic integration errors? 4) can DiffStack learn the control cost from imitation? 5) do our open-loop results translate to closed-loop evaluation?

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

We begin with open-loop experiments (1--4), and then present closed-loop results in Section 4.3.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Dataset. We use the nuScenes dataset, comprised of state annotations for vehicles and pedestrians in 1000 scenes across Boston and Singapore. For training and open-loop evaluation we sample suitable planning scenarios from the dataset with $H = 4$s history and $T = 3$s future data. For each scenario, we choose one vehicle to act as the ego. Details including dataset splits are in Appendix D.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Metrics. We evaluate DiffStack's prediction module via standard prediction metrics: average displacement error (ADE) for the most-likely prediction and negative log-likelihood (NLL) for its full distributional output. To evaluate planning and control, we use the cross-entropy planning loss $\mathcal{L}_{plan} = \mathcal{L}_{CE}$, and control loss $\mathcal{L}_{ctr}$. We report the hindsight cost for reinforcement learning ($\mathcal{L}_{ctr} = \mathcal{L}_{HC}$) and MSE for imitation learning experiments ($\mathcal{L}_{ctr} = \mathcal{L}_{MSE}$). Since control is an AV stack's end-goal, $\mathcal{L}_{ctr}$ reflects the overall performance of the stack. To make these metric values more interpretable, we report them relative to a No prediction baseline and a GT prediction-based oracle. The baseline ego plans without predictions (ignoring the predicted agent), providing a performance lower bound.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

The GT oracle plans with GT futures in place of predictions, providing a notion of a performance upper bound. All results are averaged over our validation set, and we report standard errors of the mean over 5 training seeds.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Baselines. We compare DiffStack with standard AV stacks. For a fair comparison, we use the same set of modules as in DiffStack, but without making the planner and controller differentiable. We only train the prediction model, using increasingly planning-aware training objectives. Standard trains the prediction model with only the prediction loss $\mathcal{L}_{pred}$, unaware of downstream planning. Next, we re-weight prediction losses (in each batch) based on a handcrafted measure of relevance for planning. Distance weighted weights losses with the inverse distance between the ego and agent GT futures. $\nabla$Cost weighted uses the magnitude of the control cost gradient with respect to the GT future trajectory of the agent, proposed as a planning-aware prediction metric. Finally, DiffStack backpropagates gradients of the final loss to the prediction module.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Implementation details. We implement DiffStack in PyTorch and build on the open-source code of Trajectron++ and Differentiable MPC. We use $H = 4$s, $T = 3$s, and ${\Deltat} = 0.5$s. We train all models for 20 epochs using 4 NVIDIA Tesla V100 GPUs, taking 10--20 hours. Additional details are in Appendix C. The code is available at

<!-- chunk {"id": "body-0036", "role": "body", "section": "Open-loop results", "weight": 1.0} -->

End-to-end training is useful. Our main results are summarized in Table 1. The key observation is that DiffStack improves the effectiveness of predictions on ego planning by up to 15.5% compared to standard training ($\mathcal{L}_{ctr} = {- 1.86}$ vs. $- 1.61$); and reduces the gap to the cost attainable with a GT-informed oracle by 39.1% (${- 1.86} + 2.25$ vs. ${- 1.68} + 2.25$). DiffStack also improves planning without significantly impacting raw prediction accuracy (ADE=$1.27$ vs. $1.32$, within standard error). Alternative methods that re-weight the prediction loss in a planning-aware manner (rows 2 and 3) also help, but less than DiffStack. Surprisingly, we can even recover comparable prediction performance in terms of ADE when training solely for planning and control objectives (row 4). The poor distribution fit (high NLL) is due to our control cost being agnostic to the variance of the predicted GMMs.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Open-loop results", "weight": 1.0} -->

DiffStack makes fewer prediction errors that affect planning. Qualitatively analysing predictions and plans shows that the main source of improvement from end-to-end training is the reduction of spurious and/or unrealistic predictions that lead to plans with large (unnecessary) deviations from the lane center or the goal position. Fig. 3 shows two particular examples. In both cases, DiffStack's predictions are more realistic and accurate, yielding much more reasonable downstream plans.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Open-loop results", "weight": 1.0} -->

DiffStack can compensate for system integration errors. Integrating independently developed modules into an AV stack can be challenging due to, e.g., misaligned module interfaces. Table 2 shows results for an experiment that explores this issue. We introduce an artificial interface mismatch between prediction and planning by adding a fixed 1m offset to all GT prediction targets. As a result, the standard model yields very poor plans (note the positive value in row 1, indicating worse performance than baseline planning). However, DiffStack can compensate for interface mismatch and substantially improves the overall plans, suggesting that it can learn to correct erroneous predictions that affect planning. More broadly, these results demonstrate the potential for differentiable AV stacks to reduce various development/engineering costs associated with developing AVs, e.g., by replacing tedious manual parameter tuning with end-to-end data-driven optimization. We further explore this topic in the cost tuning experiments below.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Open-loop results", "weight": 1.0} -->

DiffStack can imitate humans better. Imitation learning results are summarized in Table 4. The overall performance of the stack is now measured by $\mathcal{L}_{ctr} = \mathcal{L}_{MSE}$, the MSE between planned and human expert trajectories relative to the MSE for the baseline planner (without predictions). We observe a similar trend as before; however, the results also reveal some limitations. The standard stack performs worse in terms of MSE than the baseline stack which neglects predictions entirely (note the positive sign for relative $\mathcal{L}_{MSE}$ in row 1). While DiffStack improves MSE significantly, the absolute difference is small. We hypothesize this is caused by our cost function not being rich enough to fully capture human driving behavior; and because agent-agent interactions that affect planning are rare in nominal driving data (comprised mainly of lane- and speed-keeping). These limitations could be addressed by a richer cost function and alternative goal definitions, which we leave to future work.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Open-loop results", "weight": 1.0} -->

DiffStack can learn a better control cost. While our main use case in this paper is to learn planning-aware prediction, DiffStack opens up various other opportunities for data-driven optimization of various components of the AV stack. For example, an important challenge in practice is to design a cost function for planning and control. In this experiment, we explore DiffStack's potential to learn interpretable control costs that optimize the quality of output plans from data. Table 3 reports results in the imitation learning setting, where we first train a prediction module (as before), then we train for an additional 20 epochs allowing DiffStack to update the weights $w_{i}$ of the control cost by backpropagating gradients from the final control loss $\mathcal{L}_{ctr}$. Compared to the default hand-tuned weights (row 1), DiffStack significantly decreases plan MSEs (row 2). The resulting learned weights $w_{i}$ are lower for the control effort term, and higher for the goal and lane keeping terms (see Appendix A). To ensure safety, we fix the weights for collision avoidance.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Open-loop results", "weight": 1.0} -->

We leave comparison with alternative techniques for learning control costs to future work. We expect DiffStack to be more effective compared to, e.g., Bayesian optimization, where the number of learned parameters is large.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Open-loop results", "weight": 1.0} -->

Ablations. Results of an ablation study can be found in Appendix A. In short, improvements from DiffStack are consistent with our observations when training for $\mathcal{L} = {\mathcal{L}_{pred} + \mathcal{L}_{plan}}$; $\mathcal{L} = {\mathcal{L}_{pred} + \mathcal{L}_{ctr}}$; when changing the relative scale of loss components; with higher time resolution ${\Deltat} = 0.1$ for planning and control; and when only using one of the planning or control modules.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Closed-loop evaluation", "weight": 1.0} -->

Simulation. We perform closed-loop simulation using a simple log-replay setup, where ego states are unrolled based on the planned control outputs and known dynamics, while non-ego agents follow their fixed trajectories recorded in the dataset. The evaluation scenarios are $T_{sim} = {10s}$ long. The goal and lane inputs for planning are updated in each simulation step based on the logged ego trajectory. We compute the following metrics. Trajectory Cost captures closed-loop performance: it evaluates the cost function $C$ on unrolled simulation trajectories, ${1/T_{sim}}{\sum_{{t = 1}:T_{sim}}{C{(s_{sim}^{(t)},u_{sim}^{(t)};s_{a \in A}^{\text{gt},t},m^{(t)})}}}$, where $s_{sim}$ and $u_{sim}$ are the unrolled ego state and control. We exclude the goal cost term because the goal is updated in each simulation step.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Closed-loop evaluation", "weight": 1.0} -->

Open-loop Cost is the average of hindsight costs calculated open-loop at each simulation step, $\mathcal{L}_{HC} = {C{(s_{ctr},u_{ctr};s_{a \in A}^{\text{gt}},g,m)}}$. Collision Cost is the collision term in the trajectory cost, $w_{1}C_{coll}{(s_{sim}^{(t)},s_{a \in A}^{\text{gt},{(t)}})}$. Lane Cost is the sum of lane keeping terms, ${w_{3}C_{\ell \perp}} + {w_{4}C_{\ell\measuredangle}}$. Control Effort is the control effort term, $w_{5}C_{u}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Closed-loop evaluation", "weight": 1.0} -->

Deviation is the average distance between unrolled and logged ego trajectories from the data, $\|{s_{sim}^{(t)} - s^{\text{gt},{(t)}}}\|$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Closed-loop evaluation", "weight": 1.0} -->

Results. Simulation results are in Table 5. Most importantly, we observe similar relative improvement for DiffStack in terms of closed loop trajectory cost as in terms of open-loop cost. DiffStack performs substantially better that the *no prediction* baseline, but somewhat surprisingly the standard stack performs worse, both in terms of closed-loop trajectory cost and open-loop cost. Analysing the cost components sheds light on possible reasons. As expected, incorporating predictions into planning results in lower collision costs, but higher lane keeping costs. The contribution of these two terms to the average cost depends on the data distribution, e.g., the frequency of close interactions where predictions are useful. As we saw earlier in Fig. 3, poor predictions in the standard stack frequently lead to unnecessary lane deviations in the planner. This is reflected in the substantially higher lane cost and control effort cost for the standard stack compared to DiffStack in Table 5.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Limitations & Conclusions", "weight": 1.5} -->

Limitations. One limitation of our work is the open-loop training and log-replay based simulation setup. In lieu of a real-world AV or a simulator with strong behavioral realism, this is standard practice; however, recent efforts on accurate behavior simulation could be leveraged in the future. Our implementation of DiffStack also has limitations. First, it is not differentiable wrt. *all* possible parameters, e.g., no gradients flow from the control loss to the planner's trajectory candidate generator. Future work may develop more sophisticated differentiable algorithms and explore ideas for gradient approximation for non-differentiable components. Second, individual modules could be improved, e.g., by adding a more sophisticated prediction model, improving candidate sampling in the planner, and adding trust-region constraints to the controller. Finally, even though hand-engineered components, modularity, and intermediate training objectives in differentiable stacks remedy challenges of learning AV policies end-to-end, other challenges naturally remain. For instance, designing an overall performance metric, or reducing the scarcity of and cost to obtain (interesting) driving data remain open problems, each of which are impactful areas of future work.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Limitations & Conclusions", "weight": 1.5} -->

Conclusions. In this paper we take a step towards fully-differentiable and modular AV stacks by introducing key differentiable components for prediction, planning, and control. Our experimental results show the potential benefits of jointly training modules of AV stacks for downstream performance. For motion prediction in particular, our results indicate that there is value in moving from purely prediction-oriented evaluation metrics towards downstream task-oriented metrics, in line with arguments in recent work. While our experiments focused on learning planning-aware predictions, DiffStack opens up various exciting opportunities for task-oriented learning in modular stacks. For example, we may learn a rich neural network as part of the control cost to capture hard-to-engineer concepts, e.g., reasoning with occlusions or accounting for uncertainties. Eventually, we envision having differentiable modules for the entire AV stack, allowing any subset of modules to be learned and optimized for a downstream task. Overall, this would relax information bottlenecks and enable uncertainty to more easily propagate through the stack without needing to forgo interpretability, modularity, and verifiabilty of the various components.
