LQG Control and Sensing Co-Design

We investigate a Linear-Quadratic-Gaussian (LQG) control and sensing co-design problem, where one jointly designs sensing and control policies. We focus on the realistic case where the sensing design is selected among a finite set of available sensors, where each sensor is associated with a different cost (e.g., power consumption). We consider two dual problem instances: sensing-constrained LQG control, where one maximizes control performance subject to a sensor cost budget, and minimum-sensing LQG control, where one minimizes sensor cost subject to performance constraints. We prove no polynomial time algorithm guarantees across all problem instances a constant approximation factor from the optimal. Nonetheless, we present the first polynomial time algorithms with per-instance suboptimality guarantees. To this end, we leverage a separation principle, that partially decouples the design of sensing and control....

## Introduction

Traditional approaches to systems control assume the choice of sensors fixed. The sensors usually result from a preliminary design phase in which an expert selects a suitable sensor suite that accommodates estimation requirements, and system constraints (e.g., power consumption). However, the control applications of the Internet of Things (IoT) and Battlefield Things (IoBT), pose serious limitations to the applicability of this traditional paradigm....

Related work in control. Traditionally, the control literature has focused on co-designing control, estimation, actuation (i.e., actuator selection), and sensing (i.e., sensor selection). However, the focus so far has mostly been different from the co-design problem we consider in this paper:

The paper opens several avenues for future research. First, the development of distributed implementations of the proposed algorithms would offer computational speedups. Second, other co-design problems are interesting to be explored, such as the co-design of control-sensing-actuation. Third, while we provide bounds on an approximate sensor design against optimal design, one could provide bounds against the case where all sensors are used. Finally, in adversarial or failure-prone scenarios, one must account for sensor failures; to this end, one could leverage recent results on *robust combinatorial optimization*.

Figure 5: LQG cost for increasing horizon T and for various sensing budgets b.

This section presents a practical algorithm for Problem 2. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design") (Algorithm 3). Since the algorithm shares steps with Algorithm 1, we focus on the different ones.

*(Separability in Problem 2. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design"))* Define the constant $\overline{\kappa} \triangleq {\kappa - {\text{tr}\left( {\Sigma_{1|1}N_{1}} \right)} - {\sum_{t = 1}^{T}{\text{tr}\left( {W_{t}S_{t}} \right)}}}$. Any optimal solution $(\mathcal{S}^{\star},u_{1:T}^{\star})$ to Problem 2. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design") can be computed in cascade:
