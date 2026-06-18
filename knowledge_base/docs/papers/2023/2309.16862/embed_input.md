<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stochastic Implicit Neural Signed Distance Functions for Safe Motion Planning under Sensing Uncertainty

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motion planning under sensing uncertainty is critical for robots in unstructured environments to guarantee safety for both the robot and any nearby humans. Most work on planning under uncertainty does not scale to high-dimensional robots such as manipulators, assumes simplified geometry of the robot or environment, or requires per-object knowledge of noise. Instead, we propose a method that directly models sensor-specific aleatoric uncertainty to find safe motions for high-dimensional systems in complex environments, without exact knowledge of environment geometry. We combine a novel implicit neural model of stochastic signed distance functions with a hierarchical optimization-based motion planner to plan low-risk motions without sacrificing path quality. Our method also explicitly bounds the risk of the path, offering trustworthiness. We empirically validate that our method produces safe motions and accurate risk bounds and is safer than baseline approaches.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robots in unstructured environments must reliably plan safe (*i.e.*, collision-free) motions using only uncertain, noisy sensor percepts. For robots in human-oriented environments (*e.g.*, home or assistive robotics), this capability is crucial---as unsafe motions may hurt humans---and challenging, as these robots are often high degree-of-freedom (d o f) manipulators. Reliable safety under uncertainty requires not only producing plans that are unlikely to collide, but also providing evidence that plans are trustworthy. Moreover, for practical use, planners need to efficiently support complex environments without knowledge of the true environment geometry.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, most work on motion planning under uncertainty makes simplifying assumptions about robot or environment geometry (*e.g.*, point robots or environments with only known, simple geometry), does not scale to high d o f systems, or places strict assumptions on the distributions of noise (*e.g.*, only translational noise, segmented to individual objects or normally distributed).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, we introduce a method for reliable, safe motion planning for high d o f systems under sensing uncertainty that directly models inherent sensor noise without placing assumptions on the environment. We propose to quantify the aleatoric uncertainty of the sensor with an implicit model of the stochastic signed distance fields between the robot's links and points in the environment, conditioned on the robot's configuration. By explicitly modeling this uncertainty, we can both compute safe paths given only noisy sensing and approximately bound the remaining risk of collision.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, we contribute a variational inference perspective on modeling stochastic signed distance fields for motion planning (inspired by ), used to learn an implicit neural model of sensor-specific noisy egocentric distance, which we incorporate in a novel chance-constrained inverse kinematics (ik) formulation, allowing us to create a hierarchical planner that produces minimal risk motions (with respect to the learned distance model and an uncertainty-agnostic initial motion plan) in realistic environments. Our learned model directly predicts distribution parameters for noisy distance measurements to arbitrary points in the environment, allowing it to capture the aleatoric uncertainty of the sensor in question without assuming that noise is segmented to the level of individual objects or requiring knowledge of object geometry. We empirically validate that our model correctly predicts both distance values and their uncertainty, and that our planner finds motion plans that are both safe (*i.e.*, minimize risk) and reliable (*i.e.*, the predicted risk matches or conservatively upper-bounds the empirically measured probability of collision). We further compare our planner to a commonly used baseline and show that, despite longer planning times, we produce significantly safer and higher-quality plans.

<!-- chunk {"id": "body-0007", "role": "body", "section": "III-A Motion Planning under environmental uncertainty", "weight": 1.0} -->

Collision chance constraints, or constraints on the probability that a robot's trajectory collides with a noisy environment, have been successfully used for safe motion planning under uncertainty by a wide range of work. Chance constraints are typically determinized to keep the planning problem tractable. These deterministic reformulations are then used by either optimization or sampling -based motion planners to generate provably safe trajectories. Similarly, we also reformulate and enforce chance constraints to guarantee a desired maximum risk of collision. For example, create a disjunctive convex optimization problem that can be solved with branch-and-bound; build a tree-like planner that validates states against the reformulated constraints. uses a similar idea for non-Gaussian uncertainty and moment-based ambiguity sets of distributions. Finally, propose a differentiable surrogate risk for manipulator robots and convex obstacles under Gaussian translational uncertainty that is guaranteed to never underestimate the true risk, enforced by constraints in a nonlinear program.

