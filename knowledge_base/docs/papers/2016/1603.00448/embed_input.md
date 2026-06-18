<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Guided Cost Learning: Deep Inverse Optimal Control via Policy Optimization

Topics include Reinforcement learning, Optimal control, Robotics, Neural networks, Online algorithms, Optimization, Control, Learning, IOC.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reinforcement learning can acquire complex behaviors from high-level specifications. However, defining a cost function that can be optimized effectively and encodes the correct task is challenging in practice. We explore how inverse optimal control (IOC) can be used to learn behaviors from demonstrations, with applications to torque control of high-dimensional robotic systems. Our method addresses two key challenges in inverse optimal control: first, the need for informative features and effective regularization to impose structure on the cost, and second, the difficulty of learning the cost function under unknown dynamics for high-dimensional continuous systems. To address the former challenge, we present an algorithm capable of learning arbitrary nonlinear cost functions, such as neural networks, without meticulous feature engineering. To address the latter challenge, we formulate an efficient sample-based approximation for MaxEnt IOC. We evaluate our method on a series of simulated tasks and real-world robotic manipulation problems, demonstrating substantial improvement over prior methods both in terms of task complexity and sample efficiency.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning can be used to acquire complex behaviors from high-level specifications. However, defining a cost function that can be optimized effectively and encodes the correct task can be challenging in practice, and techniques like cost shaping are often used to solve complex real-world problems. Inverse optimal control (IOC) or inverse reinforcement learning (IRL) provide an avenue for addressing this challenge by learning a cost function directly from expert demonstrations, e.g. Ng et al.; Abbeel & Ng; Ziebart et al.. However, designing an effective IOC algorithm for learning from demonstration is difficult for two reasons. First, IOC is fundamentally underdefined in that many costs induce the same behavior. Most practical algorithms therefore require carefully designed features to impose structure on the learned cost. Second, many standard IRL and IOC methods require solving the forward problem (finding an optimal policy given the current cost) in the inner loop of an iterative cost optimization. This makes them difficult to apply to complex, high-dimensional systems, where the forward problem is itself exceedingly difficult, particularly real-world robotic systems with unknown dynamics.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address the challenge of representation, we propose to use expressive, nonlinear function approximators, such as neural networks, to represent the cost. This reduces the engineering burden required to deploy IOC methods, and makes it possible to learn cost functions for which expert intuition is insufficient for designing good features. Such expressive function approximators, however, can learn complex cost functions that lack the structure typically imposed by hand-designed features. To mitigate this challenge, we propose two regularization techniques for IOC, one which is general and one which is specific to episodic domains, such as to robotic manipulation skills.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to learn cost functions for real-world robotic tasks, our method must be able to handle unknown dynamics and high-dimensional systems. To that end, we propose a cost learning algorithm based on policy optimization with local linear models, building on prior work in reinforcement learning. In this approach, as illustrated in Figure 1, the cost function is learned in the inner loop of a policy search procedure, using samples collected for policy improvement to also update the cost function. The cost learning method itself is a nonlinear generalization of maximum entropy IOC, with samples used to approximate the partition function. In contrast to previous work that optimizes the policy in the inner loop of cost learning, our approach instead updates the cost in the inner loop of policy search, making it practical and efficient. One of the benefits of this approach is that we can couple learning the cost with learning the policy for that cost. For tasks that are too complex to acquire a good global cost function from a small number of demonstrations, our method can still recover effective behaviors by running our policy learning method and retaining the learned policy. We elaborate on this further in Section 4.4.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contribution of our work is an algorithm that learns nonlinear cost functions from user demonstrations, at the same time as learning a policy to perform the task. Since the policy optimization "guides" the cost toward good regions of the space, we call this method guided cost learning. Unlike prior methods, our algorithm can handle complex, nonlinear cost function representations and high-dimensional unknown dynamics, and can be used on real physical systems with a modest number of samples. Our evaluation demonstrates the performance of our method on a set of simulated benchmark tasks, showing that it outperforms previous methods. We also evaluate our method on two real-world tasks learned directly from human demonstrations. These tasks require using torque control and vision to perform a variety of robotic manipulation behaviors, without any hand-specified cost features.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Guided Cost Learning", "weight": 1.0} -->

