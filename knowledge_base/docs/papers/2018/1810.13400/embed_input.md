<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Differentiable MPC for End-to-end Planning and Control

Topics include Reinforcement learning, Imitation learning, Model predictive control, Predictive control, System identification, Neural networks, Planning, Control, Learning, Differentiable model predictive control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present foundations for using Model Predictive Control (MPC) as a differentiable policy class for reinforcement learning in continuous state and action spaces. This provides one way of leveraging and combining the advantages of model-free and model-based approaches. Specifically, we differentiate through MPC by using the KKT conditions of the convex approximation at a fixed point of the controller. Using this strategy, we are able to learn the cost and dynamics of a controller via end-to-end learning. Our experiments focus on imitation learning in the pendulum and cartpole domains, where we learn the cost and dynamics terms of an MPC policy class. We show that our MPC policies are significantly more data-efficient than a generic neural network and that our method is superior to traditional system identification in a setting where the expert is unrealizable.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model-free reinforcement learning has achieved state-of-the-art results in many challenging domains. However, these methods learn black-box control policies and typically suffer from poor sample complexity and generalization. Alternatively, model-based approaches seek to model the environment the agent is interacting. Many model-based approaches utilize Model Predictive Control (MPC) to perform complex control tasks. MPC leverages a predictive model of the controlled system and solves an optimization problem online in a receding horizon fashion to produce a sequence of control actions. Usually the first control action is applied to the system, after which the optimization problem is solved again for the next time step.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Formally, MPC requires that at each time step we solve the optimization problem: where $x_{t},u_{t}$ are the state and control at time $t$, $\mathcal{X}$ and $\mathcal{U}$ are constraints on valid states and controls, $C_{t}:{{\mathcal{X} \times \mathcal{U}}\rightarrow{\mathbb{R}}}$ is a (potentially time-varying) cost function, $f:{{\mathcal{X} \times \mathcal{U}}\rightarrow\mathcal{X}}$ is a dynamics model, and $x_{init}$ is the initial state of the system. The optimization problem in eq. 1 can be efficiently solved in many ways, for example with the finite-horizon iterative Linear Quadratic Regulator (iLQR) algorithm. Although these techniques are widely used in control domains, much work in deep reinforcement learning or imitation learning opts instead to use a much simpler policy class such as a linear function or neural network.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The advantages of these policy classes is that they are differentiable and the loss can be directly optimized with respect to them while it is typically not possible to do full end-to-end learning with model-based approaches.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we consider the task of learning MPC-based policies in an end-to-end fashion, illustrated in fig. 1. That is, we treat MPC as a generic policy class $u = {\pi{(x_{init};C,f)}}$ parameterized by some representations of the cost $C$ and dynamics model $f$. By differentiating *through* the optimization problem, we can learn the costs and dynamics model to perform a desired task. This is in contrast to regressing on collected dynamics or trajectory rollout data and learning each component in isolation, and comes with the typical advantages of end-to-end learning (the ability to train directly based upon the task loss of interest, the ability to "specialize" parameter for a given task, etc).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Still, efficiently differentiating through a complex policy class like MPC is challenging. Previous work with similar aims has either simply unrolled and differentiated through a simple optimization procedure or has considered generic optimization solvers that do not scale to the size of MPC problems. This paper makes the following two contributions to this space. First, we provide an efficient method for *analytically* differentiating through an iterative non-convex optimization procedure based upon a box-constrained iterative LQR solver; in particular, we show that the analytical derivative can be computed using *one additional* backward pass of a modified iterative LQR solver. Second, we empirically show that in imitation learning scenarios we can recover the *cost* and *dynamics* from an MPC expert with a loss based only on the actions (and not states). In one notable experiment, we show that directly optimizing the imitation loss results in better performance than vanilla system identification.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Differentiable LQR", "weight": 1.0} -->

Discrete-time finite-horizon LQR is a well-studied control method that optimizes a convex quadratic objective function with respect to affine state-transition dynamics from an initial system state $x_{init}$. Specifically, LQR finds the optimal nominal trajectory $\tau_{1:T}^{\star} = {\{ x_{t},u_{t}\}}_{1:T}$ by solving the optimization problem From a policy learning perspective, this can be interpreted as a module with unknown parameters $\theta = {\{ C,c,F,f\}}$, which can be integrated into a larger end-to-end learning system. The learning process involves taking derivatives of some loss function $\ell$, which are then used to update the parameters.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Differentiable LQR", "weight": 1.0} -->

