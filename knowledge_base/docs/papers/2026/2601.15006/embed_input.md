<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints

Topics include Robotics, Accuracy, DWPP, Dynamic window, Pure pursuit.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Pure pursuit and its variants are widely used for mobile robot path tracking owing to their simplicity and computational efficiency. However, many conventional approaches do not explicitly account for velocity and acceleration constraints, resulting in discrepancies between commanded and actual velocities that result in overshoot and degraded tracking performance. To address this problem, this paper proposes dynamic window pure pursuit (DWPP), which fundamentally reformulates the command velocity computation process to explicitly incorporate velocity and acceleration constraints. Specifically, DWPP formulates command velocity computation in the velocity space (the v-omega plane) and selects the command velocity as the point within the dynamic window that is closest to the line omega = kappav. Experimental results demonstrate that DWPP avoids constraint-violating commands and achieves superior path-tracking accuracy compared with conventional pure pursuit methods. The proposed method has been integrated into the official Nav2 repository and is publicly available.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, the demand for automated guided vehicles (AGVs) in environments such as factories and hospitals has been increasing. Navigation for these robots typically starts with a global planner, which computes a path on a map to reach the goal. Subsequently, a local planner generates local paths and computes command velocities to track the global path while accounting for the robot's current state and real-time sensor data.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Representative local planners include the dynamic window approach (DWA), model predictive control (MPC), and pure pursuit (PP). Among these planners, DWA and MPC address multi-objective problems such as simultaneous path tracking and obstacle avoidance, whereas PP focuses on a single objective, namely path tracking. Nevertheless, PP remains widely used owing to its simplicity and computational efficiency, and numerous improvements have continued to be proposed.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of these improved methods, regulated pure pursuit (RPP), is the standard implementation in Nav2, an autonomous navigation framework for the open-source robotics middleware Robot Operating System 2 (ROS 2). However, a common limitation of existing PP--based methods, including RPP, is that they cannot explicitly account for a robot's velocity and acceleration constraints during command velocity computation. Consequently, in conventional PP variants, either an additional layer is introduced to clip the command velocity according to velocity and acceleration limits or the raw command is sent directly to the robot and the realized velocity is clipped by the robot's hardware constraints. In such cases, a discrepancy occurs between the motion planned by PP and the actual motion executed by the robot, which not only complicates the discussion of controller stability but also can result in overshoot from the reference path owing to the inability to fully realize the planned velocity.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these problems, this paper proposes dynamic window pure pursuit (DWPP), which fundamentally reformulates command velocity computation by explicitly embedding velocity and acceleration constraints. The core concept of DWPP is to formulate command velocity computation in the velocity space, namely the $v$--$\omega$ plane, where $v$ and $\omega$ denote the linear and angular velocities, respectively. Specifically, DWPP selects the command velocity as the point within the dynamic window---representing velocity and acceleration constraints in the $v$--$\omega$ plane---that is closest to the line $\omega = {\kappav}$, which corresponds to the velocity condition derived from PP. This strategy enables the computation of velocity commands that achieve the highest possible path tracking accuracy under velocity and acceleration constraints. Robot experiments demonstrated that DWPP consistently respects velocity and acceleration limits while achieving superior path-following performance compared with existing PP variants implemented in Nav2. Furthermore, as a practical contribution, the DWPP implementation has been integrated into the Nav2 framework and is publicly available. ^11^1

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. Section 2 reviews conventional PP variants and summarizes their processing flow and limitations. Section 3 describes the proposed DWPP methodology in detail. Section 4 presents experimental results evaluating the performance of DWPP in comparison with existing methods. Section 5 provides a discussion, and Section 6 concludes the paper and outlines directions for future work.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Pure Pursuit (PP)", "weight": 1.0} -->

First, the algorithm computes the lookahead point ${\mathbf{p}}_{L}$ on the path, which serves as the reference position for path tracking. Figure 2 ‣ 2 Related work ‣ DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints") shows the geometric relationship among the robot's position, path, and lookahead point ${\mathbf{p}}_{L}$. Let $L$ be the lookahead distance. Let ${\mathbf{p}}_{r} = {(x_{r},y_{r})} \in P$ denote the point on the path nearest to the current robot position.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Pure Pursuit (PP)", "weight": 1.0} -->

