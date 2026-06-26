<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Convergence of Flow-Policy Gradient Learning for Linear Quadratic Regulator Problems

Topics include Policy gradients, Offline algorithms, Learning, Linear quadratic regulator.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Flow Q-learning has recently been introduced to integrate learning from expert demonstrations into an actor-critic structure. Central to this innovation is the ``the one-step policy'' network, which is optimized through a Q-function that is regularized with the behavioral cloning from expert trajectories, allowing learning more expressive policies using flow-based generative models. In this paper, we studied the convergence property and stabilizablity of the one-step policy during learning for linear quadratic problems under the offline settings. Our theoretical results are based on a new formulation of the one-step policy loss based on the average expected cost, and regularized with the behavioral cloning loss. Such a formulation allows us to tap into existing strong theoretical results from the policy gradient theorem to study the convergence properties of the one-step policy. We verify our theoretical finding with simulation results on a linearized inverted pendulum.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Actor-critic methods are widely used in Reinforcement Learning (RL) and have been successfully applied in various domains, including robotics, game playing, and autonomous systems. Actor-Critic structures are particularly interesting due to their ability to handle continuous state and action spaces and combining the pros of Temporal Difference (TD) learning and Policy Gradient (PG) methods. In these structures, the actor is responsible for selecting actions using an actor network, while the critic evaluates the actions taken by the actor by estimating the value function or action-value function ( Q -function). This separation of roles is particularly efficient for control problems which typically have continuous action spaces as actor-critic methods directly learn a parameterized policy and as such avoid the need for computationally expensive value function optimization in TD approaches. Despite their success, actor-critic methods face several challenges, including stability and convergence issues when applied to closed-loop dynamical systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In many RL problems, expert trajectories are available, which can be leveraged to improve learning efficiency and performance. This can be done through imitation learning techniques, such as behavioral cloning or inverse reinforcement learning, typically in offline RL setups which allows training effective policies from pre-collected datasets without further environment interactions. However, as datasets have grown larger, the distribution of the expert trajectories get more complicated, making it more challenging to learn effective policies using purely offline methods. Flow Q -learning is a recent actorcritic approach that integrates learning from expert trajectories into the RL framework and allows

<!-- chunk {"id": "body-0005", "role": "body", "section": "ADIB YAGHMAIE ∗ NAHA ∗", "weight": 1.0} -->

learning more expressive policies using flow-based generative models. Flow Q -learning uses normalizing flows to model the policy distribution, allowing for more expressive and flexible policies, and a better exploration.

<!-- chunk {"id": "body-0006", "role": "body", "section": "ADIB YAGHMAIE ∗ NAHA ∗", "weight": 1.0} -->

Integrating learning from expert demonstration with RL is particularly useful in control problems where the model of the system is not known or is inaccurate. In such scenarios, expert trajectories can provide valuable information about the system dynamics and help guide the learning process. For instance, in robotics, expert demonstrations can be used to teach robots how to perform complex tasks, such as grasping objects or navigating through environments. In autonomous driving, expert trajectories can be used to train self-driving cars to navigate safely and efficiently in complex traffic scenarios. Even though imitation learning from expert demonstrations, such as flow Q-learning, has shown promising empirical results in various control problems, the convergence and stability properties of such methods for closed-loop dynamical systems have not been well studied.

<!-- chunk {"id": "body-0007", "role": "body", "section": "ADIB YAGHMAIE ∗ NAHA ∗", "weight": 1.0} -->