Instead of directly computing each of the individual gradients, we present an efficient way of computing the derivatives of the loss function with respect to the parameters By interpreting LQR from an optimization perspective, we associate dual variables $\lambda_{0:{T - 1}}$ with the state constraints, where $\lambda_{0}$ is associated with the $x_{1} = x_{init}$ constraint and $\lambda_{1:{T - 1}}$ are associated with the remaining ones, respectively. The Lagrangian of the optimization problem is then where the initial constraint $x_{1} = x_{init}$ is represented by setting $F_{0} = 0$ and $f_{0} = x_{init}$. Differentiating eq. 4 with respect to $\tau_{t}^{\star}$ yields where the $\lambda_{t - 1}^{\star}$ term comes from the $x_{t + 1}$ term in eq. 4.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Differentiable LQR", "weight": 1.0} -->

module]alg:differentiable-lqr Input: Initial state xinit 1:τ1: T⋆ = LQRT (xinit; C, c, F, f) ⊳ Solve 1:dτ1: T⋆ = LQRT (0; C, ∇τ⋆ℓ, F, 0) ⊳ Solve, ideally reusing the factorizations from the forward pass 3:Compute the derivatives of ℓ with respect to C, c, F, f, and xinit with Module 1 Differentiable LQR (The LQR algorithm is defined in appendix A) Thus, the normal approach to solving LQR problems with dynamic Riccati recursion can be viewed as an efficient way of solving the KKT system Given an optimal nominal trajectory $\tau_{1:T}^{\star}$, eq.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Differentiable LQR", "weight": 1.0} -->

Since LQR is a constrained convex quadratic $\operatorname{argmin}$, the derivatives of the loss with respect to the LQR parameters can be obtained by implicitly differentiating the KKT conditions. Applying the approach from Section 3 of Amos and Kolter, the derivatives are where $\otimes$ is the outer product operator, and $d_{\tau}^{\star}$ and $d_{\lambda}^{\star}$ are obtained by solving the linear system We observe that eq. 18 is of the same form as the linear system in eq. 15 for the LQR problem. Therefore, we can leverage this insight and solve eq. 18 efficiently by solving another LQR problem that replaces $c_{t}$ with $\nabla_{\tau_{t}^{\star}}\ell$ and $f_{t}$ with 0. Moreover, this approach enables us to re-use the factorization of $K$ from the forward pass instead of recomputing.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Differentiable LQR", "weight": 1.0} -->

LABEL:alg:differentiable-lqr summarizes the forward and backward passes for a differentiable LQR module.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Differentiable MPC", "weight": 1.0} -->

While LQR is a powerful tool, it does not cover realistic control problems with non-linear dynamics and cost. Furthermore, most control problems have natural bounds on the control space that can often be expressed as box constraints. These highly non-convex problems, which we will refer to as model predictive control (MPC), are well-studied in the control literature and can be expressed in the general form where the non-convex cost function $C_{\theta}$ and non-convex dynamics function $f_{\theta}$ are (potentially) parameterized by some $\theta$. We note that more generic constraints on the control and state space can be represented as penalties and barriers in the cost function. The standard way of solving the control problem in eq.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Differentiable MPC", "weight": 1.0} -->

19 is by iteratively forming and optimizing a convex approximation where we have defined the second-order Taylor approximation of the cost around $\tau^{i}$ as with $p_{t}^{i} = {\nabla_{\tau_{t}^{i}}C_{\theta,t}}$ and $H_{t}^{i} = {\nabla_{\tau_{t}^{i}}^{2}C_{\theta,t}}$. We also have a first-order Taylor approximation of the dynamics around $\tau^{i}$ as with $F_{t}^{i} = {\nabla_{\tau_{t}^{i}}f_{\theta,t}}$. In practice, a fixed point of eq. 20 is often reached, especially when the dynamics are smooth. As such, differentiating the non-convex problem eq. 19 can be done exactly by using the final convex approximation. Without the box constraints, the fixed point in eq.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Differentiable MPC", "weight": 1.0} -->

20 could be differentiated with LQR as we show in section 3. In the next section, we will show how to extend this to the case where we have box constraints on the controls as well.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Differentiating Box-Constrained QPs", "weight": 1.0} -->

First, we consider how to differentiate a more generic box-constrained convex QP of the form Given active inequality constraints at the solution in the form ${\overset{\sim}{G}x} = \overset{\sim}{h}$, this problem turns into an equality-constrained optimization problem with the solution given by the linear system With some loss function $\ell$ that depends on $x^{\star}$, we can use the approach in Amos and Kolter to obtain the derivatives of $\ell$ with respect to $Q$, $p$, $A$, and $b$ as where $d_{x}^{\star}$ and $d_{\lambda}^{\star}$ are obtained by solving the linear system The constraint ${\overset{\sim}{G}d_{x}^{\star}} = 0$ is equivalent to the constraint $d_{x_{i}}^{\star} = 0$ if $x_{i}^{\star} \in

<!-- chunk {"id": "body-0017", "role": "body", "section": "Differentiating Box-Constrained QPs", "weight": 1.0} -->

{\{{\underset{¯}{x}}_{i},{\overline{x}}_{i}\}}$. Thus solving the system in eq. 26 is equivalent to solving the optimization problem

<!-- chunk {"id": "body-0018", "role": "body", "section": "Differentiating MPC with Box Constraints", "weight": 1.0} -->

module]alg:differentiable-mpc Given: Initial state xinit and initial control sequence uinit Parameters: θ of the objective Cθ (τ) and dynamics fθ (τ) 1:$\tau_{1:T}^{\star} = {{MPC}_{T,\underset{¯}{u},\overline{u}}{(x_{init},u_{init};C_{\theta},F_{\theta})}}$ ⊳ Solve eq.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Differentiating MPC with Box Constraints", "weight": 1.0} -->

19 2:The solver should reach the fixed point in to obtain approximations to the cost Hθn and dynamics Fθn 1:${\overset{\sim}{F}}_{\theta}^{n}$ is Fθn with the rows corresponding to the tight control constraints zeroed 2:$d_{\tau_{1:T}}^{\star} = {{LQR}_{T}{(0;H_{\theta}^{n},{\nabla_{\tau^{\star}}\ell},{\overset{\sim}{F}}_{\theta}^{n},0)}}$ ⊳ Solve, ideally reusing the factorizations from the forward pass 4:Differentiate ℓ with respect to the approximations Hθn and Fθn with 5:Differentiate these approximations with respect to θ and use the chain rule to obtain ∂ℓ/∂θ Module 2 Differentiable MPC (The MPC algorithm is defined in appendix A) At a fixed point, we can use eq.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Differentiating MPC with Box Constraints", "weight": 1.0} -->

Solving this system can be equivalently written as a zero-constrained LQR problem of the form | | {d_{\tau_{1:T}}^{\star} = \operatorname{argmin}\limits_{d_{\tau_{1:T}}}} & {{\sum\limits_{t}{\frac{1}{2}d_{\tau_{t}}^{\top}H_{t}^{n}d_{\tau_{t}}}} + {{({\nabla_{\tau_{t}^{\star}}\ell})}^{\top}d_{\tau_{t}}}} \\ | | | where $n$ is the iteration that eq. 20 reaches a fixed point, and $H^{n}$ and $F^{n}$ are the corresponding approximations to the objective and dynamics defined earlier. LABEL:alg:differentiable-mpc summarizes the proposed differentiable MPC module. To solve the MPC problem in eq.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Differentiating MPC with Box Constraints", "weight": 1.0} -->

19 and reach the fixed point in eq. 20, we use the box-DDP heuristic. For the zero-constrained LQR problem in eq. 28 to compute the derivatives, we use an LQR solver that zeros the appropriate controls.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Drawbacks of Our Approach", "weight": 1.0} -->