In this section, we describe the guided cost learning algorithm, which combines sample-based maximum entropy IOC with forward reinforcement learning using time-varying linear models. The central idea behind this method is to adapt the sampling distribution to match the maximum entropy cost distribution ${p{(\tau)}} = {\frac{1}{Z}{\exp{({- {c_{\theta}{(\tau)}}})}}}$, by directly optimizing a trajectory distribution with respect to the current cost $c_{\theta}{(\tau)}$ using a sample-efficient reinforcement learning algorithm. Samples generated on the physical system are used both to improve the policy and more accurately estimate the partition function $Z$. In this way, the reinforcement learning step acts to "guide" the sampling distribution toward regions where the samples are more useful for estimating the partition function. We will first describe how the IOC objective in Equation can be estimated with samples, and then describe how reinforcement learning can adapt the sampling distribution.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Sample-Based Inverse Optimal Control", "weight": 1.0} -->

In the sample-based approach to maximum entropy IOC, the partition function $Z = {\int{{\exp{({- {c_{\theta}{(\tau)}}})}}{d\tau}}}$ is estimated with samples from a background distribution $q{(\tau)}$. Prior sample-based IOC methods use a linear representation of the cost function, which simplifies the corresponding cost learning problem. In this section, we instead derive a sample-based approximation for the IOC objective for a general nonlinear parameterization of the cost function.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Sample-Based Inverse Optimal Control", "weight": 1.0} -->

where $\mathcal{D}_{\text{demo}}$ denotes the set of $N$ demonstrated trajectories, $\mathcal{D}_{\text{samp}}$ the set of $M$ background samples, and $q$ denotes the background distribution from which trajectories $\tau_{j}$ were sampled. Prior methods have chosen $q$ to be uniform or to lie in the vicinity of the demonstrations. To compute the gradients of this objective with respect to the cost parameters $\theta$, let $w_{j} = \frac{\exp{({- {c_{\theta}{(\tau_{j})}}})}}{q{(\tau_{j})}}$ and $Z = {\sum_{j}w_{j}}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Sample-Based Inverse Optimal Control", "weight": 1.0} -->

When the cost is represented by a neural network or some other function approximator, this gradient can be computed efficiently by backpropagating $- \frac{w_{j}}{Z}$ for each trajectory $\tau_{j} \in \mathcal{D}_{\text{samp}}$ and $\frac{1}{N}$ for each trajectory $\tau_{i} \in \mathcal{D}_{\text{demo}}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Adaptive Sampling via Policy Optimization", "weight": 1.0} -->

The choice of background sample distribution $q{(\tau)}$ for estimating the objective $\mathcal{L}_{\text{IOC}}$ is critical for successfully applying the sample-based IOC algorithm. The optimal importance sampling distribution for estimating the partition function $\int{{\exp{({- {c_{\theta}{(\tau)}}})}}{d\tau}}$ is ${q{(\tau)}} \propto {|{\exp{({- {c_{\theta}{(\tau)}}})}}|} = {\exp{({- {c_{\theta}{(\tau)}}})}}$. Designing a single background distribution $q{(\tau)}$ is therefore quite difficult when the cost $c_{\theta}$ is unknown. Instead, we can adaptively refine $q{(\tau)}$ to generate more samples in those regions of the trajectory space that are good according to the current cost function $c_{\theta}{(\tau)}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Adaptive Sampling via Policy Optimization", "weight": 1.0} -->

To this end, we interleave the IOC optimization, which attempts to find the cost function that maximizes the likelihood of the demonstrations, with a policy optimization procedure, which improves the trajectory distribution $q{(\tau)}$ with respect to the current cost.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Adaptive Sampling via Policy Optimization", "weight": 1.0} -->

Since one of the main advantages of the sample-based IOC approach is the ability to handle unknown dynamics, we must also choose a policy optimization procedure that can handle unknown dynamics. To this end, we adapt the method presented by Levine & Abbeel, which performs policy optimization under unknown dynamics by iteratively fitting time-varying linear dynamics to samples from the current trajectory distribution $q{(\tau)}$, updating the trajectory distribution using a modified LQR backward pass, and generating more samples for the next iteration. The trajectory distributions generated by this method are Gaussian, and each iteration of the policy optimization procedure satisfies a KL-divergence constraint of the form ${D_{\text{KL}}{({{q{(\tau)}} \parallel {\hat{q}{(\tau)}}})}} \leq \epsilon$, which prevents the policy from changing too rapidly. This has the additional benefit of not overfitting to poor initial estimates of the cost function.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Adaptive Sampling via Policy Optimization", "weight": 1.0} -->

With a small modification, we can use this algorithm to optimize a maximum entropy version of the objective, given by ${{\min_{q}E_{q}}{\lbrack{c_{\theta}{(\tau)}}\rbrack}} - {\mathcal{H}{(\tau)}}$, as discussed in prior work. This variant of the algorithm allows us to recover the trajectory distribution ${q{(\tau)}} \propto {\exp{({- {c_{\theta}{(\tau)}}})}}$ at convergence, a good distribution for sampling. For completeness, this policy optimization procedure is summarized in Appendix A.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Adaptive Sampling via Policy Optimization", "weight": 1.0} -->

1: Initialize qk (τ) as either a random initial controller or from demonstrations
3: Generate samples 𝒟traj from qk (τ)
4: Append samples: 𝒟samp ← 𝒟samp ∪ 𝒟traj
5: Use 𝒟samp to update cost cθ using Algorithm 2
6: Update qk (τ) using 𝒟traj and the method from to obtain qk + 1 (τ)
8: return optimized cost parameters θ and trajectory distribution q (τ)
Algorithm 1 Guided cost learning

<!-- chunk {"id": "body-0016", "role": "body", "section": "Adaptive Sampling via Policy Optimization", "weight": 1.0} -->

Our sample-based IOC algorithm with adaptive sampling is summarized in Algorithm 1. We call this method guided cost learning because policy optimization is used to guide sampling toward regions with lower cost. The algorithm consists of taking successive policy optimization steps, each of which generates samples $\mathcal{D}_{\text{traj}}$ from the latest trajectory distribution $q_{k}{(\tau)}$. After sampling, the cost function is updated using all samples collected thus far for the purpose of policy optimization. No additional background samples are required for this method. This procedure returns both a learned cost function $c_{\theta}{(\mathbf{x}_{t},\mathbf{u}_{t})}$ and a trajectory distribution $q{(\tau)}$, which corresponds to a time-varying linear-Gaussian controller $q{(\left. \mathbf{u}_{t} \middle| \mathbf{x}_{t} \right.)}$. This controller can be used to execute the learned behavior.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Cost Optimization and Importance Weights", "weight": 1.0} -->

The IOC objective can be optimized using standard nonlinear optimization methods and the gradient $\frac{d\mathcal{L}_{\text{IOC}}}{d\theta}$. Stochastic gradient methods are often preferred for high-dimensional function approximators, such as the neural networks. Such methods are straightforward to apply to objectives that factorize over the training samples, but the partition function does not factorize trivially in this way. Nonetheless, we found that our objective could still be optimized with stochastic gradient methods by sampling a subset of the demonstrations and background samples at each iteration. When the number of samples in the batch is small, we found it necessary to add the sampled demonstrations to the background sample set as well; without adding the demonstrations to the sample set, the objective can become unbounded and frequently does in practice. The stochastic optimization procedure is presented in Algorithm 2, and is straightforward to implement with most neural network libraries based on backpropagation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Cost Optimization and Importance Weights", "weight": 1.0} -->