Next, the curvature $\kappa$ of the arc that connects the current heading direction to the lookahead point is computed. Let $\varphi$ be the heading angle from the robot's forward direction to ${\mathbf{p}}_{L}$. Let $l$ be the distance between the robot's position and ${\mathbf{p}}_{L}$. From the geometric relationships shown in Fig. 2 ‣ 2 Related work ‣ DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints"), the radius $R$ of the circular path from the robot to ${\mathbf{p}}_{L}$ can be computed by

<!-- chunk {"id": "body-0010", "role": "body", "section": "Pure Pursuit (PP)", "weight": 1.0} -->

Hence, the curvature $\kappa$ can be derived by

<!-- chunk {"id": "body-0011", "role": "body", "section": "Pure Pursuit (PP)", "weight": 1.0} -->

Next, the command linear velocity $v_{cmd}$ is determined.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Pure Pursuit (PP)", "weight": 1.0} -->

Finally, the command angular velocity $\omega_{cmd}$ is computed as follows. If the robot moves along a path of curvature $\kappa$ at $v_{cmd}$, then

<!-- chunk {"id": "body-0013", "role": "body", "section": "Pure Pursuit (PP)", "weight": 1.0} -->

Difficulty in tuning the lookahead distance $L$: Even if $L$ is tuned carefully, excessively sharp curves may result in overshooting behavior. A short $L$ enables the robot to easily converge to the path but can introduce oscillations around the path center. A large $L$ can reduce oscillations but slow convergence, resulting in a trade-off.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Pure Pursuit (PP)", "weight": 1.0} -->

Constant command linear velocity $v_{cmd}$: It does not adapt to the scenario. For example, even if a curve is extremely tight or if an obstacle is too close to the robot, the velocity will not automatically be reduced.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Pure Pursuit (PP)", "weight": 1.0} -->

Velocity and acceleration constraints are not considered: The command linear velocity is determined without accounting for acceleration constraints, whereas the command angular velocity is computed directly from the path curvature. Consequently, command velocities that explicitly satisfy both velocity and acceleration constraints are difficult to generate.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Adaptive Pure Pursuit (APP)", "weight": 1.0} -->

Adaptive pure pursuit (APP) addresses the first limitation. It extends the lookahead distance in proportion to the robot's linear velocity.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Adaptive Pure Pursuit (APP)", "weight": 1.0} -->

where $l_{t}$ is a gain that indicates how many seconds ahead to project the velocity, and $L_{\min}$ and $L_{\max}$ are the minimum and maximum allowable lookahead distances, respectively. The function ${clamp}{(\text{value},\text{low},\text{high})}$ returns values in $\lbrack\text{low},\text{high}\rbrack$; if the value is below low, it is set to low, and if the value is above high, it is set to high. By adaptively adjusting the lookahead distance based on speed, APP reduces overshoot and oscillations at high speeds and enhances path convergence at low speeds, resulting in more stable and accurate path tracking. However, APP still leaves the second and third limitations unresolved.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Regulated Pure Pursuit (RPP)", "weight": 1.0} -->

The RPP controller extends the conventional PP method by introducing several heuristics that regulate the command linear velocity according to the path geometry and the surrounding environment. In RPP, the linear velocity is adjusted using three heuristics: curvature, proximity to obstacles, and distance to the goal.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Curvature Heuristic", "weight": 1.0} -->

The curvature heuristic reduces the linear velocity when the robot follows a path with a small curvature radius, thereby mitigating overshoot on sharp turns. The regulated velocity $v_{reg}^{curv}$ is defined based on the curvature radius $R$ of the circular path from the robot to ${\mathbf{p}}_{L}$ as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Curvature Heuristic", "weight": 1.0} -->

where $R_{\min}$ denotes the threshold radius below which velocity scaling is applied.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Proximity Heuristic", "weight": 1.0} -->