In this paper, we study the theoretical properties of a behavioral cloning-based algorithm inspired by the flow Q -learning in the context of Linear Quadratic Regulator (LQR) control problems. We focus on the convergence and stability properties of the one-step policy that optimizes the average expected cost, regularized via behavioral cloning from expert trajectories. Formulating based on the average expected cost rather than the Q function, which was originally used, allows us to apply the policy gradient framework to analyze the convergence of the one-step policy. Furthermore, In flow Q-learning, evaluating the gradient of the Q-function with respect to the policy parameters can be challenging in practice (D'Oro and Ja´ skowski ). Common obstacles include biased estimates, high variance, and the fact that the Q-function may be non-differentiable with respect to the policy parameters. Our formulation avoids these issues by directly using the policy gradient framework. Note that the established results are different from as the behavioral cloning is absent.

<!-- chunk {"id": "body-0008", "role": "body", "section": "ADIB YAGHMAIE ∗ NAHA ∗", "weight": 1.0} -->

The contribution of this paper is as follows. For the LQR problem, we prove that the one-step policy learned via optimizing the average expected cost regularized with behavioral cloning from expert trajectories converges to the optimal policy at a linear rate. This is achieved by showing that the one-step policy loss is gradient dominant. We also prove that the one-step policy remains stabilizing during the course of learning. Our formulation of the one-step loss based on the average expected cost instead of Q function which is originally used in is of independent interest as it allows us to use the policy gradient framework, beyond the LQR problem studied in this paper.

<!-- chunk {"id": "body-0009", "role": "body", "section": "ADIB YAGHMAIE ∗ NAHA ∗", "weight": 1.0} -->

The organization of this paper is as follows. In Section 2, we give the notation and background on the flow Q -learning and in Section 3, we define the LQR problem. In Section 4, we discuss the flow Q -learning algorithm for the LQR problem and establish convergence and stability. In Section 5, we give the simulation results of implementing the flow-policy gradient algorithm on a linearized inverted pendulum and in Section 6, we conclude the paper. The longer proofs of helper lemmas are given in Appendix A.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Flow Q -learning", "weight": 1.0} -->

Flow Q -learning uses actor-critic structure where a critic network Q φ c, a behavioral cloning policy π φ b and a one-step policy π φ o with parameters φ c, φ a, φ o, respectively, are trained. Initially, the data points (x, u, x ′, c) from some expert's demonstrations are recorded in a replay buffer D. The flow Q -learning can be implemented fully offline; i.e. learning from the replay buffer D or in an offline-online setup where data from online interaction is continuously added to the replay buffer. In the following, we give the loss functions for training the networks in the flow Q -learning algorithm The critic network Q φ c: This is trained using the critic loss where ¯ φ c denotes the parameters of the target critic network.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Flow Q -learning", "weight": 1.0} -->

The behavioral cloning (BC) policy µ φ b: This is trained via flow matching. Let v φ b denotes the velocity function in flow matching trained using the BC flow matching loss Here, a t = (1 -t) a 0 + ta 1. Then, the behavioral cloning policy µ φ b is given by µ φ b (x, z) = v φ b (1, x, z). Intuitively, the behavioral cloning policy µ φ b maps the noise z, sampled from the standard normal distribution to the action a via an ODE with velocity v φ b (t, x, z).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Flow Q -learning", "weight": 1.0} -->

The one-step policy µ φ o: This is trained with the following loss where α > 0 is the regularization parameter. Due to the presence of the both behavioral cloning and one-step policy, the established results on the convergence of the actor-critic structures are not applicable.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Linear Quadratic Problem", "weight": 1.0} -->

This section gives the preliminary results on the LQR problem. We consider the following fully observable linear time-invariant system with unknown parameters θ ∈ R d θ, where x k ∈ R n, u k ∈ R m are state and control input and w k ∈ R n ∼ N (0, W w). We assume that the dynamics θ = (A,B) are unknown. The stage cost for the linear dynamical system in is considered to be quadratic as follows, where R x ≥ 0 and R u > 0. For linear systems and quadratic costs, we are interested in learning a linear state feedback controller with the gain K ∈ K, where K is the feasible set of the stabilizing controller gains, i.e., K = { K ∈ R m × n | ρ (A + BK) < 1 }. In other words, we consider the following structure of the policy function, π = Kx + z k, z k ∼ N (0, W z), K ∈ K. When the dynamics are unknown, it is common to add noise to the linear state feedback controller to promote exploration.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Linear Quadratic Problem", "weight": 1.0} -->

Note that the policy π is analogous to the one-step policy µ φ o from the flow Q-learning. Finally, the average expected cost associated with the policy π is given as Optimizing for the linear dynamical system in defines an LQR problem.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Linear Quadratic Problem", "weight": 1.0} -->

Steady state covariance of the state variable: We assume that the initial state for the linear dynamical system in is zero x 0 = 0. Note that we can assume this without loss of generality as the effect of the nonzero initial state vanishes in the landscape of the average cost. The next lemma shows that the covariance of the state variable x k under the policy π = Kx k + z k converges to a steady state value.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Linear Quadratic Problem", "weight": 1.0} -->

Lemma 1 Consider the linear system in and assume that the controller gain K ∈ K, where K = { K ∈ R m × n | ρ (A + BK) < 1 }. Then, the covariance of the state variable x k under the policy π = Kx k + z k converges to a steady state value Proof Assume K is stabilizing. Then, x k ∼ N (0, Σ k) where Σ k denote the covariance of the state x k for the linear system under policy π = Kx k + z k at time k. The covariance Σ k +1 is given by As a result, one gets Since (A + BK) is stable, the solution to can be written as The stationary covariance Σ is given by replacing both Σ k +1 and Σ k in with Σ.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Linear Quadratic Problem", "weight": 1.0} -->

Average expected cost: Assume that K ∈ K, where K = { K ∈ R m × n | ρ (A + BK) < 1 }. Then there exists a unique positive definite solution P the following Bellman equation The average expected cost associated with the policy π = Kx k + z k, z k ∼ N (0, W z) is derived next.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Linear Quadratic Problem", "weight": 1.0} -->

Lemma 2 Consider the linear system in with the quadratic cost in and the average expected cost. The average expected cost J (π) associated with the policy π = Kx + z, z ∼ N (0, W z), K ∈ K, where K = { K ∈ R m × n | ρ (A + BK) < 1 } is given by where Σ and P are given in and.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Linear Quadratic Problem", "weight": 1.0} -->

Proof We derive the average cost by directly using the policy π = Kx + z in the average cost Using E x ∼ ρ K z ∼N (0,W z) [x ⊤ k z k] = 0, Tr(AB) = Tr(BA), one gets By ergodicity and using the stationary state distribution E x ∼ ρ K [x k x T k] = Σ, one gets By replacing R x + K ⊤ R u K, the average cost can equivalently written as.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Flow-Policy Gradient Learning", "weight": 1.0} -->

In this paper, we primarily use the steps from the flowQ learning algorithm discussed in Subsection 2.2 with a very useful modification that we learn the one step policy by optimizing the average expected cost regularized with the behavior cloning loss as The formulation in allows us to see learning the one-step policy as a policy gradient problem. The parameters of the one-step policy; i.e. φ o are updated by gradient descent over l φ o

<!-- chunk {"id": "body-0021", "role": "body", "section": "Flow-policy Gradient for LQR problem", "weight": 1.0} -->

In this subsection, we study the flow-policy gradient algorithm for the LQR problem. We first give the structure for the Q -function and one-step policy and then we study the converge of the parameters of the one step policy. We also theoretically prove that the one-step policy remain stabilizing during the course of learning.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Q -FUNCTION AND ONE-STEP POLICY STRUCTURE", "weight": 1.0} -->

For the linear system in with the quadratic cost in and the average cost formulation, the one-step policy is considered as µ K (x) = Kx + z, z ∼ N (0, W z) and the Q φ c function is given by where J (µ K) is the average expected cost associated with the one-step policy, which is given in and K is the controller gain to be optimized.

<!-- chunk {"id": "body-0023", "role": "body", "section": "ONE-STEP LOSS", "weight": 1.0} -->

The one-step policy loss function for the LQR problem is given as The controller gain K is updated via gradient descent over l lin φ o The loss l φ o is coercive: One can easily verify that l lin φ o (K) is coercive as l lin φ o (K) is quadratic in µ K and µ K is linear in K; i.e. µ K (x) = Kx + z.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Convergence and stabilizability of the one-step policy", "weight": 1.0} -->

As discussed in Fazel et al., optimizing the average cost J ( µ K ) for the LQR problem via gradient descent over the policy gain K is a non-convex problem. This also holds for the one-step loss l lin φ o in as it contains J ( µ K ) along with the the behavioral cloning loss. In this subsection we study the convergence by showing that l lin φ o in is gradient dominant. The stabilizability of the updated controller is also established in this subsection.

<!-- chunk {"id": "body-0025", "role": "body", "section": "CONVERGENCE", "weight": 1.0} -->

To prove that l lin φ o is gradient dominant, several helper lemmas are given below with the proofs in the appendices A.1-A.2. The proof of the Theorem 1 is also given in the appendix A.3.

<!-- chunk {"id": "body-0026", "role": "body", "section": "CONVERGENCE", "weight": 1.0} -->

Lemma 3 The gradient of the one-step policy loss l lin φ o is given by where K ∗ is the optimal gain ∇ K l lin φ o (K ∗) = 0.

<!-- chunk {"id": "body-0027", "role": "body", "section": "CONVERGENCE", "weight": 1.0} -->

Lemma 4 The one-step policy loss l lin φ o is L -smooth where L is given by Using Lemmas 3-4, one can show that l lin φ o is gradient dominant.

<!-- chunk {"id": "body-0028", "role": "body", "section": "CONVERGENCE", "weight": 1.0} -->

Theorem 1 The one-step policy loss l lin φ o is gradient dominant, i.e.,

<!-- chunk {"id": "body-0029", "role": "body", "section": "STABILIZABILITY", "weight": 1.0} -->

The stabilizability of the one-step policy is guaranteed by the following theorem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "STABILIZABILITY", "weight": 1.0} -->

Theorem 2 Assume that K 0 ∈ K, where K = { K ∈ R m × n | ρ (A + BK) < 1 }. Then for any α > 0, the one-step policy µ φ o learned via the gradient descent in with a step size η < 2 L is stabilizing. In addition, the convergence rate is linear Proof Since l lin φ o is coercive and L -smooth with constant L (Lemma 4), the controller gain learned via the gradient descent in with a step size η < 2 L is stabilizing; i.e. K t +1 ∈ K. The linear convergence rate follows from Hu et al. [Theorem 1.4].

<!-- chunk {"id": "body-0031", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

For the simulation studies, we considered a linearized inverted pendulum system as a benchmark example. Here the states are the angle and angular velocity of the pendulum, i.e., x k = [θ k, ˙ θ k] ⊤, and the angular velocity is clipped to | ˙ θ k | ≤ 8 rad/s. The control input u k corresponds to the applied torque and is bounded by | u k | ≤ 2 Nm. The noise variance is taken as W w = 0. 0001 I. The system is linearized around the upright position. For the cost evaluation, we use R x = diag (1, 0. 1) and R u = 0. 001. Furthermore, the system matrices are given by where m is the mass, l the rod length, b the viscous damping coefficient, g the gravitational constant, and ∆ t the sampling interval. We have used m = 1, l = l, b = 0, g = 10, and ∆ t = 0. 05 for the simulation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

To mimic the scenario of learning from an expert's demonstrations, we employ the linearized pendulum model controlled by a reasonably good controller, whose internal mechanism is assumed to be unknown. The resulting state-action trajectories are stored in a replay buffer D. In particular, we generate this dataset using a standard scenario-based MPC scheme from Schildbach et al. with a prediction horizon of N = 20 and 20 sampled scenarios. Here, the scenarios are obtained by drawing realisations of the process noise. In the flow-Policy gradient algorithm, we utilize the offline setting; i.e. we assume no interaction with the true system, and the algorithm relies solely on the stored data in D to learn the optimal controller K ∗.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Training and evaluation protocol: We consider the critic to be a linear function of the quadratic state-action features and is trained using the SGD optimiser from the PyTorch package with a learning rate of 10 -3 and batch size 256. A soft target update is applied with τ = 0. 005, and the target network is updated every 10 steps. The behavioral cloning (flow) policy is a four-layer network with as hidden dimensions, trained with a learning rate of 10 -3 and 10 fl ow-matching steps. The one-step actor policy is a linear state-feedback policy with additive Gaussian noise, i.e., z ∼ N (0, W z ) with W z = 0. 01 I. It is trained using a learning rate of 0. 1 and batch size 256, with behavioral cloning regularization weight α = 0. 10.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Training is performed for 100 epochs, and performance is evaluated after each epoch over 50 rollouts initialized from random states within [ -π, π ].

<!-- chunk {"id": "body-0035", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We compare the proposed method against two model-based baselines, the optimal LQR and scenario-based MPC in Fig. 3. This figure compares the sum of episodic costs for the proposed method, MPC, and LQR. Here, each episode consists of 200 time-steps. We observe that the proposed method, after convergence, slightly outperforms the MPC baseline and performs close to the optimal LQR controller. Note that, both the MPC and LQR baselines have access to the true system dynamics, while the proposed method learns solely from the offline dataset. The performance of the LQR suffers due to the fact that the inverted pendulum system is only approximately linear around the upright position, and the system is randomly initialized in [ -π, π ] for each rollout.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this paper, we have studied a behavioral cloning-based AC method, i.e., the flowQ learning algorithm, and proposed to use average expected cost regularized with behavioral cloning loss to learn the one-step policy. Formulating the one-step policy learning as a policy gradient problem allowed us to theoretically study the convergence and stabilizability of the one-step policy in the context of linear quadratic problems under the offline settings. We proved that the one-step policy loss is gradient-dominated and smooth, thereby stabilizing the learned one-step policy during learning when the learning rate is appropriately selected. In our future work, we plan to extend our convergence analysis to the complete AC algorithm, which means analyzing the convergence of both the Q -function and one-step policy together. Furthermore, we also aim to investigate ways to extend our theoretical results to nonlinear systems and the federated learning setup.
