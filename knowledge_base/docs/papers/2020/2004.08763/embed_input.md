<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Model-Predictive Control via Cross-Entropy and Gradient-Based Optimization

Topics include Trajectory optimization, Model predictive control, Cross-entropy method, Gradient-based optimization, Sampling-based control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines CEM-style action sampling with gradient descent refinement. Quite similar in spirit to Sampled DDP (SaDDP), but uses first-order (gradient) refinement instead of second-order (Hessian), and stays closer to vanilla CEM.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent works in high-dimensional model-predictive control and model-based reinforcement learning with learned dynamics and reward models have resorted to population-based optimization methods, such as the Cross-Entropy Method (CEM), for planning a sequence of actions. To decide on an action to take, CEM conducts a search for the action sequence with the highest return according to the dynamics model and reward. Action sequences are typically randomly sampled from an unconditional Gaussian distribution and evaluated on the environment. This distribution is iteratively updated towards action sequences with higher returns. However, this planning method can be very inefficient, especially for high-dimensional action spaces. An alternative line of approaches optimize action sequences directly via gradient descent, but are prone to local optima. We propose a method to solve this planning problem by interleaving CEM and gradient descent steps in optimizing the action sequence. Our experiments show faster convergence of the proposed hybrid approach, even for high-dimensional action spaces, avoidance of local minima, and better or equal performance to CEM. Code accompanying

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

High-dimensional, nonlinear Model-Predictive Control (MPC) and Model-Based Reinforcement Learning (MBRL) have seen significant progress over the last years, the task being to first learn a dynamics and a reward model of the environment and then plan using the learned models. While a number of recent approaches \[Hafner et al.Hafner, Lillicrap, Fischer, Villegas, Ha, Lee, and Davidson, Sharma et al.Sharma, Gu, Levine, Kumar, and Hausman, Chua et al.Chua, Calandra, McAllister, and Levine, Wang and Ba\] have developed efficient techniques for learning these models in MBRL, fewer papers \[Amos and Yarats, Srinivas et al.Srinivas, Jabri, Abbeel, Levine, and Finn\] have investigated the planning problem.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Instead, many state-of-the-art MBRL approaches perform planning either using the Cross-Entropy Method (CEM) \[Rubinstein, Chua et al.Chua, Calandra, McAllister, and Levine, Kobilarov\], or via Model-Predictive Path Integral (MPPI) \[Williams et al.Williams, Drews, Goldfain, Rehg, and Theodorou\]. Both these approaches are population-based search heuristics that sample random actions, execute them under the currently learned model, obtain the sum of rewards, and update the sampling distribution to increase the probability of higher reward action sequences. In MPC, the first action of the sequence is executed in the environment, the remaining planned actions are typically discarded, and the search procedure repeats.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many current MBRL approaches do not leverage gradients through the model, which are cheaply available, and resort to inefficient optimization, particularly in high dimensions, whereas gradient-based planning converges faster.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we combine the two methods, to take advantage of the convergence speed of gradient-based planning and the broader search, multi-extremum optimization performed by CEM. Gradient based optimization is one of the main approaches for a number of high-dimensional non-convex optimization problems in machine learning, yet it has not been widely adopted in planning problems due to the issue of vanishing or exploding gradients. We investigate situations where gradient-based planning fails, due to the sensitivity of shooting methods and imperfect models, and provide a simple way to mitigate it: we interleave CEM steps with gradient-based optimization, so that the latter can inform the update of the sampling distribution in the former.

<!-- chunk {"id": "body-0008", "role": "body", "section": "The Cross-Entropy Method for Planning", "weight": 1.0} -->

