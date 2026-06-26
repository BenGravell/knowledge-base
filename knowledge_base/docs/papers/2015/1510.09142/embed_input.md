<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Continuous Control Policies by Stochastic Value Gradients

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a unified framework for learning continuous control policies using backpropagation. It supports stochastic control by treating stochasticity in the Bellman equation as a deterministic function of exogenous noise. The product is a spectrum of general policy gradient algorithms that range from model-free methods with value functions to model-based methods without value functions. We use learned models but only require observations from the environment in- stead of observations from model-predicted trajectories, minimizing the impact of compounded model errors. We apply these algorithms first to a toy stochastic control problem and then to several physics-based control problems in simulation. One of these variants, SVG, shows the effectiveness of learning models, value functions, and policies simultaneously in continuous domains.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy gradient algorithms maximize the expectation of cumulative reward by following the gradient of this expectation with respect to the policy parameters. Most existing algorithms estimate this gradient in a model-free manner by sampling returns from the real environment and rely on a likelihood ratio estimator. Such estimates tend to have high variance and require large numbers of samples or, conversely, low-dimensional policy parameterizations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A second approach to estimate a policy gradient relies on backpropagation instead of likelihood ratio methods. If a differentiable environment model is available, one can link together the policy, model, and reward function to compute an analytic policy gradient by backpropagation of reward along a trajectory. Instead of using entire trajectories, one can estimate future rewards using a learned value function (a critic) and compute policy gradients from subsequences of trajectories. It is also possible to backpropagate analytic action derivatives from a Q-function to compute the policy gradient without a model. Following Fairbank, we refer to methods that compute the policy gradient through backpropagation as *value gradient* methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we address two limitations of prior value gradient algorithms. The first is that, in contrast to likelihood ratio methods, value gradient algorithms are only suitable for training deterministic policies. Stochastic policies have several advantages: for example, they can be beneficial for partially observed problems; they permit on-policy exploration; and because stochastic policies can assign probability mass to off-policy trajectories, we can train a stochastic policy on samples from an experience database in a principled manner. When an environment model is used, value gradient algorithms have also been critically limited to operation in deterministic environments. By exploiting a mathematical tool known as "re-parameterization" that has found recent use for generative models, we extend the scope of value gradient algorithms to include the optimization of stochastic policies in stochastic environments. We thus describe our framework as *Stochastic Value Gradient* (SVG) methods. Secondly, we show that an environment dynamics model, value function, and policy can be learned jointly with neural networks based only on environment interaction.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learned dynamics models are often inaccurate, which we mitigate by computing value gradients along real system trajectories instead of planned ones, a feature shared by model-free methods. This substantially reduces the impact of model error because we only use models to compute policy gradients, not for prediction, combining advantages of model-based and model-free methods with fewer of their drawbacks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present several algorithms that range from model-based to model-free methods, flexibly combining models of environment dynamics with value functions to optimize policies in stochastic or deterministic environments. Experimentally, we demonstrate that SVG methods can be applied using generic neural networks with tens of thousands of parameters while making minimal assumptions about plants or environments. By examining a simple stochastic control problem, we show that SVG algorithms can optimize policies where model-based planning and likelihood ratio methods cannot. We provide evidence that value function approximation can compensate for degraded models, demonstrating the increased robustness of SVG methods over model-based planning. Finally, we use SVG algorithms to solve a variety of challenging, under-actuated, physical control problems, including swimming of snakes, reaching, tracking, and grabbing with a robot arm, fall-recovery for a monoped, and locomotion for a planar cheetah and biped.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Deterministic value gradients", "weight": 1.0} -->

The deterministic Bellman equation takes the form ${V{(\mathbf{s})}} = {{r{(\mathbf{s},\mathbf{a})}} + {\gammaV'{({\mathbf{f}{(\mathbf{s},\mathbf{a})}})}}}$ for a deterministic model $\mathbf{s}' = {\mathbf{f}{(\mathbf{s},\mathbf{a})}}$ and deterministic policy $\mathbf{a} = {\pi{(\mathbf{s};\theta)}}$. Differentiating the equation with respect to the state and policy yields an expression for the value gradient In eq. 4, the term $\gammaV_{\theta}'$ arises because the total derivative includes policy gradient contributions from subsequent time steps (full derivation in Appendix A).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Deterministic value gradients", "weight": 1.0} -->

For a purely model-based formalism, these equations are used as a pair of coupled recursions that, starting from the termination of a trajectory, proceed backward in time to compute the gradient of the value function with respect to the state and policy parameters. $V_{\theta}^{0}$ returns the total policy gradient. When a state-value function is used after one step in the recursion, ${r_{\mathbf{a}}\pi_{\theta}} + {\gammaV_{\mathbf{s}'}'\mathbf{f}_{\mathbf{a}}\pi_{\theta}}$ directly expresses the contribution of the current time step to the policy gradient. Summing these gradients over the trajectory gives the total policy gradient. When a Q-function is used, the per-time step contribution to the policy gradient takes the form $Q_{\mathbf{a}}\pi_{\theta}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Stochastic value gradients", "weight": 1.0} -->

One limitation of the gradient computation in eqs. 3 and 4 is that the model and policy must be deterministic. Additionally, the accuracy of the policy gradient $V_{\theta}$ is highly sensitive to modeling errors. We introduce two critical changes: First, in section 4.1, we transform the stochastic Bellman equation (eq. 2) to permit backpropagating value information in a stochastic setting. This also enables us to compute gradients along real trajectories, not ones sampled from a model, making the approach robust to model error, leading to our first algorithm "SVG($\infty$)," described in section 4.2 ‣ 4 Stochastic value gradients ‣ Learning Continuous Control Policies by Stochastic Value Gradients").

<!-- chunk {"id": "body-0011", "role": "body", "section": "Stochastic value gradients", "weight": 1.0} -->

Second, in section 4.3 and SVG ‣ 4 Stochastic value gradients ‣ Learning Continuous Control Policies by Stochastic Value Gradients"), we show how value function critics can be integrated into this framework, leading to the algorithms "SVG($1$)" and "SVG($0$)", which expand the Bellman recursion for 1 and 0 steps, respectively. Value functions further increase robustness to model error and extend our framework to infinite-horizon control.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Re-parameterization of distributions", "weight": 1.0} -->

Our goal is to backpropagate through the stochastic Bellman equation. To do so, we make use of a concept called "re-parameterization", which permits us to compute derivatives of deterministic and stochastic models in the same way. A very simple example of re-parameterization is to write a conditional Gaussian density ${p{(\left. y \middle| x \right.)}} = {\mathcal{N}{(\left. y \middle| {{\mu{(x)}},{\sigma^{2}{(x)}}} \right.)}}$ as the function $y = {{\mu{(x)}} + {\sigma{(x)}\xi}}$, where $\xi \sim {\mathcal{N}{}}$. From this point of view, one produces samples procedurally by first sampling $\xi$, then deterministically constructing $y$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Re-parameterization of distributions", "weight": 1.0} -->

Here, we consider conditional densities whose samples are generated by a deterministic function of an input noise variable and other conditioning variables: $\mathbf{y} = {\mathbf{f}{(\mathbf{x},\xi)}}$, where $\xi \sim {\rho{( \cdot )}}$, a fixed noise distribution. Rich density models can be expressed in this form. Expectations of a function $\mathbf{g}{(\mathbf{y})}$ become ${{\mathbb{E}}_{p{({\mathbf{y}|\mathbf{x}})}}\mathbf{g}{(\mathbf{y})}} = {\int{\mathbf{g}{({\mathbf{f}{(\mathbf{x},\xi)}})}\rho{(\xi)}{d\xi}}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Re-parameterization of distributions", "weight": 1.0} -->

The advantage of working with re-parameterized distributions is that we can now obtain a simple Monte-Carlo estimator of the derivative of an expectation with respect to $\mathbf{x}$: In contrast to likelihood ratio-based Monte Carlo estimators, ${{\nabla_{\mathbf{x}}\log}p}{(\left. \mathbf{y} \middle| \mathbf{x} \right.)}\mathbf{g}{(\mathbf{y})}$, this formula makes direct use of the Jacobian of $\mathbf{g}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Re-parameterization of the Bellman equation", "weight": 1.0} -->

We now re-parameterize the Bellman equation. When re-parameterized, the stochastic policy takes the form $\mathbf{a} = {\pi{(\mathbf{s},\eta;\theta)}}$, and the stochastic environment the form $\mathbf{s}' = {\mathbf{f}{(\mathbf{s},\mathbf{a},\xi)}}$ for noise variables $\eta \sim {\rho{(\eta)}}$ and $\xi \sim {\rho{(\xi)}}$, respectively. Inserting these functions into eq. yields Differentiating eq. 6 with respect to the current state $\mathbf{s}$ and policy parameters $\theta$ gives We are interested in controlling systems with *a priori* unknown dynamics. Consequently, in the following, we replace instances of $\mathbf{f}$ or its derivatives with a learned model $\hat{\mathbf{f}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Gradient evaluation by planning", "weight": 1.0} -->

A planning method to compute a gradient estimate is to compute a trajectory by running the policy in loop with a model while sampling the associated noise variables, yielding a trajectory $\tau = {(\mathbf{s}^{1},\eta^{1},\mathbf{a}^{1},\xi^{1},\mathbf{s}^{2},\eta^{2},\mathbf{a}^{2},\xi^{2},\ldots)}$. On this sampled trajectory, a Monte-Carlo estimate of the policy gradient can be computed by the backward recursions: where have written lower-case $v$ to emphasize that the quantities are one-sample estimates^33^3In the finite-horizon formulation, the gradient calculation starts at the end of the trajectory for which the only terms remaining in eq.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Gradient evaluation on real trajectories", "weight": 1.0} -->

An important advantage of stochastic over deterministic models is that they can assign probability mass to observations produced by the real environment. In a deterministic formulation, there is no principled way to account for mismatch between model predictions and observed trajectories. In this case, the policy and environment noise $(\eta,\xi)$ that produced the observed trajectory are considered unknown. By an application of Bayes' rule, which we explain in Appendix B, we can rewrite the expectations in equations 7 and 8 given the observations $(\mathbf{s},\mathbf{a},\mathbf{s}')$ as where we can now replace the two outer expectations with samples derived from interaction with the real environment.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Gradient evaluation on real trajectories", "weight": 1.0} -->

In the special case of additive noise, $\mathbf{s}' = {{\hat{\mathbf{f}}{(\mathbf{s},\mathbf{a})}} + \xi}$, it is possible to use a deterministic model to compute the derivatives $({\hat{\mathbf{f}}}_{\mathbf{s}},{\hat{\mathbf{f}}}_{\mathbf{a}})$. The noise's influence is restricted to the gradient of the value of the next state, $V_{\mathbf{s}'}'$, and does not affect the model Jacobian. If we consider it desirable to capture more complicated environment noise, we can use a re-parameterized generative model and infer the missing noise variables, possibly by sampling from $p{(\eta,\left. \xi \middle| {\mathbf{s},\mathbf{a},\mathbf{s}'} \right.)}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "SVG($\\infty$)", "weight": 1.0} -->

SVG($\infty$) computes value gradients by backward recursions on finite-horizon trajectories. After every episode, we train the model, $\hat{\mathbf{f}}$, followed by the policy, $\pi$. We provide pseudocode for this in Algorithm 1 ‣ 4 Stochastic value gradients ‣ Learning Continuous Control Policies by Stochastic Value Gradients") but discuss further implementation details in section 5 and in the experiments.

<!-- chunk {"id": "body-0020", "role": "body", "section": "SVG and SVG", "weight": 1.0} -->

In our framework, we may learn a parametric estimate of the expected value $\hat{V}{(\mathbf{s};\nu)}$ (critic) with parameters $\nu$. The derivative of the critic value with respect to the state, ${\hat{V}}_{\mathbf{s}}$, can be used in place of the sample gradient estimate given in eq.. The critic can reduce the variance of the gradient estimates because $\hat{V}$ approximates the expectation of future rewards while eq. provides only a single-trajectory estimate. Additionally, the value function can be used at the end of an episode to approximate the infinite-horizon policy gradient. Finally, eq. involves the repeated multiplication of Jacobians of the approximate model ${\hat{\mathbf{f}}}_{\mathbf{s}}$, ${\hat{\mathbf{f}}}_{\mathbf{a}}$. Just as model error can compound in forward planning, model gradient error can compound during backpropagation. Furthermore, SVG($\infty$) is on-policy.

<!-- chunk {"id": "body-0021", "role": "body", "section": "SVG and SVG", "weight": 1.0} -->

That is, after each episode, a single gradient-based update is made to the policy, and the policy optimization does not revisit those trajectory data again. To increase data-efficiency, we construct an off-policy, experience replay algorithm that uses models and value functions, SVG with Experience Replay (SVG-ER). This algorithm also has the advantage that it can perform an infinite-horizon computation.

<!-- chunk {"id": "body-0022", "role": "body", "section": "SVG and SVG", "weight": 1.0} -->

To construct an off-policy estimator, we perform importance-weighting of the current policy distribution with respect to a proposal distribution, $q{(\mathbf{s},\mathbf{a})}$: Specifically, we maintain a database with tuples of past state transitions $(\mathbf{s}^{k},\mathbf{a}^{k},r^{k},\mathbf{s}^{k + 1})$. Each proposal drawn from $q$ is a sample of a tuple from the database. At time $t$, the importance-weight $w \triangleq {p/q} = \frac{p{(\left. \mathbf{a}^{k} \middle| {\mathbf{s}^{k};\theta^{t}} \right.)}}{p{(\left.

<!-- chunk {"id": "body-0023", "role": "body", "section": "SVG and SVG", "weight": 1.0} -->

\mathbf{a}^{k} \middle| {\mathbf{s}^{k},\theta^{k}} \right.)}}$, where $\theta^{k}$ comprise the policy parameters in use at the historical time step $k$. We do not importance-weight the marginal distribution over states $q{(\mathbf{s})}$ generated by a policy; this is widely considered to be intractable.

<!-- chunk {"id": "body-0024", "role": "body", "section": "SVG and SVG", "weight": 1.0} -->

Similarly, we use experience replay for value function learning. Details can be found in Appendix C. Pseudocode for the SVG($1$) algorithm with Experience Replay is in Algorithm 2 ‣ 4 Stochastic value gradients ‣ Learning Continuous Control Policies by Stochastic Value Gradients").

<!-- chunk {"id": "body-0025", "role": "body", "section": "SVG and SVG", "weight": 1.0} -->

We also provide a model-free stochastic value gradient algorithm, SVG($0$) (Algorithm 3 in the Appendix). This algorithm is very similar to SVG($1$) and is the stochastic analogue of the recently introduced Deterministic Policy Gradient algorithm (DPG). Unlike DPG, instead of assuming a deterministic policy, SVG estimates the derivative around the policy noise ${\mathbb{E}}_{p{(\eta)}}\left\lbrack {Q_{\mathbf{a}}\pi_{\theta}} \middle| \eta \right\rbrack$.^44^4Note that $\pi$ is a function of the state and noise variable. This, for example, permits learning policy noise variance. The relative merit of SVG versus SVG depends on whether the model or value function is easier to learn and is task-dependent. We expect that model-based algorithms such as SVG($1$) will show the strongest advantages in multitask settings where the system dynamics are fixed, but the reward function is variable.

<!-- chunk {"id": "body-0026", "role": "body", "section": "SVG and SVG", "weight": 1.0} -->

SVG performed well across all experiments, including ones introducing capacity constraints on the value function and model. SVG-ER demonstrated a significant advantage over all other tested algorithms.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Model and value learning", "weight": 1.0} -->

We can use almost any kind of differentiable, generative model. In our work, we have parameterized the models as neural networks. Our framework supports nonlinear state- and action-dependent noise, notable properties of biological actuators. For example, this can be described by the parametric form ${\hat{\mathbf{f}}{(\mathbf{s},\mathbf{a},\xi)}} = {{\hat{\mu}{(\mathbf{s},\mathbf{a})}} + {\hat{\sigma}{(\mathbf{s},\mathbf{a})}\xi}}$. Model learning amounts to a purely supervised problem based on observed state transitions. Our model and policy training occur *jointly*. There is no "motor-babbling" period used to identify the model. As new transitions are observed, the model is trained first, followed by the value function (for SVG($1$)), followed by the policy.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Model and value learning", "weight": 1.0} -->

To ensure that the model does not forget information about state transitions, we maintain an experience database and cull batches of examples from the database for every model update. Additionally, we model the state-change by $\mathbf{s}' = {{\hat{\mathbf{f}}{(\mathbf{s},\mathbf{a},\xi)}} + \mathbf{s}}$ and have found that constructing models as separate sub-networks per predicted state dimension improved model quality significantly.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Model and value learning", "weight": 1.0} -->

Our framework also permits a variety of means to learn the value function models. We can use temporal difference learning or regression to empirical episode returns. Since SVG($1$) is model-based, we can also use Bellman residual minimization. In practice, we used a version of "fitted" policy evaluation. Pseudocode is available in Appendix C, Algorithm 4.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

We tested the SVG algorithms in two sets of experiments. In the first set of experiments (section 6.1), we test whether evaluating gradients on real environment trajectories and value function approximation can reduce the impact of model error. In our second set (section 6.2), we show that SVG can be applied to several complicated, multidimensional physics environments involving contact dynamics (Figure 1) in the MuJoCo simulator. Below we only briefly summarize the main properties of each environment: further details of the simulations can be found in Appendix D and supplement. In all cases, we use generic, 2 hidden-layer neural networks with tanh activation functions to represent models, value functions, and policies. A video montage is available at Figure 1: From left to right: 7-Link Swimmer; Reacher; Gripper; Monoped; Half-Cheetah; Walker

<!-- chunk {"id": "body-0031", "role": "body", "section": "Gradient evaluation on real trajectories vs. planning", "weight": 1.0} -->

To demonstrate the difficulty of planning with a stochastic model, we first present a very simple control problem for which SVG($\infty$) easily learns a control policy but for which an otherwise identical planner fails entirely. Our example is based on a problem due to. The policy directly controls the velocity of a point-mass "hand" on a 2D plane. By means of a spring-coupling, the hand exerts a force on a ball mass; the ball additionally experiences a gravitational force and random forces (Gaussian noise). The goal is to bring hand and ball into one of two randomly chosen target configurations with a relevant reward being provided only at the final time step.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Gradient evaluation on real trajectories vs. planning", "weight": 1.0} -->

With simulation time step $0.01s$, this demands controlling and backpropagating the distal reward along a trajectory of $1,000$ steps. Because this experiment has a non-stationary, time-dependent value function, this problem also favors model-based value gradients over methods using value functions. SVG($\infty$) easily learns this task, but the planner, which uses trajectories from the model, shows little improvement. The planner simulates trajectories using the learned stochastic model and backpropagates along those simulated trajectories (eqs. 9 and 10). The extremely long time-horizon lets prediction error accumulate and thus renders roll-outs highly inaccurate, leading to much worse final performance (c.f. Fig. 2, left).^55^5We also tested REINFORCE on this problem but achieved very poor results due to the long horizon.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Robustness to degraded models and value functions", "weight": 1.0} -->

We investigated the sensitivity of SVG($\infty$) and SVG to the quality of the learned model on Swimmer. Swimmer is a chain body with multiple links immersed in a fluid environment with drag forces that allow the body to propel itself. We build chains of 3, 5, or 7 links, corresponding to 10, 14, or 18-dimensional state spaces with 2, 4, or 6-dimensional action spaces. The body is initialized in random configurations with respect to a central goal location. Thus, to solve the task, the body must turn to re-orient and then produce an undulation to move to the goal.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Robustness to degraded models and value functions", "weight": 1.0} -->

To assess the impact of model quality, we learned to control a link-3 swimmer with SVG($\infty$) and SVG while varying the capacity of the network used to model the environment (5, 10, or 20 hidden units for each state dimension subnetwork (Appendix D); i.e., in this task we intentionally shrink the neural network model to investigate the sensitivity of our methods to model inaccuracy. While with a high capacity model (20 hidden units per state dimension), both SVG($\infty$) and SVG successfully learn to solve the task, the performance of SVG($\infty$) drops significantly as model capacity is reduced (c.f. Fig. 3, middle). SVG still works well for models with only 5 hidden units, and it also scales up to 5 and 7-link versions of the swimmer (Figs. 3, right and 4, left).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Robustness to degraded models and value functions", "weight": 1.0} -->

To compare SVG to conventional model-free approaches, we also tested a state-of-the-art actor-critic algorithm that learns a $V$-function and updates the policy using the TD-error $\delta = {{r + {\gammaV'}} - V}$ as an estimate of the advantage, yielding the policy gradient $v_{\theta} = {\delta{{\nabla_{\theta}\log}\pi}}$. (SVG and the AC algorithm used the same code for learning $V$.) SVG outperformed the model-free approach in the 3-, 5-, and 7-link swimmer tasks (c.f. Fig. 3, left, right; Fig. 4, top left). In figure panels 2, middle, 3, right, and 4, left column, we show that experience replay for the policy can improve the data efficiency and performance of SVG.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Robustness to degraded models and value functions", "weight": 1.0} -->

Similarly, we tested the impact of varying the capacity of the value function approximator (Fig. 2, right) on a cart-pole. The V-function-based SVG degrades less severely than the Q-function-based DPG presumably because it computes the policy gradient with the aid of the dynamics model.

<!-- chunk {"id": "body-0037", "role": "body", "section": "SVG in complex environments", "weight": 1.0} -->

In a second set of experiments we demonstrated that SVG-ER can be applied to several challenging physical control problems with stochastic, non-linear, and discontinuous dynamics due to contacts. Reacher is an arm stationed within a walled box with 6 state dimensions and 3 action dimensions and the $(x,y)$ coordinates of a target site, giving 8 state dimensions in total. In 4-Target Reacher, the site was randomly placed at one of the four corners of the box, and the arm in a random configuration at the beginning of each trial. In Moving-Target Reacher, the site moved at a randomized speed and heading in the box with reflections at the walls. Solving this latter problem implies that the policy has generalized over the entire work space. Gripper augments the reacher arm with a manipulator that can grab a ball in a randomized position and return it to a specified site. Monoped has 14 state dimensions, 4 action dimensions, and ground contact dynamics. The monoped begins falling from a height and must remain standing.

<!-- chunk {"id": "body-0038", "role": "body", "section": "SVG in complex environments", "weight": 1.0} -->

Additionally, we apply Gaussian random noise to the torques controlling the joints with a standard deviation of $5\%$ of the total possible actuator strength at all points in time, reducing the stability of upright postures. Half-Cheetah is a planar cat robot designed to run based on with 18 state dimensions and 6 action dimensions. Half-Cheetah has a version with springs to aid balanced standing and a version without them. Walker is a planar biped, based on the environment.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have shown that two potential problems with value gradient methods, their reliance on planning and restriction to deterministic models, can be exorcised, broadening their relevance to reinforcement learning. We have shown experimentally that the SVG framework can train neural network policies in a robust manner to solve interesting continuous control problems. The framework includes algorithm variants beyond the ones tested in this paper, for example, ones that combine a value function with $k$ steps of back-propagation through a model (SVG(k)). Augmenting SVG with experience replay led to the best results, and a similar extension could be applied to any SVG(k). Furthermore, we did not harness sophisticated generative models of stochastic dynamics, but one could readily do so, presenting great room for growth.