The proximity heuristic decreases the velocity when the robot is close to obstacles to enhance safety. Let $d_{O}$ be the minimum distance to surrounding obstacles. The regulated velocity $v_{reg}^{prox}$ is given by

<!-- chunk {"id": "body-0022", "role": "body", "section": "Proximity Heuristic", "weight": 1.0} -->

where $d_{prox}$ is the proximity threshold, and $g_{d} \in {(0,1\rbrack}$ is a gain parameter that controls the aggressiveness of the deceleration.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Goal Heuristic", "weight": 1.0} -->

The goal heuristic gradually reduces the velocity as the robot approaches the goal to ensure a smooth and accurate stop. Let $d_{G}$ denote the remaining distance to the goal along the path, and $d_{goal}$ be the distance threshold at which deceleration begins. The regulated velocity is computed as

<!-- chunk {"id": "body-0024", "role": "body", "section": "Goal Heuristic", "weight": 1.0} -->

In the Nav2 implementation, the curvature and proximity heuristics are first applied to the command linear velocity $v_{cmd}$. The intermediate regulated velocity is computed as

<!-- chunk {"id": "body-0025", "role": "body", "section": "Goal Heuristic", "weight": 1.0} -->

where $v_{reg}^{\min}$ is a parameter that specifies the minimum allowable regulated velocity.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Goal Heuristic", "weight": 1.0} -->

Subsequently, the goal heuristic is applied to $v_{reg}^{{curv},{prox}}$, and the final regulated velocity is computed as

<!-- chunk {"id": "body-0027", "role": "body", "section": "Goal Heuristic", "weight": 1.0} -->

where $v_{goal}^{\min}$ denotes the minimum linear velocity allowed when approaching the goal.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Goal Heuristic", "weight": 1.0} -->

If the final regulated velocity $v_{reg}$ is smaller than the originally computed command velocity $v_{cmd}$, the command velocity is replaced by $v_{reg}$, thereby limiting the translational motion.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Goal Heuristic", "weight": 1.0} -->

This regulation strategy effectively reduces overshoot on sharp curves and improves safety in the vicinity of obstacles or people. However, RPP does not explicitly consider velocity and acceleration constraints during the command velocity computation, leaving this limitation unresolved.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Dynamic Window Pure Pursuit (DWPP)", "weight": 1.0} -->

The proposed DWPP fundamentally reformulates the command velocity computation process to address the third problem, namely, the lack of explicit consideration of velocity and acceleration constraints in conventional command computation and regulation. As illustrated in Fig. 1, DWPP differs from RPP through the following three processes. First, the dynamic window, defined as the feasible velocity region for the next control step under the robot's velocity and acceleration constraints, is computed. Second, this dynamic window is regulated using the regulated linear velocity $v_{reg}$. Third, from the resulting region, the velocity point closest to the line $\omega = {\kappav}$ (Eq. (7 ‣ 2 Related work ‣ DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints"))) is selected as the command velocity.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Dynamic Window Pure Pursuit (DWPP)", "weight": 1.0} -->

Through these steps, DWPP explicitly accounts for velocity and acceleration constraints when computing the path-tracking command velocity. This section describes the three processes in detail and presents the stability analysis of DWPP. The implementation is publicly available.^22^2 The overall procedure corresponds to the implementation in the computeDynamicWindowVelocities function.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Compute the dynamic window", "weight": 1.0} -->

where $v_{\max}$, $v_{\min}$, $\omega_{\max}$, and $\omega_{\min}$ represent the maximum and minimum linear and angular velocities. The parameters $a_{\max}^{acc}$ and $\alpha_{\max}^{acc}$ are the maximum linear and angular accelerations, whereas $a_{\max}^{dec}$ and $\alpha_{\max}^{dec}$ are the maximum linear and angular decelerations. $\Deltat$ denotes the control period. This procedure corresponds to the implementation in the computeDynamicWindow function.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Apply regulation to the dynamic window", "weight": 1.0} -->

Next, the values $v_{\max}^{dw}$ and $v_{\min}^{dw}$ are constrained by the regulated command linear velocity $v_{reg}$ computed by RPP.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Apply regulation to the dynamic window", "weight": 1.0} -->

Specifically, because the admissible range of the robot's linear velocity is limited to $\lbrack 0,v_{reg}\rbrack$, the dynamic window is restricted by taking the intersection between the original dynamic window and this velocity range.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Apply regulation to the dynamic window", "weight": 1.0} -->

This procedure corresponds to the implementation in the apply-\

<!-- chunk {"id": "body-0036", "role": "body", "section": "Compute Optimal Velocity within the Dynamic Window", "weight": 1.0} -->

Third, the optimal velocity command is selected from the dynamic window to best satisfy the path-following condition defined in Eq. (7 ‣ 2 Related work ‣ DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints")).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Compute Optimal Velocity within the Dynamic Window", "weight": 1.0} -->

The specific implementation is conducted as follows. Note that the following procedure corresponds to the implementation of the computeOptimalVelocityWithinDynamicWindow function.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Compute Optimal Velocity within the Dynamic Window", "weight": 1.0} -->

First, consider the case where $\kappa = 0$. The linear velocity is set to $v_{\max}^{dw}$. For the angular velocity, if the line $\omega = {\kappav}$ intersects the dynamic window, the intersection point is selected, which yields $\omega = 0$. If no intersection exists, either $\omega_{\max}^{dw}$ or $\omega_{\min}^{dw}$ is selected, whichever is closer to zero.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Compute Optimal Velocity within the Dynamic Window", "weight": 1.0} -->

Next, consider the case where $\kappa \neq 0$ and the line $\omega = {\kappav}$ intersects the dynamic window. The intersections between the line $\omega = {\kappav}$ and the four extended edges of the dynamic window are given by

<!-- chunk {"id": "body-0040", "role": "body", "section": "Compute Optimal Velocity within the Dynamic Window", "weight": 1.0} -->

Among these points, the one that lies inside the dynamic window and has the largest linear velocity is selected. If none of these intersection points lies inside the dynamic window, then the line $\omega = {\kappav}$ does not intersect the dynamic window.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Compute Optimal Velocity within the Dynamic Window", "weight": 1.0} -->

Finally, consider the case where $\kappa \neq 0$ and no intersection exists. From convex geometry, we know that when a convex set and line do not intersect, the point on the convex hull that minimizes the distance to the line must lie at a vertex of the hull or on an edge parallel to the line. Therefore, evaluating the four vertices of the dynamic window is sufficient.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Compute Optimal Velocity within the Dynamic Window", "weight": 1.0} -->

That is, the computational complexity of the DWPP algorithm is $O{}$, the same as that of conventional PP variants.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Stability Analysis", "weight": 1.0} -->

The stability of the proposed DWPP can be evaluated by leveraging the stability analysis for the PP algorithm established by Ollero et al.. This approach is justified by the fact that the fundamental control structure of DWPP is equivalent to that of the conventional PP framework. Specifically, as illustrated in Fig. 1, DWPP performs local path planning and computes velocity commands to track a local path with a specific curvature $\kappa$, which is analogous to traditional PP algorithms.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Stability Analysis", "weight": 1.0} -->

However, note that the analysis provided by Ollero et al. assumes a constant linear velocity. Therefore, the stability discussion in this section is conducted under the regime where the control period $\Deltat$ is sufficiently small and the velocity and acceleration limits ($v_{\min}$, $v_{\max}$, $\omega_{\min}$, $\omega_{\max}$, $a_{\max}^{acc}$, $a_{\max}^{dcc}$, $\alpha_{\max}^{acc}$, $\alpha_{\max}^{dcc}$) are bounded such that the velocity fluctuation within a single control period can be considered negligible. Under these quasi-static velocity conditions, the convergence properties of DWPP are expected to align with the analytical results established by Ollero et al.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Stability Analysis", "weight": 1.0} -->

The influence of the specific velocity selection strategy employed in DWPP on system stability is examined below. Ollero et al. introduced a nondimensional lookahead distance defined as

<!-- chunk {"id": "body-0046", "role": "body", "section": "Stability Analysis", "weight": 1.0} -->

where $V$ is the linear velocity, and $T$ is the steering time constant. Their analysis showed that the nondimensional lookahead distance must exceed a minimum threshold, denoted by $L_{\min}^{\prime}$, to guarantee stability. Accordingly, the stability condition for the lookahead distance $L$ can be expressed as

<!-- chunk {"id": "body-0047", "role": "body", "section": "Stability Analysis", "weight": 1.0} -->

This condition indicates that the minimum lookahead distance required for stability is proportional to the linear velocity $V$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Stability Analysis", "weight": 1.0} -->

As described in Section 3.3 ‣ DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints"), a key characteristic of DWPP is its ability to reduce the command linear velocity when tracking paths with large curvature while explicitly respecting velocity and acceleration constraints. In such scenarios, the required minimum lookahead distance for stability becomes smaller owing to the reduction in $V$. Consequently, DWPP exhibits an increased stability margin compared with conventional PP, indicating improved stability properties under sharp-curvature conditions.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Setting", "weight": 1.0} -->

