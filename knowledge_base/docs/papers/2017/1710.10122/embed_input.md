<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RRT-CoLearn: Towards Kinodynamic Planning without Numerical Trajectory Optimization

Topics include Sampling-based, Sampling-based planning, Kinodynamic, Kinodynamic planning, Motion planning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling-based kinodynamic planners, such as Rapidly-exploring Random Trees (RRTs), pose two fundamental challenges: computing a reliable (pseudo-)metric for the distance between two randomly sampled nodes, and computing a steering input to connect the nodes. The core of these challenges is a Two Point Boundary Value Problem, which is known to be NP-hard. Recently, the distance metric has been approximated using supervised learning, reducing computation time drastically. The previous work on such learning RRTs use direct optimal control to generate the data for supervised learning. This paper proposes to use indirect optimal control instead, because it provides two benefits: it reduces the computational effort to generate the data, and it provides a low dimensional parametrization of the action space. The latter allows us to learn both the distance metric and the steering input to connect two nodes. This eliminates the need for a local planner in learning RRTs. Experimental results on a pendulum swing up show 10-fold speed-up in both the offline data generation and the online planning time, leading to at least a 10-fold speed-up in the overall planning time.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

For motion planning of robotic manipulators, kinodynamic planning and sampling-based planning are getting increasingly popular. Kinodynamic planning, i.e., planning in state-space rather than configuration space, improves robustness, speed and energy efficiency of robots. Sampling based planning has been shown to be the most viable way to handle high dimensional spaces and obstacles. In this paper, we will consider how to apply Rapidly-exploring Random Trees, the most popular sampling-based planning algorithm, to kinodynamic planning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

RRT builds a tree graph structure with the states of the system as tree nodes and the trajectories of the system between two states as tree edges. The algorithm selects a node to expand from based on a *distance* to a randomly sampled node in the state space, i.e., it selects the *nearest* node in the current tree. The algorithm then expands that tree node, by means of a local planner that aims to reach the randomly-sampled node. These steps happen online, so computation time is crucial. Unfortunately, in state-space, both local planning and distance computation are computationally expensive. One approach to reduce the computational burden is to approximate the true distance function by a heuristic. Two frequently used heuristics are the Euclidean distance and the optimal cost-to go of a linear approximation to the system. The convergence of RRT variants using the Euclidean distance heuristic, and random steering inputs, was extensively analysed. For promising results for the linearizing heuristic see. However, these heuristics only minimally utilize the dynamical properties of the system, and therefore typically require more nodes to solve a given problem using RRT.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another approach, which we call Learning-RRT, was proposed recently and has already shown promising initial results. Learning-RRT involves an offline machine learning phase that learns the distance and steering function in the RRT (Figure 1). An optimal control algorithm provides a database of optimal trajectories, which is the input for a supervised learning algorithm. This algorithm learns to approximate the functions the RRT requires. Supervised learning provides two benefits: 1) generalization over state-space and 2) fast online predictions. Thereby, the computational burden of trajectory optimization does not have to be repeated for new situations, and, it is shifted offline.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Note that the final trajectory found by the RRT-algorithm is in general not optimal, even though the trajectories in the database are optimal. The database therefore is not build up of optimal trajectories to improve the cost to go of the RRT-trajectory. Rather, optimality improves learning performance by providing a meaningful cost-to go metric and trajectories that tend to have a similar shape if they connect similar points in state space.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Local planning: In literature on learning-RRT, only the distance function is approximated by machine learning. Recall that the RRT also requires a steering function. Supervised learning of that function is hard due to the large number of parameters typically required to describe optimal input signals. Therefore, previous Learning-RRTs resort to a computationally expensive numerical optimization for their steering function.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Dataset generation: The dataset for the supervised learning algorithm consists of many optimal trajectories. As optimizing a single trajectory already is a significant computational burden, generating a full dataset is very computationally demanding.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contribution of this paper is the use of indirect optimal control to generate the dataset. This allows us to solve both the problems mentioned above, thereby decreasing the computational burden by up to two orders of magnitude, both in the offline and the online phase of the learning RRT planning. However, the dataset generated by this method contains a bias, which is problematic for the learning algorithm. It turns out we can efficiently remove this bias through a simple dataset resampling algorithm.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The focus of this paper is to introduce this novel method and its implementation details. Our experiments provide proof of concept by evaluating our method on the pendulum swing-up task studied in the previous learning-RRT implementation by Bharetheesha et al.. This allows us to demonstrate and compare the validity of our method. To our knowledge, we are the first to demonstrate learning of the control input in a kinodynamic sampling-based planning task.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The structure of this paper is as follows. We start with a generic specification of the Learning-RRT algorithm (Section 2). This specification is applicable to any data generation method, and intended to structure all Learning-RRT components. Subsequently, the main contribution follows in Section 3, which tackles the problems of local planning and dataset generation. Then we discuss how to remove the dataset bias introduced by optimal control in Section 4. In Section 5, we discuss how the cost-to go metric, and the learned approximation thereof, affect the convergence of the RRT algorithm. The experimental proof of concept of our algorithm is presented in Section 6. Finally, Sections 7 and 1 contain discussion and conclusions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Learning-based RRT", "weight": 1.0} -->

Learning-based RRTs leverage the benefits of (supervised) learning to speed up the computationally expensive modules of a kinodynamic RRT. The Learning-RRT algorithm is presented in Algorithm 1.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Learning-based RRT", "weight": 1.0} -->

D̂ ← generate_data (N)// Section 3
D ← clean_data (D̂) // Section 4
V̂ ← fit_valid (D) // Section 5
while NOT(solutionfound) do
xnearest ← arg min x ∈ XĴ (x,xtarget)
(c,x,u) ← simulate (xnearest,Û (xnearest,xtarget))
Algorithm 1 Learning RRT ((V, E), N)

<!-- chunk {"id": "body-0014", "role": "body", "section": "Learning-based RRT", "weight": 1.0} -->

The first step in the algorithm is to create a dataset of optimal trajectories. Specifically, we generate a dataset $D = {\{ b^{i}\}}_{i = 1}^{N}$, where each entry $b^{i} = {\{ x_{0}^{i},x_{1}^{i},j^{i},u^{i}\}}$ consists of an initial state $x_{0} \in \mathcal{X}$, a final state $x_{1} \in \mathcal{X}$, a distance metric/cost-to-go $j \in {\mathbb{R}}^{+}$, and a set of parameters $u \in \mathcal{U}$, that describe the optimal input leading the system from state $x_{0}$ to state $x_{1}$. Note that $\mathcal{U}$ can take many forms, depending on the discretization used.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Learning-based RRT", "weight": 1.0} -->

For example, in previous work the input has been cast as a polynomial over time, with $\mathcal{U}$ being the coefficients of that polynomial. Alternatively, when the input is cast as a piecewise-linear function, $\mathcal{U}$ consists of the values of the function at the switch-times.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Learning-based RRT", "weight": 1.0} -->

The optimal trajectories are generally found using a numerical algorithm searching for local optima, which poses a challenge for the supervised learning algorithm. If two solutions are nearby in $x_{0}$ and $x_{1}$, but hail from a different local optimum, a deterministic supervised learning algorithm (for example trained on mean-squared error) will predict the average over the two solutions. This not only makes the cost prediction inaccurate, but most importantly ruins the steering input prediction: the average of the two steering inputs in the data could lead to a completely different state than the target state. This local-optimum bias requires us to create the dataset $D$ in two stages. The first stage creates a dataset $\hat{D}$ of size $N$ which contains local-optimum-bias, and is indicated in Alg. 1 by the function generate_data. The second stage clean_data removes the local-optimum-bias to create the desired dataset $D$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Learning-based RRT", "weight": 1.0} -->

