SINDy-RL: Interpretable and Efficient Model-Based Reinforcement Learning

Topics include Reinforcement learning, SINDy, Model-based reinforcement learning, Interpretable artificial intelligence, Data-driven methods.

Combines SINDy with model-based RL: a SINDy surrogate world model replaces the environment for policy training, yielding interpretable dynamics models and improved sample efficiency compared to black-box neural network surrogates.

Deep reinforcement learning (DRL) has shown significant promise for uncovering sophisticated control policies that interact in complex environments, such as stabilizing a tokamak fusion reactor or minimizing the drag force on an object in a fluid flow. However, DRL requires an abundance of training examples and may become prohibitively expensive for many applications. In addition, the reliance on deep neural networks often results in an uninterpretable, black-box policy that may be too computationally expensive to use with certain embedded systems. Recent advances in sparse dictionary learning, such as the sparse identification of nonlinear dynamics (SINDy), have shown promise for creating efficient and interpretable data-driven models in the low-data regime. In this work, we introduce SINDy-RL, a unifying framework for combining SINDy and DRL to create efficient, interpretable, and trustworthy representations of the dynamics model, reward function, and control policy. We demonstrate the effectiveness of our approaches on benchmark control environments and flow control problems, including gust mitigation on a 3D NACA 0012 airfoil at Re = 1000.

## Abstract

Deep reinforcement learning (DRL) has shown significant promise for uncovering sophisticated control policies that interact in complex environments, such as stabilizing a tokamak fusion reactor or minimizing the drag force on an object in a fluid flow. However, DRL requires an abundance of training examples and may become prohibitively expensive for many applications. In addition, the reliance on deep neural networks often results in an uninterpretable, black-box policy that may be too computationally expensive to use with certain embedded systems.

Keywords: reinforcement learning, sparse identification of nonlinear dynamics, model-based RL, deep reinforcement learning

^11^footnotetext: Corresponding author (nzolman@uw.edu)

## Discussion

This work developed a unifying framework for combining SINDy (i.e., sparse dictionary learning) with deep reinforcement learning to learn efficient, interpretable, and trustworthy representations of the environment dynamics, the reward function, and the control policy, using significantly fewer interactions with the full environment. We demonstrate the effectiveness of SINDy-RL on several challenging benchmark control environments, including performing gust mitigation of NACA 0012 airfoil at ${Re} = 1000$ in a 3D, unsteady environment.

By learning a sparse representation of the dynamics, we developed a Dyna-style MBRL algorithm that could be $10 - 100 \times$ more sample efficient than a model-free approach, while maintaining a significantly smaller model representation than a black-box neural network model. When the reward function for an objective is not easily measurable from the observations---e.g. with only access to sparse sensor data---SINDy-RL can simultaneously learn dictionary models of the reward and dynamics from the environment for sample-efficient DRL.

A key ingredient for successfully applying DRL is to learn over long time-horizons. This posed a significant challenge to SINDy-RL (and Dyna-style learning more broadly) because the learned dynamics models are not guaranteed to be stable or converge---especially under the presence of control. We address this by incorporating known constraints, such as resetting the environment if a predicted state value exits a bounding box and projecting the state-space back onto the appropriate manifold after each step.
