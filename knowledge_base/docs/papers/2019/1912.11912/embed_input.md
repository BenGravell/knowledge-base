<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Quasi-Newton Trust Region Policy Optimization

Topics include Reinforcement learning, Policy optimization, Trust region methods, Quasi-Newton methods.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Applies a quasi-Newton Hessian approximation within the TRPO trust region framework, achieving better sample efficiency and faster convergence than standard TRPO by making more informed second-order parameter updates.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a trust region method for policy optimization that employs Quasi-Newton approximation for the Hessian, called Quasi-Newton Trust Region Policy Optimization QNTRPO. Gradient descent is the de facto algorithm for reinforcement learning tasks with continuous controls. The algorithm has achieved state-of-the-art performance when used in reinforcement learning across a wide range of tasks. However, the algorithm suffers from a number of drawbacks including: lack of stepsize selection criterion, and slow convergence. We investigate the use of a trust region method using dogleg step and a Quasi-Newton approximation for the Hessian for policy optimization. We demonstrate through numerical experiments over a wide range of challenging continuous control tasks that our particular choice is efficient in terms of number of samples and improves performance

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement Learning (RL) is a learning framework that handles sequential decision-making problems, wherein an 'agent' or decision maker learns a policy to optimize a long-term reward by interacting with the (unknown) environment. At each step, an RL agent obtains evaluative feedback (called reward or cost) about the performance of its action, allowing it to improve (maximize or minimize) the performance of subsequent actions. Recent research has resulted in remarkable success of these algorithms in various domains like computer games, robotics, etc. Policy gradient algorithms can directly optimize the cumulative reward and can be used with a lot of different non-linear function approximators including neural networks. Consequently, policy gradient algorithms are appealing for a lot of different applications, and are widely used for a lot of robotic applications. As a result, it has attracted significant attention in the research community where several new algorithms have been proposed to solve the related problems. However, several problems remain open including monotonic improvement in performance of the policy, selecting the right learning rate (or step-size) during optimization, etc.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notably, the Trust Region Policy Optimization (TRPO) has been proposed to provide monotonic improvement of policy performance. TRPO relies on a linear model of the objective function and quadratic model of the constraints to determine a candidate search direction. Even though a theoretically justified trust region radius is derived such a radius cannot be computed and hence, linesearch is employed for obtaining a stepsize that ensures progress to a solution. Consequently, TRPO is a scaled gradient descent algorithm and is not a trust region algorithm as the name suggests. More importantly, TRPO does not inherit the flexibility and convergence guarantees provided by the trust region framework. As a consequence, the impact of trust region algorithms have not been fully investigated in the context of policy optimization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our objective in this work is to show that a *classical trust region method* in conjunction with *quadratic model* of the objective addresses the drawbacks of TRPO. It is well known that incorporating curvature information of the objective function (i.e. quadratic approximation) allows for rapid convergence in the neighborhood of a solution. Far from a solution, the curvature information should be incorporated in a manner that ensures the search direction improves on the reduction obtained by a linear model. We propose the *Quasi-Newton Trust Region Policy Optimization* (QNTRPO) which uses a dogleg method for computing the step, i.e. both the search direction and stepsize are determined jointly. The Quasi-Newton (QN) method allows for incorporating curvature information by approximating the Hessian of the objective without the need for computing exact second derivatives. In particular, we employ the *classical BFGS* approximation. The dogleg method is well known to produce at least as much reduction obtained using a linear model, thus ensuring that QNTRPO does at least as well as the TRPO. The choice of QN method and search direction are chosen to ensure that global convergence properties are retained and the computational cost is comparable to that of TRPO.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We want to investigate if QNTRPO, which has a different step from TRPO, can accelerate the convergence to an optimal policy, and achieve better performance in terms of average reward.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

QNTRPO computes the stepsize as part of the search direction computation and stepsize is naturally varied according to the accuracy of the quadratic model of the objective. QNTRPO learns faster than TRPO due to the quadratic model and improved search direction. We test the proposed method on several challenging locomotion tasks for simulated robots in the OpenAI Gym environment. We compare the results against the original TRPO algorithm and show that we can consistently achieve better learning rate as well as performance.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Trust Region Policy Optimization (TRPO)", "weight": 1.0} -->