The second step is to use a supervised learning algorithm on $D$ to approximate the two functions that define the optimal control solution: 1. the function $\hat{J}:{{(\mathcal{X},\mathcal{X})}\rightarrow{\mathbb{R}}^{+}}$, which maps from an initial and a final state to a cost-to-go, 2. the function $\hat{U}:{{(\mathcal{X},\mathcal{X})}\rightarrow\mathcal{U}}$, mapping the initial and final state to the required input parameters.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Learning-based RRT", "weight": 1.0} -->

For both function approximators we implement k-nearest neighbours, a standard non-parametric function approximator with robust performance in smaller state-spaces. For a dataset test point $x$, we identify the $k$ nearest neighbours in our dataset $D$ based on Euclidean distance. The predicted value (e.g. for cost $j$) for the test point then becomes the average value of these neighbours. We cover possible extensions to other supervised learning techniques in the Discussion.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Learning-based RRT", "weight": 1.0} -->

The next step in the algorithm, fit_valid, addresses some inherent limitations of supervised learning approaches. We defer further details on this step to Section 5.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Learning-based RRT", "weight": 1.0} -->

The fourth stage of the Learning-RRT algorithm is essentially the online RRT stage. First, sample a point in statespace. Then test if there is a valid connection from any node in the tree to the sampled point. If that is the case, expand the node that is nearest to the sampled point according to the function $\hat{J}$. The expansion will use the learned input parameter function $\hat{U}$, which will likely make a small error. The new node is therefore not exactly the sampled point, but a point in statespace that hails from the approximation $\hat{U}$. The algorithm iterates these steps until it connects to the desired region in state-space. Finally, as standard in RRTs the sampling of new nodes includes a goal bias: it will intermittently replace the uniform state-space sample with the desired end-point.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Data generation", "weight": 1.0} -->

The dataset for the function approximator is generated from a set of optimal trajectories for the system and cost function under consideration. The most common approach to find these trajectories are the so-called *direct* optimal control approaches. In these approaches the state equations and cost function are approximated by a discretized system, which is then numerically optimized.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Data generation", "weight": 1.0} -->

An alternative to direct optimal control is the much older *indirect* approach, which first optimizes and then discretizes. For many applications, direct approaches replaced the indirect approach due to better numerical stability at long planning distances. However, it turns out indirect optimal control is ideally suited for the RRT scenario. First, the numerical instability poses no problem for the short segments that are required for RRT. Furthermore, indirect optimal control brings two important benefits. First, it provides a parametrized control input in low dimensional space, which allows learning of the control input. Second, it removes the need for optimization in the sampling process, which speeds up data generation. We will explain both benefits at the end of this section, after introducing the indirect optimal control method. At that point, we will also explain the remaining downside of the indirect optimal control approach: a more biased dataset.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Indirect optimal control", "weight": 1.0} -->

This section will discuss the standard indirect optimal control procedure, which forms the basis for our dataset generation method. The exposition derives the optimal control equations for our experimental system: the single pendulum swing-up. The procedure for other systems will mostly follow the same outline; small differences can occur. For those differences, more details and proofs we refer to.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Indirect optimal control", "weight": 1.0} -->

where $x_{\text{initial}}$ and $x_{\text{final}}$ are fixed initial and goal states, and the final time $t_{f}$ is optimized along with the trajectory and input function. In the remainder we will often drop the explicit dependency on the time $t$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Indirect optimal control", "weight": 1.0} -->

For the single pendulum we have $x = {(\theta,\omega)}$, where $\theta$ and $\omega$ are the (angular) position and velocity respectively. With $u$ being a torque, we get $f = {(\omega,{{\sin{(\theta)}} + u})}$. Finally, as a cost function, we take into account both the time it takes to reach the goal-state, as well as the energy expended to get there, by setting the cost integrand to $C = {w + {u^{2}/2}}$, with $w$ a weight which tunes the contribution of the time component in the cost function.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Indirect optimal control", "weight": 1.0} -->

The first step in the indirect optimal control approach is to define the Hamiltonian $\mathcal{H}$, which is the sum of the integrand $C$ and the inner product of a vector of Lagrange multipliers with the state equations. The Lagrange multipliers are called the costates, and in the case of the pendulum consist of $(\lambda_{\theta},\lambda_{\omega})$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Indirect optimal control", "weight": 1.0} -->

In typical use of the indirect optimal control approach, the last step is to use the Equations 6-7 to find the optimal trajectory. For a given costate, the above system of equations are (numerically) integrated, which results in a locally optimal state trajectory. Note that this trajectory depends on the choice of initial costate, and the time duration of the integration. By tuning the initial costate and final time, we find a locally optimal state trajectory that reaches the desired state. This tuning normally requires a numerical optimization method, which minimizes the difference between final state and desired state. In the next section, we will show that such an optimization is not required for us.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Indirect optimal control", "weight": 1.0} -->

Optimal control problems solved for Learning-RRTs typically have a free final time and a cost integrand $C$ that does not explicitly depend on time. For these problems there is an additional constraint on the initial costate.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Indirect optimal control", "weight": 1.0} -->

The main reason why *indirect* optimal control is largely replaced by direct methods, such as multiple shooting, is that the resulting differential equations are unstable, and therefore difficult to numerically solve reliably. However, the RRT algorithm splits the whole motion into small parts, so it is only required to solve problems with a small integration period, making this instability less important.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Benefits of using indirect optimal control", "weight": 1.0} -->

We can immediately see two major advantages of this optimal control approach for use in Learning-RRT setting. First, the input directly follows from the costates, i.e., in principle, there is a mapping ${U{(x_{\text{initial}},x_{\text{final}})}}\rightarrow{({\lambda_{\theta}{}},{\lambda_{\omega}{}},t_{\text{f}})}$, from initial and final state to a set of only three parameters that describe the input function. This set is small, and will only grow linearly with the size of the statespace (and is even independent of the number of inputs). In contrast, direct optimal control approaches require to parametrize inputs as functions over time, which results in much larger spaces of parameters to learn. The reduction in the number of parameters means the input function can be learned efficiently, thereby solving the problem of *local planning* in RRTs as identified in the introduction.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Benefits of using indirect optimal control", "weight": 1.0} -->

To see the second major advantage, look at how the whole dataset is created. In current learning RRTs, the dataset is generated by sampling from the $(x_{\text{initial}},x_{\text{final}})$-space, and then, find an optimal trajectory and cost for each sample. Note that every combination of initial state, initial costate and final time produces an optimal trajectory for a certain final state. So, if we sample from the allowed initial states, initial costates and final times, we effectively sample over all initial state - final state combinations. While previous approaches had to numerically optimize the steering input, we can eliminate the need for numerical optimization by sampling the costate, meaning the data are generated much faster.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Benefits of using indirect optimal control", "weight": 1.0} -->

Algorithm 2 outlines the data generation procedure. The functions *random_State*, *random_Costate*, and *random_Time* specify random states, costates and final times within bounds that depend on the problem. Furthermore, the function *random_Costate* takes into account Eq. 8. Finally, the function *integrate* numerically integrates the optimal control equations until the final time. To optimize the efficiency of the data generation we incorporate the intermediate integration results in the data set as well, even though the resulting datapoints are therefore no longer independent from each-other.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Benefits of using indirect optimal control", "weight": 1.0} -->

In this section, we have outlined the indirect optimal control approach to solving the *data generation* problem in the learning RRT algorithm. Because the optimal control algorithm incorporates costates, we name the overall algorithm RRT-CoLearn. We have also discussed its two major advantages: learning optimal steering inputs (increasing online speed) and generating data without optimizing (increasing offline speed).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Benefits of using indirect optimal control", "weight": 1.0} -->

Optimal_ODEs ← Eqs. 1-7
xinitial ← random_State
λinitial ← random_Costate s.t. Eq. 8
Tfinal ← random_Time
xfinal, J ← integrate(Optimal_ODEs,xinitial,λinitial,Tfinal)
append(D̂,{xinitial,xfinal,J,λinitial})
Algorithm 2 generate_data(N)