<!-- chunk {"id": "body-0008", "role": "body", "section": "III-A Motion Planning under environmental uncertainty", "weight": 1.0} -->

Many of these methods rely on simplified robot shapes, *e.g.*, point robots, obstacle shapes, *e.g.*, polyhedral or convex, and the noise model, *e.g.*, additive Gaussian noise on obstacle positions. In contrast, our method is designed for high-d o f robots and complex, noisy scenes, where point-robot assumptions are insufficient and strict assumptions on the noise distribution may not hold.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Motion Planning under environmental uncertainty", "weight": 1.0} -->

When reformulating chance constraints, most methods allocate equal risk for every waypoint and/or obstacle in the path to make the problem tractable. However, this strategy can lead to overly conservative solutions, since robot configurations that are far from noisy obstacles will still be forced to satisfy difficult risk bounds. A few works have considered non-uniform risk allocation, either by formulating multi-stage optimization problems, iteratively penalizing and relaxing risky waypoints from previous solutions, or using differentiable surrogate risks encoded as variables in a nonlinear optimization problem. Similar to, our method enforces joint chance constraints by using the union bound (Boole's inequality) and solving a set of individual chance constraints. However, in our method, the risk bound of individual chance constraints for all obstacle-link pairs are decision variables in our optimization formulation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-A Motion Planning under environmental uncertainty", "weight": 1.0} -->

Other methods design certificates that verify that a path is safe under a noise model. assess path safety by assuming a linear-quadratic controller with Gaussian uncertainty (LQG-MP). Several candidate paths are generated using a sampling-based planner and the best is chosen for execution. certify a path as safe for a given level of risk if the robot's swept volume does not intersect a set of unsafe regions. design probabilistic collision checkers for non-Gaussian distributions, which they use in an optimization-based planner to encourage safety. also handle non-Gaussian distributions by solving a robustly formulated sequential convex programming problem. generate candidate paths, propagate the uncertainty along the path using LQG-MP and estimate the resulting risk of collision via numerical integration. Our proposed approach also generates risk-agnostic candidate paths which it then transforms into safe paths by solving a sequence of convex optimization problems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-B Implicit Representations and Uncertainty Quantification", "weight": 1.0} -->

Recent machine learning advances have produced efficient implicit neural representations of spatial information, such as Neural Radiance Fields (NeRFs) and Signed Distance Fields. Robotics researchers have used these representations to learn multi-object dynamics, as manipulation planning constraints, to achieve reactive robot manipulation and to perform visual-only robot navigation. Beyond their compact, efficient storage, these representations are advantageous for planning due to their continuous representation of geometry and ability to be learned directly from sensor data. Recent work has also investigated quantifying the uncertainty of a learned model. Methods to estimate both aleatoric and epistemic uncertainty have been proposed in the computer vision and reinforcement learning literatures. This is important to enable the design of uncertainty-aware algorithms for downstream tasks. For example, propose probabilistic frameworks that attempt to capture uncertainty in a NeRF for synthetic novel view and depth-map estimation. Similarly, our method takes a probabilistic approach to quantifying aleatoric sensing uncertainty. However, our proposed neural representation also fuses kinematic information about a robot with spatial information to produce a robot-configuration-conditioned probabilistic distance model.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Safe Motion Planning with a Stochastic Neural Representation", "weight": 1.0} -->

In this work, we assume that information about the environment is captured through a sensor as noisy $3$D points, akin to a point cloud. This noise is aleatoric from the perspective of the planner as it stems from immutable properties of the sensor and is irreducible. We propose to quantify this aleatoric sensing uncertainty through a stochastic implicit neural representation that models noisy signed distances between the environment and the robot geometry. Our neural representation, inspired, captures not only geometric information about the environment (as in work based on NeRFs or SDFs ), but also kinematic information about the robot itself, which makes it suitable for motion planning for manipulation. We find safe paths despite sensing errors by using this representation in a novel *hierarchical motion planner*, instead of directly attempting to reformulate and solve II. Our planner first finds a candidate path using only the noisy sensed points (without knowledge of their noise), and then uses this candidate path and a user-provided bound on the risk of collision to compute a safe path. The following sections describe our aleatoric sensing representation and planning framework.

<!-- chunk {"id": "body-0013", "role": "body", "section": "IV-A Stochastic Neural Implicit Signed Distance Representation", "weight": 1.0} -->

propose an implicit neural representation that models the signed distance between each robot link and arbitrary points in space. The neural representation learns $\Gamma:{{\mathcal{Q} \times {\mathbb{R}}^{3}}\rightarrow{\mathbb{R}}^{K}}$ comprising $K$ related mappings $\Gamma_{k}:{{\mathcal{Q} \times {\mathbb{R}}^{3}}\rightarrow{\mathbb{R}}}$. Each $\Gamma_{k}{(q,x)}$ is the minimum distance function for the $k$-th robot link ($1 \leq k \leq K$), evaluated at the 3D point $x$ when the robot is in configuration $q$. This representation is useful for motion planning for manipulation due to 1) representing distances to arbitrary points in the workspace without depending on specific geometry and 2) its gradients point away from obstacles in *configuration space*.

