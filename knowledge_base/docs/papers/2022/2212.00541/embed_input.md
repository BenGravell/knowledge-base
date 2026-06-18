Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo

Topics include Model predictive control, Predictive sampling, Derivative-free optimization, Real-time, MuJoCo, Robotics.

Introduces MJPC, an open-source framework for real-time predictive control built on MuJoCo physics, implementing iLQG, Gradient Descent, and a derivative-free Predictive Sampling baseline. Demonstrates that simple sampling-based methods are competitive with classical trajectory optimizers.

We introduce MuJoCo MPC (MJPC), an open-source, interactive application and software framework for real-time predictive control, based on MuJoCo physics. MJPC allows the user to easily author and solve complex robotics tasks, and currently supports three shooting-based planners: derivative-based iLQG and Gradient Descent, and a simple derivative-free method we call Predictive Sampling. Predictive Sampling was designed as an elementary baseline, mostly for its pedagogical value, but turned out to be surprisingly competitive with the more established algorithms. This work does not present algorithmic advances, and instead, prioritises performant algorithms, simple code, and accessibility of model-based methods via intuitive and interactive software. MJPC is available at: this http URL, a video summary can be viewed at:

## Introduction

Model-based approaches form the foundation of classical control and robotics. Since Kalman's seminal work \Kalman the *state* along with its dynamics and observation models has played a central role.

The classical approach is being challenged by learning-based methods, which forgo the explicit description of the state and associated models, letting internal representations emerge from the learning process \Lillicrap et al., [2015, Schulman et al., 2017, Salimans et al., 2017, Smith et al., 2022, Rudin et al., 2022\]. The flexibility afforded by learned representations makes these methods powerful and general, but the requirement for large amounts of data and computation makes them slow. In contrast, pure model-based methods, like the ones described below, can synthesise behaviour in real time \Tassa et al.,.

Transfer learning. As mentioned in 5.2, using MJPC to generate data which can then be transferred to a real robot is already possible.

Estimation. The most obvious yet difficult route to controlling hardware is to follow in the footsteps of classic control and couple MJPC to an estimator providing real-time state estimates. In the rare cases where estimation is easy, for example with fixed-base manipulators and static objects, controlling a robot directly with MJPC would be a straightforward exercise. The difficult and interesting case involves free-moving bodies and contacts, as in locomotion and manipulation. For certain specific cases, like locomotion on flat, uniform terrain, reasonable estimates should not be difficult to obtain....

The norm Hessians, $\partial^{2}{\text{n}/{\partial r^{2}}}$, are computed analytically.

This cost is a sum of $M$ terms, each comprising:

### Algorithm

Since both approaches ultimately generate behaviour by optimising an objective, there is reason to believe they can be effectively combined. Indeed, well-known discrete-domain breakthroughs like AlphaGo \Silver et al., are predicated on combining model-based search and learning-based value and policy approximation. We believe the same could happen for robotics and control, and describe our thinking on how this might happen in the Discussion (Section 5)....

To address this deficit, we present MJPC, an open-source interactive application and software framework for predictive control, based on MuJoCo physics \Todorov et al....