A real-robot experiment was conducted to verify the effectiveness of the proposed DWPP. For navigation during the evaluation, the Nav2 framework was employed, and the performance of DWPP implemented in Nav2 was compared with that of PP, APP, and RPP.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Setting", "weight": 1.0} -->

The robot used in the experiment was a WHILL Model CR, shown in Fig. 4 ‣ DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints"). The robot measured 0.985 m in length and 0.55 m in width. The experiments were conducted in an obstacle-free room, as illustrated in the Fig. 5 ‣ DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints"). A 2D map for localization was created using the SLAM Toolbox, and self-localization was performed using AMCL in Nav2.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Setting", "weight": 1.0} -->

The changed conditions in this experiment were the global path and local planner. Three paths (Paths A, B, and C) were defined as global paths, that is, reference paths, as shown in Fig. 6 ‣ DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints"). All paths shared the same segment length of 3.0 m, whereas the corner angle $\theta_{path}$ was set to $45^{\circ}$, $90^{\circ}$, and $135^{\circ}$ for Paths A, B, and C, respectively. To ensure that the robot's initial pose at the start of tracking exactly matched the reference path, we generated the reference path for each trial based on the robot's initial pose. As local planners, four methods were evaluated: PP, APP, RPP, and the proposed DWPP. In the implementation, the RegulatedPurePursuitController plugin was used in the Nav2 controller_server, and the controller type was switched among PP, APP, RPP, and DWPP via parameter settings.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Setting", "weight": 1.0} -->

To ensure statistical robustness, we conducted five trials for each combination of the four controllers and three paths, resulting in a total of 60 experimental runs.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Setting", "weight": 1.0} -->

Constraint violation ratio \[%\]: The percentage of control steps in which the computed command velocities $(v_{cmd},\omega_{cmd})$ violated the prescribed velocity or acceleration constraints.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Setting", "weight": 1.0} -->

Mean path tracking error \[m\]: The average lateral deviation between the actual robot and reference paths, representing the overall tracking accuracy.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Setting", "weight": 1.0} -->

Maximum path tracking error \[m\]: The peak lateral deviation from the reference path, which characterizes the magnitude of overshoot.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Setting", "weight": 1.0} -->

Travel time \[s\]: The total duration required for the robot to reach the goal.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Setting", "weight": 1.0} -->

The parameters used in the experiment are summarized in Table 1. The velocity and acceleration constraints were determined experimentally. The constant lookahead distance $L$ for the PP controller was set slightly larger than the stability limit, considering the maximum linear velocity. For the other controllers (APP, RPP, and DWPP), the lookahead distance limits ($L_{\min},L_{\max}$) were configured such that the distance at maximum velocity exceeded the constant value used in PP while maintaining tracking accuracy at lower speeds through a smaller $L_{\min}$. Parameters specific to RPP ($R_{\min}$, $v_{reg}^{\min}$) were set to their default Nav2 values. For simplicity, the proximity heuristic of RPP was disabled as no obstacles were present in the experimental environment. Additionally, the Nav2 parameter use_rotate_to_heading was set to false to prevent the robot from stopping at cusp points and ensure continuous path tracking. use_collision_detection was also set to false to avoid unintended deceleration caused by sensor noise.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Setting", "weight": 1.0} -->