In this section, we first describe the original TRPO problem and then we present our proposed method to contrast the difference in the optimization techniques. Using several simplifications to the conservative iteration proposed, authors in proposed a practical algorithm for solving the policy gradient problem using generalized advantage estimation. In the TRPO, the following constrained problem is solved at every iteration: where $L_{\theta_{\text{old}}}{(\theta)}$ is the following term.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Trust Region Policy Optimization (TRPO)", "weight": 1.0} -->

In contrast, the proposed algorithm approximates the objective by a quadratic model and uses the Dogleg method to compute a step. Figure 1 ‣ 2 Background ‣ Quasi-Newton Trust Region Policy Optimization") depicts the idea behind the Dogleg approximation for the trust region optimum. As seen in Figure 1 ‣ 2 Background ‣ Quasi-Newton Trust Region Policy Optimization") the Dogleg method smoothly transitions between the scaled gradient step and a Quasi-Newton step, which is the unconstrained minimizer of the quadratic model.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Quasi-Newton Trust Region Method (QNTRM)", "weight": 1.0} -->

QNTRM has three distinctive elements that sets it apart from TRPO. First, the use of a quadratic approximation for the objective via a Quasi-Newton approximation of the Hessian. Second, the Dogleg method that defines the step. Finally, the adaptive change of the stepsize through the classical trust region framework. We describe each of these in the following. In the rest of the paper, let ${f{(\theta)}} = {- {L{(\theta)}}}$ so that maximization of $L{(\theta)}$ can be equivalently expressed as minimization of $f{(\theta)}$. We use $\theta_{k}$ to refer to the value of the parameters at the $k$-th iterate of the algorithm.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Quadratic Approximation via BFGS", "weight": 1.0} -->

QNTRM approximates the objective using a quadratic model $f_{k}^{q}{(\theta)}$ defined as where $B_{k} \approx {\nabla^{2}f_{k}}$ is an approximation to the Hessian of $f$ at the point $\theta_{k}$. We employ the BFGS approximation to obtain $B_{k}$. Starting with an initial symmetric positive definite matrix $B_{0}$, the approximation $B_{k + 1}$ for $k \geq 0$ is updated at each iteration of the algorithm using the step $s_{k}$ and a difference of the gradients of $f$ along the step $y_{k} = {{{\nabla f}{({\theta_{k} + s_{k}})}} - {\nabla f_{k}}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Quadratic Approximation via BFGS", "weight": 1.0} -->

The update $B_{k + 1}$ is the smallest update (in Frobenius norm ${\|{B - B_{k}}\|}_{F}$) to $B_{k}$ such that ${B_{k + 1}s_{k}} = y_{k}$ (i.e. the secant condition holds), and $B_{k + 1}$ is symmetric positive definite, i.e.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Quadratic Approximation via BFGS", "weight": 1.0} -->

The above minimization can be solved analytically and the update step is Observe the effort involved in performing the update is quite minimal. The above update does not enforce positive definiteness of $B_{k + 1}$. By recasting (2 ‣ Quasi-Newton Trust Region Policy Optimization")) after some algebraic manipulation as it is easy to see that $B_{k + 1}$ is positive definite as long as ${y_{k}^{T}s_{k}} > 0$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Dogleg Method", "weight": 1.0} -->

The search direction in QNTRM $\Delta\theta_{k}$ is computed by approximately solving i.e. minimizing the quadratic model of the objective subject to the KL-divergence constraint. The above problem is only solved approximately since the goal is only to produce a search direction $\Delta\theta_{k}$ that furthers the overall objective of minimizing $f{(\theta)}$ at moderate computational cost. However, the search direction $\Delta\theta_{k}$ should incorporate both the curvature and attain sufficient progress towards a solution. In fact, we desire at least as much progress as the step in TRPO. The Dogleg method does precisely this by combining the scaled gradient direction ${\Delta\theta_{k}^{GD}} = {- {\beta_{k}F_{k}^{- 1}{\nabla f_{k}}}}$ and the QN direction ${\Delta\theta_{k}^{QN}} = {- {B_{k}^{- 1}{\nabla f_{k}}}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Dogleg Method", "weight": 1.0} -->

The search direction $\Delta\theta_{k}^{DL}$ is obtained using Algorithm 1 ‣ Quasi-Newton Trust Region Policy Optimization").

<!-- chunk {"id": "body-0017", "role": "body", "section": "Dogleg Method", "weight": 1.0} -->

The algorithm first computes the QN direction $\Delta\theta_{k}^{QN}$ and accepts it if the trust region constraint defined by the KL-divergence holds (Step 1 ‣ Quasi-Newton Trust Region Policy Optimization")). If not the algorithm computes the scaled gradient direction (Step 1 ‣ Quasi-Newton Trust Region Policy Optimization")) and a stepsize $\beta_{k}$ so as to minimize the quadratic model, i.e.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Dogleg Method", "weight": 1.0} -->

Unlike the TRPO, observe that due to the curvature in the objective we can now define an *optimal stepsize* for the gradient direction. If the gradient direction scaled by the optimal stepsize exceeds the trust region then it is further scaled back until the trust region constraint is satisfied and accepted (Step 1 ‣ Quasi-Newton Trust Region Policy Optimization")). If neither of the above hold then the direction is obtained as a convex combination of the two directions ${\Delta\theta{(\tau_{k})}}:={({{\Delta\theta_{k}^{GD}} + {\tau_{k}{({{\Delta\theta_{k}^{QN}} - \theta_{k}^{GD}})}}})}$. This is the *Dogleg direction*. The parameter $\tau_{k}$ is chosen so that the direction $\Delta\theta{(\tau_{k})}$ satisfies the trust region constraint as an equality (Step 1 ‣ Quasi-Newton Trust Region Policy Optimization")).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Dogleg Method", "weight": 1.0} -->

