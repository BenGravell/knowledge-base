Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo

Topics include Model predictive control, Predictive sampling, Derivative-free optimization, Real-time, MuJoCo, Robotics.

Introduces MJPC, an open-source framework for real-time predictive control built on MuJoCo physics, implementing iLQG, Gradient Descent, and a derivative-free Predictive Sampling baseline. Demonstrates that simple sampling-based methods are competitive with classical trajectory optimizers.

We introduce MuJoCo MPC (MJPC), an open-source, interactive application and software framework for real-time predictive control, based on MuJoCo physics. MJPC allows the user to easily author and solve complex robotics tasks, and currently supports three shooting-based planners: derivative-based iLQG and Gradient Descent, and a simple derivative-free method we call Predictive Sampling. Predictive Sampling was designed as an elementary baseline, mostly for its pedagogical value, but turned out to be surprisingly competitive with the more established algorithms. This work does not present algorithmic advances, and instead, prioritises performant algorithms, simple code, and accessibility of model-based methods via intuitive and interactive software.

## Introduction

Model-based approaches form the foundation of classical control and robotics. Since Kalman's seminal work \Kalman the *state* along with its dynamics and observation models has played a central role.

The classical approach is being challenged by learning-based methods, which forgo the explicit description of the state and associated models, letting internal representations emerge from the learning process \Lillicrap et al., [2015, Schulman et al., 2017, Salimans et al., 2017, Smith et al., 2022, Rudin et al., 2022\]. The flexibility afforded by learned representations makes these methods powerful and general, but the requirement for large amounts of data and computation makes them slow. In contrast, pure model-based methods, like the ones described below, can synthesise behaviour in real time \Tassa et al.,.

Since both approaches ultimately generate behaviour by optimising an objective, there is reason to believe they can be effectively combined. Indeed, well-known discrete-domain breakthroughs like AlphaGo \Silver et al., are predicated on combining model-based search and learning-based value and policy approximation. We believe the same could happen for robotics and control, and describe our thinking on how this might happen in the Discussion (Section 5).

To address this deficit, we present MJPC, an open-source interactive application and software framework for predictive control, based on MuJoCo physics \Todorov et al. which lets the user easily author and solve complex tasks using predictive control algorithms in real time. The tool offers implementations of standard derivative-based algorithms: iLQG (second-order planner) and Gradient Descent (first-order planner). Additionally, it introduces *Predictive Sampling*, a simple zero-order, sampling-based algorithm that works surprisingly well and is easy to understand.

## Discussion

The thrust of this paper is to make predictive control accessible via customisable, interactive, open-source tooling. We believe that responsive, GUI-based tools are a prerequisite for accelerated robotics research, and that due to their importance, these tools should be modifiable and the inner workings transparent to the researcher. We hope that our MJPC project will be embraced by the community, and look forward to improving and extending it together.