<!-- chunk {"id": "body-0035", "role": "body", "section": "Dataset cleaning", "weight": 1.0} -->

The dataset generated by Algorithm 2 originates from a search for local optima, and can therefore include a bias that interferes with learning performance. The problem is illustrated for with an artificial dataset in Figure 2 (top), where in the middle input region we have the global optimum at the bottom, but there are local optima above it. A standard function approximator (with squared loss) for a given point in input space (independent variable) predicts the expectation of the dependent variable. This results in the conditional mean of the datapoints, as shown by the green line in Figure 2 (top). Note how the predicted function deteriorates in the middle segment, where it predicts the average instead of the bottom (optimal) cost.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Dataset cleaning", "weight": 1.0} -->

This is problematic for predicting the cost function and especially harmful for predicting the control parameters. Averaging over two locally optimal control inputs by no means guarantees that we end up anywhere close to the target. We therefore need a dataset cleaning algorithm, i.e., a procedure that somehow eliminates the non-optimal datapoints. In literature, there are resampling methods for dataset imbalance, most noteworthy class label imbalance in classification tasks. However, our dataset is not imbalanced, but rather contains a systematic bias. It turns out we can leverage the fact that the noise is systematic to come up with a simple resampling/cleaning algorithm.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Dataset cleaning", "weight": 1.0} -->

pneigh← nearestNeighbour(psample, D)
phigh ← arg min p ∈ {psample, pneigh}Cost (p)
Algorithm 3 clean_data(D̂, d, kmax)

<!-- chunk {"id": "body-0038", "role": "body", "section": "Dataset cleaning", "weight": 1.0} -->

For each point in input space, we are interested in retaining the lower bound of the cost of the generated datapoints. First note that we prefer to remove points in high-density regions, as in low-density regions there is little to throw away, and we may only hope that our data are accurate. We implicitly remove from high density regions by first uniformly sampling a point from our dataset. We then search for its nearest neighbour in the dataset based on a Euclidean distance. If this neighbour is within a distance $d$ from our sampled point, we remove the node of the two with the highest cost. Otherwise, we retain both points. This process is repeated until no points are removed for $k_{m}$ consecutive steps, after which we return the cleaned dataset. The procedure is outlined in Algorithm 3.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Dataset cleaning", "weight": 1.0} -->

The main parameter in this algorithm, $d$, can be interpreted as a neighbourhood size. In low density regions, there will be no nearby points within distance $d$, and we will therefore never remove a point. In high-density regions, the algorithm will remove the highest cost datapoint of the two, frequently removing the biased one while retaining a good one. We can see the performance of this algorithm for different $d$ in Figure 2, which shows there is an optimal setting of $d$ that depends on the dataset. $d$ is a hyperparameter of our algorithm and has to be scaled empirically. In this case, this means fixing $d$, running the cleaning, fitting the function predictors, and then sampling new datapoints and assessing the error in cost and co-state parameters on the predictions. This is not ideal, but the proper evaluation metric (RRT performance) would come at additional computational cost. For our experimental problem, we found that a simple grid-search provides easy scaling of $d$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Machine learning considerations", "weight": 1.0} -->

The proposed algorithm adds machine learning based approximations to standard RRT, which intuitively might interfere with convergence of the algorithm. Therefore, we establish probabilistic completeness of our algorithm, by modifying the proof for the original RRT. We have not tried to make the proof outlined here as general as possible. The framework from would potentially aid in that effort.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Machine learning considerations", "weight": 1.0} -->

First, we assume there exists a solution to our planning problem, and that it is build out of a finite number of shorter trajectories. That is, the solution has $n$ waypoints $\mathcal{X} = {\{ x_{0},x_{1},\ldots,x_{n}\}}$. The controls between those waypoints are given by $\mathcal{U} = {\{ u_{0},\ldots,u_{n - 1}\}}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Machine learning considerations", "weight": 1.0} -->

If $x_{i}$ is the most advanced waypoint currently in the tree, the chance of getting to the next node can be factored as