The computation of $\tau_{k}$ requires finding the roots of a quadratic equation which can be obtained easily.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Dogleg Method", "weight": 1.0} -->

Note that QNTRM requires the solution of linear system in order to compute $B_{k}^{- 1}{\nabla f_{k}}$ and $F_{k}^{- 1}{\nabla f_{k}}$. Both of these can be accomplished by the Conjugate Gradient (CG) method since $B_{k},F_{k}$ are both positive definite. Thus, the computation QNTRM differs from TRPO by an extra CG solve and hence, comparable in computational complexity.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Dogleg Method", "weight": 1.0} -->

Result: Dogleg direction Δ θkD L 5 Compute Gradient direction Δ θkG D = −βk Fk−1 ∇fk where βk is defined; 7 return $\sqrt{\frac{\delta_{k}}{{({\Delta\theta_{k}^{GD}})}^{T}F_{k}{({\Delta\theta_{k}^{GD}})}}}\Delta\theta_{k}^{GD}$ 9Find largest τk ∈ such that Δ θ (τk):= (Δ θkG D + τk (Δ θkQ N − θkG D)) satisfies (Δ θ (τk))T Fk (Δ θ (τk)) = δk; Algorithm 1 Dogleg Method

<!-- chunk {"id": "body-0022", "role": "body", "section": "Trust Region Algorithm", "weight": 1.0} -->

QNTRM combines the curvature information from QN approximation and Dogleg step within the framework of the classical trust region algorithm. The algorithm is provided in Algorithm 2 ‣ Quasi-Newton Trust Region Policy Optimization") and incorporates safeguards to ensure that $B_{k}$'s are all positive definite. At each iteration of the algorithm, a step $\Delta\theta_{k}^{DL}$ is computed using Algorithm 1 ‣ Quasi-Newton Trust Region Policy Optimization") (Step 2 ‣ Quasi-Newton Trust Region Policy Optimization")). The trust region algorithm accepts or rejects the step based on a measure of how well the quadratic model approximates the function $f$ along the step $\Delta\theta_{k}^{DL}$. The commonly used measure is the ratio of the actual decrease in the objective and the decrease that is predicted by the quadratic model (Step 2 ‣ Quasi-Newton Trust Region Policy Optimization")). If this ratio $\nu_{k}$ is close to or larger than $1$ then the step computed using the quadratic model provides a decrease in $f$ that is comparable or much better than predicted by the model.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Trust Region Algorithm", "weight": 1.0} -->

