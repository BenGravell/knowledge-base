const mindMapData = {
  "nodes": [
    {
      "data": {
        "id": "1957_dubins_on_curves_of_minimal",
        "label": "Dubins path",
        "title": "On Curves of Minimal Length with a Constraint on Average Curvature, and with Prescribed Initial and Terminal Positions and Tangents",
        "authors": [
          "Dubins"
        ],
        "year": 1957,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Path generation",
          "Dubins",
          "Curvature"
        ],
        "summary": "Dubins provided analytic formulas for the shortest curve that connects two points in the two-dimensional Euclidean plane (i.e. x-y plane) with a constraint on the curvature of the path and with prescribed initial and terminal tangents to the path, and an assumption that the vehicle traveling the path can only travel forward. Dubins proved using tools from analysis that any such path will consist of maximum curvature and/or straight line segments. In other words, the shortest path will be made by joining circular arcs of maximum curvature and straight lines."
      }
    },
    {
      "data": {
        "id": "1970_jacobson_differential_dynamic_programming",
        "label": "DDP",
        "title": "Differential Dynamic Programming",
        "authors": [
          "Jacobson",
          "Mayne"
        ],
        "year": 1970,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Differential dynamic programming",
          "DDP",
          "Trajectory optimization",
          "Optimal control",
          "Dynamic programming"
        ],
        "summary": "Foundational text introducing Differential Dynamic Programming (DDP), a trajectory optimization method that uses second-order Taylor expansions of the value function within a dynamic programming framework for efficient nonlinear optimal control."
      }
    },
    {
      "data": {
        "id": "1978_doyle_guaranteed_margins_for_lqg",
        "label": "LQG",
        "title": "Guaranteed margins for LQG regulators",
        "authors": [
          "Doyle"
        ],
        "year": 1978,
        "category": "Control",
        "sub_category": null,
        "tags": [
          "Linear Quadratic Gaussian (LQG)",
          "Robust control"
        ],
        "summary": "Seminal paper demonstrating that there are no guaranteed robustness margins for linear quadratic Gaussian (LQG) controllers i.e. an optimal linear dynamic output feedback controller composed of a linear quadratic regulator (LQR) and a Kalman filter. This was proven by counterexample using a very simple linear system with two states, one control input, one disturbance input, and one output. This is in stark contrast to the simpler state feedback LQR setting, for which there are 60 degree phase and 6 dB gain margins. This paper is known for having the shortest abstract in the history of IEEE Transactions on Automatic Control, at just three words."
      }
    },
    {
      "data": {
        "id": "1985_bobrow_time_optimal_control_of",
        "label": "TOPP",
        "title": "Time-Optimal Control of Robotic Manipulators Along Specified Paths",
        "authors": [
          "Bobrow",
          "Dubowsky",
          "Gibson"
        ],
        "year": 1985,
        "category": "Motion Planning",
        "sub_category": "Speed Planning",
        "tags": [
          "Time-optimal control",
          "Path parameterization",
          "Manipulator trajectory planning",
          "Bang-bang control",
          "Torque constraints"
        ],
        "summary": "Seminal paper establishing the time-optimal path parameterization (TOPP) problem: given a specified geometric path and actuator torque limits, finds the minimum-time traversal by solving for bang-bang optimal torques in the velocity-position phase plane."
      }
    },
    {
      "data": {
        "id": "1985_juang_an_eigensystem_realization_algorithm",
        "label": "ERA",
        "title": "An Eigensystem Realization Algorithm for Modal Parameter Identification and Model Reduction",
        "authors": [
          "Juang",
          "Pappa"
        ],
        "year": 1985,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "System identification",
          "Modal analysis",
          "Model reduction",
          "Eigensystem realization algorithm",
          "ERA",
          "Algorithm",
          "Structural dynamics"
        ],
        "summary": "Introduces ERA, which extracts modal parameters (natural frequencies, damping ratios, mode shapes) from free-decay or impulse response data via eigendecomposition of a Hankel matrix, enabling reduced-order model construction for structural dynamics."
      }
    },
    {
      "data": {
        "id": "1990_reeds_optimal_paths_for_a",
        "label": "Reeds-Shepp path",
        "title": "Optimal paths for a car that goes both forwards and backwards",
        "authors": [
          "James Alexander Reeds",
          "Shepp"
        ],
        "year": 1990,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Path generation",
          "Reeds-Shepp",
          "Curvature"
        ],
        "summary": "Reeds and Shepp provided analytic formulas for the shortest curve that connects two points in the two-dimensional Euclidean plane (i.e. x-y plane) with a constraint on the curvature of the path and with prescribed initial and terminal tangents to the path, and an assumption that the vehicle traveling the path can travel forward or backward. Reeds and Shepp proved using tools from analysis that any such path will consist of maximum curvature and/or straight line segments, with at most two cusps of the form CCSCC where C is an arc of a circle of the minimal turning radius and S is a line segment."
      }
    },
    {
      "data": {
        "id": "1994_overschee_n4sid_numerical_algorithms_for",
        "label": "N4SID",
        "title": "N4SID: Numerical Algorithms for State Space Subspace System Identification",
        "authors": [
          "Overschee",
          "Moor"
        ],
        "year": 1994,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "System identification",
          "Subspace identification",
          "Subspace methods",
          "State space models",
          "N4SID"
        ],
        "summary": "Introduces the N4SID algorithm, which identifies linear state-space models from input-output data using projections of block Hankel matrices, providing a numerically robust approach to subspace system identification."
      }
    },
    {
      "data": {
        "id": "1996_kavraki_probabilistic_roadmaps_for_path",
        "label": "PRM",
        "title": "Probabilistic roadmaps for path planning in high-dimensional configuration spaces",
        "authors": [
          "Kavraki",
          "Svestka",
          "Latombe"
        ],
        "year": 1996,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Path planning",
          "Probabilistic",
          "Roadmap",
          "Probabilistic roadmap",
          "Graph search"
        ],
        "summary": "Seminal paper that introduced PRM."
      }
    },
    {
      "data": {
        "id": "1996_overschee_subspace_identification_for_linear",
        "label": "Overschee et al. 1996",
        "title": "Subspace Identification for Linear Systems: Theory, Implementation, Applications",
        "authors": [
          "Overschee",
          "Moor"
        ],
        "year": 1996,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "System identification",
          "Subspace identification",
          "Subspace methods",
          "Linear systems",
          "State space models"
        ],
        "summary": "Reference textbook covering the theory, numerical implementation, and applications of subspace identification methods (N4SID, MOESP, CVA) for identifying linear state-space models from input-output data."
      }
    },
    {
      "data": {
        "id": "1997_scheuer_continuous_curvature_path_planning",
        "label": "SCC-Paths",
        "title": "Continuous-Curvature Path Planning for Car-Like Vehicles",
        "authors": [
          "Scheuer",
          "Fraichard"
        ],
        "year": 1997,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Path planning",
          "Continuous curvature",
          "Clothoid",
          "Nonholonomic systems",
          "Mobile robotics"
        ],
        "summary": "Simple Continuous Curvature (SSC) paths are composed of line segments, maximum-curvature circular arcs, and clothoid arcs, which guarantee both continuous curvature and bounded curvature derivative for car-like vehicles."
      }
    },
    {
      "data": {
        "id": "1998_lavalle_rapidly_exploring_random_trees",
        "label": "RRT",
        "title": "Rapidly-exploring Random Trees: A New Tool for Path Planning",
        "authors": [
          "LaValle"
        ],
        "year": 1998,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Path planning",
          "Sampling-based",
          "RRT",
          "Rapidly-exploring random trees"
        ],
        "summary": "Introduces RRTs for sampling-based motion planning in high-dimensional configuration spaces."
      }
    },
    {
      "data": {
        "id": "1998_scokaert_constrained_linear_quadratic_regulation",
        "label": "CLQR",
        "title": "Constrained Linear Quadratic Regulation",
        "authors": [
          "Scokaert",
          "Rawlings"
        ],
        "year": 1998,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Linear quadratic regulation",
          "Constrained optimization",
          "Model predictive control",
          "Stability",
          "Optimal control"
        ],
        "summary": "Formulates constrained LQR as a finite-horizon QP, establishes closed-loop stability under receding-horizon implementation, and characterizes the relationship between the constrained optimal cost and unconstrained LQR performance."
      }
    },
    {
      "data": {
        "id": "1999_lavalle_randomized_kinodynamic_planning",
        "label": "Kinodynamic RRT",
        "title": "Randomized Kinodynamic Planning",
        "authors": [
          "LaValle",
          "James J. Kuffner"
        ],
        "year": 1999,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Motion planning",
          "Kinodynamic planning",
          "Trajectory planning",
          "Sampling-based",
          "RRT"
        ],
        "summary": "Introduces RRTs for sampling-based trajectory planning in high-dimensional configuration spaces."
      }
    },
    {
      "data": {
        "id": "2000_kuffner_rrt_connect_an_efficient",
        "label": "RRT-Connect",
        "title": "RRT-Connect: An Efficient Approach to Single-Query Path Planning",
        "authors": [
          "James J. Kuffner",
          "LaValle"
        ],
        "year": 2000,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Kinodynamic planning",
          "Trajectory planning",
          "Sampling-based",
          "RRT"
        ],
        "summary": "Extends RRT with bidirectional search (two trees, one from start and one from goal)."
      }
    },
    {
      "data": {
        "id": "2000_piazzi_quintic_g2_splines_for",
        "label": "Quintic G2-Spline",
        "title": "Quintic G2-Splines for Trajectory Planning of Autonomous Vehicles",
        "authors": [
          "Piazzi",
          "Bianco"
        ],
        "year": 2000,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Path planning",
          "Motion planning",
          "Splines",
          "G2 continuity",
          "Autonomous vehicles",
          "Nonholonomic systems",
          "Flatness-based control",
          "Differential flatness",
          "Curvature continuity"
        ],
        "summary": "Proposes a steering method for connecting pairs of states in [x, y, yaw, curvature] state space using paths that are quintic polynomials in x, y position coordinates. This leaves four free tuning parameters eta1, eta2, eta3, eta4, which influence the shape of the paths and can be set according to heuristics or can be explicitly optimized, which is investigated in the companion work by the same authors \"Optimal trajectory planning with quintic G2-splines\"."
      }
    },
    {
      "data": {
        "id": "2001_nagy_trajectory_generation_for_car",
        "label": "Cubic Curvature Polynomials",
        "title": "Trajectory Generation for Car-Like Robots Using Cubic Curvature Polynomials",
        "authors": [
          "Nagy",
          "Kelly"
        ],
        "year": 2001,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Path planning",
          "Trajectory generation",
          "Continuous curvature",
          "Nonholonomic systems"
        ],
        "summary": "Proposes a steering method for connecting boundary conditions in (x, y, yaw, curvature) state space with a curve having curvature which is a cubic polynomial of arc length, generalizing simple clothoids. The method for computing the curvature polynomial coefficients is based on an iterative procedure (essentially equivalent to Newton's method) with an informative heuristic initial guess and a residual based on the deviation from the target end state."
      }
    },
    {
      "data": {
        "id": "2004_fraichard_from_reeds_and_shepps",
        "label": "CC Steer",
        "title": "From Reeds and Shepp's to Continuous-Curvature Paths",
        "authors": [
          "Fraichard",
          "Scheuer"
        ],
        "year": 2004,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Path planning",
          "Continuous curvature",
          "Clothoid",
          "Nonholonomic systems"
        ],
        "summary": "CC Steer is a steering algorithm for car-like vehicles that produces paths composed of line segments, circular arcs, and clothoid arcs with continuous curvature and bounded curvature derivative."
      }
    },
    {
      "data": {
        "id": "2004_li_iterative_linear_quadratic_regulator",
        "label": "iLQR",
        "title": "Iterative Linear Quadratic Regulator Design for Nonlinear Biological Movement Systems",
        "authors": [
          "Li",
          "Todorov"
        ],
        "year": 2004,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Iterative linear quadratic regulator",
          "Differential dynamic programming",
          "iLQR",
          "DDP",
          "Nonlinear control"
        ],
        "summary": "Introduces iLQR, applying iterative linearization around the current nominal trajectory to reduce nonlinear trajectory optimization to a sequence of LQR problems, enabling efficient second-order trajectory optimization for nonlinear systems."
      }
    },
    {
      "data": {
        "id": "2007_geraerts_creating_high_quality_paths",
        "label": "Geraerts et al. 2007",
        "title": "Creating High-quality Paths for Motion Planning",
        "authors": [
          "Geraerts",
          "Overmars"
        ],
        "year": 2007,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Path optimization",
          "Path shortcutting",
          "Post-processing"
        ],
        "summary": "Presents path-quality improvement techniques applied as post-processing steps to paths produced by sampling-based planners. One of the clearest early treatments of path shortcutting."
      }
    },
    {
      "data": {
        "id": "2008_rickert_balancing_exploration_and_exploitation",
        "label": "EET",
        "title": "Balancing Exploration and Exploitation in Motion Planning",
        "authors": [
          "Rickert",
          "Brock",
          "Knoll"
        ],
        "year": 2008,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Path planning",
          "Sampling-based",
          "Exploration",
          "Exploitation",
          "Adaptive"
        ],
        "summary": "Introduces exploring/exploiting trees (EET) which first tries to acquire information about the workspace and exploit it (using a potential-field-like approach), then gradually shifts to exploration only as much as needed to alleviate exploitation failures."
      }
    },
    {
      "data": {
        "id": "2008_schmid_dynamic_mode_decomposition_of",
        "label": "DMD",
        "title": "Dynamic Mode Decomposition of Numerical and Experimental Data",
        "authors": [
          "Schmid",
          "Sesterhenn"
        ],
        "year": 2008,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Dynamic mode decomposition",
          "DMD",
          "Fluid dynamics",
          "Data-driven methods",
          "System identification",
          "Model reduction"
        ],
        "summary": "Introduces Dynamic Mode Decomposition (DMD), a data-driven algorithm for creating dynamic models from numerical simulations and experimental data, decomposing the observed trajectory data into modes each associated with a single frequency and growth/decay rate. Naturally allows for model reduction based on quantitative measures of mode importance. Originally proposed for fluid flow data, but relevant much more broadly to any kind of dynamical system, especially those observable with stochastic noise present and those with many states."
      }
    },
    {
      "data": {
        "id": "2008_urmson_autonomous_driving_in_urban",
        "label": "Boss",
        "title": "Autonomous Driving in Urban Environments: Boss and the Urban Challenge",
        "authors": [
          "Urmson",
          "Anhalt",
          "Bagnell"
        ],
        "year": 2008,
        "category": "Motion Planning",
        "sub_category": "Frameworks & Stack Architectures",
        "tags": [
          "Autonomous driving",
          "Urban driving",
          "DARPA Urban Challenge",
          "Behavior planning",
          "Sensor fusion",
          "Autonomous vehicles"
        ],
        "summary": "Describes Boss, the CMU autonomous vehicle that won the 2007 DARPA Urban Challenge. Presents the full software stack for urban driving including perception, behavior planning, and motion planning components that operate in complex traffic scenarios with other vehicles and pedestrians."
      }
    },
    {
      "data": {
        "id": "2009_ratliff_chomp_gradient_optimization_techniques",
        "label": "CHOMP",
        "title": "CHOMP: Gradient Optimization Techniques for Efficient Motion Planning",
        "authors": [
          "Ratliff",
          "Zucker",
          "Bagnell"
        ],
        "year": 2009,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Path planning",
          "Path optimization",
          "Gradient descent",
          "Preconditioned",
          "Obstacle avoidance",
          "Path smoothness",
          "CHOMP"
        ],
        "summary": "CHOMP formulates path optimization as minimizing an objective with terms for obstacle cost and path smoothness, then applies a covariant gradient descent (a special type of preconditioned gradient descent closely related to natural gradient descent) that exploits the special structure of the objective for fast convergence. Widely used via its MoveIt/ROS implementation."
      }
    },
    {
      "data": {
        "id": "2009_verscheure_time_optimal_path_tracking",
        "label": "Verscheure et al. 2009",
        "title": "Time-Optimal Path Tracking for Robots: A Convex Optimization Approach",
        "authors": [
          "Verscheure",
          "Demeulenaere",
          "Swevers"
        ],
        "year": 2009,
        "category": "Motion Planning",
        "sub_category": "Speed Planning",
        "tags": [
          "Speed planning",
          "Path tracking",
          "Path following",
          "Optimal control",
          "Convex optimization",
          "Convexification",
          "Second-order cone program",
          "Constraints"
        ],
        "summary": "Demonstrates how to write down a large optimal control problem (OCP) for time-optimal path tracking for a robotic manipulator, considering many constraints and the dynamics related to such systems. The resulting OCP is a convex second-order cone program, which can be solved with a variety of generic solvers. The value of the paper mostly comes from just the handwritten transcription of the OCP."
      }
    },
    {
      "data": {
        "id": "2010_karaman_optimal_kinodynamic_motion_planning",
        "label": "Kinodynamic RRT*",
        "title": "Optimal Kinodynamic Motion Planning using Incremental Sampling-based Methods",
        "authors": [
          "Karaman",
          "Frazzoli"
        ],
        "year": 2010,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Kinodynamic planning",
          "RRT*",
          "Asymptotic optimality",
          "Differential constraints"
        ],
        "summary": "Extends RRT* to kinodynamic systems with differential constraints, providing sufficient conditions for asymptotic optimality."
      }
    },
    {
      "data": {
        "id": "1105_1186",
        "label": "RRT*",
        "title": "Sampling-based Algorithms for Optimal Motion Planning",
        "authors": [
          "Karaman",
          "Frazzoli"
        ],
        "year": 2011,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Asymptotically optimal",
          "Probabilistically complete",
          "RRT*"
        ],
        "summary": "The main contribution of the paper is the introduction of new algorithms, namely, PRM* and RRT*, which are provably asymptotically optimal, i.e., such that the cost of the returned solution converges almost surely to the optimum. Moreover, it is shown that the computational complexity of the new algorithms is within a constant factor of that of their probabilistically complete (but not asymptotically optimal) counterparts."
      }
    },
    {
      "data": {
        "id": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "label": "STOMP",
        "title": "STOMP: Stochastic Trajectory Optimization for Motion Planning",
        "authors": [
          "Kalakrishnan",
          "Chitta",
          "Theodorou"
        ],
        "year": 2011,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Path planning",
          "Path optimization",
          "Stochastic optimization",
          "Path integral",
          "Sampling",
          "STOMP"
        ],
        "summary": "STOMP improves a trajectory by rolling out a large batch of noisy samples and computing a weighted average (based on a Boltzmann distribution i.e. exponentiated negative with a temperature parameter) over their costs. Effectively a path-space analogue of MPPI. Does not require cost gradients. Noise helps STOMP jiggle out of local minima that CHOMP can get stuck in, a similar mechanism and phenomenon as in general stochastic/perturbed gradient descent (c.f. \"How to Escape Saddle Points Efficiently\" by Jin et al, 2017 https://proceedings.mlr.press/v70/jin17a.html)."
      }
    },
    {
      "data": {
        "id": "2011_karaman_anytime_motion_planning_using",
        "label": "RRT*",
        "title": "Anytime Motion Planning using the RRT*",
        "authors": [
          "Karaman",
          "Walter",
          "Perez"
        ],
        "year": 2011,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Anytime",
          "Asymptotically optimal",
          "Probabilistically complete",
          "RRT*"
        ],
        "summary": "This was a companion to the original RRT* paper, and introduced key innovations for anytime motion planning including the \"committed trajectory\" and a \"branch-and-bound\" technique for periodically pruning obviously suboptimal nodes from the tree."
      }
    },
    {
      "data": {
        "id": "1204_6453",
        "label": "RRT#",
        "title": "The Role of Vertex Consistency in Sampling-based Algorithms for Optimal Motion Planning",
        "authors": [
          "Arslan",
          "Tsiotras"
        ],
        "year": 2013,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Optimal motion planning",
          "Sampling-based planning",
          "Asymptotic optimality",
          "RRT#",
          "RRT*",
          "RRT",
          "RRG",
          "Graph search",
          "Dynamic programming",
          "Vertex consistency",
          "Consistent tree"
        ],
        "summary": "RRT# is based on RRG, just like RRT*, but is aimed at obtaining faster convergence to the optimal cost compared to RRT* by maintaining better estimates of nodal costs. There is also some interesting commentary in Section 5 of the arXiv preprint where the authors discuss the \"relevant region\" as an elliptic region which could be \"used to implement more intelligent sampling strategies\"; it would seem this idea was picked up on and formalized by Gammell et al. in the \"Informed RRT*\" (https://arxiv.org/pdf/1404.2334) paper."
      }
    },
    {
      "data": {
        "id": "1205_5088",
        "label": "Linear Kinodynamic RRT*",
        "title": "Kinodynamic RRT*: Optimal Motion Planning for Systems with Linear Differential Constraints",
        "authors": [
          "Webb",
          "Berg"
        ],
        "year": 2012,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Kinodynamic planning",
          "RRT*",
          "Linear systems",
          "Optimal control",
          "Double integrator"
        ],
        "summary": "Uses a fixed-final-state-free-final-time controller that exactly and optimally connects any pair of states in RRT*, where cost trades off trajectory duration against control effort. Dynamics are restricted to linear (or linearized) systems."
      }
    },
    {
      "data": {
        "id": "1206_4621",
        "label": "PI2-CMA",
        "title": "Path Integral Policy Improvement with Covariance Matrix Adaptation",
        "authors": [
          "Stulp",
          "Sigaud"
        ],
        "year": 2012,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Path integral control",
          "Policy optimization",
          "Reinforcement learning",
          "Covariance matrix adaptation",
          "Exploration noise",
          "Continuous control"
        ],
        "summary": "Shows that PI2, CEM, and CMA-ES all share the concept of probability-weighted averaging for parameter updates, unifying them into a common family. Derives PI2-CMA, which inherits PI2's stochastic optimal control foundations while automatically adapting the exploration noise covariance, eliminating the need to manually tune exploration magnitude."
      }
    },
    {
      "data": {
        "id": "2012_kobilarov_cross_entropy_motion_planning",
        "label": "CEM",
        "title": "Cross-Entropy Motion Planning",
        "authors": [
          "Kobilarov"
        ],
        "year": 2012,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Motion planning",
          "Cross-entropy method",
          "Sampling-based planning",
          "Sampling-based control",
          "Stochastic optimal control"
        ],
        "summary": "Applies the cross-entropy method (CEM) to motion planning, framing trajectory search as a distribution estimation problem where elite samples iteratively refine a sampling distribution toward low-cost trajectories."
      }
    },
    {
      "data": {
        "id": "2012_perez_lqr_rrt_star_optimal",
        "label": "LQR-RRT*",
        "title": "LQR-RRT*: Optimal Sampling-Based Motion Planning with Automatically Derived Extension Heuristics",
        "authors": [
          "Perez",
          "Platt",
          "Konidaris"
        ],
        "year": 2012,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Kinodynamic planning",
          "RRT*",
          "LQR",
          "Steering function",
          "Underactuated systems"
        ],
        "summary": "Uses a linear-quadratic approximation for both the steering function and the cost-to-go extension heuristic in RRT*, automatically deriving these heuristics by locally linearizing system dynamics."
      }
    },
    {
      "data": {
        "id": "2012_tassa_synthesis_and_stabilization_of",
        "label": "iLQR",
        "title": "Synthesis and Stabilization of Complex Behaviors through Online Trajectory Optimization",
        "authors": [
          "Tassa",
          "Erez",
          "Todorov"
        ],
        "year": 2012,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Iterative linear quadratic regulator",
          "Differential dynamic programming",
          "iLQR",
          "DDP",
          "Nonlinear control",
          "Online optimization",
          "Synthesis",
          "Stabilization",
          "Behaviors"
        ],
        "summary": "Refines iLQR with key algorithmic improvements now standard in modern implementations: state Hessian regularization, improved feedforward gain line search, and adaptive regularization scheduling. Clearer presentation than the original Li & Todorov paper."
      }
    },
    {
      "data": {
        "id": "1305_6644",
        "label": "Bertolazzi et al. 2013",
        "title": "Fast and Accurate G1 Fitting of Clothoid Curves",
        "authors": [
          "Bertolazzi",
          "Frego"
        ],
        "year": 2013,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1306_3532",
        "label": "FMT*",
        "title": "Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many Dimensions",
        "authors": [
          "Janson",
          "Schmerling",
          "Clark"
        ],
        "year": 2013,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Optimal motion planning",
          "Sampling-based planning",
          "Asymptotic optimality",
          "Fast marching tree",
          "FMT",
          "FMT*",
          "RRT*",
          "RRT",
          "Graph search",
          "Dynamic programming",
          "Fast marching method"
        ],
        "summary": "FMT* operates on a fundamentally different mechanism than RRT*, yet still achieves asymptotic optimality. FMT* can be faster than RRT* in certain planning regimes, and it is more amenable to parallelization (c.f. Group Marching Tree)."
      }
    },
    {
      "data": {
        "id": "1312_0041",
        "label": "DMD",
        "title": "On Dynamic Mode Decomposition: Theory and Applications",
        "authors": [
          "Tu",
          "Rowley",
          "Luchtenburg"
        ],
        "year": 2013,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Dynamic mode decomposition",
          "DMD",
          "Fluid dynamics",
          "Data-driven methods",
          "Koopman operator"
        ],
        "summary": "Provides rigorous theoretical foundations for DMD, introduces the exact DMD formulation with improved numerical accuracy, and analyzes convergence properties and connections to Koopman spectral analysis."
      }
    },
    {
      "data": {
        "id": "2013_lipp_minimum_time_speed_optimisation_over",
        "label": "Lipp et al. 2013",
        "title": "Minimum-time speed optimisation over a fixed path",
        "authors": [
          "Lipp",
          "Boyd"
        ],
        "year": 2013,
        "category": "Motion Planning",
        "sub_category": "Speed Planning",
        "tags": [
          "Speed planning",
          "Convex optimization",
          "Minimum time",
          "Trajectory optimization"
        ],
        "summary": "Formulates minimum-time speed planning along a fixed geometric path as a convex optimization problem."
      }
    },
    {
      "data": {
        "id": "2013_luna_anytime_solution_optimization_for",
        "label": "Luna et al. 2013",
        "title": "Anytime Solution Optimization for Sampling-Based Motion Planning",
        "authors": [
          "Luna",
          "Şucan",
          "Moll"
        ],
        "year": 2013,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Path optimization",
          "Path shortcutting",
          "Anytime planning",
          "Sampling-based planning",
          "Post-processing"
        ],
        "summary": "Anytime algorithm that progressively improves path quality after an initial solution is found, combining random shortcutting with path hybridization. Algorithm 1 gives a particularly clear presentation of the shortcutting procedure."
      }
    },
    {
      "data": {
        "id": "2013_palamakumburu_minimum_jerk_trajectory_generation",
        "label": "Palamakumbura et al. 2013",
        "title": "Minimum Jerk Trajectory Generation for Differential Wheeled Mobile Robots",
        "authors": [
          "Palamakumbura",
          "Maithripala",
          "Martin"
        ],
        "year": 2013,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory generation",
          "Minimum jerk",
          "Differential drive",
          "Mobile robots",
          "Smooth trajectories"
        ],
        "summary": "Proposes a minimum jerk trajectory generation method for differential wheeled mobile robots, based on solving a finite-dimensional unconstrained nonlinear optimization problem."
      }
    },
    {
      "data": {
        "id": "2013_yang_spline_based_rrt_path",
        "label": "Spline-based RRT",
        "title": "Spline-Based RRT Path Planner for Non-Holonomic Robots",
        "authors": [
          "Yang",
          "Moon",
          "Yoo"
        ],
        "year": 2013,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Path planning",
          "RRT",
          "Splines",
          "Non-holonomic robots",
          "Smooth paths",
          "Curvature"
        ],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1401_7625",
        "label": "Mokhtari et al. 2014",
        "title": "RES: Regularized Stochastic BFGS Algorithm",
        "authors": [
          "Mokhtari",
          "Ribeiro"
        ],
        "year": 2014,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1404_2334",
        "label": "Informed RRT*",
        "title": "Informed RRT*: Optimal Sampling-based Path Planning Focused via Direct Sampling of an Admissible Ellipsoidal Heuristic",
        "authors": [
          "Gammell",
          "Srinivasa",
          "Barfoot"
        ],
        "year": 2014,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Sampling-based planning",
          "Asymptotic optimality",
          "Informed RRT*",
          "RRT*",
          "Heuristic search",
          "Informed set"
        ],
        "summary": "Informed RRT* accelerates convergence of RRT* by restricting sampling to the prolate hyperspheroid (ellipsoidal) subset of the state space that can possibly improve the current best solution, rather than sampling the entire domain. This focused sampling preserves RRT*'s probabilistic completeness and asymptotic optimality guarantees while significantly improving convergence rate and final solution quality, especially in high-dimensional spaces or large environments. However, the ellipsoidal region is only valid for path planning where the cost is the Euclidean path length; for other costs or kindodynamic planning the informed set has some other geometry that is not generally known to be computable in closed form."
      }
    },
    {
      "data": {
        "id": "1405_5848",
        "label": "BIT*",
        "title": "Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs",
        "authors": [
          "Gammell",
          "Srinivasa",
          "Barfoot"
        ],
        "year": 2014,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Sampling-based planning",
          "Asymptotic optimality",
          "Anytime planning",
          "Heuristic search",
          "Random geometric graphs",
          "Graph search",
          "Informed sampling"
        ],
        "summary": "BIT* unifies graph- and sampling-based planning by treating a batch of random samples as an implicit random geometric graph (RGG) and searching it with an A*/LPA*-style ordered search focused on the informed ellipsoidal subset of states that can improve the current solution. Successive batches of increasing density are searched while reusing prior information, yielding a probabilistically complete, asymptotically optimal anytime planner that converges substantially faster than RRT* and FMT*, especially in high-dimensional spaces."
      }
    },
    {
      "data": {
        "id": "1406_1078",
        "label": "Cho et al. 2014",
        "title": "Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation\n",
        "authors": [
          "Cho",
          "Merrienboer",
          "Gulcehre"
        ],
        "year": 2014,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1407_0414",
        "label": "Toussaint 2014",
        "title": "Newton methods for k-order Markov Constrained Motion Problems",
        "authors": [
          "Toussaint"
        ],
        "year": 2014,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1407_2896",
        "label": "SST*",
        "title": "Asymptotically Optimal Sampling-based Kinodynamic Planning",
        "authors": [
          "Li",
          "Littlefield",
          "Bekris"
        ],
        "year": 2014,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Kinodynamic planning",
          "Asymptotic optimality",
          "BVP-free",
          "Sparse tree",
          "SST"
        ],
        "summary": "SST is a kinodynamic planner that requires no 2-point BVP solver or steering function, instead relying solely on forward propagation of control actions while maintaining a sparse sample set for computational efficiency."
      }
    },
    {
      "data": {
        "id": "1408_4408",
        "label": "eDMD",
        "title": "A Data-Driven Approximation of the Koopman Operator: Extending Dynamic Mode Decomposition",
        "authors": [
          "Williams",
          "Kevrekidis",
          "Rowley"
        ],
        "year": 2014,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Koopman operator",
          "Dynamic mode decomposition",
          "Extended DMD",
          "Data-driven methods",
          "Nonlinear systems"
        ],
        "summary": "Extends DMD to nonlinear systems by lifting states into a function space (RKHS), yielding a data-driven approximation of the infinite-dimensional Koopman operator and enabling nonlinear system analysis via linear tools."
      }
    },
    {
      "data": {
        "id": "1409_6358",
        "label": "DMDc",
        "title": "Dynamic Mode Decomposition with Control",
        "authors": [
          "Proctor",
          "Brunton",
          "Kutz"
        ],
        "year": 2014,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Dynamic mode decomposition",
          "DMDc",
          "System identification",
          "Control systems",
          "Data-driven methods"
        ],
        "summary": "Extends DMD to systems with exogenous control inputs, enabling separate identification of the state transition matrix and control influence matrix from input-output data, making DMD applicable to controlled dynamical systems."
      }
    },
    {
      "data": {
        "id": "1411_4045",
        "label": "AVP",
        "title": "Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots",
        "authors": [
          "Pham",
          "Caron",
          "Lertkultanon"
        ],
        "year": 2014,
        "category": "Motion Planning",
        "sub_category": "Speed Planning",
        "tags": [
          "Kinodynamic planning",
          "Path-velocity decomposition",
          "Quasi-static planning",
          "Velocity propagation",
          "Dynamic motions"
        ],
        "summary": "Starting point is quasi-static (velocity ~= 0) path planning. Then augments state space with velocity and uses propagation of velocity using kinodynamics to determine the reachable set (admissible interval) of velocity, and includes that in the connection check for new nodes. Builds on the foundational TOPP velocity planner (Bobrow 1985, DOI: 10.1177/027836498500400301). AVP is modularly (re)usable in many sampling-based planners; the authors give a concrete instantiation and numerical experiments with AVP-RRT."
      }
    },
    {
      "data": {
        "id": "2014_lefevre_a_survey_on_motion",
        "label": "Lefèvre et al. 2014",
        "title": "A Survey On Motion Prediction and Risk Assessment for Intelligent Vehicles",
        "authors": [
          "Lefèvre",
          "Vasquez",
          "Laugier"
        ],
        "year": 2014,
        "category": "Motion Prediction",
        "sub_category": null,
        "tags": [
          "Motion prediction",
          "Risk assessment",
          "Intelligent vehicles",
          "Survey",
          "Physics-based prediction",
          "Maneuver-based prediction",
          "Interaction-aware prediction"
        ],
        "summary": "Surveys motion prediction and risk assessment methods for intelligent vehicles, organizing approaches into three categories - physics-based, maneuver-based, and interaction-aware - and reviewing how predicted trajectories are used to compute collision risk for safety applications."
      }
    },
    {
      "data": {
        "id": "2014_luo_an_empirical_study_of",
        "label": "Luo et al. 2014",
        "title": "An Empirical Study of Optimal Motion Planning",
        "authors": [
          "Luo",
          "Hauser"
        ],
        "year": 2014,
        "category": "Motion Planning",
        "sub_category": "Surveys & Comparative Studies",
        "tags": [
          "Survey",
          "Benchmarking",
          "Motion planning",
          "Robot motion planning",
          "Sampling-based planning",
          "Optimal motion planning"
        ],
        "summary": "Benchmarks several categories of optimal motion planners (sampling-based, grid-based, and trajectory optimization) on synthetic problems varying in dimensionality, number of homotopy classes, and passage geometry, providing empirical guidance on planner selection."
      }
    },
    {
      "data": {
        "id": "2014_pan_probabilistic_differential_dynamic_programming",
        "label": "PDDP",
        "title": "Probabilistic Differential Dynamic Programming",
        "authors": [
          "Pan",
          "Theodorou"
        ],
        "year": 2014,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Differential dynamic programming",
          "DDP",
          "Probabilistic differential dynamic programming",
          "PDDP",
          "Probabilistic methods",
          "Learning",
          "Uncertainty"
        ],
        "summary": "Extends DDP to handle probabilistic dynamics models, propagating uncertainty through the backward and forward passes to produce trajectories that are robust to model uncertainty and compatible with learned probabilistic dynamics."
      }
    },
    {
      "data": {
        "id": "1502_04269",
        "label": "Ustun et al. 2015",
        "title": "Supersparse Linear Integer Models for Optimized Medical Scoring Systems",
        "authors": [
          "Ustun",
          "Rudin"
        ],
        "year": 2015,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1502_05477",
        "label": "TRPO",
        "title": "Trust Region Policy Optimization",
        "authors": [
          "Schulman",
          "Levine",
          "Moritz"
        ],
        "year": 2015,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Reinforcement learning",
          "Policy optimization",
          "Trust region methods",
          "Continuous control"
        ],
        "summary": "Introduces TRPO, which guarantees monotonic policy improvement by constraining each update to a KL-divergence trust region. Enables stable training on complex continuous control tasks without manual learning rate tuning."
      }
    },
    {
      "data": {
        "id": "1503_05671",
        "label": "Martens et al. 2015",
        "title": "Optimizing Neural Networks with Kronecker-factored Approximate Curvature",
        "authors": [
          "Martens",
          "Grosse"
        ],
        "year": 2015,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1505_04098",
        "label": "AO-x",
        "title": "Asymptotically Optimal Planning by Feasible Kinodynamic Planning in State-Cost Space",
        "authors": [
          "Hauser",
          "Zhou"
        ],
        "year": 2015,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Kinodynamic planning",
          "Asymptotic optimality",
          "Meta algorithm"
        ],
        "summary": "AO-x meta-algorithm turns any feasible kinodynamic planner into an asymptotically optimal planner by lifting planning into a state-cost space."
      }
    },
    {
      "data": {
        "id": "1505_04597",
        "label": "Ronneberger et al. 2015",
        "title": "U-Net: Convolutional Networks for Biomedical Image Segmentation",
        "authors": [
          "Ronneberger",
          "Fischer",
          "Brox"
        ],
        "year": 2015,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1506_01085",
        "label": "CES",
        "title": "A Convex Optimization Approach to Smooth Trajectories for Motion Planning with Car-Like Robots\n",
        "authors": [
          "Zhu",
          "Schmerling",
          "Pavone"
        ],
        "year": 2015,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Smooth trajectory",
          "Car-like",
          "Optimization",
          "Heuristic",
          "Optimal",
          "Real-time",
          "Smoothing",
          "Path planning",
          "Convex optimization",
          "Self-driving",
          "Bicycle Model",
          "Bubble",
          "Ground vehicles",
          "Collision-free",
          "Vehicle dynamics",
          "Speed profile"
        ],
        "summary": "CES takes a reference trajectory as input, then re-plans both the path shape and speed profile within a sequence of obstacle-free \"bubble\" regions along the trajectory using convex programming. This makes it a powerful post-processor, reportedly outperforming traditional path shortcutting heuristics as well as elastic band approaches."
      }
    },
    {
      "data": {
        "id": "1507_08752",
        "label": "Shamir 2015",
        "title": "An Optimal Algorithm for Bandit and Zero-Order Convex Optimization with Two-Point Feedback\n",
        "authors": [
          "Shamir"
        ],
        "year": 2015,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1509_01149",
        "label": "Williams et al. 2015",
        "title": "Model Predictive Path Integral Control using Covariance Variable Importance Sampling\n",
        "authors": [
          "Williams",
          "Aldrich",
          "Theodorou"
        ],
        "year": 2015,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [],
        "summary": "Folds importance sampling into the cost function in order to address the practical issue of infrequent selection of low-cost trajectories under naive sampling of actions on the uncontrolled system, which is a known drawback of MPPI. Also discusses implementation of MPPI on a GPU for massively parallel sampling. Includes a clear description of MPPI in Algorithm 1."
      }
    },
    {
      "data": {
        "id": "1509_03580",
        "label": "SINDy",
        "title": "Discovering Governing Equations from Data: Sparse Identification of Nonlinear Dynamical Systems",
        "authors": [
          "Brunton",
          "Proctor",
          "Kutz"
        ],
        "year": 2015,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "System identification",
          "Sparse regression",
          "SINDy",
          "Nonlinear dynamics",
          "Data-driven methods"
        ],
        "summary": "Introduces SINDy, which applies sparse nonlinear least squares regression over a library of candidate nonlinear functions to identify parsimonious governing equations from trajectory data, recovering interpretable symbolic expressions for nonlinear dynamical systems."
      }
    },
    {
      "data": {
        "id": "1511_05259",
        "label": "Caron et al. 2015",
        "title": "Completeness of Randomized Kinodynamic Planners with State-based Steering",
        "authors": [
          "Caron",
          "Pham",
          "Nakamura"
        ],
        "year": 2015,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Kinodynamic planning",
          "Probabilistic completeness",
          "State-based steering",
          "Steering function",
          "Interpolation"
        ],
        "summary": "Proves probabilistic completeness for state-based (interpolating) kinodynamic planners under verifiable assumptions. Identifies second-order continuity as the key design requirement. Nice explanation of state-based steering and its beneficial properties as compraed with e.g. randomized action-propagation steering. Contains a great Section 2.3 on the differences between categories of steering functions."
      }
    },
    {
      "data": {
        "id": "2015_klemm_rrt_star_connect_faster",
        "label": "RRT*-Connect",
        "title": "RRT*-Connect: Faster, Asymptotically Optimal Motion Planning",
        "authors": [
          "Klemm",
          "Oberländer",
          "Hermann"
        ],
        "year": 2015,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Sampling-based planning",
          "Asymptotic optimality",
          "Bidirectional search",
          "RRT*",
          "RRT-Connect"
        ],
        "summary": "RRT*-Connect merges the bidirectional search strategy of RRT-Connect with the asymptotic optimality guarantees of RRT*, growing two trees simultaneously from start and goal and connecting them greedily while rewiring for cost minimization. The result finds initial solutions significantly faster than RRT* while still converging toward the optimal path, combining the speed advantage of bidirectional search with provable optimality guarantees."
      }
    },
    {
      "data": {
        "id": "2015_otte_rrtx_asymptotically_optimal_single",
        "label": "RRTX",
        "title": "RRTX: Asymptotically Optimal Single-Query Sampling-Based Motion Planning with Quick Replanning",
        "authors": [
          "Otte",
          "Frazzoli"
        ],
        "year": 2016,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Sampling-based planning",
          "Asymptotic optimality",
          "Dynamic environments",
          "Replanning",
          "RRTX",
          "RRT*",
          "Graph search"
        ],
        "summary": "Same asymptotic optimality and probabilistically complete properties as RRT*, but can handle reactions to suddenly-appearing obstacles."
      }
    },
    {
      "data": {
        "id": "2015_palmieri_distance_metric_learning_for",
        "label": "Palmieri et al. 2015",
        "title": "Distance Metric Learning for RRT-Based Motion Planning with Constant-Time Inference",
        "authors": [
          "Palmieri",
          "Arras"
        ],
        "year": 2015,
        "category": "Motion Planning",
        "sub_category": "Machine Learning in Motion Planning",
        "tags": [
          "Motion planning",
          "Trajectory planning",
          "Kinodynamic planning",
          "Sampling-based planning",
          "RRT",
          "Distance metric learning",
          "Machine learning",
          "Inference"
        ],
        "summary": "Trains a supervised model to approximate the kinodynamic steering distance for RRT-based planners. The motivation is purely for increasing performance in terms of reducing average and worst-case runtime latency; assumes we have a slow-to-compute ground truth perfect steering function used to generate training data. The features are a set of 14 hand-crafted and cheap-to-evaluate metrics, and the labels are a scalar ground truth cost. The learned model is a basis function model (BFM) using quadratic basis functions and trained using Levenberg-Marquadt. The model architecture was selected as the best (in terms of prediction quality and inference runtime latency) out of a ranking comparison against other architectures trained on the same data, including a small neural network, random forest, support vector machine with radial basis function kernel, and locally weighted projection."
      }
    },
    {
      "data": {
        "id": "1602_04915",
        "label": "Lee et al. 2016",
        "title": "Gradient Descent Converges to Minimizers",
        "authors": [
          "Lee",
          "Simchowitz",
          "Jordan"
        ],
        "year": 2016,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1603_00943",
        "label": "Diamond et al. 2016",
        "title": "CVXPY: A Python-Embedded Modeling Language for Convex Optimization",
        "authors": [
          "Diamond",
          "Boyd"
        ],
        "year": 2016,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1604_02639",
        "label": "Shen et al. 2016",
        "title": "Disciplined Convex-Concave Programming",
        "authors": [
          "Shen",
          "Diamond",
          "Gu"
        ],
        "year": 2016,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1604_07446",
        "label": "Paden et al. 2016",
        "title": "A Survey of Motion Planning and Control Techniques for Self-Driving Urban Vehicles",
        "authors": [
          "Paden",
          "Čáp",
          "Yong"
        ],
        "year": 2016,
        "category": "Motion Planning",
        "sub_category": "Surveys & Comparative Studies",
        "tags": [
          "Survey",
          "Motion planning",
          "Path planning",
          "Trajectory planning",
          "Autonomous vehicles",
          "Self-driving vehicles",
          "Urban driving",
          "Control",
          "Architecture",
          "System",
          "Hierarchy",
          "Modeling",
          "Kinematic model",
          "Dynamic model",
          "Variational methods",
          "Graph search"
        ],
        "summary": "Surveys motion planning and control algorithms for self-driving urban vehicles, reviewing methods from route planning through behavior and motion planning to feedback control, with comparative analysis of vehicle models, environmental assumptions, and computational demands."
      }
    },
    {
      "data": {
        "id": "1606_05225",
        "label": "Cohen et al. 2016",
        "title": "Geometric Median in Nearly Linear Time",
        "authors": [
          "Cohen",
          "Lee",
          "Miller"
        ],
        "year": 2016,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1612_05628",
        "label": "Asadi et al. 2016",
        "title": "An Alternative Softmax Operator for Reinforcement Learning",
        "authors": [
          "Asadi",
          "Littman"
        ],
        "year": 2016,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2016_choudhury_regionally_accelerated_batch_informed",
        "label": "RABIT*",
        "title": "Regionally Accelerated Batch Informed Trees (RABIT*): A Framework to Integrate Local Information into Optimal Path Planning",
        "authors": [
          "Choudhury",
          "Gammell",
          "Barfoot"
        ],
        "year": 2016,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Sampling-based planning",
          "Asymptotic optimality",
          "Anytime planning",
          "RABIT*",
          "BIT*",
          "Hybrid planning",
          "Local optimization"
        ],
        "summary": "RABIT* extends BIT* by hybridizing its global informed search with local gradient-based optimization (e.g. CHOMP). Rather than optimizing every edge, it selectively applies local optimization only to the subset of edges within the current informed set that are most likely to improve the solution, avoiding infeasible edges by finding alternative connections. This preserves asymptotic optimality while significantly accelerating convergence, particularly in problems with difficult-to-sample homotopy classes or narrow passages."
      }
    },
    {
      "data": {
        "id": "2016_rajamaki_sampled_differential_dynamic_programming",
        "label": "SaDDP",
        "title": "Sampled Differential Dynamic Programming",
        "authors": [
          "Rajamäki",
          "Naderi",
          "Kyrki"
        ],
        "year": 2016,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Differential dynamic programming",
          "Sampled differential dynamic programming",
          "Sampling-based control",
          "Sampling-based planning",
          "Hessian-free optimization",
          "Path integral control",
          "Evolution strategies",
          "CMA-ES",
          "Taylor expansion",
          "Gradient-based"
        ],
        "summary": "Combines DDP and path integral control by estimating the DDP Hessian via zero-order sampling rather than analytical differentiation, yielding a trajectory optimizer that blends the structure and efficiency of DDP with the robustness and simplicity of sampling-based methods. Think of it as Hessian-Free optimization (using a zero-order oracle to estimate the Hessian c.f. \"Deep Learning via Hessian-free Optimization\" by James Martens, 2010) specialized to trajectory optimization problems."
      }
    },
    {
      "data": {
        "id": "1703_03864",
        "label": "Salimans et al. 2017",
        "title": "Evolution Strategies as a Scalable Alternative to Reinforcement Learning",
        "authors": [
          "Salimans",
          "Ho",
          "Chen"
        ],
        "year": 2017,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1704_07911",
        "label": "Bojarski et al. 2017",
        "title": "Explaining How a Deep Neural Network Trained with End-to-End Learning Steers a Car\n",
        "authors": [
          "Bojarski",
          "Yeres",
          "Choromanska"
        ],
        "year": 2017,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1705_02403",
        "label": "GMT*",
        "title": "Group Marching Tree: Sampling-Based Approximately Optimal Motion Planning on GPUs",
        "authors": [
          "Ichter",
          "Schmerling",
          "Pavone"
        ],
        "year": 2017,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Kinodynamic planning",
          "Sampling-based planning",
          "Real-time planning",
          "Approximate optimality",
          "GPU",
          "Parallelized",
          "GMT*",
          "FMT*"
        ],
        "summary": "GMT* adapts FMT*'s lazy dynamic-programming tree expansion for massively parallel execution on GPUs by replacing the sequential expansion of the single minimum-cost sample with simultaneous expansion of the entire group of active samples whose cost falls below an increasing threshold. This group approximation introduces a bounded suboptimality constant but eliminates sequential data structures and reduces thread divergence. Achieves ~10 ms planning on desktop GPUs and ~30 ms on embedded GPUs."
      }
    },
    {
      "data": {
        "id": "1706_03762",
        "label": "Transformer",
        "title": "Attention Is All You Need",
        "authors": [
          "Vaswani",
          "Shazeer",
          "Parmar"
        ],
        "year": 2017,
        "category": "Machine Learning",
        "sub_category": null,
        "tags": [
          "Transformers",
          "NLP",
          "Deep learning"
        ],
        "summary": "The paper introduces the Transformer architecture, a novel neural network model based on attention mechanisms, demonstrating state-of-the-art performance on NLP tasks."
      }
    },
    {
      "data": {
        "id": "1707_01146",
        "label": "Kaiser et al. 2017",
        "title": "Data-driven discovery of Koopman eigenfunctions for control",
        "authors": [
          "Kaiser",
          "Kutz",
          "Brunton"
        ],
        "year": 2017,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1707_02342",
        "label": "Williams et al. 2017",
        "title": "Information Theoretic Model Predictive Control: Theory and Applications to Autonomous Driving\n",
        "authors": [
          "Williams",
          "Drews",
          "Goldfain"
        ],
        "year": 2017,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1707_06347",
        "label": "PPO",
        "title": "Proximal Policy Optimization Algorithms",
        "authors": [
          "Schulman",
          "Wolski",
          "Dhariwal"
        ],
        "year": 2017,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Reinforcement learning",
          "Policy optimization",
          "Proximal policy optimization",
          "Continuous control"
        ],
        "summary": "Introduces PPO, which approximates TRPO's trust region constraint via a clipped surrogate objective. Achieves comparable stability and sample efficiency to TRPO with far lower computational overhead. Became the de facto standard RL algorithm quickly over the next decade after introduction."
      }
    },
    {
      "data": {
        "id": "1707_07239",
        "label": "TOPP-RA",
        "title": "A New Approach to Time-Optimal Path Parameterization based on Reachability Analysis",
        "authors": [
          "Pham",
          "Pham"
        ],
        "year": 2017,
        "category": "Motion Planning",
        "sub_category": "Speed Planning",
        "tags": [
          "Time-optimal",
          "Speed planning",
          "Reachability"
        ],
        "summary": "Reframes TOPP as a reachability problem, propagating feasible velocity sets via small LPs, so you get the speed of numerical integration and the robustness of convex optimization in one easy-to-implement algorithm. Claims to (at least partially) generalize AVP (1411.4045)."
      }
    },
    {
      "data": {
        "id": "1708_06056",
        "label": "Paulin et al. 2017",
        "title": "Integrating asymptotically-optimal path planning with local optimization",
        "authors": [
          "Paulin",
          "Botterill",
          "Chen"
        ],
        "year": 2017,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1709_05401",
        "label": "Liu et al. 2017",
        "title": "Search-based Motion Planning for Quadrotors using Linear Quadratic Minimum Time Control\n",
        "authors": [
          "Liu",
          "Atanasov",
          "Mohta"
        ],
        "year": 2017,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1709_05448",
        "label": "Ichter et al. 2017",
        "title": "Learning Sampling Distributions for Robot Motion Planning",
        "authors": [
          "Ichter",
          "Harrison",
          "Pavone"
        ],
        "year": 2017,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1709_07174",
        "label": "Pan et al. 2017",
        "title": "Agile Autonomous Driving using End-to-End Deep Imitation Learning",
        "authors": [
          "Pan",
          "Cheng",
          "Saigol"
        ],
        "year": 2017,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Imitation learning",
          "End-to-end learning",
          "Reinforcement learning",
          "Deep learning",
          "End-to-end",
          "Trajectory optimization",
          "Autonomous driving",
          "DDP",
          "Model-based"
        ],
        "summary": "Uses a \"traditional\" autonomy stack (trajectory optimization with learned dynamics, Kalman filter state estimation, and an handcrafted cost function) as the expert policy, then trains a neural network to imitate it end-to-end, from pixels to torques. Demonstrates that a full autonomy stack can be \"compressed into\" or \"represented by\" a single neural network. Notably, the trained neural network can be deployed with less expensive compute hardware and a lower fidelty sensor suite than the original autonomy stack."
      }
    },
    {
      "data": {
        "id": "1709_07610",
        "label": "Varricchio et al. 2017",
        "title": "Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints\n",
        "authors": [
          "Varricchio",
          "Paden",
          "Yershov"
        ],
        "year": 2017,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1710_09483",
        "label": "Schmerling et al. 2017",
        "title": "Multimodal Probabilistic Model-Based Planning for Human-Robot Interaction",
        "authors": [
          "Schmerling",
          "Leung",
          "Vollprecht"
        ],
        "year": 2017,
        "category": "Motion Planning",
        "sub_category": "Interaction-aware Planning",
        "tags": [
          "Multimodal",
          "Probabilistic",
          "Motion planning",
          "Interaction-aware",
          "Human",
          "Robot",
          "Model-based"
        ],
        "summary": "The paper puts together a few cool technologies, such as massively parallel trajectory sampling and evaluation on a GPU, as well as a CVAE neural network trained on actual human driving data for prediction of future driver response at robot inference time."
      }
    },
    {
      "data": {
        "id": "1710_10122",
        "label": "RRT-CoLearn",
        "title": "RRT-CoLearn: towards kinodynamic planning without numerical trajectory optimization",
        "authors": [
          "Wolfslag",
          "Bharatheesha",
          "Moerland"
        ],
        "year": 2017,
        "category": "Motion Planning",
        "sub_category": "Machine Learning in Motion Planning",
        "tags": [
          "Sampling-based",
          "Sampling-based planning",
          "Kinodynamic",
          "Kinodynamic planning",
          "Motion planning"
        ],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1711_03449",
        "label": "OBCA",
        "title": "Optimization-Based Collision Avoidance",
        "authors": [
          "Zhang",
          "Liniger",
          "Borrelli"
        ],
        "year": 2017,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Collision avoidance",
          "Trajectory optimization",
          "Autonomous vehicles",
          "Nonlinear optimization",
          "Augmented Lagrangian"
        ],
        "summary": "Presents an optimization-based collision avoidance formulation using differentiable signed distance functions. Optimization problems are solved with general nonlinear solver IPOPT. Proposes using A* for warm-starting."
      }
    },
    {
      "data": {
        "id": "1711_05501",
        "label": "Kaiser et al. 2017",
        "title": "Sparse identification of nonlinear dynamics for model predictive control in the low-data limit\n",
        "authors": [
          "Kaiser",
          "Kutz",
          "Brunton"
        ],
        "year": 2017,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1711_06178",
        "label": "Wu et al. 2017",
        "title": "Beyond Sparsity: Tree Regularization of Deep Models for Interpretability",
        "authors": [
          "Wu",
          "Hughes",
          "Parbhoo"
        ],
        "year": 2017,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1711_11006",
        "label": "iLQR-GNMS",
        "title": "A Family of Iterative Gauss-Newton Shooting Methods for Nonlinear Optimal Control",
        "authors": [
          "Giftthaler",
          "Neunert",
          "Stäuble"
        ],
        "year": 2017,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Multiple shooting",
          "Gauss-Newton methods",
          "Nonlinear optimal control",
          "Iterative linear quadratic regulator",
          "iLQR"
        ],
        "summary": "Presents a unified family of iterative Gauss-Newton multiple-shooting methods for nonlinear optimal control, covering single and multiple shooting variants within a common framework with analysis of convergence and computational tradeoffs."
      }
    },
    {
      "data": {
        "id": "2017_roesmann_kinodynamic_trajectory_optimization_and",
        "label": "TEB",
        "title": "Kinodynamic Trajectory Optimization and Control for Car-Like Robots",
        "authors": [
          "Rösmann",
          "Hoffmann",
          "Bertram"
        ],
        "year": 2017,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Timed Elastic Band",
          "Kinodynamic planning",
          "Car-like robots",
          "Motion planning",
          "Autonomous driving"
        ],
        "summary": "Extends the Timed Elastic Band (TEB) local planner to handle kinodynamic constraints for car-like (Ackermann-steered) robots. Optimizes trajectories over time-parameterized elastic bands subject to nonholonomic constraints, enabling smooth and feasible path following for vehicles with curvature limitations."
      }
    },
    {
      "data": {
        "id": "2017_williams_model_predictive_path_integral",
        "label": "MPPI",
        "title": "Model Predictive Path Integral Control: From Theory to Parallel Computation",
        "authors": [
          "Williams",
          "Aldrich",
          "Theodorou"
        ],
        "year": 2017,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Model predictive path integral control",
          "MPPI",
          "Trajectory optimization",
          "Sampling-based control",
          "Stochastic optimal control",
          "GPU parallelization",
          "Autonomous driving"
        ],
        "summary": "Tutorial paper introducing MPPI as a sampling-based model predictive control method, deriving it from path integral control theory and demonstrating a GPU-parallelized implementation for real-time autonomous driving."
      }
    },
    {
      "data": {
        "id": "1801_08995",
        "label": "Sharpness Continuous Path",
        "title": "Trajectory Generation using Sharpness Continuous Dubins-like Paths with Applications in Control of Heavy Duty Vehicles",
        "authors": [
          "Oliveira",
          "Lima",
          "Cirillo"
        ],
        "year": 2018,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Path generation",
          "Dubins",
          "Curvature continuity",
          "Sharpness",
          "Trajectory generation",
          "Heavy vehicles",
          "Autonomous driving",
          "Steering constraints"
        ],
        "summary": "Proposes sharpness-continuous (G3) path primitives composed of cubic curvature curves, circular arcs, and straight lines. Closely related to and builds upon ”Trajectory generation for car-like robots using cubic curvature polynomials” by Nagy and Kelly (2001) and ”From Reeds and Shepp's to continuous-curvature paths” by Fraichard and Scheuer (2004)."
      }
    },
    {
      "data": {
        "id": "1802_09767",
        "label": "Terzi et al. 2018",
        "title": "On multi-step prediction models for receding horizon control",
        "authors": [
          "Terzi",
          "Fagiano",
          "Farina"
        ],
        "year": 2018,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1803_07055",
        "label": "ARS",
        "title": "Simple Random Search Provides a Competitive Approach to Reinforcement Learning",
        "authors": [
          "Mania",
          "Guy",
          "Recht"
        ],
        "year": 2018,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Reinforcement learning",
          "Random search",
          "Evolution strategies",
          "Policy optimization",
          "Continuous control",
          "Baseline",
          "Evaluation"
        ],
        "summary": "Describes Basic Random Search (BRS) and Augmented Random Search (ARS) and demonstrates that simple random perturbations to the parameters of linear policies with state normalization achieves competitive performance against deep RL on MuJoCo benchmarks. Challenges the necessity of more complicated neural network-backed policy optimization algorithms such as Trust Region Policy Optimization (TRPO), Deep Deterministic Policy Gradient (DDPG), Natural Gradients (NG), Evolution Strategies (ES), Proximal Policy Optimization (PPO), Soft Actor Critic (SAC), Soft Q-Learning (SQL), A2C, and the Cross Entropy Method (CEM)."
      }
    },
    {
      "data": {
        "id": "1804_09893",
        "label": "Avron et al. 2018",
        "title": "Random Fourier Features for Kernel Ridge Regression: Approximation Bounds and Statistical Guarantees\n",
        "authors": [
          "Avron",
          "Kapralov",
          "Musco"
        ],
        "year": 2018,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1806_06655",
        "label": "Wensing et al. 2018",
        "title": "Beyond Convexity -- Contraction and Global Convergence of Gradient Descent",
        "authors": [
          "Wensing",
          "Slotine"
        ],
        "year": 2018,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1806_09460",
        "label": "Recht 2018",
        "title": "A Tour of Reinforcement Learning: The View from Continuous Control",
        "authors": [
          "Recht"
        ],
        "year": 2018,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1808_00177",
        "label": "OpenAI et al. 2018",
        "title": "Learning Dexterous In-Hand Manipulation",
        "authors": [
          "OpenAI",
          "Andrychowicz",
          "Baker"
        ],
        "year": 2018,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1809_02399",
        "label": "RRT*_MotionPrimitives",
        "title": "Sampling-based Optimal Kinodynamic Planning with Motion Primitives",
        "authors": [
          "Sakcak",
          "Bascetta",
          "Ferretti"
        ],
        "year": 2018,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Kinodynamic planning",
          "Trajectory planning",
          "Asymptotic optimality",
          "Sampling-based",
          "RRT*",
          "Motion primitives",
          "Precomputed",
          "Lookup table",
          "Grid"
        ],
        "summary": "Integrates a grid of states and offline precomputed connecting motion primitives into RRT*. Moves the computational burden of trajectory generation to an offline phase, trading runtime efficiency for memory usage and some optimality degradation tied to grid resolution."
      }
    },
    {
      "data": {
        "id": "1809_07051",
        "label": "Kleinbort et al. 2018",
        "title": "Probabilistic completeness of RRT for geometric and kinodynamic planning with forward propagation\n",
        "authors": [
          "Kleinbort",
          "Solovey",
          "Littlefield"
        ],
        "year": 2018,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1809_10252",
        "label": "Qureshi et al. 2018",
        "title": "Deeply Informed Neural Sampling for Robot Motion Planning",
        "authors": [
          "Qureshi",
          "Yip"
        ],
        "year": 2018,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1810_02054",
        "label": "Du et al. 2018",
        "title": "Gradient Descent Provably Optimizes Over-parameterized Neural Networks",
        "authors": [
          "Du",
          "Zhai",
          "Poczos"
        ],
        "year": 2018,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1810_12575",
        "label": "Plötz et al. 2018",
        "title": "Neural Nearest Neighbors Networks",
        "authors": [
          "Plötz",
          "Roth"
        ],
        "year": 2018,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1810_12584",
        "label": "Terzi et al. 2018",
        "title": "Learning-based predictive control for linear systems: a unitary approach",
        "authors": [
          "Terzi",
          "Fagiano",
          "Farina"
        ],
        "year": 2018,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1811_04551",
        "label": "PlaNet",
        "title": "Learning Latent Dynamics for Planning from Pixels",
        "authors": [
          "Hafner",
          "Lillicrap",
          "Fischer"
        ],
        "year": 2018,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Model-based",
          "Reinforcement learning",
          "Contact dynamics",
          "Partial observability",
          "Sparse rewards",
          "Sample efficiency",
          "Dynamics"
        ],
        "summary": "One of the earlier papers describing a successful approach using a deep-learned predictive world model from image inputs."
      }
    },
    {
      "data": {
        "id": "2018_kingston_sampling_based_methods_for",
        "label": "Kingston et al. 2018",
        "title": "Sampling-Based Methods for Motion Planning with Constraints",
        "authors": [
          "Kingston",
          "Moll",
          "Kavraki"
        ],
        "year": 2018,
        "category": "Motion Planning",
        "sub_category": "Surveys & Comparative Studies",
        "tags": [
          "Survey",
          "Motion planning",
          "Robot motion planning",
          "Sampling-based planning",
          "Constrained motion planning",
          "Task constraints"
        ],
        "summary": "Surveys constraint satisfaction techniques for sampling-based motion planning, organizing methods along a spectrum from configuration-space to task-space approaches and covering both configuration sampling and steering primitives for constraint-satisfying motion."
      }
    },
    {
      "data": {
        "id": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "label": "Regularized SaDDP",
        "title": "Regularizing Sampled Differential Dynamic Programming",
        "authors": [
          "Rajamäki",
          "Hämäläinen"
        ],
        "year": 2018,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Differential dynamic programming",
          "Sampling-based optimization",
          "Regularization",
          "Path integral control"
        ],
        "summary": "Extends Sampled DDP with regularization strategies to improve numerical stability and convergence, addressing ill-conditioning issues that arise when the sampled Hessian estimates are noisy or rank-deficient."
      }
    },
    {
      "data": {
        "id": "2018_schwarting_planning_and_decision_making",
        "label": "Schwarting et al. 2018",
        "title": "Planning and Decision-Making for Autonomous Vehicles",
        "authors": [
          "Schwarting",
          "Alonso-Mora",
          "Rus"
        ],
        "year": 2018,
        "category": "Motion Planning",
        "sub_category": "Surveys & Comparative Studies",
        "tags": [
          "Survey",
          "Motion planning",
          "Autonomous vehicles",
          "Decision-making",
          "Probabilistic planning",
          "Game theory",
          "Interaction-aware planning"
        ],
        "summary": "Reviews motion planning and decision-making techniques for autonomous vehicles, covering probabilistic prediction of other agents, game-theoretic and learning-based interaction models, and socially-aware planning for urban driving scenarios."
      }
    },
    {
      "data": {
        "id": "2018_zhang_toward_a_more_complete",
        "label": "Zhang et al. 2018",
        "title": "Toward a More Complete, Flexible, and Safer Speed Planning for Autonomous Driving via Convex Optimization",
        "authors": [
          "Zhang",
          "Chen",
          "Waslander"
        ],
        "year": 2018,
        "category": "Motion Planning",
        "sub_category": "Speed Planning",
        "tags": [
          "Speed planning",
          "Autonomous driving",
          "Convex optimization",
          "Constraints",
          "Safety",
          "Comfort",
          "Mobility",
          "Flexibility"
        ],
        "summary": "Extends convex-optimization-based speed planning to handle a broader set of constraints (comfort, safety, traffic rules) more completely and flexibly than prior approaches, demonstrated on autonomous driving scenarios."
      }
    },
    {
      "data": {
        "id": "1901_00491",
        "label": "Kaya 2019",
        "title": "Optimal control of the double integrator with minimum total variation",
        "authors": [
          "Kaya"
        ],
        "year": 2019,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1903_00155",
        "label": "Bonalli et al. 2019",
        "title": "GuSTO: Guaranteed Sequential Trajectory Optimization via Sequential Convex Programming\n",
        "authors": [
          "Bonalli",
          "Cauligi",
          "Bylard"
        ],
        "year": 2019,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1907_01474",
        "label": "Lembono et al. 2019",
        "title": "Memory of Motion for Warm-starting Trajectory Optimization",
        "authors": [
          "Lembono",
          "Paolillo",
          "Pignat"
        ],
        "year": 2019,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1909_04939",
        "label": "Fawaz et al. 2019",
        "title": "InceptionTime: Finding AlexNet for Time Series Classification",
        "authors": [
          "Fawaz",
          "Lucas",
          "Forestier"
        ],
        "year": 2019,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "1909_09688",
        "label": "RRT*",
        "title": "Revisiting the Asymptotic Optimality of RRT*",
        "authors": [
          "Solovey",
          "Janson",
          "Schmerling"
        ],
        "year": 2019,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Asymptotically optimal",
          "Probabilistically complete",
          "RRT*"
        ],
        "summary": "This paper, from the original authors and friends, corrects some small mistakes in the theory of the asymptotic optimality results and offers new proof techniques."
      }
    },
    {
      "data": {
        "id": "1909_10466",
        "label": "Krake et al. 2019",
        "title": "Dynamic Mode Decomposition: Theory and Data Reconstruction",
        "authors": [
          "Krake",
          "Weiskopf",
          "Eberhardt"
        ],
        "year": 2019,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Dynamic mode decomposition",
          "DMD",
          "Data-driven",
          "Data reconstruction"
        ],
        "summary": "Tutorial and survey that presents theoretical analysis of DMD with a focus on data reconstruction from DMD modes, addressing the relationship between DMD approximations and the underlying dynamics of the system."
      }
    },
    {
      "data": {
        "id": "1912_01603",
        "label": "Dreamer",
        "title": "Dream to Control: Learning Behaviors by Latent Imagination",
        "authors": [
          "Hafner",
          "Lillicrap",
          "Ba"
        ],
        "year": 2019,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "World models",
          "Deep learning",
          "Reinforcement learning",
          "Latent",
          "Imagination",
          "Complex behaviors"
        ],
        "summary": "Build on the predecessor work PlaNet and learns an actor-critic model in place of online planning with the cross entropy method."
      }
    },
    {
      "data": {
        "id": "1912_11676",
        "label": "Mozaffari et al. 2019",
        "title": "Deep Learning-based Vehicle Behaviour Prediction For Autonomous Driving Applications: A Review",
        "authors": [
          "Mozaffari",
          "Al-Jarrah",
          "Dianati"
        ],
        "year": 2019,
        "category": "Motion Prediction",
        "sub_category": null,
        "tags": [
          "Motion prediction",
          "Vehicle behavior prediction",
          "Trajectory prediction",
          "Intention prediction",
          "Deep learning",
          "Autonomous driving",
          "Review",
          "Survey"
        ],
        "summary": "Reviews deep learning approaches for vehicle behavior prediction in autonomous driving, categorizing methods by architecture and prediction output type, with discussion of datasets and evaluation metrics."
      }
    },
    {
      "data": {
        "id": "1912_11912",
        "label": "QNTRPO",
        "title": "Quasi-Newton Trust Region Policy Optimization",
        "authors": [
          "Jha",
          "Raghunathan",
          "Romeres"
        ],
        "year": 2019,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Reinforcement learning",
          "Policy optimization",
          "Trust region methods",
          "Quasi-Newton methods"
        ],
        "summary": "Applies a quasi-Newton Hessian approximation within the TRPO trust region framework, achieving better sample efficiency and faster convergence than standard TRPO by making more informed second-order parameter updates."
      }
    },
    {
      "data": {
        "id": "2019_hannigan_sbp_guided_mpc_to",
        "label": "SBP-Guided MPC",
        "title": "SBP-Guided MPC to Overcome Local Minima in Trajectory Planning",
        "authors": [
          "Hannigan",
          "Song",
          "Khandate"
        ],
        "year": 2019,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory planning",
          "Trajectory optimization",
          "MPC",
          "iLQR",
          "RRT",
          "Sampling-based planning",
          "Local minima",
          "Hybrid planning"
        ],
        "summary": "Uses an RRT solution trajectory to warm-start iLQR, preventing the optimizer from getting stuck in local minima and simultaneously refining the crude RRT path into a smoother, more optimal trajectory."
      }
    },
    {
      "data": {
        "id": "2019_jackson_altro_a_fast_solver",
        "label": "ALTRO",
        "title": "ALTRO: A Fast Solver for Constrained Trajectory Optimization",
        "authors": [
          "Howell",
          "Jackson",
          "Manchester"
        ],
        "year": 2019,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Constrained optimization",
          "iLQR",
          "Augmented Lagrangian",
          "ALTRO"
        ],
        "summary": "Introduces ALTRO (Augmented Lagrangian TRajectory Optimizer), combining augmented Lagrangian outer iterations with iLQR inner loops for constrained trajectory optimization, with an active-set constraint handling polishing step for fast convergence near the solution."
      }
    },
    {
      "data": {
        "id": "2019_lefebvre_path_integral_policy_improvement",
        "label": "PI2-DDP",
        "title": "Path Integral Policy Improvement with Differential Dynamic Programming",
        "authors": [
          "Lefebvre",
          "Crevecoeur"
        ],
        "year": 2019,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Differential dynamic programming",
          "Path integral control",
          "MPPI",
          "Policy improvement"
        ],
        "summary": "Integrates path integral policy improvement (PI²) with differential dynamic programming (DDP), using DDP's second-order local model to guide the sampling distribution in a PI-style update."
      }
    },
    {
      "data": {
        "id": "2019_williams_model_predictive_path_integral",
        "label": "Williams 2019",
        "title": "Model Predictive Path Integral Control: Theoretical Foundations and Applications to Autonomous Driving",
        "authors": [
          "Williams"
        ],
        "year": 2019,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Model predictive path integral control",
          "MPPI",
          "Trajectory optimization",
          "Autonomous driving",
          "Stochastic optimal control",
          "Path integral control"
        ],
        "summary": "PhD dissertation by Grady Williams at Georgia Tech establishing the theoretical foundations of Model Predictive Path Integral (MPPI) control and demonstrating its application to autonomous vehicle navigation."
      }
    },
    {
      "data": {
        "id": "2001_03093",
        "label": "Trajectron++",
        "title": "Trajectron++: Dynamically-Feasible Trajectory Forecasting With Heterogeneous Data",
        "authors": [
          "Salzmann",
          "Ivanovic",
          "Chakravarty"
        ],
        "year": 2020,
        "category": "Motion Prediction",
        "sub_category": null,
        "tags": [
          "Trajectory prediction",
          "Motion forecasting",
          "Multi-agent prediction",
          "Graph neural networks",
          "Heterogeneous data",
          "Probabilistic prediction",
          "Conditional variational autoencoder"
        ],
        "summary": "Extends Trajectron with dynamic feasibility constraints and heterogeneous input data (HD maps, agent types), using a CVAE-based graph recurrent network to produce multi-modal trajectory distributions for multiple interacting agents simultaneously."
      }
    },
    {
      "data": {
        "id": "2002_08809",
        "label": "Liu et al. 2020",
        "title": "DDPNOpt: Differential Dynamic Programming Neural Optimizer",
        "authors": [
          "Liu",
          "Chen",
          "Theodorou"
        ],
        "year": 2020,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2003_02218",
        "label": "Lewkowycz et al. 2020",
        "title": "The large learning rate phase of deep learning: the catapult mechanism",
        "authors": [
          "Lewkowycz",
          "Bahri",
          "Dyer"
        ],
        "year": 2020,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2003_08934",
        "label": "Mildenhall et al. 2020",
        "title": "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis",
        "authors": [
          "Mildenhall",
          "Srinivasan",
          "Tancik"
        ],
        "year": 2020,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2004_08763",
        "label": "Grad+CEM",
        "title": "Model-Predictive Control via Cross-Entropy and Gradient-Based Optimization",
        "authors": [
          "Bharadhwaj",
          "Xie",
          "Shkurti"
        ],
        "year": 2020,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Model predictive control",
          "Cross-entropy method",
          "Gradient-based optimization",
          "Sampling-based control"
        ],
        "summary": "Combines CEM-style action sampling with gradient descent refinement. Quite similar in spirit to Sampled DDP (SaDDP), but uses first-order (gradient) refinement instead of second-order (Hessian), and stays closer to vanilla CEM."
      }
    },
    {
      "data": {
        "id": "2005_00985",
        "label": "AL-DDP",
        "title": "Constrained Differential Dynamic Programming Revisited",
        "authors": [
          "Aoyama",
          "Boutselis",
          "Patel"
        ],
        "year": 2020,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Differential dynamic programming",
          "Constrained optimization",
          "Augmented Lagrangian",
          "Trajectory optimization"
        ],
        "summary": "Revisits constrained DDP with augmented Lagrangian methods, improving constraint handling within the DDP backward-forward pass framework. Contemporary with ALTRO, but from a different group with a different perspective on convergence."
      }
    },
    {
      "data": {
        "id": "2005_04259",
        "label": "Gao et al. 2020",
        "title": "VectorNet: Encoding HD Maps and Agent Dynamics from Vectorized Representation",
        "authors": [
          "Gao",
          "Sun",
          "Zhao"
        ],
        "year": 2020,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2006_11239",
        "label": "Ho et al. 2020",
        "title": "Denoising Diffusion Probabilistic Models",
        "authors": [
          "Ho",
          "Jain",
          "Abbeel"
        ],
        "year": 2020,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2008_08835",
        "label": "Zhou et al. 2020",
        "title": "EGO-Planner: An ESDF-free Gradient-based Local Planner for Quadrotors",
        "authors": [
          "Zhou",
          "Wang",
          "Ye"
        ],
        "year": 2020,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2009_10484",
        "label": "Gammell et al. 2020",
        "title": "Asymptotically Optimal Sampling-Based Motion Planning Methods",
        "authors": [
          "Gammell",
          "Strub"
        ],
        "year": 2020,
        "category": "Motion Planning",
        "sub_category": "Surveys & Comparative Studies",
        "tags": [
          "Survey",
          "Robotics",
          "Motion planning",
          "Robot motion planning",
          "Sampling-based planning",
          "Optimal motion planning",
          "Asymptotically optimal"
        ],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2010_00411",
        "label": "FDDP",
        "title": "A Feasibility-Driven Approach to Control-Limited DDP",
        "authors": [
          "Mastalli",
          "Merkt",
          "Marti-Saumell"
        ],
        "year": 2020,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Differential dynamic programming",
          "Constrained optimization",
          "Feasibility",
          "Control limits",
          "Legged robots"
        ],
        "summary": "Introduces FDDP (Feasibility-Driven DDP) which enforces feasibility at each iteration rather than penalizing infeasibility, overcoming convergence issues in control-limited DDP."
      }
    },
    {
      "data": {
        "id": "2010_01412",
        "label": "Foret et al. 2020",
        "title": "Sharpness-Aware Minimization for Efficiently Improving Generalization",
        "authors": [
          "Foret",
          "Kleiner",
          "Mobahi"
        ],
        "year": 2020,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2010_10726",
        "label": "Tordesillas et al. 2020",
        "title": "MINVO Basis: Finding Simplexes with Minimum Volume Enclosing Polynomial Curves",
        "authors": [
          "Tordesillas",
          "How"
        ],
        "year": 2020,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2010_11929",
        "label": "Dosovitskiy et al. 2020",
        "title": "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale",
        "authors": [
          "Dosovitskiy",
          "Beyer",
          "Kolesnikov"
        ],
        "year": 2020,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2011_11303",
        "label": "Maddalena et al. 2020",
        "title": "KPC: Learning-Based Model Predictive Control with Deterministic Guarantees",
        "authors": [
          "Maddalena",
          "Scharnhorst",
          "Jiang"
        ],
        "year": 2020,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2011_14439",
        "label": "Greydanus et al. 2020",
        "title": "Scaling Down Deep Learning with MNIST-1D",
        "authors": [
          "Greydanus",
          "Kobak"
        ],
        "year": 2020,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2012_00152",
        "label": "Domingos 2020",
        "title": "Every Model Learned by Gradient Descent Is Approximately a Kernel Machine",
        "authors": [
          "Domingos"
        ],
        "year": 2020,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2012_08791",
        "label": "Dempster et al. 2020",
        "title": "MINIROCKET: A Very Fast (Almost) Deterministic Transform for Time Series Classification\n",
        "authors": [
          "Dempster",
          "Schmidt",
          "Webb"
        ],
        "year": 2020,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2012_12657",
        "label": "Sharf et al. 2020",
        "title": "Assume/Guarantee Contracts for Dynamical Systems: Theory and Computational Tools",
        "authors": [
          "Sharf",
          "Besselink",
          "Molin"
        ],
        "year": 2020,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2020_marti_saumell_squash_box_feasibility_driven",
        "label": "Squash-Box FDDP",
        "title": "Squash-Box Feasibility Driven Differential Dynamic Programming",
        "authors": [
          "Marti-Saumell",
          "Solà",
          "Mastalli"
        ],
        "year": 2020,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Differential dynamic programming",
          "Constrained optimization",
          "Control limits",
          "Feasibility",
          "Squash-Box",
          "Feasibility driven differential dynamic programming",
          "FDDP"
        ],
        "summary": "Presents a homotopy method which progressively penalizes control action constraint violations more aggressively in an outer loop, using FDDP in the inner loop solves. Solution converges to the hard-constrained optimal trajectory. Quadratic barrier keeps decision variables (control actions) near the center of the sigmoid squashing functions, i.e. avoids a kind of \"dead gradients\" numerical issue."
      }
    },
    {
      "data": {
        "id": "2020_mashayekhi_informed_rrt_star_connect",
        "label": "Informed RRT*-Connect",
        "title": "Informed RRT*-Connect: An Asymptotically Optimal Single-Query Path Planning Method",
        "authors": [
          "Mashayekhi",
          "Idris",
          "Anisi"
        ],
        "year": 2020,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Sampling-based planning",
          "Asymptotic optimality",
          "Bidirectional search",
          "RRT*",
          "RRT-Connect",
          "Informed sampling"
        ],
        "summary": "Applies Informed RRT*'s ellipsoidal focused sampling to RRT*-Connect: the planner uses bidirectional tree growth and rewiring (as in RRT*-Connect) to find an initial solution quickly, then restricts subsequent sampling to the prolate hyperspheroid subset that can improve it (as in Informed RRT*). An incremental combination of two existing techniques with no major novel theoretical contribution, but can achieve fewer iterations and lower solution cost than RRT*-Connect alone."
      }
    },
    {
      "data": {
        "id": "2020_pellegrini_a_multiple_shooting_differential",
        "label": "MS-DDP",
        "title": "A Multiple-Shooting Differential Dynamic Programming Algorithm. Part 1: Theory",
        "authors": [
          "Pellegrini",
          "Russell"
        ],
        "year": 2020,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Differential dynamic programming",
          "Multiple shooting",
          "Trajectory optimization",
          "Spacecraft",
          "Optimal control"
        ],
        "summary": "Develops a rigorous multiple-shooting formulation of DDP with theoretical convergence analysis, establishing connections to classical multiple-shooting methods."
      }
    },
    {
      "data": {
        "id": "2021_li_sliding_window_informed_rrt",
        "label": "SWIRRT*",
        "title": "Sliding-Window Informed RRT*: A Method for Speeding Up the Optimization and Path Smoothing",
        "authors": [
          "Li",
          "Wang",
          "Wang"
        ],
        "year": 2021,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Sampling-based planning",
          "Asymptotic optimality",
          "Sliding-Window Informed RRT*",
          "Informed RRT*",
          "Sliding window",
          "Path smoothing"
        ],
        "summary": "SWIRRT* addresses the degradation of Informed RRT* in large environments where the ellipsoidal sampling region covers most of the state space. Instead of sampling from a single ellipsoid spanning start to goal, it applies a sliding-window approach that focuses successive local ellipsoids along the current path, accelerating post-initial-solution optimization and improving path smoothness."
      }
    },
    {
      "data": {
        "id": "2101_04413",
        "label": "Tankaria et al. 2021",
        "title": "A Regularized Limited Memory BFGS method for Large-Scale Unconstrained Optimization and its Efficient Implementations\n",
        "authors": [
          "Tankaria",
          "Sugimoto",
          "Yamashita"
        ],
        "year": 2021,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2101_11565",
        "label": "SPP-GCS",
        "title": "Shortest Paths in Graphs of Convex Sets",
        "authors": [
          "Marcucci",
          "Umenberger",
          "Parrilo"
        ],
        "year": 2021,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Graphs of convex sets",
          "GCS",
          "Graph search",
          "Convex",
          "Convex set",
          "Convex optimization",
          "Mixed-integer programming",
          "Motion planning",
          "Optimal control",
          "Trajectory optimization"
        ],
        "summary": "Each graph vertex is associated with a convex set and edge lengths are convex functions of the endpoints' positions. The key contribution is a strong mixed-integer convex program (MICP) formulation based on perspective operators that yields a tight relaxation, enabling globally optimal paths in large graphs and high-dimensional spaces. Forms the theoretical foundation for GCS-based motion planning."
      }
    },
    {
      "data": {
        "id": "2102_03664",
        "label": "Jongeneel et al. 2021",
        "title": "Efficient Learning of a Linear Dynamical System with Stability Guarantees",
        "authors": [
          "Jongeneel",
          "Sutter",
          "Kuhn"
        ],
        "year": 2021,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2102_03861",
        "label": "Saveriano et al. 2021",
        "title": "Dynamic Movement Primitives in Robotics: A Tutorial Survey",
        "authors": [
          "Saveriano",
          "Abu-Dakka",
          "Kramberger"
        ],
        "year": 2021,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2102_08302",
        "label": "Terzi et al. 2021",
        "title": "Robust multi-rate predictive control using multi-step prediction models learned from data\n",
        "authors": [
          "Terzi",
          "Fagiano",
          "Farina"
        ],
        "year": 2021,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2103_00065",
        "label": "Cohen et al. 2021",
        "title": "Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability",
        "authors": [
          "Cohen",
          "Kaur",
          "Li"
        ],
        "year": 2021,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2103_03293",
        "label": "DDP",
        "title": "Accelerating Second-Order Differential Dynamic Programming for Rigid-Body Systems",
        "authors": [
          "Nganga",
          "Wensing"
        ],
        "year": 2021,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Differential dynamic programming",
          "DDP",
          "Second-order methods",
          "Rigid-body dynamics",
          "Trajectory optimization"
        ],
        "summary": "Shows how to efficiently evaluate the second-order dynamics derivatives required by full DDP for rigid-body systems via recursive algorithms. This can make full DDP computationally competitive with or faster than iLQR. Also provides a clear derivation of DDP."
      }
    },
    {
      "data": {
        "id": "2103_05478",
        "label": "Jongeneel et al. 2021",
        "title": "Small errors in random zeroth-order optimization are imaginary",
        "authors": [
          "Jongeneel",
          "Yue",
          "Kuhn"
        ],
        "year": 2021,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2103_14438",
        "label": "Liu et al. 2021",
        "title": "Gated Transformer Networks for Multivariate Time Series Classification",
        "authors": [
          "Liu",
          "Ren",
          "Ma"
        ],
        "year": 2021,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2103_15691",
        "label": "Arnab et al. 2021",
        "title": "ViViT: A Video Vision Transformer",
        "authors": [
          "Arnab",
          "Dehghani",
          "Heigold"
        ],
        "year": 2021,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2104_00241",
        "label": "Tsallis VI-SOC",
        "title": "Variational Inference MPC using Tsallis Divergence",
        "authors": [
          "Okada",
          "Taniguchi"
        ],
        "year": 2021,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Model predictive path integral control",
          "MPPI",
          "Variational inference",
          "Tsallis divergence",
          "Stochastic optimal control",
          "Model predictive control"
        ],
        "summary": "Extends variational inference MPC by replacing KL divergence with Tsallis divergence, yielding a broader family of sampling-based controllers that recovers MPPI as a special case and can better handle multimodal cost landscapes."
      }
    },
    {
      "data": {
        "id": "2104_03186",
        "label": "Särkkä et al. 2021",
        "title": "Temporal Parallelisation of Dynamic Programming and Linear Quadratic Control",
        "authors": [
          "Särkkä",
          "García-Fernández"
        ],
        "year": 2021,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2107_08086",
        "label": "Goyal et al. 2021",
        "title": "An Information-state based Approach to the Optimal Output Feedback Control of Nonlinear Systems\n",
        "authors": [
          "Goyal",
          "Wang",
          "Mohamed"
        ],
        "year": 2021,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2108_13404",
        "label": "SINDy with Control",
        "title": "SINDy with Control: A Tutorial",
        "authors": [
          "Fasel",
          "Kaiser",
          "Kutz"
        ],
        "year": 2021,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "SINDy",
          "System identification",
          "Control",
          "Nonlinear dynamics",
          "Data-driven methods"
        ],
        "summary": "Tutorial demonstrating how to extend SINDy to systems with exogenous control inputs (SINDy-C), covering library selection, ensemble methods for robustness, and applications to controlled nonlinear dynamical systems."
      }
    },
    {
      "data": {
        "id": "2109_03920",
        "label": "Chan et al. 2021",
        "title": "Inverse Optimization: Theory and Applications",
        "authors": [
          "Chan",
          "Mahmood",
          "Zhu"
        ],
        "year": 2021,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2109_07081",
        "label": "CL-SQP",
        "title": "Optimizing Trajectories with Closed-Loop Dynamic SQP",
        "authors": [
          "Singh",
          "Slotine",
          "Sindhwani"
        ],
        "year": 2021,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Sequential quadratic programming",
          "Closed-loop",
          "Nonlinear optimization",
          "Robot control"
        ],
        "summary": "Introduces closed-loop dynamic SQP, which integrates feedback gain computation within the SQP iteration structure, improving robustness and convergence for trajectory optimization compared to open-loop sequential approaches."
      }
    },
    {
      "data": {
        "id": "2111_08481",
        "label": "PySINDy",
        "title": "PySINDy: A Comprehensive Python Package for Robust Sparse System Identification",
        "authors": [
          "Kaptanoglu",
          "Silva",
          "Fasel"
        ],
        "year": 2021,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "SINDy",
          "System identification",
          "Software",
          "Python",
          "Sparse regression"
        ],
        "summary": "Comprehensive Python package implementing SINDy with support for multiple sparse regression algorithms, customizable feature libraries, etc."
      }
    },
    {
      "data": {
        "id": "2111_12083",
        "label": "VISTA 2.0",
        "title": "VISTA 2.0: An Open, Data-driven Simulator for Multimodal Sensing and Policy Learning for Autonomous Vehicles",
        "authors": [
          "Amini",
          "Wang",
          "Gilitschenski"
        ],
        "year": 2022,
        "category": "Motion Planning",
        "sub_category": "Interaction-aware Planning",
        "tags": [
          "Autonomous Driving",
          "Data-driven Simulation",
          "Sim-to-Real Transfer",
          "Multimodal Sensing",
          "LiDAR",
          "Event Camera",
          "Policy Learning"
        ],
        "summary": "VISTA 2.0 is an open-source, data-driven simulator from MIT that synthesizes novel viewpoints from real-world data across RGB cameras, 3D LiDAR, and event-based cameras; policies trained in it transfer directly to a full-scale autonomous vehicle without domain randomization."
      }
    },
    {
      "data": {
        "id": "2111_12137",
        "label": "Wang et al. 2022",
        "title": "Learning Interactive Driving Policies via Data-driven Simulation",
        "authors": [
          "Wang",
          "Amini",
          "Schwarting"
        ],
        "year": 2022,
        "category": "Motion Planning",
        "sub_category": "Interaction-aware Planning",
        "tags": [
          "Autonomous Driving",
          "Data-driven Simulation",
          "Multi-agent Interaction",
          "Policy Learning",
          "Sim-to-Real Transfer",
          "Inpainting"
        ],
        "summary": "Companion paper to VISTA 2.0 that extends data-driven simulation to multi-agent scenarios by inpainting other vehicles into real-world footage, enabling interactive driving policy learning that transfers directly to a full-scale autonomous vehicle."
      }
    },
    {
      "data": {
        "id": "2112_02089",
        "label": "Mishchenko 2021",
        "title": "Regularized Newton Method with Global $O(1/k^2)$ Convergence",
        "authors": [
          "Mishchenko"
        ],
        "year": 2021,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2022_honig_benchmarking_sampling_search_and",
        "label": "Hönig et al. 2022",
        "title": "Benchmarking Sampling-, Search-, and Optimization-based Approaches for Time-Optimal Kinodynamic Mobile Robot Motion Planning",
        "authors": [
          "Hönig",
          "Ortiz-Haro",
          "Toussaint"
        ],
        "year": 2022,
        "category": "Motion Planning",
        "sub_category": "Surveys & Comparative Studies",
        "tags": [
          "Benchmarking",
          "Kinodynamic planning",
          "Mobile robots",
          "Sampling-based planning",
          "Search-based planning",
          "Trajectory optimization",
          "Time-optimal planning"
        ],
        "summary": "Benchmarks and compares sampling-, search-, and optimization-based planners for time-optimal kinodynamic mobile robot motion planning, providing an empirical evaluation of modern approaches."
      }
    },
    {
      "data": {
        "id": "2022_houghton_path_planning_differential_dynamic",
        "label": "Houghton et al. 2022",
        "title": "Path Planning: Differential Dynamic Programming and Model Predictive Path Integral Control on VTOL Aircraft",
        "authors": [
          "Houghton",
          "Oshin",
          "Acheson"
        ],
        "year": 2022,
        "category": "Motion Planning",
        "sub_category": "Surveys & Comparative Studies",
        "tags": [
          "Path planning",
          "Trajectory optimization",
          "Differential dynamic programming",
          "Model predictive path integral control",
          "DDP",
          "MPPI",
          "UAV",
          "VTOL",
          "Survey",
          "Comparative study"
        ],
        "summary": "Comparative study applying DDP and MPPI trajectory optimization methods to path planning for VTOL (urban air mobility) aircraft, benchmarking their performance and practical trade-offs on this application domain."
      }
    },
    {
      "data": {
        "id": "2022_schmid_dynamic_mode_decomposition_and",
        "label": "Schmid 2022",
        "title": "Dynamic Mode Decomposition and Its Variants",
        "authors": [
          "Schmid"
        ],
        "year": 2022,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Dynamic mode decomposition",
          "DMD",
          "Fluid dynamics",
          "Data-driven methods",
          "Survey"
        ],
        "summary": "Comprehensive review of DMD from its fluid dynamics origins through current extensions, providing a unified perspective on theoretical foundations and practical applications."
      }
    },
    {
      "data": {
        "id": "2201_02177",
        "label": "Power et al. 2022",
        "title": "Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets",
        "authors": [
          "Power",
          "Burda",
          "Edwards"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2201_03163",
        "label": "Continuous-Curvature Target Tree",
        "title": "Continuous-Curvature Target Tree Algorithm for Path Planning in Complex Parking Environments",
        "authors": [
          "Kim",
          "Ahn",
          "Park"
        ],
        "year": 2022,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Path planning",
          "Parking",
          "Clothoids",
          "Curvature continuity",
          "RRT",
          "Target tree",
          "Autonomous vehicles"
        ],
        "summary": "Extends the target tree algorithm - “Model-based decision making with imagination for autonomous parking” by Feng, Chen, Chen, and Zheng (2018) - for autonomous parking by replacing circular/straight path segments with clothoid curves to achieve continuous curvature (G2). Introduces an obstacle-aware cost function for target tree construction to reduce planning time in complex environments. Combined with RRT* and shortest-path selection, yields near-optimal continuous-curvature parking solutions."
      }
    },
    {
      "data": {
        "id": "2201_09104",
        "label": "Gebotys et al. 2022",
        "title": "Understanding the Effects of Second-Order Approximations in Natural Policy Gradient Reinforcement Learning\n",
        "authors": [
          "Gebotys",
          "Wong",
          "Clausi"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2202_00817",
        "label": "Suh et al. 2022",
        "title": "Do Differentiable Simulators Give Better Policy Gradients?",
        "authors": [
          "Suh",
          "Simchowitz",
          "Zhang"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2202_04612",
        "label": "Berglund et al. 2022",
        "title": "Zeroth-Order Randomized Subspace Newton Methods",
        "authors": [
          "Berglund",
          "Khirirat",
          "Wang"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2202_07125",
        "label": "Wen et al. 2022",
        "title": "Transformers in Time Series: A Survey",
        "authors": [
          "Wen",
          "Zhou",
          "Zhang"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2203_01751",
        "label": "Kamat et al. 2022",
        "title": "BITKOMO: Combining Sampling and Optimization for Fast Convergence in Optimal Motion Planning\n",
        "authors": [
          "Kamat",
          "Ortiz-Haro",
          "Toussaint"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2203_02176",
        "label": "Grothe et al. 2022",
        "title": "ST-RRT*: Asymptotically-Optimal Bidirectional Motion Planning through Space-Time",
        "authors": [
          "Grothe",
          "Hartmann",
          "Orthey"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2203_04955",
        "label": "Hansen et al. 2022",
        "title": "Temporal Difference Learning for Model Predictive Control",
        "authors": [
          "Hansen",
          "Wang",
          "Su"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2203_11419",
        "label": "Schaller et al. 2022",
        "title": "Embedded Code Generation with CVXPY",
        "authors": [
          "Schaller",
          "Banjac",
          "Diamond"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2203_15471",
        "label": "Köhler et al. 2022",
        "title": "State space models vs. multi-step predictors in predictive control: Are state space models complicating safe data-driven designs?\n",
        "authors": [
          "Köhler",
          "Wabersich",
          "Berberich"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2204_02322",
        "label": "Roulet et al. 2025",
        "title": "On Global and Local Convergence of Iterative Linear Quadratic Optimization Algorithms for Discrete Time Nonlinear Control",
        "authors": [
          "Roulet",
          "Srinivasa",
          "Fazel"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "iLQR",
          "Differential dynamic programming",
          "Convergence analysis",
          "Nonlinear control"
        ],
        "summary": "Analyzes both global and local convergence properties of iterative LQR/DDP algorithms for discrete-time nonlinear control, providing theoretical convergence guarantees under specific regularity conditions."
      }
    },
    {
      "data": {
        "id": "2204_07319",
        "label": "Hung et al. 2022",
        "title": "A review of path following control strategies for autonomous robotic vehicles: theory, simulations, and experiments\n",
        "authors": [
          "Hung",
          "Rego",
          "Quintas"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2204_09352",
        "label": "Zimmermann et al. 2022",
        "title": "Differentiable Collision Avoidance Using Collision Primitives",
        "authors": [
          "Zimmermann",
          "Busenhart",
          "Huber"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2205_04422",
        "label": "GCS",
        "title": "Motion Planning around Obstacles with Convex Optimization",
        "authors": [
          "Marcucci",
          "Petersen",
          "Wrangel"
        ],
        "year": 2022,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Motion planning",
          "Trajectory optimization",
          "Convex optimization",
          "Mixed-integer programming",
          "Collision avoidance",
          "Bezier curves",
          "GCS"
        ],
        "summary": "Applies the GCS framework to collision-free trajectory optimization by decomposing the free configuration space into convex regions and formulating motion planning as a shortest-path problem in a GCS. Trajectories are parameterized as Bézier curves, enabling compact mixed-integer optimization with constraints on shape, duration, and velocity. A convex relaxation with randomized rounding provides near-global solutions with certified optimality bounds, outperforming both sampling-based and prior trajectory optimization methods."
      }
    },
    {
      "data": {
        "id": "2205_09991",
        "label": "Janner et al. 2022",
        "title": "Planning with Diffusion for Flexible Behavior Synthesis",
        "authors": [
          "Janner",
          "Du",
          "Tenenbaum"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2206_03004",
        "label": "DriveIRL",
        "title": "DriveIRL: Driving in Real Life with Inverse Reinforcement Learning",
        "authors": [
          "Phan-Minh",
          "Howington",
          "Chu"
        ],
        "year": 2022,
        "category": "Motion Planning",
        "sub_category": "Machine Learning in Motion Planning",
        "tags": [
          "Autonomous driving",
          "Inverse reinforcement learning",
          "Motion planning",
          "Imitation learning",
          "Real-world deployment"
        ],
        "summary": "Inverse Reinforcement Learning-based planner demonstrated on a real self-driving car in dense urban traffic. Trained on large-scale human driving logs. The architecture design is critical to the success of the approach: there is a classical trajectory generator (based on Dubins paths, pre-computed acceleration profiles, and access to a clean road geometry model) capable of generating diverse safe trajectories, a safety filter that removes all trajectory candidates that are not forward recursively safe, and the learned model is only for assigning scores to the safety-filtered trajectory candidates. Includes a useful set of standardized evaluation metrics for learned planners (see Appendix A.5)."
      }
    },
    {
      "data": {
        "id": "2207_05844",
        "label": "Wayformer",
        "title": "Wayformer: Motion Forecasting via Simple & Efficient Attention Networks",
        "authors": [
          "Nayakanti",
          "Al-Rfou",
          "Zhou"
        ],
        "year": 2022,
        "category": "Motion Prediction",
        "sub_category": null,
        "tags": [
          "Motion forecasting",
          "Transformer",
          "Attention mechanism",
          "Autonomous driving",
          "Multi-modal prediction",
          "Waymo",
          "Wayformer"
        ],
        "summary": "Proposes a simple and efficient transformer-based architecture for motion forecasting, showing that a straightforward attention design over scene and agent context can match or surpass more complex architectures on standard benchmarks like Waymo Open Motion Dataset (WOMD)."
      }
    },
    {
      "data": {
        "id": "2207_06362",
        "label": "iLQR Algorithmic Templates",
        "title": "Iterative Linear Quadratic Optimization for Nonlinear Control: Differentiable Programming Algorithmic Templates",
        "authors": [
          "Roulet",
          "Srinivasa",
          "Fazel"
        ],
        "year": 2022,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "iLQR",
          "Differentiable programming",
          "Nonlinear control",
          "Tutorial"
        ],
        "summary": "Presents iLQR and its variants as differentiable programming algorithmic templates, enabling systematic derivation, implementation, and differentiation through iLQR solvers using automatic differentiation frameworks."
      }
    },
    {
      "data": {
        "id": "2208_02439",
        "label": "MPPI-IPDDP",
        "title": "MPPI-IPDDP: Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots",
        "authors": [
          "Kim",
          "Jung",
          "Hong"
        ],
        "year": 2022,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "MPPI",
          "Differential dynamic programming",
          "Interior point",
          "Collision avoidance",
          "Hybrid trajectory optimization"
        ],
        "summary": "Hybrid method combining MPPI for global, collision-free trajectory generation with Interior Point DDP (IPDDP) for smooth, dynamically optimal local refinement, leveraging the complementary strengths of sampling and gradient-based trajectory optimization."
      }
    },
    {
      "data": {
        "id": "2208_05888",
        "label": "Doikov et al. 2022",
        "title": "Super-Universal Regularized Newton Method",
        "authors": [
          "Doikov",
          "Mishchenko",
          "Nesterov"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2209_09006",
        "label": "PLAL",
        "title": "Enforcing the Consensus Between Trajectory Optimization and Policy Learning for Precise Robot Control",
        "authors": [
          "Lidec",
          "Jallet",
          "Laptev"
        ],
        "year": 2022,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Trajectory optimization",
          "Policy learning",
          "Reinforcement learning",
          "Robot control",
          "Hybrid approaches"
        ],
        "summary": "Uses an Augmented Lagrangian / ADMM technique to penalize disagreement between a learned policy and a trajectory optimizer during training, combining the accuracy of trajectory optimization with the generalization of learned policies for precise robot control."
      }
    },
    {
      "data": {
        "id": "2210_01744",
        "label": "BB-RRT",
        "title": "Bang-Bang Boosting of RRTs",
        "authors": [
          "LaValle",
          "Sakcak",
          "LaValle"
        ],
        "year": 2022,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Kinodynamic planning",
          "RRT",
          "Bang-bang control",
          "Steering function",
          "Double integrator",
          "Time-optimal control"
        ],
        "summary": "Derives a complete, exact bang-bang time-optimal steering method for synchronized double integrators, using it to boost RRT performance via better BVP solving, improved Voronoi bias metrics, and post-hoc trajectory time-optimization."
      }
    },
    {
      "data": {
        "id": "2212_00541",
        "label": "MJPC",
        "title": "Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo",
        "authors": [
          "Howell",
          "Gileadi",
          "Tunyasuvunakool"
        ],
        "year": 2022,
        "category": "Motion Planning",
        "sub_category": "Frameworks & Stack Architectures",
        "tags": [
          "Model predictive control",
          "Predictive Sampling",
          "Derivative-free optimization",
          "Real-time",
          "MuJoCo",
          "Robotics"
        ],
        "summary": "Introduces MJPC, an open-source framework for real-time predictive control built on MuJoCo physics, implementing iLQG, Gradient Descent, and a derivative-free Predictive Sampling baseline. Demonstrates that simple sampling-based methods are competitive with classical trajectory optimizers."
      }
    },
    {
      "data": {
        "id": "2212_02603",
        "label": "Sacks et al. 2022",
        "title": "Learning to Optimize in Model Predictive Control",
        "authors": [
          "Sacks",
          "Boots"
        ],
        "year": 2022,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2212_06437",
        "label": "DiffStack",
        "title": "DiffStack: A Differentiable and Modular Control Stack for Autonomous Vehicles",
        "authors": [
          "Karkus",
          "Ivanovic",
          "Mannor"
        ],
        "year": 2022,
        "category": "Motion Planning",
        "sub_category": "Frameworks & Stack Architectures",
        "tags": [
          "Differentiable planning",
          "Autonomous driving",
          "Prediction",
          "Motion planning",
          "End-to-end learning",
          "Modular"
        ],
        "summary": "Presents DiffStack, a fully differentiable and modular autonomous driving stack that combines prediction, planning, and control. By making the entire stack differentiable, it enables end-to-end gradient-based optimization across components, improving performance over non-differentiable modular baselines."
      }
    },
    {
      "data": {
        "id": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "label": "ProxDDP",
        "title": "PROXDDP: Proximal Constrained Trajectory Optimization",
        "authors": [
          "Jallet",
          "Bambade",
          "Arlaud"
        ],
        "year": 2023,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Differential dynamic programming",
          "Constrained optimization",
          "Proximal methods",
          "ProxDDP"
        ],
        "summary": "Introduces ProxDDP, using proximal point iterations within a DDP framework to overcome convergence issues often encountered in Augmented Lagrangian DDP methods (e.g., ALTRO), with provable convergence guarantees for constrained trajectory optimization."
      }
    },
    {
      "data": {
        "id": "2023_steinecker_a_simple_and_model",
        "label": "CCMA",
        "title": "A Simple and Model-Free Path Filtering Algorithm for Smoothing and Accuracy",
        "authors": [
          "Steinecker",
          "Wuensche"
        ],
        "year": 2023,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Path planning",
          "Path smoothing",
          "Path filtering",
          "Moving average",
          "Curvature",
          "Model-free",
          "Post-processing"
        ],
        "summary": "CCMA applies an iterative spatial-curvature-corrected moving average to smooth a path without requiring any kinematic model. Takes advantage of special structure and knowledge that the data series represents a spatial path (instead of an arbitrary sequence)."
      }
    },
    {
      "data": {
        "id": "2301_11902",
        "label": "Chen et al. 2023",
        "title": "Tree-structured Policy Planning with Learned Behavior Models",
        "authors": [
          "Chen",
          "Karkus",
          "Ivanovic"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2301_13143",
        "label": "RRT-MPPI",
        "title": "RRT Guided Model Predictive Path Integral Method",
        "authors": [
          "Tao",
          "Kim",
          "Hovakimyan"
        ],
        "year": 2023,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "MPPI",
          "RRT",
          "Sampling-based planning",
          "Model predictive control"
        ],
        "summary": "Grows an RRT to produce a coarse initial plan, then uses that plan as the mean of the MPPI sampling distribution, combining the global exploration of RRT with the local refinement of MPPI."
      }
    },
    {
      "data": {
        "id": "2302_11670",
        "label": "Swedeen et al. 2023",
        "title": "Batch Informed Trees (BIT*)",
        "authors": [
          "Swedeen",
          "Droge"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2303_04137",
        "label": "Diffusion Policy",
        "title": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
        "authors": [
          "Chi",
          "Xu",
          "Feng"
        ],
        "year": 2023,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Diffusion policy",
          "Diffusion models",
          "Action diffusion",
          "Machine learning",
          "Imitation learning",
          "Robot learning",
          "Visuomotor policy",
          "Transformer"
        ],
        "summary": "Models robot visuomotor policy as a denoising diffusion process over action sequences, enabling multimodal and high-dimensional action distributions that outperform regression-based imitation learning methods on dexterous manipulation benchmarks."
      }
    },
    {
      "data": {
        "id": "2303_09824",
        "label": "Teng et al. 2023",
        "title": "Motion Planning for Autonomous Driving: The State of the Art and Future Perspectives",
        "authors": [
          "Teng",
          "Hu",
          "Deng"
        ],
        "year": 2023,
        "category": "Motion Planning",
        "sub_category": "Surveys & Comparative Studies",
        "tags": [
          "Survey",
          "Motion planning",
          "Autonomous driving",
          "End-to-end planning",
          "Pipeline planning",
          "Deep learning",
          "Intelligent vehicles"
        ],
        "summary": "Surveys both pipeline-based and end-to-end motion planning approaches for autonomous driving, analyzing selection, expansion, and optimization in classical methods alongside deep learning training strategies for end-to-end systems, with experimental comparisons and future challenges."
      }
    },
    {
      "data": {
        "id": "2303_16746",
        "label": "FATROP",
        "title": "FATROP: A Fast Constrained Optimal Control Problem Solver for Robot Trajectory Optimization and Control",
        "authors": [
          "Vanroye",
          "Sathya",
          "Schutter"
        ],
        "year": 2023,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Constrained optimization",
          "Optimal control",
          "Riccati factorization",
          "Real-time",
          "CasADi",
          "acados"
        ],
        "summary": "Presents FATROP, a fast OCP solver based on Riccati factorization of the KKT conditions, achieving sub-2ms solve times with C++ code generation via CasADi integration (ships with CasADi ≥3.6.7 which is also accessible from acados)."
      }
    },
    {
      "data": {
        "id": "2304_00346",
        "label": "Zhu et al. 2023",
        "title": "Convergent iLQR for Safe Trajectory Planning and Control of Legged Robots",
        "authors": [
          "Zhu",
          "Payne",
          "Johnson"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2304_07193",
        "label": "Oquab et al. 2023",
        "title": "DINOv2: Learning Robust Visual Features without Supervision",
        "authors": [
          "Oquab",
          "Darcet",
          "Moutakanni"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2304_13029",
        "label": "Middlehurst et al. 2023",
        "title": "Bake off redux: a review and experimental evaluation of recent time series classification algorithms\n",
        "authors": [
          "Middlehurst",
          "Schäfer",
          "Bagnall"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2305_01072",
        "label": "fastpathplanning",
        "title": "Fast Path Planning Through Large Collections of Safe Boxes",
        "authors": [
          "Marcucci",
          "Nobel",
          "Tedrake"
        ],
        "year": 2023,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Motion planning",
          "Convex optimization",
          "Path planning",
          "Trajectory optimization",
          "Free-space decomposition",
          "Graph search",
          "GCS"
        ],
        "summary": "Presents a fast two-phase path planner for environments where the free space is pre-decomposed into a large collection of axis-aligned safe boxes. An offline phase constructs a graph over box intersections. At runtime, a graph shortest-path search finds a polygonal waypoint sequence, then a convex optimal-control problem smooths it into a continuous Bézier trajectory guaranteed collision-free at all times. The decomposition into a cheap graph search followed by small convex programs gives near-real-time performance even with tens of thousands of boxes."
      }
    },
    {
      "data": {
        "id": "2305_09619",
        "label": "Pfrommer et al. 2023",
        "title": "The Power of Learned Locally Linear Models for Nonlinear Policy Optimization",
        "authors": [
          "Pfrommer",
          "Simchowitz",
          "Westenbroek"
        ],
        "year": 2023,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Reinforcement learning",
          "Trajectory optimization",
          "Nonlinear control",
          "Linear models",
          "iLQR",
          "Data-driven control",
          "Model-based"
        ],
        "summary": "Provides theoretical grounding for why locally linear models learned from data combined with model-based trajectory optimization (iLQR) can achieve sample efficiency for control of nonlinear systems with unknown dynamics."
      }
    },
    {
      "data": {
        "id": "2305_12032",
        "label": "Montali et al. 2023",
        "title": "The Waymo Open Sim Agents Challenge",
        "authors": [
          "Montali",
          "Lambert",
          "Mougin"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2306_09852",
        "label": "Romero et al. 2023",
        "title": "Actor-Critic Model Predictive Control: Differentiable Optimization meets Reinforcement Learning for Agile Flight\n",
        "authors": [
          "Romero",
          "Aljalbout",
          "Song"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2306_13867",
        "label": "Nghiem et al. 2023",
        "title": "Physics-Informed Machine Learning for Modeling and Control of Dynamical Systems",
        "authors": [
          "Nghiem",
          "Drgoňa",
          "Jones"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2307_03167",
        "label": "Lew et al. 2023",
        "title": "Risk-Averse Trajectory Optimization via Sample Average Approximation",
        "authors": [
          "Lew",
          "Bonalli",
          "Pavone"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2307_09105",
        "label": "Pezzato et al. 2023",
        "title": "Sampling-based Model Predictive Control Leveraging Parallelizable Physics Simulations\n",
        "authors": [
          "Pezzato",
          "Salmi",
          "Trevisan"
        ],
        "year": 2023,
        "category": "Motion Planning",
        "sub_category": "Frameworks & Stack Architectures",
        "tags": [
          "MPPI",
          "Motion planning",
          "Trajectory optimization",
          "GPU",
          "Parallelized",
          "Isaac",
          "Gym",
          "IsaacGym",
          "Robotics",
          "Simulation"
        ],
        "summary": "Uses IsaacGym as a simulator for forward dynamics propagation within an MPPI framework."
      }
    },
    {
      "data": {
        "id": "2308_00928",
        "label": "Dempster et al. 2023",
        "title": "QUANT: A Minimalist Interval Method for Time Series Classification",
        "authors": [
          "Dempster",
          "Schmidt",
          "Webb"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2308_04079",
        "label": "3DGS",
        "title": "3D Gaussian Splatting for Real-Time Radiance Field Rendering",
        "authors": [
          "Kerbl",
          "Kopanas",
          "Leimkühler"
        ],
        "year": 2023,
        "category": "Computer Graphics",
        "sub_category": null,
        "tags": [
          "3DGS",
          "Gaussian splat",
          "Gaussian splatting",
          "3D scene",
          "Rendering",
          "Real-time",
          "GPU",
          "Ellipsoid"
        ],
        "summary": "Seminal paper that introduced 3D Gaussian Splatting, a rendering technique that optimizes the pose, shape, transparency, and view-dependent optic properties (modeled with spherical harmonics) of a large collection of 3D Gaussians (ellipsoidal distributions) to reconstruct a ground truth represented by multiple 2D image views (typically collected by taking photos or video from multiple views around an object or scene). The trained Gaussians are rendered via differentiable tile-based rasterization, enabling high-quality novel view synthesis at real-time frame rates."
      }
    },
    {
      "data": {
        "id": "2309_07872",
        "label": "MS-DDP",
        "title": "A Unified Perspective on Multiple Shooting In Differential Dynamic Programming",
        "authors": [
          "Li",
          "Yu",
          "Zhang"
        ],
        "year": 2023,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Differential dynamic programming",
          "Multiple shooting",
          "Trajectory optimization",
          "Optimal control"
        ],
        "summary": "Provides a unified theoretical framework for multiple-shooting DDP variants, clarifying relationships between existing methods and deriving conditions under which they share convergence guarantees."
      }
    },
    {
      "data": {
        "id": "2309_12566",
        "label": "Kazim et al. 2023",
        "title": "Recent Advances in Path Integral Control for Trajectory Optimization: An Overview in Theoretical and Algorithmic Perspectives",
        "authors": [
          "Kazim",
          "Hong",
          "Kim"
        ],
        "year": 2023,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "MPPI",
          "Path integral control",
          "Survey",
          "Trajectory optimization",
          "Stochastic optimal control",
          "Variational inference"
        ],
        "summary": "Survey paper reviewing the theoretical foundations and algorithmic advances in path integral control methods for trajectory optimization, covering MPPI variants, variational inference approaches, and connections to stochastic optimal control theory."
      }
    },
    {
      "data": {
        "id": "2309_14545",
        "label": "Thomason et al. 2023",
        "title": "Motions in Microseconds via Vectorized Sampling-Based Planning",
        "authors": [
          "Thomason",
          "Kingston",
          "Kavraki"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2309_14595",
        "label": "Huang et al. 2023",
        "title": "Neural Informed RRT*: Learning-based Path Planning with Point Cloud State Representations under Admissible Ellipsoidal Constraints\n",
        "authors": [
          "Huang",
          "Chen",
          "Pohovey"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2310_02918",
        "label": "Bouzidi et al. 2023",
        "title": "Learning-Aided Warmstart of Model Predictive Control in Uncertain Fast-Changing Traffic\n",
        "authors": [
          "Bouzidi",
          "Yao",
          "Goehring"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2310_08710",
        "label": "Gulino et al. 2023",
        "title": "Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research\n",
        "authors": [
          "Gulino",
          "Fu",
          "Luo"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2310_16828",
        "label": "Hansen et al. 2023",
        "title": "TD-MPC2: Scalable, Robust World Models for Continuous Control",
        "authors": [
          "Hansen",
          "Su",
          "Wang"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2310_17274",
        "label": "cuRobo",
        "title": "cuRobo: Parallelized Collision-Free Minimum-Jerk Robot Motion Generation",
        "authors": [
          "Sundaralingam",
          "Hari",
          "Fishman"
        ],
        "year": 2023,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Trajectory optimization",
          "CUDA",
          "GPU",
          "Parallelized",
          "Inverse kinematics",
          "Robot manipulation",
          "Open source",
          "Software"
        ],
        "summary": "CUDA-accelerated library for collision-free robot motion generation. Formulates trajectory generation as a global optimization problem solved across thousands of parallel seeds on GPU. Combines L-BFGS with a novel parallel noisy line search and particle-based optimization to produce minimum-jerk, collision-free trajectories within ~50ms. Also includes a parallel geometric planner (~20ms) and a batched IK solver (>7000 queries/s). An earlier version without minimum-jerk optimization was published at ICRA 2023."
      }
    },
    {
      "data": {
        "id": "2310_17556",
        "label": "Chen et al. 2023",
        "title": "Efficient Numerical Algorithm for Large-Scale Damped Natural Gradient Descent",
        "authors": [
          "Chen",
          "Xie",
          "Wang"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2311_05135",
        "label": "Briden et al. 2023",
        "title": "Improving Computational Efficiency for Powered Descent Guidance via Transformer-based Tight Constraint Prediction\n",
        "authors": [
          "Briden",
          "Gurga",
          "Johnson"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2311_06404",
        "label": "Srikanthan et al. 2023",
        "title": "Augmented Lagrangian Methods as Layered Control Architectures",
        "authors": [
          "Srikanthan",
          "Kumar",
          "Matni"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2311_07411",
        "label": "Jongeneel et al. 2023",
        "title": "A Large Deviations Perspective on Policy Gradient Algorithms",
        "authors": [
          "Jongeneel",
          "Kuhn",
          "Li"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2311_11166",
        "label": "Kolarijani et al. 2023",
        "title": "From Optimization to Control: Quasi Policy Iteration",
        "authors": [
          "Kolarijani",
          "Esfahani"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2311_11489",
        "label": "Jiang et al. 2023",
        "title": "Beyond Nonconvexity: A Universal Trust-Region Method with New Analyses",
        "authors": [
          "Jiang",
          "He",
          "Zhang"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2311_18736",
        "label": "Zhang et al. 2023",
        "title": "Controlgym: Large-Scale Control Environments for Benchmarking Reinforcement Learning Algorithms\n",
        "authors": [
          "Zhang",
          "Mao",
          "Mowlavi"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2312_02758",
        "label": "Yin et al. 2023",
        "title": "Stochastic Data-Driven Predictive Control: Regularization, Estimation, and Constraint Tightening\n",
        "authors": [
          "Yin",
          "Iannelli",
          "Smith"
        ],
        "year": 2023,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2024_calem_action_and_trajectory_prediction",
        "label": "Calem 2024",
        "title": "Action and Trajectory Prediction for Autonomous Driving",
        "authors": [
          "Calem"
        ],
        "year": 2024,
        "category": "Motion Prediction",
        "sub_category": null,
        "tags": [
          "Action prediction",
          "Trajectory prediction",
          "Trajectory forecasting",
          "Autonomous driving",
          "Reinforcement learning",
          "Diversity",
          "Discovery",
          "Deep learning"
        ],
        "summary": "PhD thesis covering action and trajectory prediction methods for autonomous driving."
      }
    },
    {
      "data": {
        "id": "2024_jallet_real_time_constrained_trajectory",
        "label": "Jallet 2024",
        "title": "Real-time Constrained Trajectory Optimization in Robotics: Theory, Implementation and Applications",
        "authors": [
          "Jallet"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Robotics",
          "Real-time",
          "Real-time optimization",
          "Real-time control",
          "Augmented Lagrangian",
          "Primal-dual",
          "iLQR",
          "DDP",
          "Proximal DDP",
          "ProxDDP",
          "Constraint programming",
          "Constrained optimal control",
          "Multiple-shooting",
          "Aligator",
          "Library"
        ],
        "summary": "PhD dissertation by Wilson Jallet covering the ProxDDP algorithm and the Aligator library. Good discussion on recent works in constrained DDP e.g. ALTRO, primal-dual iLQR, etc."
      }
    },
    {
      "data": {
        "id": "2024_wang_a_convergence_guaranteed_multiple",
        "label": "MS-DDP",
        "title": "A Convergence Guaranteed Multiple-Shooting DDP Method for Optimization-Based Robot Motion Planning",
        "authors": [
          "Wang",
          "Li",
          "Chen"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Differential dynamic programming",
          "Multiple shooting",
          "Trajectory optimization",
          "Robot motion planning",
          "Convergence guarantees"
        ],
        "summary": "Proposes a multiple-shooting DDP method with formal convergence guarantees obtained by using a state augmentation strategy."
      }
    },
    {
      "data": {
        "id": "2401_09241",
        "label": "Biased-MPPI",
        "title": "Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers",
        "authors": [
          "Trevisan",
          "Alonso-Mora"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "MPPI",
          "Trajectory optimization",
          "Sampling-based control",
          "Informed sampling",
          "Ancillary controller"
        ],
        "summary": "Biased-MPPI augments the MPPI sampling distribution by biasing it toward trajectories suggested by one or more ancillary controllers (e.g., path-following or optimization-based), improving sample efficiency and trajectory quality while preserving the exploration benefits of random sampling."
      }
    },
    {
      "data": {
        "id": "2401_13662",
        "label": "Lehmann 2024",
        "title": "The Definitive Guide to Policy Gradients in Deep Reinforcement Learning: Theory, Algorithms and Implementations\n",
        "authors": [
          "Lehmann"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2401_15185",
        "label": "Matni et al. 2024",
        "title": "Towards a Theory of Control Architecture: A quantitative framework for layered multi-rate control\n",
        "authors": [
          "Matni",
          "Ames",
          "Doyle"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2401_16025",
        "label": "SPO",
        "title": "Simple Policy Optimization",
        "authors": [
          "Xie",
          "Zhang",
          "Yang"
        ],
        "year": 2024,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Reinforcement learning",
          "Policy optimization",
          "Proximal policy optimization",
          "PPO",
          "Simple policy optimization",
          "SPO"
        ],
        "summary": "Proposes a modified policy gradient loss that achieves better performance than PPO while maintaining simplicity."
      }
    },
    {
      "data": {
        "id": "2402_01443",
        "label": "FRENETIX",
        "title": "FRENETIX: A High-Performance and Modular Motion Planning Framework for Autonomous Driving",
        "authors": [
          "Trauth",
          "Moller",
          "Wuersching"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Frameworks & Stack Architectures",
        "tags": [
          "Motion planning",
          "Frenet frame",
          "Autonomous driving",
          "Modular",
          "High performance",
          "CommonRoad"
        ],
        "summary": "Introduces FRENETIX, a high-performance and modular motion planning framework for autonomous driving built around Frenet-frame trajectory sampling. Features a Python/C++ implementation with CommonRoad compatibility, achieving real-time performance through parallelized sampling and efficient trajectory evaluation."
      }
    },
    {
      "data": {
        "id": "2402_03300",
        "label": "GRPO",
        "title": "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models",
        "authors": [
          "Shao",
          "Wang",
          "Zhu"
        ],
        "year": 2024,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Reinforcement learning",
          "Policy optimization",
          "GRPO",
          "Large language models",
          "Mathematical reasoning"
        ],
        "summary": "Introduces GRPO (Group Relative Policy Optimization), a memory-efficient RL variant that replaces the PPO critic with group-relative reward normalization. Historically this caused a big buzz in the Machine Learning world because it was used to train DeepSeek R1, an open weights LLM from China that performed nearly as well as leading closed weights LLMs from the USA. Nevertheless, GRPO is very similar to the REINFORCE policy gradient algorithm, c.f. [A vision researcher's guide to some RL stuff: PPO & GRPO - Yuge (Jimmy) Shi](https://yugeten.github.io/posts/2025/01/ppogrpo/)"
      }
    },
    {
      "data": {
        "id": "2402_03893",
        "label": "Sánchez et al. 2024",
        "title": "Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency",
        "authors": [
          "Sánchez",
          "Ploeg",
          "Smit"
        ],
        "year": 2024,
        "category": "Motion Prediction",
        "sub_category": null,
        "tags": [
          "Motion prediction",
          "Prediction horizon",
          "Automated driving",
          "Safety",
          "Comfort",
          "Efficiency"
        ],
        "summary": "Analyzes how the required prediction horizon for autonomous driving depends on the competing objectives of safety, comfort, and efficiency, providing a framework for selecting appropriate prediction horizons for different driving scenarios and speed profiles."
      }
    },
    {
      "data": {
        "id": "2403_00748",
        "label": "Primal-Dual iLQR",
        "title": "Primal-Dual iLQR",
        "authors": [
          "Sousa-Pinto",
          "Orban"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "iLQR",
          "Trajectory optimization",
          "Constrained optimization",
          "Primal-dual methods",
          "Nonlinear optimal control",
          "JAX"
        ],
        "summary": "Introduces Primal-Dual iLQR, incorporating both primal and dual (Lagrange multiplier) variable updates within the iLQR backward/forward pass, enabling constrained trajectory optimization with favorable convergence properties."
      }
    },
    {
      "data": {
        "id": "2403_01194",
        "label": "Tengesdal et al. 2024",
        "title": "A Comparative Study of Rapidly-exploring Random Tree Algorithms Applied to Ship Trajectory Planning and Behavior Generation",
        "authors": [
          "Tengesdal",
          "Pedersen",
          "Johansen"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Surveys & Comparative Studies",
        "tags": [
          "RRT",
          "Rapidly-exploring random trees",
          "Comparison study",
          "Ship trajectory planning",
          "Scenario generation",
          "Electronic navigational charts",
          "R-trees",
          "Constrained delaunay triangulation"
        ],
        "summary": "Compares variations of RRT in an application domain for marine ship navigation. The dynamic model is basically the same as for car-like vehicles."
      }
    },
    {
      "data": {
        "id": "2403_02751",
        "label": "Chen et al. 2024",
        "title": "Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps",
        "authors": [
          "Chen",
          "Shorinwa",
          "Bruno"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2403_05466",
        "label": "Xiang et al. 2024",
        "title": "Grasping Trajectory Optimization with Point Clouds",
        "authors": [
          "Xiang",
          "Allu",
          "Peddi"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2403_09110",
        "label": "SINDy-RL",
        "title": "SINDy-RL: Interpretable and Efficient Model-Based Reinforcement Learning",
        "authors": [
          "Zolman",
          "Fasel",
          "Kutz"
        ],
        "year": 2024,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Reinforcement learning",
          "SINDy",
          "Model-based RL",
          "Interpretable AI",
          "Data-driven methods"
        ],
        "summary": "Combines SINDy with model-based RL: a SINDy surrogate world model replaces the environment for policy training, yielding interpretable dynamics models and improved sample efficiency compared to black-box neural network surrogates."
      }
    },
    {
      "data": {
        "id": "2403_10745",
        "label": "iDb-RRT",
        "title": "iDb-RRT: Sampling-based Kinodynamic Motion Planning with Motion Primitives and Trajectory Optimization",
        "authors": [
          "Ortiz-Haro",
          "Hönig",
          "Hartmann"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Kinodynamic planning",
          "RRT",
          "iDb-RRT",
          "Motion primitives",
          "Trajectory optimization",
          "Discontinuity bounded"
        ],
        "summary": "Combines short motion primitives (allowing bounded discontinuities) with the RRT exploration strategy, iteratively repairing discontinuities via trajectory optimization. Finds solutions up to 10X faster than prior methods across a benchmark of 30 problems."
      }
    },
    {
      "data": {
        "id": "2403_14606",
        "label": "Blondel et al. 2024",
        "title": "The Elements of Differentiable Programming",
        "authors": [
          "Blondel",
          "Roulet"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2403_18972",
        "label": "Akella et al. 2024",
        "title": "Risk-Aware Robotics: Tail Risk Measures in Planning, Control, and Verification",
        "authors": [
          "Akella",
          "Dixit",
          "Ahmadi"
        ],
        "year": 2024,
        "category": "Safety, Testing & Verification",
        "sub_category": null,
        "tags": [
          "Survey",
          "Safety",
          "Risk",
          "Tail risk",
          "Planning",
          "Control",
          "Verification"
        ],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2405_03281",
        "label": "FDSPC",
        "title": "FDSPC: Fast and Direct Smooth Path Planning via Continuous Curvature Integration",
        "authors": [
          "Chen",
          "Shao",
          "Liu"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Path planning",
          "Smooth paths",
          "Curvature continuity",
          "Heuristic"
        ],
        "summary": "Proposes FDSPC, a global path planner that directly produces G2 smooth paths via continuous curvature integration. It essentially uses a goal-directed heuristic for selecting (otherwise unspecified) yaw angles at sampled positions, rather than attempting to connect (x, y, yaw) boundary poses directly."
      }
    },
    {
      "data": {
        "id": "2406_02807",
        "label": "Ramsey et al. 2024",
        "title": "Collision-Affording Point Trees: SIMD-Amenable Nearest Neighbors for Fast Collision Checking\n",
        "authors": [
          "Ramsey",
          "Kingston",
          "Thomason"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2406_05846",
        "label": "Kang et al. 2024",
        "title": "Fast and Certifiable Trajectory Optimization",
        "authors": [
          "Kang",
          "Xu",
          "Sarva"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2406_16793",
        "label": "Zhang et al. 2024",
        "title": "Adam-mini: Use Fewer Learning Rates To Gain More",
        "authors": [
          "Zhang",
          "Chen",
          "Li"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2406_19617",
        "label": "Yu et al. 2024",
        "title": "Stochastic Zeroth-Order Optimization under Strongly Convexity and Lipschitz Hessian: Minimax Sample Complexity\n",
        "authors": [
          "Yu",
          "Wang",
          "Huang"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2407_15007",
        "label": "Foster et al. 2024",
        "title": "Is Behavior Cloning All You Need? Understanding Horizon in Imitation Learning",
        "authors": [
          "Foster",
          "Block",
          "Misra"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2409_06807",
        "label": "Kino-PAX",
        "title": "Kino-PAX: Highly Parallel Kinodynamic Sampling-based Planner",
        "authors": [
          "Perrault",
          "Ho",
          "Lahijanian"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Sampling-based planning",
          "Kinodynamic planning",
          "GPU",
          "Parallelized",
          "Real-time planning"
        ],
        "summary": "GPU-native kinodynamic sampling-based planner that decomposes the traditionally serial RRT tree-growth process into three massively parallel subroutines. The design aligns with GPU execution hierarchies: independent threads, balanced workloads, low-latency shared memory."
      }
    },
    {
      "data": {
        "id": "2409_09523",
        "label": "Lab2Car",
        "title": "Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-World Environments",
        "authors": [
          "Heim",
          "Suarez-Ruiz",
          "Bhuiyan"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Machine Learning in Motion Planning",
        "tags": [
          "Motion planning",
          "Autonomous driving",
          "Trajectory optimization",
          "Safety",
          "Real-world deployment",
          "Experimentation"
        ],
        "summary": "Optimization-based wrapper that converts any planner's trajectory sketch into a safe, comfortable, dynamically feasible trajectory, enabling rapid real-world testing of experimental ML and classical planners on self-driving vehicles without full safety-stack integration."
      }
    },
    {
      "data": {
        "id": "2409_11649",
        "label": "Aoyama et al. 2024",
        "title": "Second-Order Constrained Dynamic Optimization",
        "authors": [
          "Aoyama",
          "So",
          "Saravanos"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Differential dynamic programming",
          "Second-order methods",
          "Constrained optimization",
          "Trajectory optimization"
        ],
        "summary": "Comparative study over the variations of differential dynamic programming for constrained trajectory optimization problems, including interior-point, augmented Lagrangian, primal-dual, and sequential quadratic programming techniques."
      }
    },
    {
      "data": {
        "id": "2409_12266",
        "label": "C-Uniform MPPI",
        "title": "C-Uniform Trajectory Sampling For Fast Motion Planning",
        "authors": [
          "Poyrazoglu",
          "Cao",
          "Isler"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "MPPI",
          "Trajectory optimization",
          "Sampling-based control",
          "Action sampling",
          "Reachable sets",
          "Configuration space"
        ],
        "summary": "Proposes a C-Uniform action sampling distribution based on the dynamically reachable sets of the controlled system, enabling far more efficient exploration of trajectory space compared to naive Gaussian sampling, especially for tight obstacle avoidance. Offline training takes ~4 hours for a 3-state unicycle model, but runtime cost matches naive sampling."
      }
    },
    {
      "data": {
        "id": "2409_14562",
        "label": "Li et al. 2024",
        "title": "DROP: Dexterous Reorientation via Online Planning",
        "authors": [
          "Li",
          "Culbertson",
          "Kurtz"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2409_15610",
        "label": "DIAL-MPC",
        "title": "Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing",
        "authors": [
          "Xue",
          "Pan",
          "Yi"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "MPPI",
          "Diffusion",
          "Locomotion",
          "Model predictive control",
          "Annealing"
        ],
        "summary": "Takes a perspective of treating MPPI as a single step of a denoising diffusion process, and generalizes this process to a multi-step diffusion-style annealing process. DIAL-MPC starts optimizing the control sequence with smooth but inaccurate objectives and gradually shifts to more accurate local objectives."
      }
    },
    {
      "data": {
        "id": "2409_16012",
        "label": "PRESTO",
        "title": "PRESTO: Fast Motion Planning Using Diffusion Models Based on Key-Configuration Environment Representation",
        "authors": [
          "Seo",
          "Cho",
          "Sung"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Machine Learning in Motion Planning",
        "tags": [
          "PRESTO",
          "Motion planning",
          "Diffusion",
          "Diffusion models",
          "Trajectory optimization",
          "Collision-free"
        ],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2409_16915",
        "label": "SPLANNING",
        "title": "Let's Make a Splan: Risk-Aware Trajectory Optimization in a Normalized Gaussian Splat",
        "authors": [
          "Michaux",
          "Isaacson",
          "Adu"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Gaussian splatting",
          "3DGS",
          "Risk-aware planning",
          "3D scene",
          "Representation"
        ],
        "summary": "Proposes trajectory optimization directly within a Normalized Gaussian Splat (NGS) scene representation, treating Gaussian density as a risk measure to enable risk-aware collision avoidance without requiring explicit geometric extraction."
      }
    },
    {
      "data": {
        "id": "2410_04083",
        "label": "Kamzolov et al. 2024",
        "title": "OPTAMI: Global Superlinear Convergence of High-order Methods",
        "authors": [
          "Kamzolov",
          "Pasechnyuk",
          "Agafonov"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2410_13732",
        "label": "Bermeitinger et al. 2024",
        "title": "Reducing the Transformer Architecture to a Minimum",
        "authors": [
          "Bermeitinger",
          "Hrycej",
          "Pavone"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2410_16727",
        "label": "Huang et al. 2024",
        "title": "DiffusionSeeder: Seeding Motion Optimization with Diffusion for Rapid Motion Planning\n",
        "authors": [
          "Huang",
          "Sundaralingam",
          "Mousavian"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2410_19414",
        "label": "Zhang et al. 2024",
        "title": "Motion Planning for Robotics: A Review for Sampling-based Planners",
        "authors": [
          "Zhang",
          "Cai",
          "Sun"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Surveys & Comparative Studies",
        "tags": [
          "Survey",
          "Motion planning",
          "Robot motion planning",
          "Sampling-based planning",
          "Robotics",
          "Benchmarking"
        ],
        "summary": "Reviews ten popular sampling-based motion planners for robotic applications, analyzing their theoretical properties and empirical performance across diverse planning scenarios to highlight ongoing research challenges in the field."
      }
    },
    {
      "data": {
        "id": "2410_23916",
        "label": "Celestini et al. 2024",
        "title": "Transformer-based Model Predictive Control: Trajectory Optimization via Sequence Modeling\n",
        "authors": [
          "Celestini",
          "Gammelli",
          "Guffanti"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2411_02158",
        "label": "MISO",
        "title": "Learning Multiple Initial Solutions to Optimization Problems",
        "authors": [
          "Sharony",
          "Yang",
          "Che"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Learning",
          "Warm-starting",
          "Multi-modal optimization",
          "Neural network"
        ],
        "summary": "Learns a generative model that produces multiple diverse initial solutions for optimization problems, enabling warm-started solvers to explore different basins of attraction and improve the probability of finding high-quality global optima."
      }
    },
    {
      "data": {
        "id": "2411_03277",
        "label": "Jongeneel 2024",
        "title": "Asymptotic stability equals exponential stability -- while you twist your eyes",
        "authors": [
          "Jongeneel"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2411_11833",
        "label": "cuTAMP",
        "title": "Differentiable GPU-Parallelized Task and Motion Planning",
        "authors": [
          "Shen",
          "Garrett",
          "Kumar"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Task and motion planning",
          "TAMP",
          "CUDA",
          "GPU",
          "Parallelized",
          "Differentiable optimization",
          "Robot manipulation",
          "Bilevel planning"
        ],
        "summary": "Exploits GPU parallelism to simultaneously evaluate thousands of candidate continuous parameter seeds for a given plan skeleton, then applies differentiable gradient-based optimization to each seed in parallel to satisfy the induced continuous constraint satisfaction problem. This combines the discrete search of classical TAMP with massively parallel differentiable optimization, significantly reducing solve times for long-horizon manipulation tasks in highly constrained settings."
      }
    },
    {
      "data": {
        "id": "2411_15651",
        "label": "MPT",
        "title": "Model Predictive Trees: Sample-Efficient Receding Horizon Planning with Reusable Tree Search",
        "authors": [
          "Lathrop",
          "Rivière",
          "Alindogan"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Model Predictive Control",
          "Tree search",
          "Monte Carlo Tree Search",
          "Receding horizon planning",
          "Motion planning",
          "Robotics",
          "Sample efficiency"
        ],
        "summary": "Proposes reusing the entire optimal subtree (not just the best trajectory) across receding horizon planning steps, enabling simultaneous refinement toward better solutions and away from worse ones."
      }
    },
    {
      "data": {
        "id": "2411_17293",
        "label": "Dang et al. 2024",
        "title": "SIL-RRT*: Learning Sampling Distribution through Self Imitation Learning",
        "authors": [
          "Dang",
          "Edelkamp"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2411_17902",
        "label": "FCIT*",
        "title": "Nearest-Neighbourless Asymptotically Optimal Motion Planning with Fully Connected Informed Trees (FCIT*)",
        "authors": [
          "Wilson",
          "Thomason",
          "Kingston"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Sampling-based planning",
          "High-dimensional planning",
          "Anytime planning",
          "Asymptotic optimality",
          "FCIT*",
          "BIT*",
          "SIMD",
          "Hardware acceleration"
        ],
        "summary": "Use SIMD instructions to evaluate edge costs to every neighbor (hence eliminating expensive nearest neighbor routine) in Informed RRT*. Gives huge empirical computational end-to-end planning time."
      }
    },
    {
      "data": {
        "id": "2411_18714",
        "label": "Kenny et al. 2024",
        "title": "Explainable deep learning improves human mental models of self-driving cars",
        "authors": [
          "Kenny",
          "Dharmavaram",
          "Lee"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2412_11270",
        "label": "SETS",
        "title": "Monte Carlo Tree Search with Spectral Expansion for Planning with Dynamical Systems",
        "authors": [
          "Rivière",
          "Lathrop",
          "Chung"
        ],
        "year": 2024,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory planning",
          "Motion planning",
          "Monte Carlo Tree Search",
          "MCTS",
          "Spectral methods",
          "Dynamical systems",
          "Real-time planning",
          "Nonlinear systems",
          "Underactuated systems",
          "MDP"
        ],
        "summary": "Bridges Monte Carlo Tree Search and continuous physical dynamics by using the spectrum of locally linearized systems to build a low-complexity discrete model."
      }
    },
    {
      "data": {
        "id": "2412_12036",
        "label": "Singh et al. 2024",
        "title": "LeARN: Learnable and Adaptive Representations for Nonlinear Dynamics in System Identification\n",
        "authors": [
          "Singh",
          "Mukherjee"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2412_14415",
        "label": "Huang et al. 2024",
        "title": "DriveGPT: Scaling Autoregressive Behavior Models for Driving",
        "authors": [
          "Huang",
          "Wolff",
          "Vernaza"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2412_17920",
        "label": "Lin et al. 2024",
        "title": "Causal Composition Diffusion Model for Closed-loop Traffic Generation",
        "authors": [
          "Lin",
          "Huang",
          "Phan-Minh"
        ],
        "year": 2024,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2025_crestaz_td_cd_mppi_temporal",
        "label": "TD-CD-MPPI",
        "title": "TD-CD-MPPI: Temporal-Difference Constraint-Discounted Model Predictive Path Integral Control",
        "authors": [
          "Crestaz",
          "Matteis",
          "Chane-Sane"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "MPPI",
          "Trajectory optimization",
          "Constraint handling",
          "Temporal difference",
          "Safety"
        ],
        "summary": "TD-CD-MPPI enables the use of reduced control horizons by using a learned terminal value function to approximate long-term returns."
      }
    },
    {
      "data": {
        "id": "2025_hu_technically_speaking_transitioning_from",
        "label": "Hu 2025",
        "title": "Technically Speaking: Transitioning from Rule-Based to ML-Powered Motion Planning",
        "authors": [
          "Hu"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Machine Learning in Motion Planning",
        "tags": [
          "Autonomous driving",
          "Motion planning",
          "Machine learning",
          "Reinforcement learning",
          "End-to-end learning"
        ],
        "summary": "Overview of Motional's approach to motion planning: a scene encoder-generator-ranker architecture with joint prediction and planning, closed-loop reinforcement learning training, and data mining for real-world scalability."
      }
    },
    {
      "data": {
        "id": "2025_lee_time_correlated_model_predictive",
        "label": "TC-MPPI",
        "title": "Time-Correlated Model Predictive Path Integral: Smooth Action Generation for Sampling-Based Control",
        "authors": [
          "Lee",
          "Lee"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "MPPI",
          "Trajectory optimization",
          "Sampling-based control",
          "Action smoothing",
          "Time correlation"
        ],
        "summary": "Introduces temporally correlated noise sampling in MPPI to generate smoother action sequences, improving trajectory quality for sampling-based model predictive control of underactuated systems."
      }
    },
    {
      "data": {
        "id": "2025_trevisan_model_predictive_path_integral",
        "label": "Trevisan 2025",
        "title": "Model Predictive Path Integral Control for Interaction-Rich Local Motion Planning in Dynamic Environments",
        "authors": [
          "Trevisan"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "MPPI",
          "Trajectory optimization",
          "Interaction-aware planning",
          "Dynamic environments",
          "Motion planning"
        ],
        "summary": "Incorporates a trajectory prediction model into MPPI to enable interaction-aware trajectory planning."
      }
    },
    {
      "data": {
        "id": "2025_xia_an_adaptive_projection_differential",
        "label": "AP-DDP",
        "title": "An Adaptive Projection Differential Dynamic Programming Method for Control Constrained Trajectory Optimization",
        "authors": [
          "Xia",
          "Wu"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Differential dynamic programming",
          "Constrained optimization",
          "Control constraints",
          "Projection methods",
          "Trajectory optimization"
        ],
        "summary": "Proposes an adaptive projection method within the DDP framework for handling control constraints, using projection operators that adapt based on constraint activity to achieve efficient and convergent constrained trajectory optimization."
      }
    },
    {
      "data": {
        "id": "2501_05204",
        "label": "Grandia et al. 2025",
        "title": "Design and Control of a Bipedal Robotic Character",
        "authors": [
          "Grandia",
          "Knoop",
          "Hopkins"
        ],
        "year": 2025,
        "category": "Just for Fun",
        "sub_category": null,
        "tags": [
          "Robot",
          "Disney",
          "Animation",
          "Mechatronics",
          "Legged robots"
        ],
        "summary": "The Disney Research folks have created a cute small robot with surprisingly lifelike movements controllable from a gamepad. Fun!"
      }
    },
    {
      "data": {
        "id": "2502_04799",
        "label": "Zhou et al. 2025",
        "title": "A Regularized Newton Method for Nonconvex Optimization with Global and Local Complexity Guarantees\n",
        "authors": [
          "Zhou",
          "Xu",
          "Li"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2502_08664",
        "label": "Shi et al. 2025",
        "title": "Motion Forecasting for Autonomous Vehicles: A Survey",
        "authors": [
          "Shi",
          "Chen",
          "Wang"
        ],
        "year": 2025,
        "category": "Motion Prediction",
        "sub_category": null,
        "tags": [
          "Motion forecasting",
          "Autonomous vehicles",
          "Survey",
          "Trajectory prediction"
        ],
        "summary": "Comprehensive survey of motion forecasting methods for autonomous vehicles, covering classical physics-based approaches through modern deep learning methods, with discussion of datasets, metrics, and open problems."
      }
    },
    {
      "data": {
        "id": "2502_08844",
        "label": "Zakka et al. 2025",
        "title": "MuJoCo Playground",
        "authors": [
          "Zakka",
          "Tabanpour",
          "Liao"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2502_09556",
        "label": "RT-FMT",
        "title": "Real-Time Fast Marching Tree for Mobile Robot Motion Planning in Dynamic Environments",
        "authors": [
          "Silveira",
          "Cabral",
          "Givigi"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Sampling-based planning",
          "Dynamic environments",
          "Replanning",
          "FMT*",
          "Real-time planning"
        ],
        "summary": "Basically makes FMT* operable in real-time fashion. Essentially the FMT* version of RT-RRT*."
      }
    },
    {
      "data": {
        "id": "2502_12310",
        "label": "Fujinami et al. 2025",
        "title": "Domain Randomization is Sample Efficient for Linear Quadratic Control",
        "authors": [
          "Fujinami",
          "Lee",
          "Matni"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2503_00385",
        "label": "Pan et al. 2025",
        "title": "Model-Agnostic Meta-Policy Optimization via Zeroth-Order Estimation: A Linear Quadratic Regulator Perspective\n",
        "authors": [
          "Pan",
          "Li",
          "Zhu"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2503_03262",
        "label": "Madjid et al. 2025",
        "title": "Trajectory Prediction for Autonomous Driving: Progress, Limitations, and Future Directions",
        "authors": [
          "Madjid",
          "Ahmad",
          "Mebrahtu"
        ],
        "year": 2025,
        "category": "Motion Prediction",
        "sub_category": null,
        "tags": [
          "Trajectory prediction",
          "Autonomous driving",
          "Survey",
          "Motion forecasting"
        ],
        "summary": "Reviews progress in trajectory prediction for autonomous driving, systematically discussing limitations of current approaches and outlining promising future research directions."
      }
    },
    {
      "data": {
        "id": "2503_04613",
        "label": "Zhang et al. 2025",
        "title": "Whole-Body Model-Predictive Control of Legged Robots with MuJoCo",
        "authors": [
          "Zhang",
          "Howell",
          "Yi"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2503_05819",
        "label": "CU-MPPI",
        "title": "An Unsupervised C-Uniform Trajectory Sampler with Applications to Model Predictive Path Integral Control",
        "authors": [
          "Poyrazoglu",
          "Moorthy",
          "Cao"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "MPPI",
          "Trajectory optimization",
          "Sampling-based control",
          "Action sampling distribution",
          "Neural network",
          "Reachable sets"
        ],
        "summary": "Extension of C-Uniform trajectory sampling that trains a neural network to approximate the reachable-set-based sampling distribution in an unsupervised manner, achieving similar reachable state coverage as the original method with dramatically faster training time."
      }
    },
    {
      "data": {
        "id": "2503_06135",
        "label": "Nguyen et al. 2025",
        "title": "FlowMP: Learning Motion Fields for Robot Planning with Conditional Flow Matching",
        "authors": [
          "Nguyen",
          "Le",
          "Pham"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2503_06757",
        "label": "pRRTC",
        "title": "pRRTC: GPU-Parallel RRT-Connect for Fast, Consistent, and Low-Cost Motion Planning",
        "authors": [
          "Huang",
          "Jadhav",
          "Plancher"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Sampling-based planning",
          "GPU",
          "Parallelized",
          "SIMT",
          "CUDA",
          "Collision checking",
          "High-dimensional planning",
          "pRRTC",
          "RRT-Connect"
        ],
        "summary": "GPU-accelerated RRT-Connect implementation co-designed for three hierarchical levels of parallelism: concurrent bidirectional tree expansion across GPU thread blocks, SIMT-optimized parallel collision checking within each block, and thread-level forward kinematics."
      }
    },
    {
      "data": {
        "id": "2503_09722",
        "label": "Simchowitz et al. 2025",
        "title": "The Pitfalls of Imitation Learning when Actions are Continuous",
        "authors": [
          "Simchowitz",
          "Pfrommer",
          "Jadbabaie"
        ],
        "year": 2025,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Imitation learning",
          "Behavior cloning",
          "Action chunking",
          "Continuous control",
          "Diffusion Policy"
        ],
        "summary": "Provides theoretical analysis explaining why action chunking and high-capacity policy representations (Transformers, Diffusion Policy) outperform smooth or low-capacity representations in behavior cloning with continuous actions."
      }
    },
    {
      "data": {
        "id": "2503_11717",
        "label": "Low-pass MPPI",
        "title": "Low-pass Sampling in Model Predictive Path Integral Control",
        "authors": [
          "Kicki"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "MPPI",
          "Trajectory optimization",
          "Sampling-based control",
          "Action smoothing",
          "Low-pass filter"
        ],
        "summary": "Applies a low-pass filter to Gaussian noise before using it as sampled action sequences in MPPI, a heuristic that produces smoother trajectories and can improve exploration quality with minimal computational overhead."
      }
    },
    {
      "data": {
        "id": "2503_16164",
        "label": "Kříž et al. 2025",
        "title": "Asymptotically Optimal Path Planning With an Approximation of the Omniscient Set",
        "authors": [
          "Kříž",
          "Vonásek"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2503_24371",
        "label": "Fujinami et al. 2025",
        "title": "Policy Gradient for LQR with Domain Randomization",
        "authors": [
          "Fujinami",
          "Lee",
          "Matni"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2504_01766",
        "label": "Somalwar et al. 2025",
        "title": "Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error\n",
        "authors": [
          "Somalwar",
          "Lee",
          "Pappas"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2504_06437",
        "label": "DBaS-Log-MPPI",
        "title": "DBaS-Log-MPPI: Efficient and Safe Trajectory Optimization via Barrier States",
        "authors": [
          "Wang",
          "Jiang",
          "Tao"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "MPPI",
          "Trajectory optimization",
          "Safety",
          "Barrier states",
          "Constraint satisfaction"
        ],
        "summary": "Integrates logarithmic barrier states (DBaS) into the dynamics, providing smooth cost shaping that discourages safety constraint violations."
      }
    },
    {
      "data": {
        "id": "2504_12905",
        "label": "Pehlivan et al. 2025",
        "title": "Matrix-free Second-order Optimization of Gaussian Splats with Residual Sampling",
        "authors": [
          "Pehlivan",
          "Camiletto",
          "Foo"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2504_18978",
        "label": "Marcucci et al. 2025",
        "title": "A Biconvex Method for Minimum-Time Motion Planning Through Sequences of Convex Sets",
        "authors": [
          "Marcucci",
          "Halm",
          "Yang"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Motion planning",
          "Trajectory optimization",
          "Convex optimization",
          "Minimum-time planning",
          "GCS",
          "Bezier curves"
        ],
        "summary": "Addresses minimum-time trajectory design through a fixed sequence of convex sets subject to velocity and acceleration constraints - a problem that is natively nonconvex due to the coupling between time scaling and path shape. The proposed biconvex method alternates between two convex subproblems, quickly generating a feasible initial trajectory and iteratively refining it without line-search parameters."
      }
    },
    {
      "data": {
        "id": "2505_05507",
        "label": "VIMPPI",
        "title": "VIMPPI: Enhancing Model Predictive Path Integral Control with Variational Integration for Underactuated Systems",
        "authors": [
          "Alentev",
          "Kozlov",
          "Domrachev"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "MPPI",
          "Trajectory optimization",
          "Sampling-based control",
          "Variational integration",
          "Underactuated systems"
        ],
        "summary": "Enhances MPPI with variational integration (VI) to accurately simulate the system evolution inside an MPPI over long planning horizons."
      }
    },
    {
      "data": {
        "id": "2505_05588",
        "label": "Banerjee et al. 2025",
        "title": "Deep Learning Warm Starts for Trajectory Optimization on the International Space Station\n",
        "authors": [
          "Banerjee",
          "Cauligi",
          "Pavone"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2505_06791",
        "label": "Hu et al. 2025",
        "title": "cpRRTC: GPU-Parallel RRT-Connect for Constrained Motion Planning",
        "authors": [
          "Hu",
          "Wang",
          "Christensen"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2505_08510",
        "label": "FOCI",
        "title": "FOCI: Trajectory Optimization on Gaussian Splats",
        "authors": [
          "Andreu",
          "Wilder-Smith",
          "Klemm"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Gaussian splatting",
          "3DGS",
          "3D scene",
          "Representation"
        ],
        "summary": "FOCI is a trajectory optimization method that operates directly on Gaussian Splat scene representations."
      }
    },
    {
      "data": {
        "id": "2505_09074",
        "label": "Wang et al. 2025",
        "title": "Trends in Motion Prediction Toward Deployable and Generalizable Autonomy: A Revisit and Perspectives",
        "authors": [
          "Wang",
          "Lavoie",
          "Papais"
        ],
        "year": 2025,
        "category": "Motion Prediction",
        "sub_category": null,
        "tags": [
          "Motion prediction",
          "Autonomous driving",
          "Survey",
          "Taxonomy",
          "Generalization",
          "Deployment"
        ],
        "summary": "Surveys the state-of-the-art in motion prediction for autonomous driving with a focus on real-world deployability and generalization, providing a taxonomy of approaches and discussing open challenges for bringing prediction models from research to production."
      }
    },
    {
      "data": {
        "id": "2505_10542",
        "label": "AORRTC",
        "title": "AORRTC: Almost-Surely Asymptotically Optimal Planning with RRT-Connect",
        "authors": [
          "Wilson",
          "Thomason",
          "Kingston"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Motion planning",
          "Sampling-based planning",
          "Asymptotic optimality",
          "Anytime planning",
          "Bidirectional search",
          "RRT-Connect",
          "SIMD",
          "High-dimensional planning"
        ],
        "summary": "Applies the AO-x meta-algorithm to RRT-Connect, inheriting its fast initial solution times while adding almost-sure asymptotic optimality. With SIMD acceleration, AORRTC solves difficult high-DoF problems (Panda, Fetch robots) in milliseconds where other almost-surely asymptotically optimal planners failed to find solutions even with seconds of planning time."
      }
    },
    {
      "data": {
        "id": "2505_21851",
        "label": "Streaming Flow Policy",
        "title": "Streaming Flow Policy: Simplifying Diffusion/Flow-Matching Policies by Treating Action Trajectories as Flow Trajectories",
        "authors": [
          "Jiang",
          "Fang",
          "Roy"
        ],
        "year": 2025,
        "category": "Reinforcement Learning",
        "sub_category": null,
        "tags": [
          "Flow matching",
          "Diffusion models",
          "Robot learning",
          "Imitation learning",
          "Visuomotor policy",
          "Streaming flow policy"
        ],
        "summary": "Simplifies flow-matching robot policies by treating the entire action trajectory as a flow trajectory rather than denoising per-timestep, reducing inference overhead while maintaining expressive multimodal action distributions."
      }
    },
    {
      "data": {
        "id": "2506_05454",
        "label": "Zhang et al. 2025",
        "title": "Zeroth-Order Optimization Finds Flat Minima",
        "authors": [
          "Zhang",
          "Li",
          "Thekumparampil"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2506_11513",
        "label": "Schaller et al. 2025",
        "title": "Automatic Generation of Explicit Quadratic Programming Solvers",
        "authors": [
          "Schaller",
          "Arnström",
          "Bemporad"
        ],
        "year": 2025,
        "category": "Optimization",
        "sub_category": null,
        "tags": [
          "Quadratic programming",
          "CVX",
          "CVXPY",
          "CVXPYgen"
        ],
        "summary": "Generates C++ code that solves explicit MPC problems. Super fast runtime for moderate size problems. Alternative to (implicit) quadratic program solvers."
      }
    },
    {
      "data": {
        "id": "2506_14865",
        "label": "ALSPG",
        "title": "Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization",
        "authors": [
          "Chi",
          "Girgin",
          "Löw"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Trajectory optimization",
          "Constrained optimization",
          "Projection methods",
          "Real-time",
          "Robot motion planning"
        ],
        "summary": "Uses geometric projection operations to efficiently handle motion constraints in real-time robot trajectory optimization, avoiding full constraint Jacobian computations and achieving significant speedups over augmented Lagrangian approaches."
      }
    },
    {
      "data": {
        "id": "2506_17184",
        "label": "Judo",
        "title": "Judo: A User-Friendly Open-Source Package for Sampling-Based Model Predictive Control",
        "authors": [
          "Li",
          "Hung",
          "Ames"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Frameworks & Stack Architectures",
        "tags": [
          "Model predictive control",
          "Sampling-based control",
          "MPPI",
          "MuJoCo",
          "Open source",
          "Software",
          "Real-time control"
        ],
        "summary": "Judo is an open-source Python package providing standardized implementations of sampling-based MPC algorithms (MPPI, CEM, Predictive Sampling, etc.), benchmark tasks, and an interactive GUI for controller tuning. It uses MuJoCo as its physics backend for real-time performance, and supports asynchronous execution to ease sim-to-hardware transfer. The focus is on tooling and usability rather than novel algorithmic contributions. One interesting thing is that Judo runs 100% on CPU (by necessity rather than choice, as the authors indicate they are waiting for development of mujoco_warp to stabilize to provide GPU-based sim rollouts). If you get a server grade Threadripper CPU with 64 cores/128 threads you can do amazing things and plan/control in < 2ms."
      }
    },
    {
      "data": {
        "id": "2506_21205",
        "label": "Trevisan et al. 2025",
        "title": "Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations\n",
        "authors": [
          "Trevisan",
          "Mustafa",
          "Notten"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2506_22087",
        "label": "Jordana et al. 2025",
        "title": "An Introduction to Zero-Order Optimization Techniques for Robotics",
        "authors": [
          "Jordana",
          "Zhang",
          "Amigo"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2507_05331",
        "label": "Team et al. 2025",
        "title": "A Careful Examination of Large Behavior Models for Multitask Dexterous Manipulation\n",
        "authors": [
          "Team",
          "Barreiros",
          "Beaulieu"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2507_09061",
        "label": "Zhang et al. 2025",
        "title": "Action Chunking and Exploratory Data Collection Yield Exponential Improvements in Behavior Cloning for Continuous Control\n",
        "authors": [
          "Zhang",
          "Pfrommer",
          "Pan"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2507_19652",
        "label": "Risiglione et al. 2025",
        "title": "RAKOMO: Reachability-Aware K-Order Markov Path Optimization for Quadrupedal Loco-Manipulation\n",
        "authors": [
          "Risiglione",
          "Abdalla",
          "Barasuol"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2508_05027",
        "label": "Huang et al. 2025",
        "title": "Benchmarking Shortcutting Techniques for Multi-Robot-Arm Motion Planning",
        "authors": [
          "Huang",
          "Shaoul",
          "Li"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Path shortcutting",
          "Path optimization",
          "Multi-robot",
          "Robot arm",
          "Benchmarking",
          "Post-processing"
        ],
        "summary": "Systematic benchmark of shortcutting techniques applied to multi-robot-arm motion planning, where high dimensionality and inter-arm collision constraints make path quality improvement especially challenging."
      }
    },
    {
      "data": {
        "id": "2508_07400",
        "label": "Shehab et al. 2025",
        "title": "Efficient Reward Identification in Max Entropy Reinforcement Learning with Sparsity and Rank Priors\n",
        "authors": [
          "Shehab",
          "Tercan",
          "Ozay"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2508_21001",
        "label": "Hassidof et al. 2025",
        "title": "Train-Once Plan-Anywhere Kinodynamic Motion Planning via Diffusion Trees",
        "authors": [
          "Hassidof",
          "Jurgenson",
          "Solovey"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2508_21364",
        "label": "Multi-Modal MPPI",
        "title": "Multi-Modal Model Predictive Path Integral Control for Collision Avoidance",
        "authors": [
          "Bertipaglia",
          "Gavrila",
          "Shyrokau"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "MPPI",
          "Trajectory optimization",
          "Collision avoidance",
          "Multimodal",
          "Sampling-based control"
        ],
        "summary": "Extends MPPI to handle multimodal trajectory distributions for collision avoidance, enabling the controller to simultaneously explore multiple qualitatively different trajectory groups (homotopy classes) rather than collapsing to a single mode."
      }
    },
    {
      "data": {
        "id": "2508_21800",
        "label": "Jeon et al. 2025",
        "title": "Tree-Guided Diffusion Planner",
        "authors": [
          "Jeon",
          "Min",
          "Park"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2509_14978",
        "label": "Zhai et al. 2025",
        "title": "PA-MPPI: Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments\n",
        "authors": [
          "Zhai",
          "Reiter",
          "Scaramuzza"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2509_21961",
        "label": "Wang et al. 2025",
        "title": "FlowDrive: moderated flow matching with data balancing for trajectory planning",
        "authors": [
          "Wang",
          "Taş",
          "Steiner"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2510_00272",
        "label": "BC-MPPI",
        "title": "BC-MPPI: A Probabilistic Constraint Layer for Safe Model-Predictive Path-Integral Control",
        "authors": [
          "Ezeji",
          "Ziegltrum",
          "Turrisi"
        ],
        "year": 2025,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "MPPI",
          "Trajectory optimization",
          "Safety",
          "Bayesian constraints",
          "Probabilistic constraints"
        ],
        "summary": "Adds a Bayesian probabilistic layer to MPPI that models constraint satisfaction as a probability distribution, enabling principled soft constraint handling within the MPPI sampling framework."
      }
    },
    {
      "data": {
        "id": "2510_03745",
        "label": "Huffel et al. 2025",
        "title": "Neural Low-Discrepancy Sequences",
        "authors": [
          "Huffel",
          "Kirk",
          "Chahine"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2510_21074",
        "label": "Sabbadini et al. 2025",
        "title": "Revisiting Replanning from Scratch: Real-Time Incremental Planning with Fast Almost-Surely Asymptotically Optimal Planners\n",
        "authors": [
          "Sabbadini",
          "Liu",
          "Ruan"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2510_22015",
        "label": "You et al. 2025",
        "title": "Motion Planning with Precedence Specifications via Augmented Graphs of Convex Sets\n",
        "authors": [
          "You",
          "Luna",
          "Shaikh"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2511_00088",
        "label": "Alpamayo-R1",
        "title": "Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail",
        "authors": [
          "Wang",
          "Luo",
          "Bai"
        ],
        "year": 2025,
        "category": "Machine Learning",
        "sub_category": null,
        "tags": [
          "Vision-language-action model"
        ],
        "summary": "A large team of authors from NVIDIA has put together a lot of big pieces in a data and deep model architecture pipeline for training and deploying an end-to-end (E2E) vision-language-action (VLA) model for autonomous driving. It is interesting to see this hard push into end-to-end approaches, which the authors motivate by recent advances in \"reasoning\" abilities gained in large language models which is purported to address the safety gap that arises with E2E models."
      }
    },
    {
      "data": {
        "id": "2511_00814",
        "label": "Kombo et al. 2025",
        "title": "Real-Time Learning of Predictive Dynamic Obstacle Models for Robotic Motion Planning",
        "authors": [
          "Kombo",
          "Haseli",
          "Wei"
        ],
        "year": 2025,
        "category": "Motion Prediction",
        "sub_category": null,
        "tags": [
          "Prediction",
          "Dynamic Mode Decomposition"
        ],
        "summary": "Tackles the problem of data-driven motion prediction by using a special kind of Dynamic Mode Decomposition (DMD), which comes from the Koopman operator theory, to learn a model of the agent motion. The model also produces uncertainty estimates, which is useful for downstream risk-aware planning & control. This paper combines a lot of smaller techniques (Hankel-DMD, Cadzow projection, Singular Value Hard Thresholding (SVHT), etc.) together into a rather intricate bells-and-whistles learner, but that in itself is nice as it provides the reader some clues into those techniques."
      }
    },
    {
      "data": {
        "id": "2511_02015",
        "label": "Aldrich et al. 2025",
        "title": "Stein-based Optimization of Sampling Distributions in Model Predictive Path Integral Control\n",
        "authors": [
          "Aldrich",
          "Jenkins"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2511_02095",
        "label": "Valaei et al. 2025",
        "title": "Second-Order Policy Gradient Methods for the Linear Quadratic Regulator",
        "authors": [
          "Valaei",
          "Kordabad",
          "Soudjani"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2511_06385",
        "label": "Römer et al. 2025",
        "title": "From Demonstrations to Safe Deployment: Path-Consistent Safety Filtering for Diffusion Policies\n",
        "authors": [
          "Römer",
          "Balletshofer",
          "Thumm"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2511_10622",
        "label": "Sambharya et al. 2025",
        "title": "Verification of Sequential Convex Programming for Parametric Non-convex Optimization\n",
        "authors": [
          "Sambharya",
          "Matni",
          "Pappas"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2511_10626",
        "label": "Fatkhullin et al. 2025",
        "title": "Global Solutions to Non-Convex Functional Constrained Problems with Hidden Convexity\n",
        "authors": [
          "Fatkhullin",
          "He",
          "Lan"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2511_11131",
        "label": "Yaghmaie et al. 2025",
        "title": "Convergence of Flow-Policy Gradient Learning for Linear Quadratic Regulator Problems\n",
        "authors": [
          "Yaghmaie",
          "Naha"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2511_11308",
        "label": "Zuliani et al. 2025",
        "title": "Policy Optimization for Unknown Systems using Differentiable Model Predictive Control\n",
        "authors": [
          "Zuliani",
          "Balta",
          "Lygeros"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2511_14752",
        "label": "Ganiban et al. 2025",
        "title": "A Sequential Operator-Splitting Framework for Exploration of Nonconvex Trajectory Optimization Solution Spaces\n",
        "authors": [
          "Ganiban",
          "Pavlasek",
          "Acikmese"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2511_18170",
        "label": "Liang et al. 2025",
        "title": "Time-aware Motion Planning in Dynamic Environments with Conformal Prediction",
        "authors": [
          "Liang",
          "Luo",
          "Wang"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2512_00453",
        "label": "Firouzkouhi et al. 2025",
        "title": "Sample-Efficient Expert Query Control in Active Imitation Learning via Conformal Prediction\n",
        "authors": [
          "Firouzkouhi",
          "Mirzaeedodangeh",
          "Lindemann"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2512_01809",
        "label": "Pan et al. 2025",
        "title": "Much Ado About Noising: Dispelling the Myths of Generative Robotic Control",
        "authors": [
          "Pan",
          "Anantharaman",
          "Huang"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2512_18736",
        "label": "Pfrommer et al. 2025",
        "title": "Is Your Conditional Diffusion Model Actually Denoising?",
        "authors": [
          "Pfrommer",
          "Dou",
          "Scarvelis"
        ],
        "year": 2025,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2601_03220",
        "label": "Finzi et al. 2026",
        "title": "From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence\n",
        "authors": [
          "Finzi",
          "Qiu",
          "Jiang"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2601_05525",
        "label": "Vinuesa et al. 2026",
        "title": "Explainable AI: Learning from the Learners",
        "authors": [
          "Vinuesa",
          "Brunton",
          "Mengaldo"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2601_06096",
        "label": "Rahimi 2026",
        "title": "The Hessian of tall-skinny networks is easy to invert",
        "authors": [
          "Rahimi"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2601_14880",
        "label": "Zheng et al. 2026",
        "title": "Contingency Planning for Safety-Critical Autonomous Vehicles: A Review and Perspectives\n",
        "authors": [
          "Zheng",
          "Zhang",
          "Yu"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2601_15006",
        "label": "Ohnishi et al. 2026",
        "title": "DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints\n",
        "authors": [
          "Ohnishi",
          "Takahashi"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2602_00992",
        "label": "Kyaw et al. 2026",
        "title": "Geometry-Aware Sampling-Based Motion Planning on Riemannian Manifolds",
        "authors": [
          "Kyaw",
          "Kelly"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2602_02846",
        "label": "Kino-PAX+",
        "title": "Kino-PAX+: Near-Optimal Massively Parallel Kinodynamic Sampling-based Motion Planner",
        "authors": [
          "Perrault",
          "Ho",
          "Lahijanian"
        ],
        "year": 2026,
        "category": "Motion Planning",
        "sub_category": "Path Planning",
        "tags": [
          "Motion planning",
          "Sampling-based planning",
          "Kinodynamic planning",
          "GPU",
          "Parallelized",
          "Asymptotic optimality",
          "Real-time planning",
          "Kino-PAX+"
        ],
        "summary": "Extends Kino-PAX with asymptotic near-optimal guarantees by focusing each GPU thread block's computation on the most promising nodes within local neighborhoods for propagation and refinement."
      }
    },
    {
      "data": {
        "id": "2602_03639",
        "label": "Schramm et al. 2026",
        "title": "Variance-Reduced Model Predictive Path Integral via Quadratic Model Approximation\n",
        "authors": [
          "Schramm",
          "Tiofack",
          "Perrin-Gilbert"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2602_18933",
        "label": "Song et al. 2026",
        "title": "A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR",
        "authors": [
          "Song",
          "Weissmann",
          "Staudigl"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2602_19699",
        "label": "Alboni et al. 2026",
        "title": "CACTO-BIC: Scalable Actor-Critic Learning via Biased Sampling and GPU-Accelerated Trajectory Optimization\n",
        "authors": [
          "Alboni",
          "Crestaz",
          "Fontanari"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_00871",
        "label": "Zhao et al. 2026",
        "title": "Hippo: High-performance Interior-Point and Projection-based Solver for Generic Constrained Trajectory Optimization\n",
        "authors": [
          "Zhao",
          "Righetti",
          "Khadiv"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_01176",
        "label": "Shaji et al. 2026",
        "title": "Path Integral Particle Filtering for Hybrid Systems via Saltation Matrices",
        "authors": [
          "Shaji",
          "Jayadevan",
          "Yuan"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_04843",
        "label": "Pai et al. 2026",
        "title": "Policy Optimization of Mixed H2/H-infinity Control: Benign Nonconvexity and Global Optimality\n",
        "authors": [
          "Pai",
          "Watanabe",
          "Tang"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_05385",
        "label": "Hao et al. 2026",
        "title": "Accelerating Sampling-Based Control via Learned Linear Koopman Dynamics",
        "authors": [
          "Hao",
          "Fang",
          "Lu"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_06773",
        "label": "Cobo-Briesewitz et al. 2026",
        "title": "Stability-Guided Exploration for Diverse Motion Generation",
        "authors": [
          "Cobo-Briesewitz",
          "Burghoff",
          "Shcherba"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_08824",
        "label": "Paulus et al. 2026",
        "title": "SoftJAX & SoftTorch: Empowering Automatic Differentiation Libraries with Informative Gradients\n",
        "authors": [
          "Paulus",
          "Geist",
          "Musil"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_10711",
        "label": "Zou et al. 2026",
        "title": "Parallel-in-Time Nonlinear Optimal Control via GPU-native Sequential Convex Programming\n",
        "authors": [
          "Zou",
          "Zhang",
          "Robic"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_11335",
        "label": "Pries et al. 2026",
        "title": "ADMM-based Continuous Trajectory Optimization in Graphs of Convex Sets",
        "authors": [
          "Pries",
          "Arrizabalaga",
          "Manchester"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_12361",
        "label": "Xie et al. 2026",
        "title": "GNN-DIP: Neural Corridor Selection for Decomposition-Based Motion Planning",
        "authors": [
          "Xie",
          "Huang",
          "Wu"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_14197",
        "label": "Nguyen-Le et al. 2026",
        "title": "On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis\n",
        "authors": [
          "Nguyen-Le",
          "Matni"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_14392",
        "label": "Wang et al. 2026",
        "title": "WestWorld: A Knowledge-Encoded Scalable Trajectory World Model for Diverse Robotic Systems\n",
        "authors": [
          "Wang",
          "Kong",
          "Wei"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_16059",
        "label": "AkinoPDF",
        "title": "Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness",
        "authors": [
          "Duong",
          "Ramsey",
          "Kingston"
        ],
        "year": 2026,
        "category": "Motion Planning",
        "sub_category": "Trajectory Planning",
        "tags": [
          "Kinodynamic planning",
          "Differential flatness",
          "Steering function",
          "Parallelization",
          "Manipulators",
          "Quadrotors"
        ],
        "summary": "Exploits differential flatness to obtain closed-form analytical BVP solutions in a flat output space. Planning is done in the flat space (concatenation of flat outputs and several time derivatives thereof). Kinodynamic constraints and collision checking can be done very efficiently/quickly by using SIMD instructions on CPU. Closely related to the linear-systems approach of Webb & van den Berg (1205.5088) but extended to the broader class of differentially flat systems."
      }
    },
    {
      "data": {
        "id": "2603_16808",
        "label": "Bold et al. 2026",
        "title": "Exponential stability of data-driven nonlinear MPC based on input/output models",
        "authors": [
          "Bold",
          "Schimperna",
          "Worthmann"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_19968",
        "label": "Redman 2026",
        "title": "Interpreting Reinforcement Learning Model Behavior via Koopman with Control",
        "authors": [
          "Redman"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_23465",
        "label": "Somalwar et al. 2026",
        "title": "Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control\n",
        "authors": [
          "Somalwar",
          "Lee",
          "Pappas"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_24489",
        "label": "Fazlyab et al. 2026",
        "title": "Model Predictive Path Integral Control as Preconditioned Gradient Descent",
        "authors": [
          "Fazlyab",
          "Sharifi",
          "Wang"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2603_28052",
        "label": "Lee et al. 2026",
        "title": "Meta-Harness: End-to-End Optimization of Model Harnesses",
        "authors": [
          "Lee",
          "Nair",
          "Zhang"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_00900",
        "label": "Sasfi et al. 2026",
        "title": "Soft projections for robust data-driven control",
        "authors": [
          "Sasfi",
          "Eising",
          "Dörfler"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_01477",
        "label": "Banker et al. 2026",
        "title": "Soft MPCritic: Amortized Model Predictive Value Iteration",
        "authors": [
          "Banker",
          "Lawrence",
          "Mesbah"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_01614",
        "label": "Amiri et al. 2026",
        "title": "Smooth Feedback Motion Planning with Reduced Curvature",
        "authors": [
          "Amiri",
          "LaValle"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_02821",
        "label": "Liu et al. 2026",
        "title": "Goal-Conditioned Neural ODEs with Guaranteed Safety and Stability for Learning-Based All-Pairs Motion Planning\n",
        "authors": [
          "Liu",
          "Wang",
          "Manchester"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_04310",
        "label": "Morton et al. 2026",
        "title": "frax: Fast Robot Kinematics and Dynamics in JAX",
        "authors": [
          "Morton",
          "Pavone"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_04539",
        "label": "Kim et al. 2026",
        "title": "FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control\n",
        "authors": [
          "Kim",
          "Lee",
          "Park"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_05088",
        "label": "Rostami et al. 2026",
        "title": "Scalar Federated Learning for Linear Quadratic Regulator",
        "authors": [
          "Rostami",
          "Talebi",
          "Kia"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_05226",
        "label": "Wang et al. 2026",
        "title": "RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains\n",
        "authors": [
          "Wang",
          "Ung",
          "Gubarev"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_05885",
        "label": "JZ-Tree",
        "title": "JZ-Tree: GPU Friendly Neighbour Search and Friends-of-friends with Dual Tree Walks in JAX plus CUDA\n",
        "authors": [
          "Stücker",
          "Hahn",
          "Winkler"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_06406",
        "label": "Luna et al. 2026",
        "title": "Augmented Graphs of Convex Sets and the Traveling Salesman Problem",
        "authors": [
          "Luna",
          "Summers"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_07944",
        "label": "Afsharrad et al. 2026",
        "title": "On-Policy Distillation of Language Models for Autonomous Vehicle Motion Planning",
        "authors": [
          "Afsharrad",
          "Abedsoltan",
          "Moradipari"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_08266",
        "label": "Gu et al. 2026",
        "title": "Orion-Lite: Distilling LLM Reasoning into Efficient Vision-Only Driving Models",
        "authors": [
          "Gu",
          "Cavagnero",
          "Dubbelman"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_08508",
        "label": "Zhang et al. 2026",
        "title": "Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation",
        "authors": [
          "Zhang",
          "Sorokin",
          "Brüdigam"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_10635",
        "label": "Duan et al. 2026",
        "title": "On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control",
        "authors": [
          "Duan",
          "Li",
          "Ma"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_11183",
        "label": "Schießl et al. 2026",
        "title": "Closed-loop analysis of linear stochastic MPC with risk-averse constraints",
        "authors": [
          "Schießl",
          "Ou",
          "Baumann"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_12149",
        "label": "Poyrazoglu et al. 2026",
        "title": "Uncertainty Guided Exploratory Trajectory Optimization for Sampling-Based Model Predictive Control\n",
        "authors": [
          "Poyrazoglu",
          "Cao",
          "Moorthy"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_13192",
        "label": "Oh et al. 2026",
        "title": "Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning\n",
        "authors": [
          "Oh",
          "Nguyen",
          "Hu"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_13312",
        "label": "Das et al. 2026",
        "title": "Path Integral Control in Gaussian Belief Space for Partially Observed Systems",
        "authors": [
          "Das",
          "Tanaka"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_13323",
        "label": "Iyer et al. 2026",
        "title": "Vectorizing Projection in Manifold-Constrained Motion Planning for Real-Time Whole-Body Control\n",
        "authors": [
          "Iyer",
          "Chang",
          "Liu"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_14026",
        "label": "Bayraktar et al. 2026",
        "title": "Scale-Invariant Sampling in Multi-Arm Bandit Motion Planning for Object Extraction\n",
        "authors": [
          "Bayraktar",
          "Orthey",
          "Toussaint"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_14669",
        "label": "Song et al. 2026",
        "title": "Zeroth-Order Optimization at the Edge of Stability",
        "authors": [
          "Song",
          "Zhang",
          "Li"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_15918",
        "label": "Sundström et al. 2026",
        "title": "A Practical Guide to PID Controller Implementation",
        "authors": [
          "Sundström",
          "Bauer",
          "Guzmán"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_18578",
        "label": "Ao et al. 2026",
        "title": "Bounded Ratio Reinforcement Learning",
        "authors": [
          "Ao",
          "Chen",
          "Lee"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_19452",
        "label": "Bongard et al. 2026",
        "title": "Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks\n",
        "authors": [
          "Bongard",
          "Jank",
          "Sagmeister"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_21270",
        "label": "Zhou et al. 2026",
        "title": "CLT-Optimal Parameter Error Bounds for Linear System Identification",
        "authors": [
          "Zhou",
          "Tu"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_23951",
        "label": "Cederberg et al. 2026",
        "title": "Presolving for GPU-Accelerated First-Order LP Solvers",
        "authors": [
          "Cederberg",
          "Boyd"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    },
    {
      "data": {
        "id": "2604_24442",
        "label": "Lee et al. 2026",
        "title": "The Fragility of Learning LQG Controllers",
        "authors": [
          "Lee",
          "Tsiamis",
          "Matni"
        ],
        "year": 2026,
        "category": "Other",
        "sub_category": null,
        "tags": [],
        "summary": ""
      }
    }
  ],
  "edges": [
    {
      "data": {
        "id": "e0",
        "source": "1957_dubins_on_curves_of_minimal",
        "target": "1990_reeds_optimal_paths_for_a",
        "weight": 0.8668
      }
    },
    {
      "data": {
        "id": "e1",
        "source": "1957_dubins_on_curves_of_minimal",
        "target": "1997_scheuer_continuous_curvature_path_planning",
        "weight": 0.7906
      }
    },
    {
      "data": {
        "id": "e2",
        "source": "1957_dubins_on_curves_of_minimal",
        "target": "2001_nagy_trajectory_generation_for_car",
        "weight": 0.7634
      }
    },
    {
      "data": {
        "id": "e3",
        "source": "1957_dubins_on_curves_of_minimal",
        "target": "2101_11565",
        "weight": 0.7675
      }
    },
    {
      "data": {
        "id": "e4",
        "source": "1957_dubins_on_curves_of_minimal",
        "target": "1801_08995",
        "weight": 0.7638
      }
    },
    {
      "data": {
        "id": "e5",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2005_00985",
        "weight": 0.8954
      }
    },
    {
      "data": {
        "id": "e6",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2409_11649",
        "weight": 0.8906
      }
    },
    {
      "data": {
        "id": "e7",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2010_00411",
        "weight": 0.8407
      }
    },
    {
      "data": {
        "id": "e8",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2020_marti_saumell_squash_box_feasibility_driven",
        "weight": 0.8333
      }
    },
    {
      "data": {
        "id": "e9",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2020_pellegrini_a_multiple_shooting_differential",
        "weight": 0.875
      }
    },
    {
      "data": {
        "id": "e10",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2009_verscheure_time_optimal_path_tracking",
        "weight": 0.803
      }
    },
    {
      "data": {
        "id": "e11",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e12",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2103_03293",
        "weight": 0.8578
      }
    },
    {
      "data": {
        "id": "e13",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "1205_5088",
        "weight": 0.8043
      }
    },
    {
      "data": {
        "id": "e14",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8651
      }
    },
    {
      "data": {
        "id": "e15",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2104_03186",
        "weight": 0.827
      }
    },
    {
      "data": {
        "id": "e16",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2109_07081",
        "weight": 0.8541
      }
    },
    {
      "data": {
        "id": "e17",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2022_houghton_path_planning_differential_dynamic",
        "weight": 0.8414
      }
    },
    {
      "data": {
        "id": "e18",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2014_pan_probabilistic_differential_dynamic_programming",
        "weight": 0.8785
      }
    },
    {
      "data": {
        "id": "e19",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2204_02322",
        "weight": 0.8399
      }
    },
    {
      "data": {
        "id": "e20",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2207_06362",
        "weight": 0.8048
      }
    },
    {
      "data": {
        "id": "e21",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2208_02439",
        "weight": 0.8161
      }
    },
    {
      "data": {
        "id": "e22",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8544
      }
    },
    {
      "data": {
        "id": "e23",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2016_rajamaki_sampled_differential_dynamic_programming",
        "weight": 0.8687
      }
    },
    {
      "data": {
        "id": "e24",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2309_07872",
        "weight": 0.8738
      }
    },
    {
      "data": {
        "id": "e25",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2309_12566",
        "weight": 0.8158
      }
    },
    {
      "data": {
        "id": "e26",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2311_06404",
        "weight": 0.8181
      }
    },
    {
      "data": {
        "id": "e27",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8281
      }
    },
    {
      "data": {
        "id": "e28",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2024_wang_a_convergence_guaranteed_multiple",
        "weight": 0.8354
      }
    },
    {
      "data": {
        "id": "e29",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2603_11335",
        "weight": 0.8037
      }
    },
    {
      "data": {
        "id": "e30",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "weight": 0.8627
      }
    },
    {
      "data": {
        "id": "e31",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "1903_00155",
        "weight": 0.8307
      }
    },
    {
      "data": {
        "id": "e32",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2603_24489",
        "weight": 0.806
      }
    },
    {
      "data": {
        "id": "e33",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2019_lefebvre_path_integral_policy_improvement",
        "weight": 0.8015
      }
    },
    {
      "data": {
        "id": "e34",
        "source": "1970_jacobson_differential_dynamic_programming",
        "target": "2002_08809",
        "weight": 0.8312
      }
    },
    {
      "data": {
        "id": "e35",
        "source": "1978_doyle_guaranteed_margins_for_lqg",
        "target": "1806_09460",
        "weight": 0.7522
      }
    },
    {
      "data": {
        "id": "e36",
        "source": "1978_doyle_guaranteed_margins_for_lqg",
        "target": "2502_12310",
        "weight": 0.7543
      }
    },
    {
      "data": {
        "id": "e37",
        "source": "1978_doyle_guaranteed_margins_for_lqg",
        "target": "2604_10635",
        "weight": 0.7989
      }
    },
    {
      "data": {
        "id": "e38",
        "source": "1978_doyle_guaranteed_margins_for_lqg",
        "target": "1998_scokaert_constrained_linear_quadratic_regulation",
        "weight": 0.7782
      }
    },
    {
      "data": {
        "id": "e39",
        "source": "1978_doyle_guaranteed_margins_for_lqg",
        "target": "2604_24442",
        "weight": 0.8061
      }
    },
    {
      "data": {
        "id": "e40",
        "source": "1985_bobrow_time_optimal_control_of",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.7865
      }
    },
    {
      "data": {
        "id": "e41",
        "source": "1985_bobrow_time_optimal_control_of",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8172
      }
    },
    {
      "data": {
        "id": "e42",
        "source": "1985_bobrow_time_optimal_control_of",
        "target": "2303_16746",
        "weight": 0.7914
      }
    },
    {
      "data": {
        "id": "e43",
        "source": "1985_bobrow_time_optimal_control_of",
        "target": "1707_07239",
        "weight": 0.8641
      }
    },
    {
      "data": {
        "id": "e44",
        "source": "1985_bobrow_time_optimal_control_of",
        "target": "2009_verscheure_time_optimal_path_tracking",
        "weight": 0.8456
      }
    },
    {
      "data": {
        "id": "e45",
        "source": "1985_juang_an_eigensystem_realization_algorithm",
        "target": "1312_0041",
        "weight": 0.7837
      }
    },
    {
      "data": {
        "id": "e46",
        "source": "1985_juang_an_eigensystem_realization_algorithm",
        "target": "1994_overschee_n4sid_numerical_algorithms_for",
        "weight": 0.7675
      }
    },
    {
      "data": {
        "id": "e47",
        "source": "1985_juang_an_eigensystem_realization_algorithm",
        "target": "1996_overschee_subspace_identification_for_linear",
        "weight": 0.766
      }
    },
    {
      "data": {
        "id": "e48",
        "source": "1985_juang_an_eigensystem_realization_algorithm",
        "target": "1409_6358",
        "weight": 0.7496
      }
    },
    {
      "data": {
        "id": "e49",
        "source": "1985_juang_an_eigensystem_realization_algorithm",
        "target": "2008_schmid_dynamic_mode_decomposition_of",
        "weight": 0.7688
      }
    },
    {
      "data": {
        "id": "e50",
        "source": "1990_reeds_optimal_paths_for_a",
        "target": "1997_scheuer_continuous_curvature_path_planning",
        "weight": 0.8209
      }
    },
    {
      "data": {
        "id": "e51",
        "source": "1990_reeds_optimal_paths_for_a",
        "target": "2000_piazzi_quintic_g2_splines_for",
        "weight": 0.7741
      }
    },
    {
      "data": {
        "id": "e52",
        "source": "1990_reeds_optimal_paths_for_a",
        "target": "2004_fraichard_from_reeds_and_shepps",
        "weight": 0.8294
      }
    },
    {
      "data": {
        "id": "e53",
        "source": "1990_reeds_optimal_paths_for_a",
        "target": "2101_11565",
        "weight": 0.7828
      }
    },
    {
      "data": {
        "id": "e54",
        "source": "1994_overschee_n4sid_numerical_algorithms_for",
        "target": "1996_overschee_subspace_identification_for_linear",
        "weight": 0.8964
      }
    },
    {
      "data": {
        "id": "e55",
        "source": "1994_overschee_n4sid_numerical_algorithms_for",
        "target": "2412_12036",
        "weight": 0.7471
      }
    },
    {
      "data": {
        "id": "e56",
        "source": "1994_overschee_n4sid_numerical_algorithms_for",
        "target": "1711_05501",
        "weight": 0.7509
      }
    },
    {
      "data": {
        "id": "e57",
        "source": "1994_overschee_n4sid_numerical_algorithms_for",
        "target": "1509_03580",
        "weight": 0.751
      }
    },
    {
      "data": {
        "id": "e58",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "2009_10484",
        "weight": 0.817
      }
    },
    {
      "data": {
        "id": "e59",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "1998_lavalle_rapidly_exploring_random_trees",
        "weight": 0.8331
      }
    },
    {
      "data": {
        "id": "e60",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "1999_lavalle_randomized_kinodynamic_planning",
        "weight": 0.8128
      }
    },
    {
      "data": {
        "id": "e61",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "2000_kuffner_rrt_connect_an_efficient",
        "weight": 0.8373
      }
    },
    {
      "data": {
        "id": "e62",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "2410_19414",
        "weight": 0.8257
      }
    },
    {
      "data": {
        "id": "e63",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "2007_geraerts_creating_high_quality_paths",
        "weight": 0.8113
      }
    },
    {
      "data": {
        "id": "e64",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "1105_1186",
        "weight": 0.8512
      }
    },
    {
      "data": {
        "id": "e65",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "2011_karaman_anytime_motion_planning_using",
        "weight": 0.8258
      }
    },
    {
      "data": {
        "id": "e66",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "1306_3532",
        "weight": 0.8098
      }
    },
    {
      "data": {
        "id": "e67",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "2013_luna_anytime_solution_optimization_for",
        "weight": 0.8071
      }
    },
    {
      "data": {
        "id": "e68",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "1404_2334",
        "weight": 0.8129
      }
    },
    {
      "data": {
        "id": "e69",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "1405_5848",
        "weight": 0.821
      }
    },
    {
      "data": {
        "id": "e70",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "2503_16164",
        "weight": 0.8041
      }
    },
    {
      "data": {
        "id": "e71",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8078
      }
    },
    {
      "data": {
        "id": "e72",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.8
      }
    },
    {
      "data": {
        "id": "e73",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8136
      }
    },
    {
      "data": {
        "id": "e74",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "2508_21001",
        "weight": 0.808
      }
    },
    {
      "data": {
        "id": "e75",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "2301_13143",
        "weight": 0.8068
      }
    },
    {
      "data": {
        "id": "e76",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "2305_01072",
        "weight": 0.8055
      }
    },
    {
      "data": {
        "id": "e77",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "1809_02399",
        "weight": 0.8081
      }
    },
    {
      "data": {
        "id": "e78",
        "source": "1996_kavraki_probabilistic_roadmaps_for_path",
        "target": "1809_07051",
        "weight": 0.8143
      }
    },
    {
      "data": {
        "id": "e79",
        "source": "1996_overschee_subspace_identification_for_linear",
        "target": "1312_0041",
        "weight": 0.7601
      }
    },
    {
      "data": {
        "id": "e80",
        "source": "1996_overschee_subspace_identification_for_linear",
        "target": "2604_21270",
        "weight": 0.7688
      }
    },
    {
      "data": {
        "id": "e81",
        "source": "1996_overschee_subspace_identification_for_linear",
        "target": "2102_03664",
        "weight": 0.7546
      }
    },
    {
      "data": {
        "id": "e82",
        "source": "1997_scheuer_continuous_curvature_path_planning",
        "target": "2013_yang_spline_based_rrt_path",
        "weight": 0.8093
      }
    },
    {
      "data": {
        "id": "e83",
        "source": "1997_scheuer_continuous_curvature_path_planning",
        "target": "2205_04422",
        "weight": 0.8361
      }
    },
    {
      "data": {
        "id": "e84",
        "source": "1997_scheuer_continuous_curvature_path_planning",
        "target": "2201_03163",
        "weight": 0.8334
      }
    },
    {
      "data": {
        "id": "e85",
        "source": "1997_scheuer_continuous_curvature_path_planning",
        "target": "2000_piazzi_quintic_g2_splines_for",
        "weight": 0.8119
      }
    },
    {
      "data": {
        "id": "e86",
        "source": "1997_scheuer_continuous_curvature_path_planning",
        "target": "2001_nagy_trajectory_generation_for_car",
        "weight": 0.8542
      }
    },
    {
      "data": {
        "id": "e87",
        "source": "1997_scheuer_continuous_curvature_path_planning",
        "target": "2004_fraichard_from_reeds_and_shepps",
        "weight": 0.9124
      }
    },
    {
      "data": {
        "id": "e88",
        "source": "1997_scheuer_continuous_curvature_path_planning",
        "target": "2305_01072",
        "weight": 0.801
      }
    },
    {
      "data": {
        "id": "e89",
        "source": "1997_scheuer_continuous_curvature_path_planning",
        "target": "2504_18978",
        "weight": 0.8017
      }
    },
    {
      "data": {
        "id": "e90",
        "source": "1997_scheuer_continuous_curvature_path_planning",
        "target": "2604_01614",
        "weight": 0.8208
      }
    },
    {
      "data": {
        "id": "e91",
        "source": "1997_scheuer_continuous_curvature_path_planning",
        "target": "1506_01085",
        "weight": 0.8462
      }
    },
    {
      "data": {
        "id": "e92",
        "source": "1997_scheuer_continuous_curvature_path_planning",
        "target": "2405_03281",
        "weight": 0.8771
      }
    },
    {
      "data": {
        "id": "e93",
        "source": "1997_scheuer_continuous_curvature_path_planning",
        "target": "2017_roesmann_kinodynamic_trajectory_optimization_and",
        "weight": 0.8084
      }
    },
    {
      "data": {
        "id": "e94",
        "source": "1997_scheuer_continuous_curvature_path_planning",
        "target": "1801_08995",
        "weight": 0.8455
      }
    },
    {
      "data": {
        "id": "e95",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2409_12266",
        "weight": 0.8125
      }
    },
    {
      "data": {
        "id": "e96",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2009_10484",
        "weight": 0.8077
      }
    },
    {
      "data": {
        "id": "e97",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "1999_lavalle_randomized_kinodynamic_planning",
        "weight": 0.9111
      }
    },
    {
      "data": {
        "id": "e98",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2000_kuffner_rrt_connect_an_efficient",
        "weight": 0.9097
      }
    },
    {
      "data": {
        "id": "e99",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2410_19414",
        "weight": 0.8346
      }
    },
    {
      "data": {
        "id": "e100",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2007_geraerts_creating_high_quality_paths",
        "weight": 0.8
      }
    },
    {
      "data": {
        "id": "e101",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2008_rickert_balancing_exploration_and_exploitation",
        "weight": 0.8197
      }
    },
    {
      "data": {
        "id": "e102",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.881
      }
    },
    {
      "data": {
        "id": "e103",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8945
      }
    },
    {
      "data": {
        "id": "e104",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2411_15651",
        "weight": 0.856
      }
    },
    {
      "data": {
        "id": "e105",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2411_17293",
        "weight": 0.8088
      }
    },
    {
      "data": {
        "id": "e106",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2010_karaman_optimal_kinodynamic_motion_planning",
        "weight": 0.8999
      }
    },
    {
      "data": {
        "id": "e107",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "1105_1186",
        "weight": 0.89
      }
    },
    {
      "data": {
        "id": "e108",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2411_17902",
        "weight": 0.8208
      }
    },
    {
      "data": {
        "id": "e109",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2011_karaman_anytime_motion_planning_using",
        "weight": 0.9233
      }
    },
    {
      "data": {
        "id": "e110",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "1204_6453",
        "weight": 0.8738
      }
    },
    {
      "data": {
        "id": "e111",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "1205_5088",
        "weight": 0.8142
      }
    },
    {
      "data": {
        "id": "e112",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2412_11270",
        "weight": 0.83
      }
    },
    {
      "data": {
        "id": "e113",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2012_kobilarov_cross_entropy_motion_planning",
        "weight": 0.8037
      }
    },
    {
      "data": {
        "id": "e114",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2012_perez_lqr_rrt_star_optimal",
        "weight": 0.8404
      }
    },
    {
      "data": {
        "id": "e115",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "1306_3532",
        "weight": 0.8662
      }
    },
    {
      "data": {
        "id": "e116",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2502_09556",
        "weight": 0.8455
      }
    },
    {
      "data": {
        "id": "e117",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2013_luna_anytime_solution_optimization_for",
        "weight": 0.8285
      }
    },
    {
      "data": {
        "id": "e118",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2013_yang_spline_based_rrt_path",
        "weight": 0.8853
      }
    },
    {
      "data": {
        "id": "e119",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "1404_2334",
        "weight": 0.9064
      }
    },
    {
      "data": {
        "id": "e120",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "1405_5848",
        "weight": 0.862
      }
    },
    {
      "data": {
        "id": "e121",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2503_06757",
        "weight": 0.8498
      }
    },
    {
      "data": {
        "id": "e122",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2201_03163",
        "weight": 0.8417
      }
    },
    {
      "data": {
        "id": "e123",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "1407_2896",
        "weight": 0.8226
      }
    },
    {
      "data": {
        "id": "e124",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2503_16164",
        "weight": 0.8864
      }
    },
    {
      "data": {
        "id": "e125",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2203_01751",
        "weight": 0.8113
      }
    },
    {
      "data": {
        "id": "e126",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8101
      }
    },
    {
      "data": {
        "id": "e127",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2203_02176",
        "weight": 0.8401
      }
    },
    {
      "data": {
        "id": "e128",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2505_10542",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e129",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.866
      }
    },
    {
      "data": {
        "id": "e130",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.882
      }
    },
    {
      "data": {
        "id": "e131",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2015_palmieri_distance_metric_learning_for",
        "weight": 0.8139
      }
    },
    {
      "data": {
        "id": "e132",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2210_01744",
        "weight": 0.802
      }
    },
    {
      "data": {
        "id": "e133",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2508_21001",
        "weight": 0.8543
      }
    },
    {
      "data": {
        "id": "e134",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2016_choudhury_regionally_accelerated_batch_informed",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e135",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2301_13143",
        "weight": 0.9023
      }
    },
    {
      "data": {
        "id": "e136",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2302_11670",
        "weight": 0.8376
      }
    },
    {
      "data": {
        "id": "e137",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "1709_07610",
        "weight": 0.8065
      }
    },
    {
      "data": {
        "id": "e138",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "1710_10122",
        "weight": 0.899
      }
    },
    {
      "data": {
        "id": "e139",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2309_14595",
        "weight": 0.873
      }
    },
    {
      "data": {
        "id": "e140",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "1809_02399",
        "weight": 0.9
      }
    },
    {
      "data": {
        "id": "e141",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "1809_07051",
        "weight": 0.895
      }
    },
    {
      "data": {
        "id": "e142",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "1909_09688",
        "weight": 0.8456
      }
    },
    {
      "data": {
        "id": "e143",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2403_01194",
        "weight": 0.873
      }
    },
    {
      "data": {
        "id": "e144",
        "source": "1998_lavalle_rapidly_exploring_random_trees",
        "target": "2403_10745",
        "weight": 0.8944
      }
    },
    {
      "data": {
        "id": "e145",
        "source": "1998_scokaert_constrained_linear_quadratic_regulation",
        "target": "1802_09767",
        "weight": 0.8126
      }
    },
    {
      "data": {
        "id": "e146",
        "source": "1998_scokaert_constrained_linear_quadratic_regulation",
        "target": "1806_09460",
        "weight": 0.8094
      }
    },
    {
      "data": {
        "id": "e147",
        "source": "1998_scokaert_constrained_linear_quadratic_regulation",
        "target": "2604_10635",
        "weight": 0.8263
      }
    },
    {
      "data": {
        "id": "e148",
        "source": "1998_scokaert_constrained_linear_quadratic_regulation",
        "target": "2604_11183",
        "weight": 0.8123
      }
    },
    {
      "data": {
        "id": "e149",
        "source": "1998_scokaert_constrained_linear_quadratic_regulation",
        "target": "2511_02095",
        "weight": 0.8005
      }
    },
    {
      "data": {
        "id": "e150",
        "source": "1998_scokaert_constrained_linear_quadratic_regulation",
        "target": "2403_00748",
        "weight": 0.8121
      }
    },
    {
      "data": {
        "id": "e151",
        "source": "1998_scokaert_constrained_linear_quadratic_regulation",
        "target": "2204_02322",
        "weight": 0.8328
      }
    },
    {
      "data": {
        "id": "e152",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2409_12266",
        "weight": 0.8276
      }
    },
    {
      "data": {
        "id": "e153",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2009_10484",
        "weight": 0.8047
      }
    },
    {
      "data": {
        "id": "e154",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2000_kuffner_rrt_connect_an_efficient",
        "weight": 0.876
      }
    },
    {
      "data": {
        "id": "e155",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2410_19414",
        "weight": 0.8295
      }
    },
    {
      "data": {
        "id": "e156",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8118
      }
    },
    {
      "data": {
        "id": "e157",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2411_15651",
        "weight": 0.8228
      }
    },
    {
      "data": {
        "id": "e158",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.837
      }
    },
    {
      "data": {
        "id": "e159",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2412_11270",
        "weight": 0.822
      }
    },
    {
      "data": {
        "id": "e160",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2010_karaman_optimal_kinodynamic_motion_planning",
        "weight": 0.9143
      }
    },
    {
      "data": {
        "id": "e161",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1105_1186",
        "weight": 0.8331
      }
    },
    {
      "data": {
        "id": "e162",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2011_karaman_anytime_motion_planning_using",
        "weight": 0.8592
      }
    },
    {
      "data": {
        "id": "e163",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1204_6453",
        "weight": 0.8246
      }
    },
    {
      "data": {
        "id": "e164",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1205_5088",
        "weight": 0.8935
      }
    },
    {
      "data": {
        "id": "e165",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2012_perez_lqr_rrt_star_optimal",
        "weight": 0.8754
      }
    },
    {
      "data": {
        "id": "e166",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1306_3532",
        "weight": 0.8262
      }
    },
    {
      "data": {
        "id": "e167",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2013_luna_anytime_solution_optimization_for",
        "weight": 0.817
      }
    },
    {
      "data": {
        "id": "e168",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2013_yang_spline_based_rrt_path",
        "weight": 0.8287
      }
    },
    {
      "data": {
        "id": "e169",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8453
      }
    },
    {
      "data": {
        "id": "e170",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1404_2334",
        "weight": 0.8502
      }
    },
    {
      "data": {
        "id": "e171",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1405_5848",
        "weight": 0.8089
      }
    },
    {
      "data": {
        "id": "e172",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2503_06757",
        "weight": 0.8102
      }
    },
    {
      "data": {
        "id": "e173",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2503_16164",
        "weight": 0.8389
      }
    },
    {
      "data": {
        "id": "e174",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1407_2896",
        "weight": 0.8732
      }
    },
    {
      "data": {
        "id": "e175",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1411_4045",
        "weight": 0.829
      }
    },
    {
      "data": {
        "id": "e176",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2203_01751",
        "weight": 0.8142
      }
    },
    {
      "data": {
        "id": "e177",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8311
      }
    },
    {
      "data": {
        "id": "e178",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2203_02176",
        "weight": 0.8351
      }
    },
    {
      "data": {
        "id": "e179",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1505_04098",
        "weight": 0.8459
      }
    },
    {
      "data": {
        "id": "e180",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2205_04422",
        "weight": 0.8025
      }
    },
    {
      "data": {
        "id": "e181",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1511_05259",
        "weight": 0.861
      }
    },
    {
      "data": {
        "id": "e182",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.8131
      }
    },
    {
      "data": {
        "id": "e183",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8235
      }
    },
    {
      "data": {
        "id": "e184",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2015_palmieri_distance_metric_learning_for",
        "weight": 0.8093
      }
    },
    {
      "data": {
        "id": "e185",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2210_01744",
        "weight": 0.8662
      }
    },
    {
      "data": {
        "id": "e186",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2508_21001",
        "weight": 0.8557
      }
    },
    {
      "data": {
        "id": "e187",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2301_13143",
        "weight": 0.8699
      }
    },
    {
      "data": {
        "id": "e188",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1709_07610",
        "weight": 0.8033
      }
    },
    {
      "data": {
        "id": "e189",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1710_10122",
        "weight": 0.904
      }
    },
    {
      "data": {
        "id": "e190",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2309_14595",
        "weight": 0.8161
      }
    },
    {
      "data": {
        "id": "e191",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2602_00992",
        "weight": 0.8095
      }
    },
    {
      "data": {
        "id": "e192",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2602_02846",
        "weight": 0.8114
      }
    },
    {
      "data": {
        "id": "e193",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1809_02399",
        "weight": 0.9188
      }
    },
    {
      "data": {
        "id": "e194",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1809_07051",
        "weight": 0.8719
      }
    },
    {
      "data": {
        "id": "e195",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2018_kingston_sampling_based_methods_for",
        "weight": 0.8128
      }
    },
    {
      "data": {
        "id": "e196",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2603_16059",
        "weight": 0.8449
      }
    },
    {
      "data": {
        "id": "e197",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "1909_09688",
        "weight": 0.8156
      }
    },
    {
      "data": {
        "id": "e198",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2403_01194",
        "weight": 0.8261
      }
    },
    {
      "data": {
        "id": "e199",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2403_10745",
        "weight": 0.8902
      }
    },
    {
      "data": {
        "id": "e200",
        "source": "1999_lavalle_randomized_kinodynamic_planning",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8284
      }
    },
    {
      "data": {
        "id": "e201",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2410_19414",
        "weight": 0.8195
      }
    },
    {
      "data": {
        "id": "e202",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2007_geraerts_creating_high_quality_paths",
        "weight": 0.8132
      }
    },
    {
      "data": {
        "id": "e203",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.9035
      }
    },
    {
      "data": {
        "id": "e204",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8567
      }
    },
    {
      "data": {
        "id": "e205",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2411_15651",
        "weight": 0.8253
      }
    },
    {
      "data": {
        "id": "e206",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2411_17902",
        "weight": 0.8326
      }
    },
    {
      "data": {
        "id": "e207",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2412_11270",
        "weight": 0.8104
      }
    },
    {
      "data": {
        "id": "e208",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2010_karaman_optimal_kinodynamic_motion_planning",
        "weight": 0.8671
      }
    },
    {
      "data": {
        "id": "e209",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "1105_1186",
        "weight": 0.8485
      }
    },
    {
      "data": {
        "id": "e210",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2011_karaman_anytime_motion_planning_using",
        "weight": 0.886
      }
    },
    {
      "data": {
        "id": "e211",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "1204_6453",
        "weight": 0.8436
      }
    },
    {
      "data": {
        "id": "e212",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "1205_5088",
        "weight": 0.8214
      }
    },
    {
      "data": {
        "id": "e213",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2012_perez_lqr_rrt_star_optimal",
        "weight": 0.8335
      }
    },
    {
      "data": {
        "id": "e214",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "1306_3532",
        "weight": 0.8457
      }
    },
    {
      "data": {
        "id": "e215",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2502_09556",
        "weight": 0.827
      }
    },
    {
      "data": {
        "id": "e216",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2013_luna_anytime_solution_optimization_for",
        "weight": 0.8308
      }
    },
    {
      "data": {
        "id": "e217",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2013_yang_spline_based_rrt_path",
        "weight": 0.8421
      }
    },
    {
      "data": {
        "id": "e218",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "1404_2334",
        "weight": 0.8622
      }
    },
    {
      "data": {
        "id": "e219",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "1405_5848",
        "weight": 0.8317
      }
    },
    {
      "data": {
        "id": "e220",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2503_06757",
        "weight": 0.866
      }
    },
    {
      "data": {
        "id": "e221",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2201_03163",
        "weight": 0.8098
      }
    },
    {
      "data": {
        "id": "e222",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "1407_2896",
        "weight": 0.8161
      }
    },
    {
      "data": {
        "id": "e223",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2503_16164",
        "weight": 0.8478
      }
    },
    {
      "data": {
        "id": "e224",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "1411_4045",
        "weight": 0.8009
      }
    },
    {
      "data": {
        "id": "e225",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2203_01751",
        "weight": 0.8093
      }
    },
    {
      "data": {
        "id": "e226",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8019
      }
    },
    {
      "data": {
        "id": "e227",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2203_02176",
        "weight": 0.8587
      }
    },
    {
      "data": {
        "id": "e228",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2505_06791",
        "weight": 0.8015
      }
    },
    {
      "data": {
        "id": "e229",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2505_10542",
        "weight": 0.839
      }
    },
    {
      "data": {
        "id": "e230",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.9073
      }
    },
    {
      "data": {
        "id": "e231",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8842
      }
    },
    {
      "data": {
        "id": "e232",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2015_palmieri_distance_metric_learning_for",
        "weight": 0.8034
      }
    },
    {
      "data": {
        "id": "e233",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2210_01744",
        "weight": 0.8114
      }
    },
    {
      "data": {
        "id": "e234",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2508_21001",
        "weight": 0.8435
      }
    },
    {
      "data": {
        "id": "e235",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2301_13143",
        "weight": 0.8471
      }
    },
    {
      "data": {
        "id": "e236",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2302_11670",
        "weight": 0.8076
      }
    },
    {
      "data": {
        "id": "e237",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2305_01072",
        "weight": 0.8213
      }
    },
    {
      "data": {
        "id": "e238",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "1708_06056",
        "weight": 0.8131
      }
    },
    {
      "data": {
        "id": "e239",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "1709_07610",
        "weight": 0.8022
      }
    },
    {
      "data": {
        "id": "e240",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "1710_10122",
        "weight": 0.8751
      }
    },
    {
      "data": {
        "id": "e241",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2309_14595",
        "weight": 0.8311
      }
    },
    {
      "data": {
        "id": "e242",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2602_02846",
        "weight": 0.8012
      }
    },
    {
      "data": {
        "id": "e243",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "1809_02399",
        "weight": 0.8868
      }
    },
    {
      "data": {
        "id": "e244",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "1809_07051",
        "weight": 0.8576
      }
    },
    {
      "data": {
        "id": "e245",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "1909_09688",
        "weight": 0.8396
      }
    },
    {
      "data": {
        "id": "e246",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2403_01194",
        "weight": 0.8256
      }
    },
    {
      "data": {
        "id": "e247",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2403_10745",
        "weight": 0.8916
      }
    },
    {
      "data": {
        "id": "e248",
        "source": "2000_kuffner_rrt_connect_an_efficient",
        "target": "2406_02807",
        "weight": 0.8174
      }
    },
    {
      "data": {
        "id": "e249",
        "source": "2000_piazzi_quintic_g2_splines_for",
        "target": "2205_04422",
        "weight": 0.8115
      }
    },
    {
      "data": {
        "id": "e250",
        "source": "2000_piazzi_quintic_g2_splines_for",
        "target": "2001_nagy_trajectory_generation_for_car",
        "weight": 0.8711
      }
    },
    {
      "data": {
        "id": "e251",
        "source": "2000_piazzi_quintic_g2_splines_for",
        "target": "2004_fraichard_from_reeds_and_shepps",
        "weight": 0.815
      }
    },
    {
      "data": {
        "id": "e252",
        "source": "2000_piazzi_quintic_g2_splines_for",
        "target": "2504_18978",
        "weight": 0.8059
      }
    },
    {
      "data": {
        "id": "e253",
        "source": "2000_piazzi_quintic_g2_splines_for",
        "target": "1711_03449",
        "weight": 0.8089
      }
    },
    {
      "data": {
        "id": "e254",
        "source": "2000_piazzi_quintic_g2_splines_for",
        "target": "1506_01085",
        "weight": 0.8022
      }
    },
    {
      "data": {
        "id": "e255",
        "source": "2000_piazzi_quintic_g2_splines_for",
        "target": "2017_roesmann_kinodynamic_trajectory_optimization_and",
        "weight": 0.8017
      }
    },
    {
      "data": {
        "id": "e256",
        "source": "2000_piazzi_quintic_g2_splines_for",
        "target": "1801_08995",
        "weight": 0.8535
      }
    },
    {
      "data": {
        "id": "e257",
        "source": "2001_nagy_trajectory_generation_for_car",
        "target": "2205_04422",
        "weight": 0.8034
      }
    },
    {
      "data": {
        "id": "e258",
        "source": "2001_nagy_trajectory_generation_for_car",
        "target": "2004_fraichard_from_reeds_and_shepps",
        "weight": 0.8636
      }
    },
    {
      "data": {
        "id": "e259",
        "source": "2001_nagy_trajectory_generation_for_car",
        "target": "1506_01085",
        "weight": 0.8245
      }
    },
    {
      "data": {
        "id": "e260",
        "source": "2001_nagy_trajectory_generation_for_car",
        "target": "1801_08995",
        "weight": 0.8792
      }
    },
    {
      "data": {
        "id": "e261",
        "source": "2004_fraichard_from_reeds_and_shepps",
        "target": "2023_steinecker_a_simple_and_model",
        "weight": 0.8021
      }
    },
    {
      "data": {
        "id": "e262",
        "source": "2004_fraichard_from_reeds_and_shepps",
        "target": "2201_03163",
        "weight": 0.8111
      }
    },
    {
      "data": {
        "id": "e263",
        "source": "2004_fraichard_from_reeds_and_shepps",
        "target": "1506_01085",
        "weight": 0.833
      }
    },
    {
      "data": {
        "id": "e264",
        "source": "2004_fraichard_from_reeds_and_shepps",
        "target": "2405_03281",
        "weight": 0.8546
      }
    },
    {
      "data": {
        "id": "e265",
        "source": "2004_fraichard_from_reeds_and_shepps",
        "target": "1801_08995",
        "weight": 0.8575
      }
    },
    {
      "data": {
        "id": "e266",
        "source": "2004_li_iterative_linear_quadratic_regulator",
        "target": "2012_tassa_synthesis_and_stabilization_of",
        "weight": 0.8746
      }
    },
    {
      "data": {
        "id": "e267",
        "source": "2004_li_iterative_linear_quadratic_regulator",
        "target": "2109_07081",
        "weight": 0.8086
      }
    },
    {
      "data": {
        "id": "e268",
        "source": "2004_li_iterative_linear_quadratic_regulator",
        "target": "2304_00346",
        "weight": 0.8353
      }
    },
    {
      "data": {
        "id": "e269",
        "source": "2004_li_iterative_linear_quadratic_regulator",
        "target": "2511_02095",
        "weight": 0.8138
      }
    },
    {
      "data": {
        "id": "e270",
        "source": "2004_li_iterative_linear_quadratic_regulator",
        "target": "2305_09619",
        "weight": 0.8299
      }
    },
    {
      "data": {
        "id": "e271",
        "source": "2004_li_iterative_linear_quadratic_regulator",
        "target": "2403_00748",
        "weight": 0.8334
      }
    },
    {
      "data": {
        "id": "e272",
        "source": "2004_li_iterative_linear_quadratic_regulator",
        "target": "2204_02322",
        "weight": 0.8709
      }
    },
    {
      "data": {
        "id": "e273",
        "source": "2004_li_iterative_linear_quadratic_regulator",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8063
      }
    },
    {
      "data": {
        "id": "e274",
        "source": "2004_li_iterative_linear_quadratic_regulator",
        "target": "2103_03293",
        "weight": 0.8258
      }
    },
    {
      "data": {
        "id": "e275",
        "source": "2004_li_iterative_linear_quadratic_regulator",
        "target": "1711_11006",
        "weight": 0.8483
      }
    },
    {
      "data": {
        "id": "e276",
        "source": "2004_li_iterative_linear_quadratic_regulator",
        "target": "2207_06362",
        "weight": 0.868
      }
    },
    {
      "data": {
        "id": "e277",
        "source": "2007_geraerts_creating_high_quality_paths",
        "target": "2508_05027",
        "weight": 0.8637
      }
    },
    {
      "data": {
        "id": "e278",
        "source": "2007_geraerts_creating_high_quality_paths",
        "target": "2013_luna_anytime_solution_optimization_for",
        "weight": 0.8902
      }
    },
    {
      "data": {
        "id": "e279",
        "source": "2007_geraerts_creating_high_quality_paths",
        "target": "2009_10484",
        "weight": 0.8315
      }
    },
    {
      "data": {
        "id": "e280",
        "source": "2007_geraerts_creating_high_quality_paths",
        "target": "2410_19414",
        "weight": 0.825
      }
    },
    {
      "data": {
        "id": "e281",
        "source": "2007_geraerts_creating_high_quality_paths",
        "target": "1411_4045",
        "weight": 0.8052
      }
    },
    {
      "data": {
        "id": "e282",
        "source": "2007_geraerts_creating_high_quality_paths",
        "target": "1708_06056",
        "weight": 0.8034
      }
    },
    {
      "data": {
        "id": "e283",
        "source": "2007_geraerts_creating_high_quality_paths",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8006
      }
    },
    {
      "data": {
        "id": "e284",
        "source": "2007_geraerts_creating_high_quality_paths",
        "target": "2305_01072",
        "weight": 0.832
      }
    },
    {
      "data": {
        "id": "e285",
        "source": "2007_geraerts_creating_high_quality_paths",
        "target": "2205_04422",
        "weight": 0.8079
      }
    },
    {
      "data": {
        "id": "e286",
        "source": "2007_geraerts_creating_high_quality_paths",
        "target": "2405_03281",
        "weight": 0.8119
      }
    },
    {
      "data": {
        "id": "e287",
        "source": "2008_rickert_balancing_exploration_and_exploitation",
        "target": "2508_21001",
        "weight": 0.8014
      }
    },
    {
      "data": {
        "id": "e288",
        "source": "2008_rickert_balancing_exploration_and_exploitation",
        "target": "1809_02399",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e289",
        "source": "2008_rickert_balancing_exploration_and_exploitation",
        "target": "1405_5848",
        "weight": 0.813
      }
    },
    {
      "data": {
        "id": "e290",
        "source": "2008_rickert_balancing_exploration_and_exploitation",
        "target": "1404_2334",
        "weight": 0.8131
      }
    },
    {
      "data": {
        "id": "e291",
        "source": "2008_rickert_balancing_exploration_and_exploitation",
        "target": "2410_19414",
        "weight": 0.8209
      }
    },
    {
      "data": {
        "id": "e292",
        "source": "2008_rickert_balancing_exploration_and_exploitation",
        "target": "2603_06773",
        "weight": 0.8282
      }
    },
    {
      "data": {
        "id": "e293",
        "source": "2008_rickert_balancing_exploration_and_exploitation",
        "target": "2203_01751",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e294",
        "source": "2008_rickert_balancing_exploration_and_exploitation",
        "target": "2411_15651",
        "weight": 0.8068
      }
    },
    {
      "data": {
        "id": "e295",
        "source": "2008_schmid_dynamic_mode_decomposition_of",
        "target": "1312_0041",
        "weight": 0.9046
      }
    },
    {
      "data": {
        "id": "e296",
        "source": "2008_schmid_dynamic_mode_decomposition_of",
        "target": "2022_schmid_dynamic_mode_decomposition_and",
        "weight": 0.909
      }
    },
    {
      "data": {
        "id": "e297",
        "source": "2008_schmid_dynamic_mode_decomposition_of",
        "target": "1408_4408",
        "weight": 0.8238
      }
    },
    {
      "data": {
        "id": "e298",
        "source": "2008_schmid_dynamic_mode_decomposition_of",
        "target": "1409_6358",
        "weight": 0.8689
      }
    },
    {
      "data": {
        "id": "e299",
        "source": "2008_schmid_dynamic_mode_decomposition_of",
        "target": "1909_10466",
        "weight": 0.8878
      }
    },
    {
      "data": {
        "id": "e300",
        "source": "2008_schmid_dynamic_mode_decomposition_of",
        "target": "1509_03580",
        "weight": 0.8088
      }
    },
    {
      "data": {
        "id": "e301",
        "source": "2008_urmson_autonomous_driving_in_urban",
        "target": "2409_09523",
        "weight": 0.8288
      }
    },
    {
      "data": {
        "id": "e302",
        "source": "2008_urmson_autonomous_driving_in_urban",
        "target": "1604_07446",
        "weight": 0.8279
      }
    },
    {
      "data": {
        "id": "e303",
        "source": "2008_urmson_autonomous_driving_in_urban",
        "target": "2503_03262",
        "weight": 0.8063
      }
    },
    {
      "data": {
        "id": "e304",
        "source": "2008_urmson_autonomous_driving_in_urban",
        "target": "2303_09824",
        "weight": 0.7979
      }
    },
    {
      "data": {
        "id": "e305",
        "source": "2008_urmson_autonomous_driving_in_urban",
        "target": "2018_schwarting_planning_and_decision_making",
        "weight": 0.8126
      }
    },
    {
      "data": {
        "id": "e306",
        "source": "2009_ratliff_chomp_gradient_optimization_techniques",
        "target": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "weight": 0.8503
      }
    },
    {
      "data": {
        "id": "e307",
        "source": "2009_ratliff_chomp_gradient_optimization_techniques",
        "target": "1306_3532",
        "weight": 0.8026
      }
    },
    {
      "data": {
        "id": "e308",
        "source": "2009_ratliff_chomp_gradient_optimization_techniques",
        "target": "2411_11833",
        "weight": 0.8021
      }
    },
    {
      "data": {
        "id": "e309",
        "source": "2009_ratliff_chomp_gradient_optimization_techniques",
        "target": "2203_01751",
        "weight": 0.8094
      }
    },
    {
      "data": {
        "id": "e310",
        "source": "2009_ratliff_chomp_gradient_optimization_techniques",
        "target": "2504_18978",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e311",
        "source": "2009_ratliff_chomp_gradient_optimization_techniques",
        "target": "2205_04422",
        "weight": 0.8009
      }
    },
    {
      "data": {
        "id": "e312",
        "source": "2009_ratliff_chomp_gradient_optimization_techniques",
        "target": "2506_14865",
        "weight": 0.8101
      }
    },
    {
      "data": {
        "id": "e313",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "2109_07081",
        "weight": 0.8163
      }
    },
    {
      "data": {
        "id": "e314",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "2013_lipp_minimum_time_speed_optimisation_over",
        "weight": 0.8256
      }
    },
    {
      "data": {
        "id": "e315",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e316",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "2205_04422",
        "weight": 0.8322
      }
    },
    {
      "data": {
        "id": "e317",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8112
      }
    },
    {
      "data": {
        "id": "e318",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8322
      }
    },
    {
      "data": {
        "id": "e319",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "2303_16746",
        "weight": 0.8092
      }
    },
    {
      "data": {
        "id": "e320",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "2309_12566",
        "weight": 0.8
      }
    },
    {
      "data": {
        "id": "e321",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "1707_07239",
        "weight": 0.8301
      }
    },
    {
      "data": {
        "id": "e322",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "1903_00155",
        "weight": 0.8339
      }
    },
    {
      "data": {
        "id": "e323",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "2504_18978",
        "weight": 0.8417
      }
    },
    {
      "data": {
        "id": "e324",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "2603_24489",
        "weight": 0.8005
      }
    },
    {
      "data": {
        "id": "e325",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "1506_01085",
        "weight": 0.8164
      }
    },
    {
      "data": {
        "id": "e326",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "2019_jackson_altro_a_fast_solver",
        "weight": 0.8077
      }
    },
    {
      "data": {
        "id": "e327",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "2506_14865",
        "weight": 0.8069
      }
    },
    {
      "data": {
        "id": "e328",
        "source": "2009_verscheure_time_optimal_path_tracking",
        "target": "1205_5088",
        "weight": 0.8081
      }
    },
    {
      "data": {
        "id": "e329",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2409_12266",
        "weight": 0.8166
      }
    },
    {
      "data": {
        "id": "e330",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2009_10484",
        "weight": 0.847
      }
    },
    {
      "data": {
        "id": "e331",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2410_19414",
        "weight": 0.8366
      }
    },
    {
      "data": {
        "id": "e332",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8588
      }
    },
    {
      "data": {
        "id": "e333",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2411_15651",
        "weight": 0.8518
      }
    },
    {
      "data": {
        "id": "e334",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8678
      }
    },
    {
      "data": {
        "id": "e335",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2411_17902",
        "weight": 0.8277
      }
    },
    {
      "data": {
        "id": "e336",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2412_11270",
        "weight": 0.8235
      }
    },
    {
      "data": {
        "id": "e337",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1105_1186",
        "weight": 0.8923
      }
    },
    {
      "data": {
        "id": "e338",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "weight": 0.8003
      }
    },
    {
      "data": {
        "id": "e339",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2011_karaman_anytime_motion_planning_using",
        "weight": 0.8977
      }
    },
    {
      "data": {
        "id": "e340",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1204_6453",
        "weight": 0.8911
      }
    },
    {
      "data": {
        "id": "e341",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1205_5088",
        "weight": 0.9286
      }
    },
    {
      "data": {
        "id": "e342",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2012_kobilarov_cross_entropy_motion_planning",
        "weight": 0.8093
      }
    },
    {
      "data": {
        "id": "e343",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2012_perez_lqr_rrt_star_optimal",
        "weight": 0.9048
      }
    },
    {
      "data": {
        "id": "e344",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1306_3532",
        "weight": 0.8715
      }
    },
    {
      "data": {
        "id": "e345",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2502_09556",
        "weight": 0.8078
      }
    },
    {
      "data": {
        "id": "e346",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2013_luna_anytime_solution_optimization_for",
        "weight": 0.834
      }
    },
    {
      "data": {
        "id": "e347",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2013_yang_spline_based_rrt_path",
        "weight": 0.8448
      }
    },
    {
      "data": {
        "id": "e348",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8621
      }
    },
    {
      "data": {
        "id": "e349",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1404_2334",
        "weight": 0.8829
      }
    },
    {
      "data": {
        "id": "e350",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1405_5848",
        "weight": 0.826
      }
    },
    {
      "data": {
        "id": "e351",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2503_06757",
        "weight": 0.8191
      }
    },
    {
      "data": {
        "id": "e352",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2201_03163",
        "weight": 0.8218
      }
    },
    {
      "data": {
        "id": "e353",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1407_2896",
        "weight": 0.9036
      }
    },
    {
      "data": {
        "id": "e354",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2503_16164",
        "weight": 0.8627
      }
    },
    {
      "data": {
        "id": "e355",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1411_4045",
        "weight": 0.822
      }
    },
    {
      "data": {
        "id": "e356",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2203_01751",
        "weight": 0.8469
      }
    },
    {
      "data": {
        "id": "e357",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8315
      }
    },
    {
      "data": {
        "id": "e358",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2203_02176",
        "weight": 0.8401
      }
    },
    {
      "data": {
        "id": "e359",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2504_18978",
        "weight": 0.8027
      }
    },
    {
      "data": {
        "id": "e360",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1505_04098",
        "weight": 0.872
      }
    },
    {
      "data": {
        "id": "e361",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2505_10542",
        "weight": 0.8388
      }
    },
    {
      "data": {
        "id": "e362",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1511_05259",
        "weight": 0.846
      }
    },
    {
      "data": {
        "id": "e363",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.8598
      }
    },
    {
      "data": {
        "id": "e364",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8672
      }
    },
    {
      "data": {
        "id": "e365",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2015_palmieri_distance_metric_learning_for",
        "weight": 0.828
      }
    },
    {
      "data": {
        "id": "e366",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2210_01744",
        "weight": 0.8704
      }
    },
    {
      "data": {
        "id": "e367",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2508_21001",
        "weight": 0.8601
      }
    },
    {
      "data": {
        "id": "e368",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2016_choudhury_regionally_accelerated_batch_informed",
        "weight": 0.8019
      }
    },
    {
      "data": {
        "id": "e369",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2301_13143",
        "weight": 0.8917
      }
    },
    {
      "data": {
        "id": "e370",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1708_06056",
        "weight": 0.8175
      }
    },
    {
      "data": {
        "id": "e371",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1709_07610",
        "weight": 0.8229
      }
    },
    {
      "data": {
        "id": "e372",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2307_03167",
        "weight": 0.8037
      }
    },
    {
      "data": {
        "id": "e373",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1710_10122",
        "weight": 0.9159
      }
    },
    {
      "data": {
        "id": "e374",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2309_14545",
        "weight": 0.8106
      }
    },
    {
      "data": {
        "id": "e375",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2309_14595",
        "weight": 0.8279
      }
    },
    {
      "data": {
        "id": "e376",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2602_02846",
        "weight": 0.8336
      }
    },
    {
      "data": {
        "id": "e377",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1809_02399",
        "weight": 0.9289
      }
    },
    {
      "data": {
        "id": "e378",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1809_07051",
        "weight": 0.899
      }
    },
    {
      "data": {
        "id": "e379",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2018_kingston_sampling_based_methods_for",
        "weight": 0.8242
      }
    },
    {
      "data": {
        "id": "e380",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2603_16059",
        "weight": 0.8458
      }
    },
    {
      "data": {
        "id": "e381",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "1909_09688",
        "weight": 0.8844
      }
    },
    {
      "data": {
        "id": "e382",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2403_01194",
        "weight": 0.8279
      }
    },
    {
      "data": {
        "id": "e383",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2403_10745",
        "weight": 0.911
      }
    },
    {
      "data": {
        "id": "e384",
        "source": "2010_karaman_optimal_kinodynamic_motion_planning",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8405
      }
    },
    {
      "data": {
        "id": "e385",
        "source": "1105_1186",
        "target": "2409_12266",
        "weight": 0.8141
      }
    },
    {
      "data": {
        "id": "e386",
        "source": "1105_1186",
        "target": "2009_10484",
        "weight": 0.9019
      }
    },
    {
      "data": {
        "id": "e387",
        "source": "1105_1186",
        "target": "2410_19414",
        "weight": 0.8722
      }
    },
    {
      "data": {
        "id": "e388",
        "source": "1105_1186",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8793
      }
    },
    {
      "data": {
        "id": "e389",
        "source": "1105_1186",
        "target": "2411_15651",
        "weight": 0.837
      }
    },
    {
      "data": {
        "id": "e390",
        "source": "1105_1186",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8535
      }
    },
    {
      "data": {
        "id": "e391",
        "source": "1105_1186",
        "target": "2411_17293",
        "weight": 0.8076
      }
    },
    {
      "data": {
        "id": "e392",
        "source": "1105_1186",
        "target": "2411_17902",
        "weight": 0.8305
      }
    },
    {
      "data": {
        "id": "e393",
        "source": "1105_1186",
        "target": "2412_11270",
        "weight": 0.8149
      }
    },
    {
      "data": {
        "id": "e394",
        "source": "1105_1186",
        "target": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "weight": 0.8146
      }
    },
    {
      "data": {
        "id": "e395",
        "source": "1105_1186",
        "target": "2011_karaman_anytime_motion_planning_using",
        "weight": 0.8994
      }
    },
    {
      "data": {
        "id": "e396",
        "source": "1105_1186",
        "target": "1204_6453",
        "weight": 0.9257
      }
    },
    {
      "data": {
        "id": "e397",
        "source": "1105_1186",
        "target": "1205_5088",
        "weight": 0.8021
      }
    },
    {
      "data": {
        "id": "e398",
        "source": "1105_1186",
        "target": "2012_kobilarov_cross_entropy_motion_planning",
        "weight": 0.8253
      }
    },
    {
      "data": {
        "id": "e399",
        "source": "1105_1186",
        "target": "2012_perez_lqr_rrt_star_optimal",
        "weight": 0.8195
      }
    },
    {
      "data": {
        "id": "e400",
        "source": "1105_1186",
        "target": "1306_3532",
        "weight": 0.8962
      }
    },
    {
      "data": {
        "id": "e401",
        "source": "1105_1186",
        "target": "2502_09556",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e402",
        "source": "1105_1186",
        "target": "2013_luna_anytime_solution_optimization_for",
        "weight": 0.8591
      }
    },
    {
      "data": {
        "id": "e403",
        "source": "1105_1186",
        "target": "2013_yang_spline_based_rrt_path",
        "weight": 0.8231
      }
    },
    {
      "data": {
        "id": "e404",
        "source": "1105_1186",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8177
      }
    },
    {
      "data": {
        "id": "e405",
        "source": "1105_1186",
        "target": "1404_2334",
        "weight": 0.9131
      }
    },
    {
      "data": {
        "id": "e406",
        "source": "1105_1186",
        "target": "1405_5848",
        "weight": 0.8772
      }
    },
    {
      "data": {
        "id": "e407",
        "source": "1105_1186",
        "target": "2503_06757",
        "weight": 0.8161
      }
    },
    {
      "data": {
        "id": "e408",
        "source": "1105_1186",
        "target": "2503_16164",
        "weight": 0.8858
      }
    },
    {
      "data": {
        "id": "e409",
        "source": "1105_1186",
        "target": "1407_2896",
        "weight": 0.8516
      }
    },
    {
      "data": {
        "id": "e410",
        "source": "1105_1186",
        "target": "2203_01751",
        "weight": 0.855
      }
    },
    {
      "data": {
        "id": "e411",
        "source": "1105_1186",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8441
      }
    },
    {
      "data": {
        "id": "e412",
        "source": "1105_1186",
        "target": "2203_02176",
        "weight": 0.8398
      }
    },
    {
      "data": {
        "id": "e413",
        "source": "1105_1186",
        "target": "1505_04098",
        "weight": 0.8154
      }
    },
    {
      "data": {
        "id": "e414",
        "source": "1105_1186",
        "target": "2505_10542",
        "weight": 0.8378
      }
    },
    {
      "data": {
        "id": "e415",
        "source": "1105_1186",
        "target": "1511_05259",
        "weight": 0.8179
      }
    },
    {
      "data": {
        "id": "e416",
        "source": "1105_1186",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.88
      }
    },
    {
      "data": {
        "id": "e417",
        "source": "1105_1186",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8996
      }
    },
    {
      "data": {
        "id": "e418",
        "source": "1105_1186",
        "target": "2508_21001",
        "weight": 0.8097
      }
    },
    {
      "data": {
        "id": "e419",
        "source": "1105_1186",
        "target": "2016_choudhury_regionally_accelerated_batch_informed",
        "weight": 0.8386
      }
    },
    {
      "data": {
        "id": "e420",
        "source": "1105_1186",
        "target": "2301_13143",
        "weight": 0.8766
      }
    },
    {
      "data": {
        "id": "e421",
        "source": "1105_1186",
        "target": "2302_11670",
        "weight": 0.81
      }
    },
    {
      "data": {
        "id": "e422",
        "source": "1105_1186",
        "target": "2510_21074",
        "weight": 0.8162
      }
    },
    {
      "data": {
        "id": "e423",
        "source": "1105_1186",
        "target": "1708_06056",
        "weight": 0.8378
      }
    },
    {
      "data": {
        "id": "e424",
        "source": "1105_1186",
        "target": "1709_05448",
        "weight": 0.8155
      }
    },
    {
      "data": {
        "id": "e425",
        "source": "1105_1186",
        "target": "2307_03167",
        "weight": 0.8113
      }
    },
    {
      "data": {
        "id": "e426",
        "source": "1105_1186",
        "target": "1710_10122",
        "weight": 0.8345
      }
    },
    {
      "data": {
        "id": "e427",
        "source": "1105_1186",
        "target": "2309_14545",
        "weight": 0.8062
      }
    },
    {
      "data": {
        "id": "e428",
        "source": "1105_1186",
        "target": "2309_14595",
        "weight": 0.8388
      }
    },
    {
      "data": {
        "id": "e429",
        "source": "1105_1186",
        "target": "2602_02846",
        "weight": 0.8092
      }
    },
    {
      "data": {
        "id": "e430",
        "source": "1105_1186",
        "target": "1809_02399",
        "weight": 0.8708
      }
    },
    {
      "data": {
        "id": "e431",
        "source": "1105_1186",
        "target": "1809_07051",
        "weight": 0.9052
      }
    },
    {
      "data": {
        "id": "e432",
        "source": "1105_1186",
        "target": "1809_10252",
        "weight": 0.8048
      }
    },
    {
      "data": {
        "id": "e433",
        "source": "1105_1186",
        "target": "2018_kingston_sampling_based_methods_for",
        "weight": 0.8086
      }
    },
    {
      "data": {
        "id": "e434",
        "source": "1105_1186",
        "target": "1909_09688",
        "weight": 0.9277
      }
    },
    {
      "data": {
        "id": "e435",
        "source": "1105_1186",
        "target": "2403_01194",
        "weight": 0.8131
      }
    },
    {
      "data": {
        "id": "e436",
        "source": "1105_1186",
        "target": "2403_10745",
        "weight": 0.8417
      }
    },
    {
      "data": {
        "id": "e437",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2604_12149",
        "weight": 0.8023
      }
    },
    {
      "data": {
        "id": "e438",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2009_10484",
        "weight": 0.8152
      }
    },
    {
      "data": {
        "id": "e439",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2409_16012",
        "weight": 0.812
      }
    },
    {
      "data": {
        "id": "e440",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2410_19414",
        "weight": 0.8214
      }
    },
    {
      "data": {
        "id": "e441",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.815
      }
    },
    {
      "data": {
        "id": "e442",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "1306_3532",
        "weight": 0.8092
      }
    },
    {
      "data": {
        "id": "e443",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2013_luna_anytime_solution_optimization_for",
        "weight": 0.8158
      }
    },
    {
      "data": {
        "id": "e444",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8145
      }
    },
    {
      "data": {
        "id": "e445",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "1407_2896",
        "weight": 0.8133
      }
    },
    {
      "data": {
        "id": "e446",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2203_01751",
        "weight": 0.8347
      }
    },
    {
      "data": {
        "id": "e447",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2506_22087",
        "weight": 0.8126
      }
    },
    {
      "data": {
        "id": "e448",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2508_21001",
        "weight": 0.8153
      }
    },
    {
      "data": {
        "id": "e449",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2016_rajamaki_sampled_differential_dynamic_programming",
        "weight": 0.8059
      }
    },
    {
      "data": {
        "id": "e450",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2307_03167",
        "weight": 0.8256
      }
    },
    {
      "data": {
        "id": "e451",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2309_12566",
        "weight": 0.8134
      }
    },
    {
      "data": {
        "id": "e452",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "1809_02399",
        "weight": 0.8161
      }
    },
    {
      "data": {
        "id": "e453",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "1809_10252",
        "weight": 0.8045
      }
    },
    {
      "data": {
        "id": "e454",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "1907_01474",
        "weight": 0.8037
      }
    },
    {
      "data": {
        "id": "e455",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2403_10745",
        "weight": 0.8119
      }
    },
    {
      "data": {
        "id": "e456",
        "source": "2011_kalakrishnan_stomp_stochastic_trajectory_optimization",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8
      }
    },
    {
      "data": {
        "id": "e457",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2409_12266",
        "weight": 0.8079
      }
    },
    {
      "data": {
        "id": "e458",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2009_10484",
        "weight": 0.828
      }
    },
    {
      "data": {
        "id": "e459",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2410_19414",
        "weight": 0.8306
      }
    },
    {
      "data": {
        "id": "e460",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8833
      }
    },
    {
      "data": {
        "id": "e461",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2411_15651",
        "weight": 0.8644
      }
    },
    {
      "data": {
        "id": "e462",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8851
      }
    },
    {
      "data": {
        "id": "e463",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2411_17293",
        "weight": 0.8036
      }
    },
    {
      "data": {
        "id": "e464",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2411_17902",
        "weight": 0.8384
      }
    },
    {
      "data": {
        "id": "e465",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2412_11270",
        "weight": 0.8438
      }
    },
    {
      "data": {
        "id": "e466",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "1204_6453",
        "weight": 0.8786
      }
    },
    {
      "data": {
        "id": "e467",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "1205_5088",
        "weight": 0.8271
      }
    },
    {
      "data": {
        "id": "e468",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2012_perez_lqr_rrt_star_optimal",
        "weight": 0.8421
      }
    },
    {
      "data": {
        "id": "e469",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "1306_3532",
        "weight": 0.8554
      }
    },
    {
      "data": {
        "id": "e470",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2502_09556",
        "weight": 0.8513
      }
    },
    {
      "data": {
        "id": "e471",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2013_luna_anytime_solution_optimization_for",
        "weight": 0.856
      }
    },
    {
      "data": {
        "id": "e472",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2013_yang_spline_based_rrt_path",
        "weight": 0.8597
      }
    },
    {
      "data": {
        "id": "e473",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8061
      }
    },
    {
      "data": {
        "id": "e474",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "1404_2334",
        "weight": 0.8913
      }
    },
    {
      "data": {
        "id": "e475",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "1405_5848",
        "weight": 0.857
      }
    },
    {
      "data": {
        "id": "e476",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2503_06757",
        "weight": 0.8398
      }
    },
    {
      "data": {
        "id": "e477",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2201_03163",
        "weight": 0.8496
      }
    },
    {
      "data": {
        "id": "e478",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "1407_2896",
        "weight": 0.8158
      }
    },
    {
      "data": {
        "id": "e479",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2503_16164",
        "weight": 0.8751
      }
    },
    {
      "data": {
        "id": "e480",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2203_01751",
        "weight": 0.8154
      }
    },
    {
      "data": {
        "id": "e481",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8067
      }
    },
    {
      "data": {
        "id": "e482",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2203_02176",
        "weight": 0.8691
      }
    },
    {
      "data": {
        "id": "e483",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "1505_04098",
        "weight": 0.8074
      }
    },
    {
      "data": {
        "id": "e484",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2505_10542",
        "weight": 0.8625
      }
    },
    {
      "data": {
        "id": "e485",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.8959
      }
    },
    {
      "data": {
        "id": "e486",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8989
      }
    },
    {
      "data": {
        "id": "e487",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2015_palmieri_distance_metric_learning_for",
        "weight": 0.829
      }
    },
    {
      "data": {
        "id": "e488",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2210_01744",
        "weight": 0.8007
      }
    },
    {
      "data": {
        "id": "e489",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2508_21001",
        "weight": 0.8467
      }
    },
    {
      "data": {
        "id": "e490",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2016_choudhury_regionally_accelerated_batch_informed",
        "weight": 0.8091
      }
    },
    {
      "data": {
        "id": "e491",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2301_11902",
        "weight": 0.8038
      }
    },
    {
      "data": {
        "id": "e492",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2301_13143",
        "weight": 0.8956
      }
    },
    {
      "data": {
        "id": "e493",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2302_11670",
        "weight": 0.8352
      }
    },
    {
      "data": {
        "id": "e494",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2510_21074",
        "weight": 0.8274
      }
    },
    {
      "data": {
        "id": "e495",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2305_01072",
        "weight": 0.8043
      }
    },
    {
      "data": {
        "id": "e496",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "1708_06056",
        "weight": 0.8386
      }
    },
    {
      "data": {
        "id": "e497",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2307_03167",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e498",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "1710_10122",
        "weight": 0.8631
      }
    },
    {
      "data": {
        "id": "e499",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2511_18170",
        "weight": 0.8074
      }
    },
    {
      "data": {
        "id": "e500",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2309_14595",
        "weight": 0.8538
      }
    },
    {
      "data": {
        "id": "e501",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "1809_02399",
        "weight": 0.8787
      }
    },
    {
      "data": {
        "id": "e502",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "1809_07051",
        "weight": 0.891
      }
    },
    {
      "data": {
        "id": "e503",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "1909_09688",
        "weight": 0.8743
      }
    },
    {
      "data": {
        "id": "e504",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2403_01194",
        "weight": 0.8735
      }
    },
    {
      "data": {
        "id": "e505",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2403_10745",
        "weight": 0.8725
      }
    },
    {
      "data": {
        "id": "e506",
        "source": "2011_karaman_anytime_motion_planning_using",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e507",
        "source": "1204_6453",
        "target": "2009_10484",
        "weight": 0.8588
      }
    },
    {
      "data": {
        "id": "e508",
        "source": "1204_6453",
        "target": "2410_19414",
        "weight": 0.8287
      }
    },
    {
      "data": {
        "id": "e509",
        "source": "1204_6453",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8755
      }
    },
    {
      "data": {
        "id": "e510",
        "source": "1204_6453",
        "target": "2411_15651",
        "weight": 0.8176
      }
    },
    {
      "data": {
        "id": "e511",
        "source": "1204_6453",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.852
      }
    },
    {
      "data": {
        "id": "e512",
        "source": "1204_6453",
        "target": "2411_17902",
        "weight": 0.8269
      }
    },
    {
      "data": {
        "id": "e513",
        "source": "1204_6453",
        "target": "1205_5088",
        "weight": 0.8056
      }
    },
    {
      "data": {
        "id": "e514",
        "source": "1204_6453",
        "target": "2012_perez_lqr_rrt_star_optimal",
        "weight": 0.8235
      }
    },
    {
      "data": {
        "id": "e515",
        "source": "1204_6453",
        "target": "1306_3532",
        "weight": 0.8807
      }
    },
    {
      "data": {
        "id": "e516",
        "source": "1204_6453",
        "target": "2502_09556",
        "weight": 0.8055
      }
    },
    {
      "data": {
        "id": "e517",
        "source": "1204_6453",
        "target": "2013_luna_anytime_solution_optimization_for",
        "weight": 0.8329
      }
    },
    {
      "data": {
        "id": "e518",
        "source": "1204_6453",
        "target": "2013_yang_spline_based_rrt_path",
        "weight": 0.8228
      }
    },
    {
      "data": {
        "id": "e519",
        "source": "1204_6453",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8059
      }
    },
    {
      "data": {
        "id": "e520",
        "source": "1204_6453",
        "target": "1404_2334",
        "weight": 0.8874
      }
    },
    {
      "data": {
        "id": "e521",
        "source": "1204_6453",
        "target": "1405_5848",
        "weight": 0.866
      }
    },
    {
      "data": {
        "id": "e522",
        "source": "1204_6453",
        "target": "2503_06757",
        "weight": 0.8067
      }
    },
    {
      "data": {
        "id": "e523",
        "source": "1204_6453",
        "target": "2503_16164",
        "weight": 0.8637
      }
    },
    {
      "data": {
        "id": "e524",
        "source": "1204_6453",
        "target": "1407_2896",
        "weight": 0.8451
      }
    },
    {
      "data": {
        "id": "e525",
        "source": "1204_6453",
        "target": "2203_01751",
        "weight": 0.8214
      }
    },
    {
      "data": {
        "id": "e526",
        "source": "1204_6453",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.823
      }
    },
    {
      "data": {
        "id": "e527",
        "source": "1204_6453",
        "target": "2203_02176",
        "weight": 0.8174
      }
    },
    {
      "data": {
        "id": "e528",
        "source": "1204_6453",
        "target": "1505_04098",
        "weight": 0.8032
      }
    },
    {
      "data": {
        "id": "e529",
        "source": "1204_6453",
        "target": "2505_10542",
        "weight": 0.8329
      }
    },
    {
      "data": {
        "id": "e530",
        "source": "1204_6453",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.8674
      }
    },
    {
      "data": {
        "id": "e531",
        "source": "1204_6453",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8953
      }
    },
    {
      "data": {
        "id": "e532",
        "source": "1204_6453",
        "target": "2016_choudhury_regionally_accelerated_batch_informed",
        "weight": 0.8328
      }
    },
    {
      "data": {
        "id": "e533",
        "source": "1204_6453",
        "target": "2301_13143",
        "weight": 0.8549
      }
    },
    {
      "data": {
        "id": "e534",
        "source": "1204_6453",
        "target": "2510_21074",
        "weight": 0.8184
      }
    },
    {
      "data": {
        "id": "e535",
        "source": "1204_6453",
        "target": "1708_06056",
        "weight": 0.8223
      }
    },
    {
      "data": {
        "id": "e536",
        "source": "1204_6453",
        "target": "1710_10122",
        "weight": 0.8323
      }
    },
    {
      "data": {
        "id": "e537",
        "source": "1204_6453",
        "target": "2309_14595",
        "weight": 0.8294
      }
    },
    {
      "data": {
        "id": "e538",
        "source": "1204_6453",
        "target": "1809_02399",
        "weight": 0.8621
      }
    },
    {
      "data": {
        "id": "e539",
        "source": "1204_6453",
        "target": "1809_07051",
        "weight": 0.8661
      }
    },
    {
      "data": {
        "id": "e540",
        "source": "1204_6453",
        "target": "1909_09688",
        "weight": 0.8967
      }
    },
    {
      "data": {
        "id": "e541",
        "source": "1204_6453",
        "target": "2403_01194",
        "weight": 0.8021
      }
    },
    {
      "data": {
        "id": "e542",
        "source": "1204_6453",
        "target": "2403_10745",
        "weight": 0.8411
      }
    },
    {
      "data": {
        "id": "e543",
        "source": "1205_5088",
        "target": "2010_00411",
        "weight": 0.8052
      }
    },
    {
      "data": {
        "id": "e544",
        "source": "1205_5088",
        "target": "2103_03293",
        "weight": 0.8182
      }
    },
    {
      "data": {
        "id": "e545",
        "source": "1205_5088",
        "target": "2012_perez_lqr_rrt_star_optimal",
        "weight": 0.9075
      }
    },
    {
      "data": {
        "id": "e546",
        "source": "1205_5088",
        "target": "2109_07081",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e547",
        "source": "1205_5088",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8603
      }
    },
    {
      "data": {
        "id": "e548",
        "source": "1205_5088",
        "target": "1404_2334",
        "weight": 0.8085
      }
    },
    {
      "data": {
        "id": "e549",
        "source": "1205_5088",
        "target": "1407_2896",
        "weight": 0.8738
      }
    },
    {
      "data": {
        "id": "e550",
        "source": "1205_5088",
        "target": "1411_4045",
        "weight": 0.8203
      }
    },
    {
      "data": {
        "id": "e551",
        "source": "1205_5088",
        "target": "2203_01751",
        "weight": 0.8073
      }
    },
    {
      "data": {
        "id": "e552",
        "source": "1205_5088",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8033
      }
    },
    {
      "data": {
        "id": "e553",
        "source": "1205_5088",
        "target": "2203_02176",
        "weight": 0.8153
      }
    },
    {
      "data": {
        "id": "e554",
        "source": "1205_5088",
        "target": "2504_18978",
        "weight": 0.8002
      }
    },
    {
      "data": {
        "id": "e555",
        "source": "1205_5088",
        "target": "2204_02322",
        "weight": 0.8042
      }
    },
    {
      "data": {
        "id": "e556",
        "source": "1205_5088",
        "target": "1505_04098",
        "weight": 0.8392
      }
    },
    {
      "data": {
        "id": "e557",
        "source": "1205_5088",
        "target": "2505_10542",
        "weight": 0.812
      }
    },
    {
      "data": {
        "id": "e558",
        "source": "1205_5088",
        "target": "2205_04422",
        "weight": 0.8055
      }
    },
    {
      "data": {
        "id": "e559",
        "source": "1205_5088",
        "target": "1511_05259",
        "weight": 0.8339
      }
    },
    {
      "data": {
        "id": "e560",
        "source": "1205_5088",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.8205
      }
    },
    {
      "data": {
        "id": "e561",
        "source": "1205_5088",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8181
      }
    },
    {
      "data": {
        "id": "e562",
        "source": "1205_5088",
        "target": "2015_palmieri_distance_metric_learning_for",
        "weight": 0.808
      }
    },
    {
      "data": {
        "id": "e563",
        "source": "1205_5088",
        "target": "2210_01744",
        "weight": 0.8755
      }
    },
    {
      "data": {
        "id": "e564",
        "source": "1205_5088",
        "target": "2508_21001",
        "weight": 0.8235
      }
    },
    {
      "data": {
        "id": "e565",
        "source": "1205_5088",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8014
      }
    },
    {
      "data": {
        "id": "e566",
        "source": "1205_5088",
        "target": "2016_rajamaki_sampled_differential_dynamic_programming",
        "weight": 0.8116
      }
    },
    {
      "data": {
        "id": "e567",
        "source": "1205_5088",
        "target": "2301_13143",
        "weight": 0.836
      }
    },
    {
      "data": {
        "id": "e568",
        "source": "1205_5088",
        "target": "1710_10122",
        "weight": 0.8763
      }
    },
    {
      "data": {
        "id": "e569",
        "source": "1205_5088",
        "target": "1711_11006",
        "weight": 0.8003
      }
    },
    {
      "data": {
        "id": "e570",
        "source": "1205_5088",
        "target": "2017_roesmann_kinodynamic_trajectory_optimization_and",
        "weight": 0.8114
      }
    },
    {
      "data": {
        "id": "e571",
        "source": "1205_5088",
        "target": "2311_06404",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e572",
        "source": "1205_5088",
        "target": "1809_02399",
        "weight": 0.8849
      }
    },
    {
      "data": {
        "id": "e573",
        "source": "1205_5088",
        "target": "1809_07051",
        "weight": 0.834
      }
    },
    {
      "data": {
        "id": "e574",
        "source": "1205_5088",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8202
      }
    },
    {
      "data": {
        "id": "e575",
        "source": "1205_5088",
        "target": "2603_16059",
        "weight": 0.8671
      }
    },
    {
      "data": {
        "id": "e576",
        "source": "1205_5088",
        "target": "1909_09688",
        "weight": 0.8315
      }
    },
    {
      "data": {
        "id": "e577",
        "source": "1205_5088",
        "target": "2403_10745",
        "weight": 0.8704
      }
    },
    {
      "data": {
        "id": "e578",
        "source": "1205_5088",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8314
      }
    },
    {
      "data": {
        "id": "e579",
        "source": "1206_4621",
        "target": "2004_08763",
        "weight": 0.8143
      }
    },
    {
      "data": {
        "id": "e580",
        "source": "1206_4621",
        "target": "2511_02015",
        "weight": 0.807
      }
    },
    {
      "data": {
        "id": "e581",
        "source": "1206_4621",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.7977
      }
    },
    {
      "data": {
        "id": "e582",
        "source": "1206_4621",
        "target": "2309_12566",
        "weight": 0.8491
      }
    },
    {
      "data": {
        "id": "e583",
        "source": "1206_4621",
        "target": "2019_lefebvre_path_integral_policy_improvement",
        "weight": 0.9264
      }
    },
    {
      "data": {
        "id": "e584",
        "source": "2012_kobilarov_cross_entropy_motion_planning",
        "target": "2004_08763",
        "weight": 0.9045
      }
    },
    {
      "data": {
        "id": "e585",
        "source": "2012_kobilarov_cross_entropy_motion_planning",
        "target": "2409_12266",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e586",
        "source": "2012_kobilarov_cross_entropy_motion_planning",
        "target": "1809_02399",
        "weight": 0.8009
      }
    },
    {
      "data": {
        "id": "e587",
        "source": "2012_kobilarov_cross_entropy_motion_planning",
        "target": "2009_10484",
        "weight": 0.8198
      }
    },
    {
      "data": {
        "id": "e588",
        "source": "2012_kobilarov_cross_entropy_motion_planning",
        "target": "2301_13143",
        "weight": 0.8107
      }
    },
    {
      "data": {
        "id": "e589",
        "source": "2012_kobilarov_cross_entropy_motion_planning",
        "target": "2018_kingston_sampling_based_methods_for",
        "weight": 0.8111
      }
    },
    {
      "data": {
        "id": "e590",
        "source": "2012_kobilarov_cross_entropy_motion_planning",
        "target": "2410_19414",
        "weight": 0.8352
      }
    },
    {
      "data": {
        "id": "e591",
        "source": "2012_kobilarov_cross_entropy_motion_planning",
        "target": "2411_15651",
        "weight": 0.8046
      }
    },
    {
      "data": {
        "id": "e592",
        "source": "2012_kobilarov_cross_entropy_motion_planning",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8039
      }
    },
    {
      "data": {
        "id": "e593",
        "source": "2012_kobilarov_cross_entropy_motion_planning",
        "target": "1709_05448",
        "weight": 0.8163
      }
    },
    {
      "data": {
        "id": "e594",
        "source": "2012_kobilarov_cross_entropy_motion_planning",
        "target": "2309_12566",
        "weight": 0.8022
      }
    },
    {
      "data": {
        "id": "e595",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2409_12266",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e596",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2009_10484",
        "weight": 0.8092
      }
    },
    {
      "data": {
        "id": "e597",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2410_19414",
        "weight": 0.8194
      }
    },
    {
      "data": {
        "id": "e598",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8069
      }
    },
    {
      "data": {
        "id": "e599",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2411_15651",
        "weight": 0.8116
      }
    },
    {
      "data": {
        "id": "e600",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8257
      }
    },
    {
      "data": {
        "id": "e601",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2411_17293",
        "weight": 0.817
      }
    },
    {
      "data": {
        "id": "e602",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2412_11270",
        "weight": 0.8081
      }
    },
    {
      "data": {
        "id": "e603",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2109_07081",
        "weight": 0.8106
      }
    },
    {
      "data": {
        "id": "e604",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2013_luna_anytime_solution_optimization_for",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e605",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2013_yang_spline_based_rrt_path",
        "weight": 0.8109
      }
    },
    {
      "data": {
        "id": "e606",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8366
      }
    },
    {
      "data": {
        "id": "e607",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "1404_2334",
        "weight": 0.8468
      }
    },
    {
      "data": {
        "id": "e608",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2503_16164",
        "weight": 0.8132
      }
    },
    {
      "data": {
        "id": "e609",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "1407_2896",
        "weight": 0.85
      }
    },
    {
      "data": {
        "id": "e610",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "1411_4045",
        "weight": 0.8008
      }
    },
    {
      "data": {
        "id": "e611",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2203_01751",
        "weight": 0.8204
      }
    },
    {
      "data": {
        "id": "e612",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8101
      }
    },
    {
      "data": {
        "id": "e613",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2203_02176",
        "weight": 0.8223
      }
    },
    {
      "data": {
        "id": "e614",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "1505_04098",
        "weight": 0.8192
      }
    },
    {
      "data": {
        "id": "e615",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2505_10542",
        "weight": 0.8286
      }
    },
    {
      "data": {
        "id": "e616",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2506_14865",
        "weight": 0.8028
      }
    },
    {
      "data": {
        "id": "e617",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "1511_05259",
        "weight": 0.8292
      }
    },
    {
      "data": {
        "id": "e618",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.8286
      }
    },
    {
      "data": {
        "id": "e619",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8328
      }
    },
    {
      "data": {
        "id": "e620",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2015_palmieri_distance_metric_learning_for",
        "weight": 0.8473
      }
    },
    {
      "data": {
        "id": "e621",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2210_01744",
        "weight": 0.8558
      }
    },
    {
      "data": {
        "id": "e622",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2508_21001",
        "weight": 0.8211
      }
    },
    {
      "data": {
        "id": "e623",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2301_13143",
        "weight": 0.8459
      }
    },
    {
      "data": {
        "id": "e624",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2304_00346",
        "weight": 0.817
      }
    },
    {
      "data": {
        "id": "e625",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "1709_05448",
        "weight": 0.802
      }
    },
    {
      "data": {
        "id": "e626",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "1710_10122",
        "weight": 0.8861
      }
    },
    {
      "data": {
        "id": "e627",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "1711_11006",
        "weight": 0.8021
      }
    },
    {
      "data": {
        "id": "e628",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2309_14595",
        "weight": 0.8219
      }
    },
    {
      "data": {
        "id": "e629",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2602_00992",
        "weight": 0.8038
      }
    },
    {
      "data": {
        "id": "e630",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "1809_02399",
        "weight": 0.886
      }
    },
    {
      "data": {
        "id": "e631",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "1809_07051",
        "weight": 0.8376
      }
    },
    {
      "data": {
        "id": "e632",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2603_06773",
        "weight": 0.8073
      }
    },
    {
      "data": {
        "id": "e633",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2018_kingston_sampling_based_methods_for",
        "weight": 0.803
      }
    },
    {
      "data": {
        "id": "e634",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2603_14197",
        "weight": 0.8018
      }
    },
    {
      "data": {
        "id": "e635",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2603_16059",
        "weight": 0.8261
      }
    },
    {
      "data": {
        "id": "e636",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "1909_09688",
        "weight": 0.8444
      }
    },
    {
      "data": {
        "id": "e637",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2403_10745",
        "weight": 0.862
      }
    },
    {
      "data": {
        "id": "e638",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8521
      }
    },
    {
      "data": {
        "id": "e639",
        "source": "2012_perez_lqr_rrt_star_optimal",
        "target": "2019_jackson_altro_a_fast_solver",
        "weight": 0.8125
      }
    },
    {
      "data": {
        "id": "e640",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2409_15610",
        "weight": 0.802
      }
    },
    {
      "data": {
        "id": "e641",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2010_00411",
        "weight": 0.8169
      }
    },
    {
      "data": {
        "id": "e642",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2103_03293",
        "weight": 0.8201
      }
    },
    {
      "data": {
        "id": "e643",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2109_07081",
        "weight": 0.8342
      }
    },
    {
      "data": {
        "id": "e644",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2503_04613",
        "weight": 0.8277
      }
    },
    {
      "data": {
        "id": "e645",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2204_02322",
        "weight": 0.8255
      }
    },
    {
      "data": {
        "id": "e646",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2207_06362",
        "weight": 0.8333
      }
    },
    {
      "data": {
        "id": "e647",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8238
      }
    },
    {
      "data": {
        "id": "e648",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2016_rajamaki_sampled_differential_dynamic_programming",
        "weight": 0.8104
      }
    },
    {
      "data": {
        "id": "e649",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2303_16746",
        "weight": 0.8071
      }
    },
    {
      "data": {
        "id": "e650",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2304_00346",
        "weight": 0.8568
      }
    },
    {
      "data": {
        "id": "e651",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2305_09619",
        "weight": 0.8078
      }
    },
    {
      "data": {
        "id": "e652",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "1711_11006",
        "weight": 0.817
      }
    },
    {
      "data": {
        "id": "e653",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "1806_09460",
        "weight": 0.804
      }
    },
    {
      "data": {
        "id": "e654",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8567
      }
    },
    {
      "data": {
        "id": "e655",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "1903_00155",
        "weight": 0.8034
      }
    },
    {
      "data": {
        "id": "e656",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2403_00748",
        "weight": 0.8167
      }
    },
    {
      "data": {
        "id": "e657",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e658",
        "source": "2012_tassa_synthesis_and_stabilization_of",
        "target": "2019_jackson_altro_a_fast_solver",
        "weight": 0.8084
      }
    },
    {
      "data": {
        "id": "e659",
        "source": "1305_6644",
        "target": "2208_05888",
        "weight": 0.6956
      }
    },
    {
      "data": {
        "id": "e660",
        "source": "1305_6644",
        "target": "2010_10726",
        "weight": 0.7299
      }
    },
    {
      "data": {
        "id": "e661",
        "source": "1306_3532",
        "target": "2409_12266",
        "weight": 0.8111
      }
    },
    {
      "data": {
        "id": "e662",
        "source": "1306_3532",
        "target": "2009_10484",
        "weight": 0.8549
      }
    },
    {
      "data": {
        "id": "e663",
        "source": "1306_3532",
        "target": "2410_19414",
        "weight": 0.8327
      }
    },
    {
      "data": {
        "id": "e664",
        "source": "1306_3532",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8408
      }
    },
    {
      "data": {
        "id": "e665",
        "source": "1306_3532",
        "target": "2411_15651",
        "weight": 0.8321
      }
    },
    {
      "data": {
        "id": "e666",
        "source": "1306_3532",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8216
      }
    },
    {
      "data": {
        "id": "e667",
        "source": "1306_3532",
        "target": "2411_17902",
        "weight": 0.8407
      }
    },
    {
      "data": {
        "id": "e668",
        "source": "1306_3532",
        "target": "2412_11270",
        "weight": 0.8307
      }
    },
    {
      "data": {
        "id": "e669",
        "source": "1306_3532",
        "target": "2502_09556",
        "weight": 0.8997
      }
    },
    {
      "data": {
        "id": "e670",
        "source": "1306_3532",
        "target": "2013_luna_anytime_solution_optimization_for",
        "weight": 0.8281
      }
    },
    {
      "data": {
        "id": "e671",
        "source": "1306_3532",
        "target": "2013_yang_spline_based_rrt_path",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e672",
        "source": "1306_3532",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8332
      }
    },
    {
      "data": {
        "id": "e673",
        "source": "1306_3532",
        "target": "1404_2334",
        "weight": 0.8748
      }
    },
    {
      "data": {
        "id": "e674",
        "source": "1306_3532",
        "target": "1405_5848",
        "weight": 0.8654
      }
    },
    {
      "data": {
        "id": "e675",
        "source": "1306_3532",
        "target": "2503_16164",
        "weight": 0.8739
      }
    },
    {
      "data": {
        "id": "e676",
        "source": "1306_3532",
        "target": "1407_2896",
        "weight": 0.856
      }
    },
    {
      "data": {
        "id": "e677",
        "source": "1306_3532",
        "target": "2203_01751",
        "weight": 0.8567
      }
    },
    {
      "data": {
        "id": "e678",
        "source": "1306_3532",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8379
      }
    },
    {
      "data": {
        "id": "e679",
        "source": "1306_3532",
        "target": "2203_02176",
        "weight": 0.8204
      }
    },
    {
      "data": {
        "id": "e680",
        "source": "1306_3532",
        "target": "2504_18978",
        "weight": 0.8026
      }
    },
    {
      "data": {
        "id": "e681",
        "source": "1306_3532",
        "target": "1505_04098",
        "weight": 0.8327
      }
    },
    {
      "data": {
        "id": "e682",
        "source": "1306_3532",
        "target": "2505_10542",
        "weight": 0.8269
      }
    },
    {
      "data": {
        "id": "e683",
        "source": "1306_3532",
        "target": "2205_04422",
        "weight": 0.8001
      }
    },
    {
      "data": {
        "id": "e684",
        "source": "1306_3532",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.8449
      }
    },
    {
      "data": {
        "id": "e685",
        "source": "1306_3532",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.865
      }
    },
    {
      "data": {
        "id": "e686",
        "source": "1306_3532",
        "target": "2508_21001",
        "weight": 0.8197
      }
    },
    {
      "data": {
        "id": "e687",
        "source": "1306_3532",
        "target": "2016_choudhury_regionally_accelerated_batch_informed",
        "weight": 0.8222
      }
    },
    {
      "data": {
        "id": "e688",
        "source": "1306_3532",
        "target": "2301_13143",
        "weight": 0.8411
      }
    },
    {
      "data": {
        "id": "e689",
        "source": "1306_3532",
        "target": "2302_11670",
        "weight": 0.8132
      }
    },
    {
      "data": {
        "id": "e690",
        "source": "1306_3532",
        "target": "1705_02403",
        "weight": 0.8745
      }
    },
    {
      "data": {
        "id": "e691",
        "source": "1306_3532",
        "target": "2510_21074",
        "weight": 0.8083
      }
    },
    {
      "data": {
        "id": "e692",
        "source": "1306_3532",
        "target": "2305_01072",
        "weight": 0.8157
      }
    },
    {
      "data": {
        "id": "e693",
        "source": "1306_3532",
        "target": "1708_06056",
        "weight": 0.8071
      }
    },
    {
      "data": {
        "id": "e694",
        "source": "1306_3532",
        "target": "1709_05448",
        "weight": 0.8006
      }
    },
    {
      "data": {
        "id": "e695",
        "source": "1306_3532",
        "target": "1709_07610",
        "weight": 0.8146
      }
    },
    {
      "data": {
        "id": "e696",
        "source": "1306_3532",
        "target": "1710_10122",
        "weight": 0.8298
      }
    },
    {
      "data": {
        "id": "e697",
        "source": "1306_3532",
        "target": "2309_14545",
        "weight": 0.8153
      }
    },
    {
      "data": {
        "id": "e698",
        "source": "1306_3532",
        "target": "2309_14595",
        "weight": 0.8115
      }
    },
    {
      "data": {
        "id": "e699",
        "source": "1306_3532",
        "target": "2602_02846",
        "weight": 0.8329
      }
    },
    {
      "data": {
        "id": "e700",
        "source": "1306_3532",
        "target": "1809_02399",
        "weight": 0.8691
      }
    },
    {
      "data": {
        "id": "e701",
        "source": "1306_3532",
        "target": "1809_07051",
        "weight": 0.8646
      }
    },
    {
      "data": {
        "id": "e702",
        "source": "1306_3532",
        "target": "1909_09688",
        "weight": 0.8637
      }
    },
    {
      "data": {
        "id": "e703",
        "source": "1306_3532",
        "target": "2403_01194",
        "weight": 0.8138
      }
    },
    {
      "data": {
        "id": "e704",
        "source": "1306_3532",
        "target": "2403_10745",
        "weight": 0.8401
      }
    },
    {
      "data": {
        "id": "e705",
        "source": "1306_3532",
        "target": "2406_02807",
        "weight": 0.8022
      }
    },
    {
      "data": {
        "id": "e706",
        "source": "1312_0041",
        "target": "2022_schmid_dynamic_mode_decomposition_and",
        "weight": 0.9043
      }
    },
    {
      "data": {
        "id": "e707",
        "source": "1312_0041",
        "target": "1707_01146",
        "weight": 0.8548
      }
    },
    {
      "data": {
        "id": "e708",
        "source": "1312_0041",
        "target": "1408_4408",
        "weight": 0.9044
      }
    },
    {
      "data": {
        "id": "e709",
        "source": "1312_0041",
        "target": "1409_6358",
        "weight": 0.8781
      }
    },
    {
      "data": {
        "id": "e710",
        "source": "1312_0041",
        "target": "2511_00814",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e711",
        "source": "1312_0041",
        "target": "1909_10466",
        "weight": 0.9041
      }
    },
    {
      "data": {
        "id": "e712",
        "source": "1312_0041",
        "target": "1509_03580",
        "weight": 0.8207
      }
    },
    {
      "data": {
        "id": "e713",
        "source": "2013_lipp_minimum_time_speed_optimisation_over",
        "target": "2205_04422",
        "weight": 0.8057
      }
    },
    {
      "data": {
        "id": "e714",
        "source": "2013_lipp_minimum_time_speed_optimisation_over",
        "target": "2018_zhang_toward_a_more_complete",
        "weight": 0.859
      }
    },
    {
      "data": {
        "id": "e715",
        "source": "2013_lipp_minimum_time_speed_optimisation_over",
        "target": "1707_07239",
        "weight": 0.8033
      }
    },
    {
      "data": {
        "id": "e716",
        "source": "2013_lipp_minimum_time_speed_optimisation_over",
        "target": "2504_18978",
        "weight": 0.8345
      }
    },
    {
      "data": {
        "id": "e717",
        "source": "2013_lipp_minimum_time_speed_optimisation_over",
        "target": "1506_01085",
        "weight": 0.834
      }
    },
    {
      "data": {
        "id": "e718",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2409_12266",
        "weight": 0.8284
      }
    },
    {
      "data": {
        "id": "e719",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2009_10484",
        "weight": 0.8815
      }
    },
    {
      "data": {
        "id": "e720",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2410_19414",
        "weight": 0.8586
      }
    },
    {
      "data": {
        "id": "e721",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8074
      }
    },
    {
      "data": {
        "id": "e722",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2411_15651",
        "weight": 0.8027
      }
    },
    {
      "data": {
        "id": "e723",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2411_17902",
        "weight": 0.8071
      }
    },
    {
      "data": {
        "id": "e724",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8295
      }
    },
    {
      "data": {
        "id": "e725",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "1404_2334",
        "weight": 0.8377
      }
    },
    {
      "data": {
        "id": "e726",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "1405_5848",
        "weight": 0.8335
      }
    },
    {
      "data": {
        "id": "e727",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2503_16164",
        "weight": 0.8265
      }
    },
    {
      "data": {
        "id": "e728",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "1407_2896",
        "weight": 0.8528
      }
    },
    {
      "data": {
        "id": "e729",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2203_01751",
        "weight": 0.8543
      }
    },
    {
      "data": {
        "id": "e730",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.838
      }
    },
    {
      "data": {
        "id": "e731",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2504_18978",
        "weight": 0.8136
      }
    },
    {
      "data": {
        "id": "e732",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "1505_04098",
        "weight": 0.8153
      }
    },
    {
      "data": {
        "id": "e733",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2205_04422",
        "weight": 0.8103
      }
    },
    {
      "data": {
        "id": "e734",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.8201
      }
    },
    {
      "data": {
        "id": "e735",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8446
      }
    },
    {
      "data": {
        "id": "e736",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2508_05027",
        "weight": 0.8366
      }
    },
    {
      "data": {
        "id": "e737",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2508_21001",
        "weight": 0.8027
      }
    },
    {
      "data": {
        "id": "e738",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2016_choudhury_regionally_accelerated_batch_informed",
        "weight": 0.8036
      }
    },
    {
      "data": {
        "id": "e739",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2301_13143",
        "weight": 0.8313
      }
    },
    {
      "data": {
        "id": "e740",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "1707_07239",
        "weight": 0.8036
      }
    },
    {
      "data": {
        "id": "e741",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "1708_06056",
        "weight": 0.8388
      }
    },
    {
      "data": {
        "id": "e742",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2305_01072",
        "weight": 0.8348
      }
    },
    {
      "data": {
        "id": "e743",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2309_14545",
        "weight": 0.8283
      }
    },
    {
      "data": {
        "id": "e744",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2602_02846",
        "weight": 0.8135
      }
    },
    {
      "data": {
        "id": "e745",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "1809_02399",
        "weight": 0.8526
      }
    },
    {
      "data": {
        "id": "e746",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "1809_10252",
        "weight": 0.8028
      }
    },
    {
      "data": {
        "id": "e747",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2018_kingston_sampling_based_methods_for",
        "weight": 0.8236
      }
    },
    {
      "data": {
        "id": "e748",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "1909_09688",
        "weight": 0.8187
      }
    },
    {
      "data": {
        "id": "e749",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2403_10745",
        "weight": 0.8196
      }
    },
    {
      "data": {
        "id": "e750",
        "source": "2013_luna_anytime_solution_optimization_for",
        "target": "2405_03281",
        "weight": 0.8141
      }
    },
    {
      "data": {
        "id": "e751",
        "source": "2013_palamakumburu_minimum_jerk_trajectory_generation",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8047
      }
    },
    {
      "data": {
        "id": "e752",
        "source": "2013_palamakumburu_minimum_jerk_trajectory_generation",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8071
      }
    },
    {
      "data": {
        "id": "e753",
        "source": "2013_palamakumburu_minimum_jerk_trajectory_generation",
        "target": "1801_08995",
        "weight": 0.8006
      }
    },
    {
      "data": {
        "id": "e754",
        "source": "2013_palamakumburu_minimum_jerk_trajectory_generation",
        "target": "2208_02439",
        "weight": 0.8132
      }
    },
    {
      "data": {
        "id": "e755",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.823
      }
    },
    {
      "data": {
        "id": "e756",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8806
      }
    },
    {
      "data": {
        "id": "e757",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "2502_09556",
        "weight": 0.8096
      }
    },
    {
      "data": {
        "id": "e758",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "1404_2334",
        "weight": 0.8483
      }
    },
    {
      "data": {
        "id": "e759",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "2201_03163",
        "weight": 0.8363
      }
    },
    {
      "data": {
        "id": "e760",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "2503_16164",
        "weight": 0.8335
      }
    },
    {
      "data": {
        "id": "e761",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "2203_02176",
        "weight": 0.8407
      }
    },
    {
      "data": {
        "id": "e762",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.8307
      }
    },
    {
      "data": {
        "id": "e763",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8213
      }
    },
    {
      "data": {
        "id": "e764",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "2301_13143",
        "weight": 0.8346
      }
    },
    {
      "data": {
        "id": "e765",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "2302_11670",
        "weight": 0.8008
      }
    },
    {
      "data": {
        "id": "e766",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "1710_10122",
        "weight": 0.8218
      }
    },
    {
      "data": {
        "id": "e767",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "2309_14595",
        "weight": 0.8465
      }
    },
    {
      "data": {
        "id": "e768",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "1809_02399",
        "weight": 0.8123
      }
    },
    {
      "data": {
        "id": "e769",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "1809_07051",
        "weight": 0.8366
      }
    },
    {
      "data": {
        "id": "e770",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "1909_09688",
        "weight": 0.8128
      }
    },
    {
      "data": {
        "id": "e771",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "2403_01194",
        "weight": 0.8271
      }
    },
    {
      "data": {
        "id": "e772",
        "source": "2013_yang_spline_based_rrt_path",
        "target": "2403_10745",
        "weight": 0.8293
      }
    },
    {
      "data": {
        "id": "e773",
        "source": "1401_7625",
        "target": "2406_19617",
        "weight": 0.8022
      }
    },
    {
      "data": {
        "id": "e774",
        "source": "1401_7625",
        "target": "2502_04799",
        "weight": 0.7849
      }
    },
    {
      "data": {
        "id": "e775",
        "source": "1401_7625",
        "target": "2202_04612",
        "weight": 0.7802
      }
    },
    {
      "data": {
        "id": "e776",
        "source": "1401_7625",
        "target": "2101_04413",
        "weight": 0.8175
      }
    },
    {
      "data": {
        "id": "e777",
        "source": "1401_7625",
        "target": "2506_05454",
        "weight": 0.783
      }
    },
    {
      "data": {
        "id": "e778",
        "source": "1404_2334",
        "target": "2409_12266",
        "weight": 0.8087
      }
    },
    {
      "data": {
        "id": "e779",
        "source": "1404_2334",
        "target": "2009_10484",
        "weight": 0.8583
      }
    },
    {
      "data": {
        "id": "e780",
        "source": "1404_2334",
        "target": "2410_19414",
        "weight": 0.8486
      }
    },
    {
      "data": {
        "id": "e781",
        "source": "1404_2334",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.9287
      }
    },
    {
      "data": {
        "id": "e782",
        "source": "1404_2334",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.9176
      }
    },
    {
      "data": {
        "id": "e783",
        "source": "1404_2334",
        "target": "2411_15651",
        "weight": 0.8531
      }
    },
    {
      "data": {
        "id": "e784",
        "source": "1404_2334",
        "target": "2411_17293",
        "weight": 0.822
      }
    },
    {
      "data": {
        "id": "e785",
        "source": "1404_2334",
        "target": "2411_17902",
        "weight": 0.8452
      }
    },
    {
      "data": {
        "id": "e786",
        "source": "1404_2334",
        "target": "2412_11270",
        "weight": 0.8396
      }
    },
    {
      "data": {
        "id": "e787",
        "source": "1404_2334",
        "target": "2502_09556",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e788",
        "source": "1404_2334",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8095
      }
    },
    {
      "data": {
        "id": "e789",
        "source": "1404_2334",
        "target": "2503_06757",
        "weight": 0.8127
      }
    },
    {
      "data": {
        "id": "e790",
        "source": "1404_2334",
        "target": "1405_5848",
        "weight": 0.8954
      }
    },
    {
      "data": {
        "id": "e791",
        "source": "1404_2334",
        "target": "2201_03163",
        "weight": 0.8102
      }
    },
    {
      "data": {
        "id": "e792",
        "source": "1404_2334",
        "target": "1407_2896",
        "weight": 0.8409
      }
    },
    {
      "data": {
        "id": "e793",
        "source": "1404_2334",
        "target": "2503_16164",
        "weight": 0.916
      }
    },
    {
      "data": {
        "id": "e794",
        "source": "1404_2334",
        "target": "2203_01751",
        "weight": 0.8537
      }
    },
    {
      "data": {
        "id": "e795",
        "source": "1404_2334",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8256
      }
    },
    {
      "data": {
        "id": "e796",
        "source": "1404_2334",
        "target": "2203_02176",
        "weight": 0.8461
      }
    },
    {
      "data": {
        "id": "e797",
        "source": "1404_2334",
        "target": "1505_04098",
        "weight": 0.813
      }
    },
    {
      "data": {
        "id": "e798",
        "source": "1404_2334",
        "target": "2505_10542",
        "weight": 0.8381
      }
    },
    {
      "data": {
        "id": "e799",
        "source": "1404_2334",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.8788
      }
    },
    {
      "data": {
        "id": "e800",
        "source": "1404_2334",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.9085
      }
    },
    {
      "data": {
        "id": "e801",
        "source": "1404_2334",
        "target": "2015_palmieri_distance_metric_learning_for",
        "weight": 0.8095
      }
    },
    {
      "data": {
        "id": "e802",
        "source": "1404_2334",
        "target": "2508_21001",
        "weight": 0.8344
      }
    },
    {
      "data": {
        "id": "e803",
        "source": "1404_2334",
        "target": "2508_21800",
        "weight": 0.808
      }
    },
    {
      "data": {
        "id": "e804",
        "source": "1404_2334",
        "target": "2016_choudhury_regionally_accelerated_batch_informed",
        "weight": 0.8637
      }
    },
    {
      "data": {
        "id": "e805",
        "source": "1404_2334",
        "target": "2301_13143",
        "weight": 0.877
      }
    },
    {
      "data": {
        "id": "e806",
        "source": "1404_2334",
        "target": "2302_11670",
        "weight": 0.8373
      }
    },
    {
      "data": {
        "id": "e807",
        "source": "1404_2334",
        "target": "2510_21074",
        "weight": 0.8397
      }
    },
    {
      "data": {
        "id": "e808",
        "source": "1404_2334",
        "target": "2305_01072",
        "weight": 0.8046
      }
    },
    {
      "data": {
        "id": "e809",
        "source": "1404_2334",
        "target": "1708_06056",
        "weight": 0.8325
      }
    },
    {
      "data": {
        "id": "e810",
        "source": "1404_2334",
        "target": "1709_05448",
        "weight": 0.8171
      }
    },
    {
      "data": {
        "id": "e811",
        "source": "1404_2334",
        "target": "1709_07610",
        "weight": 0.8096
      }
    },
    {
      "data": {
        "id": "e812",
        "source": "1404_2334",
        "target": "1710_10122",
        "weight": 0.8562
      }
    },
    {
      "data": {
        "id": "e813",
        "source": "1404_2334",
        "target": "2309_14595",
        "weight": 0.9194
      }
    },
    {
      "data": {
        "id": "e814",
        "source": "1404_2334",
        "target": "2602_00992",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e815",
        "source": "1404_2334",
        "target": "1809_02399",
        "weight": 0.8768
      }
    },
    {
      "data": {
        "id": "e816",
        "source": "1404_2334",
        "target": "1809_07051",
        "weight": 0.8842
      }
    },
    {
      "data": {
        "id": "e817",
        "source": "1404_2334",
        "target": "1809_10252",
        "weight": 0.8111
      }
    },
    {
      "data": {
        "id": "e818",
        "source": "1404_2334",
        "target": "2603_06773",
        "weight": 0.8063
      }
    },
    {
      "data": {
        "id": "e819",
        "source": "1404_2334",
        "target": "2018_kingston_sampling_based_methods_for",
        "weight": 0.8012
      }
    },
    {
      "data": {
        "id": "e820",
        "source": "1404_2334",
        "target": "1909_09688",
        "weight": 0.8884
      }
    },
    {
      "data": {
        "id": "e821",
        "source": "1404_2334",
        "target": "2403_01194",
        "weight": 0.8224
      }
    },
    {
      "data": {
        "id": "e822",
        "source": "1404_2334",
        "target": "2403_10745",
        "weight": 0.8607
      }
    },
    {
      "data": {
        "id": "e823",
        "source": "1404_2334",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8094
      }
    },
    {
      "data": {
        "id": "e824",
        "source": "1405_5848",
        "target": "2409_12266",
        "weight": 0.8026
      }
    },
    {
      "data": {
        "id": "e825",
        "source": "1405_5848",
        "target": "2009_10484",
        "weight": 0.8315
      }
    },
    {
      "data": {
        "id": "e826",
        "source": "1405_5848",
        "target": "2604_14026",
        "weight": 0.8316
      }
    },
    {
      "data": {
        "id": "e827",
        "source": "1405_5848",
        "target": "2410_19414",
        "weight": 0.8481
      }
    },
    {
      "data": {
        "id": "e828",
        "source": "1405_5848",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8524
      }
    },
    {
      "data": {
        "id": "e829",
        "source": "1405_5848",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8233
      }
    },
    {
      "data": {
        "id": "e830",
        "source": "1405_5848",
        "target": "2411_15651",
        "weight": 0.8498
      }
    },
    {
      "data": {
        "id": "e831",
        "source": "1405_5848",
        "target": "2411_17902",
        "weight": 0.8615
      }
    },
    {
      "data": {
        "id": "e832",
        "source": "1405_5848",
        "target": "2412_11270",
        "weight": 0.8537
      }
    },
    {
      "data": {
        "id": "e833",
        "source": "1405_5848",
        "target": "2503_06757",
        "weight": 0.8133
      }
    },
    {
      "data": {
        "id": "e834",
        "source": "1405_5848",
        "target": "2503_16164",
        "weight": 0.8578
      }
    },
    {
      "data": {
        "id": "e835",
        "source": "1405_5848",
        "target": "1407_2896",
        "weight": 0.8314
      }
    },
    {
      "data": {
        "id": "e836",
        "source": "1405_5848",
        "target": "2203_01751",
        "weight": 0.8774
      }
    },
    {
      "data": {
        "id": "e837",
        "source": "1405_5848",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8198
      }
    },
    {
      "data": {
        "id": "e838",
        "source": "1405_5848",
        "target": "2505_10542",
        "weight": 0.8017
      }
    },
    {
      "data": {
        "id": "e839",
        "source": "1405_5848",
        "target": "2205_09991",
        "weight": 0.8021
      }
    },
    {
      "data": {
        "id": "e840",
        "source": "1405_5848",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.8353
      }
    },
    {
      "data": {
        "id": "e841",
        "source": "1405_5848",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8695
      }
    },
    {
      "data": {
        "id": "e842",
        "source": "1405_5848",
        "target": "2508_21001",
        "weight": 0.8496
      }
    },
    {
      "data": {
        "id": "e843",
        "source": "1405_5848",
        "target": "2508_21800",
        "weight": 0.8259
      }
    },
    {
      "data": {
        "id": "e844",
        "source": "1405_5848",
        "target": "2016_choudhury_regionally_accelerated_batch_informed",
        "weight": 0.8769
      }
    },
    {
      "data": {
        "id": "e845",
        "source": "1405_5848",
        "target": "2301_11902",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e846",
        "source": "1405_5848",
        "target": "2301_13143",
        "weight": 0.8279
      }
    },
    {
      "data": {
        "id": "e847",
        "source": "1405_5848",
        "target": "2302_11670",
        "weight": 0.8894
      }
    },
    {
      "data": {
        "id": "e848",
        "source": "1405_5848",
        "target": "1705_02403",
        "weight": 0.8088
      }
    },
    {
      "data": {
        "id": "e849",
        "source": "1405_5848",
        "target": "2510_21074",
        "weight": 0.8316
      }
    },
    {
      "data": {
        "id": "e850",
        "source": "1405_5848",
        "target": "2510_22015",
        "weight": 0.8073
      }
    },
    {
      "data": {
        "id": "e851",
        "source": "1405_5848",
        "target": "2305_01072",
        "weight": 0.8142
      }
    },
    {
      "data": {
        "id": "e852",
        "source": "1405_5848",
        "target": "1709_05448",
        "weight": 0.8231
      }
    },
    {
      "data": {
        "id": "e853",
        "source": "1405_5848",
        "target": "1709_07610",
        "weight": 0.8185
      }
    },
    {
      "data": {
        "id": "e854",
        "source": "1405_5848",
        "target": "1710_10122",
        "weight": 0.826
      }
    },
    {
      "data": {
        "id": "e855",
        "source": "1405_5848",
        "target": "2309_14545",
        "weight": 0.8123
      }
    },
    {
      "data": {
        "id": "e856",
        "source": "1405_5848",
        "target": "2309_14595",
        "weight": 0.8534
      }
    },
    {
      "data": {
        "id": "e857",
        "source": "1405_5848",
        "target": "2602_00992",
        "weight": 0.807
      }
    },
    {
      "data": {
        "id": "e858",
        "source": "1405_5848",
        "target": "2602_02846",
        "weight": 0.8189
      }
    },
    {
      "data": {
        "id": "e859",
        "source": "1405_5848",
        "target": "1809_02399",
        "weight": 0.8504
      }
    },
    {
      "data": {
        "id": "e860",
        "source": "1405_5848",
        "target": "1809_07051",
        "weight": 0.8498
      }
    },
    {
      "data": {
        "id": "e861",
        "source": "1405_5848",
        "target": "1809_10252",
        "weight": 0.8133
      }
    },
    {
      "data": {
        "id": "e862",
        "source": "1405_5848",
        "target": "2603_06773",
        "weight": 0.8069
      }
    },
    {
      "data": {
        "id": "e863",
        "source": "1405_5848",
        "target": "2603_12361",
        "weight": 0.8219
      }
    },
    {
      "data": {
        "id": "e864",
        "source": "1405_5848",
        "target": "1909_09688",
        "weight": 0.8271
      }
    },
    {
      "data": {
        "id": "e865",
        "source": "1405_5848",
        "target": "2403_10745",
        "weight": 0.8299
      }
    },
    {
      "data": {
        "id": "e866",
        "source": "1405_5848",
        "target": "2406_02807",
        "weight": 0.8278
      }
    },
    {
      "data": {
        "id": "e867",
        "source": "1406_1078",
        "target": "2410_13732",
        "weight": 0.7289
      }
    },
    {
      "data": {
        "id": "e868",
        "source": "1406_1078",
        "target": "1706_03762",
        "weight": 0.7503
      }
    },
    {
      "data": {
        "id": "e869",
        "source": "1406_1078",
        "target": "2202_07125",
        "weight": 0.706
      }
    },
    {
      "data": {
        "id": "e870",
        "source": "1406_1078",
        "target": "1711_06178",
        "weight": 0.6994
      }
    },
    {
      "data": {
        "id": "e871",
        "source": "1406_1078",
        "target": "2103_14438",
        "weight": 0.71
      }
    },
    {
      "data": {
        "id": "e872",
        "source": "1407_0414",
        "target": "2005_00985",
        "weight": 0.8127
      }
    },
    {
      "data": {
        "id": "e873",
        "source": "1407_0414",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8016
      }
    },
    {
      "data": {
        "id": "e874",
        "source": "1407_0414",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8241
      }
    },
    {
      "data": {
        "id": "e875",
        "source": "1407_0414",
        "target": "2410_23916",
        "weight": 0.815
      }
    },
    {
      "data": {
        "id": "e876",
        "source": "1407_0414",
        "target": "2307_03167",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e877",
        "source": "1407_0414",
        "target": "2506_14865",
        "weight": 0.8367
      }
    },
    {
      "data": {
        "id": "e878",
        "source": "1407_0414",
        "target": "2019_jackson_altro_a_fast_solver",
        "weight": 0.8296
      }
    },
    {
      "data": {
        "id": "e879",
        "source": "1407_0414",
        "target": "1711_11006",
        "weight": 0.8121
      }
    },
    {
      "data": {
        "id": "e880",
        "source": "1407_0414",
        "target": "2506_22087",
        "weight": 0.8228
      }
    },
    {
      "data": {
        "id": "e881",
        "source": "1407_2896",
        "target": "2004_08763",
        "weight": 0.808
      }
    },
    {
      "data": {
        "id": "e882",
        "source": "1407_2896",
        "target": "2409_06807",
        "weight": 0.8205
      }
    },
    {
      "data": {
        "id": "e883",
        "source": "1407_2896",
        "target": "2409_12266",
        "weight": 0.8376
      }
    },
    {
      "data": {
        "id": "e884",
        "source": "1407_2896",
        "target": "2009_10484",
        "weight": 0.8599
      }
    },
    {
      "data": {
        "id": "e885",
        "source": "1407_2896",
        "target": "2410_19414",
        "weight": 0.8456
      }
    },
    {
      "data": {
        "id": "e886",
        "source": "1407_2896",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8014
      }
    },
    {
      "data": {
        "id": "e887",
        "source": "1407_2896",
        "target": "2411_15651",
        "weight": 0.8194
      }
    },
    {
      "data": {
        "id": "e888",
        "source": "1407_2896",
        "target": "2411_17902",
        "weight": 0.8409
      }
    },
    {
      "data": {
        "id": "e889",
        "source": "1407_2896",
        "target": "2412_11270",
        "weight": 0.8236
      }
    },
    {
      "data": {
        "id": "e890",
        "source": "1407_2896",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8009
      }
    },
    {
      "data": {
        "id": "e891",
        "source": "1407_2896",
        "target": "2109_07081",
        "weight": 0.8103
      }
    },
    {
      "data": {
        "id": "e892",
        "source": "1407_2896",
        "target": "2503_05819",
        "weight": 0.8098
      }
    },
    {
      "data": {
        "id": "e893",
        "source": "1407_2896",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8693
      }
    },
    {
      "data": {
        "id": "e894",
        "source": "1407_2896",
        "target": "2503_16164",
        "weight": 0.8365
      }
    },
    {
      "data": {
        "id": "e895",
        "source": "1407_2896",
        "target": "1411_4045",
        "weight": 0.8416
      }
    },
    {
      "data": {
        "id": "e896",
        "source": "1407_2896",
        "target": "2203_01751",
        "weight": 0.8662
      }
    },
    {
      "data": {
        "id": "e897",
        "source": "1407_2896",
        "target": "2014_luo_an_empirical_study_of",
        "weight": 0.8462
      }
    },
    {
      "data": {
        "id": "e898",
        "source": "1407_2896",
        "target": "2504_18978",
        "weight": 0.8174
      }
    },
    {
      "data": {
        "id": "e899",
        "source": "1407_2896",
        "target": "1505_04098",
        "weight": 0.8707
      }
    },
    {
      "data": {
        "id": "e900",
        "source": "1407_2896",
        "target": "2505_10542",
        "weight": 0.8096
      }
    },
    {
      "data": {
        "id": "e901",
        "source": "1407_2896",
        "target": "2205_04422",
        "weight": 0.8278
      }
    },
    {
      "data": {
        "id": "e902",
        "source": "1407_2896",
        "target": "1511_05259",
        "weight": 0.8682
      }
    },
    {
      "data": {
        "id": "e903",
        "source": "1407_2896",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.8161
      }
    },
    {
      "data": {
        "id": "e904",
        "source": "1407_2896",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8354
      }
    },
    {
      "data": {
        "id": "e905",
        "source": "1407_2896",
        "target": "2210_01744",
        "weight": 0.8501
      }
    },
    {
      "data": {
        "id": "e906",
        "source": "1407_2896",
        "target": "2508_21001",
        "weight": 0.8646
      }
    },
    {
      "data": {
        "id": "e907",
        "source": "1407_2896",
        "target": "2508_21800",
        "weight": 0.8009
      }
    },
    {
      "data": {
        "id": "e908",
        "source": "1407_2896",
        "target": "2016_rajamaki_sampled_differential_dynamic_programming",
        "weight": 0.8279
      }
    },
    {
      "data": {
        "id": "e909",
        "source": "1407_2896",
        "target": "2301_13143",
        "weight": 0.8166
      }
    },
    {
      "data": {
        "id": "e910",
        "source": "1407_2896",
        "target": "2511_02015",
        "weight": 0.8113
      }
    },
    {
      "data": {
        "id": "e911",
        "source": "1407_2896",
        "target": "1709_05448",
        "weight": 0.8097
      }
    },
    {
      "data": {
        "id": "e912",
        "source": "1407_2896",
        "target": "1709_07610",
        "weight": 0.8152
      }
    },
    {
      "data": {
        "id": "e913",
        "source": "1407_2896",
        "target": "2307_03167",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e914",
        "source": "1407_2896",
        "target": "1710_10122",
        "weight": 0.8666
      }
    },
    {
      "data": {
        "id": "e915",
        "source": "1407_2896",
        "target": "2307_09105",
        "weight": 0.8042
      }
    },
    {
      "data": {
        "id": "e916",
        "source": "1407_2896",
        "target": "2309_14545",
        "weight": 0.8369
      }
    },
    {
      "data": {
        "id": "e917",
        "source": "1407_2896",
        "target": "2602_00992",
        "weight": 0.8242
      }
    },
    {
      "data": {
        "id": "e918",
        "source": "1407_2896",
        "target": "2602_02846",
        "weight": 0.8813
      }
    },
    {
      "data": {
        "id": "e919",
        "source": "1407_2896",
        "target": "2602_03639",
        "weight": 0.8095
      }
    },
    {
      "data": {
        "id": "e920",
        "source": "1407_2896",
        "target": "1809_02399",
        "weight": 0.8904
      }
    },
    {
      "data": {
        "id": "e921",
        "source": "1407_2896",
        "target": "1809_07051",
        "weight": 0.8463
      }
    },
    {
      "data": {
        "id": "e922",
        "source": "1407_2896",
        "target": "1809_10252",
        "weight": 0.8225
      }
    },
    {
      "data": {
        "id": "e923",
        "source": "1407_2896",
        "target": "2604_01614",
        "weight": 0.8012
      }
    },
    {
      "data": {
        "id": "e924",
        "source": "1407_2896",
        "target": "2603_06773",
        "weight": 0.8073
      }
    },
    {
      "data": {
        "id": "e925",
        "source": "1407_2896",
        "target": "2018_kingston_sampling_based_methods_for",
        "weight": 0.825
      }
    },
    {
      "data": {
        "id": "e926",
        "source": "1407_2896",
        "target": "2401_09241",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e927",
        "source": "1407_2896",
        "target": "2603_16059",
        "weight": 0.8645
      }
    },
    {
      "data": {
        "id": "e928",
        "source": "1407_2896",
        "target": "1903_00155",
        "weight": 0.8095
      }
    },
    {
      "data": {
        "id": "e929",
        "source": "1407_2896",
        "target": "1909_09688",
        "weight": 0.8451
      }
    },
    {
      "data": {
        "id": "e930",
        "source": "1407_2896",
        "target": "2603_24489",
        "weight": 0.8078
      }
    },
    {
      "data": {
        "id": "e931",
        "source": "1407_2896",
        "target": "2403_10745",
        "weight": 0.8495
      }
    },
    {
      "data": {
        "id": "e932",
        "source": "1407_2896",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8337
      }
    },
    {
      "data": {
        "id": "e933",
        "source": "1408_4408",
        "target": "2022_schmid_dynamic_mode_decomposition_and",
        "weight": 0.8254
      }
    },
    {
      "data": {
        "id": "e934",
        "source": "1408_4408",
        "target": "1707_01146",
        "weight": 0.9102
      }
    },
    {
      "data": {
        "id": "e935",
        "source": "1408_4408",
        "target": "1409_6358",
        "weight": 0.8413
      }
    },
    {
      "data": {
        "id": "e936",
        "source": "1408_4408",
        "target": "1909_10466",
        "weight": 0.8261
      }
    },
    {
      "data": {
        "id": "e937",
        "source": "1409_6358",
        "target": "2108_13404",
        "weight": 0.8276
      }
    },
    {
      "data": {
        "id": "e938",
        "source": "1409_6358",
        "target": "2022_schmid_dynamic_mode_decomposition_and",
        "weight": 0.8555
      }
    },
    {
      "data": {
        "id": "e939",
        "source": "1409_6358",
        "target": "1707_01146",
        "weight": 0.8025
      }
    },
    {
      "data": {
        "id": "e940",
        "source": "1409_6358",
        "target": "2511_00814",
        "weight": 0.8164
      }
    },
    {
      "data": {
        "id": "e941",
        "source": "1409_6358",
        "target": "2203_04955",
        "weight": 0.804
      }
    },
    {
      "data": {
        "id": "e942",
        "source": "1409_6358",
        "target": "1909_10466",
        "weight": 0.8664
      }
    },
    {
      "data": {
        "id": "e943",
        "source": "1409_6358",
        "target": "1711_05501",
        "weight": 0.8225
      }
    },
    {
      "data": {
        "id": "e944",
        "source": "1411_4045",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8111
      }
    },
    {
      "data": {
        "id": "e945",
        "source": "1411_4045",
        "target": "2503_06135",
        "weight": 0.8047
      }
    },
    {
      "data": {
        "id": "e946",
        "source": "1411_4045",
        "target": "2504_18978",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e947",
        "source": "1411_4045",
        "target": "1505_04098",
        "weight": 0.8295
      }
    },
    {
      "data": {
        "id": "e948",
        "source": "1411_4045",
        "target": "2205_04422",
        "weight": 0.8116
      }
    },
    {
      "data": {
        "id": "e949",
        "source": "1411_4045",
        "target": "1511_05259",
        "weight": 0.8083
      }
    },
    {
      "data": {
        "id": "e950",
        "source": "1411_4045",
        "target": "2508_21001",
        "weight": 0.8255
      }
    },
    {
      "data": {
        "id": "e951",
        "source": "1411_4045",
        "target": "1707_07239",
        "weight": 0.8419
      }
    },
    {
      "data": {
        "id": "e952",
        "source": "1411_4045",
        "target": "2305_01072",
        "weight": 0.8171
      }
    },
    {
      "data": {
        "id": "e953",
        "source": "1411_4045",
        "target": "1710_10122",
        "weight": 0.8038
      }
    },
    {
      "data": {
        "id": "e954",
        "source": "1411_4045",
        "target": "2602_02846",
        "weight": 0.8141
      }
    },
    {
      "data": {
        "id": "e955",
        "source": "1411_4045",
        "target": "1809_02399",
        "weight": 0.8222
      }
    },
    {
      "data": {
        "id": "e956",
        "source": "1411_4045",
        "target": "1809_07051",
        "weight": 0.8048
      }
    },
    {
      "data": {
        "id": "e957",
        "source": "1411_4045",
        "target": "2604_01614",
        "weight": 0.8073
      }
    },
    {
      "data": {
        "id": "e958",
        "source": "1411_4045",
        "target": "2603_16059",
        "weight": 0.847
      }
    },
    {
      "data": {
        "id": "e959",
        "source": "1411_4045",
        "target": "2403_10745",
        "weight": 0.8264
      }
    },
    {
      "data": {
        "id": "e960",
        "source": "2014_lefevre_a_survey_on_motion",
        "target": "2502_08664",
        "weight": 0.8654
      }
    },
    {
      "data": {
        "id": "e961",
        "source": "2014_lefevre_a_survey_on_motion",
        "target": "1604_07446",
        "weight": 0.815
      }
    },
    {
      "data": {
        "id": "e962",
        "source": "2014_lefevre_a_survey_on_motion",
        "target": "2503_03262",
        "weight": 0.8694
      }
    },
    {
      "data": {
        "id": "e963",
        "source": "2014_lefevre_a_survey_on_motion",
        "target": "2303_09824",
        "weight": 0.8361
      }
    },
    {
      "data": {
        "id": "e964",
        "source": "2014_lefevre_a_survey_on_motion",
        "target": "2018_schwarting_planning_and_decision_making",
        "weight": 0.8434
      }
    },
    {
      "data": {
        "id": "e965",
        "source": "2014_lefevre_a_survey_on_motion",
        "target": "2402_03893",
        "weight": 0.8133
      }
    },
    {
      "data": {
        "id": "e966",
        "source": "2014_lefevre_a_survey_on_motion",
        "target": "2505_09074",
        "weight": 0.8404
      }
    },
    {
      "data": {
        "id": "e967",
        "source": "2014_lefevre_a_survey_on_motion",
        "target": "1912_11676",
        "weight": 0.8274
      }
    },
    {
      "data": {
        "id": "e968",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2409_12266",
        "weight": 0.8249
      }
    },
    {
      "data": {
        "id": "e969",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2009_10484",
        "weight": 0.8821
      }
    },
    {
      "data": {
        "id": "e970",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2410_19414",
        "weight": 0.9044
      }
    },
    {
      "data": {
        "id": "e971",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.9077
      }
    },
    {
      "data": {
        "id": "e972",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2503_16164",
        "weight": 0.8126
      }
    },
    {
      "data": {
        "id": "e973",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2203_01751",
        "weight": 0.8503
      }
    },
    {
      "data": {
        "id": "e974",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2504_18978",
        "weight": 0.8138
      }
    },
    {
      "data": {
        "id": "e975",
        "source": "2014_luo_an_empirical_study_of",
        "target": "1505_04098",
        "weight": 0.8105
      }
    },
    {
      "data": {
        "id": "e976",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2204_09352",
        "weight": 0.8048
      }
    },
    {
      "data": {
        "id": "e977",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2205_04422",
        "weight": 0.826
      }
    },
    {
      "data": {
        "id": "e978",
        "source": "2014_luo_an_empirical_study_of",
        "target": "1511_05259",
        "weight": 0.8077
      }
    },
    {
      "data": {
        "id": "e979",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2015_klemm_rrt_star_connect_faster",
        "weight": 0.8056
      }
    },
    {
      "data": {
        "id": "e980",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8083
      }
    },
    {
      "data": {
        "id": "e981",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2508_05027",
        "weight": 0.8099
      }
    },
    {
      "data": {
        "id": "e982",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2508_21001",
        "weight": 0.822
      }
    },
    {
      "data": {
        "id": "e983",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2508_21800",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e984",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2016_rajamaki_sampled_differential_dynamic_programming",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e985",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2301_13143",
        "weight": 0.8127
      }
    },
    {
      "data": {
        "id": "e986",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2305_01072",
        "weight": 0.8104
      }
    },
    {
      "data": {
        "id": "e987",
        "source": "2014_luo_an_empirical_study_of",
        "target": "1709_05448",
        "weight": 0.8338
      }
    },
    {
      "data": {
        "id": "e988",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2307_03167",
        "weight": 0.8058
      }
    },
    {
      "data": {
        "id": "e989",
        "source": "2014_luo_an_empirical_study_of",
        "target": "1710_10122",
        "weight": 0.8086
      }
    },
    {
      "data": {
        "id": "e990",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2309_14545",
        "weight": 0.832
      }
    },
    {
      "data": {
        "id": "e991",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2602_00992",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e992",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2602_02846",
        "weight": 0.8076
      }
    },
    {
      "data": {
        "id": "e993",
        "source": "2014_luo_an_empirical_study_of",
        "target": "1809_02399",
        "weight": 0.854
      }
    },
    {
      "data": {
        "id": "e994",
        "source": "2014_luo_an_empirical_study_of",
        "target": "1809_10252",
        "weight": 0.819
      }
    },
    {
      "data": {
        "id": "e995",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2018_kingston_sampling_based_methods_for",
        "weight": 0.8401
      }
    },
    {
      "data": {
        "id": "e996",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2603_16059",
        "weight": 0.8128
      }
    },
    {
      "data": {
        "id": "e997",
        "source": "2014_luo_an_empirical_study_of",
        "target": "1909_09688",
        "weight": 0.8141
      }
    },
    {
      "data": {
        "id": "e998",
        "source": "2014_luo_an_empirical_study_of",
        "target": "2403_10745",
        "weight": 0.8251
      }
    },
    {
      "data": {
        "id": "e999",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2005_00985",
        "weight": 0.8579
      }
    },
    {
      "data": {
        "id": "e1000",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2409_11649",
        "weight": 0.8449
      }
    },
    {
      "data": {
        "id": "e1001",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2604_12149",
        "weight": 0.8178
      }
    },
    {
      "data": {
        "id": "e1002",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2010_00411",
        "weight": 0.8151
      }
    },
    {
      "data": {
        "id": "e1003",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2020_pellegrini_a_multiple_shooting_differential",
        "weight": 0.8124
      }
    },
    {
      "data": {
        "id": "e1004",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e1005",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2103_03293",
        "weight": 0.8104
      }
    },
    {
      "data": {
        "id": "e1006",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8156
      }
    },
    {
      "data": {
        "id": "e1007",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2109_07081",
        "weight": 0.8361
      }
    },
    {
      "data": {
        "id": "e1008",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2022_houghton_path_planning_differential_dynamic",
        "weight": 0.8166
      }
    },
    {
      "data": {
        "id": "e1009",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2203_04955",
        "weight": 0.8095
      }
    },
    {
      "data": {
        "id": "e1010",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2205_09991",
        "weight": 0.8195
      }
    },
    {
      "data": {
        "id": "e1011",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2208_02439",
        "weight": 0.8127
      }
    },
    {
      "data": {
        "id": "e1012",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2209_09006",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e1013",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8307
      }
    },
    {
      "data": {
        "id": "e1014",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2016_rajamaki_sampled_differential_dynamic_programming",
        "weight": 0.8614
      }
    },
    {
      "data": {
        "id": "e1015",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2305_09619",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e1016",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2307_03167",
        "weight": 0.818
      }
    },
    {
      "data": {
        "id": "e1017",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2511_11308",
        "weight": 0.8303
      }
    },
    {
      "data": {
        "id": "e1018",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2309_07872",
        "weight": 0.8165
      }
    },
    {
      "data": {
        "id": "e1019",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2309_12566",
        "weight": 0.8211
      }
    },
    {
      "data": {
        "id": "e1020",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2310_16828",
        "weight": 0.8087
      }
    },
    {
      "data": {
        "id": "e1021",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2024_wang_a_convergence_guaranteed_multiple",
        "weight": 0.8076
      }
    },
    {
      "data": {
        "id": "e1022",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "weight": 0.8551
      }
    },
    {
      "data": {
        "id": "e1023",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "1903_00155",
        "weight": 0.8113
      }
    },
    {
      "data": {
        "id": "e1024",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2603_24489",
        "weight": 0.8009
      }
    },
    {
      "data": {
        "id": "e1025",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2019_lefebvre_path_integral_policy_improvement",
        "weight": 0.8424
      }
    },
    {
      "data": {
        "id": "e1026",
        "source": "2014_pan_probabilistic_differential_dynamic_programming",
        "target": "2002_08809",
        "weight": 0.8326
      }
    },
    {
      "data": {
        "id": "e1027",
        "source": "1502_04269",
        "target": "2010_01412",
        "weight": 0.7121
      }
    },
    {
      "data": {
        "id": "e1028",
        "source": "1502_04269",
        "target": "2201_02177",
        "weight": 0.713
      }
    },
    {
      "data": {
        "id": "e1029",
        "source": "1502_04269",
        "target": "2308_00928",
        "weight": 0.7233
      }
    },
    {
      "data": {
        "id": "e1030",
        "source": "1502_04269",
        "target": "2506_05454",
        "weight": 0.7401
      }
    },
    {
      "data": {
        "id": "e1031",
        "source": "1502_04269",
        "target": "1711_06178",
        "weight": 0.7571
      }
    },
    {
      "data": {
        "id": "e1032",
        "source": "1502_05477",
        "target": "2310_16828",
        "weight": 0.8
      }
    },
    {
      "data": {
        "id": "e1033",
        "source": "1502_05477",
        "target": "1803_07055",
        "weight": 0.8099
      }
    },
    {
      "data": {
        "id": "e1034",
        "source": "1502_05477",
        "target": "2209_09006",
        "weight": 0.8064
      }
    },
    {
      "data": {
        "id": "e1035",
        "source": "1502_05477",
        "target": "2604_18578",
        "weight": 0.8424
      }
    },
    {
      "data": {
        "id": "e1036",
        "source": "1502_05477",
        "target": "2401_13662",
        "weight": 0.8227
      }
    },
    {
      "data": {
        "id": "e1037",
        "source": "1502_05477",
        "target": "1707_06347",
        "weight": 0.9172
      }
    },
    {
      "data": {
        "id": "e1038",
        "source": "1502_05477",
        "target": "2401_16025",
        "weight": 0.8692
      }
    },
    {
      "data": {
        "id": "e1039",
        "source": "1502_05477",
        "target": "1912_11912",
        "weight": 0.901
      }
    },
    {
      "data": {
        "id": "e1040",
        "source": "1503_05671",
        "target": "2502_04799",
        "weight": 0.7779
      }
    },
    {
      "data": {
        "id": "e1041",
        "source": "1503_05671",
        "target": "1806_06655",
        "weight": 0.7601
      }
    },
    {
      "data": {
        "id": "e1042",
        "source": "1503_05671",
        "target": "1810_02054",
        "weight": 0.7505
      }
    },
    {
      "data": {
        "id": "e1043",
        "source": "1503_05671",
        "target": "2506_05454",
        "weight": 0.7722
      }
    },
    {
      "data": {
        "id": "e1044",
        "source": "1503_05671",
        "target": "2601_06096",
        "weight": 0.7717
      }
    },
    {
      "data": {
        "id": "e1045",
        "source": "1505_04098",
        "target": "2009_10484",
        "weight": 0.8159
      }
    },
    {
      "data": {
        "id": "e1046",
        "source": "1505_04098",
        "target": "2411_15651",
        "weight": 0.8013
      }
    },
    {
      "data": {
        "id": "e1047",
        "source": "1505_04098",
        "target": "2412_11270",
        "weight": 0.8124
      }
    },
    {
      "data": {
        "id": "e1048",
        "source": "1505_04098",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8379
      }
    },
    {
      "data": {
        "id": "e1049",
        "source": "1505_04098",
        "target": "2503_16164",
        "weight": 0.8152
      }
    },
    {
      "data": {
        "id": "e1050",
        "source": "1505_04098",
        "target": "2203_01751",
        "weight": 0.8164
      }
    },
    {
      "data": {
        "id": "e1051",
        "source": "1505_04098",
        "target": "2505_10542",
        "weight": 0.8413
      }
    },
    {
      "data": {
        "id": "e1052",
        "source": "1505_04098",
        "target": "1511_05259",
        "weight": 0.8169
      }
    },
    {
      "data": {
        "id": "e1053",
        "source": "1505_04098",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.8051
      }
    },
    {
      "data": {
        "id": "e1054",
        "source": "1505_04098",
        "target": "2210_01744",
        "weight": 0.8096
      }
    },
    {
      "data": {
        "id": "e1055",
        "source": "1505_04098",
        "target": "2508_21001",
        "weight": 0.8232
      }
    },
    {
      "data": {
        "id": "e1056",
        "source": "1505_04098",
        "target": "1710_10122",
        "weight": 0.8368
      }
    },
    {
      "data": {
        "id": "e1057",
        "source": "1505_04098",
        "target": "2602_02846",
        "weight": 0.8273
      }
    },
    {
      "data": {
        "id": "e1058",
        "source": "1505_04098",
        "target": "1809_02399",
        "weight": 0.85
      }
    },
    {
      "data": {
        "id": "e1059",
        "source": "1505_04098",
        "target": "1809_07051",
        "weight": 0.8206
      }
    },
    {
      "data": {
        "id": "e1060",
        "source": "1505_04098",
        "target": "2603_16059",
        "weight": 0.8104
      }
    },
    {
      "data": {
        "id": "e1061",
        "source": "1505_04098",
        "target": "1909_09688",
        "weight": 0.8161
      }
    },
    {
      "data": {
        "id": "e1062",
        "source": "1505_04098",
        "target": "2403_10745",
        "weight": 0.8141
      }
    },
    {
      "data": {
        "id": "e1063",
        "source": "1505_04597",
        "target": "1810_12575",
        "weight": 0.7175
      }
    },
    {
      "data": {
        "id": "e1064",
        "source": "1505_04597",
        "target": "2010_11929",
        "weight": 0.7171
      }
    },
    {
      "data": {
        "id": "e1065",
        "source": "1505_04597",
        "target": "2011_14439",
        "weight": 0.728
      }
    },
    {
      "data": {
        "id": "e1066",
        "source": "1505_04597",
        "target": "2603_12361",
        "weight": 0.7059
      }
    },
    {
      "data": {
        "id": "e1067",
        "source": "1505_04597",
        "target": "2304_07193",
        "weight": 0.7147
      }
    },
    {
      "data": {
        "id": "e1068",
        "source": "1506_01085",
        "target": "1604_07446",
        "weight": 0.821
      }
    },
    {
      "data": {
        "id": "e1069",
        "source": "1506_01085",
        "target": "2604_01614",
        "weight": 0.8014
      }
    },
    {
      "data": {
        "id": "e1070",
        "source": "1506_01085",
        "target": "2201_03163",
        "weight": 0.8005
      }
    },
    {
      "data": {
        "id": "e1071",
        "source": "1506_01085",
        "target": "2018_zhang_toward_a_more_complete",
        "weight": 0.854
      }
    },
    {
      "data": {
        "id": "e1072",
        "source": "1506_01085",
        "target": "1903_00155",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e1073",
        "source": "1506_01085",
        "target": "2305_01072",
        "weight": 0.8106
      }
    },
    {
      "data": {
        "id": "e1074",
        "source": "1506_01085",
        "target": "2504_18978",
        "weight": 0.8678
      }
    },
    {
      "data": {
        "id": "e1075",
        "source": "1506_01085",
        "target": "1711_03449",
        "weight": 0.8188
      }
    },
    {
      "data": {
        "id": "e1076",
        "source": "1506_01085",
        "target": "2205_04422",
        "weight": 0.8643
      }
    },
    {
      "data": {
        "id": "e1077",
        "source": "1506_01085",
        "target": "2405_03281",
        "weight": 0.8299
      }
    },
    {
      "data": {
        "id": "e1078",
        "source": "1506_01085",
        "target": "2017_roesmann_kinodynamic_trajectory_optimization_and",
        "weight": 0.8486
      }
    },
    {
      "data": {
        "id": "e1079",
        "source": "1506_01085",
        "target": "1801_08995",
        "weight": 0.8177
      }
    },
    {
      "data": {
        "id": "e1080",
        "source": "1507_08752",
        "target": "2406_19617",
        "weight": 0.8724
      }
    },
    {
      "data": {
        "id": "e1081",
        "source": "1507_08752",
        "target": "2503_00385",
        "weight": 0.7752
      }
    },
    {
      "data": {
        "id": "e1082",
        "source": "1507_08752",
        "target": "2506_05454",
        "weight": 0.8047
      }
    },
    {
      "data": {
        "id": "e1083",
        "source": "1507_08752",
        "target": "2103_05478",
        "weight": 0.7997
      }
    },
    {
      "data": {
        "id": "e1084",
        "source": "1507_08752",
        "target": "2506_22087",
        "weight": 0.7946
      }
    },
    {
      "data": {
        "id": "e1085",
        "source": "1509_01149",
        "target": "2004_08763",
        "weight": 0.8084
      }
    },
    {
      "data": {
        "id": "e1086",
        "source": "1509_01149",
        "target": "2409_12266",
        "weight": 0.8082
      }
    },
    {
      "data": {
        "id": "e1087",
        "source": "1509_01149",
        "target": "2604_12149",
        "weight": 0.8296
      }
    },
    {
      "data": {
        "id": "e1088",
        "source": "1509_01149",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8389
      }
    },
    {
      "data": {
        "id": "e1089",
        "source": "1509_01149",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8563
      }
    },
    {
      "data": {
        "id": "e1090",
        "source": "1509_01149",
        "target": "2104_00241",
        "weight": 0.826
      }
    },
    {
      "data": {
        "id": "e1091",
        "source": "1509_01149",
        "target": "2503_05819",
        "weight": 0.8356
      }
    },
    {
      "data": {
        "id": "e1092",
        "source": "1509_01149",
        "target": "2022_houghton_path_planning_differential_dynamic",
        "weight": 0.8145
      }
    },
    {
      "data": {
        "id": "e1093",
        "source": "1509_01149",
        "target": "2503_11717",
        "weight": 0.8524
      }
    },
    {
      "data": {
        "id": "e1094",
        "source": "1509_01149",
        "target": "2203_04955",
        "weight": 0.8054
      }
    },
    {
      "data": {
        "id": "e1095",
        "source": "1509_01149",
        "target": "2506_21205",
        "weight": 0.8067
      }
    },
    {
      "data": {
        "id": "e1096",
        "source": "1509_01149",
        "target": "2212_02603",
        "weight": 0.8315
      }
    },
    {
      "data": {
        "id": "e1097",
        "source": "1509_01149",
        "target": "2016_rajamaki_sampled_differential_dynamic_programming",
        "weight": 0.8009
      }
    },
    {
      "data": {
        "id": "e1098",
        "source": "1509_01149",
        "target": "2301_13143",
        "weight": 0.8413
      }
    },
    {
      "data": {
        "id": "e1099",
        "source": "1509_01149",
        "target": "2511_02015",
        "weight": 0.8609
      }
    },
    {
      "data": {
        "id": "e1100",
        "source": "1509_01149",
        "target": "2511_11308",
        "weight": 0.8006
      }
    },
    {
      "data": {
        "id": "e1101",
        "source": "1509_01149",
        "target": "2307_09105",
        "weight": 0.8545
      }
    },
    {
      "data": {
        "id": "e1102",
        "source": "1509_01149",
        "target": "2309_12566",
        "weight": 0.8777
      }
    },
    {
      "data": {
        "id": "e1103",
        "source": "1509_01149",
        "target": "2017_williams_model_predictive_path_integral",
        "weight": 0.9505
      }
    },
    {
      "data": {
        "id": "e1104",
        "source": "1509_01149",
        "target": "2602_03639",
        "weight": 0.8732
      }
    },
    {
      "data": {
        "id": "e1105",
        "source": "1509_01149",
        "target": "2603_05385",
        "weight": 0.8397
      }
    },
    {
      "data": {
        "id": "e1106",
        "source": "1509_01149",
        "target": "2401_09241",
        "weight": 0.8736
      }
    },
    {
      "data": {
        "id": "e1107",
        "source": "1509_01149",
        "target": "2603_24489",
        "weight": 0.8891
      }
    },
    {
      "data": {
        "id": "e1108",
        "source": "1509_01149",
        "target": "2019_williams_model_predictive_path_integral",
        "weight": 0.8619
      }
    },
    {
      "data": {
        "id": "e1109",
        "source": "1509_03580",
        "target": "2108_13404",
        "weight": 0.8863
      }
    },
    {
      "data": {
        "id": "e1110",
        "source": "1509_03580",
        "target": "2111_08481",
        "weight": 0.8926
      }
    },
    {
      "data": {
        "id": "e1111",
        "source": "1509_03580",
        "target": "1707_01146",
        "weight": 0.8176
      }
    },
    {
      "data": {
        "id": "e1112",
        "source": "1509_03580",
        "target": "2412_12036",
        "weight": 0.8904
      }
    },
    {
      "data": {
        "id": "e1113",
        "source": "1509_03580",
        "target": "2403_09110",
        "weight": 0.8197
      }
    },
    {
      "data": {
        "id": "e1114",
        "source": "1509_03580",
        "target": "1711_05501",
        "weight": 0.893
      }
    },
    {
      "data": {
        "id": "e1115",
        "source": "1511_05259",
        "target": "2409_12266",
        "weight": 0.8234
      }
    },
    {
      "data": {
        "id": "e1116",
        "source": "1511_05259",
        "target": "2009_10484",
        "weight": 0.8008
      }
    },
    {
      "data": {
        "id": "e1117",
        "source": "1511_05259",
        "target": "2410_19414",
        "weight": 0.823
      }
    },
    {
      "data": {
        "id": "e1118",
        "source": "1511_05259",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8226
      }
    },
    {
      "data": {
        "id": "e1119",
        "source": "1511_05259",
        "target": "2203_01751",
        "weight": 0.8159
      }
    },
    {
      "data": {
        "id": "e1120",
        "source": "1511_05259",
        "target": "2205_04422",
        "weight": 0.8023
      }
    },
    {
      "data": {
        "id": "e1121",
        "source": "1511_05259",
        "target": "2210_01744",
        "weight": 0.8282
      }
    },
    {
      "data": {
        "id": "e1122",
        "source": "1511_05259",
        "target": "2508_21001",
        "weight": 0.8381
      }
    },
    {
      "data": {
        "id": "e1123",
        "source": "1511_05259",
        "target": "1710_10122",
        "weight": 0.8239
      }
    },
    {
      "data": {
        "id": "e1124",
        "source": "1511_05259",
        "target": "2602_02846",
        "weight": 0.8207
      }
    },
    {
      "data": {
        "id": "e1125",
        "source": "1511_05259",
        "target": "1809_02399",
        "weight": 0.8463
      }
    },
    {
      "data": {
        "id": "e1126",
        "source": "1511_05259",
        "target": "1809_07051",
        "weight": 0.8901
      }
    },
    {
      "data": {
        "id": "e1127",
        "source": "1511_05259",
        "target": "2603_16059",
        "weight": 0.833
      }
    },
    {
      "data": {
        "id": "e1128",
        "source": "1511_05259",
        "target": "1909_09688",
        "weight": 0.8115
      }
    },
    {
      "data": {
        "id": "e1129",
        "source": "1511_05259",
        "target": "2403_10745",
        "weight": 0.8231
      }
    },
    {
      "data": {
        "id": "e1130",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2009_10484",
        "weight": 0.8446
      }
    },
    {
      "data": {
        "id": "e1131",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2410_19414",
        "weight": 0.8211
      }
    },
    {
      "data": {
        "id": "e1132",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.9366
      }
    },
    {
      "data": {
        "id": "e1133",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2411_15651",
        "weight": 0.8203
      }
    },
    {
      "data": {
        "id": "e1134",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8499
      }
    },
    {
      "data": {
        "id": "e1135",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2411_17902",
        "weight": 0.8646
      }
    },
    {
      "data": {
        "id": "e1136",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2412_11270",
        "weight": 0.806
      }
    },
    {
      "data": {
        "id": "e1137",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2502_09556",
        "weight": 0.8117
      }
    },
    {
      "data": {
        "id": "e1138",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8135
      }
    },
    {
      "data": {
        "id": "e1139",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2503_06757",
        "weight": 0.8461
      }
    },
    {
      "data": {
        "id": "e1140",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2201_03163",
        "weight": 0.8119
      }
    },
    {
      "data": {
        "id": "e1141",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2503_16164",
        "weight": 0.8656
      }
    },
    {
      "data": {
        "id": "e1142",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2203_01751",
        "weight": 0.8208
      }
    },
    {
      "data": {
        "id": "e1143",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2203_02176",
        "weight": 0.8882
      }
    },
    {
      "data": {
        "id": "e1144",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2505_10542",
        "weight": 0.8968
      }
    },
    {
      "data": {
        "id": "e1145",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2015_otte_rrtx_asymptotically_optimal_single",
        "weight": 0.9128
      }
    },
    {
      "data": {
        "id": "e1146",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2015_palmieri_distance_metric_learning_for",
        "weight": 0.8128
      }
    },
    {
      "data": {
        "id": "e1147",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2508_21001",
        "weight": 0.8232
      }
    },
    {
      "data": {
        "id": "e1148",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2016_choudhury_regionally_accelerated_batch_informed",
        "weight": 0.8107
      }
    },
    {
      "data": {
        "id": "e1149",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2301_13143",
        "weight": 0.8223
      }
    },
    {
      "data": {
        "id": "e1150",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2302_11670",
        "weight": 0.8016
      }
    },
    {
      "data": {
        "id": "e1151",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2510_21074",
        "weight": 0.8277
      }
    },
    {
      "data": {
        "id": "e1152",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2305_01072",
        "weight": 0.8053
      }
    },
    {
      "data": {
        "id": "e1153",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "1708_06056",
        "weight": 0.8813
      }
    },
    {
      "data": {
        "id": "e1154",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "1709_07610",
        "weight": 0.8067
      }
    },
    {
      "data": {
        "id": "e1155",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "1710_10122",
        "weight": 0.8276
      }
    },
    {
      "data": {
        "id": "e1156",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2309_14595",
        "weight": 0.8447
      }
    },
    {
      "data": {
        "id": "e1157",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "1809_02399",
        "weight": 0.8487
      }
    },
    {
      "data": {
        "id": "e1158",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "1809_07051",
        "weight": 0.8329
      }
    },
    {
      "data": {
        "id": "e1159",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "1909_09688",
        "weight": 0.8974
      }
    },
    {
      "data": {
        "id": "e1160",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2403_01194",
        "weight": 0.8065
      }
    },
    {
      "data": {
        "id": "e1161",
        "source": "2015_klemm_rrt_star_connect_faster",
        "target": "2403_10745",
        "weight": 0.8471
      }
    },
    {
      "data": {
        "id": "e1162",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2409_12266",
        "weight": 0.8087
      }
    },
    {
      "data": {
        "id": "e1163",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2009_10484",
        "weight": 0.8523
      }
    },
    {
      "data": {
        "id": "e1164",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2410_19414",
        "weight": 0.8422
      }
    },
    {
      "data": {
        "id": "e1165",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.904
      }
    },
    {
      "data": {
        "id": "e1166",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2411_15651",
        "weight": 0.8406
      }
    },
    {
      "data": {
        "id": "e1167",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8645
      }
    },
    {
      "data": {
        "id": "e1168",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2411_17902",
        "weight": 0.8379
      }
    },
    {
      "data": {
        "id": "e1169",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2412_11270",
        "weight": 0.8119
      }
    },
    {
      "data": {
        "id": "e1170",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2502_09556",
        "weight": 0.8418
      }
    },
    {
      "data": {
        "id": "e1171",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8155
      }
    },
    {
      "data": {
        "id": "e1172",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2503_06757",
        "weight": 0.8244
      }
    },
    {
      "data": {
        "id": "e1173",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2503_16164",
        "weight": 0.8797
      }
    },
    {
      "data": {
        "id": "e1174",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2203_01751",
        "weight": 0.8341
      }
    },
    {
      "data": {
        "id": "e1175",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2203_02176",
        "weight": 0.8618
      }
    },
    {
      "data": {
        "id": "e1176",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2505_10542",
        "weight": 0.854
      }
    },
    {
      "data": {
        "id": "e1177",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2015_palmieri_distance_metric_learning_for",
        "weight": 0.8087
      }
    },
    {
      "data": {
        "id": "e1178",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2508_21001",
        "weight": 0.842
      }
    },
    {
      "data": {
        "id": "e1179",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2016_choudhury_regionally_accelerated_batch_informed",
        "weight": 0.8254
      }
    },
    {
      "data": {
        "id": "e1180",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2301_13143",
        "weight": 0.8491
      }
    },
    {
      "data": {
        "id": "e1181",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2302_11670",
        "weight": 0.8174
      }
    },
    {
      "data": {
        "id": "e1182",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2510_21074",
        "weight": 0.8826
      }
    },
    {
      "data": {
        "id": "e1183",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2305_01072",
        "weight": 0.8143
      }
    },
    {
      "data": {
        "id": "e1184",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "1708_06056",
        "weight": 0.8542
      }
    },
    {
      "data": {
        "id": "e1185",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "1710_10122",
        "weight": 0.8365
      }
    },
    {
      "data": {
        "id": "e1186",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2511_18170",
        "weight": 0.8061
      }
    },
    {
      "data": {
        "id": "e1187",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2309_14545",
        "weight": 0.8028
      }
    },
    {
      "data": {
        "id": "e1188",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2309_14595",
        "weight": 0.8521
      }
    },
    {
      "data": {
        "id": "e1189",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2602_02846",
        "weight": 0.8127
      }
    },
    {
      "data": {
        "id": "e1190",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "1809_02399",
        "weight": 0.8768
      }
    },
    {
      "data": {
        "id": "e1191",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "1809_07051",
        "weight": 0.855
      }
    },
    {
      "data": {
        "id": "e1192",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "1909_09688",
        "weight": 0.8925
      }
    },
    {
      "data": {
        "id": "e1193",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2403_01194",
        "weight": 0.8075
      }
    },
    {
      "data": {
        "id": "e1194",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2403_10745",
        "weight": 0.8536
      }
    },
    {
      "data": {
        "id": "e1195",
        "source": "2015_otte_rrtx_asymptotically_optimal_single",
        "target": "2406_02807",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e1196",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "2410_19414",
        "weight": 0.8007
      }
    },
    {
      "data": {
        "id": "e1197",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "2411_17293",
        "weight": 0.825
      }
    },
    {
      "data": {
        "id": "e1198",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8096
      }
    },
    {
      "data": {
        "id": "e1199",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8059
      }
    },
    {
      "data": {
        "id": "e1200",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "2503_06135",
        "weight": 0.8208
      }
    },
    {
      "data": {
        "id": "e1201",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "2203_02176",
        "weight": 0.8111
      }
    },
    {
      "data": {
        "id": "e1202",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "2505_09074",
        "weight": 0.803
      }
    },
    {
      "data": {
        "id": "e1203",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "2508_21001",
        "weight": 0.8267
      }
    },
    {
      "data": {
        "id": "e1204",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "2301_13143",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e1205",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "1709_07610",
        "weight": 0.8023
      }
    },
    {
      "data": {
        "id": "e1206",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "1710_10122",
        "weight": 0.8768
      }
    },
    {
      "data": {
        "id": "e1207",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "2309_14595",
        "weight": 0.8486
      }
    },
    {
      "data": {
        "id": "e1208",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "1809_02399",
        "weight": 0.8182
      }
    },
    {
      "data": {
        "id": "e1209",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "1809_07051",
        "weight": 0.8107
      }
    },
    {
      "data": {
        "id": "e1210",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "1907_01474",
        "weight": 0.8192
      }
    },
    {
      "data": {
        "id": "e1211",
        "source": "2015_palmieri_distance_metric_learning_for",
        "target": "2403_10745",
        "weight": 0.8223
      }
    },
    {
      "data": {
        "id": "e1212",
        "source": "1602_04915",
        "target": "2502_04799",
        "weight": 0.7645
      }
    },
    {
      "data": {
        "id": "e1213",
        "source": "1602_04915",
        "target": "1806_06655",
        "weight": 0.8411
      }
    },
    {
      "data": {
        "id": "e1214",
        "source": "1602_04915",
        "target": "2311_07411",
        "weight": 0.7726
      }
    },
    {
      "data": {
        "id": "e1215",
        "source": "1602_04915",
        "target": "1810_02054",
        "weight": 0.812
      }
    },
    {
      "data": {
        "id": "e1216",
        "source": "1602_04915",
        "target": "2103_00065",
        "weight": 0.796
      }
    },
    {
      "data": {
        "id": "e1217",
        "source": "1603_00943",
        "target": "1604_02639",
        "weight": 0.8284
      }
    },
    {
      "data": {
        "id": "e1218",
        "source": "1603_00943",
        "target": "2603_08824",
        "weight": 0.7459
      }
    },
    {
      "data": {
        "id": "e1219",
        "source": "1603_00943",
        "target": "2511_10622",
        "weight": 0.7546
      }
    },
    {
      "data": {
        "id": "e1220",
        "source": "1603_00943",
        "target": "2203_11419",
        "weight": 0.903
      }
    },
    {
      "data": {
        "id": "e1221",
        "source": "1603_00943",
        "target": "2506_11513",
        "weight": 0.8295
      }
    },
    {
      "data": {
        "id": "e1222",
        "source": "1604_02639",
        "target": "2005_00985",
        "weight": 0.7945
      }
    },
    {
      "data": {
        "id": "e1223",
        "source": "1604_02639",
        "target": "2511_10622",
        "weight": 0.8464
      }
    },
    {
      "data": {
        "id": "e1224",
        "source": "1604_02639",
        "target": "2511_10626",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e1225",
        "source": "1604_02639",
        "target": "2506_11513",
        "weight": 0.793
      }
    },
    {
      "data": {
        "id": "e1226",
        "source": "1604_07446",
        "target": "2502_08664",
        "weight": 0.8438
      }
    },
    {
      "data": {
        "id": "e1227",
        "source": "1604_07446",
        "target": "2409_09523",
        "weight": 0.8318
      }
    },
    {
      "data": {
        "id": "e1228",
        "source": "1604_07446",
        "target": "2503_03262",
        "weight": 0.8495
      }
    },
    {
      "data": {
        "id": "e1229",
        "source": "1604_07446",
        "target": "2303_09824",
        "weight": 0.8566
      }
    },
    {
      "data": {
        "id": "e1230",
        "source": "1604_07446",
        "target": "2201_03163",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e1231",
        "source": "1604_07446",
        "target": "2410_19414",
        "weight": 0.8082
      }
    },
    {
      "data": {
        "id": "e1232",
        "source": "1604_07446",
        "target": "2018_schwarting_planning_and_decision_making",
        "weight": 0.864
      }
    },
    {
      "data": {
        "id": "e1233",
        "source": "1604_07446",
        "target": "2018_zhang_toward_a_more_complete",
        "weight": 0.8232
      }
    },
    {
      "data": {
        "id": "e1234",
        "source": "1604_07446",
        "target": "2402_01443",
        "weight": 0.8151
      }
    },
    {
      "data": {
        "id": "e1235",
        "source": "1604_07446",
        "target": "2019_williams_model_predictive_path_integral",
        "weight": 0.8076
      }
    },
    {
      "data": {
        "id": "e1236",
        "source": "1604_07446",
        "target": "2505_09074",
        "weight": 0.8159
      }
    },
    {
      "data": {
        "id": "e1237",
        "source": "1604_07446",
        "target": "2204_07319",
        "weight": 0.8337
      }
    },
    {
      "data": {
        "id": "e1238",
        "source": "1604_07446",
        "target": "2206_03004",
        "weight": 0.8081
      }
    },
    {
      "data": {
        "id": "e1239",
        "source": "1604_07446",
        "target": "2017_roesmann_kinodynamic_trajectory_optimization_and",
        "weight": 0.8032
      }
    },
    {
      "data": {
        "id": "e1240",
        "source": "1606_05225",
        "target": "2604_06406",
        "weight": 0.7419
      }
    },
    {
      "data": {
        "id": "e1241",
        "source": "1606_05225",
        "target": "1806_06655",
        "weight": 0.7365
      }
    },
    {
      "data": {
        "id": "e1242",
        "source": "1606_05225",
        "target": "1909_09688",
        "weight": 0.7338
      }
    },
    {
      "data": {
        "id": "e1243",
        "source": "1606_05225",
        "target": "1709_07610",
        "weight": 0.7575
      }
    },
    {
      "data": {
        "id": "e1244",
        "source": "1612_05628",
        "target": "2508_07400",
        "weight": 0.7827
      }
    },
    {
      "data": {
        "id": "e1245",
        "source": "1612_05628",
        "target": "2311_07411",
        "weight": 0.7905
      }
    },
    {
      "data": {
        "id": "e1246",
        "source": "1612_05628",
        "target": "2202_00817",
        "weight": 0.7868
      }
    },
    {
      "data": {
        "id": "e1247",
        "source": "1612_05628",
        "target": "1707_06347",
        "weight": 0.7876
      }
    },
    {
      "data": {
        "id": "e1248",
        "source": "1612_05628",
        "target": "2604_01477",
        "weight": 0.7811
      }
    },
    {
      "data": {
        "id": "e1249",
        "source": "2016_choudhury_regionally_accelerated_batch_informed",
        "target": "2009_10484",
        "weight": 0.8203
      }
    },
    {
      "data": {
        "id": "e1250",
        "source": "2016_choudhury_regionally_accelerated_batch_informed",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8374
      }
    },
    {
      "data": {
        "id": "e1251",
        "source": "2016_choudhury_regionally_accelerated_batch_informed",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8109
      }
    },
    {
      "data": {
        "id": "e1252",
        "source": "2016_choudhury_regionally_accelerated_batch_informed",
        "target": "2411_17902",
        "weight": 0.831
      }
    },
    {
      "data": {
        "id": "e1253",
        "source": "2016_choudhury_regionally_accelerated_batch_informed",
        "target": "2503_16164",
        "weight": 0.8134
      }
    },
    {
      "data": {
        "id": "e1254",
        "source": "2016_choudhury_regionally_accelerated_batch_informed",
        "target": "2203_01751",
        "weight": 0.843
      }
    },
    {
      "data": {
        "id": "e1255",
        "source": "2016_choudhury_regionally_accelerated_batch_informed",
        "target": "2302_11670",
        "weight": 0.8528
      }
    },
    {
      "data": {
        "id": "e1256",
        "source": "2016_choudhury_regionally_accelerated_batch_informed",
        "target": "1708_06056",
        "weight": 0.8318
      }
    },
    {
      "data": {
        "id": "e1257",
        "source": "2016_choudhury_regionally_accelerated_batch_informed",
        "target": "2309_14595",
        "weight": 0.8016
      }
    },
    {
      "data": {
        "id": "e1258",
        "source": "2016_choudhury_regionally_accelerated_batch_informed",
        "target": "1809_02399",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e1259",
        "source": "2016_choudhury_regionally_accelerated_batch_informed",
        "target": "1909_09688",
        "weight": 0.8142
      }
    },
    {
      "data": {
        "id": "e1260",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2004_08763",
        "weight": 0.8366
      }
    },
    {
      "data": {
        "id": "e1261",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2005_00985",
        "weight": 0.8802
      }
    },
    {
      "data": {
        "id": "e1262",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2409_11649",
        "weight": 0.8599
      }
    },
    {
      "data": {
        "id": "e1263",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2409_12266",
        "weight": 0.8183
      }
    },
    {
      "data": {
        "id": "e1264",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2604_12149",
        "weight": 0.8055
      }
    },
    {
      "data": {
        "id": "e1265",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2409_15610",
        "weight": 0.8198
      }
    },
    {
      "data": {
        "id": "e1266",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2010_00411",
        "weight": 0.8675
      }
    },
    {
      "data": {
        "id": "e1267",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2410_19414",
        "weight": 0.8102
      }
    },
    {
      "data": {
        "id": "e1268",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2410_23916",
        "weight": 0.8051
      }
    },
    {
      "data": {
        "id": "e1269",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2020_marti_saumell_squash_box_feasibility_driven",
        "weight": 0.8402
      }
    },
    {
      "data": {
        "id": "e1270",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2020_pellegrini_a_multiple_shooting_differential",
        "weight": 0.8173
      }
    },
    {
      "data": {
        "id": "e1271",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2103_03293",
        "weight": 0.85
      }
    },
    {
      "data": {
        "id": "e1272",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8365
      }
    },
    {
      "data": {
        "id": "e1273",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8291
      }
    },
    {
      "data": {
        "id": "e1274",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8259
      }
    },
    {
      "data": {
        "id": "e1275",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2109_07081",
        "weight": 0.8648
      }
    },
    {
      "data": {
        "id": "e1276",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2503_05819",
        "weight": 0.8235
      }
    },
    {
      "data": {
        "id": "e1277",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.821
      }
    },
    {
      "data": {
        "id": "e1278",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2022_houghton_path_planning_differential_dynamic",
        "weight": 0.8439
      }
    },
    {
      "data": {
        "id": "e1279",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2503_11717",
        "weight": 0.8052
      }
    },
    {
      "data": {
        "id": "e1280",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2203_01751",
        "weight": 0.8061
      }
    },
    {
      "data": {
        "id": "e1281",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2204_02322",
        "weight": 0.8032
      }
    },
    {
      "data": {
        "id": "e1282",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2205_09991",
        "weight": 0.8111
      }
    },
    {
      "data": {
        "id": "e1283",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2208_02439",
        "weight": 0.8523
      }
    },
    {
      "data": {
        "id": "e1284",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2209_09006",
        "weight": 0.8008
      }
    },
    {
      "data": {
        "id": "e1285",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2212_00541",
        "weight": 0.8119
      }
    },
    {
      "data": {
        "id": "e1286",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2212_02603",
        "weight": 0.8173
      }
    },
    {
      "data": {
        "id": "e1287",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2508_21001",
        "weight": 0.8027
      }
    },
    {
      "data": {
        "id": "e1288",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8621
      }
    },
    {
      "data": {
        "id": "e1289",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2511_02015",
        "weight": 0.8307
      }
    },
    {
      "data": {
        "id": "e1290",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2307_03167",
        "weight": 0.8119
      }
    },
    {
      "data": {
        "id": "e1291",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2307_09105",
        "weight": 0.8189
      }
    },
    {
      "data": {
        "id": "e1292",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2511_11308",
        "weight": 0.8069
      }
    },
    {
      "data": {
        "id": "e1293",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2309_07872",
        "weight": 0.8582
      }
    },
    {
      "data": {
        "id": "e1294",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2309_12566",
        "weight": 0.8339
      }
    },
    {
      "data": {
        "id": "e1295",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2017_williams_model_predictive_path_integral",
        "weight": 0.8208
      }
    },
    {
      "data": {
        "id": "e1296",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2602_03639",
        "weight": 0.8228
      }
    },
    {
      "data": {
        "id": "e1297",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2311_06404",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e1298",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "1809_10252",
        "weight": 0.8035
      }
    },
    {
      "data": {
        "id": "e1299",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2603_05385",
        "weight": 0.8136
      }
    },
    {
      "data": {
        "id": "e1300",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8373
      }
    },
    {
      "data": {
        "id": "e1301",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2024_wang_a_convergence_guaranteed_multiple",
        "weight": 0.8385
      }
    },
    {
      "data": {
        "id": "e1302",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2401_09241",
        "weight": 0.8242
      }
    },
    {
      "data": {
        "id": "e1303",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "weight": 0.9167
      }
    },
    {
      "data": {
        "id": "e1304",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2603_16059",
        "weight": 0.8112
      }
    },
    {
      "data": {
        "id": "e1305",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "1903_00155",
        "weight": 0.8232
      }
    },
    {
      "data": {
        "id": "e1306",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2603_24489",
        "weight": 0.8305
      }
    },
    {
      "data": {
        "id": "e1307",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8114
      }
    },
    {
      "data": {
        "id": "e1308",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2019_lefebvre_path_integral_policy_improvement",
        "weight": 0.8547
      }
    },
    {
      "data": {
        "id": "e1309",
        "source": "2016_rajamaki_sampled_differential_dynamic_programming",
        "target": "2002_08809",
        "weight": 0.8236
      }
    },
    {
      "data": {
        "id": "e1310",
        "source": "1703_03864",
        "target": "1803_07055",
        "weight": 0.8168
      }
    },
    {
      "data": {
        "id": "e1311",
        "source": "1703_03864",
        "target": "2604_18578",
        "weight": 0.7759
      }
    },
    {
      "data": {
        "id": "e1312",
        "source": "1703_03864",
        "target": "1707_06347",
        "weight": 0.7714
      }
    },
    {
      "data": {
        "id": "e1313",
        "source": "1703_03864",
        "target": "2603_19968",
        "weight": 0.7669
      }
    },
    {
      "data": {
        "id": "e1314",
        "source": "1703_03864",
        "target": "2205_09991",
        "weight": 0.7793
      }
    },
    {
      "data": {
        "id": "e1315",
        "source": "1704_07911",
        "target": "2303_09824",
        "weight": 0.7937
      }
    },
    {
      "data": {
        "id": "e1316",
        "source": "1704_07911",
        "target": "2511_00088",
        "weight": 0.8036
      }
    },
    {
      "data": {
        "id": "e1317",
        "source": "1704_07911",
        "target": "2411_18714",
        "weight": 0.8443
      }
    },
    {
      "data": {
        "id": "e1318",
        "source": "1704_07911",
        "target": "1709_07174",
        "weight": 0.8223
      }
    },
    {
      "data": {
        "id": "e1319",
        "source": "1704_07911",
        "target": "1912_11676",
        "weight": 0.803
      }
    },
    {
      "data": {
        "id": "e1320",
        "source": "1705_02403",
        "target": "2310_17274",
        "weight": 0.8022
      }
    },
    {
      "data": {
        "id": "e1321",
        "source": "1705_02403",
        "target": "2409_06807",
        "weight": 0.8564
      }
    },
    {
      "data": {
        "id": "e1322",
        "source": "1705_02403",
        "target": "2502_09556",
        "weight": 0.8059
      }
    },
    {
      "data": {
        "id": "e1323",
        "source": "1705_02403",
        "target": "2602_02846",
        "weight": 0.8575
      }
    },
    {
      "data": {
        "id": "e1324",
        "source": "1705_02403",
        "target": "1809_02399",
        "weight": 0.8175
      }
    },
    {
      "data": {
        "id": "e1325",
        "source": "1705_02403",
        "target": "2503_06757",
        "weight": 0.8372
      }
    },
    {
      "data": {
        "id": "e1326",
        "source": "1705_02403",
        "target": "2410_16727",
        "weight": 0.8172
      }
    },
    {
      "data": {
        "id": "e1327",
        "source": "1705_02403",
        "target": "2603_10711",
        "weight": 0.8328
      }
    },
    {
      "data": {
        "id": "e1328",
        "source": "1705_02403",
        "target": "2411_11833",
        "weight": 0.8275
      }
    },
    {
      "data": {
        "id": "e1329",
        "source": "1705_02403",
        "target": "2505_06791",
        "weight": 0.8364
      }
    },
    {
      "data": {
        "id": "e1330",
        "source": "1705_02403",
        "target": "2309_14545",
        "weight": 0.8143
      }
    },
    {
      "data": {
        "id": "e1331",
        "source": "1706_03762",
        "target": "2410_13732",
        "weight": 0.8543
      }
    },
    {
      "data": {
        "id": "e1332",
        "source": "1706_03762",
        "target": "2010_11929",
        "weight": 0.8219
      }
    },
    {
      "data": {
        "id": "e1333",
        "source": "1706_03762",
        "target": "2207_05844",
        "weight": 0.7301
      }
    },
    {
      "data": {
        "id": "e1334",
        "source": "1706_03762",
        "target": "2406_16793",
        "weight": 0.7276
      }
    },
    {
      "data": {
        "id": "e1335",
        "source": "1707_01146",
        "target": "2603_05385",
        "weight": 0.8322
      }
    },
    {
      "data": {
        "id": "e1336",
        "source": "1707_01146",
        "target": "2011_11303",
        "weight": 0.805
      }
    },
    {
      "data": {
        "id": "e1337",
        "source": "1707_01146",
        "target": "2412_12036",
        "weight": 0.8147
      }
    },
    {
      "data": {
        "id": "e1338",
        "source": "1707_01146",
        "target": "1711_05501",
        "weight": 0.8274
      }
    },
    {
      "data": {
        "id": "e1339",
        "source": "1707_01146",
        "target": "2604_00900",
        "weight": 0.8053
      }
    },
    {
      "data": {
        "id": "e1340",
        "source": "1707_02342",
        "target": "2107_08086",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e1341",
        "source": "1707_02342",
        "target": "2212_02603",
        "weight": 0.8297
      }
    },
    {
      "data": {
        "id": "e1342",
        "source": "1707_02342",
        "target": "2401_09241",
        "weight": 0.8134
      }
    },
    {
      "data": {
        "id": "e1343",
        "source": "1707_02342",
        "target": "2603_24489",
        "weight": 0.8012
      }
    },
    {
      "data": {
        "id": "e1344",
        "source": "1707_02342",
        "target": "2511_11308",
        "weight": 0.8033
      }
    },
    {
      "data": {
        "id": "e1345",
        "source": "1707_02342",
        "target": "2309_12566",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e1346",
        "source": "1707_02342",
        "target": "2019_williams_model_predictive_path_integral",
        "weight": 0.8692
      }
    },
    {
      "data": {
        "id": "e1347",
        "source": "1707_02342",
        "target": "2017_williams_model_predictive_path_integral",
        "weight": 0.8395
      }
    },
    {
      "data": {
        "id": "e1348",
        "source": "1707_06347",
        "target": "2310_16828",
        "weight": 0.8062
      }
    },
    {
      "data": {
        "id": "e1349",
        "source": "1707_06347",
        "target": "1803_07055",
        "weight": 0.8209
      }
    },
    {
      "data": {
        "id": "e1350",
        "source": "1707_06347",
        "target": "2209_09006",
        "weight": 0.8202
      }
    },
    {
      "data": {
        "id": "e1351",
        "source": "1707_06347",
        "target": "2602_18933",
        "weight": 0.8038
      }
    },
    {
      "data": {
        "id": "e1352",
        "source": "1707_06347",
        "target": "2311_07411",
        "weight": 0.8122
      }
    },
    {
      "data": {
        "id": "e1353",
        "source": "1707_06347",
        "target": "2311_11166",
        "weight": 0.8035
      }
    },
    {
      "data": {
        "id": "e1354",
        "source": "1707_06347",
        "target": "2604_18578",
        "weight": 0.8951
      }
    },
    {
      "data": {
        "id": "e1355",
        "source": "1707_06347",
        "target": "2201_09104",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e1356",
        "source": "1707_06347",
        "target": "2401_13662",
        "weight": 0.8482
      }
    },
    {
      "data": {
        "id": "e1357",
        "source": "1707_06347",
        "target": "2401_16025",
        "weight": 0.9177
      }
    },
    {
      "data": {
        "id": "e1358",
        "source": "1707_06347",
        "target": "2511_02095",
        "weight": 0.8103
      }
    },
    {
      "data": {
        "id": "e1359",
        "source": "1707_06347",
        "target": "1912_11912",
        "weight": 0.8783
      }
    },
    {
      "data": {
        "id": "e1360",
        "source": "1707_06347",
        "target": "2604_04539",
        "weight": 0.8073
      }
    },
    {
      "data": {
        "id": "e1361",
        "source": "1707_07239",
        "target": "2504_18978",
        "weight": 0.8126
      }
    },
    {
      "data": {
        "id": "e1362",
        "source": "1707_07239",
        "target": "1711_03449",
        "weight": 0.8012
      }
    },
    {
      "data": {
        "id": "e1363",
        "source": "1708_06056",
        "target": "2009_10484",
        "weight": 0.8439
      }
    },
    {
      "data": {
        "id": "e1364",
        "source": "1708_06056",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8412
      }
    },
    {
      "data": {
        "id": "e1365",
        "source": "1708_06056",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8138
      }
    },
    {
      "data": {
        "id": "e1366",
        "source": "1708_06056",
        "target": "2411_17902",
        "weight": 0.822
      }
    },
    {
      "data": {
        "id": "e1367",
        "source": "1708_06056",
        "target": "2503_16164",
        "weight": 0.8419
      }
    },
    {
      "data": {
        "id": "e1368",
        "source": "1708_06056",
        "target": "2203_01751",
        "weight": 0.8224
      }
    },
    {
      "data": {
        "id": "e1369",
        "source": "1708_06056",
        "target": "2203_02176",
        "weight": 0.8179
      }
    },
    {
      "data": {
        "id": "e1370",
        "source": "1708_06056",
        "target": "2505_10542",
        "weight": 0.8546
      }
    },
    {
      "data": {
        "id": "e1371",
        "source": "1708_06056",
        "target": "2301_13143",
        "weight": 0.8032
      }
    },
    {
      "data": {
        "id": "e1372",
        "source": "1708_06056",
        "target": "2510_21074",
        "weight": 0.8437
      }
    },
    {
      "data": {
        "id": "e1373",
        "source": "1708_06056",
        "target": "2305_01072",
        "weight": 0.8068
      }
    },
    {
      "data": {
        "id": "e1374",
        "source": "1708_06056",
        "target": "1809_02399",
        "weight": 0.8071
      }
    },
    {
      "data": {
        "id": "e1375",
        "source": "1708_06056",
        "target": "1909_09688",
        "weight": 0.8412
      }
    },
    {
      "data": {
        "id": "e1376",
        "source": "1708_06056",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8025
      }
    },
    {
      "data": {
        "id": "e1377",
        "source": "1709_05401",
        "target": "2008_08835",
        "weight": 0.8176
      }
    },
    {
      "data": {
        "id": "e1378",
        "source": "1709_05401",
        "target": "2509_14978",
        "weight": 0.8346
      }
    },
    {
      "data": {
        "id": "e1379",
        "source": "1709_05401",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8062
      }
    },
    {
      "data": {
        "id": "e1380",
        "source": "1709_05401",
        "target": "2504_18978",
        "weight": 0.8036
      }
    },
    {
      "data": {
        "id": "e1381",
        "source": "1709_05401",
        "target": "2306_09852",
        "weight": 0.8048
      }
    },
    {
      "data": {
        "id": "e1382",
        "source": "1709_05401",
        "target": "2205_04422",
        "weight": 0.807
      }
    },
    {
      "data": {
        "id": "e1383",
        "source": "1709_05448",
        "target": "2409_12266",
        "weight": 0.8286
      }
    },
    {
      "data": {
        "id": "e1384",
        "source": "1709_05448",
        "target": "2009_10484",
        "weight": 0.8428
      }
    },
    {
      "data": {
        "id": "e1385",
        "source": "1709_05448",
        "target": "2409_16012",
        "weight": 0.8104
      }
    },
    {
      "data": {
        "id": "e1386",
        "source": "1709_05448",
        "target": "2604_14026",
        "weight": 0.8208
      }
    },
    {
      "data": {
        "id": "e1387",
        "source": "1709_05448",
        "target": "2410_19414",
        "weight": 0.8805
      }
    },
    {
      "data": {
        "id": "e1388",
        "source": "1709_05448",
        "target": "2411_17293",
        "weight": 0.8605
      }
    },
    {
      "data": {
        "id": "e1389",
        "source": "1709_05448",
        "target": "2503_05819",
        "weight": 0.8388
      }
    },
    {
      "data": {
        "id": "e1390",
        "source": "1709_05448",
        "target": "2503_06135",
        "weight": 0.8019
      }
    },
    {
      "data": {
        "id": "e1391",
        "source": "1709_05448",
        "target": "2203_01751",
        "weight": 0.829
      }
    },
    {
      "data": {
        "id": "e1392",
        "source": "1709_05448",
        "target": "2205_09991",
        "weight": 0.8434
      }
    },
    {
      "data": {
        "id": "e1393",
        "source": "1709_05448",
        "target": "2212_02603",
        "weight": 0.8318
      }
    },
    {
      "data": {
        "id": "e1394",
        "source": "1709_05448",
        "target": "2508_21001",
        "weight": 0.8118
      }
    },
    {
      "data": {
        "id": "e1395",
        "source": "1709_05448",
        "target": "2511_02015",
        "weight": 0.8059
      }
    },
    {
      "data": {
        "id": "e1396",
        "source": "1709_05448",
        "target": "2307_03167",
        "weight": 0.8098
      }
    },
    {
      "data": {
        "id": "e1397",
        "source": "1709_05448",
        "target": "1710_09483",
        "weight": 0.8135
      }
    },
    {
      "data": {
        "id": "e1398",
        "source": "1709_05448",
        "target": "2309_14545",
        "weight": 0.8163
      }
    },
    {
      "data": {
        "id": "e1399",
        "source": "1709_05448",
        "target": "2309_14595",
        "weight": 0.807
      }
    },
    {
      "data": {
        "id": "e1400",
        "source": "1709_05448",
        "target": "2602_00992",
        "weight": 0.8126
      }
    },
    {
      "data": {
        "id": "e1401",
        "source": "1709_05448",
        "target": "1809_02399",
        "weight": 0.8199
      }
    },
    {
      "data": {
        "id": "e1402",
        "source": "1709_05448",
        "target": "1809_10252",
        "weight": 0.8942
      }
    },
    {
      "data": {
        "id": "e1403",
        "source": "1709_05448",
        "target": "2024_calem_action_and_trajectory_prediction",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e1404",
        "source": "1709_05448",
        "target": "2603_06773",
        "weight": 0.8389
      }
    },
    {
      "data": {
        "id": "e1405",
        "source": "1709_05448",
        "target": "2018_kingston_sampling_based_methods_for",
        "weight": 0.8609
      }
    },
    {
      "data": {
        "id": "e1406",
        "source": "1709_05448",
        "target": "2401_09241",
        "weight": 0.8194
      }
    },
    {
      "data": {
        "id": "e1407",
        "source": "1709_07174",
        "target": "2407_15007",
        "weight": 0.8126
      }
    },
    {
      "data": {
        "id": "e1408",
        "source": "1709_07174",
        "target": "2604_07944",
        "weight": 0.8373
      }
    },
    {
      "data": {
        "id": "e1409",
        "source": "1709_07174",
        "target": "2409_09523",
        "weight": 0.8357
      }
    },
    {
      "data": {
        "id": "e1410",
        "source": "1709_07174",
        "target": "2604_08266",
        "weight": 0.8199
      }
    },
    {
      "data": {
        "id": "e1411",
        "source": "1709_07174",
        "target": "2411_18714",
        "weight": 0.8033
      }
    },
    {
      "data": {
        "id": "e1412",
        "source": "1709_07174",
        "target": "2412_14415",
        "weight": 0.8293
      }
    },
    {
      "data": {
        "id": "e1413",
        "source": "1709_07174",
        "target": "2025_hu_technically_speaking_transitioning_from",
        "weight": 0.8188
      }
    },
    {
      "data": {
        "id": "e1414",
        "source": "1709_07174",
        "target": "2111_12083",
        "weight": 0.8062
      }
    },
    {
      "data": {
        "id": "e1415",
        "source": "1709_07174",
        "target": "2111_12137",
        "weight": 0.8328
      }
    },
    {
      "data": {
        "id": "e1416",
        "source": "1709_07174",
        "target": "2505_09074",
        "weight": 0.8132
      }
    },
    {
      "data": {
        "id": "e1417",
        "source": "1709_07174",
        "target": "2206_03004",
        "weight": 0.8522
      }
    },
    {
      "data": {
        "id": "e1418",
        "source": "1709_07174",
        "target": "2212_06437",
        "weight": 0.8516
      }
    },
    {
      "data": {
        "id": "e1419",
        "source": "1709_07174",
        "target": "2301_11902",
        "weight": 0.8108
      }
    },
    {
      "data": {
        "id": "e1420",
        "source": "1709_07174",
        "target": "2303_09824",
        "weight": 0.859
      }
    },
    {
      "data": {
        "id": "e1421",
        "source": "1709_07174",
        "target": "2511_00088",
        "weight": 0.8595
      }
    },
    {
      "data": {
        "id": "e1422",
        "source": "1709_07174",
        "target": "2306_09852",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e1423",
        "source": "1709_07174",
        "target": "2310_08710",
        "weight": 0.8327
      }
    },
    {
      "data": {
        "id": "e1424",
        "source": "1709_07174",
        "target": "1912_11676",
        "weight": 0.804
      }
    },
    {
      "data": {
        "id": "e1425",
        "source": "1709_07174",
        "target": "2604_04539",
        "weight": 0.8045
      }
    },
    {
      "data": {
        "id": "e1426",
        "source": "1709_07610",
        "target": "2411_17902",
        "weight": 0.8206
      }
    },
    {
      "data": {
        "id": "e1427",
        "source": "1709_07610",
        "target": "2412_11270",
        "weight": 0.8153
      }
    },
    {
      "data": {
        "id": "e1428",
        "source": "1709_07610",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8188
      }
    },
    {
      "data": {
        "id": "e1429",
        "source": "1709_07610",
        "target": "2503_16164",
        "weight": 0.8178
      }
    },
    {
      "data": {
        "id": "e1430",
        "source": "1709_07610",
        "target": "2203_01751",
        "weight": 0.8186
      }
    },
    {
      "data": {
        "id": "e1431",
        "source": "1709_07610",
        "target": "2205_04422",
        "weight": 0.808
      }
    },
    {
      "data": {
        "id": "e1432",
        "source": "1709_07610",
        "target": "2508_21001",
        "weight": 0.8252
      }
    },
    {
      "data": {
        "id": "e1433",
        "source": "1709_07610",
        "target": "1710_10122",
        "weight": 0.8146
      }
    },
    {
      "data": {
        "id": "e1434",
        "source": "1709_07610",
        "target": "2602_00992",
        "weight": 0.844
      }
    },
    {
      "data": {
        "id": "e1435",
        "source": "1709_07610",
        "target": "2602_02846",
        "weight": 0.8026
      }
    },
    {
      "data": {
        "id": "e1436",
        "source": "1709_07610",
        "target": "1809_02399",
        "weight": 0.8131
      }
    },
    {
      "data": {
        "id": "e1437",
        "source": "1709_07610",
        "target": "1809_07051",
        "weight": 0.805
      }
    },
    {
      "data": {
        "id": "e1438",
        "source": "1709_07610",
        "target": "2604_01614",
        "weight": 0.8012
      }
    },
    {
      "data": {
        "id": "e1439",
        "source": "1709_07610",
        "target": "2403_10745",
        "weight": 0.8012
      }
    },
    {
      "data": {
        "id": "e1440",
        "source": "1709_07610",
        "target": "2406_02807",
        "weight": 0.833
      }
    },
    {
      "data": {
        "id": "e1441",
        "source": "1710_09483",
        "target": "2604_07944",
        "weight": 0.8317
      }
    },
    {
      "data": {
        "id": "e1442",
        "source": "1710_09483",
        "target": "2409_09523",
        "weight": 0.8009
      }
    },
    {
      "data": {
        "id": "e1443",
        "source": "1710_09483",
        "target": "2111_12137",
        "weight": 0.8154
      }
    },
    {
      "data": {
        "id": "e1444",
        "source": "1710_09483",
        "target": "2301_11902",
        "weight": 0.8391
      }
    },
    {
      "data": {
        "id": "e1445",
        "source": "1710_09483",
        "target": "2024_calem_action_and_trajectory_prediction",
        "weight": 0.823
      }
    },
    {
      "data": {
        "id": "e1446",
        "source": "1710_09483",
        "target": "2303_09824",
        "weight": 0.8026
      }
    },
    {
      "data": {
        "id": "e1447",
        "source": "1710_09483",
        "target": "2511_00088",
        "weight": 0.8193
      }
    },
    {
      "data": {
        "id": "e1448",
        "source": "1710_09483",
        "target": "2018_schwarting_planning_and_decision_making",
        "weight": 0.831
      }
    },
    {
      "data": {
        "id": "e1449",
        "source": "1710_09483",
        "target": "2505_09074",
        "weight": 0.8145
      }
    },
    {
      "data": {
        "id": "e1450",
        "source": "1710_09483",
        "target": "2412_14415",
        "weight": 0.8151
      }
    },
    {
      "data": {
        "id": "e1451",
        "source": "1710_09483",
        "target": "2205_09991",
        "weight": 0.8037
      }
    },
    {
      "data": {
        "id": "e1452",
        "source": "1710_09483",
        "target": "2001_03093",
        "weight": 0.8095
      }
    },
    {
      "data": {
        "id": "e1453",
        "source": "1710_10122",
        "target": "2004_08763",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e1454",
        "source": "1710_10122",
        "target": "2409_12266",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e1455",
        "source": "1710_10122",
        "target": "2410_19414",
        "weight": 0.8064
      }
    },
    {
      "data": {
        "id": "e1456",
        "source": "1710_10122",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8315
      }
    },
    {
      "data": {
        "id": "e1457",
        "source": "1710_10122",
        "target": "2411_15651",
        "weight": 0.8428
      }
    },
    {
      "data": {
        "id": "e1458",
        "source": "1710_10122",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8439
      }
    },
    {
      "data": {
        "id": "e1459",
        "source": "1710_10122",
        "target": "2411_17293",
        "weight": 0.8136
      }
    },
    {
      "data": {
        "id": "e1460",
        "source": "1710_10122",
        "target": "2411_17902",
        "weight": 0.8082
      }
    },
    {
      "data": {
        "id": "e1461",
        "source": "1710_10122",
        "target": "2412_11270",
        "weight": 0.8241
      }
    },
    {
      "data": {
        "id": "e1462",
        "source": "1710_10122",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8257
      }
    },
    {
      "data": {
        "id": "e1463",
        "source": "1710_10122",
        "target": "2503_06757",
        "weight": 0.8141
      }
    },
    {
      "data": {
        "id": "e1464",
        "source": "1710_10122",
        "target": "2503_16164",
        "weight": 0.8294
      }
    },
    {
      "data": {
        "id": "e1465",
        "source": "1710_10122",
        "target": "2203_01751",
        "weight": 0.8183
      }
    },
    {
      "data": {
        "id": "e1466",
        "source": "1710_10122",
        "target": "2203_02176",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e1467",
        "source": "1710_10122",
        "target": "2505_10542",
        "weight": 0.8135
      }
    },
    {
      "data": {
        "id": "e1468",
        "source": "1710_10122",
        "target": "2210_01744",
        "weight": 0.8564
      }
    },
    {
      "data": {
        "id": "e1469",
        "source": "1710_10122",
        "target": "2508_21001",
        "weight": 0.8707
      }
    },
    {
      "data": {
        "id": "e1470",
        "source": "1710_10122",
        "target": "2508_21800",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e1471",
        "source": "1710_10122",
        "target": "2301_13143",
        "weight": 0.8708
      }
    },
    {
      "data": {
        "id": "e1472",
        "source": "1710_10122",
        "target": "2309_14595",
        "weight": 0.845
      }
    },
    {
      "data": {
        "id": "e1473",
        "source": "1710_10122",
        "target": "2602_02846",
        "weight": 0.8109
      }
    },
    {
      "data": {
        "id": "e1474",
        "source": "1710_10122",
        "target": "1809_02399",
        "weight": 0.9096
      }
    },
    {
      "data": {
        "id": "e1475",
        "source": "1710_10122",
        "target": "1809_07051",
        "weight": 0.8791
      }
    },
    {
      "data": {
        "id": "e1476",
        "source": "1710_10122",
        "target": "2603_06773",
        "weight": 0.8118
      }
    },
    {
      "data": {
        "id": "e1477",
        "source": "1710_10122",
        "target": "2603_16059",
        "weight": 0.8116
      }
    },
    {
      "data": {
        "id": "e1478",
        "source": "1710_10122",
        "target": "1909_09688",
        "weight": 0.8251
      }
    },
    {
      "data": {
        "id": "e1479",
        "source": "1710_10122",
        "target": "2403_01194",
        "weight": 0.8152
      }
    },
    {
      "data": {
        "id": "e1480",
        "source": "1710_10122",
        "target": "2403_10745",
        "weight": 0.8943
      }
    },
    {
      "data": {
        "id": "e1481",
        "source": "1710_10122",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8338
      }
    },
    {
      "data": {
        "id": "e1482",
        "source": "1711_03449",
        "target": "2005_00985",
        "weight": 0.8009
      }
    },
    {
      "data": {
        "id": "e1483",
        "source": "1711_03449",
        "target": "2008_08835",
        "weight": 0.8006
      }
    },
    {
      "data": {
        "id": "e1484",
        "source": "1711_03449",
        "target": "2109_07081",
        "weight": 0.804
      }
    },
    {
      "data": {
        "id": "e1485",
        "source": "1711_03449",
        "target": "2504_06437",
        "weight": 0.8194
      }
    },
    {
      "data": {
        "id": "e1486",
        "source": "1711_03449",
        "target": "2504_18978",
        "weight": 0.8307
      }
    },
    {
      "data": {
        "id": "e1487",
        "source": "1711_03449",
        "target": "2204_09352",
        "weight": 0.9007
      }
    },
    {
      "data": {
        "id": "e1488",
        "source": "1711_03449",
        "target": "2205_04422",
        "weight": 0.8696
      }
    },
    {
      "data": {
        "id": "e1489",
        "source": "1711_03449",
        "target": "2506_14865",
        "weight": 0.8265
      }
    },
    {
      "data": {
        "id": "e1490",
        "source": "1711_03449",
        "target": "2207_06362",
        "weight": 0.8012
      }
    },
    {
      "data": {
        "id": "e1491",
        "source": "1711_03449",
        "target": "2208_02439",
        "weight": 0.8364
      }
    },
    {
      "data": {
        "id": "e1492",
        "source": "1711_03449",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8128
      }
    },
    {
      "data": {
        "id": "e1493",
        "source": "1711_03449",
        "target": "2508_21364",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e1494",
        "source": "1711_03449",
        "target": "2307_03167",
        "weight": 0.8032
      }
    },
    {
      "data": {
        "id": "e1495",
        "source": "1711_03449",
        "target": "2603_11335",
        "weight": 0.8199
      }
    },
    {
      "data": {
        "id": "e1496",
        "source": "1711_03449",
        "target": "2018_zhang_toward_a_more_complete",
        "weight": 0.829
      }
    },
    {
      "data": {
        "id": "e1497",
        "source": "1711_03449",
        "target": "2019_jackson_altro_a_fast_solver",
        "weight": 0.821
      }
    },
    {
      "data": {
        "id": "e1498",
        "source": "1711_05501",
        "target": "2011_11303",
        "weight": 0.818
      }
    },
    {
      "data": {
        "id": "e1499",
        "source": "1711_05501",
        "target": "2410_23916",
        "weight": 0.8129
      }
    },
    {
      "data": {
        "id": "e1500",
        "source": "1711_05501",
        "target": "2412_12036",
        "weight": 0.8872
      }
    },
    {
      "data": {
        "id": "e1501",
        "source": "1711_05501",
        "target": "2108_13404",
        "weight": 0.942
      }
    },
    {
      "data": {
        "id": "e1502",
        "source": "1711_05501",
        "target": "2111_08481",
        "weight": 0.8508
      }
    },
    {
      "data": {
        "id": "e1503",
        "source": "1711_05501",
        "target": "2203_04955",
        "weight": 0.836
      }
    },
    {
      "data": {
        "id": "e1504",
        "source": "1711_05501",
        "target": "2204_02322",
        "weight": 0.8025
      }
    },
    {
      "data": {
        "id": "e1505",
        "source": "1711_05501",
        "target": "2212_02603",
        "weight": 0.8447
      }
    },
    {
      "data": {
        "id": "e1506",
        "source": "1711_05501",
        "target": "2305_09619",
        "weight": 0.8155
      }
    },
    {
      "data": {
        "id": "e1507",
        "source": "1711_05501",
        "target": "2306_13867",
        "weight": 0.805
      }
    },
    {
      "data": {
        "id": "e1508",
        "source": "1711_05501",
        "target": "2511_11308",
        "weight": 0.8328
      }
    },
    {
      "data": {
        "id": "e1509",
        "source": "1711_05501",
        "target": "2310_02918",
        "weight": 0.8001
      }
    },
    {
      "data": {
        "id": "e1510",
        "source": "1711_05501",
        "target": "2602_03639",
        "weight": 0.8186
      }
    },
    {
      "data": {
        "id": "e1511",
        "source": "1711_05501",
        "target": "2312_02758",
        "weight": 0.8162
      }
    },
    {
      "data": {
        "id": "e1512",
        "source": "1711_05501",
        "target": "2603_23465",
        "weight": 0.8209
      }
    },
    {
      "data": {
        "id": "e1513",
        "source": "1711_05501",
        "target": "2603_24489",
        "weight": 0.8099
      }
    },
    {
      "data": {
        "id": "e1514",
        "source": "1711_05501",
        "target": "2604_00900",
        "weight": 0.8248
      }
    },
    {
      "data": {
        "id": "e1515",
        "source": "1711_05501",
        "target": "2403_09110",
        "weight": 0.8721
      }
    },
    {
      "data": {
        "id": "e1516",
        "source": "1711_06178",
        "target": "2201_02177",
        "weight": 0.752
      }
    },
    {
      "data": {
        "id": "e1517",
        "source": "1711_06178",
        "target": "2202_07125",
        "weight": 0.7495
      }
    },
    {
      "data": {
        "id": "e1518",
        "source": "1711_06178",
        "target": "1909_04939",
        "weight": 0.7513
      }
    },
    {
      "data": {
        "id": "e1519",
        "source": "1711_06178",
        "target": "2412_12036",
        "weight": 0.7502
      }
    },
    {
      "data": {
        "id": "e1520",
        "source": "1711_11006",
        "target": "2311_06404",
        "weight": 0.8
      }
    },
    {
      "data": {
        "id": "e1521",
        "source": "1711_11006",
        "target": "2409_11649",
        "weight": 0.8076
      }
    },
    {
      "data": {
        "id": "e1522",
        "source": "1711_11006",
        "target": "2309_07872",
        "weight": 0.8286
      }
    },
    {
      "data": {
        "id": "e1523",
        "source": "1711_11006",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8013
      }
    },
    {
      "data": {
        "id": "e1524",
        "source": "1711_11006",
        "target": "2304_00346",
        "weight": 0.8178
      }
    },
    {
      "data": {
        "id": "e1525",
        "source": "1711_11006",
        "target": "2305_09619",
        "weight": 0.8183
      }
    },
    {
      "data": {
        "id": "e1526",
        "source": "1711_11006",
        "target": "2020_pellegrini_a_multiple_shooting_differential",
        "weight": 0.8173
      }
    },
    {
      "data": {
        "id": "e1527",
        "source": "1711_11006",
        "target": "2403_00748",
        "weight": 0.8673
      }
    },
    {
      "data": {
        "id": "e1528",
        "source": "1711_11006",
        "target": "2511_02095",
        "weight": 0.8008
      }
    },
    {
      "data": {
        "id": "e1529",
        "source": "1711_11006",
        "target": "2204_02322",
        "weight": 0.8691
      }
    },
    {
      "data": {
        "id": "e1530",
        "source": "1711_11006",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8138
      }
    },
    {
      "data": {
        "id": "e1531",
        "source": "1711_11006",
        "target": "2019_jackson_altro_a_fast_solver",
        "weight": 0.8023
      }
    },
    {
      "data": {
        "id": "e1532",
        "source": "1711_11006",
        "target": "2207_06362",
        "weight": 0.8575
      }
    },
    {
      "data": {
        "id": "e1533",
        "source": "2017_roesmann_kinodynamic_trajectory_optimization_and",
        "target": "2205_04422",
        "weight": 0.8041
      }
    },
    {
      "data": {
        "id": "e1534",
        "source": "2017_roesmann_kinodynamic_trajectory_optimization_and",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.811
      }
    },
    {
      "data": {
        "id": "e1535",
        "source": "2017_roesmann_kinodynamic_trajectory_optimization_and",
        "target": "2504_18978",
        "weight": 0.8061
      }
    },
    {
      "data": {
        "id": "e1536",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2004_08763",
        "weight": 0.8069
      }
    },
    {
      "data": {
        "id": "e1537",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2409_12266",
        "weight": 0.8329
      }
    },
    {
      "data": {
        "id": "e1538",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2604_12149",
        "weight": 0.8263
      }
    },
    {
      "data": {
        "id": "e1539",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2409_15610",
        "weight": 0.8204
      }
    },
    {
      "data": {
        "id": "e1540",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2604_13312",
        "weight": 0.8069
      }
    },
    {
      "data": {
        "id": "e1541",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2410_23916",
        "weight": 0.8146
      }
    },
    {
      "data": {
        "id": "e1542",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2411_15651",
        "weight": 0.8062
      }
    },
    {
      "data": {
        "id": "e1543",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8686
      }
    },
    {
      "data": {
        "id": "e1544",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8746
      }
    },
    {
      "data": {
        "id": "e1545",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2025_trevisan_model_predictive_path_integral",
        "weight": 0.8375
      }
    },
    {
      "data": {
        "id": "e1546",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2104_00241",
        "weight": 0.8406
      }
    },
    {
      "data": {
        "id": "e1547",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2104_03186",
        "weight": 0.8002
      }
    },
    {
      "data": {
        "id": "e1548",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2503_05819",
        "weight": 0.8559
      }
    },
    {
      "data": {
        "id": "e1549",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2022_houghton_path_planning_differential_dynamic",
        "weight": 0.8569
      }
    },
    {
      "data": {
        "id": "e1550",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2503_11717",
        "weight": 0.8828
      }
    },
    {
      "data": {
        "id": "e1551",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2504_06437",
        "weight": 0.8354
      }
    },
    {
      "data": {
        "id": "e1552",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2505_05507",
        "weight": 0.8101
      }
    },
    {
      "data": {
        "id": "e1553",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2203_04955",
        "weight": 0.8196
      }
    },
    {
      "data": {
        "id": "e1554",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2205_09991",
        "weight": 0.8032
      }
    },
    {
      "data": {
        "id": "e1555",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2506_21205",
        "weight": 0.8334
      }
    },
    {
      "data": {
        "id": "e1556",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2208_02439",
        "weight": 0.8234
      }
    },
    {
      "data": {
        "id": "e1557",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2212_02603",
        "weight": 0.8417
      }
    },
    {
      "data": {
        "id": "e1558",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2508_21364",
        "weight": 0.8588
      }
    },
    {
      "data": {
        "id": "e1559",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2509_14978",
        "weight": 0.8163
      }
    },
    {
      "data": {
        "id": "e1560",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2301_13143",
        "weight": 0.8602
      }
    },
    {
      "data": {
        "id": "e1561",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2510_00272",
        "weight": 0.8342
      }
    },
    {
      "data": {
        "id": "e1562",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2511_02015",
        "weight": 0.8659
      }
    },
    {
      "data": {
        "id": "e1563",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2511_11308",
        "weight": 0.8212
      }
    },
    {
      "data": {
        "id": "e1564",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2307_09105",
        "weight": 0.8842
      }
    },
    {
      "data": {
        "id": "e1565",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2309_12566",
        "weight": 0.9116
      }
    },
    {
      "data": {
        "id": "e1566",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2602_03639",
        "weight": 0.8759
      }
    },
    {
      "data": {
        "id": "e1567",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2311_06404",
        "weight": 0.8
      }
    },
    {
      "data": {
        "id": "e1568",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2603_05385",
        "weight": 0.8657
      }
    },
    {
      "data": {
        "id": "e1569",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2603_10711",
        "weight": 0.8191
      }
    },
    {
      "data": {
        "id": "e1570",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2401_09241",
        "weight": 0.9003
      }
    },
    {
      "data": {
        "id": "e1571",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "1903_00155",
        "weight": 0.8062
      }
    },
    {
      "data": {
        "id": "e1572",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2603_24489",
        "weight": 0.9041
      }
    },
    {
      "data": {
        "id": "e1573",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2604_01477",
        "weight": 0.81
      }
    },
    {
      "data": {
        "id": "e1574",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2019_lefebvre_path_integral_policy_improvement",
        "weight": 0.811
      }
    },
    {
      "data": {
        "id": "e1575",
        "source": "2017_williams_model_predictive_path_integral",
        "target": "2019_williams_model_predictive_path_integral",
        "weight": 0.9369
      }
    },
    {
      "data": {
        "id": "e1576",
        "source": "1801_08995",
        "target": "2405_03281",
        "weight": 0.8157
      }
    },
    {
      "data": {
        "id": "e1577",
        "source": "1802_09767",
        "target": "2212_02603",
        "weight": 0.8173
      }
    },
    {
      "data": {
        "id": "e1578",
        "source": "1802_09767",
        "target": "2312_02758",
        "weight": 0.8477
      }
    },
    {
      "data": {
        "id": "e1579",
        "source": "1802_09767",
        "target": "1810_12584",
        "weight": 0.8617
      }
    },
    {
      "data": {
        "id": "e1580",
        "source": "1802_09767",
        "target": "2011_11303",
        "weight": 0.8236
      }
    },
    {
      "data": {
        "id": "e1581",
        "source": "1802_09767",
        "target": "2504_01766",
        "weight": 0.8226
      }
    },
    {
      "data": {
        "id": "e1582",
        "source": "1802_09767",
        "target": "2203_04955",
        "weight": 0.825
      }
    },
    {
      "data": {
        "id": "e1583",
        "source": "1802_09767",
        "target": "2603_23465",
        "weight": 0.8654
      }
    },
    {
      "data": {
        "id": "e1584",
        "source": "1802_09767",
        "target": "2203_15471",
        "weight": 0.871
      }
    },
    {
      "data": {
        "id": "e1585",
        "source": "1802_09767",
        "target": "2511_11308",
        "weight": 0.8057
      }
    },
    {
      "data": {
        "id": "e1586",
        "source": "1802_09767",
        "target": "2102_08302",
        "weight": 0.8985
      }
    },
    {
      "data": {
        "id": "e1587",
        "source": "1802_09767",
        "target": "2310_02918",
        "weight": 0.8023
      }
    },
    {
      "data": {
        "id": "e1588",
        "source": "1803_07055",
        "target": "1806_09460",
        "weight": 0.8131
      }
    },
    {
      "data": {
        "id": "e1589",
        "source": "1803_07055",
        "target": "2506_22087",
        "weight": 0.8312
      }
    },
    {
      "data": {
        "id": "e1590",
        "source": "1804_09893",
        "target": "2604_21270",
        "weight": 0.7351
      }
    },
    {
      "data": {
        "id": "e1591",
        "source": "1804_09893",
        "target": "2506_05454",
        "weight": 0.7318
      }
    },
    {
      "data": {
        "id": "e1592",
        "source": "1804_09893",
        "target": "2103_05478",
        "weight": 0.7301
      }
    },
    {
      "data": {
        "id": "e1593",
        "source": "1806_06655",
        "target": "2208_05888",
        "weight": 0.8128
      }
    },
    {
      "data": {
        "id": "e1594",
        "source": "1806_06655",
        "target": "2406_19617",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e1595",
        "source": "1806_06655",
        "target": "2502_04799",
        "weight": 0.8428
      }
    },
    {
      "data": {
        "id": "e1596",
        "source": "1806_06655",
        "target": "2311_07411",
        "weight": 0.8203
      }
    },
    {
      "data": {
        "id": "e1597",
        "source": "1806_06655",
        "target": "2503_00385",
        "weight": 0.8029
      }
    },
    {
      "data": {
        "id": "e1598",
        "source": "1806_06655",
        "target": "2311_11489",
        "weight": 0.8273
      }
    },
    {
      "data": {
        "id": "e1599",
        "source": "1806_06655",
        "target": "2112_02089",
        "weight": 0.8005
      }
    },
    {
      "data": {
        "id": "e1600",
        "source": "1806_06655",
        "target": "2410_04083",
        "weight": 0.8197
      }
    },
    {
      "data": {
        "id": "e1601",
        "source": "1806_06655",
        "target": "2511_10626",
        "weight": 0.8526
      }
    },
    {
      "data": {
        "id": "e1602",
        "source": "1806_06655",
        "target": "2204_02322",
        "weight": 0.8175
      }
    },
    {
      "data": {
        "id": "e1603",
        "source": "1806_06655",
        "target": "2506_05454",
        "weight": 0.8265
      }
    },
    {
      "data": {
        "id": "e1604",
        "source": "1806_06655",
        "target": "2511_14752",
        "weight": 0.8035
      }
    },
    {
      "data": {
        "id": "e1605",
        "source": "1806_09460",
        "target": "2604_10635",
        "weight": 0.8719
      }
    },
    {
      "data": {
        "id": "e1606",
        "source": "1806_09460",
        "target": "2604_24442",
        "weight": 0.8358
      }
    },
    {
      "data": {
        "id": "e1607",
        "source": "1806_09460",
        "target": "2502_12310",
        "weight": 0.809
      }
    },
    {
      "data": {
        "id": "e1608",
        "source": "1806_09460",
        "target": "2503_00385",
        "weight": 0.8382
      }
    },
    {
      "data": {
        "id": "e1609",
        "source": "1806_09460",
        "target": "2503_24371",
        "weight": 0.8449
      }
    },
    {
      "data": {
        "id": "e1610",
        "source": "1806_09460",
        "target": "2203_04955",
        "weight": 0.8093
      }
    },
    {
      "data": {
        "id": "e1611",
        "source": "1806_09460",
        "target": "2204_02322",
        "weight": 0.8306
      }
    },
    {
      "data": {
        "id": "e1612",
        "source": "1806_09460",
        "target": "2205_09991",
        "weight": 0.8256
      }
    },
    {
      "data": {
        "id": "e1613",
        "source": "1806_09460",
        "target": "2207_06362",
        "weight": 0.8076
      }
    },
    {
      "data": {
        "id": "e1614",
        "source": "1806_09460",
        "target": "2209_09006",
        "weight": 0.8213
      }
    },
    {
      "data": {
        "id": "e1615",
        "source": "1806_09460",
        "target": "2212_02603",
        "weight": 0.8352
      }
    },
    {
      "data": {
        "id": "e1616",
        "source": "1806_09460",
        "target": "2511_02095",
        "weight": 0.8782
      }
    },
    {
      "data": {
        "id": "e1617",
        "source": "1806_09460",
        "target": "2305_09619",
        "weight": 0.856
      }
    },
    {
      "data": {
        "id": "e1618",
        "source": "1806_09460",
        "target": "2306_09852",
        "weight": 0.8247
      }
    },
    {
      "data": {
        "id": "e1619",
        "source": "1806_09460",
        "target": "2511_11131",
        "weight": 0.8541
      }
    },
    {
      "data": {
        "id": "e1620",
        "source": "1806_09460",
        "target": "2511_11308",
        "weight": 0.8342
      }
    },
    {
      "data": {
        "id": "e1621",
        "source": "1806_09460",
        "target": "2309_12566",
        "weight": 0.8019
      }
    },
    {
      "data": {
        "id": "e1622",
        "source": "1806_09460",
        "target": "2310_16828",
        "weight": 0.8199
      }
    },
    {
      "data": {
        "id": "e1623",
        "source": "1806_09460",
        "target": "2602_18933",
        "weight": 0.8542
      }
    },
    {
      "data": {
        "id": "e1624",
        "source": "1806_09460",
        "target": "2311_11166",
        "weight": 0.8085
      }
    },
    {
      "data": {
        "id": "e1625",
        "source": "1806_09460",
        "target": "2311_18736",
        "weight": 0.8289
      }
    },
    {
      "data": {
        "id": "e1626",
        "source": "1806_09460",
        "target": "2401_13662",
        "weight": 0.842
      }
    },
    {
      "data": {
        "id": "e1627",
        "source": "1806_09460",
        "target": "2603_14197",
        "weight": 0.8307
      }
    },
    {
      "data": {
        "id": "e1628",
        "source": "1806_09460",
        "target": "2603_19968",
        "weight": 0.8462
      }
    },
    {
      "data": {
        "id": "e1629",
        "source": "1808_00177",
        "target": "2507_05331",
        "weight": 0.8459
      }
    },
    {
      "data": {
        "id": "e1630",
        "source": "1808_00177",
        "target": "2409_14562",
        "weight": 0.8852
      }
    },
    {
      "data": {
        "id": "e1631",
        "source": "1808_00177",
        "target": "2303_04137",
        "weight": 0.8237
      }
    },
    {
      "data": {
        "id": "e1632",
        "source": "1808_00177",
        "target": "2102_03861",
        "weight": 0.7949
      }
    },
    {
      "data": {
        "id": "e1633",
        "source": "1808_00177",
        "target": "2604_04539",
        "weight": 0.7973
      }
    },
    {
      "data": {
        "id": "e1634",
        "source": "1809_02399",
        "target": "2409_06807",
        "weight": 0.8437
      }
    },
    {
      "data": {
        "id": "e1635",
        "source": "1809_02399",
        "target": "2409_12266",
        "weight": 0.8517
      }
    },
    {
      "data": {
        "id": "e1636",
        "source": "1809_02399",
        "target": "2604_12149",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e1637",
        "source": "1809_02399",
        "target": "2009_10484",
        "weight": 0.8386
      }
    },
    {
      "data": {
        "id": "e1638",
        "source": "1809_02399",
        "target": "2410_19414",
        "weight": 0.8623
      }
    },
    {
      "data": {
        "id": "e1639",
        "source": "1809_02399",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8472
      }
    },
    {
      "data": {
        "id": "e1640",
        "source": "1809_02399",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8424
      }
    },
    {
      "data": {
        "id": "e1641",
        "source": "1809_02399",
        "target": "2411_15651",
        "weight": 0.8551
      }
    },
    {
      "data": {
        "id": "e1642",
        "source": "1809_02399",
        "target": "2411_17293",
        "weight": 0.8058
      }
    },
    {
      "data": {
        "id": "e1643",
        "source": "1809_02399",
        "target": "2411_17902",
        "weight": 0.8414
      }
    },
    {
      "data": {
        "id": "e1644",
        "source": "1809_02399",
        "target": "2412_11270",
        "weight": 0.8299
      }
    },
    {
      "data": {
        "id": "e1645",
        "source": "1809_02399",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8059
      }
    },
    {
      "data": {
        "id": "e1646",
        "source": "1809_02399",
        "target": "2502_09556",
        "weight": 0.8095
      }
    },
    {
      "data": {
        "id": "e1647",
        "source": "1809_02399",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8667
      }
    },
    {
      "data": {
        "id": "e1648",
        "source": "1809_02399",
        "target": "2503_05819",
        "weight": 0.8255
      }
    },
    {
      "data": {
        "id": "e1649",
        "source": "1809_02399",
        "target": "2503_06757",
        "weight": 0.8482
      }
    },
    {
      "data": {
        "id": "e1650",
        "source": "1809_02399",
        "target": "2503_16164",
        "weight": 0.8529
      }
    },
    {
      "data": {
        "id": "e1651",
        "source": "1809_02399",
        "target": "2203_01751",
        "weight": 0.8679
      }
    },
    {
      "data": {
        "id": "e1652",
        "source": "1809_02399",
        "target": "2203_02176",
        "weight": 0.8283
      }
    },
    {
      "data": {
        "id": "e1653",
        "source": "1809_02399",
        "target": "2504_18978",
        "weight": 0.805
      }
    },
    {
      "data": {
        "id": "e1654",
        "source": "1809_02399",
        "target": "2505_06791",
        "weight": 0.8026
      }
    },
    {
      "data": {
        "id": "e1655",
        "source": "1809_02399",
        "target": "2204_09352",
        "weight": 0.8133
      }
    },
    {
      "data": {
        "id": "e1656",
        "source": "1809_02399",
        "target": "2205_04422",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e1657",
        "source": "1809_02399",
        "target": "2505_10542",
        "weight": 0.8263
      }
    },
    {
      "data": {
        "id": "e1658",
        "source": "1809_02399",
        "target": "2210_01744",
        "weight": 0.8607
      }
    },
    {
      "data": {
        "id": "e1659",
        "source": "1809_02399",
        "target": "2508_21001",
        "weight": 0.8722
      }
    },
    {
      "data": {
        "id": "e1660",
        "source": "1809_02399",
        "target": "2301_13143",
        "weight": 0.8802
      }
    },
    {
      "data": {
        "id": "e1661",
        "source": "1809_02399",
        "target": "2305_01072",
        "weight": 0.8034
      }
    },
    {
      "data": {
        "id": "e1662",
        "source": "1809_02399",
        "target": "2307_09105",
        "weight": 0.8096
      }
    },
    {
      "data": {
        "id": "e1663",
        "source": "1809_02399",
        "target": "2309_14545",
        "weight": 0.8544
      }
    },
    {
      "data": {
        "id": "e1664",
        "source": "1809_02399",
        "target": "2309_14595",
        "weight": 0.8329
      }
    },
    {
      "data": {
        "id": "e1665",
        "source": "1809_02399",
        "target": "2602_00992",
        "weight": 0.8088
      }
    },
    {
      "data": {
        "id": "e1666",
        "source": "1809_02399",
        "target": "2602_02846",
        "weight": 0.872
      }
    },
    {
      "data": {
        "id": "e1667",
        "source": "1809_02399",
        "target": "1809_07051",
        "weight": 0.864
      }
    },
    {
      "data": {
        "id": "e1668",
        "source": "1809_02399",
        "target": "1809_10252",
        "weight": 0.8228
      }
    },
    {
      "data": {
        "id": "e1669",
        "source": "1809_02399",
        "target": "2603_06773",
        "weight": 0.8298
      }
    },
    {
      "data": {
        "id": "e1670",
        "source": "1809_02399",
        "target": "2018_kingston_sampling_based_methods_for",
        "weight": 0.8379
      }
    },
    {
      "data": {
        "id": "e1671",
        "source": "1809_02399",
        "target": "2603_16059",
        "weight": 0.8548
      }
    },
    {
      "data": {
        "id": "e1672",
        "source": "1809_02399",
        "target": "1909_09688",
        "weight": 0.8439
      }
    },
    {
      "data": {
        "id": "e1673",
        "source": "1809_02399",
        "target": "2403_01194",
        "weight": 0.817
      }
    },
    {
      "data": {
        "id": "e1674",
        "source": "1809_02399",
        "target": "2403_10745",
        "weight": 0.9214
      }
    },
    {
      "data": {
        "id": "e1675",
        "source": "1809_02399",
        "target": "2019_hannigan_sbp_guided_mpc_to",
        "weight": 0.8364
      }
    },
    {
      "data": {
        "id": "e1676",
        "source": "1809_02399",
        "target": "2406_02807",
        "weight": 0.8232
      }
    },
    {
      "data": {
        "id": "e1677",
        "source": "1809_07051",
        "target": "2009_10484",
        "weight": 0.808
      }
    },
    {
      "data": {
        "id": "e1678",
        "source": "1809_07051",
        "target": "2410_19414",
        "weight": 0.8152
      }
    },
    {
      "data": {
        "id": "e1679",
        "source": "1809_07051",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8357
      }
    },
    {
      "data": {
        "id": "e1680",
        "source": "1809_07051",
        "target": "2411_15651",
        "weight": 0.8368
      }
    },
    {
      "data": {
        "id": "e1681",
        "source": "1809_07051",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8501
      }
    },
    {
      "data": {
        "id": "e1682",
        "source": "1809_07051",
        "target": "2411_17902",
        "weight": 0.8028
      }
    },
    {
      "data": {
        "id": "e1683",
        "source": "1809_07051",
        "target": "2412_11270",
        "weight": 0.8366
      }
    },
    {
      "data": {
        "id": "e1684",
        "source": "1809_07051",
        "target": "2503_06757",
        "weight": 0.8079
      }
    },
    {
      "data": {
        "id": "e1685",
        "source": "1809_07051",
        "target": "2201_03163",
        "weight": 0.8139
      }
    },
    {
      "data": {
        "id": "e1686",
        "source": "1809_07051",
        "target": "2503_16164",
        "weight": 0.8569
      }
    },
    {
      "data": {
        "id": "e1687",
        "source": "1809_07051",
        "target": "2203_01751",
        "weight": 0.818
      }
    },
    {
      "data": {
        "id": "e1688",
        "source": "1809_07051",
        "target": "2203_02176",
        "weight": 0.8279
      }
    },
    {
      "data": {
        "id": "e1689",
        "source": "1809_07051",
        "target": "2505_10542",
        "weight": 0.8061
      }
    },
    {
      "data": {
        "id": "e1690",
        "source": "1809_07051",
        "target": "2210_01744",
        "weight": 0.8231
      }
    },
    {
      "data": {
        "id": "e1691",
        "source": "1809_07051",
        "target": "2508_21001",
        "weight": 0.8494
      }
    },
    {
      "data": {
        "id": "e1692",
        "source": "1809_07051",
        "target": "2301_13143",
        "weight": 0.8607
      }
    },
    {
      "data": {
        "id": "e1693",
        "source": "1809_07051",
        "target": "2309_14595",
        "weight": 0.8424
      }
    },
    {
      "data": {
        "id": "e1694",
        "source": "1809_07051",
        "target": "2604_01614",
        "weight": 0.8017
      }
    },
    {
      "data": {
        "id": "e1695",
        "source": "1809_07051",
        "target": "1909_09688",
        "weight": 0.8945
      }
    },
    {
      "data": {
        "id": "e1696",
        "source": "1809_07051",
        "target": "2403_01194",
        "weight": 0.8244
      }
    },
    {
      "data": {
        "id": "e1697",
        "source": "1809_07051",
        "target": "2403_10745",
        "weight": 0.8652
      }
    },
    {
      "data": {
        "id": "e1698",
        "source": "1809_10252",
        "target": "2409_12266",
        "weight": 0.8019
      }
    },
    {
      "data": {
        "id": "e1699",
        "source": "1809_10252",
        "target": "2009_10484",
        "weight": 0.8162
      }
    },
    {
      "data": {
        "id": "e1700",
        "source": "1809_10252",
        "target": "2409_16012",
        "weight": 0.8006
      }
    },
    {
      "data": {
        "id": "e1701",
        "source": "1809_10252",
        "target": "2604_14026",
        "weight": 0.814
      }
    },
    {
      "data": {
        "id": "e1702",
        "source": "1809_10252",
        "target": "2410_19414",
        "weight": 0.8787
      }
    },
    {
      "data": {
        "id": "e1703",
        "source": "1809_10252",
        "target": "2411_17293",
        "weight": 0.8529
      }
    },
    {
      "data": {
        "id": "e1704",
        "source": "1809_10252",
        "target": "2503_05819",
        "weight": 0.8269
      }
    },
    {
      "data": {
        "id": "e1705",
        "source": "1809_10252",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8036
      }
    },
    {
      "data": {
        "id": "e1706",
        "source": "1809_10252",
        "target": "2503_06135",
        "weight": 0.8037
      }
    },
    {
      "data": {
        "id": "e1707",
        "source": "1809_10252",
        "target": "2203_01751",
        "weight": 0.8382
      }
    },
    {
      "data": {
        "id": "e1708",
        "source": "1809_10252",
        "target": "2205_09991",
        "weight": 0.8111
      }
    },
    {
      "data": {
        "id": "e1709",
        "source": "1809_10252",
        "target": "2212_00541",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e1710",
        "source": "1809_10252",
        "target": "2212_02603",
        "weight": 0.8119
      }
    },
    {
      "data": {
        "id": "e1711",
        "source": "1809_10252",
        "target": "2508_21001",
        "weight": 0.8258
      }
    },
    {
      "data": {
        "id": "e1712",
        "source": "1809_10252",
        "target": "2309_14545",
        "weight": 0.849
      }
    },
    {
      "data": {
        "id": "e1713",
        "source": "1809_10252",
        "target": "2309_14595",
        "weight": 0.8219
      }
    },
    {
      "data": {
        "id": "e1714",
        "source": "1809_10252",
        "target": "2602_00992",
        "weight": 0.8096
      }
    },
    {
      "data": {
        "id": "e1715",
        "source": "1809_10252",
        "target": "2602_02846",
        "weight": 0.8101
      }
    },
    {
      "data": {
        "id": "e1716",
        "source": "1809_10252",
        "target": "2603_06773",
        "weight": 0.8461
      }
    },
    {
      "data": {
        "id": "e1717",
        "source": "1809_10252",
        "target": "2018_kingston_sampling_based_methods_for",
        "weight": 0.8209
      }
    },
    {
      "data": {
        "id": "e1718",
        "source": "1809_10252",
        "target": "2603_12361",
        "weight": 0.8303
      }
    },
    {
      "data": {
        "id": "e1719",
        "source": "1810_02054",
        "target": "2502_04799",
        "weight": 0.7864
      }
    },
    {
      "data": {
        "id": "e1720",
        "source": "1810_02054",
        "target": "2003_02218",
        "weight": 0.788
      }
    },
    {
      "data": {
        "id": "e1721",
        "source": "1810_02054",
        "target": "2103_00065",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e1722",
        "source": "1810_12575",
        "target": "2502_04799",
        "weight": 0.7295
      }
    },
    {
      "data": {
        "id": "e1723",
        "source": "1810_12575",
        "target": "2510_03745",
        "weight": 0.7382
      }
    },
    {
      "data": {
        "id": "e1724",
        "source": "1810_12575",
        "target": "2010_11929",
        "weight": 0.7361
      }
    },
    {
      "data": {
        "id": "e1725",
        "source": "1810_12575",
        "target": "2304_07193",
        "weight": 0.7287
      }
    },
    {
      "data": {
        "id": "e1726",
        "source": "1810_12584",
        "target": "2212_02603",
        "weight": 0.8427
      }
    },
    {
      "data": {
        "id": "e1727",
        "source": "1810_12584",
        "target": "2604_11183",
        "weight": 0.8023
      }
    },
    {
      "data": {
        "id": "e1728",
        "source": "1810_12584",
        "target": "2312_02758",
        "weight": 0.8291
      }
    },
    {
      "data": {
        "id": "e1729",
        "source": "1810_12584",
        "target": "2011_11303",
        "weight": 0.8771
      }
    },
    {
      "data": {
        "id": "e1730",
        "source": "1810_12584",
        "target": "2410_23916",
        "weight": 0.8034
      }
    },
    {
      "data": {
        "id": "e1731",
        "source": "1810_12584",
        "target": "2203_04955",
        "weight": 0.8175
      }
    },
    {
      "data": {
        "id": "e1732",
        "source": "1810_12584",
        "target": "2603_23465",
        "weight": 0.8036
      }
    },
    {
      "data": {
        "id": "e1733",
        "source": "1810_12584",
        "target": "2203_15471",
        "weight": 0.8203
      }
    },
    {
      "data": {
        "id": "e1734",
        "source": "1810_12584",
        "target": "2511_11308",
        "weight": 0.8159
      }
    },
    {
      "data": {
        "id": "e1735",
        "source": "1810_12584",
        "target": "2102_08302",
        "weight": 0.9016
      }
    },
    {
      "data": {
        "id": "e1736",
        "source": "1810_12584",
        "target": "2310_02918",
        "weight": 0.8213
      }
    },
    {
      "data": {
        "id": "e1737",
        "source": "1810_12584",
        "target": "2604_00900",
        "weight": 0.8107
      }
    },
    {
      "data": {
        "id": "e1738",
        "source": "1811_04551",
        "target": "2310_16828",
        "weight": 0.8217
      }
    },
    {
      "data": {
        "id": "e1739",
        "source": "1811_04551",
        "target": "2301_11902",
        "weight": 0.8056
      }
    },
    {
      "data": {
        "id": "e1740",
        "source": "1811_04551",
        "target": "2603_14392",
        "weight": 0.8021
      }
    },
    {
      "data": {
        "id": "e1741",
        "source": "1811_04551",
        "target": "2203_04955",
        "weight": 0.8026
      }
    },
    {
      "data": {
        "id": "e1742",
        "source": "1811_04551",
        "target": "1912_01603",
        "weight": 0.8199
      }
    },
    {
      "data": {
        "id": "e1743",
        "source": "1811_04551",
        "target": "2205_09991",
        "weight": 0.8284
      }
    },
    {
      "data": {
        "id": "e1744",
        "source": "2018_kingston_sampling_based_methods_for",
        "target": "2409_12266",
        "weight": 0.8195
      }
    },
    {
      "data": {
        "id": "e1745",
        "source": "2018_kingston_sampling_based_methods_for",
        "target": "2009_10484",
        "weight": 0.8656
      }
    },
    {
      "data": {
        "id": "e1746",
        "source": "2018_kingston_sampling_based_methods_for",
        "target": "2604_14026",
        "weight": 0.8154
      }
    },
    {
      "data": {
        "id": "e1747",
        "source": "2018_kingston_sampling_based_methods_for",
        "target": "2410_19414",
        "weight": 0.8992
      }
    },
    {
      "data": {
        "id": "e1748",
        "source": "2018_kingston_sampling_based_methods_for",
        "target": "2503_05819",
        "weight": 0.8041
      }
    },
    {
      "data": {
        "id": "e1749",
        "source": "2018_kingston_sampling_based_methods_for",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8149
      }
    },
    {
      "data": {
        "id": "e1750",
        "source": "2018_kingston_sampling_based_methods_for",
        "target": "2203_01751",
        "weight": 0.8232
      }
    },
    {
      "data": {
        "id": "e1751",
        "source": "2018_kingston_sampling_based_methods_for",
        "target": "2309_14545",
        "weight": 0.8272
      }
    },
    {
      "data": {
        "id": "e1752",
        "source": "2018_kingston_sampling_based_methods_for",
        "target": "2602_00992",
        "weight": 0.8044
      }
    },
    {
      "data": {
        "id": "e1753",
        "source": "2018_kingston_sampling_based_methods_for",
        "target": "2603_06773",
        "weight": 0.8081
      }
    },
    {
      "data": {
        "id": "e1754",
        "source": "2018_kingston_sampling_based_methods_for",
        "target": "2603_16059",
        "weight": 0.815
      }
    },
    {
      "data": {
        "id": "e1755",
        "source": "2018_kingston_sampling_based_methods_for",
        "target": "2403_10745",
        "weight": 0.8178
      }
    },
    {
      "data": {
        "id": "e1756",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2004_08763",
        "weight": 0.8052
      }
    },
    {
      "data": {
        "id": "e1757",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2005_00985",
        "weight": 0.8486
      }
    },
    {
      "data": {
        "id": "e1758",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2409_11649",
        "weight": 0.8459
      }
    },
    {
      "data": {
        "id": "e1759",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2010_00411",
        "weight": 0.8147
      }
    },
    {
      "data": {
        "id": "e1760",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2020_marti_saumell_squash_box_feasibility_driven",
        "weight": 0.802
      }
    },
    {
      "data": {
        "id": "e1761",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2020_pellegrini_a_multiple_shooting_differential",
        "weight": 0.8131
      }
    },
    {
      "data": {
        "id": "e1762",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2103_03293",
        "weight": 0.8073
      }
    },
    {
      "data": {
        "id": "e1763",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8307
      }
    },
    {
      "data": {
        "id": "e1764",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2109_07081",
        "weight": 0.8191
      }
    },
    {
      "data": {
        "id": "e1765",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2022_houghton_path_planning_differential_dynamic",
        "weight": 0.8093
      }
    },
    {
      "data": {
        "id": "e1766",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2204_02322",
        "weight": 0.8058
      }
    },
    {
      "data": {
        "id": "e1767",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8094
      }
    },
    {
      "data": {
        "id": "e1768",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2309_07872",
        "weight": 0.8332
      }
    },
    {
      "data": {
        "id": "e1769",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2602_03639",
        "weight": 0.8018
      }
    },
    {
      "data": {
        "id": "e1770",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2603_24489",
        "weight": 0.813
      }
    },
    {
      "data": {
        "id": "e1771",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2019_lefebvre_path_integral_policy_improvement",
        "weight": 0.8222
      }
    },
    {
      "data": {
        "id": "e1772",
        "source": "2018_rajamaki_regularizing_sampled_differential_dynamic",
        "target": "2002_08809",
        "weight": 0.8114
      }
    },
    {
      "data": {
        "id": "e1773",
        "source": "2018_schwarting_planning_and_decision_making",
        "target": "2502_08664",
        "weight": 0.853
      }
    },
    {
      "data": {
        "id": "e1774",
        "source": "2018_schwarting_planning_and_decision_making",
        "target": "2604_07944",
        "weight": 0.8002
      }
    },
    {
      "data": {
        "id": "e1775",
        "source": "2018_schwarting_planning_and_decision_making",
        "target": "2409_09523",
        "weight": 0.8284
      }
    },
    {
      "data": {
        "id": "e1776",
        "source": "2018_schwarting_planning_and_decision_making",
        "target": "2503_03262",
        "weight": 0.8375
      }
    },
    {
      "data": {
        "id": "e1777",
        "source": "2018_schwarting_planning_and_decision_making",
        "target": "2111_12137",
        "weight": 0.8148
      }
    },
    {
      "data": {
        "id": "e1778",
        "source": "2018_schwarting_planning_and_decision_making",
        "target": "2301_11902",
        "weight": 0.8306
      }
    },
    {
      "data": {
        "id": "e1779",
        "source": "2018_schwarting_planning_and_decision_making",
        "target": "2601_14880",
        "weight": 0.8524
      }
    },
    {
      "data": {
        "id": "e1780",
        "source": "2018_schwarting_planning_and_decision_making",
        "target": "2303_09824",
        "weight": 0.8607
      }
    },
    {
      "data": {
        "id": "e1781",
        "source": "2018_schwarting_planning_and_decision_making",
        "target": "2511_00088",
        "weight": 0.8084
      }
    },
    {
      "data": {
        "id": "e1782",
        "source": "2018_schwarting_planning_and_decision_making",
        "target": "2018_zhang_toward_a_more_complete",
        "weight": 0.8122
      }
    },
    {
      "data": {
        "id": "e1783",
        "source": "2018_schwarting_planning_and_decision_making",
        "target": "2412_14415",
        "weight": 0.8064
      }
    },
    {
      "data": {
        "id": "e1784",
        "source": "2018_schwarting_planning_and_decision_making",
        "target": "2206_03004",
        "weight": 0.8052
      }
    },
    {
      "data": {
        "id": "e1785",
        "source": "2018_schwarting_planning_and_decision_making",
        "target": "2505_09074",
        "weight": 0.8406
      }
    },
    {
      "data": {
        "id": "e1786",
        "source": "2018_schwarting_planning_and_decision_making",
        "target": "2310_08710",
        "weight": 0.8042
      }
    },
    {
      "data": {
        "id": "e1787",
        "source": "2018_zhang_toward_a_more_complete",
        "target": "2409_09523",
        "weight": 0.8193
      }
    },
    {
      "data": {
        "id": "e1788",
        "source": "2018_zhang_toward_a_more_complete",
        "target": "2205_04422",
        "weight": 0.8263
      }
    },
    {
      "data": {
        "id": "e1789",
        "source": "2018_zhang_toward_a_more_complete",
        "target": "2303_09824",
        "weight": 0.8097
      }
    },
    {
      "data": {
        "id": "e1790",
        "source": "2018_zhang_toward_a_more_complete",
        "target": "2402_01443",
        "weight": 0.8042
      }
    },
    {
      "data": {
        "id": "e1791",
        "source": "2018_zhang_toward_a_more_complete",
        "target": "2504_18978",
        "weight": 0.8237
      }
    },
    {
      "data": {
        "id": "e1792",
        "source": "2018_zhang_toward_a_more_complete",
        "target": "2402_03893",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e1793",
        "source": "1901_00491",
        "target": "2311_06404",
        "weight": 0.7804
      }
    },
    {
      "data": {
        "id": "e1794",
        "source": "1901_00491",
        "target": "2020_pellegrini_a_multiple_shooting_differential",
        "weight": 0.7656
      }
    },
    {
      "data": {
        "id": "e1795",
        "source": "1901_00491",
        "target": "2204_02322",
        "weight": 0.763
      }
    },
    {
      "data": {
        "id": "e1796",
        "source": "1903_00155",
        "target": "2005_00985",
        "weight": 0.8241
      }
    },
    {
      "data": {
        "id": "e1797",
        "source": "1903_00155",
        "target": "2409_11649",
        "weight": 0.8252
      }
    },
    {
      "data": {
        "id": "e1798",
        "source": "1903_00155",
        "target": "2409_12266",
        "weight": 0.8054
      }
    },
    {
      "data": {
        "id": "e1799",
        "source": "1903_00155",
        "target": "2604_12149",
        "weight": 0.8343
      }
    },
    {
      "data": {
        "id": "e1800",
        "source": "1903_00155",
        "target": "2410_23916",
        "weight": 0.8252
      }
    },
    {
      "data": {
        "id": "e1801",
        "source": "1903_00155",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8149
      }
    },
    {
      "data": {
        "id": "e1802",
        "source": "1903_00155",
        "target": "2109_07081",
        "weight": 0.8529
      }
    },
    {
      "data": {
        "id": "e1803",
        "source": "1903_00155",
        "target": "2503_05819",
        "weight": 0.8017
      }
    },
    {
      "data": {
        "id": "e1804",
        "source": "1903_00155",
        "target": "2504_06437",
        "weight": 0.8069
      }
    },
    {
      "data": {
        "id": "e1805",
        "source": "1903_00155",
        "target": "2203_01751",
        "weight": 0.8155
      }
    },
    {
      "data": {
        "id": "e1806",
        "source": "1903_00155",
        "target": "2504_18978",
        "weight": 0.8306
      }
    },
    {
      "data": {
        "id": "e1807",
        "source": "1903_00155",
        "target": "2204_02322",
        "weight": 0.8113
      }
    },
    {
      "data": {
        "id": "e1808",
        "source": "1903_00155",
        "target": "2205_04422",
        "weight": 0.8233
      }
    },
    {
      "data": {
        "id": "e1809",
        "source": "1903_00155",
        "target": "2205_09991",
        "weight": 0.8124
      }
    },
    {
      "data": {
        "id": "e1810",
        "source": "1903_00155",
        "target": "2207_06362",
        "weight": 0.8098
      }
    },
    {
      "data": {
        "id": "e1811",
        "source": "1903_00155",
        "target": "2506_22087",
        "weight": 0.8247
      }
    },
    {
      "data": {
        "id": "e1812",
        "source": "1903_00155",
        "target": "2209_09006",
        "weight": 0.8001
      }
    },
    {
      "data": {
        "id": "e1813",
        "source": "1903_00155",
        "target": "2212_02603",
        "weight": 0.8083
      }
    },
    {
      "data": {
        "id": "e1814",
        "source": "1903_00155",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.832
      }
    },
    {
      "data": {
        "id": "e1815",
        "source": "1903_00155",
        "target": "2303_16746",
        "weight": 0.8342
      }
    },
    {
      "data": {
        "id": "e1816",
        "source": "1903_00155",
        "target": "2511_10622",
        "weight": 0.8334
      }
    },
    {
      "data": {
        "id": "e1817",
        "source": "1903_00155",
        "target": "2307_03167",
        "weight": 0.8499
      }
    },
    {
      "data": {
        "id": "e1818",
        "source": "1903_00155",
        "target": "2511_11308",
        "weight": 0.8182
      }
    },
    {
      "data": {
        "id": "e1819",
        "source": "1903_00155",
        "target": "2511_14752",
        "weight": 0.85
      }
    },
    {
      "data": {
        "id": "e1820",
        "source": "1903_00155",
        "target": "2511_18170",
        "weight": 0.8018
      }
    },
    {
      "data": {
        "id": "e1821",
        "source": "1903_00155",
        "target": "2309_12566",
        "weight": 0.8403
      }
    },
    {
      "data": {
        "id": "e1822",
        "source": "1903_00155",
        "target": "2602_03639",
        "weight": 0.8114
      }
    },
    {
      "data": {
        "id": "e1823",
        "source": "1903_00155",
        "target": "2311_06404",
        "weight": 0.8175
      }
    },
    {
      "data": {
        "id": "e1824",
        "source": "1903_00155",
        "target": "2602_19699",
        "weight": 0.8042
      }
    },
    {
      "data": {
        "id": "e1825",
        "source": "1903_00155",
        "target": "2603_00871",
        "weight": 0.8358
      }
    },
    {
      "data": {
        "id": "e1826",
        "source": "1903_00155",
        "target": "2603_04843",
        "weight": 0.8067
      }
    },
    {
      "data": {
        "id": "e1827",
        "source": "1903_00155",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8223
      }
    },
    {
      "data": {
        "id": "e1828",
        "source": "1903_00155",
        "target": "2603_10711",
        "weight": 0.8294
      }
    },
    {
      "data": {
        "id": "e1829",
        "source": "1903_00155",
        "target": "2401_09241",
        "weight": 0.8059
      }
    },
    {
      "data": {
        "id": "e1830",
        "source": "1903_00155",
        "target": "2603_11335",
        "weight": 0.8209
      }
    },
    {
      "data": {
        "id": "e1831",
        "source": "1903_00155",
        "target": "2603_24489",
        "weight": 0.8382
      }
    },
    {
      "data": {
        "id": "e1832",
        "source": "1903_00155",
        "target": "2604_01477",
        "weight": 0.8062
      }
    },
    {
      "data": {
        "id": "e1833",
        "source": "1903_00155",
        "target": "2019_jackson_altro_a_fast_solver",
        "weight": 0.8445
      }
    },
    {
      "data": {
        "id": "e1834",
        "source": "1903_00155",
        "target": "2406_05846",
        "weight": 0.8099
      }
    },
    {
      "data": {
        "id": "e1835",
        "source": "1907_01474",
        "target": "2503_06135",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e1836",
        "source": "1907_01474",
        "target": "2411_02158",
        "weight": 0.7979
      }
    },
    {
      "data": {
        "id": "e1837",
        "source": "1907_01474",
        "target": "2505_05588",
        "weight": 0.8124
      }
    },
    {
      "data": {
        "id": "e1838",
        "source": "1909_04939",
        "target": "2012_08791",
        "weight": 0.7578
      }
    },
    {
      "data": {
        "id": "e1839",
        "source": "1909_04939",
        "target": "2304_13029",
        "weight": 0.8095
      }
    },
    {
      "data": {
        "id": "e1840",
        "source": "1909_04939",
        "target": "2202_07125",
        "weight": 0.7702
      }
    },
    {
      "data": {
        "id": "e1841",
        "source": "1909_04939",
        "target": "2308_00928",
        "weight": 0.7741
      }
    },
    {
      "data": {
        "id": "e1842",
        "source": "1909_04939",
        "target": "2103_14438",
        "weight": 0.7756
      }
    },
    {
      "data": {
        "id": "e1843",
        "source": "1909_09688",
        "target": "2009_10484",
        "weight": 0.8778
      }
    },
    {
      "data": {
        "id": "e1844",
        "source": "1909_09688",
        "target": "2410_19414",
        "weight": 0.8183
      }
    },
    {
      "data": {
        "id": "e1845",
        "source": "1909_09688",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.8755
      }
    },
    {
      "data": {
        "id": "e1846",
        "source": "1909_09688",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8373
      }
    },
    {
      "data": {
        "id": "e1847",
        "source": "1909_09688",
        "target": "2411_17902",
        "weight": 0.8215
      }
    },
    {
      "data": {
        "id": "e1848",
        "source": "1909_09688",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8054
      }
    },
    {
      "data": {
        "id": "e1849",
        "source": "1909_09688",
        "target": "2503_16164",
        "weight": 0.8797
      }
    },
    {
      "data": {
        "id": "e1850",
        "source": "1909_09688",
        "target": "2203_01751",
        "weight": 0.8213
      }
    },
    {
      "data": {
        "id": "e1851",
        "source": "1909_09688",
        "target": "2203_02176",
        "weight": 0.8561
      }
    },
    {
      "data": {
        "id": "e1852",
        "source": "1909_09688",
        "target": "2505_10542",
        "weight": 0.8726
      }
    },
    {
      "data": {
        "id": "e1853",
        "source": "1909_09688",
        "target": "2301_13143",
        "weight": 0.8231
      }
    },
    {
      "data": {
        "id": "e1854",
        "source": "1909_09688",
        "target": "2309_14595",
        "weight": 0.8205
      }
    },
    {
      "data": {
        "id": "e1855",
        "source": "1909_09688",
        "target": "2403_10745",
        "weight": 0.8284
      }
    },
    {
      "data": {
        "id": "e1856",
        "source": "1909_10466",
        "target": "2022_schmid_dynamic_mode_decomposition_and",
        "weight": 0.9143
      }
    },
    {
      "data": {
        "id": "e1857",
        "source": "1912_01603",
        "target": "2310_16828",
        "weight": 0.809
      }
    },
    {
      "data": {
        "id": "e1858",
        "source": "1912_01603",
        "target": "2407_15007",
        "weight": 0.7864
      }
    },
    {
      "data": {
        "id": "e1859",
        "source": "1912_01603",
        "target": "2603_19968",
        "weight": 0.7882
      }
    },
    {
      "data": {
        "id": "e1860",
        "source": "1912_01603",
        "target": "2205_09991",
        "weight": 0.7948
      }
    },
    {
      "data": {
        "id": "e1861",
        "source": "1912_11676",
        "target": "2502_08664",
        "weight": 0.8891
      }
    },
    {
      "data": {
        "id": "e1862",
        "source": "1912_11676",
        "target": "2005_04259",
        "weight": 0.8051
      }
    },
    {
      "data": {
        "id": "e1863",
        "source": "1912_11676",
        "target": "2503_03262",
        "weight": 0.8608
      }
    },
    {
      "data": {
        "id": "e1864",
        "source": "1912_11676",
        "target": "2024_calem_action_and_trajectory_prediction",
        "weight": 0.8252
      }
    },
    {
      "data": {
        "id": "e1865",
        "source": "1912_11676",
        "target": "2303_09824",
        "weight": 0.8416
      }
    },
    {
      "data": {
        "id": "e1866",
        "source": "1912_11676",
        "target": "2511_00088",
        "weight": 0.8082
      }
    },
    {
      "data": {
        "id": "e1867",
        "source": "1912_11676",
        "target": "2505_09074",
        "weight": 0.8339
      }
    },
    {
      "data": {
        "id": "e1868",
        "source": "1912_11676",
        "target": "2412_14415",
        "weight": 0.8072
      }
    },
    {
      "data": {
        "id": "e1869",
        "source": "1912_11676",
        "target": "2207_05844",
        "weight": 0.8098
      }
    },
    {
      "data": {
        "id": "e1870",
        "source": "1912_11912",
        "target": "2209_09006",
        "weight": 0.8047
      }
    },
    {
      "data": {
        "id": "e1871",
        "source": "1912_11912",
        "target": "2602_18933",
        "weight": 0.8163
      }
    },
    {
      "data": {
        "id": "e1872",
        "source": "1912_11912",
        "target": "2311_07411",
        "weight": 0.8018
      }
    },
    {
      "data": {
        "id": "e1873",
        "source": "1912_11912",
        "target": "2311_11166",
        "weight": 0.8455
      }
    },
    {
      "data": {
        "id": "e1874",
        "source": "1912_11912",
        "target": "2311_11489",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e1875",
        "source": "1912_11912",
        "target": "2604_18578",
        "weight": 0.8289
      }
    },
    {
      "data": {
        "id": "e1876",
        "source": "1912_11912",
        "target": "2401_13662",
        "weight": 0.8071
      }
    },
    {
      "data": {
        "id": "e1877",
        "source": "1912_11912",
        "target": "2401_16025",
        "weight": 0.8377
      }
    },
    {
      "data": {
        "id": "e1878",
        "source": "1912_11912",
        "target": "2511_02095",
        "weight": 0.8313
      }
    },
    {
      "data": {
        "id": "e1879",
        "source": "1912_11912",
        "target": "2511_11131",
        "weight": 0.8008
      }
    },
    {
      "data": {
        "id": "e1880",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2004_08763",
        "weight": 0.8016
      }
    },
    {
      "data": {
        "id": "e1881",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2409_12266",
        "weight": 0.8005
      }
    },
    {
      "data": {
        "id": "e1882",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2604_12149",
        "weight": 0.821
      }
    },
    {
      "data": {
        "id": "e1883",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2409_15610",
        "weight": 0.8037
      }
    },
    {
      "data": {
        "id": "e1884",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2410_23916",
        "weight": 0.82
      }
    },
    {
      "data": {
        "id": "e1885",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2411_15651",
        "weight": 0.8094
      }
    },
    {
      "data": {
        "id": "e1886",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8026
      }
    },
    {
      "data": {
        "id": "e1887",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2109_07081",
        "weight": 0.829
      }
    },
    {
      "data": {
        "id": "e1888",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8124
      }
    },
    {
      "data": {
        "id": "e1889",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2203_01751",
        "weight": 0.8038
      }
    },
    {
      "data": {
        "id": "e1890",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2204_02322",
        "weight": 0.83
      }
    },
    {
      "data": {
        "id": "e1891",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2207_06362",
        "weight": 0.8205
      }
    },
    {
      "data": {
        "id": "e1892",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2208_02439",
        "weight": 0.8113
      }
    },
    {
      "data": {
        "id": "e1893",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2210_01744",
        "weight": 0.8149
      }
    },
    {
      "data": {
        "id": "e1894",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2508_21001",
        "weight": 0.8043
      }
    },
    {
      "data": {
        "id": "e1895",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2301_13143",
        "weight": 0.8565
      }
    },
    {
      "data": {
        "id": "e1896",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2304_00346",
        "weight": 0.804
      }
    },
    {
      "data": {
        "id": "e1897",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2305_09619",
        "weight": 0.8152
      }
    },
    {
      "data": {
        "id": "e1898",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2602_03639",
        "weight": 0.8002
      }
    },
    {
      "data": {
        "id": "e1899",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2401_09241",
        "weight": 0.8119
      }
    },
    {
      "data": {
        "id": "e1900",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2403_00748",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e1901",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2403_10745",
        "weight": 0.8281
      }
    },
    {
      "data": {
        "id": "e1902",
        "source": "2019_hannigan_sbp_guided_mpc_to",
        "target": "2019_jackson_altro_a_fast_solver",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e1903",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2005_00985",
        "weight": 0.8402
      }
    },
    {
      "data": {
        "id": "e1904",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2409_11649",
        "weight": 0.8293
      }
    },
    {
      "data": {
        "id": "e1905",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2410_23916",
        "weight": 0.8103
      }
    },
    {
      "data": {
        "id": "e1906",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2103_03293",
        "weight": 0.8091
      }
    },
    {
      "data": {
        "id": "e1907",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2109_07081",
        "weight": 0.8258
      }
    },
    {
      "data": {
        "id": "e1908",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8032
      }
    },
    {
      "data": {
        "id": "e1909",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2203_01751",
        "weight": 0.8013
      }
    },
    {
      "data": {
        "id": "e1910",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2504_18978",
        "weight": 0.8143
      }
    },
    {
      "data": {
        "id": "e1911",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2204_02322",
        "weight": 0.8074
      }
    },
    {
      "data": {
        "id": "e1912",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2205_04422",
        "weight": 0.8231
      }
    },
    {
      "data": {
        "id": "e1913",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2506_14865",
        "weight": 0.8579
      }
    },
    {
      "data": {
        "id": "e1914",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2207_06362",
        "weight": 0.8046
      }
    },
    {
      "data": {
        "id": "e1915",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2506_22087",
        "weight": 0.8096
      }
    },
    {
      "data": {
        "id": "e1916",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2209_09006",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e1917",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8535
      }
    },
    {
      "data": {
        "id": "e1918",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2303_16746",
        "weight": 0.8541
      }
    },
    {
      "data": {
        "id": "e1919",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2304_00346",
        "weight": 0.8143
      }
    },
    {
      "data": {
        "id": "e1920",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2307_03167",
        "weight": 0.8258
      }
    },
    {
      "data": {
        "id": "e1921",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2511_14752",
        "weight": 0.8137
      }
    },
    {
      "data": {
        "id": "e1922",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2311_06404",
        "weight": 0.8164
      }
    },
    {
      "data": {
        "id": "e1923",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2603_00871",
        "weight": 0.8519
      }
    },
    {
      "data": {
        "id": "e1924",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.862
      }
    },
    {
      "data": {
        "id": "e1925",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2603_10711",
        "weight": 0.8006
      }
    },
    {
      "data": {
        "id": "e1926",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2603_11335",
        "weight": 0.8416
      }
    },
    {
      "data": {
        "id": "e1927",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2403_00748",
        "weight": 0.8282
      }
    },
    {
      "data": {
        "id": "e1928",
        "source": "2019_jackson_altro_a_fast_solver",
        "target": "2406_05846",
        "weight": 0.831
      }
    },
    {
      "data": {
        "id": "e1929",
        "source": "2019_lefebvre_path_integral_policy_improvement",
        "target": "2004_08763",
        "weight": 0.81
      }
    },
    {
      "data": {
        "id": "e1930",
        "source": "2019_lefebvre_path_integral_policy_improvement",
        "target": "2005_00985",
        "weight": 0.8082
      }
    },
    {
      "data": {
        "id": "e1931",
        "source": "2019_lefebvre_path_integral_policy_improvement",
        "target": "2409_11649",
        "weight": 0.8003
      }
    },
    {
      "data": {
        "id": "e1932",
        "source": "2019_lefebvre_path_integral_policy_improvement",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.844
      }
    },
    {
      "data": {
        "id": "e1933",
        "source": "2019_lefebvre_path_integral_policy_improvement",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8192
      }
    },
    {
      "data": {
        "id": "e1934",
        "source": "2019_lefebvre_path_integral_policy_improvement",
        "target": "2109_07081",
        "weight": 0.8133
      }
    },
    {
      "data": {
        "id": "e1935",
        "source": "2019_lefebvre_path_integral_policy_improvement",
        "target": "2022_houghton_path_planning_differential_dynamic",
        "weight": 0.8112
      }
    },
    {
      "data": {
        "id": "e1936",
        "source": "2019_lefebvre_path_integral_policy_improvement",
        "target": "2208_02439",
        "weight": 0.8019
      }
    },
    {
      "data": {
        "id": "e1937",
        "source": "2019_lefebvre_path_integral_policy_improvement",
        "target": "2209_09006",
        "weight": 0.8323
      }
    },
    {
      "data": {
        "id": "e1938",
        "source": "2019_lefebvre_path_integral_policy_improvement",
        "target": "2511_02015",
        "weight": 0.8253
      }
    },
    {
      "data": {
        "id": "e1939",
        "source": "2019_lefebvre_path_integral_policy_improvement",
        "target": "2309_12566",
        "weight": 0.8585
      }
    },
    {
      "data": {
        "id": "e1940",
        "source": "2019_lefebvre_path_integral_policy_improvement",
        "target": "2602_03639",
        "weight": 0.8084
      }
    },
    {
      "data": {
        "id": "e1941",
        "source": "2019_lefebvre_path_integral_policy_improvement",
        "target": "2603_05385",
        "weight": 0.8097
      }
    },
    {
      "data": {
        "id": "e1942",
        "source": "2019_lefebvre_path_integral_policy_improvement",
        "target": "2603_24489",
        "weight": 0.8232
      }
    },
    {
      "data": {
        "id": "e1943",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2409_12266",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e1944",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2604_12149",
        "weight": 0.8007
      }
    },
    {
      "data": {
        "id": "e1945",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2604_13312",
        "weight": 0.8266
      }
    },
    {
      "data": {
        "id": "e1946",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2410_23916",
        "weight": 0.8117
      }
    },
    {
      "data": {
        "id": "e1947",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8627
      }
    },
    {
      "data": {
        "id": "e1948",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8512
      }
    },
    {
      "data": {
        "id": "e1949",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2025_trevisan_model_predictive_path_integral",
        "weight": 0.8394
      }
    },
    {
      "data": {
        "id": "e1950",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2104_00241",
        "weight": 0.8197
      }
    },
    {
      "data": {
        "id": "e1951",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2503_05819",
        "weight": 0.8193
      }
    },
    {
      "data": {
        "id": "e1952",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2022_houghton_path_planning_differential_dynamic",
        "weight": 0.8344
      }
    },
    {
      "data": {
        "id": "e1953",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2503_11717",
        "weight": 0.8556
      }
    },
    {
      "data": {
        "id": "e1954",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2504_06437",
        "weight": 0.8264
      }
    },
    {
      "data": {
        "id": "e1955",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2203_04955",
        "weight": 0.8087
      }
    },
    {
      "data": {
        "id": "e1956",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2506_21205",
        "weight": 0.8208
      }
    },
    {
      "data": {
        "id": "e1957",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2208_02439",
        "weight": 0.8095
      }
    },
    {
      "data": {
        "id": "e1958",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2212_02603",
        "weight": 0.8067
      }
    },
    {
      "data": {
        "id": "e1959",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2508_21364",
        "weight": 0.8683
      }
    },
    {
      "data": {
        "id": "e1960",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2509_14978",
        "weight": 0.8225
      }
    },
    {
      "data": {
        "id": "e1961",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2301_13143",
        "weight": 0.8342
      }
    },
    {
      "data": {
        "id": "e1962",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2510_00272",
        "weight": 0.8369
      }
    },
    {
      "data": {
        "id": "e1963",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2511_02015",
        "weight": 0.843
      }
    },
    {
      "data": {
        "id": "e1964",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2511_11308",
        "weight": 0.8084
      }
    },
    {
      "data": {
        "id": "e1965",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2307_09105",
        "weight": 0.8252
      }
    },
    {
      "data": {
        "id": "e1966",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2309_12566",
        "weight": 0.8983
      }
    },
    {
      "data": {
        "id": "e1967",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2602_03639",
        "weight": 0.8502
      }
    },
    {
      "data": {
        "id": "e1968",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2603_05385",
        "weight": 0.8464
      }
    },
    {
      "data": {
        "id": "e1969",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2401_09241",
        "weight": 0.8614
      }
    },
    {
      "data": {
        "id": "e1970",
        "source": "2019_williams_model_predictive_path_integral",
        "target": "2603_24489",
        "weight": 0.8794
      }
    },
    {
      "data": {
        "id": "e1971",
        "source": "2001_03093",
        "target": "2502_08664",
        "weight": 0.8074
      }
    },
    {
      "data": {
        "id": "e1972",
        "source": "2001_03093",
        "target": "2409_09523",
        "weight": 0.816
      }
    },
    {
      "data": {
        "id": "e1973",
        "source": "2001_03093",
        "target": "2005_04259",
        "weight": 0.8373
      }
    },
    {
      "data": {
        "id": "e1974",
        "source": "2001_03093",
        "target": "2503_03262",
        "weight": 0.847
      }
    },
    {
      "data": {
        "id": "e1975",
        "source": "2001_03093",
        "target": "2301_11902",
        "weight": 0.828
      }
    },
    {
      "data": {
        "id": "e1976",
        "source": "2001_03093",
        "target": "2503_06135",
        "weight": 0.8038
      }
    },
    {
      "data": {
        "id": "e1977",
        "source": "2001_03093",
        "target": "2024_calem_action_and_trajectory_prediction",
        "weight": 0.8417
      }
    },
    {
      "data": {
        "id": "e1978",
        "source": "2001_03093",
        "target": "2603_14392",
        "weight": 0.827
      }
    },
    {
      "data": {
        "id": "e1979",
        "source": "2001_03093",
        "target": "2505_09074",
        "weight": 0.8551
      }
    },
    {
      "data": {
        "id": "e1980",
        "source": "2001_03093",
        "target": "2412_14415",
        "weight": 0.8184
      }
    },
    {
      "data": {
        "id": "e1981",
        "source": "2001_03093",
        "target": "2207_05844",
        "weight": 0.8168
      }
    },
    {
      "data": {
        "id": "e1982",
        "source": "2002_08809",
        "target": "2005_00985",
        "weight": 0.8309
      }
    },
    {
      "data": {
        "id": "e1983",
        "source": "2002_08809",
        "target": "2109_07081",
        "weight": 0.8186
      }
    },
    {
      "data": {
        "id": "e1984",
        "source": "2002_08809",
        "target": "2409_11649",
        "weight": 0.822
      }
    },
    {
      "data": {
        "id": "e1985",
        "source": "2002_08809",
        "target": "2010_00411",
        "weight": 0.8125
      }
    },
    {
      "data": {
        "id": "e1986",
        "source": "2002_08809",
        "target": "2020_marti_saumell_squash_box_feasibility_driven",
        "weight": 0.8126
      }
    },
    {
      "data": {
        "id": "e1987",
        "source": "2002_08809",
        "target": "2309_07872",
        "weight": 0.8112
      }
    },
    {
      "data": {
        "id": "e1988",
        "source": "2003_02218",
        "target": "2201_02177",
        "weight": 0.7804
      }
    },
    {
      "data": {
        "id": "e1989",
        "source": "2003_02218",
        "target": "2012_00152",
        "weight": 0.7714
      }
    },
    {
      "data": {
        "id": "e1990",
        "source": "2003_02218",
        "target": "2412_12036",
        "weight": 0.7886
      }
    },
    {
      "data": {
        "id": "e1991",
        "source": "2003_02218",
        "target": "2103_00065",
        "weight": 0.8046
      }
    },
    {
      "data": {
        "id": "e1992",
        "source": "2003_08934",
        "target": "2006_11239",
        "weight": 0.7397
      }
    },
    {
      "data": {
        "id": "e1993",
        "source": "2003_08934",
        "target": "2304_07193",
        "weight": 0.736
      }
    },
    {
      "data": {
        "id": "e1994",
        "source": "2003_08934",
        "target": "2504_12905",
        "weight": 0.7638
      }
    },
    {
      "data": {
        "id": "e1995",
        "source": "2003_08934",
        "target": "2308_04079",
        "weight": 0.8243
      }
    },
    {
      "data": {
        "id": "e1996",
        "source": "2003_08934",
        "target": "2103_15691",
        "weight": 0.7329
      }
    },
    {
      "data": {
        "id": "e1997",
        "source": "2004_08763",
        "target": "2409_12266",
        "weight": 0.8088
      }
    },
    {
      "data": {
        "id": "e1998",
        "source": "2004_08763",
        "target": "2604_12149",
        "weight": 0.8369
      }
    },
    {
      "data": {
        "id": "e1999",
        "source": "2004_08763",
        "target": "2409_15610",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e2000",
        "source": "2004_08763",
        "target": "2410_23916",
        "weight": 0.8086
      }
    },
    {
      "data": {
        "id": "e2001",
        "source": "2004_08763",
        "target": "2411_15651",
        "weight": 0.8216
      }
    },
    {
      "data": {
        "id": "e2002",
        "source": "2004_08763",
        "target": "2412_11270",
        "weight": 0.8056
      }
    },
    {
      "data": {
        "id": "e2003",
        "source": "2004_08763",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8005
      }
    },
    {
      "data": {
        "id": "e2004",
        "source": "2004_08763",
        "target": "2104_00241",
        "weight": 0.8084
      }
    },
    {
      "data": {
        "id": "e2005",
        "source": "2004_08763",
        "target": "2503_05819",
        "weight": 0.8186
      }
    },
    {
      "data": {
        "id": "e2006",
        "source": "2004_08763",
        "target": "2203_01751",
        "weight": 0.8035
      }
    },
    {
      "data": {
        "id": "e2007",
        "source": "2004_08763",
        "target": "2203_04955",
        "weight": 0.8087
      }
    },
    {
      "data": {
        "id": "e2008",
        "source": "2004_08763",
        "target": "2205_09991",
        "weight": 0.8148
      }
    },
    {
      "data": {
        "id": "e2009",
        "source": "2004_08763",
        "target": "2209_09006",
        "weight": 0.8118
      }
    },
    {
      "data": {
        "id": "e2010",
        "source": "2004_08763",
        "target": "2212_02603",
        "weight": 0.8242
      }
    },
    {
      "data": {
        "id": "e2011",
        "source": "2004_08763",
        "target": "2508_21800",
        "weight": 0.8043
      }
    },
    {
      "data": {
        "id": "e2012",
        "source": "2004_08763",
        "target": "2301_13143",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e2013",
        "source": "2004_08763",
        "target": "2511_02015",
        "weight": 0.8278
      }
    },
    {
      "data": {
        "id": "e2014",
        "source": "2004_08763",
        "target": "2511_11308",
        "weight": 0.8133
      }
    },
    {
      "data": {
        "id": "e2015",
        "source": "2004_08763",
        "target": "2309_12566",
        "weight": 0.8389
      }
    },
    {
      "data": {
        "id": "e2016",
        "source": "2004_08763",
        "target": "2602_03639",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e2017",
        "source": "2004_08763",
        "target": "2603_24489",
        "weight": 0.83
      }
    },
    {
      "data": {
        "id": "e2018",
        "source": "2005_00985",
        "target": "2409_11649",
        "weight": 0.9261
      }
    },
    {
      "data": {
        "id": "e2019",
        "source": "2005_00985",
        "target": "2010_00411",
        "weight": 0.8773
      }
    },
    {
      "data": {
        "id": "e2020",
        "source": "2005_00985",
        "target": "2020_marti_saumell_squash_box_feasibility_driven",
        "weight": 0.8608
      }
    },
    {
      "data": {
        "id": "e2021",
        "source": "2005_00985",
        "target": "2020_pellegrini_a_multiple_shooting_differential",
        "weight": 0.849
      }
    },
    {
      "data": {
        "id": "e2022",
        "source": "2005_00985",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8169
      }
    },
    {
      "data": {
        "id": "e2023",
        "source": "2005_00985",
        "target": "2103_03293",
        "weight": 0.8803
      }
    },
    {
      "data": {
        "id": "e2024",
        "source": "2005_00985",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8901
      }
    },
    {
      "data": {
        "id": "e2025",
        "source": "2005_00985",
        "target": "2109_07081",
        "weight": 0.8776
      }
    },
    {
      "data": {
        "id": "e2026",
        "source": "2005_00985",
        "target": "2022_houghton_path_planning_differential_dynamic",
        "weight": 0.8299
      }
    },
    {
      "data": {
        "id": "e2027",
        "source": "2005_00985",
        "target": "2204_02322",
        "weight": 0.8322
      }
    },
    {
      "data": {
        "id": "e2028",
        "source": "2005_00985",
        "target": "2506_14865",
        "weight": 0.8042
      }
    },
    {
      "data": {
        "id": "e2029",
        "source": "2005_00985",
        "target": "2207_06362",
        "weight": 0.8132
      }
    },
    {
      "data": {
        "id": "e2030",
        "source": "2005_00985",
        "target": "2208_02439",
        "weight": 0.824
      }
    },
    {
      "data": {
        "id": "e2031",
        "source": "2005_00985",
        "target": "2209_09006",
        "weight": 0.8207
      }
    },
    {
      "data": {
        "id": "e2032",
        "source": "2005_00985",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.9079
      }
    },
    {
      "data": {
        "id": "e2033",
        "source": "2005_00985",
        "target": "2511_14752",
        "weight": 0.8018
      }
    },
    {
      "data": {
        "id": "e2034",
        "source": "2005_00985",
        "target": "2309_07872",
        "weight": 0.8795
      }
    },
    {
      "data": {
        "id": "e2035",
        "source": "2005_00985",
        "target": "2311_06404",
        "weight": 0.8439
      }
    },
    {
      "data": {
        "id": "e2036",
        "source": "2005_00985",
        "target": "2603_00871",
        "weight": 0.802
      }
    },
    {
      "data": {
        "id": "e2037",
        "source": "2005_00985",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8752
      }
    },
    {
      "data": {
        "id": "e2038",
        "source": "2005_00985",
        "target": "2024_wang_a_convergence_guaranteed_multiple",
        "weight": 0.8576
      }
    },
    {
      "data": {
        "id": "e2039",
        "source": "2005_00985",
        "target": "2603_11335",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e2040",
        "source": "2005_00985",
        "target": "2403_00748",
        "weight": 0.8093
      }
    },
    {
      "data": {
        "id": "e2041",
        "source": "2005_04259",
        "target": "2412_14415",
        "weight": 0.8295
      }
    },
    {
      "data": {
        "id": "e2042",
        "source": "2005_04259",
        "target": "2111_12137",
        "weight": 0.8051
      }
    },
    {
      "data": {
        "id": "e2043",
        "source": "2005_04259",
        "target": "2411_18714",
        "weight": 0.8208
      }
    },
    {
      "data": {
        "id": "e2044",
        "source": "2005_04259",
        "target": "2505_09074",
        "weight": 0.8179
      }
    },
    {
      "data": {
        "id": "e2045",
        "source": "2005_04259",
        "target": "2207_05844",
        "weight": 0.8462
      }
    },
    {
      "data": {
        "id": "e2046",
        "source": "2005_04259",
        "target": "2310_08710",
        "weight": 0.8197
      }
    },
    {
      "data": {
        "id": "e2047",
        "source": "2006_11239",
        "target": "2010_01412",
        "weight": 0.7106
      }
    },
    {
      "data": {
        "id": "e2048",
        "source": "2006_11239",
        "target": "2205_09991",
        "weight": 0.7233
      }
    },
    {
      "data": {
        "id": "e2049",
        "source": "2006_11239",
        "target": "2304_07193",
        "weight": 0.7066
      }
    },
    {
      "data": {
        "id": "e2050",
        "source": "2006_11239",
        "target": "2512_18736",
        "weight": 0.8485
      }
    },
    {
      "data": {
        "id": "e2051",
        "source": "2008_08835",
        "target": "2509_14978",
        "weight": 0.8003
      }
    },
    {
      "data": {
        "id": "e2052",
        "source": "2008_08835",
        "target": "2306_09852",
        "weight": 0.7895
      }
    },
    {
      "data": {
        "id": "e2053",
        "source": "2008_08835",
        "target": "2205_04422",
        "weight": 0.7858
      }
    },
    {
      "data": {
        "id": "e2054",
        "source": "2009_10484",
        "target": "2409_12266",
        "weight": 0.8311
      }
    },
    {
      "data": {
        "id": "e2055",
        "source": "2009_10484",
        "target": "2410_19414",
        "weight": 0.9036
      }
    },
    {
      "data": {
        "id": "e2056",
        "source": "2009_10484",
        "target": "2020_mashayekhi_informed_rrt_star_connect",
        "weight": 0.815
      }
    },
    {
      "data": {
        "id": "e2057",
        "source": "2009_10484",
        "target": "2411_17902",
        "weight": 0.8177
      }
    },
    {
      "data": {
        "id": "e2058",
        "source": "2009_10484",
        "target": "2022_honig_benchmarking_sampling_search_and",
        "weight": 0.8529
      }
    },
    {
      "data": {
        "id": "e2059",
        "source": "2009_10484",
        "target": "2503_16164",
        "weight": 0.8462
      }
    },
    {
      "data": {
        "id": "e2060",
        "source": "2009_10484",
        "target": "2203_01751",
        "weight": 0.857
      }
    },
    {
      "data": {
        "id": "e2061",
        "source": "2009_10484",
        "target": "2203_02176",
        "weight": 0.816
      }
    },
    {
      "data": {
        "id": "e2062",
        "source": "2009_10484",
        "target": "2505_10542",
        "weight": 0.8018
      }
    },
    {
      "data": {
        "id": "e2063",
        "source": "2009_10484",
        "target": "2205_04422",
        "weight": 0.8029
      }
    },
    {
      "data": {
        "id": "e2064",
        "source": "2009_10484",
        "target": "2506_22087",
        "weight": 0.815
      }
    },
    {
      "data": {
        "id": "e2065",
        "source": "2009_10484",
        "target": "2508_21001",
        "weight": 0.8013
      }
    },
    {
      "data": {
        "id": "e2066",
        "source": "2009_10484",
        "target": "2301_13143",
        "weight": 0.8161
      }
    },
    {
      "data": {
        "id": "e2067",
        "source": "2009_10484",
        "target": "2510_21074",
        "weight": 0.8033
      }
    },
    {
      "data": {
        "id": "e2068",
        "source": "2009_10484",
        "target": "2305_01072",
        "weight": 0.8021
      }
    },
    {
      "data": {
        "id": "e2069",
        "source": "2009_10484",
        "target": "2307_03167",
        "weight": 0.8351
      }
    },
    {
      "data": {
        "id": "e2070",
        "source": "2009_10484",
        "target": "2309_14545",
        "weight": 0.8336
      }
    },
    {
      "data": {
        "id": "e2071",
        "source": "2009_10484",
        "target": "2602_00992",
        "weight": 0.8062
      }
    },
    {
      "data": {
        "id": "e2072",
        "source": "2009_10484",
        "target": "2602_02846",
        "weight": 0.8122
      }
    },
    {
      "data": {
        "id": "e2073",
        "source": "2009_10484",
        "target": "2401_09241",
        "weight": 0.8028
      }
    },
    {
      "data": {
        "id": "e2074",
        "source": "2009_10484",
        "target": "2403_10745",
        "weight": 0.8135
      }
    },
    {
      "data": {
        "id": "e2075",
        "source": "2010_00411",
        "target": "2409_11649",
        "weight": 0.8671
      }
    },
    {
      "data": {
        "id": "e2076",
        "source": "2010_00411",
        "target": "2409_15610",
        "weight": 0.8103
      }
    },
    {
      "data": {
        "id": "e2077",
        "source": "2010_00411",
        "target": "2020_marti_saumell_squash_box_feasibility_driven",
        "weight": 0.8996
      }
    },
    {
      "data": {
        "id": "e2078",
        "source": "2010_00411",
        "target": "2020_pellegrini_a_multiple_shooting_differential",
        "weight": 0.8336
      }
    },
    {
      "data": {
        "id": "e2079",
        "source": "2010_00411",
        "target": "2103_03293",
        "weight": 0.8428
      }
    },
    {
      "data": {
        "id": "e2080",
        "source": "2010_00411",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8427
      }
    },
    {
      "data": {
        "id": "e2081",
        "source": "2010_00411",
        "target": "2109_07081",
        "weight": 0.872
      }
    },
    {
      "data": {
        "id": "e2082",
        "source": "2010_00411",
        "target": "2022_houghton_path_planning_differential_dynamic",
        "weight": 0.8015
      }
    },
    {
      "data": {
        "id": "e2083",
        "source": "2010_00411",
        "target": "2208_02439",
        "weight": 0.8285
      }
    },
    {
      "data": {
        "id": "e2084",
        "source": "2010_00411",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8904
      }
    },
    {
      "data": {
        "id": "e2085",
        "source": "2010_00411",
        "target": "2309_07872",
        "weight": 0.9061
      }
    },
    {
      "data": {
        "id": "e2086",
        "source": "2010_00411",
        "target": "2603_00871",
        "weight": 0.8021
      }
    },
    {
      "data": {
        "id": "e2087",
        "source": "2010_00411",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8602
      }
    },
    {
      "data": {
        "id": "e2088",
        "source": "2010_00411",
        "target": "2024_wang_a_convergence_guaranteed_multiple",
        "weight": 0.8808
      }
    },
    {
      "data": {
        "id": "e2089",
        "source": "2010_01412",
        "target": "2201_02177",
        "weight": 0.7683
      }
    },
    {
      "data": {
        "id": "e2090",
        "source": "2010_01412",
        "target": "2304_07193",
        "weight": 0.7445
      }
    },
    {
      "data": {
        "id": "e2091",
        "source": "2010_01412",
        "target": "2506_05454",
        "weight": 0.78
      }
    },
    {
      "data": {
        "id": "e2092",
        "source": "2010_01412",
        "target": "2406_16793",
        "weight": 0.751
      }
    },
    {
      "data": {
        "id": "e2093",
        "source": "2010_10726",
        "target": "2504_18978",
        "weight": 0.7262
      }
    },
    {
      "data": {
        "id": "e2094",
        "source": "2010_10726",
        "target": "2205_04422",
        "weight": 0.7204
      }
    },
    {
      "data": {
        "id": "e2095",
        "source": "2010_11929",
        "target": "2410_13732",
        "weight": 0.8356
      }
    },
    {
      "data": {
        "id": "e2096",
        "source": "2010_11929",
        "target": "2011_14439",
        "weight": 0.7388
      }
    },
    {
      "data": {
        "id": "e2097",
        "source": "2010_11929",
        "target": "2304_07193",
        "weight": 0.7924
      }
    },
    {
      "data": {
        "id": "e2098",
        "source": "2010_11929",
        "target": "2103_15691",
        "weight": 0.8404
      }
    },
    {
      "data": {
        "id": "e2099",
        "source": "2011_11303",
        "target": "2212_02603",
        "weight": 0.8616
      }
    },
    {
      "data": {
        "id": "e2100",
        "source": "2011_11303",
        "target": "2604_11183",
        "weight": 0.8093
      }
    },
    {
      "data": {
        "id": "e2101",
        "source": "2011_11303",
        "target": "2312_02758",
        "weight": 0.8599
      }
    },
    {
      "data": {
        "id": "e2102",
        "source": "2011_11303",
        "target": "2603_05385",
        "weight": 0.8177
      }
    },
    {
      "data": {
        "id": "e2103",
        "source": "2011_11303",
        "target": "2410_23916",
        "weight": 0.8282
      }
    },
    {
      "data": {
        "id": "e2104",
        "source": "2011_11303",
        "target": "2603_16808",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e2105",
        "source": "2011_11303",
        "target": "2203_04955",
        "weight": 0.8348
      }
    },
    {
      "data": {
        "id": "e2106",
        "source": "2011_11303",
        "target": "2603_23465",
        "weight": 0.8055
      }
    },
    {
      "data": {
        "id": "e2107",
        "source": "2011_11303",
        "target": "2203_15471",
        "weight": 0.8136
      }
    },
    {
      "data": {
        "id": "e2108",
        "source": "2011_11303",
        "target": "2511_11308",
        "weight": 0.8307
      }
    },
    {
      "data": {
        "id": "e2109",
        "source": "2011_11303",
        "target": "2603_24489",
        "weight": 0.8189
      }
    },
    {
      "data": {
        "id": "e2110",
        "source": "2011_11303",
        "target": "2102_08302",
        "weight": 0.8429
      }
    },
    {
      "data": {
        "id": "e2111",
        "source": "2011_11303",
        "target": "2310_02918",
        "weight": 0.8236
      }
    },
    {
      "data": {
        "id": "e2112",
        "source": "2011_11303",
        "target": "2604_00900",
        "weight": 0.8269
      }
    },
    {
      "data": {
        "id": "e2113",
        "source": "2011_14439",
        "target": "2410_13732",
        "weight": 0.7297
      }
    },
    {
      "data": {
        "id": "e2114",
        "source": "2011_14439",
        "target": "2201_02177",
        "weight": 0.7577
      }
    },
    {
      "data": {
        "id": "e2115",
        "source": "2011_14439",
        "target": "2406_16793",
        "weight": 0.7956
      }
    },
    {
      "data": {
        "id": "e2116",
        "source": "2012_00152",
        "target": "2201_02177",
        "weight": 0.7656
      }
    },
    {
      "data": {
        "id": "e2117",
        "source": "2012_00152",
        "target": "2103_00065",
        "weight": 0.7697
      }
    },
    {
      "data": {
        "id": "e2118",
        "source": "2012_08791",
        "target": "2304_13029",
        "weight": 0.8062
      }
    },
    {
      "data": {
        "id": "e2119",
        "source": "2012_08791",
        "target": "2202_07125",
        "weight": 0.77
      }
    },
    {
      "data": {
        "id": "e2120",
        "source": "2012_08791",
        "target": "2308_00928",
        "weight": 0.826
      }
    },
    {
      "data": {
        "id": "e2121",
        "source": "2012_08791",
        "target": "2103_14438",
        "weight": 0.7452
      }
    },
    {
      "data": {
        "id": "e2122",
        "source": "2012_12657",
        "target": "2604_11183",
        "weight": 0.7612
      }
    },
    {
      "data": {
        "id": "e2123",
        "source": "2012_12657",
        "target": "2511_10622",
        "weight": 0.7748
      }
    },
    {
      "data": {
        "id": "e2124",
        "source": "2012_12657",
        "target": "2403_18972",
        "weight": 0.7682
      }
    },
    {
      "data": {
        "id": "e2125",
        "source": "2012_12657",
        "target": "2601_14880",
        "weight": 0.7718
      }
    },
    {
      "data": {
        "id": "e2126",
        "source": "2020_marti_saumell_squash_box_feasibility_driven",
        "target": "2208_02439",
        "weight": 0.8082
      }
    },
    {
      "data": {
        "id": "e2127",
        "source": "2020_marti_saumell_squash_box_feasibility_driven",
        "target": "2109_07081",
        "weight": 0.8537
      }
    },
    {
      "data": {
        "id": "e2128",
        "source": "2020_marti_saumell_squash_box_feasibility_driven",
        "target": "2409_11649",
        "weight": 0.8315
      }
    },
    {
      "data": {
        "id": "e2129",
        "source": "2020_marti_saumell_squash_box_feasibility_driven",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8632
      }
    },
    {
      "data": {
        "id": "e2130",
        "source": "2020_marti_saumell_squash_box_feasibility_driven",
        "target": "2603_00871",
        "weight": 0.8008
      }
    },
    {
      "data": {
        "id": "e2131",
        "source": "2020_marti_saumell_squash_box_feasibility_driven",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.834
      }
    },
    {
      "data": {
        "id": "e2132",
        "source": "2020_marti_saumell_squash_box_feasibility_driven",
        "target": "2024_wang_a_convergence_guaranteed_multiple",
        "weight": 0.8212
      }
    },
    {
      "data": {
        "id": "e2133",
        "source": "2020_marti_saumell_squash_box_feasibility_driven",
        "target": "2204_02322",
        "weight": 0.8026
      }
    },
    {
      "data": {
        "id": "e2134",
        "source": "2020_marti_saumell_squash_box_feasibility_driven",
        "target": "2309_07872",
        "weight": 0.8275
      }
    },
    {
      "data": {
        "id": "e2135",
        "source": "2020_marti_saumell_squash_box_feasibility_driven",
        "target": "2103_03293",
        "weight": 0.8222
      }
    },
    {
      "data": {
        "id": "e2136",
        "source": "2020_marti_saumell_squash_box_feasibility_driven",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8157
      }
    },
    {
      "data": {
        "id": "e2137",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2411_15651",
        "weight": 0.8139
      }
    },
    {
      "data": {
        "id": "e2138",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2021_li_sliding_window_informed_rrt",
        "weight": 0.8878
      }
    },
    {
      "data": {
        "id": "e2139",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2411_17902",
        "weight": 0.8579
      }
    },
    {
      "data": {
        "id": "e2140",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2502_09556",
        "weight": 0.8006
      }
    },
    {
      "data": {
        "id": "e2141",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2503_06757",
        "weight": 0.8265
      }
    },
    {
      "data": {
        "id": "e2142",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2503_16164",
        "weight": 0.8687
      }
    },
    {
      "data": {
        "id": "e2143",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2203_01751",
        "weight": 0.8041
      }
    },
    {
      "data": {
        "id": "e2144",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2203_02176",
        "weight": 0.8516
      }
    },
    {
      "data": {
        "id": "e2145",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2505_10542",
        "weight": 0.8605
      }
    },
    {
      "data": {
        "id": "e2146",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2508_21001",
        "weight": 0.8038
      }
    },
    {
      "data": {
        "id": "e2147",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2301_13143",
        "weight": 0.8387
      }
    },
    {
      "data": {
        "id": "e2148",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2302_11670",
        "weight": 0.8262
      }
    },
    {
      "data": {
        "id": "e2149",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2510_21074",
        "weight": 0.8201
      }
    },
    {
      "data": {
        "id": "e2150",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2309_14595",
        "weight": 0.8735
      }
    },
    {
      "data": {
        "id": "e2151",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2403_01194",
        "weight": 0.8167
      }
    },
    {
      "data": {
        "id": "e2152",
        "source": "2020_mashayekhi_informed_rrt_star_connect",
        "target": "2403_10745",
        "weight": 0.8423
      }
    },
    {
      "data": {
        "id": "e2153",
        "source": "2020_pellegrini_a_multiple_shooting_differential",
        "target": "2109_07081",
        "weight": 0.8193
      }
    },
    {
      "data": {
        "id": "e2154",
        "source": "2020_pellegrini_a_multiple_shooting_differential",
        "target": "2409_11649",
        "weight": 0.8758
      }
    },
    {
      "data": {
        "id": "e2155",
        "source": "2020_pellegrini_a_multiple_shooting_differential",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.822
      }
    },
    {
      "data": {
        "id": "e2156",
        "source": "2020_pellegrini_a_multiple_shooting_differential",
        "target": "2022_houghton_path_planning_differential_dynamic",
        "weight": 0.8089
      }
    },
    {
      "data": {
        "id": "e2157",
        "source": "2020_pellegrini_a_multiple_shooting_differential",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.807
      }
    },
    {
      "data": {
        "id": "e2158",
        "source": "2020_pellegrini_a_multiple_shooting_differential",
        "target": "2024_wang_a_convergence_guaranteed_multiple",
        "weight": 0.8674
      }
    },
    {
      "data": {
        "id": "e2159",
        "source": "2020_pellegrini_a_multiple_shooting_differential",
        "target": "2403_00748",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e2160",
        "source": "2020_pellegrini_a_multiple_shooting_differential",
        "target": "2309_07872",
        "weight": 0.9185
      }
    },
    {
      "data": {
        "id": "e2161",
        "source": "2020_pellegrini_a_multiple_shooting_differential",
        "target": "2103_03293",
        "weight": 0.8362
      }
    },
    {
      "data": {
        "id": "e2162",
        "source": "2020_pellegrini_a_multiple_shooting_differential",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8258
      }
    },
    {
      "data": {
        "id": "e2163",
        "source": "2021_li_sliding_window_informed_rrt",
        "target": "2411_15651",
        "weight": 0.8187
      }
    },
    {
      "data": {
        "id": "e2164",
        "source": "2021_li_sliding_window_informed_rrt",
        "target": "2411_17902",
        "weight": 0.8021
      }
    },
    {
      "data": {
        "id": "e2165",
        "source": "2021_li_sliding_window_informed_rrt",
        "target": "2502_09556",
        "weight": 0.8165
      }
    },
    {
      "data": {
        "id": "e2166",
        "source": "2021_li_sliding_window_informed_rrt",
        "target": "2503_06757",
        "weight": 0.81
      }
    },
    {
      "data": {
        "id": "e2167",
        "source": "2021_li_sliding_window_informed_rrt",
        "target": "2201_03163",
        "weight": 0.8097
      }
    },
    {
      "data": {
        "id": "e2168",
        "source": "2021_li_sliding_window_informed_rrt",
        "target": "2503_16164",
        "weight": 0.8619
      }
    },
    {
      "data": {
        "id": "e2169",
        "source": "2021_li_sliding_window_informed_rrt",
        "target": "2203_02176",
        "weight": 0.8328
      }
    },
    {
      "data": {
        "id": "e2170",
        "source": "2021_li_sliding_window_informed_rrt",
        "target": "2505_10542",
        "weight": 0.8123
      }
    },
    {
      "data": {
        "id": "e2171",
        "source": "2021_li_sliding_window_informed_rrt",
        "target": "2301_13143",
        "weight": 0.8662
      }
    },
    {
      "data": {
        "id": "e2172",
        "source": "2021_li_sliding_window_informed_rrt",
        "target": "2302_11670",
        "weight": 0.8205
      }
    },
    {
      "data": {
        "id": "e2173",
        "source": "2021_li_sliding_window_informed_rrt",
        "target": "2510_21074",
        "weight": 0.8038
      }
    },
    {
      "data": {
        "id": "e2174",
        "source": "2021_li_sliding_window_informed_rrt",
        "target": "2309_14595",
        "weight": 0.8795
      }
    },
    {
      "data": {
        "id": "e2175",
        "source": "2021_li_sliding_window_informed_rrt",
        "target": "2403_01194",
        "weight": 0.8324
      }
    },
    {
      "data": {
        "id": "e2176",
        "source": "2021_li_sliding_window_informed_rrt",
        "target": "2403_10745",
        "weight": 0.8486
      }
    },
    {
      "data": {
        "id": "e2177",
        "source": "2101_04413",
        "target": "2502_04799",
        "weight": 0.7575
      }
    },
    {
      "data": {
        "id": "e2178",
        "source": "2101_04413",
        "target": "2208_05888",
        "weight": 0.7385
      }
    },
    {
      "data": {
        "id": "e2179",
        "source": "2101_04413",
        "target": "2112_02089",
        "weight": 0.7376
      }
    },
    {
      "data": {
        "id": "e2180",
        "source": "2101_04413",
        "target": "2410_04083",
        "weight": 0.757
      }
    },
    {
      "data": {
        "id": "e2181",
        "source": "2101_11565",
        "target": "2604_06406",
        "weight": 0.8669
      }
    },
    {
      "data": {
        "id": "e2182",
        "source": "2101_11565",
        "target": "2603_11335",
        "weight": 0.8339
      }
    },
    {
      "data": {
        "id": "e2183",
        "source": "2101_11565",
        "target": "2510_22015",
        "weight": 0.8426
      }
    },
    {
      "data": {
        "id": "e2184",
        "source": "2101_11565",
        "target": "2305_01072",
        "weight": 0.8352
      }
    },
    {
      "data": {
        "id": "e2185",
        "source": "2101_11565",
        "target": "2504_18978",
        "weight": 0.8307
      }
    },
    {
      "data": {
        "id": "e2186",
        "source": "2101_11565",
        "target": "2205_04422",
        "weight": 0.8666
      }
    },
    {
      "data": {
        "id": "e2187",
        "source": "2102_03664",
        "target": "2604_10635",
        "weight": 0.82
      }
    },
    {
      "data": {
        "id": "e2188",
        "source": "2102_03664",
        "target": "2503_00385",
        "weight": 0.8057
      }
    },
    {
      "data": {
        "id": "e2189",
        "source": "2102_03664",
        "target": "2604_21270",
        "weight": 0.8257
      }
    },
    {
      "data": {
        "id": "e2190",
        "source": "2102_03664",
        "target": "2604_24442",
        "weight": 0.8303
      }
    },
    {
      "data": {
        "id": "e2191",
        "source": "2102_03664",
        "target": "2604_00900",
        "weight": 0.806
      }
    },
    {
      "data": {
        "id": "e2192",
        "source": "2102_03861",
        "target": "2507_05331",
        "weight": 0.8137
      }
    },
    {
      "data": {
        "id": "e2193",
        "source": "2102_03861",
        "target": "2507_09061",
        "weight": 0.8084
      }
    },
    {
      "data": {
        "id": "e2194",
        "source": "2102_03861",
        "target": "2604_08508",
        "weight": 0.8037
      }
    },
    {
      "data": {
        "id": "e2195",
        "source": "2102_03861",
        "target": "2409_14562",
        "weight": 0.804
      }
    },
    {
      "data": {
        "id": "e2196",
        "source": "2102_03861",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.7975
      }
    },
    {
      "data": {
        "id": "e2197",
        "source": "2102_08302",
        "target": "2212_02603",
        "weight": 0.8261
      }
    },
    {
      "data": {
        "id": "e2198",
        "source": "2102_08302",
        "target": "2312_02758",
        "weight": 0.819
      }
    },
    {
      "data": {
        "id": "e2199",
        "source": "2102_08302",
        "target": "2203_04955",
        "weight": 0.8016
      }
    },
    {
      "data": {
        "id": "e2200",
        "source": "2102_08302",
        "target": "2603_23465",
        "weight": 0.8279
      }
    },
    {
      "data": {
        "id": "e2201",
        "source": "2102_08302",
        "target": "2203_15471",
        "weight": 0.839
      }
    },
    {
      "data": {
        "id": "e2202",
        "source": "2102_08302",
        "target": "2511_11308",
        "weight": 0.8054
      }
    },
    {
      "data": {
        "id": "e2203",
        "source": "2102_08302",
        "target": "2310_02918",
        "weight": 0.8091
      }
    },
    {
      "data": {
        "id": "e2204",
        "source": "2103_00065",
        "target": "2604_14669",
        "weight": 0.8753
      }
    },
    {
      "data": {
        "id": "e2205",
        "source": "2103_03293",
        "target": "2409_11649",
        "weight": 0.9103
      }
    },
    {
      "data": {
        "id": "e2206",
        "source": "2103_03293",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8359
      }
    },
    {
      "data": {
        "id": "e2207",
        "source": "2103_03293",
        "target": "2109_07081",
        "weight": 0.8579
      }
    },
    {
      "data": {
        "id": "e2208",
        "source": "2103_03293",
        "target": "2022_houghton_path_planning_differential_dynamic",
        "weight": 0.8101
      }
    },
    {
      "data": {
        "id": "e2209",
        "source": "2103_03293",
        "target": "2204_02322",
        "weight": 0.8259
      }
    },
    {
      "data": {
        "id": "e2210",
        "source": "2103_03293",
        "target": "2207_06362",
        "weight": 0.8183
      }
    },
    {
      "data": {
        "id": "e2211",
        "source": "2103_03293",
        "target": "2208_02439",
        "weight": 0.8041
      }
    },
    {
      "data": {
        "id": "e2212",
        "source": "2103_03293",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8691
      }
    },
    {
      "data": {
        "id": "e2213",
        "source": "2103_03293",
        "target": "2309_07872",
        "weight": 0.8556
      }
    },
    {
      "data": {
        "id": "e2214",
        "source": "2103_03293",
        "target": "2311_06404",
        "weight": 0.8078
      }
    },
    {
      "data": {
        "id": "e2215",
        "source": "2103_03293",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8571
      }
    },
    {
      "data": {
        "id": "e2216",
        "source": "2103_03293",
        "target": "2024_wang_a_convergence_guaranteed_multiple",
        "weight": 0.8297
      }
    },
    {
      "data": {
        "id": "e2217",
        "source": "2103_03293",
        "target": "2603_16059",
        "weight": 0.8084
      }
    },
    {
      "data": {
        "id": "e2218",
        "source": "2103_05478",
        "target": "2406_19617",
        "weight": 0.846
      }
    },
    {
      "data": {
        "id": "e2219",
        "source": "2103_05478",
        "target": "2503_00385",
        "weight": 0.8027
      }
    },
    {
      "data": {
        "id": "e2220",
        "source": "2103_05478",
        "target": "2410_04083",
        "weight": 0.8025
      }
    },
    {
      "data": {
        "id": "e2221",
        "source": "2103_05478",
        "target": "2604_14669",
        "weight": 0.8137
      }
    },
    {
      "data": {
        "id": "e2222",
        "source": "2103_05478",
        "target": "2202_04612",
        "weight": 0.8419
      }
    },
    {
      "data": {
        "id": "e2223",
        "source": "2103_05478",
        "target": "2506_05454",
        "weight": 0.8748
      }
    },
    {
      "data": {
        "id": "e2224",
        "source": "2103_14438",
        "target": "2304_13029",
        "weight": 0.7512
      }
    },
    {
      "data": {
        "id": "e2225",
        "source": "2103_14438",
        "target": "2202_07125",
        "weight": 0.8571
      }
    },
    {
      "data": {
        "id": "e2226",
        "source": "2103_14438",
        "target": "2308_00928",
        "weight": 0.7441
      }
    },
    {
      "data": {
        "id": "e2227",
        "source": "2103_15691",
        "target": "2410_13732",
        "weight": 0.7386
      }
    },
    {
      "data": {
        "id": "e2228",
        "source": "2103_15691",
        "target": "2304_07193",
        "weight": 0.8215
      }
    },
    {
      "data": {
        "id": "e2229",
        "source": "2103_15691",
        "target": "2207_05844",
        "weight": 0.7535
      }
    },
    {
      "data": {
        "id": "e2230",
        "source": "2104_00241",
        "target": "2602_03639",
        "weight": 0.8258
      }
    },
    {
      "data": {
        "id": "e2231",
        "source": "2104_00241",
        "target": "2212_02603",
        "weight": 0.812
      }
    },
    {
      "data": {
        "id": "e2232",
        "source": "2104_00241",
        "target": "2511_02015",
        "weight": 0.8387
      }
    },
    {
      "data": {
        "id": "e2233",
        "source": "2104_00241",
        "target": "2203_04955",
        "weight": 0.8007
      }
    },
    {
      "data": {
        "id": "e2234",
        "source": "2104_00241",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8101
      }
    },
    {
      "data": {
        "id": "e2235",
        "source": "2104_00241",
        "target": "2511_11308",
        "weight": 0.804
      }
    },
    {
      "data": {
        "id": "e2236",
        "source": "2104_00241",
        "target": "2603_24489",
        "weight": 0.842
      }
    },
    {
      "data": {
        "id": "e2237",
        "source": "2104_00241",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8297
      }
    },
    {
      "data": {
        "id": "e2238",
        "source": "2104_00241",
        "target": "2309_12566",
        "weight": 0.8549
      }
    },
    {
      "data": {
        "id": "e2239",
        "source": "2104_03186",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8018
      }
    },
    {
      "data": {
        "id": "e2240",
        "source": "2104_03186",
        "target": "2603_10711",
        "weight": 0.8012
      }
    },
    {
      "data": {
        "id": "e2241",
        "source": "2104_03186",
        "target": "2204_02322",
        "weight": 0.8129
      }
    },
    {
      "data": {
        "id": "e2242",
        "source": "2104_03186",
        "target": "2207_06362",
        "weight": 0.8028
      }
    },
    {
      "data": {
        "id": "e2243",
        "source": "2107_08086",
        "target": "2604_10635",
        "weight": 0.8399
      }
    },
    {
      "data": {
        "id": "e2244",
        "source": "2107_08086",
        "target": "2604_24442",
        "weight": 0.8022
      }
    },
    {
      "data": {
        "id": "e2245",
        "source": "2107_08086",
        "target": "2305_09619",
        "weight": 0.8043
      }
    },
    {
      "data": {
        "id": "e2246",
        "source": "2107_08086",
        "target": "2204_02322",
        "weight": 0.7953
      }
    },
    {
      "data": {
        "id": "e2247",
        "source": "2108_13404",
        "target": "2212_02603",
        "weight": 0.809
      }
    },
    {
      "data": {
        "id": "e2248",
        "source": "2108_13404",
        "target": "2111_08481",
        "weight": 0.8547
      }
    },
    {
      "data": {
        "id": "e2249",
        "source": "2108_13404",
        "target": "2203_04955",
        "weight": 0.8164
      }
    },
    {
      "data": {
        "id": "e2250",
        "source": "2108_13404",
        "target": "2412_12036",
        "weight": 0.8491
      }
    },
    {
      "data": {
        "id": "e2251",
        "source": "2108_13404",
        "target": "2403_09110",
        "weight": 0.8512
      }
    },
    {
      "data": {
        "id": "e2252",
        "source": "2109_03920",
        "target": "2506_05454",
        "weight": 0.7438
      }
    },
    {
      "data": {
        "id": "e2253",
        "source": "2109_03920",
        "target": "2403_14606",
        "weight": 0.7423
      }
    },
    {
      "data": {
        "id": "e2254",
        "source": "2109_03920",
        "target": "2506_22087",
        "weight": 0.746
      }
    },
    {
      "data": {
        "id": "e2255",
        "source": "2109_07081",
        "target": "2409_11649",
        "weight": 0.9034
      }
    },
    {
      "data": {
        "id": "e2256",
        "source": "2109_07081",
        "target": "2410_23916",
        "weight": 0.8191
      }
    },
    {
      "data": {
        "id": "e2257",
        "source": "2109_07081",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8252
      }
    },
    {
      "data": {
        "id": "e2258",
        "source": "2109_07081",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8247
      }
    },
    {
      "data": {
        "id": "e2259",
        "source": "2109_07081",
        "target": "2022_houghton_path_planning_differential_dynamic",
        "weight": 0.8225
      }
    },
    {
      "data": {
        "id": "e2260",
        "source": "2109_07081",
        "target": "2504_06437",
        "weight": 0.8132
      }
    },
    {
      "data": {
        "id": "e2261",
        "source": "2109_07081",
        "target": "2504_18978",
        "weight": 0.8235
      }
    },
    {
      "data": {
        "id": "e2262",
        "source": "2109_07081",
        "target": "2204_02322",
        "weight": 0.8403
      }
    },
    {
      "data": {
        "id": "e2263",
        "source": "2109_07081",
        "target": "2205_04422",
        "weight": 0.8269
      }
    },
    {
      "data": {
        "id": "e2264",
        "source": "2109_07081",
        "target": "2506_14865",
        "weight": 0.8123
      }
    },
    {
      "data": {
        "id": "e2265",
        "source": "2109_07081",
        "target": "2207_06362",
        "weight": 0.832
      }
    },
    {
      "data": {
        "id": "e2266",
        "source": "2109_07081",
        "target": "2208_02439",
        "weight": 0.8463
      }
    },
    {
      "data": {
        "id": "e2267",
        "source": "2109_07081",
        "target": "2209_09006",
        "weight": 0.816
      }
    },
    {
      "data": {
        "id": "e2268",
        "source": "2109_07081",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8775
      }
    },
    {
      "data": {
        "id": "e2269",
        "source": "2109_07081",
        "target": "2303_16746",
        "weight": 0.8207
      }
    },
    {
      "data": {
        "id": "e2270",
        "source": "2109_07081",
        "target": "2511_02095",
        "weight": 0.8064
      }
    },
    {
      "data": {
        "id": "e2271",
        "source": "2109_07081",
        "target": "2307_03167",
        "weight": 0.8195
      }
    },
    {
      "data": {
        "id": "e2272",
        "source": "2109_07081",
        "target": "2511_11308",
        "weight": 0.8101
      }
    },
    {
      "data": {
        "id": "e2273",
        "source": "2109_07081",
        "target": "2511_14752",
        "weight": 0.8072
      }
    },
    {
      "data": {
        "id": "e2274",
        "source": "2109_07081",
        "target": "2309_07872",
        "weight": 0.8583
      }
    },
    {
      "data": {
        "id": "e2275",
        "source": "2109_07081",
        "target": "2309_12566",
        "weight": 0.8133
      }
    },
    {
      "data": {
        "id": "e2276",
        "source": "2109_07081",
        "target": "2602_03639",
        "weight": 0.8038
      }
    },
    {
      "data": {
        "id": "e2277",
        "source": "2109_07081",
        "target": "2311_06404",
        "weight": 0.8015
      }
    },
    {
      "data": {
        "id": "e2278",
        "source": "2109_07081",
        "target": "2603_00871",
        "weight": 0.8176
      }
    },
    {
      "data": {
        "id": "e2279",
        "source": "2109_07081",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8493
      }
    },
    {
      "data": {
        "id": "e2280",
        "source": "2109_07081",
        "target": "2024_wang_a_convergence_guaranteed_multiple",
        "weight": 0.8421
      }
    },
    {
      "data": {
        "id": "e2281",
        "source": "2109_07081",
        "target": "2603_10711",
        "weight": 0.8097
      }
    },
    {
      "data": {
        "id": "e2282",
        "source": "2109_07081",
        "target": "2603_11335",
        "weight": 0.8108
      }
    },
    {
      "data": {
        "id": "e2283",
        "source": "2109_07081",
        "target": "2403_00748",
        "weight": 0.8235
      }
    },
    {
      "data": {
        "id": "e2284",
        "source": "2111_08481",
        "target": "2412_12036",
        "weight": 0.8257
      }
    },
    {
      "data": {
        "id": "e2285",
        "source": "2111_08481",
        "target": "2403_09110",
        "weight": 0.796
      }
    },
    {
      "data": {
        "id": "e2286",
        "source": "2111_12083",
        "target": "2409_09523",
        "weight": 0.8143
      }
    },
    {
      "data": {
        "id": "e2287",
        "source": "2111_12083",
        "target": "2111_12137",
        "weight": 0.889
      }
    },
    {
      "data": {
        "id": "e2288",
        "source": "2111_12083",
        "target": "2301_11902",
        "weight": 0.808
      }
    },
    {
      "data": {
        "id": "e2289",
        "source": "2111_12083",
        "target": "2511_00088",
        "weight": 0.8178
      }
    },
    {
      "data": {
        "id": "e2290",
        "source": "2111_12083",
        "target": "2505_09074",
        "weight": 0.8103
      }
    },
    {
      "data": {
        "id": "e2291",
        "source": "2111_12083",
        "target": "2310_08710",
        "weight": 0.8379
      }
    },
    {
      "data": {
        "id": "e2292",
        "source": "2111_12137",
        "target": "2310_16828",
        "weight": 0.8028
      }
    },
    {
      "data": {
        "id": "e2293",
        "source": "2111_12137",
        "target": "2604_07944",
        "weight": 0.8235
      }
    },
    {
      "data": {
        "id": "e2294",
        "source": "2111_12137",
        "target": "2409_09523",
        "weight": 0.8156
      }
    },
    {
      "data": {
        "id": "e2295",
        "source": "2111_12137",
        "target": "2301_11902",
        "weight": 0.8141
      }
    },
    {
      "data": {
        "id": "e2296",
        "source": "2111_12137",
        "target": "2511_00088",
        "weight": 0.8239
      }
    },
    {
      "data": {
        "id": "e2297",
        "source": "2111_12137",
        "target": "2412_14415",
        "weight": 0.8288
      }
    },
    {
      "data": {
        "id": "e2298",
        "source": "2111_12137",
        "target": "2412_17920",
        "weight": 0.8246
      }
    },
    {
      "data": {
        "id": "e2299",
        "source": "2111_12137",
        "target": "2206_03004",
        "weight": 0.8256
      }
    },
    {
      "data": {
        "id": "e2300",
        "source": "2111_12137",
        "target": "2310_08710",
        "weight": 0.8688
      }
    },
    {
      "data": {
        "id": "e2301",
        "source": "2112_02089",
        "target": "2208_05888",
        "weight": 0.9055
      }
    },
    {
      "data": {
        "id": "e2302",
        "source": "2112_02089",
        "target": "2502_04799",
        "weight": 0.9109
      }
    },
    {
      "data": {
        "id": "e2303",
        "source": "2112_02089",
        "target": "2311_11489",
        "weight": 0.802
      }
    },
    {
      "data": {
        "id": "e2304",
        "source": "2112_02089",
        "target": "2410_04083",
        "weight": 0.8296
      }
    },
    {
      "data": {
        "id": "e2305",
        "source": "2112_02089",
        "target": "2202_04612",
        "weight": 0.8077
      }
    },
    {
      "data": {
        "id": "e2306",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2409_12266",
        "weight": 0.8287
      }
    },
    {
      "data": {
        "id": "e2307",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2410_19414",
        "weight": 0.8767
      }
    },
    {
      "data": {
        "id": "e2308",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2411_15651",
        "weight": 0.8061
      }
    },
    {
      "data": {
        "id": "e2309",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2411_17902",
        "weight": 0.8075
      }
    },
    {
      "data": {
        "id": "e2310",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2412_11270",
        "weight": 0.807
      }
    },
    {
      "data": {
        "id": "e2311",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2503_06135",
        "weight": 0.8014
      }
    },
    {
      "data": {
        "id": "e2312",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2203_01751",
        "weight": 0.8538
      }
    },
    {
      "data": {
        "id": "e2313",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2203_02176",
        "weight": 0.8118
      }
    },
    {
      "data": {
        "id": "e2314",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2504_18978",
        "weight": 0.8198
      }
    },
    {
      "data": {
        "id": "e2315",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2204_09352",
        "weight": 0.8059
      }
    },
    {
      "data": {
        "id": "e2316",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2205_04422",
        "weight": 0.8204
      }
    },
    {
      "data": {
        "id": "e2317",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2210_01744",
        "weight": 0.8367
      }
    },
    {
      "data": {
        "id": "e2318",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2506_22087",
        "weight": 0.8042
      }
    },
    {
      "data": {
        "id": "e2319",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2508_05027",
        "weight": 0.8235
      }
    },
    {
      "data": {
        "id": "e2320",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2508_21001",
        "weight": 0.8496
      }
    },
    {
      "data": {
        "id": "e2321",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2301_13143",
        "weight": 0.8044
      }
    },
    {
      "data": {
        "id": "e2322",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2307_03167",
        "weight": 0.8029
      }
    },
    {
      "data": {
        "id": "e2323",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2511_18170",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e2324",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2309_14545",
        "weight": 0.8401
      }
    },
    {
      "data": {
        "id": "e2325",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2602_02846",
        "weight": 0.8509
      }
    },
    {
      "data": {
        "id": "e2326",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8008
      }
    },
    {
      "data": {
        "id": "e2327",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2603_16059",
        "weight": 0.8548
      }
    },
    {
      "data": {
        "id": "e2328",
        "source": "2022_honig_benchmarking_sampling_search_and",
        "target": "2403_10745",
        "weight": 0.8489
      }
    },
    {
      "data": {
        "id": "e2329",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2409_11649",
        "weight": 0.8397
      }
    },
    {
      "data": {
        "id": "e2330",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8492
      }
    },
    {
      "data": {
        "id": "e2331",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8322
      }
    },
    {
      "data": {
        "id": "e2332",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8123
      }
    },
    {
      "data": {
        "id": "e2333",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2503_11717",
        "weight": 0.8172
      }
    },
    {
      "data": {
        "id": "e2334",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2504_06437",
        "weight": 0.831
      }
    },
    {
      "data": {
        "id": "e2335",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2208_02439",
        "weight": 0.8785
      }
    },
    {
      "data": {
        "id": "e2336",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8381
      }
    },
    {
      "data": {
        "id": "e2337",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2508_21364",
        "weight": 0.8026
      }
    },
    {
      "data": {
        "id": "e2338",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2509_14978",
        "weight": 0.8146
      }
    },
    {
      "data": {
        "id": "e2339",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2301_13143",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e2340",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2510_00272",
        "weight": 0.8045
      }
    },
    {
      "data": {
        "id": "e2341",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2307_09105",
        "weight": 0.8008
      }
    },
    {
      "data": {
        "id": "e2342",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2309_07872",
        "weight": 0.8529
      }
    },
    {
      "data": {
        "id": "e2343",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2309_12566",
        "weight": 0.8313
      }
    },
    {
      "data": {
        "id": "e2344",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2602_03639",
        "weight": 0.8076
      }
    },
    {
      "data": {
        "id": "e2345",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2603_05385",
        "weight": 0.8067
      }
    },
    {
      "data": {
        "id": "e2346",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2024_wang_a_convergence_guaranteed_multiple",
        "weight": 0.8244
      }
    },
    {
      "data": {
        "id": "e2347",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2401_09241",
        "weight": 0.809
      }
    },
    {
      "data": {
        "id": "e2348",
        "source": "2022_houghton_path_planning_differential_dynamic",
        "target": "2603_24489",
        "weight": 0.8317
      }
    },
    {
      "data": {
        "id": "e2349",
        "source": "2201_02177",
        "target": "2406_16793",
        "weight": 0.7615
      }
    },
    {
      "data": {
        "id": "e2350",
        "source": "2201_03163",
        "target": "2301_13143",
        "weight": 0.8054
      }
    },
    {
      "data": {
        "id": "e2351",
        "source": "2201_03163",
        "target": "2503_16164",
        "weight": 0.8015
      }
    },
    {
      "data": {
        "id": "e2352",
        "source": "2201_03163",
        "target": "2411_15651",
        "weight": 0.805
      }
    },
    {
      "data": {
        "id": "e2353",
        "source": "2201_03163",
        "target": "2403_01194",
        "weight": 0.8267
      }
    },
    {
      "data": {
        "id": "e2354",
        "source": "2201_03163",
        "target": "2309_14595",
        "weight": 0.8158
      }
    },
    {
      "data": {
        "id": "e2355",
        "source": "2201_09104",
        "target": "2311_07411",
        "weight": 0.7976
      }
    },
    {
      "data": {
        "id": "e2356",
        "source": "2201_09104",
        "target": "2401_13662",
        "weight": 0.806
      }
    },
    {
      "data": {
        "id": "e2357",
        "source": "2201_09104",
        "target": "2202_00817",
        "weight": 0.8309
      }
    },
    {
      "data": {
        "id": "e2358",
        "source": "2201_09104",
        "target": "2511_02095",
        "weight": 0.8391
      }
    },
    {
      "data": {
        "id": "e2359",
        "source": "2202_00817",
        "target": "2602_18933",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e2360",
        "source": "2202_00817",
        "target": "2311_07411",
        "weight": 0.8005
      }
    },
    {
      "data": {
        "id": "e2361",
        "source": "2202_00817",
        "target": "2401_13662",
        "weight": 0.8104
      }
    },
    {
      "data": {
        "id": "e2362",
        "source": "2202_00817",
        "target": "2511_02095",
        "weight": 0.8213
      }
    },
    {
      "data": {
        "id": "e2363",
        "source": "2202_00817",
        "target": "2511_11131",
        "weight": 0.8012
      }
    },
    {
      "data": {
        "id": "e2364",
        "source": "2202_00817",
        "target": "2511_11308",
        "weight": 0.8325
      }
    },
    {
      "data": {
        "id": "e2365",
        "source": "2202_04612",
        "target": "2406_19617",
        "weight": 0.8103
      }
    },
    {
      "data": {
        "id": "e2366",
        "source": "2202_04612",
        "target": "2410_04083",
        "weight": 0.8124
      }
    },
    {
      "data": {
        "id": "e2367",
        "source": "2202_04612",
        "target": "2604_14669",
        "weight": 0.8023
      }
    },
    {
      "data": {
        "id": "e2368",
        "source": "2202_04612",
        "target": "2506_05454",
        "weight": 0.832
      }
    },
    {
      "data": {
        "id": "e2369",
        "source": "2202_07125",
        "target": "2304_13029",
        "weight": 0.7998
      }
    },
    {
      "data": {
        "id": "e2370",
        "source": "2202_07125",
        "target": "2308_00928",
        "weight": 0.7846
      }
    },
    {
      "data": {
        "id": "e2371",
        "source": "2203_01751",
        "target": "2204_09352",
        "weight": 0.8084
      }
    },
    {
      "data": {
        "id": "e2372",
        "source": "2203_01751",
        "target": "2205_04422",
        "weight": 0.8286
      }
    },
    {
      "data": {
        "id": "e2373",
        "source": "2203_01751",
        "target": "2205_09991",
        "weight": 0.815
      }
    },
    {
      "data": {
        "id": "e2374",
        "source": "2203_01751",
        "target": "2210_01744",
        "weight": 0.8101
      }
    },
    {
      "data": {
        "id": "e2375",
        "source": "2203_01751",
        "target": "2212_00541",
        "weight": 0.804
      }
    },
    {
      "data": {
        "id": "e2376",
        "source": "2203_01751",
        "target": "2212_02603",
        "weight": 0.8191
      }
    },
    {
      "data": {
        "id": "e2377",
        "source": "2203_01751",
        "target": "2301_13143",
        "weight": 0.8224
      }
    },
    {
      "data": {
        "id": "e2378",
        "source": "2203_01751",
        "target": "2302_11670",
        "weight": 0.8196
      }
    },
    {
      "data": {
        "id": "e2379",
        "source": "2203_01751",
        "target": "2305_01072",
        "weight": 0.8091
      }
    },
    {
      "data": {
        "id": "e2380",
        "source": "2203_01751",
        "target": "2307_03167",
        "weight": 0.8279
      }
    },
    {
      "data": {
        "id": "e2381",
        "source": "2203_01751",
        "target": "2307_09105",
        "weight": 0.8055
      }
    },
    {
      "data": {
        "id": "e2382",
        "source": "2203_01751",
        "target": "2309_12566",
        "weight": 0.8087
      }
    },
    {
      "data": {
        "id": "e2383",
        "source": "2203_01751",
        "target": "2309_14545",
        "weight": 0.8527
      }
    },
    {
      "data": {
        "id": "e2384",
        "source": "2203_01751",
        "target": "2401_09241",
        "weight": 0.8186
      }
    },
    {
      "data": {
        "id": "e2385",
        "source": "2203_01751",
        "target": "2403_10745",
        "weight": 0.8365
      }
    },
    {
      "data": {
        "id": "e2386",
        "source": "2203_01751",
        "target": "2406_02807",
        "weight": 0.8129
      }
    },
    {
      "data": {
        "id": "e2387",
        "source": "2203_01751",
        "target": "2409_12266",
        "weight": 0.8289
      }
    },
    {
      "data": {
        "id": "e2388",
        "source": "2203_01751",
        "target": "2409_16012",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e2389",
        "source": "2203_01751",
        "target": "2410_16727",
        "weight": 0.801
      }
    },
    {
      "data": {
        "id": "e2390",
        "source": "2203_01751",
        "target": "2410_19414",
        "weight": 0.8697
      }
    },
    {
      "data": {
        "id": "e2391",
        "source": "2203_01751",
        "target": "2411_15651",
        "weight": 0.8326
      }
    },
    {
      "data": {
        "id": "e2392",
        "source": "2203_01751",
        "target": "2411_17902",
        "weight": 0.8385
      }
    },
    {
      "data": {
        "id": "e2393",
        "source": "2203_01751",
        "target": "2412_11270",
        "weight": 0.8299
      }
    },
    {
      "data": {
        "id": "e2394",
        "source": "2203_01751",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8034
      }
    },
    {
      "data": {
        "id": "e2395",
        "source": "2203_01751",
        "target": "2503_05819",
        "weight": 0.8039
      }
    },
    {
      "data": {
        "id": "e2396",
        "source": "2203_01751",
        "target": "2503_06135",
        "weight": 0.8073
      }
    },
    {
      "data": {
        "id": "e2397",
        "source": "2203_01751",
        "target": "2503_16164",
        "weight": 0.8239
      }
    },
    {
      "data": {
        "id": "e2398",
        "source": "2203_01751",
        "target": "2504_18978",
        "weight": 0.8194
      }
    },
    {
      "data": {
        "id": "e2399",
        "source": "2203_01751",
        "target": "2506_22087",
        "weight": 0.801
      }
    },
    {
      "data": {
        "id": "e2400",
        "source": "2203_01751",
        "target": "2507_19652",
        "weight": 0.8359
      }
    },
    {
      "data": {
        "id": "e2401",
        "source": "2203_01751",
        "target": "2508_21001",
        "weight": 0.8499
      }
    },
    {
      "data": {
        "id": "e2402",
        "source": "2203_01751",
        "target": "2508_21800",
        "weight": 0.822
      }
    },
    {
      "data": {
        "id": "e2403",
        "source": "2203_01751",
        "target": "2510_21074",
        "weight": 0.8036
      }
    },
    {
      "data": {
        "id": "e2404",
        "source": "2203_01751",
        "target": "2511_02015",
        "weight": 0.8096
      }
    },
    {
      "data": {
        "id": "e2405",
        "source": "2203_01751",
        "target": "2511_14752",
        "weight": 0.8041
      }
    },
    {
      "data": {
        "id": "e2406",
        "source": "2203_01751",
        "target": "2602_00992",
        "weight": 0.8206
      }
    },
    {
      "data": {
        "id": "e2407",
        "source": "2203_01751",
        "target": "2602_02846",
        "weight": 0.8585
      }
    },
    {
      "data": {
        "id": "e2408",
        "source": "2203_01751",
        "target": "2602_03639",
        "weight": 0.8146
      }
    },
    {
      "data": {
        "id": "e2409",
        "source": "2203_01751",
        "target": "2603_05385",
        "weight": 0.8281
      }
    },
    {
      "data": {
        "id": "e2410",
        "source": "2203_01751",
        "target": "2603_06773",
        "weight": 0.8181
      }
    },
    {
      "data": {
        "id": "e2411",
        "source": "2203_01751",
        "target": "2603_12361",
        "weight": 0.8007
      }
    },
    {
      "data": {
        "id": "e2412",
        "source": "2203_01751",
        "target": "2603_16059",
        "weight": 0.8241
      }
    },
    {
      "data": {
        "id": "e2413",
        "source": "2203_01751",
        "target": "2603_24489",
        "weight": 0.833
      }
    },
    {
      "data": {
        "id": "e2414",
        "source": "2203_01751",
        "target": "2604_12149",
        "weight": 0.8177
      }
    },
    {
      "data": {
        "id": "e2415",
        "source": "2203_01751",
        "target": "2604_14026",
        "weight": 0.8127
      }
    },
    {
      "data": {
        "id": "e2416",
        "source": "2203_02176",
        "target": "2410_19414",
        "weight": 0.8056
      }
    },
    {
      "data": {
        "id": "e2417",
        "source": "2203_02176",
        "target": "2502_09556",
        "weight": 0.8
      }
    },
    {
      "data": {
        "id": "e2418",
        "source": "2203_02176",
        "target": "2503_06757",
        "weight": 0.8033
      }
    },
    {
      "data": {
        "id": "e2419",
        "source": "2203_02176",
        "target": "2503_16164",
        "weight": 0.8416
      }
    },
    {
      "data": {
        "id": "e2420",
        "source": "2203_02176",
        "target": "2505_10542",
        "weight": 0.8375
      }
    },
    {
      "data": {
        "id": "e2421",
        "source": "2203_02176",
        "target": "2301_13143",
        "weight": 0.8079
      }
    },
    {
      "data": {
        "id": "e2422",
        "source": "2203_02176",
        "target": "2511_18170",
        "weight": 0.8
      }
    },
    {
      "data": {
        "id": "e2423",
        "source": "2203_02176",
        "target": "2309_14595",
        "weight": 0.8208
      }
    },
    {
      "data": {
        "id": "e2424",
        "source": "2203_02176",
        "target": "2403_10745",
        "weight": 0.8214
      }
    },
    {
      "data": {
        "id": "e2425",
        "source": "2203_04955",
        "target": "2604_12149",
        "weight": 0.805
      }
    },
    {
      "data": {
        "id": "e2426",
        "source": "2203_04955",
        "target": "2410_23916",
        "weight": 0.8418
      }
    },
    {
      "data": {
        "id": "e2427",
        "source": "2203_04955",
        "target": "2411_15651",
        "weight": 0.8089
      }
    },
    {
      "data": {
        "id": "e2428",
        "source": "2203_04955",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8736
      }
    },
    {
      "data": {
        "id": "e2429",
        "source": "2203_04955",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8122
      }
    },
    {
      "data": {
        "id": "e2430",
        "source": "2203_04955",
        "target": "2203_15471",
        "weight": 0.8029
      }
    },
    {
      "data": {
        "id": "e2431",
        "source": "2203_04955",
        "target": "2205_09991",
        "weight": 0.8256
      }
    },
    {
      "data": {
        "id": "e2432",
        "source": "2203_04955",
        "target": "2212_02603",
        "weight": 0.8854
      }
    },
    {
      "data": {
        "id": "e2433",
        "source": "2203_04955",
        "target": "2511_00814",
        "weight": 0.8127
      }
    },
    {
      "data": {
        "id": "e2434",
        "source": "2203_04955",
        "target": "2305_09619",
        "weight": 0.8275
      }
    },
    {
      "data": {
        "id": "e2435",
        "source": "2203_04955",
        "target": "2306_09852",
        "weight": 0.8187
      }
    },
    {
      "data": {
        "id": "e2436",
        "source": "2203_04955",
        "target": "2511_11308",
        "weight": 0.8529
      }
    },
    {
      "data": {
        "id": "e2437",
        "source": "2203_04955",
        "target": "2309_12566",
        "weight": 0.8076
      }
    },
    {
      "data": {
        "id": "e2438",
        "source": "2203_04955",
        "target": "2310_02918",
        "weight": 0.827
      }
    },
    {
      "data": {
        "id": "e2439",
        "source": "2203_04955",
        "target": "2310_16828",
        "weight": 0.8826
      }
    },
    {
      "data": {
        "id": "e2440",
        "source": "2203_04955",
        "target": "2602_03639",
        "weight": 0.8136
      }
    },
    {
      "data": {
        "id": "e2441",
        "source": "2203_04955",
        "target": "2603_05385",
        "weight": 0.8158
      }
    },
    {
      "data": {
        "id": "e2442",
        "source": "2203_04955",
        "target": "2603_23465",
        "weight": 0.8121
      }
    },
    {
      "data": {
        "id": "e2443",
        "source": "2203_04955",
        "target": "2603_24489",
        "weight": 0.8247
      }
    },
    {
      "data": {
        "id": "e2444",
        "source": "2203_04955",
        "target": "2604_00900",
        "weight": 0.8057
      }
    },
    {
      "data": {
        "id": "e2445",
        "source": "2203_04955",
        "target": "2604_01477",
        "weight": 0.8233
      }
    },
    {
      "data": {
        "id": "e2446",
        "source": "2203_11419",
        "target": "2604_23951",
        "weight": 0.7475
      }
    },
    {
      "data": {
        "id": "e2447",
        "source": "2203_11419",
        "target": "2511_10622",
        "weight": 0.741
      }
    },
    {
      "data": {
        "id": "e2448",
        "source": "2203_11419",
        "target": "2506_11513",
        "weight": 0.8803
      }
    },
    {
      "data": {
        "id": "e2449",
        "source": "2203_15471",
        "target": "2312_02758",
        "weight": 0.8603
      }
    },
    {
      "data": {
        "id": "e2450",
        "source": "2203_15471",
        "target": "2504_01766",
        "weight": 0.8014
      }
    },
    {
      "data": {
        "id": "e2451",
        "source": "2203_15471",
        "target": "2603_23465",
        "weight": 0.8533
      }
    },
    {
      "data": {
        "id": "e2452",
        "source": "2204_02322",
        "target": "2409_11649",
        "weight": 0.8434
      }
    },
    {
      "data": {
        "id": "e2453",
        "source": "2204_02322",
        "target": "2604_10635",
        "weight": 0.8497
      }
    },
    {
      "data": {
        "id": "e2454",
        "source": "2204_02322",
        "target": "2604_24442",
        "weight": 0.8074
      }
    },
    {
      "data": {
        "id": "e2455",
        "source": "2204_02322",
        "target": "2503_00385",
        "weight": 0.8233
      }
    },
    {
      "data": {
        "id": "e2456",
        "source": "2204_02322",
        "target": "2503_24371",
        "weight": 0.819
      }
    },
    {
      "data": {
        "id": "e2457",
        "source": "2204_02322",
        "target": "2207_06362",
        "weight": 0.9006
      }
    },
    {
      "data": {
        "id": "e2458",
        "source": "2204_02322",
        "target": "2212_02603",
        "weight": 0.8029
      }
    },
    {
      "data": {
        "id": "e2459",
        "source": "2204_02322",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8217
      }
    },
    {
      "data": {
        "id": "e2460",
        "source": "2204_02322",
        "target": "2304_00346",
        "weight": 0.8041
      }
    },
    {
      "data": {
        "id": "e2461",
        "source": "2204_02322",
        "target": "2511_02095",
        "weight": 0.8489
      }
    },
    {
      "data": {
        "id": "e2462",
        "source": "2204_02322",
        "target": "2305_09619",
        "weight": 0.8594
      }
    },
    {
      "data": {
        "id": "e2463",
        "source": "2204_02322",
        "target": "2511_11131",
        "weight": 0.8373
      }
    },
    {
      "data": {
        "id": "e2464",
        "source": "2204_02322",
        "target": "2511_11308",
        "weight": 0.815
      }
    },
    {
      "data": {
        "id": "e2465",
        "source": "2204_02322",
        "target": "2309_07872",
        "weight": 0.8099
      }
    },
    {
      "data": {
        "id": "e2466",
        "source": "2204_02322",
        "target": "2311_06404",
        "weight": 0.8187
      }
    },
    {
      "data": {
        "id": "e2467",
        "source": "2204_02322",
        "target": "2311_11166",
        "weight": 0.8131
      }
    },
    {
      "data": {
        "id": "e2468",
        "source": "2204_02322",
        "target": "2602_03639",
        "weight": 0.8075
      }
    },
    {
      "data": {
        "id": "e2469",
        "source": "2204_02322",
        "target": "2602_18933",
        "weight": 0.8472
      }
    },
    {
      "data": {
        "id": "e2470",
        "source": "2204_02322",
        "target": "2603_04843",
        "weight": 0.8185
      }
    },
    {
      "data": {
        "id": "e2471",
        "source": "2204_02322",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8081
      }
    },
    {
      "data": {
        "id": "e2472",
        "source": "2204_02322",
        "target": "2603_14197",
        "weight": 0.8061
      }
    },
    {
      "data": {
        "id": "e2473",
        "source": "2204_02322",
        "target": "2403_00748",
        "weight": 0.8832
      }
    },
    {
      "data": {
        "id": "e2474",
        "source": "2204_02322",
        "target": "2603_24489",
        "weight": 0.8239
      }
    },
    {
      "data": {
        "id": "e2475",
        "source": "2204_02322",
        "target": "2604_05088",
        "weight": 0.8045
      }
    },
    {
      "data": {
        "id": "e2476",
        "source": "2204_07319",
        "target": "2601_15006",
        "weight": 0.7958
      }
    },
    {
      "data": {
        "id": "e2477",
        "source": "2204_07319",
        "target": "2025_trevisan_model_predictive_path_integral",
        "weight": 0.8017
      }
    },
    {
      "data": {
        "id": "e2478",
        "source": "2204_09352",
        "target": "2604_13323",
        "weight": 0.8138
      }
    },
    {
      "data": {
        "id": "e2479",
        "source": "2204_09352",
        "target": "2410_19414",
        "weight": 0.8329
      }
    },
    {
      "data": {
        "id": "e2480",
        "source": "2204_09352",
        "target": "2504_18978",
        "weight": 0.8121
      }
    },
    {
      "data": {
        "id": "e2481",
        "source": "2204_09352",
        "target": "2205_04422",
        "weight": 0.8616
      }
    },
    {
      "data": {
        "id": "e2482",
        "source": "2204_09352",
        "target": "2506_14865",
        "weight": 0.8256
      }
    },
    {
      "data": {
        "id": "e2483",
        "source": "2204_09352",
        "target": "2208_02439",
        "weight": 0.8165
      }
    },
    {
      "data": {
        "id": "e2484",
        "source": "2204_09352",
        "target": "2305_01072",
        "weight": 0.8328
      }
    },
    {
      "data": {
        "id": "e2485",
        "source": "2204_09352",
        "target": "2309_14545",
        "weight": 0.8151
      }
    },
    {
      "data": {
        "id": "e2486",
        "source": "2204_09352",
        "target": "2310_17274",
        "weight": 0.8112
      }
    },
    {
      "data": {
        "id": "e2487",
        "source": "2204_09352",
        "target": "2604_01614",
        "weight": 0.8075
      }
    },
    {
      "data": {
        "id": "e2488",
        "source": "2204_09352",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.81
      }
    },
    {
      "data": {
        "id": "e2489",
        "source": "2204_09352",
        "target": "2603_16059",
        "weight": 0.8267
      }
    },
    {
      "data": {
        "id": "e2490",
        "source": "2204_09352",
        "target": "2403_10745",
        "weight": 0.8216
      }
    },
    {
      "data": {
        "id": "e2491",
        "source": "2204_09352",
        "target": "2406_02807",
        "weight": 0.8555
      }
    },
    {
      "data": {
        "id": "e2492",
        "source": "2205_04422",
        "target": "2409_12266",
        "weight": 0.811
      }
    },
    {
      "data": {
        "id": "e2493",
        "source": "2205_04422",
        "target": "2604_12149",
        "weight": 0.8012
      }
    },
    {
      "data": {
        "id": "e2494",
        "source": "2205_04422",
        "target": "2604_13323",
        "weight": 0.8215
      }
    },
    {
      "data": {
        "id": "e2495",
        "source": "2205_04422",
        "target": "2410_19414",
        "weight": 0.818
      }
    },
    {
      "data": {
        "id": "e2496",
        "source": "2205_04422",
        "target": "2412_11270",
        "weight": 0.8141
      }
    },
    {
      "data": {
        "id": "e2497",
        "source": "2205_04422",
        "target": "2503_16164",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e2498",
        "source": "2205_04422",
        "target": "2504_06437",
        "weight": 0.8238
      }
    },
    {
      "data": {
        "id": "e2499",
        "source": "2205_04422",
        "target": "2504_18978",
        "weight": 0.9109
      }
    },
    {
      "data": {
        "id": "e2500",
        "source": "2205_04422",
        "target": "2506_14865",
        "weight": 0.8376
      }
    },
    {
      "data": {
        "id": "e2501",
        "source": "2205_04422",
        "target": "2208_02439",
        "weight": 0.8219
      }
    },
    {
      "data": {
        "id": "e2502",
        "source": "2205_04422",
        "target": "2506_22087",
        "weight": 0.8014
      }
    },
    {
      "data": {
        "id": "e2503",
        "source": "2205_04422",
        "target": "2508_21001",
        "weight": 0.8106
      }
    },
    {
      "data": {
        "id": "e2504",
        "source": "2205_04422",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8232
      }
    },
    {
      "data": {
        "id": "e2505",
        "source": "2205_04422",
        "target": "2303_16746",
        "weight": 0.8023
      }
    },
    {
      "data": {
        "id": "e2506",
        "source": "2205_04422",
        "target": "2510_22015",
        "weight": 0.8465
      }
    },
    {
      "data": {
        "id": "e2507",
        "source": "2205_04422",
        "target": "2305_01072",
        "weight": 0.8794
      }
    },
    {
      "data": {
        "id": "e2508",
        "source": "2205_04422",
        "target": "2307_03167",
        "weight": 0.8305
      }
    },
    {
      "data": {
        "id": "e2509",
        "source": "2205_04422",
        "target": "2511_18170",
        "weight": 0.817
      }
    },
    {
      "data": {
        "id": "e2510",
        "source": "2205_04422",
        "target": "2602_00992",
        "weight": 0.8277
      }
    },
    {
      "data": {
        "id": "e2511",
        "source": "2205_04422",
        "target": "2603_00871",
        "weight": 0.8191
      }
    },
    {
      "data": {
        "id": "e2512",
        "source": "2205_04422",
        "target": "2604_01614",
        "weight": 0.8588
      }
    },
    {
      "data": {
        "id": "e2513",
        "source": "2205_04422",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8138
      }
    },
    {
      "data": {
        "id": "e2514",
        "source": "2205_04422",
        "target": "2603_10711",
        "weight": 0.8142
      }
    },
    {
      "data": {
        "id": "e2515",
        "source": "2205_04422",
        "target": "2603_11335",
        "weight": 0.8506
      }
    },
    {
      "data": {
        "id": "e2516",
        "source": "2205_04422",
        "target": "2603_12361",
        "weight": 0.8117
      }
    },
    {
      "data": {
        "id": "e2517",
        "source": "2205_04422",
        "target": "2603_16059",
        "weight": 0.8114
      }
    },
    {
      "data": {
        "id": "e2518",
        "source": "2205_04422",
        "target": "2603_24489",
        "weight": 0.809
      }
    },
    {
      "data": {
        "id": "e2519",
        "source": "2205_04422",
        "target": "2403_10745",
        "weight": 0.8002
      }
    },
    {
      "data": {
        "id": "e2520",
        "source": "2205_04422",
        "target": "2405_03281",
        "weight": 0.8405
      }
    },
    {
      "data": {
        "id": "e2521",
        "source": "2205_04422",
        "target": "2406_02807",
        "weight": 0.8158
      }
    },
    {
      "data": {
        "id": "e2522",
        "source": "2205_04422",
        "target": "2406_05846",
        "weight": 0.8154
      }
    },
    {
      "data": {
        "id": "e2523",
        "source": "2205_09991",
        "target": "2407_15007",
        "weight": 0.8074
      }
    },
    {
      "data": {
        "id": "e2524",
        "source": "2205_09991",
        "target": "2409_09523",
        "weight": 0.8075
      }
    },
    {
      "data": {
        "id": "e2525",
        "source": "2205_09991",
        "target": "2604_07944",
        "weight": 0.8158
      }
    },
    {
      "data": {
        "id": "e2526",
        "source": "2205_09991",
        "target": "2409_12266",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e2527",
        "source": "2205_09991",
        "target": "2604_12149",
        "weight": 0.8223
      }
    },
    {
      "data": {
        "id": "e2528",
        "source": "2205_09991",
        "target": "2409_15610",
        "weight": 0.8268
      }
    },
    {
      "data": {
        "id": "e2529",
        "source": "2205_09991",
        "target": "2409_16012",
        "weight": 0.8363
      }
    },
    {
      "data": {
        "id": "e2530",
        "source": "2205_09991",
        "target": "2410_16727",
        "weight": 0.8235
      }
    },
    {
      "data": {
        "id": "e2531",
        "source": "2205_09991",
        "target": "2410_19414",
        "weight": 0.8081
      }
    },
    {
      "data": {
        "id": "e2532",
        "source": "2205_09991",
        "target": "2410_23916",
        "weight": 0.812
      }
    },
    {
      "data": {
        "id": "e2533",
        "source": "2205_09991",
        "target": "2411_17293",
        "weight": 0.8064
      }
    },
    {
      "data": {
        "id": "e2534",
        "source": "2205_09991",
        "target": "2412_11270",
        "weight": 0.8269
      }
    },
    {
      "data": {
        "id": "e2535",
        "source": "2205_09991",
        "target": "2412_14415",
        "weight": 0.8023
      }
    },
    {
      "data": {
        "id": "e2536",
        "source": "2205_09991",
        "target": "2412_17920",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e2537",
        "source": "2205_09991",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8204
      }
    },
    {
      "data": {
        "id": "e2538",
        "source": "2205_09991",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8009
      }
    },
    {
      "data": {
        "id": "e2539",
        "source": "2205_09991",
        "target": "2503_00385",
        "weight": 0.8006
      }
    },
    {
      "data": {
        "id": "e2540",
        "source": "2205_09991",
        "target": "2503_05819",
        "weight": 0.8226
      }
    },
    {
      "data": {
        "id": "e2541",
        "source": "2205_09991",
        "target": "2503_06135",
        "weight": 0.8248
      }
    },
    {
      "data": {
        "id": "e2542",
        "source": "2205_09991",
        "target": "2503_09722",
        "weight": 0.8037
      }
    },
    {
      "data": {
        "id": "e2543",
        "source": "2205_09991",
        "target": "2505_21851",
        "weight": 0.8276
      }
    },
    {
      "data": {
        "id": "e2544",
        "source": "2205_09991",
        "target": "2507_05331",
        "weight": 0.807
      }
    },
    {
      "data": {
        "id": "e2545",
        "source": "2205_09991",
        "target": "2209_09006",
        "weight": 0.8263
      }
    },
    {
      "data": {
        "id": "e2546",
        "source": "2205_09991",
        "target": "2212_02603",
        "weight": 0.8662
      }
    },
    {
      "data": {
        "id": "e2547",
        "source": "2205_09991",
        "target": "2508_21001",
        "weight": 0.8487
      }
    },
    {
      "data": {
        "id": "e2548",
        "source": "2205_09991",
        "target": "2508_21800",
        "weight": 0.8732
      }
    },
    {
      "data": {
        "id": "e2549",
        "source": "2205_09991",
        "target": "2301_11902",
        "weight": 0.8251
      }
    },
    {
      "data": {
        "id": "e2550",
        "source": "2205_09991",
        "target": "2509_21961",
        "weight": 0.8213
      }
    },
    {
      "data": {
        "id": "e2551",
        "source": "2205_09991",
        "target": "2303_04137",
        "weight": 0.8559
      }
    },
    {
      "data": {
        "id": "e2552",
        "source": "2205_09991",
        "target": "2511_02015",
        "weight": 0.8154
      }
    },
    {
      "data": {
        "id": "e2553",
        "source": "2205_09991",
        "target": "2305_09619",
        "weight": 0.8097
      }
    },
    {
      "data": {
        "id": "e2554",
        "source": "2205_09991",
        "target": "2511_11131",
        "weight": 0.8134
      }
    },
    {
      "data": {
        "id": "e2555",
        "source": "2205_09991",
        "target": "2307_03167",
        "weight": 0.8199
      }
    },
    {
      "data": {
        "id": "e2556",
        "source": "2205_09991",
        "target": "2511_11308",
        "weight": 0.8356
      }
    },
    {
      "data": {
        "id": "e2557",
        "source": "2205_09991",
        "target": "2512_01809",
        "weight": 0.8321
      }
    },
    {
      "data": {
        "id": "e2558",
        "source": "2205_09991",
        "target": "2309_12566",
        "weight": 0.8333
      }
    },
    {
      "data": {
        "id": "e2559",
        "source": "2205_09991",
        "target": "2310_16828",
        "weight": 0.8367
      }
    },
    {
      "data": {
        "id": "e2560",
        "source": "2205_09991",
        "target": "2602_03639",
        "weight": 0.8115
      }
    },
    {
      "data": {
        "id": "e2561",
        "source": "2205_09991",
        "target": "2603_06773",
        "weight": 0.8346
      }
    },
    {
      "data": {
        "id": "e2562",
        "source": "2205_09991",
        "target": "2401_09241",
        "weight": 0.8139
      }
    },
    {
      "data": {
        "id": "e2563",
        "source": "2205_09991",
        "target": "2401_13662",
        "weight": 0.8047
      }
    },
    {
      "data": {
        "id": "e2564",
        "source": "2205_09991",
        "target": "2603_14197",
        "weight": 0.8102
      }
    },
    {
      "data": {
        "id": "e2565",
        "source": "2205_09991",
        "target": "2603_19968",
        "weight": 0.8313
      }
    },
    {
      "data": {
        "id": "e2566",
        "source": "2205_09991",
        "target": "2603_24489",
        "weight": 0.8218
      }
    },
    {
      "data": {
        "id": "e2567",
        "source": "2205_09991",
        "target": "2604_01477",
        "weight": 0.8496
      }
    },
    {
      "data": {
        "id": "e2568",
        "source": "2205_09991",
        "target": "2604_04539",
        "weight": 0.804
      }
    },
    {
      "data": {
        "id": "e2569",
        "source": "2206_03004",
        "target": "2604_07944",
        "weight": 0.8356
      }
    },
    {
      "data": {
        "id": "e2570",
        "source": "2206_03004",
        "target": "2409_09523",
        "weight": 0.8555
      }
    },
    {
      "data": {
        "id": "e2571",
        "source": "2206_03004",
        "target": "2503_03262",
        "weight": 0.8159
      }
    },
    {
      "data": {
        "id": "e2572",
        "source": "2206_03004",
        "target": "2301_11902",
        "weight": 0.8243
      }
    },
    {
      "data": {
        "id": "e2573",
        "source": "2206_03004",
        "target": "2509_21961",
        "weight": 0.8344
      }
    },
    {
      "data": {
        "id": "e2574",
        "source": "2206_03004",
        "target": "2303_09824",
        "weight": 0.8372
      }
    },
    {
      "data": {
        "id": "e2575",
        "source": "2206_03004",
        "target": "2511_00088",
        "weight": 0.8274
      }
    },
    {
      "data": {
        "id": "e2576",
        "source": "2206_03004",
        "target": "2505_09074",
        "weight": 0.8033
      }
    },
    {
      "data": {
        "id": "e2577",
        "source": "2206_03004",
        "target": "2412_14415",
        "weight": 0.8387
      }
    },
    {
      "data": {
        "id": "e2578",
        "source": "2206_03004",
        "target": "2310_08710",
        "weight": 0.8345
      }
    },
    {
      "data": {
        "id": "e2579",
        "source": "2207_05844",
        "target": "2412_14415",
        "weight": 0.8404
      }
    },
    {
      "data": {
        "id": "e2580",
        "source": "2207_05844",
        "target": "2502_08664",
        "weight": 0.854
      }
    },
    {
      "data": {
        "id": "e2581",
        "source": "2207_05844",
        "target": "2409_09523",
        "weight": 0.8163
      }
    },
    {
      "data": {
        "id": "e2582",
        "source": "2207_05844",
        "target": "2604_07944",
        "weight": 0.8022
      }
    },
    {
      "data": {
        "id": "e2583",
        "source": "2207_05844",
        "target": "2503_03262",
        "weight": 0.8391
      }
    },
    {
      "data": {
        "id": "e2584",
        "source": "2207_05844",
        "target": "2604_08266",
        "weight": 0.8125
      }
    },
    {
      "data": {
        "id": "e2585",
        "source": "2207_05844",
        "target": "2024_calem_action_and_trajectory_prediction",
        "weight": 0.809
      }
    },
    {
      "data": {
        "id": "e2586",
        "source": "2207_05844",
        "target": "2303_09824",
        "weight": 0.8085
      }
    },
    {
      "data": {
        "id": "e2587",
        "source": "2207_05844",
        "target": "2511_00088",
        "weight": 0.8373
      }
    },
    {
      "data": {
        "id": "e2588",
        "source": "2207_05844",
        "target": "2505_09074",
        "weight": 0.8696
      }
    },
    {
      "data": {
        "id": "e2589",
        "source": "2207_05844",
        "target": "2310_08710",
        "weight": 0.8324
      }
    },
    {
      "data": {
        "id": "e2590",
        "source": "2207_06362",
        "target": "2409_11649",
        "weight": 0.8246
      }
    },
    {
      "data": {
        "id": "e2591",
        "source": "2207_06362",
        "target": "2604_10635",
        "weight": 0.8131
      }
    },
    {
      "data": {
        "id": "e2592",
        "source": "2207_06362",
        "target": "2410_23916",
        "weight": 0.8095
      }
    },
    {
      "data": {
        "id": "e2593",
        "source": "2207_06362",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8115
      }
    },
    {
      "data": {
        "id": "e2594",
        "source": "2207_06362",
        "target": "2511_02095",
        "weight": 0.8429
      }
    },
    {
      "data": {
        "id": "e2595",
        "source": "2207_06362",
        "target": "2305_09619",
        "weight": 0.8436
      }
    },
    {
      "data": {
        "id": "e2596",
        "source": "2207_06362",
        "target": "2306_09852",
        "weight": 0.8025
      }
    },
    {
      "data": {
        "id": "e2597",
        "source": "2207_06362",
        "target": "2511_11308",
        "weight": 0.8443
      }
    },
    {
      "data": {
        "id": "e2598",
        "source": "2207_06362",
        "target": "2602_03639",
        "weight": 0.8032
      }
    },
    {
      "data": {
        "id": "e2599",
        "source": "2207_06362",
        "target": "2311_06404",
        "weight": 0.81
      }
    },
    {
      "data": {
        "id": "e2600",
        "source": "2207_06362",
        "target": "2602_18933",
        "weight": 0.8296
      }
    },
    {
      "data": {
        "id": "e2601",
        "source": "2207_06362",
        "target": "2403_00748",
        "weight": 0.8565
      }
    },
    {
      "data": {
        "id": "e2602",
        "source": "2207_06362",
        "target": "2603_24489",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e2603",
        "source": "2208_02439",
        "target": "2409_11649",
        "weight": 0.8315
      }
    },
    {
      "data": {
        "id": "e2604",
        "source": "2208_02439",
        "target": "2409_12266",
        "weight": 0.8104
      }
    },
    {
      "data": {
        "id": "e2605",
        "source": "2208_02439",
        "target": "2409_15610",
        "weight": 0.8086
      }
    },
    {
      "data": {
        "id": "e2606",
        "source": "2208_02439",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8326
      }
    },
    {
      "data": {
        "id": "e2607",
        "source": "2208_02439",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8286
      }
    },
    {
      "data": {
        "id": "e2608",
        "source": "2208_02439",
        "target": "2025_trevisan_model_predictive_path_integral",
        "weight": 0.8142
      }
    },
    {
      "data": {
        "id": "e2609",
        "source": "2208_02439",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8003
      }
    },
    {
      "data": {
        "id": "e2610",
        "source": "2208_02439",
        "target": "2503_05819",
        "weight": 0.8116
      }
    },
    {
      "data": {
        "id": "e2611",
        "source": "2208_02439",
        "target": "2503_11717",
        "weight": 0.8186
      }
    },
    {
      "data": {
        "id": "e2612",
        "source": "2208_02439",
        "target": "2504_06437",
        "weight": 0.8473
      }
    },
    {
      "data": {
        "id": "e2613",
        "source": "2208_02439",
        "target": "2504_18978",
        "weight": 0.805
      }
    },
    {
      "data": {
        "id": "e2614",
        "source": "2208_02439",
        "target": "2506_21205",
        "weight": 0.8223
      }
    },
    {
      "data": {
        "id": "e2615",
        "source": "2208_02439",
        "target": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "weight": 0.8645
      }
    },
    {
      "data": {
        "id": "e2616",
        "source": "2208_02439",
        "target": "2508_21364",
        "weight": 0.8273
      }
    },
    {
      "data": {
        "id": "e2617",
        "source": "2208_02439",
        "target": "2301_13143",
        "weight": 0.8044
      }
    },
    {
      "data": {
        "id": "e2618",
        "source": "2208_02439",
        "target": "2510_00272",
        "weight": 0.8041
      }
    },
    {
      "data": {
        "id": "e2619",
        "source": "2208_02439",
        "target": "2511_02015",
        "weight": 0.8002
      }
    },
    {
      "data": {
        "id": "e2620",
        "source": "2208_02439",
        "target": "2307_09105",
        "weight": 0.8072
      }
    },
    {
      "data": {
        "id": "e2621",
        "source": "2208_02439",
        "target": "2309_07872",
        "weight": 0.8341
      }
    },
    {
      "data": {
        "id": "e2622",
        "source": "2208_02439",
        "target": "2309_12566",
        "weight": 0.8134
      }
    },
    {
      "data": {
        "id": "e2623",
        "source": "2208_02439",
        "target": "2602_03639",
        "weight": 0.8083
      }
    },
    {
      "data": {
        "id": "e2624",
        "source": "2208_02439",
        "target": "2603_05385",
        "weight": 0.806
      }
    },
    {
      "data": {
        "id": "e2625",
        "source": "2208_02439",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8264
      }
    },
    {
      "data": {
        "id": "e2626",
        "source": "2208_02439",
        "target": "2024_wang_a_convergence_guaranteed_multiple",
        "weight": 0.8333
      }
    },
    {
      "data": {
        "id": "e2627",
        "source": "2208_02439",
        "target": "2401_09241",
        "weight": 0.8299
      }
    },
    {
      "data": {
        "id": "e2628",
        "source": "2208_02439",
        "target": "2603_16059",
        "weight": 0.8068
      }
    },
    {
      "data": {
        "id": "e2629",
        "source": "2208_02439",
        "target": "2405_03281",
        "weight": 0.8009
      }
    },
    {
      "data": {
        "id": "e2630",
        "source": "2208_02439",
        "target": "2603_24489",
        "weight": 0.8255
      }
    },
    {
      "data": {
        "id": "e2631",
        "source": "2208_05888",
        "target": "2502_04799",
        "weight": 0.8853
      }
    },
    {
      "data": {
        "id": "e2632",
        "source": "2208_05888",
        "target": "2311_11489",
        "weight": 0.837
      }
    },
    {
      "data": {
        "id": "e2633",
        "source": "2208_05888",
        "target": "2410_04083",
        "weight": 0.854
      }
    },
    {
      "data": {
        "id": "e2634",
        "source": "2208_05888",
        "target": "2511_10626",
        "weight": 0.8005
      }
    },
    {
      "data": {
        "id": "e2635",
        "source": "2209_09006",
        "target": "2410_23916",
        "weight": 0.8059
      }
    },
    {
      "data": {
        "id": "e2636",
        "source": "2209_09006",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8039
      }
    },
    {
      "data": {
        "id": "e2637",
        "source": "2209_09006",
        "target": "2212_02603",
        "weight": 0.811
      }
    },
    {
      "data": {
        "id": "e2638",
        "source": "2209_09006",
        "target": "2511_02095",
        "weight": 0.8083
      }
    },
    {
      "data": {
        "id": "e2639",
        "source": "2209_09006",
        "target": "2305_09619",
        "weight": 0.8413
      }
    },
    {
      "data": {
        "id": "e2640",
        "source": "2209_09006",
        "target": "2511_11131",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e2641",
        "source": "2209_09006",
        "target": "2307_03167",
        "weight": 0.81
      }
    },
    {
      "data": {
        "id": "e2642",
        "source": "2209_09006",
        "target": "2511_11308",
        "weight": 0.8085
      }
    },
    {
      "data": {
        "id": "e2643",
        "source": "2209_09006",
        "target": "2309_12566",
        "weight": 0.8185
      }
    },
    {
      "data": {
        "id": "e2644",
        "source": "2209_09006",
        "target": "2310_16828",
        "weight": 0.8086
      }
    },
    {
      "data": {
        "id": "e2645",
        "source": "2209_09006",
        "target": "2311_06404",
        "weight": 0.8337
      }
    },
    {
      "data": {
        "id": "e2646",
        "source": "2209_09006",
        "target": "2602_18933",
        "weight": 0.8008
      }
    },
    {
      "data": {
        "id": "e2647",
        "source": "2209_09006",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8047
      }
    },
    {
      "data": {
        "id": "e2648",
        "source": "2209_09006",
        "target": "2401_13662",
        "weight": 0.8132
      }
    },
    {
      "data": {
        "id": "e2649",
        "source": "2210_01744",
        "target": "2505_10542",
        "weight": 0.8003
      }
    },
    {
      "data": {
        "id": "e2650",
        "source": "2210_01744",
        "target": "2508_21001",
        "weight": 0.8043
      }
    },
    {
      "data": {
        "id": "e2651",
        "source": "2210_01744",
        "target": "2301_13143",
        "weight": 0.8195
      }
    },
    {
      "data": {
        "id": "e2652",
        "source": "2210_01744",
        "target": "2603_16059",
        "weight": 0.8324
      }
    },
    {
      "data": {
        "id": "e2653",
        "source": "2210_01744",
        "target": "2403_10745",
        "weight": 0.8411
      }
    },
    {
      "data": {
        "id": "e2654",
        "source": "2212_00541",
        "target": "2502_08844",
        "weight": 0.812
      }
    },
    {
      "data": {
        "id": "e2655",
        "source": "2212_00541",
        "target": "2212_02603",
        "weight": 0.8369
      }
    },
    {
      "data": {
        "id": "e2656",
        "source": "2212_00541",
        "target": "2604_12149",
        "weight": 0.8083
      }
    },
    {
      "data": {
        "id": "e2657",
        "source": "2212_00541",
        "target": "2409_15610",
        "weight": 0.8243
      }
    },
    {
      "data": {
        "id": "e2658",
        "source": "2212_00541",
        "target": "2503_04613",
        "weight": 0.857
      }
    },
    {
      "data": {
        "id": "e2659",
        "source": "2212_00541",
        "target": "2503_05819",
        "weight": 0.8116
      }
    },
    {
      "data": {
        "id": "e2660",
        "source": "2212_00541",
        "target": "2603_05385",
        "weight": 0.8122
      }
    },
    {
      "data": {
        "id": "e2661",
        "source": "2212_00541",
        "target": "2401_09241",
        "weight": 0.8128
      }
    },
    {
      "data": {
        "id": "e2662",
        "source": "2212_00541",
        "target": "2410_23916",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e2663",
        "source": "2212_00541",
        "target": "2307_09105",
        "weight": 0.8234
      }
    },
    {
      "data": {
        "id": "e2664",
        "source": "2212_00541",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8185
      }
    },
    {
      "data": {
        "id": "e2665",
        "source": "2212_00541",
        "target": "2506_17184",
        "weight": 0.8765
      }
    },
    {
      "data": {
        "id": "e2666",
        "source": "2212_02603",
        "target": "2604_10635",
        "weight": 0.8003
      }
    },
    {
      "data": {
        "id": "e2667",
        "source": "2212_02603",
        "target": "2604_11183",
        "weight": 0.8153
      }
    },
    {
      "data": {
        "id": "e2668",
        "source": "2212_02603",
        "target": "2604_12149",
        "weight": 0.8457
      }
    },
    {
      "data": {
        "id": "e2669",
        "source": "2212_02603",
        "target": "2409_15610",
        "weight": 0.8421
      }
    },
    {
      "data": {
        "id": "e2670",
        "source": "2212_02603",
        "target": "2410_23916",
        "weight": 0.8799
      }
    },
    {
      "data": {
        "id": "e2671",
        "source": "2212_02603",
        "target": "2411_15651",
        "weight": 0.8121
      }
    },
    {
      "data": {
        "id": "e2672",
        "source": "2212_02603",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8203
      }
    },
    {
      "data": {
        "id": "e2673",
        "source": "2212_02603",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8136
      }
    },
    {
      "data": {
        "id": "e2674",
        "source": "2212_02603",
        "target": "2503_00385",
        "weight": 0.8279
      }
    },
    {
      "data": {
        "id": "e2675",
        "source": "2212_02603",
        "target": "2503_05819",
        "weight": 0.8258
      }
    },
    {
      "data": {
        "id": "e2676",
        "source": "2212_02603",
        "target": "2503_11717",
        "weight": 0.8026
      }
    },
    {
      "data": {
        "id": "e2677",
        "source": "2212_02603",
        "target": "2503_24371",
        "weight": 0.8005
      }
    },
    {
      "data": {
        "id": "e2678",
        "source": "2212_02603",
        "target": "2504_01766",
        "weight": 0.8199
      }
    },
    {
      "data": {
        "id": "e2679",
        "source": "2212_02603",
        "target": "2506_17184",
        "weight": 0.8121
      }
    },
    {
      "data": {
        "id": "e2680",
        "source": "2212_02603",
        "target": "2301_13143",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e2681",
        "source": "2212_02603",
        "target": "2511_02015",
        "weight": 0.8305
      }
    },
    {
      "data": {
        "id": "e2682",
        "source": "2212_02603",
        "target": "2305_09619",
        "weight": 0.8298
      }
    },
    {
      "data": {
        "id": "e2683",
        "source": "2212_02603",
        "target": "2306_09852",
        "weight": 0.8413
      }
    },
    {
      "data": {
        "id": "e2684",
        "source": "2212_02603",
        "target": "2307_03167",
        "weight": 0.8006
      }
    },
    {
      "data": {
        "id": "e2685",
        "source": "2212_02603",
        "target": "2511_11131",
        "weight": 0.8075
      }
    },
    {
      "data": {
        "id": "e2686",
        "source": "2212_02603",
        "target": "2511_11308",
        "weight": 0.8822
      }
    },
    {
      "data": {
        "id": "e2687",
        "source": "2212_02603",
        "target": "2309_12566",
        "weight": 0.8238
      }
    },
    {
      "data": {
        "id": "e2688",
        "source": "2212_02603",
        "target": "2310_02918",
        "weight": 0.8449
      }
    },
    {
      "data": {
        "id": "e2689",
        "source": "2212_02603",
        "target": "2310_16828",
        "weight": 0.843
      }
    },
    {
      "data": {
        "id": "e2690",
        "source": "2212_02603",
        "target": "2602_03639",
        "weight": 0.8488
      }
    },
    {
      "data": {
        "id": "e2691",
        "source": "2212_02603",
        "target": "2311_06404",
        "weight": 0.8104
      }
    },
    {
      "data": {
        "id": "e2692",
        "source": "2212_02603",
        "target": "2311_18736",
        "weight": 0.8009
      }
    },
    {
      "data": {
        "id": "e2693",
        "source": "2212_02603",
        "target": "2312_02758",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e2694",
        "source": "2212_02603",
        "target": "2603_05385",
        "weight": 0.844
      }
    },
    {
      "data": {
        "id": "e2695",
        "source": "2212_02603",
        "target": "2401_09241",
        "weight": 0.8606
      }
    },
    {
      "data": {
        "id": "e2696",
        "source": "2212_02603",
        "target": "2603_06773",
        "weight": 0.8076
      }
    },
    {
      "data": {
        "id": "e2697",
        "source": "2212_02603",
        "target": "2603_14197",
        "weight": 0.8083
      }
    },
    {
      "data": {
        "id": "e2698",
        "source": "2212_02603",
        "target": "2603_19968",
        "weight": 0.804
      }
    },
    {
      "data": {
        "id": "e2699",
        "source": "2212_02603",
        "target": "2603_23465",
        "weight": 0.8345
      }
    },
    {
      "data": {
        "id": "e2700",
        "source": "2212_02603",
        "target": "2603_24489",
        "weight": 0.8575
      }
    },
    {
      "data": {
        "id": "e2701",
        "source": "2212_02603",
        "target": "2604_00900",
        "weight": 0.8157
      }
    },
    {
      "data": {
        "id": "e2702",
        "source": "2212_02603",
        "target": "2604_01477",
        "weight": 0.8529
      }
    },
    {
      "data": {
        "id": "e2703",
        "source": "2212_06437",
        "target": "2604_07944",
        "weight": 0.8121
      }
    },
    {
      "data": {
        "id": "e2704",
        "source": "2212_06437",
        "target": "2409_09523",
        "weight": 0.8307
      }
    },
    {
      "data": {
        "id": "e2705",
        "source": "2212_06437",
        "target": "2301_11902",
        "weight": 0.8074
      }
    },
    {
      "data": {
        "id": "e2706",
        "source": "2212_06437",
        "target": "2303_09824",
        "weight": 0.8216
      }
    },
    {
      "data": {
        "id": "e2707",
        "source": "2212_06437",
        "target": "2511_00088",
        "weight": 0.8272
      }
    },
    {
      "data": {
        "id": "e2708",
        "source": "2212_06437",
        "target": "2505_09074",
        "weight": 0.8217
      }
    },
    {
      "data": {
        "id": "e2709",
        "source": "2212_06437",
        "target": "2025_hu_technically_speaking_transitioning_from",
        "weight": 0.8152
      }
    },
    {
      "data": {
        "id": "e2710",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2409_11649",
        "weight": 0.8826
      }
    },
    {
      "data": {
        "id": "e2711",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2409_15610",
        "weight": 0.8045
      }
    },
    {
      "data": {
        "id": "e2712",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2410_23916",
        "weight": 0.818
      }
    },
    {
      "data": {
        "id": "e2713",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8204
      }
    },
    {
      "data": {
        "id": "e2714",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8595
      }
    },
    {
      "data": {
        "id": "e2715",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2504_06437",
        "weight": 0.807
      }
    },
    {
      "data": {
        "id": "e2716",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2504_18978",
        "weight": 0.8214
      }
    },
    {
      "data": {
        "id": "e2717",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2506_14865",
        "weight": 0.8238
      }
    },
    {
      "data": {
        "id": "e2718",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2303_16746",
        "weight": 0.8431
      }
    },
    {
      "data": {
        "id": "e2719",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2511_14752",
        "weight": 0.8048
      }
    },
    {
      "data": {
        "id": "e2720",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2309_07872",
        "weight": 0.8685
      }
    },
    {
      "data": {
        "id": "e2721",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2311_06404",
        "weight": 0.803
      }
    },
    {
      "data": {
        "id": "e2722",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2603_00871",
        "weight": 0.836
      }
    },
    {
      "data": {
        "id": "e2723",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.9257
      }
    },
    {
      "data": {
        "id": "e2724",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2024_wang_a_convergence_guaranteed_multiple",
        "weight": 0.8483
      }
    },
    {
      "data": {
        "id": "e2725",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2603_10711",
        "weight": 0.8054
      }
    },
    {
      "data": {
        "id": "e2726",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2603_11335",
        "weight": 0.8327
      }
    },
    {
      "data": {
        "id": "e2727",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2403_00748",
        "weight": 0.8138
      }
    },
    {
      "data": {
        "id": "e2728",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2603_24489",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e2729",
        "source": "2023_jallet_proxddp_proximal_constrained_trajectory",
        "target": "2406_05846",
        "weight": 0.8166
      }
    },
    {
      "data": {
        "id": "e2730",
        "source": "2023_steinecker_a_simple_and_model",
        "target": "2405_03281",
        "weight": 0.7946
      }
    },
    {
      "data": {
        "id": "e2731",
        "source": "2301_11902",
        "target": "2604_07944",
        "weight": 0.8595
      }
    },
    {
      "data": {
        "id": "e2732",
        "source": "2301_11902",
        "target": "2409_09523",
        "weight": 0.8302
      }
    },
    {
      "data": {
        "id": "e2733",
        "source": "2301_11902",
        "target": "2411_15651",
        "weight": 0.8409
      }
    },
    {
      "data": {
        "id": "e2734",
        "source": "2301_11902",
        "target": "2412_11270",
        "weight": 0.8361
      }
    },
    {
      "data": {
        "id": "e2735",
        "source": "2301_11902",
        "target": "2412_14415",
        "weight": 0.831
      }
    },
    {
      "data": {
        "id": "e2736",
        "source": "2301_11902",
        "target": "2025_hu_technically_speaking_transitioning_from",
        "weight": 0.8139
      }
    },
    {
      "data": {
        "id": "e2737",
        "source": "2301_11902",
        "target": "2505_09074",
        "weight": 0.8264
      }
    },
    {
      "data": {
        "id": "e2738",
        "source": "2301_11902",
        "target": "2508_21001",
        "weight": 0.8465
      }
    },
    {
      "data": {
        "id": "e2739",
        "source": "2301_11902",
        "target": "2508_21800",
        "weight": 0.8411
      }
    },
    {
      "data": {
        "id": "e2740",
        "source": "2301_11902",
        "target": "2509_21961",
        "weight": 0.8005
      }
    },
    {
      "data": {
        "id": "e2741",
        "source": "2301_11902",
        "target": "2303_09824",
        "weight": 0.8229
      }
    },
    {
      "data": {
        "id": "e2742",
        "source": "2301_11902",
        "target": "2511_00088",
        "weight": 0.8167
      }
    },
    {
      "data": {
        "id": "e2743",
        "source": "2301_11902",
        "target": "2309_14595",
        "weight": 0.8143
      }
    },
    {
      "data": {
        "id": "e2744",
        "source": "2301_11902",
        "target": "2310_08710",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e2745",
        "source": "2301_11902",
        "target": "2310_16828",
        "weight": 0.8104
      }
    },
    {
      "data": {
        "id": "e2746",
        "source": "2301_11902",
        "target": "2024_calem_action_and_trajectory_prediction",
        "weight": 0.8036
      }
    },
    {
      "data": {
        "id": "e2747",
        "source": "2301_13143",
        "target": "2409_12266",
        "weight": 0.8435
      }
    },
    {
      "data": {
        "id": "e2748",
        "source": "2301_13143",
        "target": "2604_12149",
        "weight": 0.8268
      }
    },
    {
      "data": {
        "id": "e2749",
        "source": "2301_13143",
        "target": "2410_19414",
        "weight": 0.825
      }
    },
    {
      "data": {
        "id": "e2750",
        "source": "2301_13143",
        "target": "2411_15651",
        "weight": 0.8783
      }
    },
    {
      "data": {
        "id": "e2751",
        "source": "2301_13143",
        "target": "2412_11270",
        "weight": 0.8295
      }
    },
    {
      "data": {
        "id": "e2752",
        "source": "2301_13143",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8249
      }
    },
    {
      "data": {
        "id": "e2753",
        "source": "2301_13143",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8426
      }
    },
    {
      "data": {
        "id": "e2754",
        "source": "2301_13143",
        "target": "2025_trevisan_model_predictive_path_integral",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e2755",
        "source": "2301_13143",
        "target": "2502_09556",
        "weight": 0.823
      }
    },
    {
      "data": {
        "id": "e2756",
        "source": "2301_13143",
        "target": "2503_05819",
        "weight": 0.8327
      }
    },
    {
      "data": {
        "id": "e2757",
        "source": "2301_13143",
        "target": "2503_06757",
        "weight": 0.8017
      }
    },
    {
      "data": {
        "id": "e2758",
        "source": "2301_13143",
        "target": "2503_11717",
        "weight": 0.83
      }
    },
    {
      "data": {
        "id": "e2759",
        "source": "2301_13143",
        "target": "2503_16164",
        "weight": 0.8428
      }
    },
    {
      "data": {
        "id": "e2760",
        "source": "2301_13143",
        "target": "2506_21205",
        "weight": 0.824
      }
    },
    {
      "data": {
        "id": "e2761",
        "source": "2301_13143",
        "target": "2508_21001",
        "weight": 0.8215
      }
    },
    {
      "data": {
        "id": "e2762",
        "source": "2301_13143",
        "target": "2511_02015",
        "weight": 0.8259
      }
    },
    {
      "data": {
        "id": "e2763",
        "source": "2301_13143",
        "target": "2307_09105",
        "weight": 0.8255
      }
    },
    {
      "data": {
        "id": "e2764",
        "source": "2301_13143",
        "target": "2511_18170",
        "weight": 0.8016
      }
    },
    {
      "data": {
        "id": "e2765",
        "source": "2301_13143",
        "target": "2309_12566",
        "weight": 0.8455
      }
    },
    {
      "data": {
        "id": "e2766",
        "source": "2301_13143",
        "target": "2309_14595",
        "weight": 0.8369
      }
    },
    {
      "data": {
        "id": "e2767",
        "source": "2301_13143",
        "target": "2602_03639",
        "weight": 0.8228
      }
    },
    {
      "data": {
        "id": "e2768",
        "source": "2301_13143",
        "target": "2603_05385",
        "weight": 0.8102
      }
    },
    {
      "data": {
        "id": "e2769",
        "source": "2301_13143",
        "target": "2401_09241",
        "weight": 0.8503
      }
    },
    {
      "data": {
        "id": "e2770",
        "source": "2301_13143",
        "target": "2403_01194",
        "weight": 0.8295
      }
    },
    {
      "data": {
        "id": "e2771",
        "source": "2301_13143",
        "target": "2603_24489",
        "weight": 0.8372
      }
    },
    {
      "data": {
        "id": "e2772",
        "source": "2301_13143",
        "target": "2403_10745",
        "weight": 0.8581
      }
    },
    {
      "data": {
        "id": "e2773",
        "source": "2302_11670",
        "target": "2411_17902",
        "weight": 0.8199
      }
    },
    {
      "data": {
        "id": "e2774",
        "source": "2302_11670",
        "target": "2502_09556",
        "weight": 0.8225
      }
    },
    {
      "data": {
        "id": "e2775",
        "source": "2302_11670",
        "target": "2503_16164",
        "weight": 0.8091
      }
    },
    {
      "data": {
        "id": "e2776",
        "source": "2302_11670",
        "target": "2508_21001",
        "weight": 0.8014
      }
    },
    {
      "data": {
        "id": "e2777",
        "source": "2302_11670",
        "target": "2510_21074",
        "weight": 0.809
      }
    },
    {
      "data": {
        "id": "e2778",
        "source": "2302_11670",
        "target": "2309_14595",
        "weight": 0.8271
      }
    },
    {
      "data": {
        "id": "e2779",
        "source": "2303_04137",
        "target": "2507_05331",
        "weight": 0.8612
      }
    },
    {
      "data": {
        "id": "e2780",
        "source": "2303_04137",
        "target": "2507_09061",
        "weight": 0.8017
      }
    },
    {
      "data": {
        "id": "e2781",
        "source": "2303_04137",
        "target": "2409_14562",
        "weight": 0.8053
      }
    },
    {
      "data": {
        "id": "e2782",
        "source": "2303_04137",
        "target": "2503_09722",
        "weight": 0.8432
      }
    },
    {
      "data": {
        "id": "e2783",
        "source": "2303_04137",
        "target": "2511_06385",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e2784",
        "source": "2303_04137",
        "target": "2505_21851",
        "weight": 0.8821
      }
    },
    {
      "data": {
        "id": "e2785",
        "source": "2303_04137",
        "target": "2512_01809",
        "weight": 0.8475
      }
    },
    {
      "data": {
        "id": "e2786",
        "source": "2303_04137",
        "target": "2604_04539",
        "weight": 0.8234
      }
    },
    {
      "data": {
        "id": "e2787",
        "source": "2303_09824",
        "target": "2604_07944",
        "weight": 0.8231
      }
    },
    {
      "data": {
        "id": "e2788",
        "source": "2303_09824",
        "target": "2604_08266",
        "weight": 0.8039
      }
    },
    {
      "data": {
        "id": "e2789",
        "source": "2303_09824",
        "target": "2409_09523",
        "weight": 0.847
      }
    },
    {
      "data": {
        "id": "e2790",
        "source": "2303_09824",
        "target": "2025_hu_technically_speaking_transitioning_from",
        "weight": 0.8494
      }
    },
    {
      "data": {
        "id": "e2791",
        "source": "2303_09824",
        "target": "2502_08664",
        "weight": 0.8654
      }
    },
    {
      "data": {
        "id": "e2792",
        "source": "2303_09824",
        "target": "2503_03262",
        "weight": 0.8689
      }
    },
    {
      "data": {
        "id": "e2793",
        "source": "2303_09824",
        "target": "2505_09074",
        "weight": 0.8459
      }
    },
    {
      "data": {
        "id": "e2794",
        "source": "2303_09824",
        "target": "2509_21961",
        "weight": 0.8365
      }
    },
    {
      "data": {
        "id": "e2795",
        "source": "2303_09824",
        "target": "2511_00088",
        "weight": 0.8318
      }
    },
    {
      "data": {
        "id": "e2796",
        "source": "2303_09824",
        "target": "2310_08710",
        "weight": 0.8209
      }
    },
    {
      "data": {
        "id": "e2797",
        "source": "2303_09824",
        "target": "2601_14880",
        "weight": 0.8056
      }
    },
    {
      "data": {
        "id": "e2798",
        "source": "2303_09824",
        "target": "2402_01443",
        "weight": 0.8139
      }
    },
    {
      "data": {
        "id": "e2799",
        "source": "2303_09824",
        "target": "2402_03893",
        "weight": 0.8014
      }
    },
    {
      "data": {
        "id": "e2800",
        "source": "2303_16746",
        "target": "2603_00871",
        "weight": 0.8464
      }
    },
    {
      "data": {
        "id": "e2801",
        "source": "2303_16746",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8529
      }
    },
    {
      "data": {
        "id": "e2802",
        "source": "2303_16746",
        "target": "2603_10711",
        "weight": 0.8141
      }
    },
    {
      "data": {
        "id": "e2803",
        "source": "2303_16746",
        "target": "2410_23916",
        "weight": 0.803
      }
    },
    {
      "data": {
        "id": "e2804",
        "source": "2303_16746",
        "target": "2506_14865",
        "weight": 0.818
      }
    },
    {
      "data": {
        "id": "e2805",
        "source": "2303_16746",
        "target": "2406_05846",
        "weight": 0.8053
      }
    },
    {
      "data": {
        "id": "e2806",
        "source": "2304_00346",
        "target": "2503_04613",
        "weight": 0.8212
      }
    },
    {
      "data": {
        "id": "e2807",
        "source": "2304_00346",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8175
      }
    },
    {
      "data": {
        "id": "e2808",
        "source": "2304_07193",
        "target": "2604_08266",
        "weight": 0.736
      }
    },
    {
      "data": {
        "id": "e2809",
        "source": "2304_13029",
        "target": "2308_00928",
        "weight": 0.8172
      }
    },
    {
      "data": {
        "id": "e2810",
        "source": "2305_01072",
        "target": "2409_16012",
        "weight": 0.8018
      }
    },
    {
      "data": {
        "id": "e2811",
        "source": "2305_01072",
        "target": "2410_19414",
        "weight": 0.8128
      }
    },
    {
      "data": {
        "id": "e2812",
        "source": "2305_01072",
        "target": "2411_17902",
        "weight": 0.805
      }
    },
    {
      "data": {
        "id": "e2813",
        "source": "2305_01072",
        "target": "2503_16164",
        "weight": 0.8013
      }
    },
    {
      "data": {
        "id": "e2814",
        "source": "2305_01072",
        "target": "2504_18978",
        "weight": 0.8532
      }
    },
    {
      "data": {
        "id": "e2815",
        "source": "2305_01072",
        "target": "2508_21001",
        "weight": 0.8071
      }
    },
    {
      "data": {
        "id": "e2816",
        "source": "2305_01072",
        "target": "2510_22015",
        "weight": 0.8491
      }
    },
    {
      "data": {
        "id": "e2817",
        "source": "2305_01072",
        "target": "2511_18170",
        "weight": 0.8041
      }
    },
    {
      "data": {
        "id": "e2818",
        "source": "2305_01072",
        "target": "2309_14545",
        "weight": 0.8026
      }
    },
    {
      "data": {
        "id": "e2819",
        "source": "2305_01072",
        "target": "2602_02846",
        "weight": 0.8132
      }
    },
    {
      "data": {
        "id": "e2820",
        "source": "2305_01072",
        "target": "2603_11335",
        "weight": 0.8071
      }
    },
    {
      "data": {
        "id": "e2821",
        "source": "2305_01072",
        "target": "2603_12361",
        "weight": 0.827
      }
    },
    {
      "data": {
        "id": "e2822",
        "source": "2305_01072",
        "target": "2604_01614",
        "weight": 0.8357
      }
    },
    {
      "data": {
        "id": "e2823",
        "source": "2305_01072",
        "target": "2405_03281",
        "weight": 0.8357
      }
    },
    {
      "data": {
        "id": "e2824",
        "source": "2305_01072",
        "target": "2406_02807",
        "weight": 0.8308
      }
    },
    {
      "data": {
        "id": "e2825",
        "source": "2305_09619",
        "target": "2604_10635",
        "weight": 0.8133
      }
    },
    {
      "data": {
        "id": "e2826",
        "source": "2305_09619",
        "target": "2604_24442",
        "weight": 0.8115
      }
    },
    {
      "data": {
        "id": "e2827",
        "source": "2305_09619",
        "target": "2503_00385",
        "weight": 0.8282
      }
    },
    {
      "data": {
        "id": "e2828",
        "source": "2305_09619",
        "target": "2503_24371",
        "weight": 0.8129
      }
    },
    {
      "data": {
        "id": "e2829",
        "source": "2305_09619",
        "target": "2511_02095",
        "weight": 0.8386
      }
    },
    {
      "data": {
        "id": "e2830",
        "source": "2305_09619",
        "target": "2511_11131",
        "weight": 0.8335
      }
    },
    {
      "data": {
        "id": "e2831",
        "source": "2305_09619",
        "target": "2511_11308",
        "weight": 0.8219
      }
    },
    {
      "data": {
        "id": "e2832",
        "source": "2305_09619",
        "target": "2310_16828",
        "weight": 0.8081
      }
    },
    {
      "data": {
        "id": "e2833",
        "source": "2305_09619",
        "target": "2602_18933",
        "weight": 0.85
      }
    },
    {
      "data": {
        "id": "e2834",
        "source": "2305_09619",
        "target": "2603_19968",
        "weight": 0.8028
      }
    },
    {
      "data": {
        "id": "e2835",
        "source": "2305_09619",
        "target": "2403_00748",
        "weight": 0.8248
      }
    },
    {
      "data": {
        "id": "e2836",
        "source": "2305_09619",
        "target": "2603_23465",
        "weight": 0.8045
      }
    },
    {
      "data": {
        "id": "e2837",
        "source": "2305_09619",
        "target": "2403_09110",
        "weight": 0.8113
      }
    },
    {
      "data": {
        "id": "e2838",
        "source": "2305_09619",
        "target": "2604_05088",
        "weight": 0.8006
      }
    },
    {
      "data": {
        "id": "e2839",
        "source": "2305_12032",
        "target": "2409_09523",
        "weight": 0.7717
      }
    },
    {
      "data": {
        "id": "e2840",
        "source": "2305_12032",
        "target": "2310_08710",
        "weight": 0.8493
      }
    },
    {
      "data": {
        "id": "e2841",
        "source": "2306_09852",
        "target": "2409_15610",
        "weight": 0.803
      }
    },
    {
      "data": {
        "id": "e2842",
        "source": "2306_09852",
        "target": "2410_23916",
        "weight": 0.8391
      }
    },
    {
      "data": {
        "id": "e2843",
        "source": "2306_09852",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8091
      }
    },
    {
      "data": {
        "id": "e2844",
        "source": "2306_09852",
        "target": "2504_06437",
        "weight": 0.8013
      }
    },
    {
      "data": {
        "id": "e2845",
        "source": "2306_09852",
        "target": "2509_14978",
        "weight": 0.8287
      }
    },
    {
      "data": {
        "id": "e2846",
        "source": "2306_09852",
        "target": "2510_00272",
        "weight": 0.8154
      }
    },
    {
      "data": {
        "id": "e2847",
        "source": "2306_09852",
        "target": "2511_11308",
        "weight": 0.885
      }
    },
    {
      "data": {
        "id": "e2848",
        "source": "2306_09852",
        "target": "2310_16828",
        "weight": 0.8129
      }
    },
    {
      "data": {
        "id": "e2849",
        "source": "2306_09852",
        "target": "2602_03639",
        "weight": 0.8075
      }
    },
    {
      "data": {
        "id": "e2850",
        "source": "2306_09852",
        "target": "2602_19699",
        "weight": 0.8155
      }
    },
    {
      "data": {
        "id": "e2851",
        "source": "2306_09852",
        "target": "2603_05385",
        "weight": 0.8036
      }
    },
    {
      "data": {
        "id": "e2852",
        "source": "2306_09852",
        "target": "2603_10711",
        "weight": 0.8142
      }
    },
    {
      "data": {
        "id": "e2853",
        "source": "2306_09852",
        "target": "2604_01477",
        "weight": 0.8156
      }
    },
    {
      "data": {
        "id": "e2854",
        "source": "2306_13867",
        "target": "2603_23465",
        "weight": 0.7649
      }
    },
    {
      "data": {
        "id": "e2855",
        "source": "2306_13867",
        "target": "2412_12036",
        "weight": 0.8039
      }
    },
    {
      "data": {
        "id": "e2856",
        "source": "2307_03167",
        "target": "2409_12266",
        "weight": 0.8002
      }
    },
    {
      "data": {
        "id": "e2857",
        "source": "2307_03167",
        "target": "2604_11183",
        "weight": 0.826
      }
    },
    {
      "data": {
        "id": "e2858",
        "source": "2307_03167",
        "target": "2604_12149",
        "weight": 0.8487
      }
    },
    {
      "data": {
        "id": "e2859",
        "source": "2307_03167",
        "target": "2410_19414",
        "weight": 0.8247
      }
    },
    {
      "data": {
        "id": "e2860",
        "source": "2307_03167",
        "target": "2411_15651",
        "weight": 0.8041
      }
    },
    {
      "data": {
        "id": "e2861",
        "source": "2307_03167",
        "target": "2412_11270",
        "weight": 0.8078
      }
    },
    {
      "data": {
        "id": "e2862",
        "source": "2307_03167",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8063
      }
    },
    {
      "data": {
        "id": "e2863",
        "source": "2307_03167",
        "target": "2503_16164",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e2864",
        "source": "2307_03167",
        "target": "2504_06437",
        "weight": 0.8196
      }
    },
    {
      "data": {
        "id": "e2865",
        "source": "2307_03167",
        "target": "2504_18978",
        "weight": 0.8029
      }
    },
    {
      "data": {
        "id": "e2866",
        "source": "2307_03167",
        "target": "2506_21205",
        "weight": 0.851
      }
    },
    {
      "data": {
        "id": "e2867",
        "source": "2307_03167",
        "target": "2506_22087",
        "weight": 0.8252
      }
    },
    {
      "data": {
        "id": "e2868",
        "source": "2307_03167",
        "target": "2508_21001",
        "weight": 0.8013
      }
    },
    {
      "data": {
        "id": "e2869",
        "source": "2307_03167",
        "target": "2510_00272",
        "weight": 0.8058
      }
    },
    {
      "data": {
        "id": "e2870",
        "source": "2307_03167",
        "target": "2511_18170",
        "weight": 0.8302
      }
    },
    {
      "data": {
        "id": "e2871",
        "source": "2307_03167",
        "target": "2309_12566",
        "weight": 0.8088
      }
    },
    {
      "data": {
        "id": "e2872",
        "source": "2307_03167",
        "target": "2602_03639",
        "weight": 0.8075
      }
    },
    {
      "data": {
        "id": "e2873",
        "source": "2307_03167",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e2874",
        "source": "2307_03167",
        "target": "2603_11335",
        "weight": 0.8215
      }
    },
    {
      "data": {
        "id": "e2875",
        "source": "2307_03167",
        "target": "2403_18972",
        "weight": 0.8322
      }
    },
    {
      "data": {
        "id": "e2876",
        "source": "2307_03167",
        "target": "2603_24489",
        "weight": 0.8154
      }
    },
    {
      "data": {
        "id": "e2877",
        "source": "2307_09105",
        "target": "2409_06807",
        "weight": 0.8077
      }
    },
    {
      "data": {
        "id": "e2878",
        "source": "2307_09105",
        "target": "2409_12266",
        "weight": 0.8388
      }
    },
    {
      "data": {
        "id": "e2879",
        "source": "2307_09105",
        "target": "2604_12149",
        "weight": 0.8248
      }
    },
    {
      "data": {
        "id": "e2880",
        "source": "2307_09105",
        "target": "2409_15610",
        "weight": 0.825
      }
    },
    {
      "data": {
        "id": "e2881",
        "source": "2307_09105",
        "target": "2410_19414",
        "weight": 0.8175
      }
    },
    {
      "data": {
        "id": "e2882",
        "source": "2307_09105",
        "target": "2411_15651",
        "weight": 0.8008
      }
    },
    {
      "data": {
        "id": "e2883",
        "source": "2307_09105",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8267
      }
    },
    {
      "data": {
        "id": "e2884",
        "source": "2307_09105",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8438
      }
    },
    {
      "data": {
        "id": "e2885",
        "source": "2307_09105",
        "target": "2025_trevisan_model_predictive_path_integral",
        "weight": 0.8129
      }
    },
    {
      "data": {
        "id": "e2886",
        "source": "2307_09105",
        "target": "2503_05819",
        "weight": 0.8311
      }
    },
    {
      "data": {
        "id": "e2887",
        "source": "2307_09105",
        "target": "2503_11717",
        "weight": 0.8431
      }
    },
    {
      "data": {
        "id": "e2888",
        "source": "2307_09105",
        "target": "2505_05507",
        "weight": 0.8025
      }
    },
    {
      "data": {
        "id": "e2889",
        "source": "2307_09105",
        "target": "2506_17184",
        "weight": 0.8423
      }
    },
    {
      "data": {
        "id": "e2890",
        "source": "2307_09105",
        "target": "2506_21205",
        "weight": 0.8231
      }
    },
    {
      "data": {
        "id": "e2891",
        "source": "2307_09105",
        "target": "2510_00272",
        "weight": 0.8096
      }
    },
    {
      "data": {
        "id": "e2892",
        "source": "2307_09105",
        "target": "2511_02015",
        "weight": 0.8473
      }
    },
    {
      "data": {
        "id": "e2893",
        "source": "2307_09105",
        "target": "2309_12566",
        "weight": 0.8325
      }
    },
    {
      "data": {
        "id": "e2894",
        "source": "2307_09105",
        "target": "2309_14545",
        "weight": 0.8251
      }
    },
    {
      "data": {
        "id": "e2895",
        "source": "2307_09105",
        "target": "2602_02846",
        "weight": 0.8234
      }
    },
    {
      "data": {
        "id": "e2896",
        "source": "2307_09105",
        "target": "2602_03639",
        "weight": 0.838
      }
    },
    {
      "data": {
        "id": "e2897",
        "source": "2307_09105",
        "target": "2603_05385",
        "weight": 0.845
      }
    },
    {
      "data": {
        "id": "e2898",
        "source": "2307_09105",
        "target": "2603_10711",
        "weight": 0.8054
      }
    },
    {
      "data": {
        "id": "e2899",
        "source": "2307_09105",
        "target": "2401_09241",
        "weight": 0.8565
      }
    },
    {
      "data": {
        "id": "e2900",
        "source": "2307_09105",
        "target": "2603_16059",
        "weight": 0.8124
      }
    },
    {
      "data": {
        "id": "e2901",
        "source": "2307_09105",
        "target": "2603_24489",
        "weight": 0.8441
      }
    },
    {
      "data": {
        "id": "e2902",
        "source": "2308_04079",
        "target": "2409_16915",
        "weight": 0.8168
      }
    },
    {
      "data": {
        "id": "e2903",
        "source": "2308_04079",
        "target": "2504_12905",
        "weight": 0.8932
      }
    },
    {
      "data": {
        "id": "e2904",
        "source": "2308_04079",
        "target": "2505_08510",
        "weight": 0.8373
      }
    },
    {
      "data": {
        "id": "e2905",
        "source": "2308_04079",
        "target": "2403_02751",
        "weight": 0.7827
      }
    },
    {
      "data": {
        "id": "e2906",
        "source": "2309_07872",
        "target": "2409_11649",
        "weight": 0.8957
      }
    },
    {
      "data": {
        "id": "e2907",
        "source": "2309_07872",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.846
      }
    },
    {
      "data": {
        "id": "e2908",
        "source": "2309_07872",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8412
      }
    },
    {
      "data": {
        "id": "e2909",
        "source": "2309_07872",
        "target": "2024_wang_a_convergence_guaranteed_multiple",
        "weight": 0.9167
      }
    },
    {
      "data": {
        "id": "e2910",
        "source": "2309_07872",
        "target": "2403_00748",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e2911",
        "source": "2309_12566",
        "target": "2409_12266",
        "weight": 0.8249
      }
    },
    {
      "data": {
        "id": "e2912",
        "source": "2309_12566",
        "target": "2604_12149",
        "weight": 0.8333
      }
    },
    {
      "data": {
        "id": "e2913",
        "source": "2309_12566",
        "target": "2409_15610",
        "weight": 0.8104
      }
    },
    {
      "data": {
        "id": "e2914",
        "source": "2309_12566",
        "target": "2604_13312",
        "weight": 0.8373
      }
    },
    {
      "data": {
        "id": "e2915",
        "source": "2309_12566",
        "target": "2410_23916",
        "weight": 0.8133
      }
    },
    {
      "data": {
        "id": "e2916",
        "source": "2309_12566",
        "target": "2411_15651",
        "weight": 0.8134
      }
    },
    {
      "data": {
        "id": "e2917",
        "source": "2309_12566",
        "target": "2412_11270",
        "weight": 0.8138
      }
    },
    {
      "data": {
        "id": "e2918",
        "source": "2309_12566",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8856
      }
    },
    {
      "data": {
        "id": "e2919",
        "source": "2309_12566",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8608
      }
    },
    {
      "data": {
        "id": "e2920",
        "source": "2309_12566",
        "target": "2025_trevisan_model_predictive_path_integral",
        "weight": 0.8291
      }
    },
    {
      "data": {
        "id": "e2921",
        "source": "2309_12566",
        "target": "2503_05819",
        "weight": 0.8396
      }
    },
    {
      "data": {
        "id": "e2922",
        "source": "2309_12566",
        "target": "2503_11717",
        "weight": 0.8492
      }
    },
    {
      "data": {
        "id": "e2923",
        "source": "2309_12566",
        "target": "2504_06437",
        "weight": 0.8382
      }
    },
    {
      "data": {
        "id": "e2924",
        "source": "2309_12566",
        "target": "2505_05507",
        "weight": 0.8182
      }
    },
    {
      "data": {
        "id": "e2925",
        "source": "2309_12566",
        "target": "2506_21205",
        "weight": 0.8303
      }
    },
    {
      "data": {
        "id": "e2926",
        "source": "2309_12566",
        "target": "2508_21364",
        "weight": 0.8061
      }
    },
    {
      "data": {
        "id": "e2927",
        "source": "2309_12566",
        "target": "2509_14978",
        "weight": 0.8167
      }
    },
    {
      "data": {
        "id": "e2928",
        "source": "2309_12566",
        "target": "2510_00272",
        "weight": 0.8278
      }
    },
    {
      "data": {
        "id": "e2929",
        "source": "2309_12566",
        "target": "2511_02015",
        "weight": 0.8763
      }
    },
    {
      "data": {
        "id": "e2930",
        "source": "2309_12566",
        "target": "2511_11308",
        "weight": 0.8343
      }
    },
    {
      "data": {
        "id": "e2931",
        "source": "2309_12566",
        "target": "2511_14752",
        "weight": 0.8022
      }
    },
    {
      "data": {
        "id": "e2932",
        "source": "2309_12566",
        "target": "2310_16828",
        "weight": 0.8153
      }
    },
    {
      "data": {
        "id": "e2933",
        "source": "2309_12566",
        "target": "2602_03639",
        "weight": 0.8575
      }
    },
    {
      "data": {
        "id": "e2934",
        "source": "2309_12566",
        "target": "2311_06404",
        "weight": 0.8244
      }
    },
    {
      "data": {
        "id": "e2935",
        "source": "2309_12566",
        "target": "2311_11166",
        "weight": 0.8101
      }
    },
    {
      "data": {
        "id": "e2936",
        "source": "2309_12566",
        "target": "2603_05385",
        "weight": 0.8567
      }
    },
    {
      "data": {
        "id": "e2937",
        "source": "2309_12566",
        "target": "2401_09241",
        "weight": 0.8641
      }
    },
    {
      "data": {
        "id": "e2938",
        "source": "2309_12566",
        "target": "2603_24489",
        "weight": 0.9041
      }
    },
    {
      "data": {
        "id": "e2939",
        "source": "2309_12566",
        "target": "2604_01477",
        "weight": 0.8156
      }
    },
    {
      "data": {
        "id": "e2940",
        "source": "2309_14545",
        "target": "2409_06807",
        "weight": 0.8381
      }
    },
    {
      "data": {
        "id": "e2941",
        "source": "2309_14545",
        "target": "2409_12266",
        "weight": 0.8318
      }
    },
    {
      "data": {
        "id": "e2942",
        "source": "2309_14545",
        "target": "2604_13323",
        "weight": 0.8366
      }
    },
    {
      "data": {
        "id": "e2943",
        "source": "2309_14545",
        "target": "2604_14026",
        "weight": 0.813
      }
    },
    {
      "data": {
        "id": "e2944",
        "source": "2309_14545",
        "target": "2410_16727",
        "weight": 0.8165
      }
    },
    {
      "data": {
        "id": "e2945",
        "source": "2309_14545",
        "target": "2410_19414",
        "weight": 0.888
      }
    },
    {
      "data": {
        "id": "e2946",
        "source": "2309_14545",
        "target": "2411_17902",
        "weight": 0.8264
      }
    },
    {
      "data": {
        "id": "e2947",
        "source": "2309_14545",
        "target": "2503_06757",
        "weight": 0.8364
      }
    },
    {
      "data": {
        "id": "e2948",
        "source": "2309_14545",
        "target": "2505_06791",
        "weight": 0.8183
      }
    },
    {
      "data": {
        "id": "e2949",
        "source": "2309_14545",
        "target": "2508_21001",
        "weight": 0.8256
      }
    },
    {
      "data": {
        "id": "e2950",
        "source": "2309_14545",
        "target": "2310_17274",
        "weight": 0.8123
      }
    },
    {
      "data": {
        "id": "e2951",
        "source": "2309_14545",
        "target": "2602_00992",
        "weight": 0.8213
      }
    },
    {
      "data": {
        "id": "e2952",
        "source": "2309_14545",
        "target": "2602_02846",
        "weight": 0.8667
      }
    },
    {
      "data": {
        "id": "e2953",
        "source": "2309_14545",
        "target": "2603_06773",
        "weight": 0.8046
      }
    },
    {
      "data": {
        "id": "e2954",
        "source": "2309_14545",
        "target": "2603_16059",
        "weight": 0.8735
      }
    },
    {
      "data": {
        "id": "e2955",
        "source": "2309_14545",
        "target": "2604_04310",
        "weight": 0.8149
      }
    },
    {
      "data": {
        "id": "e2956",
        "source": "2309_14545",
        "target": "2406_02807",
        "weight": 0.8516
      }
    },
    {
      "data": {
        "id": "e2957",
        "source": "2309_14595",
        "target": "2410_19414",
        "weight": 0.8003
      }
    },
    {
      "data": {
        "id": "e2958",
        "source": "2309_14595",
        "target": "2411_15651",
        "weight": 0.8383
      }
    },
    {
      "data": {
        "id": "e2959",
        "source": "2309_14595",
        "target": "2411_17293",
        "weight": 0.8576
      }
    },
    {
      "data": {
        "id": "e2960",
        "source": "2309_14595",
        "target": "2411_17902",
        "weight": 0.8084
      }
    },
    {
      "data": {
        "id": "e2961",
        "source": "2309_14595",
        "target": "2412_11270",
        "weight": 0.8152
      }
    },
    {
      "data": {
        "id": "e2962",
        "source": "2309_14595",
        "target": "2503_16164",
        "weight": 0.8617
      }
    },
    {
      "data": {
        "id": "e2963",
        "source": "2309_14595",
        "target": "2505_10542",
        "weight": 0.8001
      }
    },
    {
      "data": {
        "id": "e2964",
        "source": "2309_14595",
        "target": "2508_21001",
        "weight": 0.8257
      }
    },
    {
      "data": {
        "id": "e2965",
        "source": "2309_14595",
        "target": "2508_21800",
        "weight": 0.8176
      }
    },
    {
      "data": {
        "id": "e2966",
        "source": "2309_14595",
        "target": "2510_21074",
        "weight": 0.8115
      }
    },
    {
      "data": {
        "id": "e2967",
        "source": "2309_14595",
        "target": "2511_18170",
        "weight": 0.8007
      }
    },
    {
      "data": {
        "id": "e2968",
        "source": "2309_14595",
        "target": "2603_12361",
        "weight": 0.8119
      }
    },
    {
      "data": {
        "id": "e2969",
        "source": "2309_14595",
        "target": "2403_01194",
        "weight": 0.8193
      }
    },
    {
      "data": {
        "id": "e2970",
        "source": "2309_14595",
        "target": "2403_10745",
        "weight": 0.8294
      }
    },
    {
      "data": {
        "id": "e2971",
        "source": "2310_02918",
        "target": "2604_12149",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e2972",
        "source": "2310_02918",
        "target": "2410_23916",
        "weight": 0.8146
      }
    },
    {
      "data": {
        "id": "e2973",
        "source": "2310_02918",
        "target": "2411_02158",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e2974",
        "source": "2310_02918",
        "target": "2603_23465",
        "weight": 0.805
      }
    },
    {
      "data": {
        "id": "e2975",
        "source": "2310_02918",
        "target": "2511_11308",
        "weight": 0.8167
      }
    },
    {
      "data": {
        "id": "e2976",
        "source": "2310_02918",
        "target": "2604_01477",
        "weight": 0.8052
      }
    },
    {
      "data": {
        "id": "e2977",
        "source": "2310_08710",
        "target": "2604_07944",
        "weight": 0.8249
      }
    },
    {
      "data": {
        "id": "e2978",
        "source": "2310_08710",
        "target": "2604_08266",
        "weight": 0.8064
      }
    },
    {
      "data": {
        "id": "e2979",
        "source": "2310_08710",
        "target": "2409_09523",
        "weight": 0.8442
      }
    },
    {
      "data": {
        "id": "e2980",
        "source": "2310_08710",
        "target": "2412_14415",
        "weight": 0.8514
      }
    },
    {
      "data": {
        "id": "e2981",
        "source": "2310_08710",
        "target": "2505_09074",
        "weight": 0.8181
      }
    },
    {
      "data": {
        "id": "e2982",
        "source": "2310_08710",
        "target": "2509_21961",
        "weight": 0.8204
      }
    },
    {
      "data": {
        "id": "e2983",
        "source": "2310_08710",
        "target": "2511_00088",
        "weight": 0.8354
      }
    },
    {
      "data": {
        "id": "e2984",
        "source": "2310_08710",
        "target": "2310_16828",
        "weight": 0.809
      }
    },
    {
      "data": {
        "id": "e2985",
        "source": "2310_08710",
        "target": "2603_14392",
        "weight": 0.8064
      }
    },
    {
      "data": {
        "id": "e2986",
        "source": "2310_16828",
        "target": "2604_07944",
        "weight": 0.8118
      }
    },
    {
      "data": {
        "id": "e2987",
        "source": "2310_16828",
        "target": "2409_09523",
        "weight": 0.8121
      }
    },
    {
      "data": {
        "id": "e2988",
        "source": "2310_16828",
        "target": "2409_15610",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e2989",
        "source": "2310_16828",
        "target": "2410_23916",
        "weight": 0.8241
      }
    },
    {
      "data": {
        "id": "e2990",
        "source": "2310_16828",
        "target": "2411_15651",
        "weight": 0.808
      }
    },
    {
      "data": {
        "id": "e2991",
        "source": "2310_16828",
        "target": "2412_14415",
        "weight": 0.8203
      }
    },
    {
      "data": {
        "id": "e2992",
        "source": "2310_16828",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8365
      }
    },
    {
      "data": {
        "id": "e2993",
        "source": "2310_16828",
        "target": "2507_05331",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e2994",
        "source": "2310_16828",
        "target": "2508_21800",
        "weight": 0.8067
      }
    },
    {
      "data": {
        "id": "e2995",
        "source": "2310_16828",
        "target": "2511_11308",
        "weight": 0.8212
      }
    },
    {
      "data": {
        "id": "e2996",
        "source": "2310_16828",
        "target": "2604_01477",
        "weight": 0.823
      }
    },
    {
      "data": {
        "id": "e2997",
        "source": "2310_16828",
        "target": "2311_18736",
        "weight": 0.8362
      }
    },
    {
      "data": {
        "id": "e2998",
        "source": "2310_16828",
        "target": "2603_05385",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e2999",
        "source": "2310_16828",
        "target": "2401_13662",
        "weight": 0.8036
      }
    },
    {
      "data": {
        "id": "e3000",
        "source": "2310_16828",
        "target": "2603_14392",
        "weight": 0.8192
      }
    },
    {
      "data": {
        "id": "e3001",
        "source": "2310_16828",
        "target": "2603_19968",
        "weight": 0.8122
      }
    },
    {
      "data": {
        "id": "e3002",
        "source": "2310_16828",
        "target": "2403_09110",
        "weight": 0.8119
      }
    },
    {
      "data": {
        "id": "e3003",
        "source": "2310_17274",
        "target": "2409_06807",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e3004",
        "source": "2310_17274",
        "target": "2602_02846",
        "weight": 0.8291
      }
    },
    {
      "data": {
        "id": "e3005",
        "source": "2310_17274",
        "target": "2503_06757",
        "weight": 0.8333
      }
    },
    {
      "data": {
        "id": "e3006",
        "source": "2310_17274",
        "target": "2410_16727",
        "weight": 0.8523
      }
    },
    {
      "data": {
        "id": "e3007",
        "source": "2310_17274",
        "target": "2411_11833",
        "weight": 0.8383
      }
    },
    {
      "data": {
        "id": "e3008",
        "source": "2310_17274",
        "target": "2505_06791",
        "weight": 0.824
      }
    },
    {
      "data": {
        "id": "e3009",
        "source": "2310_17274",
        "target": "2604_04310",
        "weight": 0.8406
      }
    },
    {
      "data": {
        "id": "e3010",
        "source": "2310_17556",
        "target": "2410_04083",
        "weight": 0.7413
      }
    },
    {
      "data": {
        "id": "e3011",
        "source": "2311_05135",
        "target": "2603_10711",
        "weight": 0.7351
      }
    },
    {
      "data": {
        "id": "e3012",
        "source": "2311_05135",
        "target": "2410_23916",
        "weight": 0.7855
      }
    },
    {
      "data": {
        "id": "e3013",
        "source": "2311_05135",
        "target": "2505_05588",
        "weight": 0.7596
      }
    },
    {
      "data": {
        "id": "e3014",
        "source": "2311_05135",
        "target": "2506_14865",
        "weight": 0.731
      }
    },
    {
      "data": {
        "id": "e3015",
        "source": "2311_06404",
        "target": "2409_11649",
        "weight": 0.8329
      }
    },
    {
      "data": {
        "id": "e3016",
        "source": "2311_06404",
        "target": "2604_10635",
        "weight": 0.8041
      }
    },
    {
      "data": {
        "id": "e3017",
        "source": "2311_06404",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8015
      }
    },
    {
      "data": {
        "id": "e3018",
        "source": "2311_06404",
        "target": "2506_14865",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e3019",
        "source": "2311_06404",
        "target": "2511_02095",
        "weight": 0.8107
      }
    },
    {
      "data": {
        "id": "e3020",
        "source": "2311_06404",
        "target": "2511_11308",
        "weight": 0.82
      }
    },
    {
      "data": {
        "id": "e3021",
        "source": "2311_06404",
        "target": "2511_14752",
        "weight": 0.8243
      }
    },
    {
      "data": {
        "id": "e3022",
        "source": "2311_06404",
        "target": "2602_03639",
        "weight": 0.8164
      }
    },
    {
      "data": {
        "id": "e3023",
        "source": "2311_06404",
        "target": "2603_04843",
        "weight": 0.8113
      }
    },
    {
      "data": {
        "id": "e3024",
        "source": "2311_06404",
        "target": "2603_05385",
        "weight": 0.8044
      }
    },
    {
      "data": {
        "id": "e3025",
        "source": "2311_06404",
        "target": "2024_jallet_real_time_constrained_trajectory",
        "weight": 0.8143
      }
    },
    {
      "data": {
        "id": "e3026",
        "source": "2311_06404",
        "target": "2603_11335",
        "weight": 0.8227
      }
    },
    {
      "data": {
        "id": "e3027",
        "source": "2311_06404",
        "target": "2603_24489",
        "weight": 0.8255
      }
    },
    {
      "data": {
        "id": "e3028",
        "source": "2311_07411",
        "target": "2508_07400",
        "weight": 0.8025
      }
    },
    {
      "data": {
        "id": "e3029",
        "source": "2311_07411",
        "target": "2503_00385",
        "weight": 0.8058
      }
    },
    {
      "data": {
        "id": "e3030",
        "source": "2311_07411",
        "target": "2602_18933",
        "weight": 0.8205
      }
    },
    {
      "data": {
        "id": "e3031",
        "source": "2311_07411",
        "target": "2401_13662",
        "weight": 0.8502
      }
    },
    {
      "data": {
        "id": "e3032",
        "source": "2311_07411",
        "target": "2511_02095",
        "weight": 0.8053
      }
    },
    {
      "data": {
        "id": "e3033",
        "source": "2311_07411",
        "target": "2511_11131",
        "weight": 0.8221
      }
    },
    {
      "data": {
        "id": "e3034",
        "source": "2311_11166",
        "target": "2511_02095",
        "weight": 0.814
      }
    },
    {
      "data": {
        "id": "e3035",
        "source": "2311_11166",
        "target": "2511_11131",
        "weight": 0.8027
      }
    },
    {
      "data": {
        "id": "e3036",
        "source": "2311_11166",
        "target": "2603_24489",
        "weight": 0.8036
      }
    },
    {
      "data": {
        "id": "e3037",
        "source": "2311_11489",
        "target": "2502_04799",
        "weight": 0.8261
      }
    },
    {
      "data": {
        "id": "e3038",
        "source": "2311_11489",
        "target": "2410_04083",
        "weight": 0.8045
      }
    },
    {
      "data": {
        "id": "e3039",
        "source": "2311_11489",
        "target": "2511_10626",
        "weight": 0.8273
      }
    },
    {
      "data": {
        "id": "e3040",
        "source": "2311_18736",
        "target": "2603_19968",
        "weight": 0.8106
      }
    },
    {
      "data": {
        "id": "e3041",
        "source": "2311_18736",
        "target": "2403_09110",
        "weight": 0.8229
      }
    },
    {
      "data": {
        "id": "e3042",
        "source": "2312_02758",
        "target": "2602_18933",
        "weight": 0.8047
      }
    },
    {
      "data": {
        "id": "e3043",
        "source": "2312_02758",
        "target": "2604_11183",
        "weight": 0.8222
      }
    },
    {
      "data": {
        "id": "e3044",
        "source": "2312_02758",
        "target": "2603_23465",
        "weight": 0.8169
      }
    },
    {
      "data": {
        "id": "e3045",
        "source": "2312_02758",
        "target": "2511_11308",
        "weight": 0.8073
      }
    },
    {
      "data": {
        "id": "e3046",
        "source": "2312_02758",
        "target": "2604_00900",
        "weight": 0.8345
      }
    },
    {
      "data": {
        "id": "e3047",
        "source": "2024_calem_action_and_trajectory_prediction",
        "target": "2412_14415",
        "weight": 0.8312
      }
    },
    {
      "data": {
        "id": "e3048",
        "source": "2024_calem_action_and_trajectory_prediction",
        "target": "2502_08664",
        "weight": 0.8458
      }
    },
    {
      "data": {
        "id": "e3049",
        "source": "2024_calem_action_and_trajectory_prediction",
        "target": "2409_09523",
        "weight": 0.8099
      }
    },
    {
      "data": {
        "id": "e3050",
        "source": "2024_calem_action_and_trajectory_prediction",
        "target": "2604_07944",
        "weight": 0.8012
      }
    },
    {
      "data": {
        "id": "e3051",
        "source": "2024_calem_action_and_trajectory_prediction",
        "target": "2503_03262",
        "weight": 0.8512
      }
    },
    {
      "data": {
        "id": "e3052",
        "source": "2024_calem_action_and_trajectory_prediction",
        "target": "2509_21961",
        "weight": 0.8003
      }
    },
    {
      "data": {
        "id": "e3053",
        "source": "2024_calem_action_and_trajectory_prediction",
        "target": "2603_06773",
        "weight": 0.8076
      }
    },
    {
      "data": {
        "id": "e3054",
        "source": "2024_calem_action_and_trajectory_prediction",
        "target": "2511_00088",
        "weight": 0.8193
      }
    },
    {
      "data": {
        "id": "e3055",
        "source": "2024_calem_action_and_trajectory_prediction",
        "target": "2505_09074",
        "weight": 0.8638
      }
    },
    {
      "data": {
        "id": "e3056",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2409_11649",
        "weight": 0.8456
      }
    },
    {
      "data": {
        "id": "e3057",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2604_13323",
        "weight": 0.827
      }
    },
    {
      "data": {
        "id": "e3058",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2410_23916",
        "weight": 0.825
      }
    },
    {
      "data": {
        "id": "e3059",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8087
      }
    },
    {
      "data": {
        "id": "e3060",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.811
      }
    },
    {
      "data": {
        "id": "e3061",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2504_18978",
        "weight": 0.8038
      }
    },
    {
      "data": {
        "id": "e3062",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2506_14865",
        "weight": 0.8517
      }
    },
    {
      "data": {
        "id": "e3063",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2506_22087",
        "weight": 0.8202
      }
    },
    {
      "data": {
        "id": "e3064",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2603_00871",
        "weight": 0.8269
      }
    },
    {
      "data": {
        "id": "e3065",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2024_wang_a_convergence_guaranteed_multiple",
        "weight": 0.8259
      }
    },
    {
      "data": {
        "id": "e3066",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2603_10711",
        "weight": 0.8081
      }
    },
    {
      "data": {
        "id": "e3067",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2603_11335",
        "weight": 0.8104
      }
    },
    {
      "data": {
        "id": "e3068",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2603_16059",
        "weight": 0.8095
      }
    },
    {
      "data": {
        "id": "e3069",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2604_04310",
        "weight": 0.8056
      }
    },
    {
      "data": {
        "id": "e3070",
        "source": "2024_jallet_real_time_constrained_trajectory",
        "target": "2403_00748",
        "weight": 0.8122
      }
    },
    {
      "data": {
        "id": "e3071",
        "source": "2024_wang_a_convergence_guaranteed_multiple",
        "target": "2409_11649",
        "weight": 0.8582
      }
    },
    {
      "data": {
        "id": "e3072",
        "source": "2024_wang_a_convergence_guaranteed_multiple",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8179
      }
    },
    {
      "data": {
        "id": "e3073",
        "source": "2401_09241",
        "target": "2409_12266",
        "weight": 0.8668
      }
    },
    {
      "data": {
        "id": "e3074",
        "source": "2401_09241",
        "target": "2604_12149",
        "weight": 0.8473
      }
    },
    {
      "data": {
        "id": "e3075",
        "source": "2401_09241",
        "target": "2409_15610",
        "weight": 0.8384
      }
    },
    {
      "data": {
        "id": "e3076",
        "source": "2401_09241",
        "target": "2410_19414",
        "weight": 0.833
      }
    },
    {
      "data": {
        "id": "e3077",
        "source": "2401_09241",
        "target": "2410_23916",
        "weight": 0.8143
      }
    },
    {
      "data": {
        "id": "e3078",
        "source": "2401_09241",
        "target": "2411_15651",
        "weight": 0.8207
      }
    },
    {
      "data": {
        "id": "e3079",
        "source": "2401_09241",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8584
      }
    },
    {
      "data": {
        "id": "e3080",
        "source": "2401_09241",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8846
      }
    },
    {
      "data": {
        "id": "e3081",
        "source": "2401_09241",
        "target": "2025_trevisan_model_predictive_path_integral",
        "weight": 0.8373
      }
    },
    {
      "data": {
        "id": "e3082",
        "source": "2401_09241",
        "target": "2503_05819",
        "weight": 0.8764
      }
    },
    {
      "data": {
        "id": "e3083",
        "source": "2401_09241",
        "target": "2503_11717",
        "weight": 0.8815
      }
    },
    {
      "data": {
        "id": "e3084",
        "source": "2401_09241",
        "target": "2504_06437",
        "weight": 0.8135
      }
    },
    {
      "data": {
        "id": "e3085",
        "source": "2401_09241",
        "target": "2505_05507",
        "weight": 0.8101
      }
    },
    {
      "data": {
        "id": "e3086",
        "source": "2401_09241",
        "target": "2506_17184",
        "weight": 0.807
      }
    },
    {
      "data": {
        "id": "e3087",
        "source": "2401_09241",
        "target": "2506_21205",
        "weight": 0.8481
      }
    },
    {
      "data": {
        "id": "e3088",
        "source": "2401_09241",
        "target": "2508_21364",
        "weight": 0.8119
      }
    },
    {
      "data": {
        "id": "e3089",
        "source": "2401_09241",
        "target": "2509_14978",
        "weight": 0.8232
      }
    },
    {
      "data": {
        "id": "e3090",
        "source": "2401_09241",
        "target": "2510_00272",
        "weight": 0.8398
      }
    },
    {
      "data": {
        "id": "e3091",
        "source": "2401_09241",
        "target": "2511_02015",
        "weight": 0.862
      }
    },
    {
      "data": {
        "id": "e3092",
        "source": "2401_09241",
        "target": "2511_11308",
        "weight": 0.8129
      }
    },
    {
      "data": {
        "id": "e3093",
        "source": "2401_09241",
        "target": "2602_03639",
        "weight": 0.8827
      }
    },
    {
      "data": {
        "id": "e3094",
        "source": "2401_09241",
        "target": "2603_05385",
        "weight": 0.8628
      }
    },
    {
      "data": {
        "id": "e3095",
        "source": "2401_09241",
        "target": "2603_24489",
        "weight": 0.867
      }
    },
    {
      "data": {
        "id": "e3096",
        "source": "2401_09241",
        "target": "2604_01477",
        "weight": 0.8171
      }
    },
    {
      "data": {
        "id": "e3097",
        "source": "2401_13662",
        "target": "2602_18933",
        "weight": 0.8222
      }
    },
    {
      "data": {
        "id": "e3098",
        "source": "2401_13662",
        "target": "2604_18578",
        "weight": 0.8002
      }
    },
    {
      "data": {
        "id": "e3099",
        "source": "2401_13662",
        "target": "2503_24371",
        "weight": 0.8006
      }
    },
    {
      "data": {
        "id": "e3100",
        "source": "2401_13662",
        "target": "2511_02095",
        "weight": 0.8361
      }
    },
    {
      "data": {
        "id": "e3101",
        "source": "2401_13662",
        "target": "2511_11131",
        "weight": 0.8293
      }
    },
    {
      "data": {
        "id": "e3102",
        "source": "2401_15185",
        "target": "2604_10635",
        "weight": 0.7693
      }
    },
    {
      "data": {
        "id": "e3103",
        "source": "2401_15185",
        "target": "2603_19968",
        "weight": 0.7726
      }
    },
    {
      "data": {
        "id": "e3104",
        "source": "2401_15185",
        "target": "2403_18972",
        "weight": 0.7658
      }
    },
    {
      "data": {
        "id": "e3105",
        "source": "2401_16025",
        "target": "2604_18578",
        "weight": 0.8613
      }
    },
    {
      "data": {
        "id": "e3106",
        "source": "2402_01443",
        "target": "2409_09523",
        "weight": 0.8222
      }
    },
    {
      "data": {
        "id": "e3107",
        "source": "2402_01443",
        "target": "2503_03262",
        "weight": 0.7983
      }
    },
    {
      "data": {
        "id": "e3108",
        "source": "2402_03300",
        "target": "2604_07944",
        "weight": 0.7521
      }
    },
    {
      "data": {
        "id": "e3109",
        "source": "2402_03300",
        "target": "2604_18578",
        "weight": 0.7736
      }
    },
    {
      "data": {
        "id": "e3110",
        "source": "2402_03893",
        "target": "2502_08664",
        "weight": 0.8286
      }
    },
    {
      "data": {
        "id": "e3111",
        "source": "2402_03893",
        "target": "2503_03262",
        "weight": 0.8628
      }
    },
    {
      "data": {
        "id": "e3112",
        "source": "2402_03893",
        "target": "2505_09074",
        "weight": 0.8261
      }
    },
    {
      "data": {
        "id": "e3113",
        "source": "2403_00748",
        "target": "2409_11649",
        "weight": 0.8462
      }
    },
    {
      "data": {
        "id": "e3114",
        "source": "2403_00748",
        "target": "2511_02095",
        "weight": 0.8147
      }
    },
    {
      "data": {
        "id": "e3115",
        "source": "2403_01194",
        "target": "2411_15651",
        "weight": 0.8251
      }
    },
    {
      "data": {
        "id": "e3116",
        "source": "2403_01194",
        "target": "2502_09556",
        "weight": 0.8082
      }
    },
    {
      "data": {
        "id": "e3117",
        "source": "2403_01194",
        "target": "2503_16164",
        "weight": 0.8063
      }
    },
    {
      "data": {
        "id": "e3118",
        "source": "2403_01194",
        "target": "2403_10745",
        "weight": 0.8178
      }
    },
    {
      "data": {
        "id": "e3119",
        "source": "2403_02751",
        "target": "2409_16915",
        "weight": 0.8764
      }
    },
    {
      "data": {
        "id": "e3120",
        "source": "2403_02751",
        "target": "2505_08510",
        "weight": 0.8498
      }
    },
    {
      "data": {
        "id": "e3121",
        "source": "2403_02751",
        "target": "2511_18170",
        "weight": 0.7941
      }
    },
    {
      "data": {
        "id": "e3122",
        "source": "2403_02751",
        "target": "2406_02807",
        "weight": 0.8218
      }
    },
    {
      "data": {
        "id": "e3123",
        "source": "2403_05466",
        "target": "2603_00871",
        "weight": 0.7781
      }
    },
    {
      "data": {
        "id": "e3124",
        "source": "2403_05466",
        "target": "2406_02807",
        "weight": 0.8249
      }
    },
    {
      "data": {
        "id": "e3125",
        "source": "2403_09110",
        "target": "2603_19968",
        "weight": 0.8238
      }
    },
    {
      "data": {
        "id": "e3126",
        "source": "2403_09110",
        "target": "2412_12036",
        "weight": 0.8427
      }
    },
    {
      "data": {
        "id": "e3127",
        "source": "2403_10745",
        "target": "2409_12266",
        "weight": 0.8071
      }
    },
    {
      "data": {
        "id": "e3128",
        "source": "2403_10745",
        "target": "2410_19414",
        "weight": 0.8406
      }
    },
    {
      "data": {
        "id": "e3129",
        "source": "2403_10745",
        "target": "2411_15651",
        "weight": 0.8307
      }
    },
    {
      "data": {
        "id": "e3130",
        "source": "2403_10745",
        "target": "2411_17902",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e3131",
        "source": "2403_10745",
        "target": "2502_09556",
        "weight": 0.8022
      }
    },
    {
      "data": {
        "id": "e3132",
        "source": "2403_10745",
        "target": "2503_06757",
        "weight": 0.8175
      }
    },
    {
      "data": {
        "id": "e3133",
        "source": "2403_10745",
        "target": "2503_16164",
        "weight": 0.8326
      }
    },
    {
      "data": {
        "id": "e3134",
        "source": "2403_10745",
        "target": "2504_18978",
        "weight": 0.8065
      }
    },
    {
      "data": {
        "id": "e3135",
        "source": "2403_10745",
        "target": "2505_10542",
        "weight": 0.8045
      }
    },
    {
      "data": {
        "id": "e3136",
        "source": "2403_10745",
        "target": "2508_21001",
        "weight": 0.8734
      }
    },
    {
      "data": {
        "id": "e3137",
        "source": "2403_10745",
        "target": "2602_02846",
        "weight": 0.8259
      }
    },
    {
      "data": {
        "id": "e3138",
        "source": "2403_10745",
        "target": "2603_06773",
        "weight": 0.8155
      }
    },
    {
      "data": {
        "id": "e3139",
        "source": "2403_10745",
        "target": "2603_16059",
        "weight": 0.8288
      }
    },
    {
      "data": {
        "id": "e3140",
        "source": "2403_14606",
        "target": "2603_08824",
        "weight": 0.7936
      }
    },
    {
      "data": {
        "id": "e3141",
        "source": "2403_14606",
        "target": "2511_11308",
        "weight": 0.7431
      }
    },
    {
      "data": {
        "id": "e3142",
        "source": "2403_18972",
        "target": "2510_00272",
        "weight": 0.7928
      }
    },
    {
      "data": {
        "id": "e3143",
        "source": "2403_18972",
        "target": "2410_19414",
        "weight": 0.7937
      }
    },
    {
      "data": {
        "id": "e3144",
        "source": "2403_18972",
        "target": "2506_21205",
        "weight": 0.807
      }
    },
    {
      "data": {
        "id": "e3145",
        "source": "2403_18972",
        "target": "2601_14880",
        "weight": 0.8084
      }
    },
    {
      "data": {
        "id": "e3146",
        "source": "2405_03281",
        "target": "2602_00992",
        "weight": 0.8053
      }
    },
    {
      "data": {
        "id": "e3147",
        "source": "2405_03281",
        "target": "2410_19414",
        "weight": 0.8058
      }
    },
    {
      "data": {
        "id": "e3148",
        "source": "2405_03281",
        "target": "2504_18978",
        "weight": 0.8197
      }
    },
    {
      "data": {
        "id": "e3149",
        "source": "2405_03281",
        "target": "2603_16059",
        "weight": 0.8192
      }
    },
    {
      "data": {
        "id": "e3150",
        "source": "2405_03281",
        "target": "2511_18170",
        "weight": 0.8059
      }
    },
    {
      "data": {
        "id": "e3151",
        "source": "2405_03281",
        "target": "2604_01614",
        "weight": 0.838
      }
    },
    {
      "data": {
        "id": "e3152",
        "source": "2406_02807",
        "target": "2604_13323",
        "weight": 0.8136
      }
    },
    {
      "data": {
        "id": "e3153",
        "source": "2406_02807",
        "target": "2410_16727",
        "weight": 0.8002
      }
    },
    {
      "data": {
        "id": "e3154",
        "source": "2406_02807",
        "target": "2410_19414",
        "weight": 0.8399
      }
    },
    {
      "data": {
        "id": "e3155",
        "source": "2406_02807",
        "target": "2411_17902",
        "weight": 0.8427
      }
    },
    {
      "data": {
        "id": "e3156",
        "source": "2406_02807",
        "target": "2503_06757",
        "weight": 0.844
      }
    },
    {
      "data": {
        "id": "e3157",
        "source": "2406_02807",
        "target": "2508_21001",
        "weight": 0.8279
      }
    },
    {
      "data": {
        "id": "e3158",
        "source": "2406_02807",
        "target": "2602_00992",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e3159",
        "source": "2406_02807",
        "target": "2602_02846",
        "weight": 0.8168
      }
    },
    {
      "data": {
        "id": "e3160",
        "source": "2406_02807",
        "target": "2603_12361",
        "weight": 0.8077
      }
    },
    {
      "data": {
        "id": "e3161",
        "source": "2406_02807",
        "target": "2603_16059",
        "weight": 0.826
      }
    },
    {
      "data": {
        "id": "e3162",
        "source": "2406_02807",
        "target": "2604_01614",
        "weight": 0.8072
      }
    },
    {
      "data": {
        "id": "e3163",
        "source": "2406_05846",
        "target": "2603_00871",
        "weight": 0.8083
      }
    },
    {
      "data": {
        "id": "e3164",
        "source": "2406_05846",
        "target": "2603_10711",
        "weight": 0.8522
      }
    },
    {
      "data": {
        "id": "e3165",
        "source": "2406_05846",
        "target": "2603_11335",
        "weight": 0.8741
      }
    },
    {
      "data": {
        "id": "e3166",
        "source": "2406_05846",
        "target": "2504_18978",
        "weight": 0.8225
      }
    },
    {
      "data": {
        "id": "e3167",
        "source": "2406_05846",
        "target": "2603_24489",
        "weight": 0.8107
      }
    },
    {
      "data": {
        "id": "e3168",
        "source": "2406_05846",
        "target": "2511_14752",
        "weight": 0.8424
      }
    },
    {
      "data": {
        "id": "e3169",
        "source": "2406_05846",
        "target": "2506_14865",
        "weight": 0.8073
      }
    },
    {
      "data": {
        "id": "e3170",
        "source": "2406_16793",
        "target": "2410_13732",
        "weight": 0.772
      }
    },
    {
      "data": {
        "id": "e3171",
        "source": "2406_16793",
        "target": "2506_05454",
        "weight": 0.7535
      }
    },
    {
      "data": {
        "id": "e3172",
        "source": "2406_19617",
        "target": "2602_18933",
        "weight": 0.8173
      }
    },
    {
      "data": {
        "id": "e3173",
        "source": "2406_19617",
        "target": "2503_00385",
        "weight": 0.8425
      }
    },
    {
      "data": {
        "id": "e3174",
        "source": "2406_19617",
        "target": "2410_04083",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e3175",
        "source": "2406_19617",
        "target": "2604_14669",
        "weight": 0.8146
      }
    },
    {
      "data": {
        "id": "e3176",
        "source": "2406_19617",
        "target": "2506_05454",
        "weight": 0.884
      }
    },
    {
      "data": {
        "id": "e3177",
        "source": "2407_15007",
        "target": "2507_05331",
        "weight": 0.8229
      }
    },
    {
      "data": {
        "id": "e3178",
        "source": "2407_15007",
        "target": "2507_09061",
        "weight": 0.8487
      }
    },
    {
      "data": {
        "id": "e3179",
        "source": "2407_15007",
        "target": "2512_00453",
        "weight": 0.8241
      }
    },
    {
      "data": {
        "id": "e3180",
        "source": "2407_15007",
        "target": "2503_09722",
        "weight": 0.8747
      }
    },
    {
      "data": {
        "id": "e3181",
        "source": "2407_15007",
        "target": "2603_19968",
        "weight": 0.821
      }
    },
    {
      "data": {
        "id": "e3182",
        "source": "2407_15007",
        "target": "2505_21851",
        "weight": 0.8102
      }
    },
    {
      "data": {
        "id": "e3183",
        "source": "2409_06807",
        "target": "2602_02846",
        "weight": 0.9552
      }
    },
    {
      "data": {
        "id": "e3184",
        "source": "2409_06807",
        "target": "2508_21001",
        "weight": 0.808
      }
    },
    {
      "data": {
        "id": "e3185",
        "source": "2409_06807",
        "target": "2503_06757",
        "weight": 0.8366
      }
    },
    {
      "data": {
        "id": "e3186",
        "source": "2409_06807",
        "target": "2410_16727",
        "weight": 0.816
      }
    },
    {
      "data": {
        "id": "e3187",
        "source": "2409_06807",
        "target": "2411_11833",
        "weight": 0.8113
      }
    },
    {
      "data": {
        "id": "e3188",
        "source": "2409_06807",
        "target": "2603_16059",
        "weight": 0.8299
      }
    },
    {
      "data": {
        "id": "e3189",
        "source": "2409_06807",
        "target": "2505_06791",
        "weight": 0.8069
      }
    },
    {
      "data": {
        "id": "e3190",
        "source": "2409_09523",
        "target": "2604_07944",
        "weight": 0.8282
      }
    },
    {
      "data": {
        "id": "e3191",
        "source": "2409_09523",
        "target": "2604_08266",
        "weight": 0.801
      }
    },
    {
      "data": {
        "id": "e3192",
        "source": "2409_09523",
        "target": "2409_16012",
        "weight": 0.8033
      }
    },
    {
      "data": {
        "id": "e3193",
        "source": "2409_09523",
        "target": "2410_19414",
        "weight": 0.8064
      }
    },
    {
      "data": {
        "id": "e3194",
        "source": "2409_09523",
        "target": "2410_23916",
        "weight": 0.809
      }
    },
    {
      "data": {
        "id": "e3195",
        "source": "2409_09523",
        "target": "2411_18714",
        "weight": 0.8254
      }
    },
    {
      "data": {
        "id": "e3196",
        "source": "2409_09523",
        "target": "2412_14415",
        "weight": 0.8396
      }
    },
    {
      "data": {
        "id": "e3197",
        "source": "2409_09523",
        "target": "2412_17920",
        "weight": 0.8043
      }
    },
    {
      "data": {
        "id": "e3198",
        "source": "2409_09523",
        "target": "2025_hu_technically_speaking_transitioning_from",
        "weight": 0.8136
      }
    },
    {
      "data": {
        "id": "e3199",
        "source": "2409_09523",
        "target": "2502_08664",
        "weight": 0.8094
      }
    },
    {
      "data": {
        "id": "e3200",
        "source": "2409_09523",
        "target": "2503_03262",
        "weight": 0.8271
      }
    },
    {
      "data": {
        "id": "e3201",
        "source": "2409_09523",
        "target": "2503_06135",
        "weight": 0.8028
      }
    },
    {
      "data": {
        "id": "e3202",
        "source": "2409_09523",
        "target": "2505_09074",
        "weight": 0.8611
      }
    },
    {
      "data": {
        "id": "e3203",
        "source": "2409_09523",
        "target": "2508_21001",
        "weight": 0.8219
      }
    },
    {
      "data": {
        "id": "e3204",
        "source": "2409_09523",
        "target": "2509_21961",
        "weight": 0.8445
      }
    },
    {
      "data": {
        "id": "e3205",
        "source": "2409_09523",
        "target": "2511_00088",
        "weight": 0.8498
      }
    },
    {
      "data": {
        "id": "e3206",
        "source": "2409_09523",
        "target": "2511_18170",
        "weight": 0.8173
      }
    },
    {
      "data": {
        "id": "e3207",
        "source": "2409_09523",
        "target": "2601_14880",
        "weight": 0.8113
      }
    },
    {
      "data": {
        "id": "e3208",
        "source": "2409_09523",
        "target": "2603_06773",
        "weight": 0.8083
      }
    },
    {
      "data": {
        "id": "e3209",
        "source": "2409_09523",
        "target": "2603_14392",
        "weight": 0.8047
      }
    },
    {
      "data": {
        "id": "e3210",
        "source": "2409_11649",
        "target": "2025_xia_an_adaptive_projection_differential",
        "weight": 0.8787
      }
    },
    {
      "data": {
        "id": "e3211",
        "source": "2409_11649",
        "target": "2511_02095",
        "weight": 0.8058
      }
    },
    {
      "data": {
        "id": "e3212",
        "source": "2409_11649",
        "target": "2511_14752",
        "weight": 0.8093
      }
    },
    {
      "data": {
        "id": "e3213",
        "source": "2409_11649",
        "target": "2603_11335",
        "weight": 0.8183
      }
    },
    {
      "data": {
        "id": "e3214",
        "source": "2409_12266",
        "target": "2604_12149",
        "weight": 0.8368
      }
    },
    {
      "data": {
        "id": "e3215",
        "source": "2409_12266",
        "target": "2409_15610",
        "weight": 0.813
      }
    },
    {
      "data": {
        "id": "e3216",
        "source": "2409_12266",
        "target": "2410_19414",
        "weight": 0.8527
      }
    },
    {
      "data": {
        "id": "e3217",
        "source": "2409_12266",
        "target": "2411_15651",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e3218",
        "source": "2409_12266",
        "target": "2412_11270",
        "weight": 0.8039
      }
    },
    {
      "data": {
        "id": "e3219",
        "source": "2409_12266",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8079
      }
    },
    {
      "data": {
        "id": "e3220",
        "source": "2409_12266",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8463
      }
    },
    {
      "data": {
        "id": "e3221",
        "source": "2409_12266",
        "target": "2503_05819",
        "weight": 0.9383
      }
    },
    {
      "data": {
        "id": "e3222",
        "source": "2409_12266",
        "target": "2503_11717",
        "weight": 0.83
      }
    },
    {
      "data": {
        "id": "e3223",
        "source": "2409_12266",
        "target": "2504_18978",
        "weight": 0.8075
      }
    },
    {
      "data": {
        "id": "e3224",
        "source": "2409_12266",
        "target": "2506_17184",
        "weight": 0.8006
      }
    },
    {
      "data": {
        "id": "e3225",
        "source": "2409_12266",
        "target": "2506_21205",
        "weight": 0.8048
      }
    },
    {
      "data": {
        "id": "e3226",
        "source": "2409_12266",
        "target": "2508_21001",
        "weight": 0.819
      }
    },
    {
      "data": {
        "id": "e3227",
        "source": "2409_12266",
        "target": "2509_21961",
        "weight": 0.8003
      }
    },
    {
      "data": {
        "id": "e3228",
        "source": "2409_12266",
        "target": "2511_02015",
        "weight": 0.8217
      }
    },
    {
      "data": {
        "id": "e3229",
        "source": "2409_12266",
        "target": "2511_18170",
        "weight": 0.8076
      }
    },
    {
      "data": {
        "id": "e3230",
        "source": "2409_12266",
        "target": "2602_00992",
        "weight": 0.8003
      }
    },
    {
      "data": {
        "id": "e3231",
        "source": "2409_12266",
        "target": "2602_02846",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e3232",
        "source": "2409_12266",
        "target": "2602_03639",
        "weight": 0.8191
      }
    },
    {
      "data": {
        "id": "e3233",
        "source": "2409_12266",
        "target": "2603_05385",
        "weight": 0.8249
      }
    },
    {
      "data": {
        "id": "e3234",
        "source": "2409_12266",
        "target": "2603_06773",
        "weight": 0.8058
      }
    },
    {
      "data": {
        "id": "e3235",
        "source": "2409_12266",
        "target": "2603_16059",
        "weight": 0.823
      }
    },
    {
      "data": {
        "id": "e3236",
        "source": "2409_12266",
        "target": "2603_24489",
        "weight": 0.8156
      }
    },
    {
      "data": {
        "id": "e3237",
        "source": "2409_14562",
        "target": "2507_05331",
        "weight": 0.84
      }
    },
    {
      "data": {
        "id": "e3238",
        "source": "2409_14562",
        "target": "2507_09061",
        "weight": 0.8005
      }
    },
    {
      "data": {
        "id": "e3239",
        "source": "2409_14562",
        "target": "2603_06773",
        "weight": 0.8382
      }
    },
    {
      "data": {
        "id": "e3240",
        "source": "2409_14562",
        "target": "2604_04539",
        "weight": 0.8268
      }
    },
    {
      "data": {
        "id": "e3241",
        "source": "2409_15610",
        "target": "2604_12149",
        "weight": 0.8154
      }
    },
    {
      "data": {
        "id": "e3242",
        "source": "2409_15610",
        "target": "2410_23916",
        "weight": 0.841
      }
    },
    {
      "data": {
        "id": "e3243",
        "source": "2409_15610",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8322
      }
    },
    {
      "data": {
        "id": "e3244",
        "source": "2409_15610",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8207
      }
    },
    {
      "data": {
        "id": "e3245",
        "source": "2409_15610",
        "target": "2503_04613",
        "weight": 0.8485
      }
    },
    {
      "data": {
        "id": "e3246",
        "source": "2409_15610",
        "target": "2503_05819",
        "weight": 0.8272
      }
    },
    {
      "data": {
        "id": "e3247",
        "source": "2409_15610",
        "target": "2503_11717",
        "weight": 0.8474
      }
    },
    {
      "data": {
        "id": "e3248",
        "source": "2409_15610",
        "target": "2507_19652",
        "weight": 0.8272
      }
    },
    {
      "data": {
        "id": "e3249",
        "source": "2409_15610",
        "target": "2511_02015",
        "weight": 0.8204
      }
    },
    {
      "data": {
        "id": "e3250",
        "source": "2409_15610",
        "target": "2511_11308",
        "weight": 0.8139
      }
    },
    {
      "data": {
        "id": "e3251",
        "source": "2409_15610",
        "target": "2602_03639",
        "weight": 0.8367
      }
    },
    {
      "data": {
        "id": "e3252",
        "source": "2409_15610",
        "target": "2603_05385",
        "weight": 0.8313
      }
    },
    {
      "data": {
        "id": "e3253",
        "source": "2409_15610",
        "target": "2603_24489",
        "weight": 0.8361
      }
    },
    {
      "data": {
        "id": "e3254",
        "source": "2409_15610",
        "target": "2604_01477",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e3255",
        "source": "2409_16012",
        "target": "2508_21001",
        "weight": 0.835
      }
    },
    {
      "data": {
        "id": "e3256",
        "source": "2409_16012",
        "target": "2508_21800",
        "weight": 0.8456
      }
    },
    {
      "data": {
        "id": "e3257",
        "source": "2409_16012",
        "target": "2503_06135",
        "weight": 0.822
      }
    },
    {
      "data": {
        "id": "e3258",
        "source": "2409_16012",
        "target": "2509_21961",
        "weight": 0.8227
      }
    },
    {
      "data": {
        "id": "e3259",
        "source": "2409_16012",
        "target": "2410_16727",
        "weight": 0.857
      }
    },
    {
      "data": {
        "id": "e3260",
        "source": "2409_16012",
        "target": "2410_19414",
        "weight": 0.8085
      }
    },
    {
      "data": {
        "id": "e3261",
        "source": "2409_16012",
        "target": "2510_22015",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e3262",
        "source": "2409_16012",
        "target": "2603_12361",
        "weight": 0.812
      }
    },
    {
      "data": {
        "id": "e3263",
        "source": "2409_16915",
        "target": "2504_12905",
        "weight": 0.8063
      }
    },
    {
      "data": {
        "id": "e3264",
        "source": "2409_16915",
        "target": "2505_08510",
        "weight": 0.8891
      }
    },
    {
      "data": {
        "id": "e3265",
        "source": "2410_04083",
        "target": "2502_04799",
        "weight": 0.8237
      }
    },
    {
      "data": {
        "id": "e3266",
        "source": "2410_04083",
        "target": "2506_05454",
        "weight": 0.8366
      }
    },
    {
      "data": {
        "id": "e3267",
        "source": "2410_16727",
        "target": "2410_19414",
        "weight": 0.8069
      }
    },
    {
      "data": {
        "id": "e3268",
        "source": "2410_16727",
        "target": "2411_11833",
        "weight": 0.837
      }
    },
    {
      "data": {
        "id": "e3269",
        "source": "2410_16727",
        "target": "2503_06135",
        "weight": 0.8213
      }
    },
    {
      "data": {
        "id": "e3270",
        "source": "2410_16727",
        "target": "2503_06757",
        "weight": 0.8199
      }
    },
    {
      "data": {
        "id": "e3271",
        "source": "2410_16727",
        "target": "2505_06791",
        "weight": 0.8045
      }
    },
    {
      "data": {
        "id": "e3272",
        "source": "2410_16727",
        "target": "2508_21001",
        "weight": 0.8398
      }
    },
    {
      "data": {
        "id": "e3273",
        "source": "2410_16727",
        "target": "2508_21800",
        "weight": 0.839
      }
    },
    {
      "data": {
        "id": "e3274",
        "source": "2410_16727",
        "target": "2602_02846",
        "weight": 0.8391
      }
    },
    {
      "data": {
        "id": "e3275",
        "source": "2410_16727",
        "target": "2603_06773",
        "weight": 0.8133
      }
    },
    {
      "data": {
        "id": "e3276",
        "source": "2410_16727",
        "target": "2603_10711",
        "weight": 0.8017
      }
    },
    {
      "data": {
        "id": "e3277",
        "source": "2410_16727",
        "target": "2603_12361",
        "weight": 0.8063
      }
    },
    {
      "data": {
        "id": "e3278",
        "source": "2410_19414",
        "target": "2604_12149",
        "weight": 0.8047
      }
    },
    {
      "data": {
        "id": "e3279",
        "source": "2410_19414",
        "target": "2604_14026",
        "weight": 0.8518
      }
    },
    {
      "data": {
        "id": "e3280",
        "source": "2410_19414",
        "target": "2411_15651",
        "weight": 0.8175
      }
    },
    {
      "data": {
        "id": "e3281",
        "source": "2410_19414",
        "target": "2411_17293",
        "weight": 0.833
      }
    },
    {
      "data": {
        "id": "e3282",
        "source": "2410_19414",
        "target": "2411_17902",
        "weight": 0.8171
      }
    },
    {
      "data": {
        "id": "e3283",
        "source": "2410_19414",
        "target": "2412_11270",
        "weight": 0.8112
      }
    },
    {
      "data": {
        "id": "e3284",
        "source": "2410_19414",
        "target": "2503_05819",
        "weight": 0.8152
      }
    },
    {
      "data": {
        "id": "e3285",
        "source": "2410_19414",
        "target": "2503_06135",
        "weight": 0.8022
      }
    },
    {
      "data": {
        "id": "e3286",
        "source": "2410_19414",
        "target": "2503_06757",
        "weight": 0.8122
      }
    },
    {
      "data": {
        "id": "e3287",
        "source": "2410_19414",
        "target": "2503_16164",
        "weight": 0.8041
      }
    },
    {
      "data": {
        "id": "e3288",
        "source": "2410_19414",
        "target": "2506_21205",
        "weight": 0.8134
      }
    },
    {
      "data": {
        "id": "e3289",
        "source": "2410_19414",
        "target": "2506_22087",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e3290",
        "source": "2410_19414",
        "target": "2508_05027",
        "weight": 0.8123
      }
    },
    {
      "data": {
        "id": "e3291",
        "source": "2410_19414",
        "target": "2508_21001",
        "weight": 0.8536
      }
    },
    {
      "data": {
        "id": "e3292",
        "source": "2410_19414",
        "target": "2508_21800",
        "weight": 0.8039
      }
    },
    {
      "data": {
        "id": "e3293",
        "source": "2410_19414",
        "target": "2510_21074",
        "weight": 0.8035
      }
    },
    {
      "data": {
        "id": "e3294",
        "source": "2410_19414",
        "target": "2511_18170",
        "weight": 0.8161
      }
    },
    {
      "data": {
        "id": "e3295",
        "source": "2410_19414",
        "target": "2602_00992",
        "weight": 0.8356
      }
    },
    {
      "data": {
        "id": "e3296",
        "source": "2410_19414",
        "target": "2602_02846",
        "weight": 0.8429
      }
    },
    {
      "data": {
        "id": "e3297",
        "source": "2410_19414",
        "target": "2603_06773",
        "weight": 0.8333
      }
    },
    {
      "data": {
        "id": "e3298",
        "source": "2410_19414",
        "target": "2603_12361",
        "weight": 0.8153
      }
    },
    {
      "data": {
        "id": "e3299",
        "source": "2410_19414",
        "target": "2603_16059",
        "weight": 0.8285
      }
    },
    {
      "data": {
        "id": "e3300",
        "source": "2410_23916",
        "target": "2604_12149",
        "weight": 0.8201
      }
    },
    {
      "data": {
        "id": "e3301",
        "source": "2410_23916",
        "target": "2411_15651",
        "weight": 0.8083
      }
    },
    {
      "data": {
        "id": "e3302",
        "source": "2410_23916",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8239
      }
    },
    {
      "data": {
        "id": "e3303",
        "source": "2410_23916",
        "target": "2503_05819",
        "weight": 0.8095
      }
    },
    {
      "data": {
        "id": "e3304",
        "source": "2410_23916",
        "target": "2506_14865",
        "weight": 0.8076
      }
    },
    {
      "data": {
        "id": "e3305",
        "source": "2410_23916",
        "target": "2506_22087",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e3306",
        "source": "2410_23916",
        "target": "2511_11308",
        "weight": 0.8523
      }
    },
    {
      "data": {
        "id": "e3307",
        "source": "2410_23916",
        "target": "2602_03639",
        "weight": 0.814
      }
    },
    {
      "data": {
        "id": "e3308",
        "source": "2410_23916",
        "target": "2603_00871",
        "weight": 0.8038
      }
    },
    {
      "data": {
        "id": "e3309",
        "source": "2410_23916",
        "target": "2603_05385",
        "weight": 0.8211
      }
    },
    {
      "data": {
        "id": "e3310",
        "source": "2410_23916",
        "target": "2603_24489",
        "weight": 0.8312
      }
    },
    {
      "data": {
        "id": "e3311",
        "source": "2410_23916",
        "target": "2604_01477",
        "weight": 0.823
      }
    },
    {
      "data": {
        "id": "e3312",
        "source": "2411_02158",
        "target": "2505_05588",
        "weight": 0.7905
      }
    },
    {
      "data": {
        "id": "e3313",
        "source": "2411_02158",
        "target": "2511_14752",
        "weight": 0.7942
      }
    },
    {
      "data": {
        "id": "e3314",
        "source": "2411_03277",
        "target": "2603_16808",
        "weight": 0.6948
      }
    },
    {
      "data": {
        "id": "e3315",
        "source": "2411_11833",
        "target": "2602_02846",
        "weight": 0.8334
      }
    },
    {
      "data": {
        "id": "e3316",
        "source": "2411_11833",
        "target": "2604_13323",
        "weight": 0.8071
      }
    },
    {
      "data": {
        "id": "e3317",
        "source": "2411_11833",
        "target": "2503_06757",
        "weight": 0.8177
      }
    },
    {
      "data": {
        "id": "e3318",
        "source": "2411_11833",
        "target": "2603_10711",
        "weight": 0.8378
      }
    },
    {
      "data": {
        "id": "e3319",
        "source": "2411_11833",
        "target": "2505_06791",
        "weight": 0.8229
      }
    },
    {
      "data": {
        "id": "e3320",
        "source": "2411_15651",
        "target": "2604_12149",
        "weight": 0.8223
      }
    },
    {
      "data": {
        "id": "e3321",
        "source": "2411_15651",
        "target": "2411_17902",
        "weight": 0.8063
      }
    },
    {
      "data": {
        "id": "e3322",
        "source": "2411_15651",
        "target": "2412_11270",
        "weight": 0.8815
      }
    },
    {
      "data": {
        "id": "e3323",
        "source": "2411_15651",
        "target": "2025_crestaz_td_cd_mppi_temporal",
        "weight": 0.8242
      }
    },
    {
      "data": {
        "id": "e3324",
        "source": "2411_15651",
        "target": "2502_09556",
        "weight": 0.8033
      }
    },
    {
      "data": {
        "id": "e3325",
        "source": "2411_15651",
        "target": "2503_05819",
        "weight": 0.8038
      }
    },
    {
      "data": {
        "id": "e3326",
        "source": "2411_15651",
        "target": "2503_16164",
        "weight": 0.8338
      }
    },
    {
      "data": {
        "id": "e3327",
        "source": "2411_15651",
        "target": "2506_21205",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e3328",
        "source": "2411_15651",
        "target": "2508_21001",
        "weight": 0.8611
      }
    },
    {
      "data": {
        "id": "e3329",
        "source": "2411_15651",
        "target": "2508_21800",
        "weight": 0.8342
      }
    },
    {
      "data": {
        "id": "e3330",
        "source": "2411_15651",
        "target": "2509_21961",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e3331",
        "source": "2411_15651",
        "target": "2510_21074",
        "weight": 0.8096
      }
    },
    {
      "data": {
        "id": "e3332",
        "source": "2411_15651",
        "target": "2511_18170",
        "weight": 0.816
      }
    },
    {
      "data": {
        "id": "e3333",
        "source": "2411_15651",
        "target": "2603_06773",
        "weight": 0.8067
      }
    },
    {
      "data": {
        "id": "e3334",
        "source": "2411_15651",
        "target": "2603_24489",
        "weight": 0.8028
      }
    },
    {
      "data": {
        "id": "e3335",
        "source": "2411_17293",
        "target": "2508_21001",
        "weight": 0.8091
      }
    },
    {
      "data": {
        "id": "e3336",
        "source": "2411_17293",
        "target": "2603_06773",
        "weight": 0.8269
      }
    },
    {
      "data": {
        "id": "e3337",
        "source": "2411_17902",
        "target": "2503_06757",
        "weight": 0.8257
      }
    },
    {
      "data": {
        "id": "e3338",
        "source": "2411_17902",
        "target": "2503_16164",
        "weight": 0.8221
      }
    },
    {
      "data": {
        "id": "e3339",
        "source": "2411_17902",
        "target": "2505_10542",
        "weight": 0.838
      }
    },
    {
      "data": {
        "id": "e3340",
        "source": "2411_17902",
        "target": "2508_21001",
        "weight": 0.8404
      }
    },
    {
      "data": {
        "id": "e3341",
        "source": "2411_17902",
        "target": "2510_21074",
        "weight": 0.8061
      }
    },
    {
      "data": {
        "id": "e3342",
        "source": "2411_17902",
        "target": "2602_02846",
        "weight": 0.8372
      }
    },
    {
      "data": {
        "id": "e3343",
        "source": "2411_18714",
        "target": "2604_07944",
        "weight": 0.8088
      }
    },
    {
      "data": {
        "id": "e3344",
        "source": "2411_18714",
        "target": "2604_08266",
        "weight": 0.8173
      }
    },
    {
      "data": {
        "id": "e3345",
        "source": "2411_18714",
        "target": "2511_00088",
        "weight": 0.8337
      }
    },
    {
      "data": {
        "id": "e3346",
        "source": "2411_18714",
        "target": "2412_14415",
        "weight": 0.8116
      }
    },
    {
      "data": {
        "id": "e3347",
        "source": "2412_11270",
        "target": "2604_12149",
        "weight": 0.8092
      }
    },
    {
      "data": {
        "id": "e3348",
        "source": "2412_11270",
        "target": "2503_16164",
        "weight": 0.8356
      }
    },
    {
      "data": {
        "id": "e3349",
        "source": "2412_11270",
        "target": "2506_14865",
        "weight": 0.8029
      }
    },
    {
      "data": {
        "id": "e3350",
        "source": "2412_11270",
        "target": "2506_22087",
        "weight": 0.8085
      }
    },
    {
      "data": {
        "id": "e3351",
        "source": "2412_11270",
        "target": "2508_21001",
        "weight": 0.8599
      }
    },
    {
      "data": {
        "id": "e3352",
        "source": "2412_11270",
        "target": "2508_21800",
        "weight": 0.8423
      }
    },
    {
      "data": {
        "id": "e3353",
        "source": "2412_11270",
        "target": "2511_18170",
        "weight": 0.8043
      }
    },
    {
      "data": {
        "id": "e3354",
        "source": "2412_11270",
        "target": "2603_06773",
        "weight": 0.8225
      }
    },
    {
      "data": {
        "id": "e3355",
        "source": "2412_11270",
        "target": "2603_24489",
        "weight": 0.8051
      }
    },
    {
      "data": {
        "id": "e3356",
        "source": "2412_12036",
        "target": "2603_23465",
        "weight": 0.8056
      }
    },
    {
      "data": {
        "id": "e3357",
        "source": "2412_14415",
        "target": "2604_07944",
        "weight": 0.8515
      }
    },
    {
      "data": {
        "id": "e3358",
        "source": "2412_14415",
        "target": "2604_08266",
        "weight": 0.8156
      }
    },
    {
      "data": {
        "id": "e3359",
        "source": "2412_14415",
        "target": "2412_17920",
        "weight": 0.8047
      }
    },
    {
      "data": {
        "id": "e3360",
        "source": "2412_14415",
        "target": "2502_08664",
        "weight": 0.8075
      }
    },
    {
      "data": {
        "id": "e3361",
        "source": "2412_14415",
        "target": "2503_03262",
        "weight": 0.8251
      }
    },
    {
      "data": {
        "id": "e3362",
        "source": "2412_14415",
        "target": "2505_09074",
        "weight": 0.8561
      }
    },
    {
      "data": {
        "id": "e3363",
        "source": "2412_14415",
        "target": "2509_21961",
        "weight": 0.8149
      }
    },
    {
      "data": {
        "id": "e3364",
        "source": "2412_14415",
        "target": "2511_00088",
        "weight": 0.8517
      }
    },
    {
      "data": {
        "id": "e3365",
        "source": "2412_17920",
        "target": "2509_21961",
        "weight": 0.8115
      }
    },
    {
      "data": {
        "id": "e3366",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2604_12149",
        "weight": 0.8095
      }
    },
    {
      "data": {
        "id": "e3367",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2025_lee_time_correlated_model_predictive",
        "weight": 0.8834
      }
    },
    {
      "data": {
        "id": "e3368",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2025_trevisan_model_predictive_path_integral",
        "weight": 0.82
      }
    },
    {
      "data": {
        "id": "e3369",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2503_05819",
        "weight": 0.8157
      }
    },
    {
      "data": {
        "id": "e3370",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2503_11717",
        "weight": 0.8636
      }
    },
    {
      "data": {
        "id": "e3371",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2504_06437",
        "weight": 0.8492
      }
    },
    {
      "data": {
        "id": "e3372",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2505_05507",
        "weight": 0.8084
      }
    },
    {
      "data": {
        "id": "e3373",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2506_21205",
        "weight": 0.8444
      }
    },
    {
      "data": {
        "id": "e3374",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2508_21364",
        "weight": 0.8154
      }
    },
    {
      "data": {
        "id": "e3375",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2509_14978",
        "weight": 0.8301
      }
    },
    {
      "data": {
        "id": "e3376",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2510_00272",
        "weight": 0.8556
      }
    },
    {
      "data": {
        "id": "e3377",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2511_02015",
        "weight": 0.865
      }
    },
    {
      "data": {
        "id": "e3378",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2511_11308",
        "weight": 0.818
      }
    },
    {
      "data": {
        "id": "e3379",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2511_18170",
        "weight": 0.8153
      }
    },
    {
      "data": {
        "id": "e3380",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2602_03639",
        "weight": 0.8625
      }
    },
    {
      "data": {
        "id": "e3381",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2603_05385",
        "weight": 0.8578
      }
    },
    {
      "data": {
        "id": "e3382",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2603_24489",
        "weight": 0.8786
      }
    },
    {
      "data": {
        "id": "e3383",
        "source": "2025_crestaz_td_cd_mppi_temporal",
        "target": "2604_01477",
        "weight": 0.8363
      }
    },
    {
      "data": {
        "id": "e3384",
        "source": "2025_hu_technically_speaking_transitioning_from",
        "target": "2502_08664",
        "weight": 0.8135
      }
    },
    {
      "data": {
        "id": "e3385",
        "source": "2025_hu_technically_speaking_transitioning_from",
        "target": "2604_07944",
        "weight": 0.8266
      }
    },
    {
      "data": {
        "id": "e3386",
        "source": "2025_hu_technically_speaking_transitioning_from",
        "target": "2604_08266",
        "weight": 0.8307
      }
    },
    {
      "data": {
        "id": "e3387",
        "source": "2025_hu_technically_speaking_transitioning_from",
        "target": "2511_00088",
        "weight": 0.845
      }
    },
    {
      "data": {
        "id": "e3388",
        "source": "2025_hu_technically_speaking_transitioning_from",
        "target": "2505_09074",
        "weight": 0.8346
      }
    },
    {
      "data": {
        "id": "e3389",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2604_12149",
        "weight": 0.8182
      }
    },
    {
      "data": {
        "id": "e3390",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2604_13312",
        "weight": 0.8031
      }
    },
    {
      "data": {
        "id": "e3391",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2025_trevisan_model_predictive_path_integral",
        "weight": 0.8237
      }
    },
    {
      "data": {
        "id": "e3392",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2503_05819",
        "weight": 0.8567
      }
    },
    {
      "data": {
        "id": "e3393",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2503_11717",
        "weight": 0.8966
      }
    },
    {
      "data": {
        "id": "e3394",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2504_06437",
        "weight": 0.8218
      }
    },
    {
      "data": {
        "id": "e3395",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2505_05507",
        "weight": 0.8505
      }
    },
    {
      "data": {
        "id": "e3396",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2506_21205",
        "weight": 0.8179
      }
    },
    {
      "data": {
        "id": "e3397",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2509_14978",
        "weight": 0.8117
      }
    },
    {
      "data": {
        "id": "e3398",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2510_00272",
        "weight": 0.8417
      }
    },
    {
      "data": {
        "id": "e3399",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2511_02015",
        "weight": 0.8605
      }
    },
    {
      "data": {
        "id": "e3400",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2511_18170",
        "weight": 0.8017
      }
    },
    {
      "data": {
        "id": "e3401",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2602_03639",
        "weight": 0.8798
      }
    },
    {
      "data": {
        "id": "e3402",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2603_05385",
        "weight": 0.8597
      }
    },
    {
      "data": {
        "id": "e3403",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2603_16059",
        "weight": 0.8034
      }
    },
    {
      "data": {
        "id": "e3404",
        "source": "2025_lee_time_correlated_model_predictive",
        "target": "2603_24489",
        "weight": 0.8506
      }
    },
    {
      "data": {
        "id": "e3405",
        "source": "2025_trevisan_model_predictive_path_integral",
        "target": "2503_11717",
        "weight": 0.8047
      }
    },
    {
      "data": {
        "id": "e3406",
        "source": "2025_trevisan_model_predictive_path_integral",
        "target": "2504_06437",
        "weight": 0.8038
      }
    },
    {
      "data": {
        "id": "e3407",
        "source": "2025_trevisan_model_predictive_path_integral",
        "target": "2506_21205",
        "weight": 0.835
      }
    },
    {
      "data": {
        "id": "e3408",
        "source": "2025_trevisan_model_predictive_path_integral",
        "target": "2508_21364",
        "weight": 0.8246
      }
    },
    {
      "data": {
        "id": "e3409",
        "source": "2025_trevisan_model_predictive_path_integral",
        "target": "2509_14978",
        "weight": 0.8261
      }
    },
    {
      "data": {
        "id": "e3410",
        "source": "2025_trevisan_model_predictive_path_integral",
        "target": "2510_00272",
        "weight": 0.8066
      }
    },
    {
      "data": {
        "id": "e3411",
        "source": "2025_trevisan_model_predictive_path_integral",
        "target": "2511_02015",
        "weight": 0.8072
      }
    },
    {
      "data": {
        "id": "e3412",
        "source": "2025_trevisan_model_predictive_path_integral",
        "target": "2511_18170",
        "weight": 0.8059
      }
    },
    {
      "data": {
        "id": "e3413",
        "source": "2025_trevisan_model_predictive_path_integral",
        "target": "2602_03639",
        "weight": 0.8027
      }
    },
    {
      "data": {
        "id": "e3414",
        "source": "2025_trevisan_model_predictive_path_integral",
        "target": "2603_05385",
        "weight": 0.8115
      }
    },
    {
      "data": {
        "id": "e3415",
        "source": "2025_trevisan_model_predictive_path_integral",
        "target": "2603_24489",
        "weight": 0.8093
      }
    },
    {
      "data": {
        "id": "e3416",
        "source": "2501_05204",
        "target": "2507_05331",
        "weight": 0.7527
      }
    },
    {
      "data": {
        "id": "e3417",
        "source": "2501_05204",
        "target": "2604_08508",
        "weight": 0.789
      }
    },
    {
      "data": {
        "id": "e3418",
        "source": "2501_05204",
        "target": "2503_04613",
        "weight": 0.7769
      }
    },
    {
      "data": {
        "id": "e3419",
        "source": "2501_05204",
        "target": "2603_14392",
        "weight": 0.7523
      }
    },
    {
      "data": {
        "id": "e3420",
        "source": "2501_05204",
        "target": "2604_04539",
        "weight": 0.7622
      }
    },
    {
      "data": {
        "id": "e3421",
        "source": "2502_04799",
        "target": "2511_10626",
        "weight": 0.815
      }
    },
    {
      "data": {
        "id": "e3422",
        "source": "2502_04799",
        "target": "2506_05454",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e3423",
        "source": "2502_08664",
        "target": "2503_03262",
        "weight": 0.9211
      }
    },
    {
      "data": {
        "id": "e3424",
        "source": "2502_08664",
        "target": "2511_00088",
        "weight": 0.8064
      }
    },
    {
      "data": {
        "id": "e3425",
        "source": "2502_08664",
        "target": "2511_00814",
        "weight": 0.8091
      }
    },
    {
      "data": {
        "id": "e3426",
        "source": "2502_08664",
        "target": "2505_09074",
        "weight": 0.8922
      }
    },
    {
      "data": {
        "id": "e3427",
        "source": "2502_08844",
        "target": "2503_04613",
        "weight": 0.8196
      }
    },
    {
      "data": {
        "id": "e3428",
        "source": "2502_08844",
        "target": "2604_04310",
        "weight": 0.7985
      }
    },
    {
      "data": {
        "id": "e3429",
        "source": "2502_08844",
        "target": "2506_17184",
        "weight": 0.7956
      }
    },
    {
      "data": {
        "id": "e3430",
        "source": "2502_08844",
        "target": "2604_05226",
        "weight": 0.7976
      }
    },
    {
      "data": {
        "id": "e3431",
        "source": "2502_09556",
        "target": "2510_21074",
        "weight": 0.8205
      }
    },
    {
      "data": {
        "id": "e3432",
        "source": "2502_12310",
        "target": "2602_03639",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e3433",
        "source": "2502_12310",
        "target": "2602_18933",
        "weight": 0.8048
      }
    },
    {
      "data": {
        "id": "e3434",
        "source": "2502_12310",
        "target": "2503_00385",
        "weight": 0.8064
      }
    },
    {
      "data": {
        "id": "e3435",
        "source": "2502_12310",
        "target": "2604_10635",
        "weight": 0.8262
      }
    },
    {
      "data": {
        "id": "e3436",
        "source": "2502_12310",
        "target": "2503_24371",
        "weight": 0.9295
      }
    },
    {
      "data": {
        "id": "e3437",
        "source": "2502_12310",
        "target": "2603_14197",
        "weight": 0.9285
      }
    },
    {
      "data": {
        "id": "e3438",
        "source": "2502_12310",
        "target": "2604_24442",
        "weight": 0.8178
      }
    },
    {
      "data": {
        "id": "e3439",
        "source": "2503_00385",
        "target": "2604_10635",
        "weight": 0.8421
      }
    },
    {
      "data": {
        "id": "e3440",
        "source": "2503_00385",
        "target": "2604_24442",
        "weight": 0.8099
      }
    },
    {
      "data": {
        "id": "e3441",
        "source": "2503_00385",
        "target": "2503_24371",
        "weight": 0.8376
      }
    },
    {
      "data": {
        "id": "e3442",
        "source": "2503_00385",
        "target": "2506_05454",
        "weight": 0.8291
      }
    },
    {
      "data": {
        "id": "e3443",
        "source": "2503_00385",
        "target": "2506_22087",
        "weight": 0.8084
      }
    },
    {
      "data": {
        "id": "e3444",
        "source": "2503_00385",
        "target": "2511_02095",
        "weight": 0.8455
      }
    },
    {
      "data": {
        "id": "e3445",
        "source": "2503_00385",
        "target": "2511_11131",
        "weight": 0.8775
      }
    },
    {
      "data": {
        "id": "e3446",
        "source": "2503_00385",
        "target": "2511_11308",
        "weight": 0.8399
      }
    },
    {
      "data": {
        "id": "e3447",
        "source": "2503_00385",
        "target": "2602_03639",
        "weight": 0.8061
      }
    },
    {
      "data": {
        "id": "e3448",
        "source": "2503_00385",
        "target": "2602_18933",
        "weight": 0.8697
      }
    },
    {
      "data": {
        "id": "e3449",
        "source": "2503_00385",
        "target": "2603_04843",
        "weight": 0.803
      }
    },
    {
      "data": {
        "id": "e3450",
        "source": "2503_00385",
        "target": "2603_14197",
        "weight": 0.8303
      }
    },
    {
      "data": {
        "id": "e3451",
        "source": "2503_00385",
        "target": "2603_24489",
        "weight": 0.8037
      }
    },
    {
      "data": {
        "id": "e3452",
        "source": "2503_00385",
        "target": "2604_05088",
        "weight": 0.833
      }
    },
    {
      "data": {
        "id": "e3453",
        "source": "2503_03262",
        "target": "2505_09074",
        "weight": 0.8997
      }
    },
    {
      "data": {
        "id": "e3454",
        "source": "2503_03262",
        "target": "2509_21961",
        "weight": 0.8165
      }
    },
    {
      "data": {
        "id": "e3455",
        "source": "2503_03262",
        "target": "2511_00088",
        "weight": 0.8147
      }
    },
    {
      "data": {
        "id": "e3456",
        "source": "2503_03262",
        "target": "2511_00814",
        "weight": 0.8107
      }
    },
    {
      "data": {
        "id": "e3457",
        "source": "2503_03262",
        "target": "2511_18170",
        "weight": 0.8171
      }
    },
    {
      "data": {
        "id": "e3458",
        "source": "2503_04613",
        "target": "2507_19652",
        "weight": 0.8272
      }
    },
    {
      "data": {
        "id": "e3459",
        "source": "2503_04613",
        "target": "2604_08508",
        "weight": 0.8577
      }
    },
    {
      "data": {
        "id": "e3460",
        "source": "2503_04613",
        "target": "2506_17184",
        "weight": 0.8214
      }
    },
    {
      "data": {
        "id": "e3461",
        "source": "2503_05819",
        "target": "2604_12149",
        "weight": 0.8656
      }
    },
    {
      "data": {
        "id": "e3462",
        "source": "2503_05819",
        "target": "2503_11717",
        "weight": 0.8431
      }
    },
    {
      "data": {
        "id": "e3463",
        "source": "2503_05819",
        "target": "2506_17184",
        "weight": 0.8025
      }
    },
    {
      "data": {
        "id": "e3464",
        "source": "2503_05819",
        "target": "2509_21961",
        "weight": 0.8007
      }
    },
    {
      "data": {
        "id": "e3465",
        "source": "2503_05819",
        "target": "2510_00272",
        "weight": 0.8035
      }
    },
    {
      "data": {
        "id": "e3466",
        "source": "2503_05819",
        "target": "2511_02015",
        "weight": 0.8388
      }
    },
    {
      "data": {
        "id": "e3467",
        "source": "2503_05819",
        "target": "2602_03639",
        "weight": 0.8484
      }
    },
    {
      "data": {
        "id": "e3468",
        "source": "2503_05819",
        "target": "2603_05385",
        "weight": 0.8371
      }
    },
    {
      "data": {
        "id": "e3469",
        "source": "2503_05819",
        "target": "2603_06773",
        "weight": 0.8078
      }
    },
    {
      "data": {
        "id": "e3470",
        "source": "2503_05819",
        "target": "2603_24489",
        "weight": 0.8428
      }
    },
    {
      "data": {
        "id": "e3471",
        "source": "2503_05819",
        "target": "2604_01477",
        "weight": 0.8125
      }
    },
    {
      "data": {
        "id": "e3472",
        "source": "2503_06135",
        "target": "2505_09074",
        "weight": 0.8098
      }
    },
    {
      "data": {
        "id": "e3473",
        "source": "2503_06135",
        "target": "2505_21851",
        "weight": 0.8367
      }
    },
    {
      "data": {
        "id": "e3474",
        "source": "2503_06135",
        "target": "2506_14865",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e3475",
        "source": "2503_06135",
        "target": "2508_21001",
        "weight": 0.8282
      }
    },
    {
      "data": {
        "id": "e3476",
        "source": "2503_06135",
        "target": "2508_21800",
        "weight": 0.812
      }
    },
    {
      "data": {
        "id": "e3477",
        "source": "2503_06135",
        "target": "2509_21961",
        "weight": 0.8619
      }
    },
    {
      "data": {
        "id": "e3478",
        "source": "2503_06135",
        "target": "2511_00814",
        "weight": 0.8056
      }
    },
    {
      "data": {
        "id": "e3479",
        "source": "2503_06135",
        "target": "2511_18170",
        "weight": 0.8056
      }
    },
    {
      "data": {
        "id": "e3480",
        "source": "2503_06135",
        "target": "2603_06773",
        "weight": 0.8056
      }
    },
    {
      "data": {
        "id": "e3481",
        "source": "2503_06135",
        "target": "2603_14392",
        "weight": 0.8062
      }
    },
    {
      "data": {
        "id": "e3482",
        "source": "2503_06757",
        "target": "2604_13323",
        "weight": 0.8016
      }
    },
    {
      "data": {
        "id": "e3483",
        "source": "2503_06757",
        "target": "2505_06791",
        "weight": 0.9275
      }
    },
    {
      "data": {
        "id": "e3484",
        "source": "2503_06757",
        "target": "2505_10542",
        "weight": 0.858
      }
    },
    {
      "data": {
        "id": "e3485",
        "source": "2503_06757",
        "target": "2602_02846",
        "weight": 0.8344
      }
    },
    {
      "data": {
        "id": "e3486",
        "source": "2503_09722",
        "target": "2507_05331",
        "weight": 0.8252
      }
    },
    {
      "data": {
        "id": "e3487",
        "source": "2503_09722",
        "target": "2507_09061",
        "weight": 0.9063
      }
    },
    {
      "data": {
        "id": "e3488",
        "source": "2503_09722",
        "target": "2512_00453",
        "weight": 0.8104
      }
    },
    {
      "data": {
        "id": "e3489",
        "source": "2503_09722",
        "target": "2603_19968",
        "weight": 0.8028
      }
    },
    {
      "data": {
        "id": "e3490",
        "source": "2503_09722",
        "target": "2505_21851",
        "weight": 0.8543
      }
    },
    {
      "data": {
        "id": "e3491",
        "source": "2503_09722",
        "target": "2512_01809",
        "weight": 0.8158
      }
    },
    {
      "data": {
        "id": "e3492",
        "source": "2503_09722",
        "target": "2604_04539",
        "weight": 0.8148
      }
    },
    {
      "data": {
        "id": "e3493",
        "source": "2503_11717",
        "target": "2604_12149",
        "weight": 0.8021
      }
    },
    {
      "data": {
        "id": "e3494",
        "source": "2503_11717",
        "target": "2504_06437",
        "weight": 0.8264
      }
    },
    {
      "data": {
        "id": "e3495",
        "source": "2503_11717",
        "target": "2505_05507",
        "weight": 0.8404
      }
    },
    {
      "data": {
        "id": "e3496",
        "source": "2503_11717",
        "target": "2508_21364",
        "weight": 0.8258
      }
    },
    {
      "data": {
        "id": "e3497",
        "source": "2503_11717",
        "target": "2509_14978",
        "weight": 0.8261
      }
    },
    {
      "data": {
        "id": "e3498",
        "source": "2503_11717",
        "target": "2510_00272",
        "weight": 0.8327
      }
    },
    {
      "data": {
        "id": "e3499",
        "source": "2503_11717",
        "target": "2511_02015",
        "weight": 0.8553
      }
    },
    {
      "data": {
        "id": "e3500",
        "source": "2503_11717",
        "target": "2602_03639",
        "weight": 0.8663
      }
    },
    {
      "data": {
        "id": "e3501",
        "source": "2503_11717",
        "target": "2603_05385",
        "weight": 0.8664
      }
    },
    {
      "data": {
        "id": "e3502",
        "source": "2503_11717",
        "target": "2603_24489",
        "weight": 0.8594
      }
    },
    {
      "data": {
        "id": "e3503",
        "source": "2503_16164",
        "target": "2505_10542",
        "weight": 0.8333
      }
    },
    {
      "data": {
        "id": "e3504",
        "source": "2503_16164",
        "target": "2508_21001",
        "weight": 0.8106
      }
    },
    {
      "data": {
        "id": "e3505",
        "source": "2503_16164",
        "target": "2510_21074",
        "weight": 0.8109
      }
    },
    {
      "data": {
        "id": "e3506",
        "source": "2503_24371",
        "target": "2602_18933",
        "weight": 0.8694
      }
    },
    {
      "data": {
        "id": "e3507",
        "source": "2503_24371",
        "target": "2604_10635",
        "weight": 0.8576
      }
    },
    {
      "data": {
        "id": "e3508",
        "source": "2503_24371",
        "target": "2603_14197",
        "weight": 0.9434
      }
    },
    {
      "data": {
        "id": "e3509",
        "source": "2503_24371",
        "target": "2511_02095",
        "weight": 0.8534
      }
    },
    {
      "data": {
        "id": "e3510",
        "source": "2503_24371",
        "target": "2604_24442",
        "weight": 0.8078
      }
    },
    {
      "data": {
        "id": "e3511",
        "source": "2503_24371",
        "target": "2511_11131",
        "weight": 0.8403
      }
    },
    {
      "data": {
        "id": "e3512",
        "source": "2503_24371",
        "target": "2511_11308",
        "weight": 0.8276
      }
    },
    {
      "data": {
        "id": "e3513",
        "source": "2503_24371",
        "target": "2604_05088",
        "weight": 0.8156
      }
    },
    {
      "data": {
        "id": "e3514",
        "source": "2504_01766",
        "target": "2507_09061",
        "weight": 0.8093
      }
    },
    {
      "data": {
        "id": "e3515",
        "source": "2504_01766",
        "target": "2603_23465",
        "weight": 0.9373
      }
    },
    {
      "data": {
        "id": "e3516",
        "source": "2504_01766",
        "target": "2511_11131",
        "weight": 0.8017
      }
    },
    {
      "data": {
        "id": "e3517",
        "source": "2504_06437",
        "target": "2604_12149",
        "weight": 0.8149
      }
    },
    {
      "data": {
        "id": "e3518",
        "source": "2504_06437",
        "target": "2506_21205",
        "weight": 0.83
      }
    },
    {
      "data": {
        "id": "e3519",
        "source": "2504_06437",
        "target": "2508_21364",
        "weight": 0.8085
      }
    },
    {
      "data": {
        "id": "e3520",
        "source": "2504_06437",
        "target": "2509_14978",
        "weight": 0.8345
      }
    },
    {
      "data": {
        "id": "e3521",
        "source": "2504_06437",
        "target": "2510_00272",
        "weight": 0.8739
      }
    },
    {
      "data": {
        "id": "e3522",
        "source": "2504_06437",
        "target": "2511_02015",
        "weight": 0.8155
      }
    },
    {
      "data": {
        "id": "e3523",
        "source": "2504_06437",
        "target": "2511_11308",
        "weight": 0.8167
      }
    },
    {
      "data": {
        "id": "e3524",
        "source": "2504_06437",
        "target": "2511_18170",
        "weight": 0.8072
      }
    },
    {
      "data": {
        "id": "e3525",
        "source": "2504_06437",
        "target": "2602_03639",
        "weight": 0.8161
      }
    },
    {
      "data": {
        "id": "e3526",
        "source": "2504_06437",
        "target": "2603_05385",
        "weight": 0.8148
      }
    },
    {
      "data": {
        "id": "e3527",
        "source": "2504_06437",
        "target": "2603_11335",
        "weight": 0.8059
      }
    },
    {
      "data": {
        "id": "e3528",
        "source": "2504_06437",
        "target": "2603_24489",
        "weight": 0.8481
      }
    },
    {
      "data": {
        "id": "e3529",
        "source": "2504_12905",
        "target": "2505_08510",
        "weight": 0.8214
      }
    },
    {
      "data": {
        "id": "e3530",
        "source": "2504_18978",
        "target": "2506_14865",
        "weight": 0.8196
      }
    },
    {
      "data": {
        "id": "e3531",
        "source": "2504_18978",
        "target": "2510_22015",
        "weight": 0.8298
      }
    },
    {
      "data": {
        "id": "e3532",
        "source": "2504_18978",
        "target": "2511_14752",
        "weight": 0.8099
      }
    },
    {
      "data": {
        "id": "e3533",
        "source": "2504_18978",
        "target": "2603_00871",
        "weight": 0.8065
      }
    },
    {
      "data": {
        "id": "e3534",
        "source": "2504_18978",
        "target": "2604_01614",
        "weight": 0.8267
      }
    },
    {
      "data": {
        "id": "e3535",
        "source": "2504_18978",
        "target": "2603_11335",
        "weight": 0.8485
      }
    },
    {
      "data": {
        "id": "e3536",
        "source": "2504_18978",
        "target": "2603_16059",
        "weight": 0.8013
      }
    },
    {
      "data": {
        "id": "e3537",
        "source": "2504_18978",
        "target": "2603_24489",
        "weight": 0.8019
      }
    },
    {
      "data": {
        "id": "e3538",
        "source": "2505_05507",
        "target": "2602_03639",
        "weight": 0.8366
      }
    },
    {
      "data": {
        "id": "e3539",
        "source": "2505_05507",
        "target": "2603_05385",
        "weight": 0.8286
      }
    },
    {
      "data": {
        "id": "e3540",
        "source": "2505_05507",
        "target": "2511_02015",
        "weight": 0.8169
      }
    },
    {
      "data": {
        "id": "e3541",
        "source": "2505_05507",
        "target": "2603_24489",
        "weight": 0.828
      }
    },
    {
      "data": {
        "id": "e3542",
        "source": "2505_06791",
        "target": "2602_02846",
        "weight": 0.8072
      }
    },
    {
      "data": {
        "id": "e3543",
        "source": "2505_06791",
        "target": "2604_13323",
        "weight": 0.8004
      }
    },
    {
      "data": {
        "id": "e3544",
        "source": "2505_06791",
        "target": "2603_10711",
        "weight": 0.8281
      }
    },
    {
      "data": {
        "id": "e3545",
        "source": "2505_06791",
        "target": "2505_10542",
        "weight": 0.8208
      }
    },
    {
      "data": {
        "id": "e3546",
        "source": "2505_09074",
        "target": "2604_07944",
        "weight": 0.8229
      }
    },
    {
      "data": {
        "id": "e3547",
        "source": "2505_09074",
        "target": "2604_08266",
        "weight": 0.8015
      }
    },
    {
      "data": {
        "id": "e3548",
        "source": "2505_09074",
        "target": "2509_21961",
        "weight": 0.8127
      }
    },
    {
      "data": {
        "id": "e3549",
        "source": "2505_09074",
        "target": "2511_00088",
        "weight": 0.8446
      }
    },
    {
      "data": {
        "id": "e3550",
        "source": "2505_09074",
        "target": "2511_00814",
        "weight": 0.8315
      }
    },
    {
      "data": {
        "id": "e3551",
        "source": "2505_09074",
        "target": "2511_18170",
        "weight": 0.8294
      }
    },
    {
      "data": {
        "id": "e3552",
        "source": "2505_09074",
        "target": "2603_14392",
        "weight": 0.8338
      }
    },
    {
      "data": {
        "id": "e3553",
        "source": "2505_10542",
        "target": "2510_21074",
        "weight": 0.8115
      }
    },
    {
      "data": {
        "id": "e3554",
        "source": "2505_21851",
        "target": "2507_05331",
        "weight": 0.815
      }
    },
    {
      "data": {
        "id": "e3555",
        "source": "2505_21851",
        "target": "2507_09061",
        "weight": 0.8244
      }
    },
    {
      "data": {
        "id": "e3556",
        "source": "2505_21851",
        "target": "2512_01809",
        "weight": 0.8501
      }
    },
    {
      "data": {
        "id": "e3557",
        "source": "2505_21851",
        "target": "2604_04539",
        "weight": 0.8228
      }
    },
    {
      "data": {
        "id": "e3558",
        "source": "2506_05454",
        "target": "2604_14669",
        "weight": 0.8629
      }
    },
    {
      "data": {
        "id": "e3559",
        "source": "2506_11513",
        "target": "2511_10622",
        "weight": 0.7636
      }
    },
    {
      "data": {
        "id": "e3560",
        "source": "2506_14865",
        "target": "2604_13323",
        "weight": 0.8674
      }
    },
    {
      "data": {
        "id": "e3561",
        "source": "2506_14865",
        "target": "2602_00992",
        "weight": 0.818
      }
    },
    {
      "data": {
        "id": "e3562",
        "source": "2506_14865",
        "target": "2603_00871",
        "weight": 0.835
      }
    },
    {
      "data": {
        "id": "e3563",
        "source": "2506_14865",
        "target": "2603_10711",
        "weight": 0.8108
      }
    },
    {
      "data": {
        "id": "e3564",
        "source": "2506_14865",
        "target": "2603_11335",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e3565",
        "source": "2506_14865",
        "target": "2603_16059",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e3566",
        "source": "2506_14865",
        "target": "2604_01614",
        "weight": 0.8067
      }
    },
    {
      "data": {
        "id": "e3567",
        "source": "2506_17184",
        "target": "2603_05385",
        "weight": 0.8011
      }
    },
    {
      "data": {
        "id": "e3568",
        "source": "2506_17184",
        "target": "2604_04310",
        "weight": 0.8071
      }
    },
    {
      "data": {
        "id": "e3569",
        "source": "2506_21205",
        "target": "2604_12149",
        "weight": 0.8002
      }
    },
    {
      "data": {
        "id": "e3570",
        "source": "2506_21205",
        "target": "2508_21001",
        "weight": 0.8096
      }
    },
    {
      "data": {
        "id": "e3571",
        "source": "2506_21205",
        "target": "2508_21364",
        "weight": 0.8177
      }
    },
    {
      "data": {
        "id": "e3572",
        "source": "2506_21205",
        "target": "2509_14978",
        "weight": 0.8242
      }
    },
    {
      "data": {
        "id": "e3573",
        "source": "2506_21205",
        "target": "2510_00272",
        "weight": 0.8463
      }
    },
    {
      "data": {
        "id": "e3574",
        "source": "2506_21205",
        "target": "2511_00814",
        "weight": 0.8028
      }
    },
    {
      "data": {
        "id": "e3575",
        "source": "2506_21205",
        "target": "2511_02015",
        "weight": 0.812
      }
    },
    {
      "data": {
        "id": "e3576",
        "source": "2506_21205",
        "target": "2511_18170",
        "weight": 0.8521
      }
    },
    {
      "data": {
        "id": "e3577",
        "source": "2506_21205",
        "target": "2602_03639",
        "weight": 0.8169
      }
    },
    {
      "data": {
        "id": "e3578",
        "source": "2506_21205",
        "target": "2603_05385",
        "weight": 0.8153
      }
    },
    {
      "data": {
        "id": "e3579",
        "source": "2506_21205",
        "target": "2603_24489",
        "weight": 0.819
      }
    },
    {
      "data": {
        "id": "e3580",
        "source": "2506_22087",
        "target": "2603_14197",
        "weight": 0.8034
      }
    },
    {
      "data": {
        "id": "e3581",
        "source": "2506_22087",
        "target": "2511_11308",
        "weight": 0.8015
      }
    },
    {
      "data": {
        "id": "e3582",
        "source": "2507_05331",
        "target": "2507_09061",
        "weight": 0.8535
      }
    },
    {
      "data": {
        "id": "e3583",
        "source": "2507_05331",
        "target": "2604_08508",
        "weight": 0.8102
      }
    },
    {
      "data": {
        "id": "e3584",
        "source": "2507_05331",
        "target": "2603_06773",
        "weight": 0.8332
      }
    },
    {
      "data": {
        "id": "e3585",
        "source": "2507_05331",
        "target": "2603_19968",
        "weight": 0.8151
      }
    },
    {
      "data": {
        "id": "e3586",
        "source": "2507_05331",
        "target": "2512_01809",
        "weight": 0.8482
      }
    },
    {
      "data": {
        "id": "e3587",
        "source": "2507_05331",
        "target": "2604_04539",
        "weight": 0.8308
      }
    },
    {
      "data": {
        "id": "e3588",
        "source": "2507_05331",
        "target": "2604_05226",
        "weight": 0.8506
      }
    },
    {
      "data": {
        "id": "e3589",
        "source": "2507_09061",
        "target": "2512_00453",
        "weight": 0.816
      }
    },
    {
      "data": {
        "id": "e3590",
        "source": "2507_09061",
        "target": "2603_06773",
        "weight": 0.8175
      }
    },
    {
      "data": {
        "id": "e3591",
        "source": "2507_09061",
        "target": "2603_19968",
        "weight": 0.8151
      }
    },
    {
      "data": {
        "id": "e3592",
        "source": "2507_09061",
        "target": "2512_01809",
        "weight": 0.8052
      }
    },
    {
      "data": {
        "id": "e3593",
        "source": "2507_09061",
        "target": "2604_04539",
        "weight": 0.8231
      }
    },
    {
      "data": {
        "id": "e3594",
        "source": "2507_19652",
        "target": "2604_08508",
        "weight": 0.823
      }
    },
    {
      "data": {
        "id": "e3595",
        "source": "2508_05027",
        "target": "2602_02846",
        "weight": 0.801
      }
    },
    {
      "data": {
        "id": "e3596",
        "source": "2508_07400",
        "target": "2604_18578",
        "weight": 0.7983
      }
    },
    {
      "data": {
        "id": "e3597",
        "source": "2508_07400",
        "target": "2603_19968",
        "weight": 0.7847
      }
    },
    {
      "data": {
        "id": "e3598",
        "source": "2508_21001",
        "target": "2604_07944",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e3599",
        "source": "2508_21001",
        "target": "2508_21800",
        "weight": 0.8803
      }
    },
    {
      "data": {
        "id": "e3600",
        "source": "2508_21001",
        "target": "2509_21961",
        "weight": 0.8125
      }
    },
    {
      "data": {
        "id": "e3601",
        "source": "2508_21001",
        "target": "2511_18170",
        "weight": 0.8136
      }
    },
    {
      "data": {
        "id": "e3602",
        "source": "2508_21001",
        "target": "2602_00992",
        "weight": 0.8098
      }
    },
    {
      "data": {
        "id": "e3603",
        "source": "2508_21001",
        "target": "2602_02846",
        "weight": 0.8508
      }
    },
    {
      "data": {
        "id": "e3604",
        "source": "2508_21001",
        "target": "2603_06773",
        "weight": 0.8412
      }
    },
    {
      "data": {
        "id": "e3605",
        "source": "2508_21001",
        "target": "2603_12361",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e3606",
        "source": "2508_21001",
        "target": "2603_14392",
        "weight": 0.8047
      }
    },
    {
      "data": {
        "id": "e3607",
        "source": "2508_21001",
        "target": "2603_16059",
        "weight": 0.8354
      }
    },
    {
      "data": {
        "id": "e3608",
        "source": "2508_21364",
        "target": "2510_00272",
        "weight": 0.8049
      }
    },
    {
      "data": {
        "id": "e3609",
        "source": "2508_21364",
        "target": "2604_19452",
        "weight": 0.8075
      }
    },
    {
      "data": {
        "id": "e3610",
        "source": "2508_21364",
        "target": "2603_24489",
        "weight": 0.8042
      }
    },
    {
      "data": {
        "id": "e3611",
        "source": "2508_21800",
        "target": "2509_21961",
        "weight": 0.8144
      }
    },
    {
      "data": {
        "id": "e3612",
        "source": "2508_21800",
        "target": "2603_06773",
        "weight": 0.8221
      }
    },
    {
      "data": {
        "id": "e3613",
        "source": "2508_21800",
        "target": "2603_12361",
        "weight": 0.8259
      }
    },
    {
      "data": {
        "id": "e3614",
        "source": "2509_14978",
        "target": "2510_00272",
        "weight": 0.8589
      }
    },
    {
      "data": {
        "id": "e3615",
        "source": "2509_14978",
        "target": "2511_18170",
        "weight": 0.8078
      }
    },
    {
      "data": {
        "id": "e3616",
        "source": "2509_14978",
        "target": "2602_03639",
        "weight": 0.8263
      }
    },
    {
      "data": {
        "id": "e3617",
        "source": "2509_14978",
        "target": "2603_05385",
        "weight": 0.8157
      }
    },
    {
      "data": {
        "id": "e3618",
        "source": "2509_14978",
        "target": "2603_24489",
        "weight": 0.8203
      }
    },
    {
      "data": {
        "id": "e3619",
        "source": "2509_21961",
        "target": "2604_07944",
        "weight": 0.8119
      }
    },
    {
      "data": {
        "id": "e3620",
        "source": "2509_21961",
        "target": "2604_12149",
        "weight": 0.8073
      }
    },
    {
      "data": {
        "id": "e3621",
        "source": "2509_21961",
        "target": "2511_18170",
        "weight": 0.8207
      }
    },
    {
      "data": {
        "id": "e3622",
        "source": "2510_00272",
        "target": "2604_12149",
        "weight": 0.8007
      }
    },
    {
      "data": {
        "id": "e3623",
        "source": "2510_00272",
        "target": "2511_02015",
        "weight": 0.8183
      }
    },
    {
      "data": {
        "id": "e3624",
        "source": "2510_00272",
        "target": "2511_18170",
        "weight": 0.8135
      }
    },
    {
      "data": {
        "id": "e3625",
        "source": "2510_00272",
        "target": "2602_03639",
        "weight": 0.8423
      }
    },
    {
      "data": {
        "id": "e3626",
        "source": "2510_00272",
        "target": "2603_05385",
        "weight": 0.8208
      }
    },
    {
      "data": {
        "id": "e3627",
        "source": "2510_00272",
        "target": "2603_24489",
        "weight": 0.8278
      }
    },
    {
      "data": {
        "id": "e3628",
        "source": "2510_03745",
        "target": "2601_03220",
        "weight": 0.7352
      }
    },
    {
      "data": {
        "id": "e3629",
        "source": "2510_21074",
        "target": "2511_18170",
        "weight": 0.8081
      }
    },
    {
      "data": {
        "id": "e3630",
        "source": "2510_22015",
        "target": "2604_06406",
        "weight": 0.8282
      }
    },
    {
      "data": {
        "id": "e3631",
        "source": "2510_22015",
        "target": "2603_11335",
        "weight": 0.8231
      }
    },
    {
      "data": {
        "id": "e3632",
        "source": "2510_22015",
        "target": "2603_12361",
        "weight": 0.8243
      }
    },
    {
      "data": {
        "id": "e3633",
        "source": "2510_22015",
        "target": "2511_18170",
        "weight": 0.8032
      }
    },
    {
      "data": {
        "id": "e3634",
        "source": "2511_00088",
        "target": "2604_07944",
        "weight": 0.8497
      }
    },
    {
      "data": {
        "id": "e3635",
        "source": "2511_00088",
        "target": "2604_08266",
        "weight": 0.8751
      }
    },
    {
      "data": {
        "id": "e3636",
        "source": "2511_00814",
        "target": "2603_05385",
        "weight": 0.8033
      }
    },
    {
      "data": {
        "id": "e3637",
        "source": "2511_00814",
        "target": "2511_18170",
        "weight": 0.8118
      }
    },
    {
      "data": {
        "id": "e3638",
        "source": "2511_02015",
        "target": "2604_12149",
        "weight": 0.8344
      }
    },
    {
      "data": {
        "id": "e3639",
        "source": "2511_02015",
        "target": "2604_13312",
        "weight": 0.8013
      }
    },
    {
      "data": {
        "id": "e3640",
        "source": "2511_02015",
        "target": "2511_11308",
        "weight": 0.8076
      }
    },
    {
      "data": {
        "id": "e3641",
        "source": "2511_02015",
        "target": "2602_03639",
        "weight": 0.8866
      }
    },
    {
      "data": {
        "id": "e3642",
        "source": "2511_02015",
        "target": "2603_05385",
        "weight": 0.8726
      }
    },
    {
      "data": {
        "id": "e3643",
        "source": "2511_02015",
        "target": "2603_24489",
        "weight": 0.902
      }
    },
    {
      "data": {
        "id": "e3644",
        "source": "2511_02015",
        "target": "2604_01477",
        "weight": 0.8075
      }
    },
    {
      "data": {
        "id": "e3645",
        "source": "2511_02095",
        "target": "2604_10635",
        "weight": 0.8495
      }
    },
    {
      "data": {
        "id": "e3646",
        "source": "2511_02095",
        "target": "2511_11131",
        "weight": 0.8728
      }
    },
    {
      "data": {
        "id": "e3647",
        "source": "2511_02095",
        "target": "2511_11308",
        "weight": 0.8353
      }
    },
    {
      "data": {
        "id": "e3648",
        "source": "2511_02095",
        "target": "2602_18933",
        "weight": 0.8928
      }
    },
    {
      "data": {
        "id": "e3649",
        "source": "2511_02095",
        "target": "2603_14197",
        "weight": 0.8323
      }
    },
    {
      "data": {
        "id": "e3650",
        "source": "2511_02095",
        "target": "2604_05088",
        "weight": 0.8247
      }
    },
    {
      "data": {
        "id": "e3651",
        "source": "2511_06385",
        "target": "2604_04539",
        "weight": 0.7999
      }
    },
    {
      "data": {
        "id": "e3652",
        "source": "2511_10622",
        "target": "2511_10626",
        "weight": 0.8308
      }
    },
    {
      "data": {
        "id": "e3653",
        "source": "2511_10622",
        "target": "2511_14752",
        "weight": 0.8136
      }
    },
    {
      "data": {
        "id": "e3654",
        "source": "2511_11131",
        "target": "2604_10635",
        "weight": 0.8347
      }
    },
    {
      "data": {
        "id": "e3655",
        "source": "2511_11131",
        "target": "2604_24442",
        "weight": 0.8028
      }
    },
    {
      "data": {
        "id": "e3656",
        "source": "2511_11131",
        "target": "2511_11308",
        "weight": 0.8073
      }
    },
    {
      "data": {
        "id": "e3657",
        "source": "2511_11131",
        "target": "2602_18933",
        "weight": 0.8714
      }
    },
    {
      "data": {
        "id": "e3658",
        "source": "2511_11131",
        "target": "2603_14197",
        "weight": 0.8197
      }
    },
    {
      "data": {
        "id": "e3659",
        "source": "2511_11131",
        "target": "2604_05088",
        "weight": 0.8299
      }
    },
    {
      "data": {
        "id": "e3660",
        "source": "2511_11308",
        "target": "2604_10635",
        "weight": 0.8231
      }
    },
    {
      "data": {
        "id": "e3661",
        "source": "2511_11308",
        "target": "2604_11183",
        "weight": 0.8166
      }
    },
    {
      "data": {
        "id": "e3662",
        "source": "2511_11308",
        "target": "2604_12149",
        "weight": 0.8366
      }
    },
    {
      "data": {
        "id": "e3663",
        "source": "2511_11308",
        "target": "2602_03639",
        "weight": 0.842
      }
    },
    {
      "data": {
        "id": "e3664",
        "source": "2511_11308",
        "target": "2602_18933",
        "weight": 0.8291
      }
    },
    {
      "data": {
        "id": "e3665",
        "source": "2511_11308",
        "target": "2603_04843",
        "weight": 0.8057
      }
    },
    {
      "data": {
        "id": "e3666",
        "source": "2511_11308",
        "target": "2603_05385",
        "weight": 0.8101
      }
    },
    {
      "data": {
        "id": "e3667",
        "source": "2511_11308",
        "target": "2603_10711",
        "weight": 0.8127
      }
    },
    {
      "data": {
        "id": "e3668",
        "source": "2511_11308",
        "target": "2603_14197",
        "weight": 0.823
      }
    },
    {
      "data": {
        "id": "e3669",
        "source": "2511_11308",
        "target": "2603_24489",
        "weight": 0.8545
      }
    },
    {
      "data": {
        "id": "e3670",
        "source": "2511_11308",
        "target": "2604_00900",
        "weight": 0.8143
      }
    },
    {
      "data": {
        "id": "e3671",
        "source": "2511_11308",
        "target": "2604_01477",
        "weight": 0.8289
      }
    },
    {
      "data": {
        "id": "e3672",
        "source": "2511_14752",
        "target": "2603_00871",
        "weight": 0.8107
      }
    },
    {
      "data": {
        "id": "e3673",
        "source": "2511_14752",
        "target": "2603_11335",
        "weight": 0.8843
      }
    },
    {
      "data": {
        "id": "e3674",
        "source": "2511_14752",
        "target": "2603_24489",
        "weight": 0.8202
      }
    },
    {
      "data": {
        "id": "e3675",
        "source": "2511_18170",
        "target": "2604_12149",
        "weight": 0.8153
      }
    },
    {
      "data": {
        "id": "e3676",
        "source": "2511_18170",
        "target": "2601_14880",
        "weight": 0.8039
      }
    },
    {
      "data": {
        "id": "e3677",
        "source": "2512_00453",
        "target": "2603_06773",
        "weight": 0.798
      }
    },
    {
      "data": {
        "id": "e3678",
        "source": "2512_00453",
        "target": "2604_04539",
        "weight": 0.8035
      }
    },
    {
      "data": {
        "id": "e3679",
        "source": "2512_01809",
        "target": "2603_06773",
        "weight": 0.8163
      }
    },
    {
      "data": {
        "id": "e3680",
        "source": "2512_01809",
        "target": "2604_04539",
        "weight": 0.8146
      }
    },
    {
      "data": {
        "id": "e3681",
        "source": "2601_03220",
        "target": "2603_19968",
        "weight": 0.7598
      }
    },
    {
      "data": {
        "id": "e3682",
        "source": "2601_03220",
        "target": "2601_05525",
        "weight": 0.7551
      }
    },
    {
      "data": {
        "id": "e3683",
        "source": "2601_05525",
        "target": "2603_19968",
        "weight": 0.7374
      }
    },
    {
      "data": {
        "id": "e3684",
        "source": "2601_05525",
        "target": "2604_05226",
        "weight": 0.7399
      }
    },
    {
      "data": {
        "id": "e3685",
        "source": "2602_00992",
        "target": "2604_13323",
        "weight": 0.8496
      }
    },
    {
      "data": {
        "id": "e3686",
        "source": "2602_00992",
        "target": "2603_16059",
        "weight": 0.8231
      }
    },
    {
      "data": {
        "id": "e3687",
        "source": "2602_00992",
        "target": "2604_01614",
        "weight": 0.8571
      }
    },
    {
      "data": {
        "id": "e3688",
        "source": "2602_02846",
        "target": "2604_13323",
        "weight": 0.815
      }
    },
    {
      "data": {
        "id": "e3689",
        "source": "2602_02846",
        "target": "2603_10711",
        "weight": 0.8135
      }
    },
    {
      "data": {
        "id": "e3690",
        "source": "2602_02846",
        "target": "2603_16059",
        "weight": 0.8568
      }
    },
    {
      "data": {
        "id": "e3691",
        "source": "2602_02846",
        "target": "2604_04310",
        "weight": 0.8045
      }
    },
    {
      "data": {
        "id": "e3692",
        "source": "2602_03639",
        "target": "2604_10635",
        "weight": 0.8036
      }
    },
    {
      "data": {
        "id": "e3693",
        "source": "2602_03639",
        "target": "2604_12149",
        "weight": 0.8319
      }
    },
    {
      "data": {
        "id": "e3694",
        "source": "2602_03639",
        "target": "2604_13312",
        "weight": 0.8121
      }
    },
    {
      "data": {
        "id": "e3695",
        "source": "2602_03639",
        "target": "2603_05385",
        "weight": 0.8805
      }
    },
    {
      "data": {
        "id": "e3696",
        "source": "2602_03639",
        "target": "2603_23465",
        "weight": 0.8089
      }
    },
    {
      "data": {
        "id": "e3697",
        "source": "2602_03639",
        "target": "2603_24489",
        "weight": 0.9145
      }
    },
    {
      "data": {
        "id": "e3698",
        "source": "2602_03639",
        "target": "2604_00900",
        "weight": 0.8024
      }
    },
    {
      "data": {
        "id": "e3699",
        "source": "2602_03639",
        "target": "2604_01477",
        "weight": 0.8138
      }
    },
    {
      "data": {
        "id": "e3700",
        "source": "2602_18933",
        "target": "2604_10635",
        "weight": 0.8476
      }
    },
    {
      "data": {
        "id": "e3701",
        "source": "2602_18933",
        "target": "2603_14197",
        "weight": 0.8674
      }
    },
    {
      "data": {
        "id": "e3702",
        "source": "2602_18933",
        "target": "2604_05088",
        "weight": 0.8328
      }
    },
    {
      "data": {
        "id": "e3703",
        "source": "2602_19699",
        "target": "2604_04539",
        "weight": 0.8133
      }
    },
    {
      "data": {
        "id": "e3704",
        "source": "2603_00871",
        "target": "2604_13323",
        "weight": 0.8063
      }
    },
    {
      "data": {
        "id": "e3705",
        "source": "2603_00871",
        "target": "2603_10711",
        "weight": 0.8
      }
    },
    {
      "data": {
        "id": "e3706",
        "source": "2603_00871",
        "target": "2603_11335",
        "weight": 0.8185
      }
    },
    {
      "data": {
        "id": "e3707",
        "source": "2603_01176",
        "target": "2604_13312",
        "weight": 0.7876
      }
    },
    {
      "data": {
        "id": "e3708",
        "source": "2603_04843",
        "target": "2604_10635",
        "weight": 0.8194
      }
    },
    {
      "data": {
        "id": "e3709",
        "source": "2603_04843",
        "target": "2603_24489",
        "weight": 0.8093
      }
    },
    {
      "data": {
        "id": "e3710",
        "source": "2603_05385",
        "target": "2604_12149",
        "weight": 0.8019
      }
    },
    {
      "data": {
        "id": "e3711",
        "source": "2603_05385",
        "target": "2603_19968",
        "weight": 0.8173
      }
    },
    {
      "data": {
        "id": "e3712",
        "source": "2603_05385",
        "target": "2603_24489",
        "weight": 0.873
      }
    },
    {
      "data": {
        "id": "e3713",
        "source": "2603_06773",
        "target": "2604_12149",
        "weight": 0.8191
      }
    },
    {
      "data": {
        "id": "e3714",
        "source": "2603_06773",
        "target": "2604_14026",
        "weight": 0.8001
      }
    },
    {
      "data": {
        "id": "e3715",
        "source": "2603_06773",
        "target": "2603_14392",
        "weight": 0.8169
      }
    },
    {
      "data": {
        "id": "e3716",
        "source": "2603_06773",
        "target": "2604_04539",
        "weight": 0.8166
      }
    },
    {
      "data": {
        "id": "e3717",
        "source": "2603_08824",
        "target": "2604_04310",
        "weight": 0.7546
      }
    },
    {
      "data": {
        "id": "e3718",
        "source": "2603_10711",
        "target": "2604_13323",
        "weight": 0.805
      }
    },
    {
      "data": {
        "id": "e3719",
        "source": "2603_10711",
        "target": "2604_23951",
        "weight": 0.8105
      }
    },
    {
      "data": {
        "id": "e3720",
        "source": "2603_10711",
        "target": "2603_24489",
        "weight": 0.8183
      }
    },
    {
      "data": {
        "id": "e3721",
        "source": "2603_11335",
        "target": "2604_06406",
        "weight": 0.8123
      }
    },
    {
      "data": {
        "id": "e3722",
        "source": "2603_11335",
        "target": "2603_24489",
        "weight": 0.8128
      }
    },
    {
      "data": {
        "id": "e3723",
        "source": "2603_12361",
        "target": "2604_01614",
        "weight": 0.8064
      }
    },
    {
      "data": {
        "id": "e3724",
        "source": "2603_14197",
        "target": "2604_10635",
        "weight": 0.8301
      }
    },
    {
      "data": {
        "id": "e3725",
        "source": "2603_16059",
        "target": "2604_13323",
        "weight": 0.8493
      }
    },
    {
      "data": {
        "id": "e3726",
        "source": "2603_16059",
        "target": "2604_01614",
        "weight": 0.8185
      }
    },
    {
      "data": {
        "id": "e3727",
        "source": "2603_19968",
        "target": "2604_04539",
        "weight": 0.8007
      }
    },
    {
      "data": {
        "id": "e3728",
        "source": "2603_23465",
        "target": "2604_21270",
        "weight": 0.8114
      }
    },
    {
      "data": {
        "id": "e3729",
        "source": "2603_23465",
        "target": "2604_00900",
        "weight": 0.8052
      }
    },
    {
      "data": {
        "id": "e3730",
        "source": "2603_24489",
        "target": "2604_12149",
        "weight": 0.8378
      }
    },
    {
      "data": {
        "id": "e3731",
        "source": "2603_24489",
        "target": "2604_13312",
        "weight": 0.8185
      }
    },
    {
      "data": {
        "id": "e3732",
        "source": "2603_24489",
        "target": "2604_01477",
        "weight": 0.8309
      }
    },
    {
      "data": {
        "id": "e3733",
        "source": "2603_28052",
        "target": "2604_07944",
        "weight": 0.7495
      }
    },
    {
      "data": {
        "id": "e3734",
        "source": "2603_28052",
        "target": "2604_08266",
        "weight": 0.7576
      }
    },
    {
      "data": {
        "id": "e3735",
        "source": "2603_28052",
        "target": "2604_05226",
        "weight": 0.7558
      }
    },
    {
      "data": {
        "id": "e3736",
        "source": "2604_00900",
        "target": "2604_01477",
        "weight": 0.8235
      }
    },
    {
      "data": {
        "id": "e3737",
        "source": "2604_01477",
        "target": "2604_12149",
        "weight": 0.8101
      }
    },
    {
      "data": {
        "id": "e3738",
        "source": "2604_01614",
        "target": "2604_13323",
        "weight": 0.8446
      }
    },
    {
      "data": {
        "id": "e3739",
        "source": "2604_04310",
        "target": "2604_13323",
        "weight": 0.8132
      }
    },
    {
      "data": {
        "id": "e3740",
        "source": "2604_05088",
        "target": "2604_10635",
        "weight": 0.8176
      }
    },
    {
      "data": {
        "id": "e3741",
        "source": "2604_05885",
        "target": "2604_23951",
        "weight": 0.7585
      }
    },
    {
      "data": {
        "id": "e3742",
        "source": "2604_07944",
        "target": "2604_08266",
        "weight": 0.8871
      }
    },
    {
      "data": {
        "id": "e3743",
        "source": "2604_10635",
        "target": "2604_24442",
        "weight": 0.849
      }
    },
    {
      "data": {
        "id": "e3744",
        "source": "2604_13192",
        "target": "2604_24442",
        "weight": 0.7758
      }
    },
    {
      "data": {
        "id": "e3745",
        "source": "2604_21270",
        "target": "2604_24442",
        "weight": 0.7966
      }
    }
  ],
  "meta": {
    "model": "mixedbread-ai/mxbai-embed-large-v1",
    "threshold": 0.8,
    "top_k": 5,
    "total_papers": 402,
    "total_edges": 3746
  }
};
