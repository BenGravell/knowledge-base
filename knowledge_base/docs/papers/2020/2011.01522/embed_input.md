Higher-Order Moment-Based Anomaly Detection

The identification of anomalies is a critical component of operating complex, and possibly large-scale and geo-graphically distributed cyber-physical systems. While designing anomaly detectors, it is common to assume Gaussian noise models to maintain tractability; however, this assumption can lead to the actual false alarm rate being significantly higher than expected. Here we design a distributionally robust threshold of detection using finite and fixed higher-order moments of the detection measure data such that it guarantees the actual false alarm rate to be upper bounded by the desired one. Further, we bound the states reachable through the action of a stealthy attack and identify the trade-off between this impact of attacks that cannot be detected and the worst-case false alarm rate. Through numerical experiments, we illustrate how knowledge of higher-order moments results in a tightened threshold, thereby restricting an attacker's potential impact.

## INTRODUCTION

From critical infrastructures and industrial process control to autonomous driving and various biomedical applications, dynamical control systems are increasingly able to be instrumented with new sensing and actuation capabilities. These cyber-physical systems (CPS) comprise growing webs of interconnected feedback loops and must operate efficiently and resiliently in dynamic and uncertain environments. As these systems become large, devising both model-based and data-driven methods for detecting anomalies (such as component failures or malicious attacks) are critical for their robust and efficient operation.

To simplify the analysis and design, often such complex cyber-networks are modeled as a discrete-time linear time invariant system with Gaussian noises. However, this can lead to a significant miscalculation of probabilities and risk if the underlying processes behave differently, for example due to various nonlinearities or malicious attacks. In the context of attacks, it is possible for an attacker to modify the sensor outputs and effectively generate aggressive and strategic noise profiles to sabotage the operation of the system.

This paper is a significant extension of our previous work where we used a moment-based ambiguity set formulation with fixed first two moments (Proposition 2) to obtain a detector threshold via generalized Chebyshev inequality.

We propose an approach to construct moment-based ambiguity sets with fixed moments up to $k$ order for the anomaly detection measure and design an anomaly detector threshold for CPSs that exhibit non-Gaussian uncertainties. The approach can utilize either residual moments obtained through a dynamic model or estimated directly from residual data.

## Conclusion & Future Outlook

We have proposed a distributionally robust approach to form the $k$ moments based ambiguity set for the detection measure data and used it to tune the anomaly detectors for a desired false alarm rate. We found a detector threshold which guaranteed that the false alarm rate did not exceed a desired value using a semidefinite program. We have demonstrated the effectiveness of our proposed approach with a numerical example. Further, our approach using higher-order moments restricted the attacker's potential impact.