In model-based reinforcement learning and model predictive control, a model of the environment and reward is learned from real transitions in the environment. To select an action, MPC searches for an optimal action sequence under the learned model and executes the first action of that sequence, discarding the remaining actions. Typically this search is repeated after every step in the real environment, to account for any prediction errors by the model and to get feedback from the environment. In many works this planning step is done using the Cross-Entropy Method (CEM) \[Chua et al.Chua, Calandra, McAllister, and Levine, Hafner et al.Hafner, Lillicrap, Fischer, Villegas, Ha, Lee, and Davidson, Wang and Ba, Kobilarov\]. CEM samples action sequences from a time-evolving distribution, usually a diagonal Gaussian $a_{t:{t + H}} \sim {\mathcal{N}{(\mu_{t:{t + H}},{\text{diag}{(\sigma_{t:{t + H}}^{2})}})}}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The Cross-Entropy Method for Planning", "weight": 1.0} -->

These open-loop action sequences are simulated using the learned dynamics model to obtain approximate resulting state sequences and rewards. By repeatedly sampling random action trajectories, evaluating them under the model, and re-fitting the sampling distribution to the best $K$ trajectories, a new Gaussian distribution $\mu_{t:{t + H}},\sigma_{t:{t + H}}^{2}$ of actions for the current time-step is obtained. Convergence analysis for CEM for rare event simulation is given in \[Homem-de-Mello and Rubinstein\].

<!-- chunk {"id": "body-0010", "role": "body", "section": "The Cross-Entropy Method for Planning", "weight": 1.0} -->

Sampling random action sequences in this manner and evaluating the sum of rewards from them is very costly in practice because it does not leverage any implicit structure in the planning problem, and does not take advantage of the fact that gradients through the model can in fact be used to direct the search procedure, instead of naively sampling random action sequences.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Gradient-Based Planning", "weight": 1.0} -->

Gradient-based methods for planning typically correspond to backpropagating derivatives of a cumulative loss (or reward) function with respect to actions for updating the sequence of actions iteratively through gradient descent. In \[Henaff et al.Henaff, Whitney, and LeCun\], the gradients of the cumulative reward with respect to actions are computed by differentiating through the learned reward and forward dynamics models. In \[Srinivas et al.Srinivas, Jabri, Abbeel, Levine, and Finn\], gradients of the inner loss of the Gradient-Descent Planner (GDP) with respect to actions are computed in the latent space, by differentiating through a learned latent forward dynamics model. The ultimate aim is to update actions through an iterative gradient descent approach: Here, $H$ denotes the time-horizon of the episode, $a$ denotes action and $s$ denotes state. One of the most important drawbacks of gradient descent for non-convex optimization is that the optimization procedure is only guaranteed to converge to a local optima, not the global optima. In MPC for MBRL, these planners may converge to sub-optimal plans.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Gradient-Based Planning", "weight": 1.0} -->

In addition, for a long horizon $H$, there is the exploding and vanishing gradients problem which must be taken care of during optimization. An important point to note is that when the action dimension increases, CEM becomes highly inefficient and requires significantly more optimization epochs due to a blow-up of the search space, whereas there is only a slight increase (one gradient dimension) in computational burden for gradient descent. This is because, for optimization CEM utilizes just the aggregate reward which is a one-dimensional feedback signal per rollout, while gradient-based planning makes use of an $D$-dimensional feedback signal, namely the gradient of the cumulative reward with respect to the actions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Approach", "weight": 1.0} -->

Our approach is based on the motivation that in MPC, model gradients should be effectively used for conducting a more informed search during the planning phase. In the subsequent subsections, we describe a simple technique for doing this in practice.

<!-- chunk {"id": "body-0014", "role": "body", "section": "CEM+Gradient Descent", "weight": 1.0} -->

Since gradient descent is prone to getting stuck at local optima and in practice requires sufficiently different random initializations to alleviate this, we consider a very simple idea - interleave CEM steps with gradient descent on the samples to locally refine each plan. This method incorporates gradients through the model, thereby yielding more refined action sequences that can be used to update the CEM sampling distribution faster. Instead of resampling all plans, we choose to keep the top K plans from the previous iteration to continue optimizing them via gradient descent.