<!-- chunk {"id": "body-0043", "role": "body", "section": "Machine learning considerations", "weight": 1.0} -->

Now if we can guarantee both factors are positive, i.e., ${P{({\text{expand~}x_{i}})}} > 0$ and ${P{(\left. u_{i} \middle| {\text{expand~}x_{i}} \right.)}} > 0$, we get: ${P{({\text{reach~}x_{i + 1}})}} > 0$. This means the chance of getting to the next node of the solution is finite, so at some point the algorithm will get to the next node, and the next one, and so. Therefore the algorithm will converge.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Bounding the chance of picking the right action", "weight": 1.0} -->

To ensure the chance of picking the right action is bounded from below, the number of possible inputs should be finite. Therefore we discretize the continuous input representation (the initial costate and the time duration of the trajectory). In the experiments, this is done by rounding them to 2-decimals.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Bounding the chance of picking the right action", "weight": 1.0} -->

Furthermore, a deterministic function approximator might not select the right steering input. Therefore we should use a probabilistic steering input, which could assign a higher probability to steering inputs closer to those suggested by the function approximator, but which gives at least some probability to each input.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Bounding the chance of picking the right action", "weight": 1.0} -->

In our experiments, the control parameters were sampled from truncated normals, with the bounds for each parameter specified by its sampled domain. The means are the value predicted by the learned model. The standard deviation $\sigma$ of the (non-truncated)-normal is a parameter of the algorithm.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Bounding the chance of picking the right action", "weight": 1.0} -->

When looking at practical performance, inaccurate prediction makes selecting the right action particularly difficult whenever the problem requires the RRT to very precisely reach a small region in state-space, for example when near the goal region. In experiments we found that we could reduce the time to get from 'close to' the goal region to inside the goal region by increasing the standard deviation when the predicion involves the goal state.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Bounding the chance of picking the right node", "weight": 1.0} -->

Since the volume of $\mathcal{X}_{free}$ is fixed and finite, we only need to make sure the numerator is non-zero. This should be done while taking into account that the cost-to-go function is piecewise continuous, with a discontinuity at $0$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Bounding the chance of picking the right node", "weight": 1.0} -->

There should also be something affecting an upper bound to the distance function.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Bounding the chance of picking the right node", "weight": 1.0} -->

Note that these conditions are not met in two frequently studied cases: 1. when the cost function is the integral of the squared input, 2. when the system is not small time locally accessible, as happens for instance in underactuated systems.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Bounding the chance of picking the right node", "weight": 1.0} -->

Take the largest ball $\mathcal{B}_{\rho}{(x_{i})}$ centered around point $x_{i}$, such that ${c_{\text{ub}}{\|{x_{i} - y}\|}} \leq {c_{\text{lb}}{\|{x - y}\|}}$ for all $y$ in the ball, and all nodes $x$ in the tree. Based on simple Euclidean geometry, $\rho > 0$. Furthermore, by construction, the intersection ${\mathcal{B}_{\rho}{(x_{i})}} \cap {\mathcal{G}{(x_{i})}}$ has positive volume, and all points in that intersection are closer (by measure $d$) to node $x_{i}$ than to any other node in the tree. Together this shows that ${P{({\text{expand~}x_{i}})}} > 0$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Bounding the chance of picking the right node", "weight": 1.0} -->

If we had access to the true distance function, or an approximation of it that meets the conditions specified above, this would conclude the proof of convergence. However, learning algorithms are intended to generalize using interpolation, so may make large errors when extrapolating. This is especially true for Learning RRTs, for which this problem has not been identified in literature yet. For most machine learning, test data usually originate from the same data distribution (e.g. a picture, video, audio fragment or person characteristics) as the training data. However, in RRTs we *uniformly* sample state-space, while we have confined our dataset to only contain short motion segments. Therefore, if we sample a new combination $(x_{0},x_{1})$, we have a reasonable chance of sampling outside of our dataset, where function approximation may make large errors, which might cause conditions 10 and 12 to be violated. Particularly, the approximated distance metric might greatly underestimate the cost-to-go from a certain node, causing that node to be incorrectly chosen for expansion.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Bounding the chance of picking the right node", "weight": 1.0} -->

