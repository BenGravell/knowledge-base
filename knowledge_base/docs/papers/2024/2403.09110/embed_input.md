SINDy-RL: Interpretable and Efficient Model-Based Reinforcement Learning

Topics include Reinforcement learning, SINDy, Model-based reinforcement learning, Interpretable artificial intelligence, Data-driven methods.

Combines SINDy with model-based RL: a SINDy surrogate world model replaces the environment for policy training, yielding interpretable dynamics models and improved sample efficiency compared to black-box neural network surrogates.

Deep reinforcement learning (DRL) has shown significant promise for uncovering sophisticated control policies that interact in complex environments, such as stabilizing a tokamak fusion reactor or minimizing the drag force on an object in a fluid flow. However, DRL requires an abundance of training examples and may become prohibitively expensive for many applications. In addition, the reliance on deep neural networks often results in an uninterpretable, black-box policy that may be too computationally expensive to use with certain embedded systems. Recent advances in sparse dictionary learning, such as the sparse identification of nonlinear dynamics (SINDy), have shown promise for creating efficient and interpretable data-driven models in the low-data regime. In this work, we introduce SINDy-RL, a unifying framework for combining SINDy and DRL to create efficient, interpretable, and trustworthy representations of the dynamics model, reward function, and control policy. We demonstrate the effectiveness of our approaches on benchmark control environments and flow control problems, including gust mitigation on a 3D NACA 0012 airfoil at Re = 1000....

## Abstract

Deep reinforcement learning (DRL) has shown significant promise for uncovering sophisticated control policies that interact in complex environments, such as stabilizing a tokamak fusion reactor or minimizing the drag force on an object in a fluid flow. However, DRL requires an abundance of training examples and may become prohibitively expensive for many applications. In addition, the reliance on deep neural networks often results in an uninterpretable, black-box policy that may be too computationally expensive to use with certain embedded systems....

Keywords: reinforcement learning, sparse identification of nonlinear dynamics, model-based RL, deep reinforcement learning

## Materials, Data, and Code Availability

All experiments, with the exception of the 3D Airfoil environment, were performed using a single-node, Linux engineering workstation consisting of a total of 40 CPUs (Intel$^{\text{®}}$ Xeon$^{\text{®}}$ Gold 6230). The 3D Airfoil experiments used NVIDIA A100 GPUs on JUWELS Booster and JURECA at the Jülich Supercomputing Centre (JSC) / Forschungszentrum Jülich. Code and training configurations are publicly available in our repository:

We evaluate our methods on five environments depicted in Figure: dm_control swing-up \[\] balances a pole on a cart in the unstable upright position starting from the stable down position at rest, gymnasium Swimmer-v4 \[\] controls a 3-segment robot to travel as far as possible in the horizontal direction (along the $x$-axis) for a fixed time, HydroGym Cylinder \[\] reduces the drag force, $C_{D}$, of a rotating cylinder in an unsteady fluid flow at ${Re} = 100$ with measurements of the lift force, $C_{L}$, HydroGym Pinball reduces the net drag force $C_{D1} + C_{D2} + C_{D3}$ on the system of cylinders to stabilize the quasi-periodic...

## SINDy-RL: Sparse Dictionary Learning for RL

### Generalization

^11^footnotetext: Corresponding author (nzolman@uw.edu)

Much of the success of modern technology can be attributed to our ability to control dynamical systems: designing safe biomedical implants for homeostatic regulation, gimbling rocket boosters for reusable launch vehicles, operating power plants and power grids, industrial manufacturing, among many other examples....