The algorithm uses this as an indication that the quadratic model approximates $f$ well. Accordingly, if the ratio (Step 2 ‣ Quasi-Newton Trust Region Policy Optimization")) is larger than a threshold ($\underset{¯}{\nu}$), the parameters are updated (Step 2 ‣ Quasi-Newton Trust Region Policy Optimization")). If in addition, the ratio is larger than $\overline{\nu}$ and $\Delta\theta_{k}$ satisfies the trust region size as an equality then the size of the trust region is increased in the next iteration (Step 2 ‣ Quasi-Newton Trust Region Policy Optimization")). This condition indicates that the quadratic model matches the objective $f$ with high accuracy and that the progress is being impeded by the size of the trust region. Hence, the algorithm increases the trust region for the next iteration. With the increased trust region size the algorithm promotes the possible acceptance of a direction other than the scaled gradient direction.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Trust Region Algorithm", "weight": 1.0} -->

On the other hand, if the ratio is below $\underset{¯}{\nu}$ then the computed direction is rejected (Step 2 ‣ Quasi-Newton Trust Region Policy Optimization")) and the size of the trust region is decreased (Step 2 ‣ Quasi-Newton Trust Region Policy Optimization")). This reflects the situation that the quadratic model does not the capture the objective variation well. Note that as the size of the trust region decreases the performance of the algorithm mirrors that of TRPO very closely. Thus, QNTRM is naturally designed to be no worse than the TRPO and often surpass TRPO's performance whenever the quadratic model approximates the objective function well. Finally, we update the QN approximation whenever the $s_{k}^{T}y_{k}$ is greater than a minimum threshold. This ensures that the matrices $B_{k}$ are all positive definite (Step 2 ‣ Quasi-Newton Trust Region Policy Optimization")). Note that this safeguard is necessary since the Dogleg step cannot be designed to ensure that ${s_{k}^{T}y_{k}} > 0$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Quasi-Newton Trust Region Policy Optimization (QNTRPO)", "weight": 1.0} -->

QNTRPO is the trust region algorithm that we propose in this paper for policy optimization, The algorithm differs from TRPO in the step that is computed at every iteration of policy iteration. For completeness of the paper, it is presented as an Algorithm 3 ‣ Quasi-Newton Trust Region Policy Optimization"). It is noted that the only difference between QNTRPO and TRPO is the way the trust region optimization problem is solved (see line $4$ in Algorithm 3 ‣ Quasi-Newton Trust Region Policy Optimization")). It is noted that in the original TRPO formulation, the line $4$ in Algorithm 3 ‣ Quasi-Newton Trust Region Policy Optimization") is performed using the scaled gradient method as discussed earlier. This is the major difference between the proposed and the algorithm proposed in TRPO. Note that QNTRM is an iterative procedure and that the step for every iteration of Algorithm 3 ‣ Quasi-Newton Trust Region Policy Optimization") is computed by iterating over $K$ steps of QNTRM (see Algorithm 2 ‣ Quasi-Newton Trust Region Policy Optimization")). This is yet another difference over TRPO where a single gradient descent step is computed for each episode.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Quasi-Newton Trust Region Policy Optimization (QNTRPO)", "weight": 1.0} -->

As a result, the computational time per episode for QNTRPO is no more than $({2 \times K})$ that of TRPO owing to the possibly two linear systems solves in Dogleg method and K iterations in QNTRM.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Quasi-Newton Trust Region Policy Optimization (QNTRPO)", "weight": 1.0} -->