In our implementation, we enforce the conditions by using a binary classifier that decides whether a query would yield a valid prediction of the cost and input parameters. We learn a function $\hat{V}:{{(\mathcal{X},\mathcal{X})}\rightarrow\text{v}}$, with $v \in {\lbrack\text{true},\text{false}\rbrack}$ which identifies when a combination of initial state and final state is valid (true), i.e. when the dataset $D$ covers that point in input-space. We implement a basic, but functional, $\hat{V}$-function that computes the summed distance to the nearest neighbours of the queried point to the points in the dataset, and rejects the query point if this sum becomes too large. An alternative approach relies on the notion that the dataset contains only short segments, meaning the final states should be reachable within a short period of time. The use of reachable sets to classify the validity of a distance metric in state-space RRT was already explored.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Bounding the chance of picking the right node", "weight": 1.0} -->

Also, to avoid violations of conditions 10 and 12 by small approximation errors in the learned function, the predicted cost-to go is saturated at lower and upper bounds of $10^{\mp 5}$. These bounds were chosen such that they enforce the conditions on the cost function, while their effect on the computation is negligable.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Experiments", "weight": 1.0} -->

To test our approach, we perform experiments on a relatively simple problem: pendulum swingup. This is a task on a single degree of freedom system in which a pendulum has to move from its stable equilibrium ${(\theta,\omega)} = {({- \pi},0)}$ to its unstable equilibrium $$. The equations of motion for the pendulum are given in Section 3.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experiments", "weight": 1.0} -->

Data were generated and cleaned 10 times, to create 10 epochs, with 300 runs of the RRT algorithm per epoch. The data for each epoch consist of 40000 simulations, which ended when the costs or norm of the state difference with the initial state exceeds $2$ or $1.5$. Integration was done by the 4th order Runge-Kutta algorithm with a time step of $0.01\ s$. The initial position was uniformly sampled from $({- {{3\pi}/2}},{\pi/2})$$rad$, the initial velocity from $({- \pi},\pi)$${rad}\ s^{- 1}$, and the initial costate sampled as described below. The data cleaning resolution $d$ equals 0.05. The data cleaning stopping parameter $k_{\text{max}}$ is set to 5000. The nearest neighbour fitting algorithm during the RRT takes $m = 3$ nearest neighbours. Finally, the standard deviation of the sampling distribution $\sigma = {\pi/4}$ normally, and $\pi/2$ when the query involves the goal state.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experiments", "weight": 1.0} -->

To avoid projecting on the costate constraint (Eq. 8), which is computationally expensive for larger systems, we solve the constraint explicitly, i.e.,

<!-- chunk {"id": "body-0058", "role": "body", "section": "Experiments", "weight": 1.0} -->

If $\lambda_{\omega}$ has an imaginary part, the simulation is disregarded. The choice for the free parameter influences the sampling-density of the initial costates. Because the $\tan$-function has a low value on most of its domain, the initial costates tend to be small as well. This causes low initial torques, which is desired for the pendulum swing up. The above parametrization can be generalized for input affine systems with a cost function that is quadratic in the input, a class that includes many mechanical systems.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Results", "weight": 1.0} -->

The experiments were performed on a MacBook with Intel(R) Core(TM) i5-3210M CPU 2.50GHz processor and 8GB of RAM, running Ubuntu Linux 14.04. All the relevant code is written in Python. Figure 4 shows the variation in computation times for each epoch separately. The computation time does not change much between epochs, indicating that the data generation and cleaning are robust against random perturbations. Furthermore, it suggests that using multiple datapoints from a single simulation does not deteriorate the quality (i.i.d.-ness) of the dataset. The median time to reach the target over all samples was 2.36 seconds, more than 10 times faster than on the same hardware.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Results", "weight": 1.0} -->

