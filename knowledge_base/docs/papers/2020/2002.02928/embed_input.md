Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints

Safely deploying robots in uncertain and dynamic environments requires a systematic accounting of various risks, both within and across layers in an autonomy stack from perception to motion planning and control. Many widely used motion planning algorithms do not adequately incorporate inherent perception and prediction uncertainties, often ignoring them altogether or making questionable assumptions of Gaussianity. We propose a distributionally robust incremental sampling-based motion planning framework that explicitly and coherently incorporates perception and prediction uncertainties. We design output feedback policies and consider moment-based ambiguity sets of distributions to enforce probabilistic collision avoidance constraints under the worst-case distribution in the ambiguity set. Our solution approach, called Output Feedback Distributionally Robust RRT^*(OFDR-RRT^*), produces asymptotically optimal risk-bounded trajectories for robots operating in dynamic, cluttered, and uncertain environments, explicitly incorporating mapping and localization error, stochastic process disturbances, unpredictable obstacle motion, and uncertain obstacle locations....

## Introduction

More sophisticated motion planning and control algorithms are needed for the robots to operate in increasingly dynamic and uncertain environments to ensure safe and effective autonomous behavior. Many widely used motion planning algorithms have been developed in deterministic settings. However, since motion planning algorithms must be coupled with the outputs of inherently uncertain perception systems, there is a crucial need for more tightly coupled perception and planning frameworks that explicitly incorporate perception uncertainties.

Motion planning under uncertainty has been considered in several lines of recent research Blackmore et al.; Agha-Mohammadi et al.; Luders et al.; Blackmore et al.; Liu and Ang; Zhu and Alonso-Mora. Many approaches make questionable assumptions of Gaussianity and utilize chance constraints, ostensibly to maintain computational tractability. However, this can cause significant miscalculations of risk, and the underlying risk metrics do not necessarily possess desirable coherence properties Rockafellar; Majumdar and Pavone....

## Conclusion

In this paper, we presented a methodological framework aimed towards tighter integration of perception and planning in autonomous robotic systems. The environmental state is estimated from sensor data to propagate both estimates and uncertainties of both robot and obstacles. Risk constraints are posed in a meaningful and coherent manner through distributionally robust chance constraints. Using a dynamic output feedback controller together with the distributionally robust risk constraints, a new algorithm called OFDR-$\text{RRT}^{\ast}$ is shown to produce risk bounded trajectories with coherent risk assessment....

Together with the control law (22 ‣ Towards Integrated Perception and Motion Planning with Distributionally Robust Risk Constraints")) we can write the combined dynamics for the true unknown state $\mathcal{Z}_{t}$ and the state estimate ${\overset{\sim}{\mathcal{Z}}}_{t}$ as

### Distributionaly Robust Motion Planning Problem

### Sample-Based Motion Planning Algorithm

Traditionally, the perception and planning components in a robot autonomy stack are loosely coupled, in the sense that nominal estimates from the perception system may be used for planning, while inherent perception uncertainties are usually ignored....