Sometimes the controller does not run for long enough to reach a fixed point of eq. 20, or a fixed point doesn't exist, which often happens when using neural networks to approximate the dynamics. When this happens, eq. 28 cannot be used to differentiate through the controller, because it assumes a fixed point. Differentiating through the final iLQR iterate that's not a fixed point will usually give the wrong gradients. Treating the iLQR procedure as a compute graph and differentiating through the unrolled operations is a reasonable alternative in this scenario that obtains surrogate gradients to the control problem. However, as we empirically show in section 5.1, the backward pass of this method scales linearly with the number of iLQR iterations used in the forward. Instead, fixed-point differentiation is constant time and only requires a single LQR solve.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In this section, we present several results that highlight the performance and capabilities of differentiable MPC in comparison to neural network policies and vanilla system identification (SysId). We show 1) superior runtime performance compared to an unrolled solver, 2) the ability of our method to recover the cost and dynamics of a controller with imitation, and 3) the benefit of directly optimizing the task loss over vanilla SysId.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We have released our differentiable MPC solver as a standalone open source package that is available at and our experimental code for this paper is also openly available at Our experiments are implemented with PyTorch.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Imitation Learning: Linear-Dynamics Quadratic-Cost (LQR)", "weight": 1.0} -->

In this section, we show results to validate the MPC solver and gradient-based learning approach for an imitation learning problem. The expert and learner are LQR controllers that share all information except for the linear system dynamics ${f{(x_{t},u_{t})}} = {{Ax_{t}} + {Bu_{t}}}$. The controllers have the same quadratic cost (the identity), control bounds $\lbrack{- 1},1\rbrack$, horizon (5 timesteps), and 3-dimensional state and control spaces. Though the dynamics can also be recovered by fitting next-state transitions, we show that we can alternatively use imitation learning to recover the dynamics using only controls.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Imitation Learning: Linear-Dynamics Quadratic-Cost (LQR)", "weight": 1.0} -->

Given an initial state $x$, we can obtain nominal actions from the controllers as $u_{1:T}{(x;\theta)}$, where $\theta = {\{ A,B\}}$. We randomly initialize the learner's dynamics with $\hat{\theta}$ and minimize the imitation loss We do learning by differentiating $\mathcal{L}$ with respect to $\hat{\theta}$ (using mini-batches with 32 examples) and taking gradient steps with RMSprop. Figure 3 shows the model and imitation loss of eight randomly sampled initial dynamics, where the model loss is ${MSE}{(\theta,\hat{\theta})}$. The model converges to the true parameters in half of the trials and achieves a perfect imitation loss. The other trials get stuck in a local minimum of the imitation loss and causes the approximate model to significantly diverge from the true model. These faulty trials highlight that despite the LQR problem being convex, the optimization problem of some loss function w.r.t.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Imitation Learning: Linear-Dynamics Quadratic-Cost (LQR)", "weight": 1.0} -->

the controller's parameters is a (potentially difficult) non-convex optimization problem that typically does not have convergence guarantees.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Imitation Learning: Non-Convex Continuous Control", "weight": 1.0} -->

We next demonstrate the ability of our method to do imitation learning in the pendulum and cartpole benchmark domains. Despite being simple tasks, they are relatively challenging for a generic poicy to learn quickly in the imitation learning setting. In our experiments we use MPC experts and learners that produce a nominal action sequence $u_{1:T}{(x;\theta)}$ where $\theta$ parameterizes the model that's being optimized. The goal of these experiments is to optimize the imitation loss $\mathcal{L} = {{\mathbb{E}}_{x}\left\lbrack {\|{{u_{1:T}{(x;\theta)}} - {u_{1:T}{(x;\hat{\theta})}}}\|}_{2}^{2} \right\rbrack}$, again which we can uniquely do using *only* observed controls and *no* observations. We consider the following methods: Baselines: *nn* is an LSTM that takes the state $x$ as input and predicts the nominal action sequence.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Imitation Learning: Non-Convex Continuous Control", "weight": 1.0} -->

In this setting we optimize the imitation loss directly. *sysid* assumes the cost of the controller is known and approximates the parameters of the dynamics by optimizing the next-state transitions.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Imitation Learning: Non-Convex Continuous Control", "weight": 1.0} -->

Our Methods: *mpc.dx* assumes the cost of the controller is known and approximates the parameters of the dynamics by directly optimizing the imitation loss. *mpc.cost* assumes the dynamics of the controller is known and approximates the cost by directly optimizing the imitation loss. *mpc.cost.dx* approximates both the cost and parameters of the dynamics of the controller by directly optimizing the imitation loss.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Imitation Learning: Non-Convex Continuous Control", "weight": 1.0} -->