The simulations and data cleaning in this algorithm took a total of approximately $25\ \min$ per epoch. This also is an order of magnitude faster than the algorithm from ^11^1The cited paper does not report the offline computation time. However, the authors of that paper overlap with the authors of this paper, so we know that the offline computation took nearly a week..

<!-- chunk {"id": "body-0061", "role": "body", "section": "Results", "weight": 1.0} -->

The performance of the optimal control function approximation is assessed using the mean squared error between the target state and the final state attained by using the predicted costate. The median of this error over all the epochs is 0.11. Furthermore, the approximation quality is indirectly measured by the number of nodes needed to reach the target. The median over all runs is $84$ nodes, with a standard deviation of $180$ nodes, which is about 30% smaller (better) than the previous algorithm. A slight decrease is expected, as the problem no longer requires the pendulum to swing back and forth to reach the final position. The decrease is therefore best interpreted as a roughly equal performance of the distance metric and optimal trajectory functions. This equal performance is obtained even though the optimal trajectory now uses function approximation.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Discussion", "weight": 1.5} -->

The algorithm introduced in this paper allows learning of not only the distance metric, but also the steering input. As proof of concept, we tested our algorithm on a basic pendulum swing up problem, showing that it reduces the time spend both in the offline learning and in the online-computation by a factor of more than 10. This result is a large step towards making sampling based state-space planning in a practical setting feasible.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Discussion", "weight": 1.5} -->

The main direction for future research is extending the algorithm for use on higher degree of freedom systems. The number of simulations required to learn the cost and costate functions is expected to grow rapidly with the number of degrees of freedom. Extension towards higher degrees of freedom would require a switch to different function approximators than the k-nearest neighbours used in this work. To handle higher dimensions, it would be beneficial to have a higher sample efficiency of the dataset. The current data generation procedure samples uniformly from state and costate, which is likely inefficient. This might be improved by sampling new simulations based on the already obtained data, and the (partially) learned cost and costate functions. Similar ideas have been used in reinforcement learning and might be beneficial for use in Learning RRTs. Finally, higher dimensional systems also require a more robust clean-up function. One improvement over the current cleaning function would be to not only compare trajectories based on their endpoints, but to explicitly take into account the distance in input-and-cost-to-go space. Alternatively, (deep) generative models allow to sample from complex, high-dimensional probability distributions.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Discussion", "weight": 1.5} -->

Using the approach, we could retain all solutions while avoiding the averaging over solutions that is done in standard discriminative models.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Discussion", "weight": 1.5} -->

A secondary direction for future research is to incorporate input bounds. Such bounds are readily incorporated in the indirect optimal control scheme, see. However, there is an issue with the resulting costates: there can be an exact overlap between trajectories of a system with input bounds starting from different costates, at least for a finite time. Such overlapping trajectories cannot be handled by the basic learning and cleaning algorithms we used. Extending these algorithms, such that they can cope with such overlapping trajectories is an important theoretical and practical issue.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Optimal local planner
Fast online prediction

<!-- chunk {"id": "body-0067", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Needs large dataset3
Needs distance metric

<!-- chunk {"id": "body-0068", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Local optima→bias4
Needs unbiased data4
Needs local planner3

<!-- chunk {"id": "body-0069", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we described a general Learning RRT algorithm, and identified several problems with state-of the art versions. Table 1 summarizes the parts that make up the algorithm, and their benefits and challenges.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We proposed the RRT-CoLearn Algorithm which addresses three problems of Learning RRT: 1. By using indirect optimal control the number of parameters that describe the input is very small. The parameters of this function can thus be learned, alleviating the need for local planning in the online phase. 2. By using indirect optimal control, the data generation can be done much faster, as a numerical optimization is replaced by sampling. 3. An algorithm was proposed that removes the dataset bias caused by local optima.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The RRT coLearn algorithm was tested on a pendulum swing up. It achieves a median planning time of $2.4\ s$, which is $10$ times faster than the state-of the art learning algorithm for kinodynamic RRT.
