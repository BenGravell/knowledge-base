<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SCTOMP: Spatially Constrained Time-Optimal Motion Planning

Topics include Motion planning, Time-optimal control, Trajectory optimization, Obstacle avoidance, Path planning, Path parameterization, Spatial planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Generalizes time-optimal path following by optimizing inside a spatial corridor instead of assuming a fixed collision-free reference path. SCTOMP combines corridor construction, smooth spline representation, and minimum-time optimization to produce dynamically feasible trajectories.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper focuses on spatial time-optimal motion planning, a generalization of the exact time-optimal path following problem that allows the system to plan within a predefined space. In contrast to state-of-the-art methods, we drop the assumption that a collision-free geometric reference is given. Instead, we present a two-stage motion planning method that solely relies on a goal location and a geometric representation of the environment to compute a time-optimal trajectory that is compliant with system dynamics and constraints. To do so, the proposed scheme first computes an obstacle-free Pythagorean Hodograph parametric spline, and second solves a spatially reformulated minimum-time optimization problem. The spline obtained in the first stage is not a geometric reference, but an extension of the environment representation, and thus, time-optimality of the solution is guaranteed. The efficacy of the proposed approach is benchmarked by a known planar example and validated in a more complex spatial system, illustrating its versatility and applicability.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Time-optimal motion planning within cluttered environments poses multiple challenges. The underlying motion planning scheme needs to compute a set of input commands that drive the system from its current state to a goal location in minimum-time, without compromising system constraints and spatial bounds. Thus, its solution implies a trading-off between time-optimality and spatial-awareness.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The de facto approach to solve this problem has been to decouple it into two stages. First, the *path planning* stage determines a collision-free geometric path according to high level -- task related -- commands. Second, the predefined path is (exactly) tracked either by *path tracking* or *path following*. The former computes a dynamically feasible timing law for traversing along the predetermined geometric path -- *when* to be *where* --, while the latter introduces the timing law and the (bounded) distance to the path as control freedoms.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

When tackling time-optimality, previous work mainly focused on the second stage. *Time-optimal path-tracking* for robotic manipulators is a long studied problem. Its convexity was proven in and in it was extended to a wider range of systems. Enhanced numerical implementations to exploit this convexity were presented. Regarding *time-optimal path-following*, leveraged a spatial reformulation of the system dynamics, allowing to compute minimum-time trajectories *around* the predefined path. Similarly, assuming waypoints to be predetermined, made use of Complementary Progress Constraints (CPC) to compute time-optimal trajectories for quadrotors. Lastly, exploiting optimal control, nonlinear model predictive control (NMPC) methods based on the aforementioned spatial reformulation and contouring control have shown to approximate time-optimal performance in race-alike scenarios, i.e., *around* a predefined geometric path (the centerline of the track). However, the optimality of all these approaches is upper bounded by the geometric reference predetermined by the path planning stage.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In other words, only if *both* the path planning and path tracking/following stages are optimal, will the resultant planned trajectory be optimal, implying that the decoupled nature of these methods jeopardizes the time-optimality of the planned trajectories.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

To overcome this conceptual shortcoming, presented a hierarchical sampling-based method capable of computing time-optimal trajectories to fly a quadrotor over a set of waypoints within cluttered environments. This was further extended, where planning and control were simultaneously solved with a deep Reinforcement Learning (deep RL) approach. Despite the ability to roughly approximate time-optimal trajectories in congested scenarios, none of these methods can guarantee that the resultant trajectory is the true-optimal. On the one hand, the sampling-based nature of renders it nondeterministic, introducing randomness into the solution. On the other hand, the additional tracking capabilities brought by the end-to-end learning approach in come at the expense of 1) system-specificity -- changes in the system dynamics require retraining -- and 2) sub-optimal trajectories resulting from learning the trade-off between flying safe and fast.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This raises the question on how to formulate a motion planning scheme, applicable to any system and constrained environment, that guarantees to compute the time-optimal trajectory compliant with system dynamics, state/input constraints and spatial bounds. To answer this question, in this paper we present a Spatially Constrained Time-Optimal Motion Planner (SCTOMP): an *offline* motion planning approach capable of *computing dynamically feasible, collision-free and time-optimal trajectories*, by solely relying on a goal location and a geometric representation of the obstacle-free environment.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