1Initialize policy parameters θ0 2 for i = 0, 1, 2, … until convergence do 3 Compute all Advantage values Aπθi (s, a) and state-visitation frequency ρθi; 4 Define the objective function for the episode Lθi (θ) = −fi (θ); 5 Obtain θi + 1 using QNTRM to minimize fi (θ) with initial policy parameters θ0 = θi

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In this section, we present experimental results for policy optimization using several different environments for continuous control from the openAI Gym benchmark. In these experiments, we try to answer the following questions: Can QNTRPO achieve better learning rate (sample efficiency) than TRPO consistently over a range of tasks?

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Can QNTRPO achieve better performance than TRPO over a range of tasks in terms of average reward?

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In the following, we try to answer these two questions by evaluating our algorithm on several continuous control tasks. In particular, we investigate and present results on four different environments in Mujoco physics simulator. We implement four locomotion tasks of varying dynamics and difficulty: Humanoid, Half-Cheetah, Walker and Hopper. The goal for all these tasks is to move forward as quickly as possible. These tasks have been proven to be challenging to learn due to the high degrees of freedom of the robots. A great amount of exploration is needed to learn to move forward without getting stuck at local minima. During the initial learning stages, it is easy for the algorithm to get stuck in a local minima as the controls are penalized and the robots have to avoid falling. The state and action dimensions of these tasks are listed in Table 1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We run both TRPO and QNTRPO for 500 episodes and average all results across five different runs with different random seeds for the environment initialization. All hyperparameters for the algorithms -- batch size, policy network architecture, step size and the generalized advantage estimation coefficient ($\lambda$) -- are identical for both algorithms. As TRPO (and thus QNTRPO ) performs better with bigger batches, we use a batch size of $15000$. In each of these episodes, trajectories are generated for a maximum length of $2000$ and then restarted either if the terminal condition is met or the trajectory length is satisfied. The network architecture is kept the same across all the tasks. The trust region radius is chosen to be $0.1$ (note that this is the parameter $\overline{\delta}$ in Algorithm 2 ‣ Quasi-Newton Trust Region Policy Optimization")). At lower trust region radius both algorithms performed slower and thus the results are not reported here. The discount factor $\gamma$ is chosen to be $0.99$ and the constant $\lambda$ for advantage function estimation is chosen to be $0.97$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

The parameters for QNTRM were chosen to be the following: $K = 10$, $\overline{\nu} = 0.75$, $\underset{¯}{\nu} = 0.1$, $\underset{¯}{\omega} = 0.3$, $\overline{\omega} = 2$ and $\underset{¯}{\kappa} = 10^{- 3}$. Codes for running these experiments are available at [www.merl.com/research/license#QNTRPO](www.merl.com/research/license#QNTRPO).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Results of our experiments are shown in Figure 3. For all four tasks, we can demonstrate that QNTRPO can achieve faster learning, and thus better sample efficiency than the original TRPO. Furthermore, the performance of QNTRPO is also significantly better than TRPO. This is evident from the fact that QNTRPO achieves higher rewards than TRPO, which also has longer transitory. For high complexity problems like Humanoid, QNTRPO takes about $350$ episodes with the current batch size to reach the maximum score (of around $3000$). These results show that QNTRPO can calculate a better step for the constrained optimization problem for policy iteration using QNTRM.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

In this paper, we presented an algorithm for policy iteration using a Quasi-Newton trust region method. The problem was inspired by the policy optimization problem formulated in where a linesearch is performed to compute the step size in the direction of steepest descent using a quadratic model of the constraint. In this paper, we proposed a dogleg method for computing the step during policy iteration which has theoretical guarantees of better performance over the scaled gradient descent method used. The proposed method was compared against the original TRPO algorithm in four different continuous control tasks in Mujoco physics simulator. The proposed algorithm outperformed TRPO in learning speed as well performance indicating that the proposed method can compute better step for the policy optimization problem.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

Despite the good performance, there are a number of open issues for which we do not have a complete understanding. We have observed that the maximum trust region radius ($\overline{\delta}$) plays an important role in speed of learning. However, choosing this arbitrarily might result in poor convergence. Furthermore, to achieve monotonic improvement in policy performance, one has to select the trust region radius very carefully which is undesirable. It would also be interesting to study the interplay of batch size and trust region radius. This can help address the issue of steplength selection. In the future, we would like to further investigate several features of the proposed algorithm including the following.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

Analyze the stability of the proposed algorithm to the size of trust region radius and batch size. We believe that the proposed method can be used to fine tune the hyperparameter of trust region radius which controls the maximum step size in each iteration of the algorithm.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

Evaluate the proposed algorithm on much higher dimension learning problem for end-to-end learning using a limited memory version of the proposed algorithm.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

Use ideas from ensemble methods, scalable bootstrapping and factored methods to curvature for better and efficient approximation of the objective function.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

Evaluate the performance on challenging, sparse reward environments.