<!-- chunk {"id": "body-0014", "role": "body", "section": "IV-A Stochastic Neural Implicit Signed Distance Representation", "weight": 1.0} -->

Inspired by this representation, we propose to learn a distribution, $S$, over signed distance functions, such that the distance between each robot link and points in the workspace is modeled as a Gaussian random variable. We want to learn the posterior of $S$ conditioned on a training set $\mathcal{T}$ consisting of a finite collection of robot configurations $q_{i}$, 3D points $x_{i}$ and per-link noisy signed distance values $d_{i}^{k}$, *i.e.*, $\mathcal{T} = {\{\left( {\{ d_{i}^{k}\}}_{k = 1}^{K},q_{i},x_{i} \right)\}}_{i = 1}^{N}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-A Stochastic Neural Implicit Signed Distance Representation", "weight": 1.0} -->

We formulate the problem using a Bayesian approach to compute the posterior $\text{Pr}\left( S \middle| \mathcal{T} \right)$. Note that explicitly computing this posterior is intractable since it would require the computation of the evidence *i.e.*, the marginal density of the observations. Instead, we approximate it using variational inference (VI), where a parametric distribution $\psi_{\theta}{(S)}$ approximates the true distribution. The goal of VI is to find the parametric distribution that is closest to the true distribution, measured via their KL divergence. As the KL divergence is not computable because it requires the evidence, VI typically optimizes the evidence lower bound (ELBO).

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A Stochastic Neural Implicit Signed Distance Representation", "weight": 1.0} -->

where the first term is the KL divergence between $\psi_{\theta}$ and a prior $p{(S)}$ on the signed distance field, to encourage densities close to the prior, and the second term is the negative training set likelihood over the approximate posterior $\psi_{\theta}$, which will choose parameters $\theta$ that best explain the observed data.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A Stochastic Neural Implicit Signed Distance Representation", "weight": 1.0} -->

We assume that $\psi_{\theta}$ can be factored as the product of independent Gaussian densities, $\psi_{\theta}^{k}{(\left. d \middle| {q,x} \right.)}$, representing the distance fields for each robot link $k$. These densities are jointly modeled as a neural network, $\Gamma{(q,x)}$, that outputs the parameters of $\psi_{\theta}$, $\{\mu_{1},\sigma_{1},\ldots,\mu_{K},\sigma_{K}\}$ (see Fig. 2 for network architecture). The second term in Eq. 3a is computed in closed form using the likelihood of the Gaussian distribution.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Stochastic Neural Implicit Signed Distance Representation", "weight": 1.0} -->

For the first term we assume that (similar to $\psi_{\theta}$) the prior can be factored as a product of Gaussians, $p^{k}{(d)}$ with parameters $\{\mu_{k}^{p},\sigma_{k}^{p},\}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Stochastic Neural Implicit Signed Distance Representation", "weight": 1.0} -->

In practice, we use a fixed number of samples to remove the dependency of the approximate posterior on $x$ and $q$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Chance-Constrained Hierarchical Planning", "weight": 1.0} -->

We propose a hierarchical motion planner to generate safe robot motions, described in Alg. 1. First, an off-the-shelf motion planner is used to find a candidate path $\rho^{c}$ in the noisy sensed environment $\Xi$ (Alg. 1). For each waypoint of $\rho^{c}$ (Alg. 1), we solve a chance-constrained ik problem (ccikopt, Alg. 1) to compute the motion to the *next* waypoint. We use the pose of the robot's end-effector at $q_{j + 1}^{c}$ as a soft constraint for the $j$-th ik problem, encouraging solutions close to the original path. We accumulate the risk allocated to each waypoint to ensure that it does not exceed the bound $\Delta$ for the total path (Alg. 1). Each ik problem is allowed up to the full remaining risk available, and returns an upper bound on the risk allocated to the corresponding waypoint.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Chance-Constrained Hierarchical Planning", "weight": 1.0} -->

This method can be seen as using $\rho^{c}$ as *guidance* for the sequence of ik problems, while flexibly accommodates the allowable risk bounds to compute a safe path, $\rho^{s}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Chance-Constrained Hierarchical Planning", "weight": 1.0} -->

input: qstart, 𝒬goal, Ξ, Δ
1 ρc ← MotionPlan (qstart,𝒬goal,Ξ);
4 if (Δq,δ,γ) ←CCIKOPT (qj + 1c,qjs,Δj) then
Algorithm 1 Chance-Constrained Hierarchical Motion Planner

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Chance-Constrained Hierarchical Planning", "weight": 1.0} -->

with decision variables $\mathbf{\Delta}{\mathbf{q}}$ and $\mathbf{δ}$. $\mathbf{\Delta}{\mathbf{q}}$ corresponds to the robot motion between $q_{j}^{s}$ and $q_{j + 1}^{s}$; $\mathbf{δ}$ is a vector of slack variables that provide flexibility on the goal pose of the end-effector. We minimize a quadratic function of the decision variables to encourage small motions that end close to the original end-effector pose from $\rho^{c}$. Constraint (4a) is the joint chance constraint requiring the risk of collision to remain under a given threshold $\Delta_{j}$ for all robot links $1 \leq k \leq K$ and noisy points $1 \leq r \leq R$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Chance-Constrained Hierarchical Planning", "weight": 1.0} -->

In its deterministic version, when $\Gamma_{k,r} = {\Gamma_{k}{(q_{j}^{s},x_{r})}}$ becomes small, $\mathbf{\Delta}{\mathbf{q}}$ is forced to align with $- {\nabla\Gamma_{k,r}}$ (which points away from collision with $r$) to avoid potential collisions. In our approach, $\Gamma_{k,r}$ are random Gaussian variables, and we enforce that the probability that this constraint is satisfied is above a given threshold. In the next section we describe our reformulation of the constraint to make the problem tractable.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-C Reformulation of the Chance-Constrained IK Problem", "weight": 1.0} -->

which requires the risk variables to be in $0 < {\mathbf{γ}}_{{\mathbf{k}},{\mathbf{r}}} \leq 0.5$. This restriction is reasonable in our context since we are interested in paths with low collision risk.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-C Reformulation of the Chance-Constrained IK Problem", "weight": 1.0} -->

We have added a linear term on the objective function of the reformulated problem to minimize the amount of risk allocated to the waypoint at the $j$-th iteration. This per-waypoint minimum risk behavior of our formulation is necessary to account for potentially high-risk future waypoints on the path. It also has the effect of allowing us to *globally* minimize (with respect to $\Gamma$ and $\rho^{c}$) the risk of $\rho^{s}$. To solve Prob. 3, we create piecewise-affine conservative approximations of the $\log$ functions in the collision risk chance-constraints. This approximation creates mixed-integer programs that can be solved using commercial solvers to global optimality at the cost of potentially high computation time.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Evaluation and Results", "weight": 1.0} -->

We evaluate our proposed approach on a $n = 8$ d o f Fetch robot with $K = 11$ links, corresponding to those in the kinematic chain of its end effector (including the torso and fingers). We use PyBullet for collision checking, PyTorch for neural network training, OMPL's Python bindings for planning and Gurobi as our optimizer. All experiments were conducted on an Intel i7-12700K CPU and a RTX2080Ti GPU.

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-A Implicit Neural Representation", "weight": 1.0} -->

We parameterize our implicit stochastic distance model as a feed-forward neural network (Fig. 2c). For a $n$-d o f robot, the network takes an input tensor of size $3*{({n + 3})}$ comprising the $n$ values of the robot configuration concatenated with the $3$ coordinates of the environment point, as well as the sine and cosine of these values. These trigonometric components serve as a form of positional encoding similar to that used in standard neural radiance fields. The network has a shared core of four fully connected 256-wide layers with rectified linear unit (ReLU) activation. For a robot with $K$ links, the output of these layers is used (independently) with one additional fully connected layer of size $256 \times K$ to predict the mean distance from the environment point to each link's geometry, as well as with another fully connected layer of size $256 \times K$ and a softplus layer of size $K$ to predict the standard deviation of these distances.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-A Implicit Neural Representation", "weight": 1.0} -->

We generate a dataset of noisy distance samples from a simulated sensor to train the distance model. Similarly to, we sample a set of robot configurations ($Q$) uniformly at random. For each configuration, we sample a set of environment points uniformly at random ($P_{R}$), a set of environment points *near* to each link ($P_{N}$) and a set of environment points *inside* each link ($P_{I}$). We compute the true shortest distance between each point and link using PyBullet. We then simulate a set of noisy sensor measurements ($NS$) with mean at the true distance for each environment point and a fixed standard deviation ($\sigma$). In our experiments, ${|Q|} = 3000$, ${|P_{R}|} = 500$, ${|P_{N}|} = {K*10}$, ${|P_{I}|} = {K*20}$, ${|{NS}|} = 50$, and $\sigma = {2\ {cm}}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-A Implicit Neural Representation", "weight": 1.0} -->

This results in a total of 2.49 million sampled points, each of which has 50 noisy distance samples. Empirically, this dataset is roughly balanced between points in collision and points in free space.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-A Implicit Neural Representation", "weight": 1.0} -->

We train the model on the collected dataset for $500$ epochs with an Adam optimizer, learning rate of $1 \times 10^{- 4}$, and batch size of $512$. We verify its performance by predicting distance distributions between robot links and a set of randomly generated 3D points from the waypoints of $1000$ discretized paths. The gripper link shows an average error of $1\ {cm}$ for mean and $3.7\ {mm}$ for standard deviation while the elbow attains $0.7\ {mm}$ and $0.3\ {mm}$, respectively. Fig. 3 shows the predicted and true distribution parameters for one path, one randomly selected point and these two robot links.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-B Safe Motion Planning with Implicit Neural Representation", "weight": 1.0} -->

We evaluate our proposed approach on a set of simulated tabletop manipulation problems generated using MotionBenchMaker. The Fetch robot needs to plan to grasp an object, avoiding collisions with the table and obstacles upon it (Fig. 1). We create 50 problems by randomly perturbing the positions ($\pm 2.5$cm in $x,y,z$) and orientations ($\pm 15^{\circ}$) of the objects of a nominal scene and the relative pose of the robot's base ($\pm 10$cm in $x,y,z$ and $\pm 90^{\circ}$) with respect to the table. The environment is represented as a point cloud-like set of noisy 3D spheres of different radii that covers the (unknown to the planner) collision geometries of all objects.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-B Safe Motion Planning with Implicit Neural Representation", "weight": 1.0} -->

We assume that the table's geometry is noise-free while the objects on top are noisily sensed, per Sec. V-A. Note that these problems were designed by to be challenging and "realistic" from the motion planning perspective and require the robot to plan long, elaborate paths that need to avoid the table and then dodge collisions with the objects on top.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-B Safe Motion Planning with Implicit Neural Representation", "weight": 1.0} -->