For this purpose, we formulate a three-stage approach, where, firstly collision-free navigation corridors are found, secondly parametric paths within all corridors are computed, and thirdly a spatially reformulated time minimization per corridor is solved. In contrast to the aforementioned decoupled approaches, the parametric paths obtained in the second stage are not a geometric reference, but an extension of the free space associated with the respective corridor, and consequently, have no effect on the optimality of the time-minimizing problem in the third stage.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The presented scheme consists of three main ingredients: 1) Through the use of a spatial reformulation presented, we perform a spatial transformation of the time-based system states to path coordinates. The resultant system dynamics evolve according to a *path parameter* $\xi$ instead of *time* $t$. 2) We leverage Pythagorean Hodograph curves to efficiently and analytically compute the parametric functions required by this spatial reformulation. 3) Using the first and second ingredients, the time minimization problem is reduced into a finite horizon spatial problem with convex spatial bounds.

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

More specifically, we make the following contributions: We extend the applicability of the spatial reformulation introduced, by showing how it allows to conduct a singularity-free spatial transformation of the dynamics for any arbitrary system.

<!-- chunk {"id": "body-0013", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We identify a computationally tractable methodology to compute Pythagorean Hodograph splines in a closed form, without the need for additional optimizations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We derive a motion planning methodology that, given a nonlinear system and constrained environment, finds the collision-free and dynamically feasible time-optimal trajectory.

<!-- chunk {"id": "body-0015", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The remainder of this paper is structured as follows: Section II introduces the spatially constrained time-optimal motion planning problem. Section III presents the solution proposed in this paper, by revisiting the aforementioned spatial reformulation, its compatibility with PH curves, and performing a spatial transformation of the time minimization problem. Experimental results are shown in Section IV before Section V presents the conclusions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

To ensure that the system remains in the obstacle free space, the geometrically constrained environment is described as where we also assume the function $g:{{\mathbb{R}}^{n_{y}}\mapsto{\mathbb{R}}^{n_{y}}}$ to be sufficiently continuously differentiable.

<!-- chunk {"id": "body-0017", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

Spatially Constrained Time-Optimal Motion Planning refers to the problem of planning a trajectory that steers system from its initial state ${\mathbf{x}}_{\mathbf{0}}$ to a goal output state ${\mathbf{y}}_{\mathbf{f}} \in {\mathbb{R}}^{n_{y}}$ in minimum-time, without compromising the system dynamics in (1a), ensuring the integrity of state and input constraints -- ${\mathbf{x}} \in \mathcal{X}$, ${\mathbf{u}} \in \mathcal{U}$ -- and guaranteeing that output (1b) remains within the free space, i.e., ${\mathbf{y}} \in \Omega$. This is equivalent to solving the following optimal control problem (OCP): As mentioned earlier, *decoupled* approaches separate this problem into a path planning and path tracking/following problem. The computational tractability advantages brought by these methods come at the expense of an inherited suboptimality in the planned trajectories.

<!-- chunk {"id": "body-0018", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

We seek to close this gap by formulating a method that *directly* solves the minimum-time problem, eliminating the need for the path planning stage, and thus leveraging the entire free space to compute the time-optimal trajectory.

<!-- chunk {"id": "body-0019", "role": "body", "section": "SOLUTION APPROACH", "weight": 1.0} -->

The motion planning scheme presented in this paper leverages (i) a *spatial transformation of the system dynamics* with respect to (ii) an *arbitrary parametric curve with an associated adapted frame* to perform (iii) a *spatial reformulation of the time-minimizing problem*. These three ingredients are the main building blocks of the proposed methodology. In this section, we present further details on each of them.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A SPATIAL TRANSFORMATION OF SYSTEM DYNAMICS", "weight": 1.0} -->

In we demonstrated that the equations of motion of the spatial coordinates -- progress along the path $\xi$ and the orthogonal distance to it ${\mathbf{w}} = \left\lbrack w_{1},w_{2} \right\rbrack$ -- associated to a point-mass moving at velocity ${\mathbf{v}} \in {\mathbb{R}}^{3}$ with respect to path $\Gamma$ are given by where $\sigma{(\cdot)}$ stands for the parametric speed of path $\Gamma$. For a better understanding of the spatial states, see Fig. 1. These states, alongside their respective equations of motion, allow for a projection of the Euclidean coordinates into the geometric path $\Gamma$, resulting in a change of coordinates. Doing so, embeds the geometric properties *around path $\Gamma$* into the system dynamics, and thus, it has become a very popular approach among recent path following methods.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A SPATIAL TRANSFORMATION OF SYSTEM DYNAMICS", "weight": 1.0} -->

Given that our solution aims to be agnostic from a geometric reference, we perform a spatial transformation of the system dynamics. To do so, we leverage the chain rule as follows: Noticing that $\frac{dt}{d\xi} = {1/\overset{˙}{\xi}}$ and assuming that $\overset{˙}{\xi} \neq 0$, is simplified into The resultant spatially transformed equations of motion for the dynamic system are where $\overset{˙}{\xi}{({{\mathbf{x}}{(\xi)}},{{\mathbf{u}}{(\xi)}})}$ is obtained from (5a). Comparing the *spatially transformed* system with respect to the original system, it becomes apparent that the dynamics evolve with respect to *path parameter $\xi$* instead of *time $t$*.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A SPATIAL TRANSFORMATION OF SYSTEM DYNAMICS", "weight": 1.0} -->

Transforming the system dynamics according to the chain rule is a mature technique. Nevertheless, to the best of the authors' knowledge, this is the first time that it is applied to the recently derived spatial reformulation. When doing so, the benefits of this reformulation are inherited by the transformed system. As opposed to state-of-the-art Frenet-Serret based reformulations, does not take any assumptions in its adapted frame, and as result, it overcomes the two major drawbacks of the Frenet-Serret frame: (i) *singularities* when the curvature vanishes and (ii) an *undesired twist* with respect to its tangent component.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B PYTHAGOREAN HODOGRAPH SPLINES", "weight": 1.0} -->

For a complete definition of the spatially transformed system, the *parametric functions* associated to $\xi$ -- the parametric speed $\sigma{(\xi)}$ and the adapted frame's rotation matrix $\text{R}{(\xi)}$ and angular velocity ${\mathbf{ω}}{(\xi)}$ -- need to be expressed in closed form. To this end, we employ Pythagorean Hodograph (PH) curves.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B1 Preliminaries on PH curves", "weight": 1.0} -->

PH curves are a subset of polynomial curves whose parametric speed is a polynomial of the path parameter $\xi$. Decomposing the components of ${\mathbf{γ}}{(\xi)}$ in into ${x{(\xi)}},{y{(\xi)}},{z{(\xi)}}$, the condition for a polynomial to be a PH curve is equivalent to where $\sigma{(\xi)}$ is a polynomial.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B1 Preliminaries on PH curves", "weight": 1.0} -->

As proven, every term in can be expressed in terms of a *quaternion polynomial* ${{\mathbf{Z}}{(\xi)}} = {{u{(\xi)}} + {v{(\xi)}\text{i}} + {g{(\xi)}\text{j}} + {h{(\xi)}\text{k}}}$ ^11^1$\{\text{i},\text{j},\text{k}\}$ refers to the ${\mathbb{R}}^{4}$ standard basis, whose components ${u{(\xi)}},{v{(\xi)}},{g{(\xi)}},{h{(\xi)}}$ are also polynomial functions of the path parameter $\xi$. Consequently, the parametric speed can be reformulated as Another notable benefit of PH curves is that they inherit a continuous adapted frame, denoted as *Euler Rodrigues Frame* (ERF), which also exclusively depends on its quaternion polynomial.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B1 Preliminaries on PH curves", "weight": 1.0} -->

Its respective rotation matrix is given by where ${(\cdot)}^{\ast}$ refers to the quaternion's conjugate. Finally, considering that the components of its angular velocity are expressed as the adapted frame's angular velocity ${\mathbf{ω}}{(\xi)}$ is likewise exclusively reliant on the quaternion polynomial.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B1 Preliminaries on PH curves", "weight": 1.0} -->

From, and, it can be stated that all *parametric functions* -- ${\sigma{(\xi)}},{\text{R}{(\xi)}},{{\mathbf{ω}}{(\xi)}}$ -- solely depend on the quaternion polynomial ${\mathbf{Z}}{(\xi)}$, and consequently, they are fully defined by the coefficients of the underlying polynomial functions ${u{(\xi)}},{v{(\xi)}},{g{(\xi)}},{h{(\xi)}}$. For convenience we will refer to these as *PH coefficients*, ${\mathbf{ζ}} \in {\mathbb{R}}^{n_{\zeta}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B1 Preliminaries on PH curves", "weight": 1.0} -->

Finally, notice that entails that a quaternion polynomial ${\mathbf{Z}}{(\xi)}$ of degree $n$ corresponds to a curve ${\mathbf{γ}}{(\xi)}$ of degree ${2n} + 1$, while relying just on $4{({n + 1})}$ PH coefficients. This implies that all three parametric functions, and hence the spatial reformulation underpinning system, are effectively encoded into a handful of coefficients.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B2 Efficiently computing collision-free PH splines", "weight": 1.0} -->

To ensure planning capabilities within highly non-convex and complex environments, we concatenate multiple PH curves into a *PH spline*. As mentioned before, the PH spline is not a geometric reference, but a parametric path that encodes the geometric properties of the environment into the spatially transformed system dynamics. Thus, as proven in the upcoming Section IV-A, it has no influence on the time-optimality of the computed trajectory. However, when choosing the PH spline the requirements are twofold: First, the parametric functions -- ${\sigma{(\xi)}},{\text{R}{(\xi)}},{{\mathbf{ω}}{(\xi)}}$ -- need to remain sufficiently often continuously differentiable, and second, it must be located within the obstacle-free space.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B2 Efficiently computing collision-free PH splines", "weight": 1.0} -->

For this purpose, reduces the amount of free PH coefficients according to the continuity conditions, and subsequently, tailors the shape of the PH spline based on a desired criterion by solving an optimization problem on the remaining coefficients. To ensure the integrity of the spatial bounds it performs a convex decomposition of the free space $\Omega$ and constraints the control points of each segment of the PH spline to be encompassed inside the associated convex set. These control points can readily be obtained from a function that takes the starting location of the spline and the PH coefficients as inputs. However, given that the coefficients relate to the hodograph, these constraints, as well as the cost function, are highly nonlinear and nonconvex, resulting in a large and numerically involved nonlinear program.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B2 Efficiently computing collision-free PH splines", "weight": 1.0} -->

To alleviate this burden, rather than executing a convex decomposition and directly computing a PH spline, the proposed methodology in the first-stage identifies all navigation corridors within the free-space ${\mathcal{C}} = {\{\mathcal{C}_{1},\ldots,\mathcal{C}_{m}\}} \subseteq \Omega$, and in the second-stage locates an arbitrary curve, enclosed within each of these corridors $\lambda_{1,\ldots,m}$, and transforms each of these curves into a PH spline whose coefficients are ${\mathcal{Z}}_{1,\ldots,m}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B2 Efficiently computing collision-free PH splines", "weight": 1.0} -->

The presented hierarchical methodology exhibits modularity in that the finding of the corridors, computation of the curves and the successive conversion algorithm are entirely decoupled. Specifically, the former can be carried out effectively by employing state-of-the-art planning algorithms, whereas for the latter, we expand upon the $C^{2}$ hermite interpolation algorithm outlined in to $C^{4}$. Given that the conversion algorithm is presented as a closed-form solution, it entails no computational cost, and the burden of solving the aforementioned intractable nonlinear program is diminished to identifying a collision-free curve.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-C TIME MINIMIZATION: A SPATIAL APPROACH", "weight": 1.0} -->

In order to encompass the entirety of the free space $\Omega$ and ensure time-optimality of the calculated trajectory, the third-stage of SCTOMP involves solving a time-minimizing OCP for all corridors $k = 1 \ldots,m$ and selecting the one with the minimum navigation time.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-C TIME MINIMIZATION: A SPATIAL APPROACH", "weight": 1.0} -->

At a given corridor $k$, the PH coefficients ${\mathcal{Z}}_{k}$ associated to the PH spline computed in the second-stage explicitly describe the parametric coefficients, and therefore, allow to rewrite the equation of motion of the spatially transformed system (7a) as This equation represents the spatially transformed dynamics model of a system whose temporal dynamics are given by $f$, with respect to a PH spline defined by PH coefficients ${\mathcal{Z}}_{k}$. In contrast to, the system in accounts for a method to compute the underlying parametric functions -- based on PH splines --, and thus, it is fully defined.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-C TIME MINIMIZATION: A SPATIAL APPROACH", "weight": 1.0} -->

Revisiting the fact that $\frac{dt}{d\xi} = {1/\overset{˙}{\xi}}$ and leveraging the spatially transformed system dynamics, the time-minimizing problem within the free space associated to corridor $k$ can be reformulated as A summary of the proposed motion planning scheme, showing the first, second- and third-stages is depicted in Algorithm 1.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-C TIME MINIMIZATION: A SPATIAL APPROACH", "weight": 1.0} -->

5: λk ← Find Collision-Free Path (x0, yf, 𝒞k) Algorithm 1 Spatially Constrained Time-Optimal Motion Planning (SCTOMP): Given state x0, goal yf and environment Ω, find the time-optimal set of states and inputs x*, u*

<!-- chunk {"id": "body-0037", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

To evaluate our approach, we divide the experimental analysis into two parts, including systems with different dynamics. First, we test SCTOMP by analyzing its performance in a well-known single-corridor planar scenario (2D, Sec. IV-A), demonstrating that the proposed scheme remains time-optimal regardless of the underlying PH spline. Secondly, the evaluation is expanded to a spatial system (3D, Sec. IV-B) and compared against existing state-of-the-art approaches in a range of case-studies across two different cluttered environments.

<!-- chunk {"id": "body-0038", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

*Numerical implementation:* The OCP is modeled in CasADi and solved by IPOPT after being approximated by a multiple-shooting approach, where the optimization horizon $\xi_{f} - \xi_{0}$ is discretized into sections with constant decision variables. The integration routines respective to the dynamic constraints (13c) are approximated by a 4th-order Runge-Kutta method.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A PLANAR SYSTEM IN SINGLE-CORRIDOR SCENARIO", "weight": 1.0} -->

We assess the performance of our method in a state-of-the-art race track for 1:43 scale autonomous cars. Given that this case-study has been the research focus of previous work, its time-optimality is well-understood.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A PLANAR SYSTEM IN SINGLE-CORRIDOR SCENARIO", "weight": 1.0} -->

It is worth highlighting that our method shows its full potential in unstructured environments, where imposing a geometric reference might be detrimental for planning time-optimal trajectories. However, race-alike scenarios, consist of well-structured -- single-corridor-- environments in which the progress along the track and its boundaries are perfectly referenced by the centerline, and thus are better suited to path following methods, such as. Nevertheless, the proposed case-study allows for (i) performing an *approximated benchmark* on time-optimality, (ii) demonstrating that the underlying PH splines have no effect on the computed trajectory and (iii) showing the method's applicability to constrained planar systems.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A PLANAR SYSTEM IN SINGLE-CORRIDOR SCENARIO", "weight": 1.0} -->

To this end, in a similar way to and, we employ the dynamic bicycle model with states ${\mathbf{x}} = \left\lbrack p_{x},p_{y},\psi,v,D,\delta \right\rbrack \in {\mathbb{R}}^{6}$ and inputs ${\mathbf{u}} = \left\lbrack \overset{˙}{D},\overset{˙}{\delta} \right\rbrack \in {\mathbb{R}}^{2}$, where ${\{ p_{x},p_{y},\psi,v,D,\delta\}} \in {\mathbb{R}}$, refer to the position, yaw, longitudinal velocity, throttle and steering angle. For the respective equations of motion and model coefficients, please refer to eq.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A PLANAR SYSTEM IN SINGLE-CORRIDOR SCENARIO", "weight": 1.0} -->

3. To exploit the aforementioned convexity in the spatial constraints (13e), we adopt a similar approach presented in and, where the Euclidean position coordinates $\lbrack p_{x},p_{y}\rbrack$ are projected onto their corresponding spatial counterparts $\lbrack\xi,w\rbrack$. In addition, to guarantee the validity of the first-principles model's approximation, we impose constraints on the throttle, steering angle, their respective change rates, as well as the longitudinal and lateral accelerations ${\{ a_{\parallel},a_{\perp}\}} \in {\mathbb{R}}$. The numerical values associated with these constraints can be found in Table I.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-A PLANAR SYSTEM IN SINGLE-CORRIDOR SCENARIO", "weight": 1.0} -->

Following Algorithm 1, and given the single-corridor nature of the present case-study, the first-stage results in the race-track itself. Subsequently, before solving the time-minimizing problem, in the second-stage we need to compute a PH spline that lies within the race-track. As discussed in Section III-B2, the definition of the collision-free curve upon which the spline is converted does not influence the computation of the time-optimal trajectory. Putting it another way, any curve that lies within the race-track is eligible to be embedded as a PH spline into the time optimization problem. Nonetheless, because the obstacle-free space remains fixed, the time-optimal solution is invariant regardless of the PH spline used.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-A PLANAR SYSTEM IN SINGLE-CORRIDOR SCENARIO", "weight": 1.0} -->

To demonstrate the non-sensitivity of SCTOMP with respect to PH splines, in the second-stage we compute four different versions, according to four different criteria: the track's center, outer and inner-lines, as well as an intermediary slalom. Their geometrical locations are visualized in the left of Fig. 2 and their characteristics are given in the second and third columns of Table II. Comparing the PH splines against each other, the one denoted as *interior* is the shortest and sharpest, followed by *centerline*, while *exterior* and *slalom* are smoother, longer and more curvy. Their differences on shape and size allow for challenging our methodology's robustness with respect to PH spline variations.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A PLANAR SYSTEM IN SINGLE-CORRIDOR SCENARIO", "weight": 1.0} -->

Upon solving the third-stage for all four splines, a closely-matched series of lap times are obtained, exhibiting an average duration of $4.922 \pm 0.002$$\ s$ and a maximum gap of $0.005\ s$. These timings are presented in the fourth column of Table II and the minor differences in time are attributed to numerical implementation. In fact, all four solutions result in the same trajectory as the one stated, thereby rendering the aforementioned differences negligible and demonstrating that the obtained solution is agnostic of the underlying PH spline.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A PLANAR SYSTEM IN SINGLE-CORRIDOR SCENARIO", "weight": 1.0} -->

The resultant trajectory is illustrated in the center column of Fig. 2. As common in racing scenarios, the time-optimal trajectory enters a corner from its inner side and exists from the outside. Moreover, the longitudinal and angular accelerations attached in the right column of Fig. 2 show that the car's actuation is fully exploited by always remaining on its physical limit.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B SPATIAL SYSTEM IN MULTI-CORRIDOR SCENARIOS", "weight": 1.0} -->

After analyzing SCTOMP's ability to compute time-optimal trajectories in a planar case-study with a single-corridor, we study its applicability to spatial systems within more challenging, i.e., multi-corridor, scenarios.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B SPATIAL SYSTEM IN MULTI-CORRIDOR SCENARIOS", "weight": 1.0} -->

To this end, we focus on a benchmark introduced, and further extended, which entails the navigation of a quadrotor between start and goal states in two intricate and congested environments: a "forest" characterized by scattered columns, and an indoor "office". To compute time-optimal trajectories for a quadrotor, it is necessary to select single rotor thrust commands as control inputs, as this approach enables full exploitation of the system's physical limits. However, to ensure a fair comparison, we adopt the same input modality as, namely, collective thrust and body rates. It is worth noting that this is the preferred control choice for professional human pilots and has recently been demonstrated to be the most successful input selection for training policies on quadrotors.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-B SPATIAL SYSTEM IN MULTI-CORRIDOR SCENARIOS", "weight": 1.0} -->

For the specific coefficients we use the same racing quadrotor as. As conducted in the preceding planar study, to capitalize the convexity of the spatial constraints (13e), we perform a spatial reformulation from the Euclidean coordinates $\mathbf{p}$ to the spatial ones $\lbrack\xi,w_{1},w_{2}\rbrack$. Moreover, to ensure the integrity of the first-principles model, the collective thrust and the angular velocities are bounded to the values in Table I.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-B SPATIAL SYSTEM IN MULTI-CORRIDOR SCENARIOS", "weight": 1.0} -->

We compare the performance of SCTOMP against three baseline algorithms. Among these, the first one is a variant of CPC, a methodology capable of computing theoretically time-optimal trajectories according to the physical limits of the quadrotor, extended by the authors in to make it applicable in cluttered environments. The second baseline is the hierarchical sampling-based method, while the third refers to the deep Reinforcement Learning approach. Each of these methods is tested in three and four case-studies, i.e., different start and goal positions in the forest and office environments, respectively. Notice that these case-studies are identical to the ones in and are listed in the second column of Table III.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-B SPATIAL SYSTEM IN MULTI-CORRIDOR SCENARIOS", "weight": 1.0} -->

Leveraging the aforementioned modularity of the first-stage, we find the collision-free corridors by defining a tunnel around the topological paths computed. The radius of the tunnel is specified by the distance to the closest point in an inflated voxel grid of the occupancy map, resulting in overly conservative corridors. As already mentioned, this stage is modular in such a way that it could be replaced by other methods, e.g.,. After computing all corridors and solving the second- and third-stages for each of them, the trajectory with lowest navigation time is picked. The corridors and trajectories computed for two different case-studies can be visualized in Fig 3.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-B SPATIAL SYSTEM IN MULTI-CORRIDOR SCENARIOS", "weight": 1.0} -->

The obtained navigation times are reported in Table III. Due to the randomness associated to the sampling-based method, we give the average duration for 30 runs, alongside the best solution in parentheses. The results show that SCTOMP is able to compute the trajectories with the minimum navigation time for all test-cases, except for one. As mentioned, the extended CPC method only finds solutions for the easiest forest case-studies. Reductions of SCTOMP with respect to these theoretical lower bounds are attributed to avoiding the singularity $\overset{˙}{\xi} = 0$; instead of starting from a stationary position, we initialize the quadrotor with a minimal velocity ${\|{\mathbf{v}}\|}_{2} \neq$$0\ {m\ s^{- 1}}$. In the remaining more complex test cases, SCTOMP shows capable of computing shorter time solutions than the baseline methods. On the one hand, the excessively hierarchical procedure of the sampling-based algorithm jeopardizes its time-optimality.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B SPATIAL SYSTEM IN MULTI-CORRIDOR SCENARIOS", "weight": 1.0} -->

On the other hand, aiming to account for tracking disturbances, the RL method learns to prioritize safety over time-optimality by avoiding to fly too close to obstacles, and thus, rendering the obtained trajectories sub-optimal. In contrast, SCTOMP fully exploits the free-space within a given corridor, resulting in trajectories that tangentially touch its borders. This feature can be visualized at the graphs attached to the lower-left side of Figs 3b and 3d. As a consequence, once the corridor associated to the optimal trajectory is found, SCTOMP guarantees to compute the time-optimal trajectory. This relates to the second office case-study, where SCTOMP shows higher navigation times than the RL due to the fact that none of the corridors obtained in first-stage contained the optimal trajectory. This can be overcome by implementing more detailed sampling-based method in stage 1.

<!-- chunk {"id": "body-0054", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

In this work, we presented a motion planning approach capable of computing time-optimal trajectories in spatially constrained environments. The time-optimal trajectories obtained by our method, not only exploit the system's actuation, but also the available free space. For this purpose, we rely on a spatial reformulation that allows for performing a singularity-free spatial transformation of the system dynamics, as well as the time minimization problem. To compute the underlying parametric functions required by this reformulation, we leverage Pythagorean Hodograph splines. This results in a three-stage scheme, where after finding collision-free corridors with PH splines enclosed in them, their respective coefficients are fed into a spatially reformulated time minimization problem. Experiments on a single-corridor planar case-study show that the solution's time-optimality is agnostic to the underlying PH spline. Moreover, an extensive benchmark against baseline algorithms account for the method's time-optimal capabilities.

<!-- chunk {"id": "body-0055", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Lastly, the versatility of the systems -- a planar bicycle model and a spatial quadrotor -- and differences in the scale of the environments upon which the experiments were conducted emphasize the motion planner's generality and applicability to a wide range of systems and scenarios.