<!-- chunk {"id": "body-0015", "role": "body", "section": "CEM+Gradient Descent", "weight": 1.0} -->

Let $f_{\phi}$ denote the learned dynamics model, $r_{\psi}$ the learned reward model, $a_{h}$ the action at time-step $h$, $s_{h}$ the state of the environment at time-step $h$, and $H$ the planning horizon. Let $\mathcal{N}{(\mu_{0:H}^{(t)},\Sigma_{0:H}^{(t)})}$ denote the CEM sampling distribution from which action sequences are sampled in the $t^{th}$ CEM iteration. Here our notation for $\mathcal{N}$, refers to $H$ independent multivariate Gaussian distributions. We arbitrarily set the parameters $({{\mu_{0:H}^{} = 0},{\Sigma_{0:H}^{} = I}})$ of this distribution initially.

<!-- chunk {"id": "body-0016", "role": "body", "section": "CEM+Gradient Descent", "weight": 1.0} -->

At the beginning of each CEM iteration, the planner first samples multiple ($G$) random action sequences: We next evaluate the cumulative reward obtained from each of these action sequences, under the current learned dynamics model $f_{\phi}$ and the current reward model $r_{\psi}$: Here, $t$ indexes the CEM iterations. Now, treating these initial sampled plans as initialization of the gradient-descent procedure, we perform $J$ steps of gradient descent on all of the sequences. In all of our experiments to ensure fair comparison to CEM, we set $J = 1$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "CEM+Gradient Descent", "weight": 1.0} -->

Then we update the parameters of our proposal (sampling) distribution $\mathcal{N}{(\mu_{0:H}^{({t + 1})},\Sigma_{0:H}^{({t + 1})})}$ to match the top $K$ updated action sequences: Finally, we replace the bottom $G - K$ action sequences, with samples from the updated proposal distribution. After $T$ iterations of this, the remaining action sequence with the highest reward is returned. Our approach is summarized in Algorithm 1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "CEM+Gradient Descent", "weight": 1.0} -->

H(t), Σ0: H(t)) Execute first action from the highest model return action sequence Record real transition in 𝒟 Algorithm 1 Grad+CEM Algorithm (The proposed approach)

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experiments", "weight": 1.0} -->

Through the experiments we aim to demonstrate the benefits and pitfalls of CEM and gradient descent, and demonstrate the efficacy of the proposed approach. The gradient-based planner baseline is hereafter referred to as Grad. This is implemented as SGD (Stochastic Gradient Descent). It samples $G$ initial samples and separately performs $T$ stochastic gradient steps on them. To better demonstrate our claims, we created a toy environment, the details of which are described in the next sub-section. Code for the experiments is available in this repository Figure 2: Illustrative diagram of the toy environment. The black paths are 2D projections of multiple paths of a point mass. Red denotes high reward and blue denotes low reward regions. The green circle is an obstacle with soft contact.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Details of the toy environment", "weight": 1.0} -->

To consider the planning problem in isolation, we created a toy environment in which we have access to ground truth gradients through the dynamics model. The agent controls a mass in an N dimensional space by applying forces at each time step. Fig. 2 shows a 2D projection of the environment. The task is to move towards high reward regions of the state-space (red region) from the blue region. The black lines and dots show 2D projections of multiple rolled out trajectories starting from the origin. The fluorescent green region denotes an obstacle with soft contact. The soft contact is modeled as a repulsive spring force at every time step that increases proportionally to the penetration depth of the agent into the obstacle. The "hardness" of the contact can be tuned by the spring constant. The larger the spring constant is, the stronger is the repulsion force. For all the toy environment results, all the methods used $T = 10$ number of iterations. To make a fair comparison we set the number of inner gradient steps per iteration $J = 1$ for Grad+CEM. All methods used $G = 20$ sampled plans at each iteration.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Details of the toy environment", "weight": 1.0} -->