All other parameters were maintained at their default values provided by the Nav2 framework. Experimental data were recorded at a frequency of 30 Hz.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Setting", "weight": 1.0} -->

The software was implemented on Ubuntu 24.04 using ROS 2 Jazzy. All computations were executed on a Minisforum UM890 Pro mini-PC equipped with an AMD Ryzen 9 8945HS CPU and 96 GB of RAM.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Results", "weight": 1.0} -->

Tables 5--5 summarize the quantitative results for each method; the reported values represent the means and standard deviations computed over five runs. Specifically, Table 5 lists the percentage of velocity and acceleration constraint violations, whereas Tables 5 and 5 present the means and maximum cross-track errors, respectively. The travel times required to reach the goal are listed in Table 5. Furthermore, Figs. 7--9 illustrate the path tracking performance and velocity profiles obtained with each controller. The paths are plotted for all trials, whereas the velocity profiles show a representative trial for each controller. The experimental behavior is demonstrated in the supplementary video.^33^3

<!-- chunk {"id": "body-0061", "role": "body", "section": "Results", "weight": 1.0} -->

As shown in Table 5, conventional methods resulted in non-zero velocity and acceleration constraint violations; in contrast, DWPP produced no constraint violations for any path.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Results", "weight": 1.0} -->

Tables 5 and 5 indicate that DWPP achieved the smallest mean and maximum errors among all evaluated methods, with the errors decreasing in the order of PP, APP, RPP, and DWPP for all paths. These results indicated that DWPP yielded smaller overall path-tracking errors and reduced overshoot compared with the other methods. In addition, the difference in tracking error between DWPP and the conventional methods became more pronounced as the path corner angle $\theta_{path}$ increased.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Results", "weight": 1.0} -->

Table 5 shows that DWPP required a longer travel time than the conventional methods for all paths.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Results", "weight": 1.0} -->

Figures 7(a)--9(a) show that the differences among controllers became more pronounced as the path corner angle $\theta_{path}$ increased, and the path tracking error decreased accordingly. In particular, for Path C with $\theta_{path} = 135^{\circ}$, DWPP exhibited the smallest overshoot, as shown in Fig. 9(a). These observations were consistent with the quantitative results reported in Tables 5 and 5.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Results", "weight": 1.0} -->

Figures 7(b)--9(e) show that PP, APP, and RPP generated velocity commands that were not always feasible, resulting in discrepancies between the commanded and executed velocities. In contrast, DWPP produced feasible velocity commands, and the commanded and executed velocities closely matched. This observation was consistent with the results shown in Table 5.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Results", "weight": 1.0} -->

In addition, the velocity commands of PP and APP remained constant at the maximum velocity, whereas RPP and DWPP reduced the velocity at corners. Among these methods, DWPP exhibited a greater decrease in velocity. This behavior corresponded to the longer travel times observed for DWPP in Table 5. We hypothesized that this increase in travel time could be mitigated by using a longer lookahead distance, as a longer lookahead distance leads to a smaller curvature of the circular arc toward the lookahead point and thus makes velocity reduction less likely. However, using a longer lookahead distance is also expected to degrade the path-tracking accuracy. Therefore, the next subsection describes the effect of the lookahead distance on the path-tracking error and travel time of DWPP.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Setting", "weight": 1.0} -->

To investigate the effect of the lookahead distance on the path-tracking error and the travel time in DWPP, we conducted a set of simulations. The simulations were performed using Gazebo with a TurtleBot3 Waffle Pi, and navigation was executed using DWPP on Nav2. The global path was set to Path C (Fig. 6(c) ‣ DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints")) because this path exhibited the largest variation in performance among the controller settings. The simulations were conducted in an obstacle-free environment. The robot trajectory was recorded using the ground-truth pose provided by Gazebo to eliminate the influence of localization errors.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Setting", "weight": 1.0} -->

The parameters used in the simulation are summarized in Table 6. The velocity and acceleration constraints were determined according to the robot specifications. In this simulation, the functions of APP and RPP were disabled by setting the Nav2 parameters use_velocity_scaled_lookahead\_\
dist, use_regulated_linear_velocity_scaling, and use_cost\_\
regulated_linear_velocity_scaling to false to isolate and evaluate only the effect of DWPP. All other parameters were set to the same values as those used in the experiment described in Section 4.1.1.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Setting", "weight": 1.0} -->

The only condition varied in this simulation was the lookahead distance. The lookahead distance was set to 0.26, 0.39, 0.52, 0.65, 0.78, 0.91, and 1.04 m. These values corresponded to 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, and 4.0 times the maximum linear velocity, respectively.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Setting", "weight": 1.0} -->

The simulations were conducted on Ubuntu 24.04 with ROS 2 Rolling. The computational experiments were executed on a workstation equipped with an Intel(R) Core(TM) i9-12900K CPU (3.19 GHz), 64 GB of RAM, and an NVIDIA GeForce RTX 3090 GPU (24 GB VRAM). Experimental data were recorded at a frequency of 30 Hz. For reproducibility, the Docker environment used for these simulations is publicly available^44^4

<!-- chunk {"id": "body-0071", "role": "body", "section": "Results", "weight": 1.0} -->

Figures 10 and 11 depict the simulation results. Figure 10 illustrates the trade-off between the mean tracking error and travel time for different lookahead distances, whereas Fig. 11 shows the tracked paths and actual linear velocity profiles for each lookahead distance. The simulation behavior is also demonstrated in the supplementary video.^55^5

<!-- chunk {"id": "body-0072", "role": "body", "section": "Results", "weight": 1.0} -->

As shown in Fig. 10, a clear trade-off existed between the lookahead distance, mean tracking error, and travel time. When the lookahead distance was small, the mean tracking error decreased, whereas the travel time increased. Conversely, as the lookahead distance increased, the mean tracking error increased, whereas the travel time decreased.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Results", "weight": 1.0} -->

These results indicated that, in DWPP, the lookahead distance introduces a trade-off between path-tracking accuracy and traversal efficiency. Therefore, when using DWPP, the lookahead distance should be appropriately tuned by considering this trade-off to achieve better overall navigation performance.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Why DWPP Outperforms RPP", "weight": 1.0} -->

(a) Command velocity profile of RPP and DWPP during tracking Path C

<!-- chunk {"id": "body-0075", "role": "body", "section": "Why DWPP Outperforms RPP", "weight": 1.0} -->

(b) Transition of the dynamic window in RPP.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Why DWPP Outperforms RPP", "weight": 1.0} -->

(c) Transition of the dynamic window in the proposed DWPP.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Why DWPP Outperforms RPP", "weight": 1.0} -->

These results provide the following insights. In RPP, the linear velocity is fixed at $v_{reg}^{\min}$, and the angular velocity is determined based on Eq. (7 ‣ 2 Related work ‣ DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints")) without considering velocity and acceleration constraints. Consequently, the velocity commands are clipped by these constraints during execution. Consequently, although the left vertex of the dynamic window is the optimal feasible point for path tracking, the actual realized velocity corresponds to the right vertex.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Why DWPP Outperforms RPP", "weight": 1.0} -->

In contrast, DWPP selects the point within the dynamic window that is closest to the line defined by Eq. (7 ‣ 2 Related work ‣ DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints")) (i.e., $\omega = {\kappav}$). This approach ensures that the calculated velocity commands are directly executable without being saturated. Moreover, DWPP effectively manages deceleration from $t = 7.033$ to $7.100$ to maintain tracking and accelerates from $t = 7.133$ to $7.166$. This demonstrates that DWPP can calculate velocity commands that maximize path-tracking performance while strictly adhering to velocity and acceleration constraints. These observations confirm that by explicitly incorporating these constraints into the calculation phase, DWPP achieves a more ideal and superior path-tracking performance compared with RPP.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Key Advantages of DWPP over Conventional Pure Pursuit Variants", "weight": 1.0} -->