We compare the performance and safety of our approach with a commonly used baseline: inflating the environment's geometry to encourage the computation of paths that maintain larger clearance and have therefore less chances of colliding. We inflate each sphere by increasing its radius by ${{20\%},{40\%}},$ or $60\%$. We also include results of $0\%$ inflation as a baseline to show the performance of a planner that is unaware of the sensing uncertainty. Motion plans for all baselines, as well as the candidate paths used by our method, are computed using RRT-Connect with simplification enabled to encourage short and smooth paths.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-B Safe Motion Planning with Implicit Neural Representation", "weight": 1.0} -->

We estimate the risk of collision for each computed path using Monte-Carlo sampling with $20,000$ samples, where each sample draws sphere poses from the noisy sensed distribution. For our method, we also show the guaranteed path-wise risk bound (Risk Bound) and estimated risk of collision of the candidate path before optimization (Initial Risk). All problems have a maximum number of $15$ attempts to find any valid (*i.e.*, collision-free with respect to the inflated obstacles, for the baselines) plan. The results are shown in Fig. 4.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-B Safe Motion Planning with Implicit Neural Representation", "weight": 1.0} -->

[width=]svg-inkscape/risk_svg-tex.pdf_tex
Figure 4: Estimated CDF of the risk attained by each method on all 50 problems.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-B Safe Motion Planning with Implicit Neural Representation", "weight": 1.0} -->

We note that the uncertainty-unaware planner produces paths with the highly variable risk of collision (an average of $60\%$), which is likely unacceptable for safety-critical applications. For higher parameter values of the inflated baseline, the estimated risk of collision decreases as expected due to a larger $\mathcal{Q}$-space obstacle region that encourages larger clearance with the true geometry. However, there is no clear relation between the inflation increase and the drop in risk which makes the baselines difficult to tune when a desired level of risk is required (see also Table I). Additionally, we note that success rate (not shown here) for the baseline methods started dropping significantly as the inflation ratio increased, suggesting a potential limit on minimum risk that they can attain for these problems. We give our planner a maximum allowable risk bound of $10\%$ and ask it to return the minimum risk for each waypoint. Our proposed approach can compute paths with significantly lower risk for most problems, starting from risky candidate paths.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B Safe Motion Planning with Implicit Neural Representation", "weight": 1.0} -->

For each problem and method we also compute the path length and end-effector displacement as path quality metrics, as well as the time taken by the planner. The results are summarized in Table I.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Safe Motion Planning with Implicit Neural Representation", "weight": 1.0} -->

The table shows mean and standard deviation for each method over all $50$ problems. The large values of path length and end-effector displacement are evidence of the high complexity of the computed paths due to the challenging motion planning problems. Our method finds paths with lowest end-effector displacement and path length, which is the result of the minimization of motion displacement in our planner. However, our method shows planning times that are orders of magnitude larger than the baselines. This is mostly due to a large number of risk constraints being added to each chance-constrained problem, which creates large mixed-integer programs that require deep branch and bounds searches to find optimal solutions. Despite this, it is noteworthy that our method can find paths with the lowest collision risk among the baselines without sacrificing path quality.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

This paper presents a novel approach to planning under sensing uncertainty for high d o f robots that reliably computes safe paths without strong assumptions on the true environment geometry. Our planner relies on an implicit neural representation trained to capture aleatoric uncertainty arising from the robot's sensor. Our representation does not place assumptions on the environment but instead directly approximates signed distance distributions between the robot and points in space, conditioned on robot configurations. We further show how this representation can be integrated with a hierarchical planner to compute paths with guaranteed bounds on the probability of collision (up to the quality of the model). We have experimentally validated the merits of our approach on challenging, realistic manipulation motion planning problems to show that our method is capable of finding safe paths despite sensing uncertainty without reducing path quality. As future work we will investigate how to further reduce the need for conservative over-approximations in our approach, since this will allow us to solve more tightly constrained motion planning problems, such as those found in manipulation in clutter. We will also seek to reduce the time taken by our method, in part by applying intelligent constraint subset selection heuristics to simplify the optimization problems solved at each waypoint.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

Finally, we will further investigate the need to consider the epistemic uncertainty coming from our neural representation for planning; a problem that has recently gained much attention in machine learning.