In all settings that involve learning the dynamics (*sysid*, *mpc.dx*, and *mpc.cost.dx*) we use a parameterized version of the true dynamics. In the pendulum domain, the parameters are the mass, length, and gravity; and in the cartpole domain, the parameters are the cart's mass, pole's mass, gravity, and length. For cost learning in *mpc.cost* and *mpc.cost.dx* we parameterize the cost of the controller as the weighted distance to a goal state ${C{(\tau)}} = {\|{w_{g} \circ {({\tau - \tau_{g}})}}\|}_{2}^{2}$. We have found that simultaneously learning the weights $w_{g}$ and goal state $\tau_{g}$ is instable and in our experiments we alternate learning of $w_{g}$ and $\tau_{g}$ independently every 10 epochs.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Imitation Learning: Non-Convex Continuous Control", "weight": 1.0} -->

We collected a dataset of trajectories from an expert controller and vary the number of trajectories our models are trained. A single trial of our experiments takes 1-2 hours on a modern CPU. We optimize the *nn* setting with Adam with a learning rate of $10^{- 4}$ and all other settings are optimized with RMSprop with a learning rate of $10^{- 2}$ and a decay term of $0.5$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Imitation Learning: Non-Convex Continuous Control", "weight": 1.0} -->

Again, while we emphasize that these are simple tasks, there are stark differences between the approaches. Unlike the generic network-based imitation learning, the MPC policy can exploit its inherent structure. Specifically, because the network contains a well-defined notion of the dynamics and cost, it is able to learn with much lower sample complexity that a typical network. But unlike pure system identification (which would be reasonable only for the case where the physical parameters are unknown but all other costs are known), the differentiable MPC policy can naturally be adapted to objectives *besides* simple state prediction, such as incorporating the additional cost learning portion.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Imitation Learning: SysId with a non-realizable expert", "weight": 1.0} -->

All of our previous experiments that involve SysId and learning the dynamics are in the unrealistic case when the expert's dynamics are in the model class being learned. In this experiment we study a case where the expert's dynamics are *outside* of the model class being learned. In this setting we will do imitation learning for the parameters of a dynamics function with vanilla SysId and by directly optimizing the imitation loss (*sysid* and the *mpc.dx* in the previous section, respectively).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Imitation Learning: SysId with a non-realizable expert", "weight": 1.0} -->

SysId often fits observations from a noisy environment to a simpler model. In our setting, we collect optimal trajectories from an expert in the pendulum environment that has an additional damping term and also has another force acting on the point-mass at the end (which can be interpreted as a "wind" force). We do learning with dynamics models that *do not* have these additional terms and therefore we *cannot* recover the expert's parameters. Figure 5 shows that even though vanilla SysId is slightly better at optimizing the next-state transitions, it finds an inferior model for imitation compared to our approach that directly optimizes the imitation loss.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Imitation Learning: SysId with a non-realizable expert", "weight": 1.0} -->

We argue that the goal of doing SysId is rarely in isolation and always serves the purpose of performing a more sophisticated task such as imitation or policy learning. Typically SysId is merely a surrogate for optimizing the task and we claim that the task's loss signal provides useful information to guide the dynamics learning. Our method provides one way of doing this by allowing the task's loss function to be directly differentiated with respect to the dynamics function being learned.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper lays the foundations for differentiating and learning MPC-based controllers within reinforcement learning and imitation learning. Our approach, in contrast to the more traditional strategy of "unrolling" a policy, has the benefit that it is much less computationally and memory intensive, with a backward pass that is essentially free given the number of iterations required for a the iLQR optimizer to converge to a fixed point. We have demonstrated our approach in the context of imitation learning, and have highlighted the potential advantages that the approach brings over generic imitation learning and system identification.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We also emphasize that one of the primary contributions of this paper is to define and set up the framework for differentiating through MPC in general. Given the recent prominence of attempting to incorporate planning and control methods into the loop of deep network architectures, the techniques here offer a method for efficiently integrating MPC policies into such situations, allowing these architectures to make use of a very powerful function class that has proven extremely effective in practice. The future applications of our differentiable MPC method include tuning model parameters to task-specific goals and incorporating joint model-based and policy-based loss functions; and our method can also be extended for stochastic control.