Direct compliance with velocity and acceleration constraints: DWPP generates velocity commands that inherently satisfy velocity and acceleration constraints. This eliminates the need for external clipping mechanisms or post-processing layers, such as the velocity_smoother in Nav2, which were previously required to ensure feasibility before command execution.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Key Advantages of DWPP over Conventional Pure Pursuit Variants", "weight": 1.0} -->

Optimal tracking within velocity and acceleration constraints: By incorporating velocity and acceleration constraints directly into the command velocity calculation phase, DWPP can determine the optimal velocity commands to maximize path-tracking performance---for instance, by automatically decelerating at sharp corners. Consequently, DWPP can track challenging paths with discontinuous or high curvature (e.g., Path C) with significantly reduced overshoot compared with conventional methods.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Key Advantages of DWPP over Conventional Pure Pursuit Variants", "weight": 1.0} -->

Parameter-free optimal deceleration: DWPP achieves optimal deceleration by fully leveraging the constraints without the need for manual parameter tuning. While RPP can also decelerate at high-curvature sections using its curvature heuristic, it requires the manual design of parameters such as $R_{\min}$ and $v_{reg}^{\min}$. In contrast, DWPP automatically calculates the best possible deceleration based solely on the provided velocity and acceleration limits. Furthermore, DWPP remains compatible with manually designed heuristics, enabling it to inherit their benefits if additional specific tuning is desired.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Key Advantages of DWPP over Dynamic Window Approach", "weight": 1.0} -->

DWA is another prominent local planner that utilizes the dynamic window. In this section, we discuss the comparative advantages of DWPP over DWA, specifically when DWA is employed solely for the purpose of path tracking.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Key Advantages of DWPP over Dynamic Window Approach", "weight": 1.0} -->

Analytical optimality in a continuous solution space: In DWA, candidate velocity commands are obtained through discrete sampling within the dynamic window. This results in a set of discrete solutions, which may result in velocity commands that slightly deviate from the true optimum. In contrast, DWPP analytically computes the command velocity within a continuous solution space by directly exploiting the geometric relationship between the line $\omega = {\kappav}$ and the dynamic window in the $v$-$\omega$ space. This ensures that the optimal velocity command is always obtained within the feasible constraints.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Key Advantages of DWPP over Dynamic Window Approach", "weight": 1.0} -->

Computational efficiency: The computational complexity of DWA is typically $O{({NM})}$, where $N$ denotes the number of velocity samples and $M$ represents the number of simulated time steps in the prediction horizon. On the other hand, as described in Section 3.3 ‣ DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints"), the computational cost of DWPP is $O{}$ because it derives the velocity commands through a closed-form analytical solution.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Key Advantages of DWPP over Dynamic Window Approach", "weight": 1.0} -->

Consequently, when the primary objective of the local planner is pure path tracking without obstacle avoidance, DWPP can calculate more optimal velocity commands with significantly lower computational overhead compared with DWA.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presents dynamic window pure pursuit (DWPP), a novel pure pursuit method designed to explicitly incorporate velocity and acceleration constraints into the velocity command computation process. By selecting the optimal point within the dynamic window closest to the line $\omega = {\kappav}$, the proposed method analytically derives commands that maximize path-tracking performance while ensuring strict adherence to these constraints. Real-robot experiments integrated with the Nav2 framework demonstrated that DWPP outperforms conventional pure pursuit variants. Specifically, the method ensures that generated commands remain within specified velocity and acceleration limits, resulting in a reduction in path-tracking errors compared with traditional approaches. The DWPP implementation has been integrated into the Nav2 framework and is publicly available ^66^6 enabling engineers to readily evaluate and adopt the proposed method.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Future research will focus on the autonomous determination of the lookahead distance to eliminate the need for manual parameter tuning and to further enhance navigation performance.