Estimating the partition function requires us to use importance sampling. Although prior work has suggested dropping the importance weights, we show in Appendix B that this produces an inconsistent likelihood estimate and fails to recover good cost functions. Since our samples are drawn from multiple distributions, we compute a fusion distribution to evaluate the importance weights. Specifically, if we have samples from $k$ distributions ${q_{1}{(\tau)}},\ldots,{q_{\kappa}{(\tau)}}$, we can construct a consistent estimator of the expectation of a function $f{(\tau)}$ under a uniform distribution as ${E{\lbrack{f{(\tau)}}\rbrack}} \approx {\frac{1}{M}{\sum_{\tau_{j}}{\frac{1}{\frac{1}{k}{\sum_{\kappa}{q_{\kappa}{(\tau_{j})}}}}f{(\tau_{j})}}}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Cost Optimization and Importance Weights", "weight": 1.0} -->

The distributions $q_{\kappa}$ underlying background samples are obtained from the controller at iteration $k$. We must also append the demonstrations to the samples in Algorithm 2, yet the distribution that generated the demonstrations is unknown. To estimate it, we assume the demonstrations come from a single Gaussian trajectory distribution and compute its empirical mean and variance. We found this approximation sufficiently accurate for estimating the importance weights of the demonstrations, as shown in Appendix B.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Learning Costs and Controllers", "weight": 1.0} -->

In contrast to many previous IOC and IRL methods, our approach can be used to learn a cost while simultaneously optimizing the policy for a new instance of the task not in the demos, such as a new position of a target cup for a pouring task, as shown in our experiments. Since the algorithm produces both a cost function $c_{\theta}{(\mathbf{x}_{t},\mathbf{u}_{t})}$ and a controller $q{(\left. \mathbf{u}_{t} \middle| \mathbf{x}_{t} \right.)}$ that optimizes this cost on the new task instance, we can directly use this controller to execute the desired behavior. In this way, the method actually learns a policy from demonstration, using the additional knowledge that the demonstrations are near-optimal under some unknown cost function, similar to recent work on IOC by direct loss minimization.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Learning Costs and Controllers", "weight": 1.0} -->

The learned cost function $c_{\theta}{(\mathbf{x}_{t},\mathbf{u}_{t})}$ can often also be used to optimize new policies for new instances of the task without additional cost learning. However, we found that on the most challenging tasks we tested, running policy learning with IOC in the loop for each new task instance typically succeeded more frequently than running IOC once and reusing the learned cost. We hypothesize that this is because training the policy on a new instance of the task provides the algorithm with additional information about task variation, thus producing a better cost function and reducing overfitting. The intuition behind this hypothesis is that the demonstrations only cover a small portion of the degrees of variation in the task. Observing samples from a new task instance provides the algorithm with a better idea of the particular factors that distinguish successful task executions from failures.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Representation and Regularization", "weight": 1.0} -->

We parametrize our cost functions as neural networks, expanding their expressive power and enabling IOC to be applied to the state of a robotic system directly, without hand-designed features. Our experiments in Section 6.2 confirm that an affine cost function is not expressive enough to learn some behaviors. Neural network parametrizations are particularly useful for learning visual representations on raw image pixels. In our experiments, we make use of the unsupervised visual feature learning method developed by Finn et al. to learn cost functions that depend on visual input. Learning cost functions on raw pixels is an interesting direction for future work, which we discuss in Section 7.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Representation and Regularization", "weight": 1.0} -->

While the expressive power of nonlinear cost functions provide a range of benefits, they introduce significant model complexity to an already underspecified IOC objective. To mitigate this challenge, we propose two regularization methods for IOC. Prior methods regularize the IOC objective by penalizing the $\ell_{1}$ or $\ell_{2}$ norm of the cost parameters $\theta$. For high-dimensional nonlinear cost functions, this regularizer is often insufficient, since different entries in the parameter vector can have drastically different effects on the cost. We use two regularization terms.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Representation and Regularization", "weight": 1.0} -->

This term reduces high-frequency variation that is often symptomatic of overfitting, making the cost easier to reoptimize. Although sharp changes in the cost slope are sometimes preferred, we found that temporally slow-changing costs were able to adequately capture all of the behaviors in our experiments.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Representation and Regularization", "weight": 1.0} -->

The rationale behind this regularizer is that, for tasks that essentially consist of reaching a target condition or state, the demonstrations typically make monotonic progress toward the goal on some (potentially nonlinear) manifold. While this assumption does not always hold perfectly, we again found that this type of regularizer improved performance on the tasks in our evaluation. We show a detailed comparison with regard to both regularizers in Appendix E.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

We evaluated our sampling-based IOC algorithm on a set of robotic control tasks, both in simulation and on a real robotic platform. Each of the experiments involve complex second order dynamics with force or torque control and no manually designed cost function features, with the raw state provided as input to the learned cost function.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

We also tested the consistency of our algorithm on a toy point mass example for which the ground truth distribution is known. These experiments, discussed fully in Appendix B, show that using a maximum entropy version of the policy optimization objective (see Section 4.2) and using importance weights are both necessary for recovering the true distribution.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Simulated Comparisons", "weight": 1.0} -->

In this section, we provide simulated comparisons between guided cost learning and prior sample-based methods. We focus on task performance and sample complexity, and also perform comparisons across two different sampling distribution initializations and regularizations (in Appendix E).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Simulated Comparisons", "weight": 1.0} -->

To compare guided cost learning to prior methods, we ran experiments on three simulated tasks of varying difficulty, all using the MuJoCo physics simulator. The first task is 2D navigation around obstacles, modeled on the task by Levine & Koltun. This task has simple, linear dynamics and a low-dimensional state space, but a complex cost function, which we visualize in Figure 2. The second task involves a 3-link arm reaching towards a goal location in 2D, in the presence of physical obstacles. The third, most challenging, task is 3D peg insertion with a 7 DOF arm. This task is significantly more difficult than tasks evaluated in prior IOC work as it involves complex contact dynamics between the peg and the table and high-dimensional, continuous state and action spaces. The arm is controlled by selecting torques at the joint motors at 20 Hz. More details on the experimental setup are provided in Appendix D.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Simulated Comparisons", "weight": 1.0} -->

In addition to the expert demonstrations, prior methods require a set of "suboptimal" samples for estimating the partition function. We obtain these samples in one of two ways: by using a baseline random controller that randomly explores around the initial state (random), and by fitting a linear-Gaussian controller to the demonstrations (demo). The latter initialization typically produces a motion that tracks the average demonstration with variance proportional to the variation between demonstrated motions.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Simulated Comparisons", "weight": 1.0} -->

Between 20 and 32 demonstrations were generated from a policy learned using the method of Levine & Abbeel, with a ground truth cost function determined by the agent's pose relative to the goal. We found that for the more precise peg insertion task, a relatively complex ground truth cost function was needed to afford the necessary degree of precision. We used a cost function of the form ${wd^{2}} + {v{\log{({d^{2} + \alpha})}}}$, where $d$ is the distance between the two tips of the peg and their target positions, and $v$ and $\alpha$ are constants. Note that the affine cost is incapable of exactly representing this function. We generated demonstration trajectories under several different starting conditions. For 2D navigation, we varied the initial position of the agent, and for peg insertion, we varied the position of the peg hole. We then evaluated the performance of our method and prior sample-based methods on each task from four arbitrarily-chosen test states. We chose these prior methods because, to our knowledge, they are the only methods which can handle unknown dynamics.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Simulated Comparisons", "weight": 1.0} -->

We used a neural network cost function with two hidden layers with 24--52 units and rectifying nonlinearities of the form $\max{(z,0)}$ followed by linear connections to a set of features $\mathbf{y}_{t}$, which had a size of 20 for the 2D navigation task and 100 for the other two tasks. The cost is then given by

<!-- chunk {"id": "body-0033", "role": "body", "section": "Simulated Comparisons", "weight": 1.0} -->

with a fixed torque weight $w_{\mathbf{u}}$ and the parameters consisting of $A$, $b$, and the network weights. These cost functions range from about 3,000 parameters for the 2D navigation task to 16,000 parameters for peg insertion. For further details, see Appendix C. Although the prior methods learn only linear cost functions, we can extend them to the nonlinear setting following the derivation in Section 4.1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Real-World Robotic Control", "weight": 1.0} -->

We also evaluated our method on a set of real robotic manipulation tasks using the PR2 robot, with comparisons to relative entropy IRL, which we found to be the better of the two prior methods in our simulated experiments. We chose two robotic manipulation tasks which involve complex dynamics and interactions with delicate objects, for which it is challenging to write down a cost function by hand. For all methods, we used a two-layer neural network cost parametrization and the regularization objective described in Section 5, and compared to an affine cost function on one task to evaluate the importance of non-linear cost representations. The affine cost followed the form of equation 2 but with $\mathbf{y}_{t}$ equal to the input $\mathbf{x}_{t}$.^11^1Note that a cost function that is quadratic in the state is linear in the coefficients of the monomials, and therefore corresponds to a linear parameterization. For both tasks, between 25 and 30 human demonstrations were provided via kinesthetic teaching, and each IOC algorithm was initialized by automatically fitting a controller to the demonstrations that roughly tracked the average trajectory.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Real-World Robotic Control", "weight": 1.0} -->

Full details on both tasks are in Appendix D, and summaries are below.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Real-World Robotic Control", "weight": 1.0} -->

In the first task, illustrated in Figure 3, the robot must gently place a grasped plate into a specific slot of dish rack. The state space consists of the joint angles, the pose of the gripper relative to the target pose, and the time derivatives of each; the actions correspond to torques on the robot's motors; and the input to the cost function is the pose and velocity of the gripper relative to the target position. Note that we do not provide the robot with an existing trajectory tracking controller or any manually-designed policy representation beyond linear-Gaussian controllers, in contrast to prior methods that use trajectory following or dynamic movement primitives with features. Our attempt to design a hand-crafted cost function for inserting the plate into the dish rack produced a fast but overly aggressive behavior that cracked one of the plates during learning.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Real-World Robotic Control", "weight": 1.0} -->

The second task, also shown in Figure 3, consisted of pouring almonds from one cup to another. In order to succeed, the robot must keep the cup upright until reaching the target cup, then rotate the cup so that the almonds are poured. Instead of including the position of the target cup in the state space, we train autoencoder features from camera images captured from the demonstrations and add a pruned feature point representation and its time derivative to the state, as proposed by Finn et al.. The input to the cost function includes these visual features, as well as the pose and velocity of the gripper. Note that the position of the target cup can only be obtained from the visual features, so the algorithm must learn to use them in the cost function in order to succeed at the task.

<!-- chunk {"id": "body-0038", "role": "body", "section": "samples", "weight": 1.0} -->

The results, presented in Table 1, show that our algorithm successfully learned both tasks. The prior relative entropy IRL algorithm could not acquire a suitable cost function, due to the complexity of this domain. On the pouring task, where we also evaluated a simpler affine cost function, we found that only the neural network representation could recover a successful behavior, illustrating the need for rich and expressive function approximators when learning cost functions directly on raw state representations.^22^2We did attempt to learn costs directly on image pixels, but found that the problem was too underdetermined to succeed. Better image-specific regularization is likely required for this.

<!-- chunk {"id": "body-0039", "role": "body", "section": "samples", "weight": 1.0} -->

The results in Table 1 also evaluate the generalizability of the cost function learned by our method and prior work. On the dish rack task, we can use the learned cost to optimize new policies for different target dish positions successfully, while the prior method does not produce a generalizable cost function. On the harder pouring task, we found that the learned cost succeeded less often on new positions. However, as discussed in Section 4.4, our method produces both a policy $q{(\left. \mathbf{u}_{t} \middle| \mathbf{x}_{t} \right.)}$ and a cost function $c_{\theta}$ when trained on a novel instance of the task, and although the learned cost functions for this task were worse, the learned policy succeeded on the test positions when optimized with IOC in the inner loop using our algorithm. This indicates an interesting property of our approach: although the learned cost function is local in nature due to the choice of sampling distribution, the learned policy tends to succeed even when the cost function is too local to produce good results in very different situations.

<!-- chunk {"id": "body-0040", "role": "body", "section": "samples", "weight": 1.0} -->

An interesting avenue for future work is to further explore the implications of this property, and to improve the generalizability of the learned cost by successively training policies on different novel instances of the task until enough global training data is available to produce a cost function that is a good fit to the demonstrations in previously unseen parts of the state space.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

We presented an inverse optimal control algorithm that can learn complex, nonlinear cost representations, such as neural networks, and can be applied to high-dimensional systems with unknown dynamics. Our algorithm uses a sample-based approximation of the maximum entropy IOC objective, with samples generated from a policy learning algorithm based on local linear models. To our knowledge, this approach is the first to combine the benefits of sample-based IOC under unknown dynamics with nonlinear cost representations that directly use the raw state of the system, without the need for manual feature engineering. This allows us to apply our method to a variety of real-world robotic manipulation tasks. Our evaluation demonstrates that our method outperforms prior IOC algorithms on a set of simulated benchmarks, and achieves good results on several real-world tasks.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

Our evaluation shows that our approach can learn good cost functions for a variety of simulated tasks. For complex robotic motion skills, the learned cost functions tend to explain the demonstrations only locally. This makes them difficult to reoptimize from scratch for new conditions. It should be noted that this challenge is not unique to our method. In our comparisons, no prior sample-based method was able to learn good global costs for these tasks. However, since our method interleaves cost optimization with policy learning, it still recovers successful policies for these tasks. For this reason, we can still learn from demonstration simply by retaining the learned policy, and discarding the cost function. This allows us to tackle substantially more challenging tasks that involve direct torque control of real robotic systems with feedback from vision.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

To incorporate vision into our experiments, we used unsupervised learning to acquire a vision-based state representation, following prior work. An exciting avenue for future work is to extend our approach to learn cost functions directly from natural images. The principal challenge for this extension is to avoid overfitting when using substantially larger and more expressive networks. Our current regularization techniques mitigate overfitting to a high degree, but visual inputs tend to vary dramatically between demonstrations and on-policy samples, particularly when the demonstrations are provided by a human via kinesthetic teaching. One promising avenue for mitigating these challenges is to introduce regularization methods developed for domain adaptation in computer vision, to encode the prior knowledge that demonstrations have similar visual features to samples.