CEM and Grad+CEM both select the top $K = 4$ plans at each iteration.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Results in high dimensions", "weight": 1.0} -->

In the toy environment shown in Fig. 2, we hypothesize that increasing the dimensions of the action space is likely to deteriorate the performance of a vanilla CEM planner but not of a gradient descent based planner. Fig. 3 shows a comparative analysis of total reward collected in the environment as the number of action dimensions are increased from 2 to 20.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Results in high dimensions", "weight": 1.0} -->

(a) Performance of different planners for single obstacle, soft contact case as the environment dimensionality (both states and actions) is increased.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Results in high dimensions", "weight": 1.0} -->

(b) Multi-object, hard contact two-dimensional case as the number of obstacles is increased. For simulating hard contact, the spring constant 10 times larger.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Results in high dimensions", "weight": 1.0} -->

There is a significant drop in the performance of the CEM based planner with increasing action dimensionality. For optimization CEM utilizes just the aggregate reward, which is a one-dimensional error signal per rollout, while gradient-based planning makes use of a $D$-dimensional error signal, namely the gradient.

<!-- chunk {"id": "body-0026", "role": "body", "section": "When gradient based optimization fails", "weight": 1.0} -->

Fig. 4 shows an experimental scenario that involves multiple obstacles with non-smooth contact (the spring constant is set 10 times higher). Here it is evident that the purely gradient based approach does not succeed and gets stuck in some local optima. The main reason for this is that the non-smooth contact results in discontinuous gradients (e.g. consider the edge of a table. There is a sudden jump in the magnitude of the gradients when moving from one edge to the other) which make learning difficult. To alleviate this, we show in Fig. 3 that interleaving CEM and gradient-descent update steps helps learn better plans.

<!-- chunk {"id": "body-0027", "role": "body", "section": "When gradient based optimization fails", "weight": 1.0} -->

Note that we decrease the size of obstacles as we increase their number in order to pack them into the same space and that is why it is possible for Grad+CEM to do better as the number of obstacles increases.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments with Planning over Learned Dynamics Models", "weight": 1.0} -->

In this section, we consider the complete MBRL problem of learning dynamics+reward models and using the learned models to do planning. In particular, we consider the SOTA Planet \[Hafner et al.Hafner, Lillicrap, Fischer, Villegas, Ha, Lee, and Davidson\] model and replace the CEM based planning module with the proposed Grad+CEM approach. Fig. 5 shows that for two different OpenAI Gym \[Brockman et al.Brockman, Cheung, Pettersson, Schneider, Schulman, Tang, and Zaremba\] environments, Pendulum and Half-Cheetah, while the default CEM based planning scheme struggles to converge in terms of the test rewards, incorporating model gradients for planning ensures a quick and reliable convergence. So, from the experiments we conclude that the Grad+CEM scheme helps in converging to higher rewards faster, with fewer optimization iterations.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments with Planning over Learned Dynamics Models", "weight": 1.0} -->

For Fig. 5 and Fig. 5, for a pairwise t-test between the two variants CEM and Grad+CEM, we respectively obtain p-values 0.019 and 0.004. Both results are significant at $p < 0.05$. In Fig. 6, conducting a pairwise t-test for (a), (b), (c), and (d), we respectively obtain p-values 0.314, 0.103, 0.121, and 0.136. These results are not significant at $p < 0.05$. In the Pendulum environment, the pendulum starts at a random position, and the goal is to swing it up so that it stays upright. In the Half-Cheetah environment, the agent gets rewarded for moving a fast as possible and maintaining proper gait (not toppling over). In both these environments, the input to the policy are high dimensional rendered images, which make the tasks challenging. Our main conclusions from these experiments are that the hybrid method has equal or better search performance compared to CEM. The main advantages of the proposed hybrid method, as shown in Figs.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments with Planning over Learned Dynamics Models", "weight": 1.0} -->

