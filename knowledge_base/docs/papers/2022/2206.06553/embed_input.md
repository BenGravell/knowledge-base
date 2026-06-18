Safe Output Feedback Motion Planning from Images via Learned Perception Modules and Contraction Theory

Topics include Motion planning, Output feedback, Learned perception, Contraction theory, Safety guarantees, RGB-D perception.

Integrates learned perception error bounds, contraction-based tracking, and sampling-based planning to provide safety and reachability guarantees from high-dimensional observations. The paper is a useful template for treating perception uncertainty as part of the motion-planning certificate rather than as a separate preprocessing concern.

We present a motion planning algorithm for a class of uncertain control-affine nonlinear systems which guarantees runtime safety and goal reachability when using high-dimensional sensor measurements (e.g., RGB-D images) and a learned perception module in the feedback control loop. First, given a dataset of states and observations, we train a perception system that seeks to invert a subset of the state from an observation, and estimate an upper bound on the perception error which is valid with high probability in a trusted domain near the data. Next, we use contraction theory to design a stabilizing state feedback controller and a convergent dynamic state observer which uses the learned perception system to update its state estimate. We derive a bound on the trajectory tracking error when this controller is subjected to errors in the dynamics and incorrect state estimates. Finally, we integrate this bound into a sampling-based motion planner, guiding it to return trajectories that can be safely tracked at runtime using sensor data....

## Introduction

Figure 1: For a 4D car, a 6D quadrotor, and a 14D arm, we compute plans that can be safely stabilized to reach goals at runtime using rich sensor observations in the form of RGB(-D) images.

Safely and reliably deploying an autonomous robot requires a systematic analysis of the uncertainties that it may face across its perception, planning, and feedback control modules. State-of-the-art methods largely analyze each module separately; e.g., by first certifying perception, finding a safe plan under a nominal dynamics model, and then using a stable tracking controller. However, this ignores how the errors in each module can propagate....

We present a motion planning algorithm for control-affine systems that enables safe tracking at runtime using an output feedback controller with image observations as input. To achieve this, we learn a perception system and use it in an OCM and CCM-based output feedback control loop. We derive tracking tubes for the closed-loop system and use them within an RRT-based planner to compute plans that theoretically guarantee safe goal-reaching at runtime....

Our method has some weaknesses which reveal directions for future work. While the large dataset $\mathcal{S}$ used to train ${\hat{h}}^{- 1}$ is easy to gather in simulation, sim-to-real is then needed for ${\hat{h}}^{- 1}$ to transfer to the real world. Thus, in future work, we will combine synthetic, domain-randomized perception data with a small real-world labeled dataset to train generalizable perception modules that have calibrated estimates of the sim-to-real error....

### Lemma 4.2 (${\overset{˙}{d}}_{e}{(t)}$)

Figure 2: Our method. Offline: After learning a perception system ĥ−1 (Sec. 4.1), we bound its error to derive tracking tubes under imperfect perception (Sec. 4.2). We use these tubes to find safely-trackable plans (Sec. 4.4). Online: We design a CCM/OCM-based controller/observer (Sec. 4.3) to track the plan/perform state estimation at runtime, using ĥ−1 to process rich observations y.

### Theorem 4.1 (From derivative to value)

To address this gap, we consider one such unified approach: the Output Feedback Motion Planning problem (OFMP), which jointly plans nominal trajectories and designs feedback controllers which safely stabilize the system to some goal when using imperfect state information (i.e., output feedback)....