2, 3, and 4 include faster speed of convergence compared to CEM, when the dimensionality of the action space increases, as well as broader coverage of local minima than gradient-based optimization.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments with Planning over Learned Dynamics Models", "weight": 1.0} -->

(a) OpenAI Gym Half-Cheetah [Brockman et al.Brockman, Cheung, Pettersson, Schneider, Schulman, Tang, and Zaremba] (b) OpenAI Gym Pendulum [Brockman et al.Brockman, Cheung, Pettersson, Schneider, Schulman, Tang, and Zaremba] Figure 5: Variation of rewards at test time during the course of training. OpenAI Gym (a) Pendulum and (b) Half-Cheetah environments. CEM is the default Planet [Hafner et al.Hafner, Lillicrap, Fischer, Villegas, Ha, Lee, and Davidson] algorithm that plans through CEM. Grad+CEM is the version of Planet that plans using the proposed Grad+CEM scheme. The error bars correspond to the standard deviation during evaluation with three random seeds. Higher is better.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments with Planning over Learned Dynamics Models", "weight": 1.0} -->

(a) DM Control Suite Cartpole-SwingUp (b) DM Control Suite WalkerWalk (c) DM Control Suite Reacher (d) DM Control Suite Cartpole-Balance Figure 6: Variation of rewards at test time during the course of training. DeepMind Control Suite [Tassa et al.Tassa, Doron, Muldal, Erez, Li, Casas, Budden, Abdolmaleki, Merel, Lefrancq, et al.] (a) Cartpole-SwingUp, (b) Walker-Walk, (c) Reacher, and (d) Cartpole-Balance environments. CEM is the default Planet [Hafner et al.Hafner, Lillicrap, Fischer, Villegas, Ha, Lee, and Davidson] algorithm that plans through CEM. Grad+CEM is the version of Planet that plans using the proposed Grad+CEM scheme. The error bars correspond to standard deviation during evaluation with three random seeds. Higher is better.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Related Works", "weight": 1.0} -->

Our paper is broadly based on the theme of model-based reinforcement learning (MBRL) \[Chua et al.Chua, Calandra, McAllister, and Levine, Hafner et al.Hafner, Lillicrap, Fischer, Villegas, Ha, Lee, and Davidson\], where the idea is to learn a dynamics model of the world and plan using the learned dynamics model. For high dimensional inputs like images, the dynamics are typically learned in a learnt latent space \[Hafner et al.Hafner, Lillicrap, Fischer, Villegas, Ha, Lee, and Davidson\]. Most current MBRL approaches use some version of the Cross-Entropy Method (CEM) for doing a random population based search of plans given the current model \[Wang and Ba, Hafner et al.Hafner, Lillicrap, Fischer, Villegas, Ha, Lee, and Davidson\].

<!-- chunk {"id": "body-0034", "role": "body", "section": "Related Works", "weight": 1.0} -->

Some papers \[Sharma et al.Sharma, Gu, Levine, Kumar, and Hausman\] use other population based search approaches like Model-Predictive Path Integral (MPPI) \[Williams et al.Williams, Drews, Goldfain, Rehg, and Theodorou\] for planning. A recent paper \[Okada and Taniguchi\] discusses how in the control as inference framework, the two approaches, CEM, and MPPI are very similar, and differ only with respect to the reward function $r{(s_{1:H})}$. Both these random shooting approaches are very costly and take a long time to converge because they involve sampling random action sequences and evaluating them under the current model to determine the high performing sequences. Although \[Wang and Ba\] introduces the idea of performing the CEM search in the parameter space of a distilled policy, it still is very costly and requires a lot of samples for convergence.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Related Works", "weight": 1.0} -->

Gradient-descent based optimization methods have been successful in a wide range of machine learning domains \[Finn et al.Finn, Abbeel, and Levine\], but for planning, there are very few papers that have been able to successfully perform gradient-descent based planning. Universal Planning Networks (UPNs) \[Srinivas et al.Srinivas, Jabri, Abbeel, Levine, and Finn\] optimizes action sequences in a latent space such that the optimized sequence matches expert demonstrations of actions. So the approach requires high quality expert data, and is based on imitation learning, not end-to-end reinforcement learning. SGD for model predictive control is also done in \[Henaff et al.Henaff, Whitney, and LeCun\] but without a diverse initialization it can lead to local optima. Hence the approach is limited to simple grid worlds, and cannot scale to more challenging robotic tasks \[Von Stryk and Bulirsch, Diehl et al.Diehl, Bock, Diedam, and Wieber\].

<!-- chunk {"id": "body-0036", "role": "body", "section": "Related Works", "weight": 1.0} -->

In the context of model-free reinforcement learning, \[Pourchot and Sigaud\] also introduce the idea of interleaving CEM and policy gradient steps in optimizing in the parameter space of policies. We show how interleaving CEM and gradient descent steps can be used as an effective planner for model predictive control in the context of model based reinforcement learning.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Related Works", "weight": 1.0} -->

Direct collocation approaches for control, address some of the ill-conditioning of shooting methods, and avoid backpropagating the model through time, by parameterizing the state and action sequences and optimizing both jointly. In this setting, \[Subbarao and Shippey\] propose initializing the collocation optimization from a solution found by a genetic algorithm similar to CEM. However, they do not interleave the two optimizations and the collocation method requires parameterizing state trajectories with analytic functions such as splines.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Limitations and Future Works", "weight": 1.5} -->

One of the main directions for future works is to investigate the implications of model-bias in the planning scheme. In MBRL, one of the primary issues leading to a suboptimal plan is that the planner exploits model bias of an imperfectly learned model \[Wang et al.Wang, Bao, Clavera, Hoang, Wen, Langlois, Zhang, Zhang, Abbeel, and Ba\]. So, for better planning, we also need to develop better strategies for learning the dynamics model itself. Some papers \[Chua et al.Chua, Calandra, McAllister, and Levine, Kurutach et al.Kurutach, Clavera, Duan, Tamar, and Abbeel\] aim to learn a better model by maintaining an ensemble of neural network models. This helps model epistemic uncertainty, but an ensemble of networks for the dynamics is difficult to scale to image-based environments without introducing a huge computational burden during training.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Limitations and Future Works", "weight": 1.5} -->

Another effective direction for tackling model-bias is by learning dynamics models conditioned on some latent variables, instead of trying to learn a global dynamics model. A recent paper, DADS \[Sharma et al.Sharma, Gu, Levine, Kumar, and Hausman\] does this by conditioning the dynamics model on latent 'skills' and the main idea is to learn smaller behavior-specific dynamics models instead of trying to learn a global dynamics model. The latent 'skills' are basically an abstraction for the low-level action sequences that get executed in the environment. However, DADS does not leverage the latent abstractions for planning, it uses them only for learning the dynamics model. One potential extension of our approach would be to use such latent variable models for planning as well, by backpropagating gradients wrt the latent variables through the model, in order to update the low-level actions.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we investigate the problem of planning and optimization in model predictive control and in the context of model-based reinforcement learning. We address the scaling problems of the widely-used, but gradient-free, Cross-Entropy Method, which struggles as the dimensionality of the environment increases. This is an important issue as we scale these methods to real world control problems. On the other hand, gradient-descent-based planning is conveniently applicable to high-dimensional continuous control problems, especially since the learned dynamics models are typically parameterized by differentiable functions. We show that in environments with many local optima, pure gradient descent can fail to find an optimal solution, compared to CEM. Combining the strengths of the two approaches, we propose a simple method that interleaves CEM and gradient descent updates, and we show that this method scales to higher dimensions and performs at least as well as CEM on multi-extrema settings, while benefiting from the convergence speed of gradient-based optimization.
