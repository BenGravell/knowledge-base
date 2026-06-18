Understanding the Effects of Second-Order Approximations in Natural Policy Gradient Reinforcement Learning

Topics include Natural gradients, Policy gradients, Reinforcement learning, Stability analysis, Learning.

Natural policy gradient methods are popular reinforcement learning methods that improve the stability of policy gradient methods by utilizing second-order approximations to precondition the gradient with the inverse of the Fisher-information matrix. However, to the best of the authors' knowledge, there has not been a study that has investigated the effects of different second-order approximations in a comprehensive and systematic manner. To address this, five different second-order approximations were studied and compared across multiple key metrics including performance, stability, sample efficiency, and computation time. Furthermore, hyperparameters which aren't typically acknowledged in the literature are studied including the effect of different batch sizes and optimizing the critic network with the natural gradient. Experimental results show that on average, improved second-order approximations achieve the best performance and that using properly tuned hyperparameters can lead to large improvements in performance and sample efficiency ranging up to +181%. We also make the code in this study available at

## Introduction

The policy gradient method is a popular optimization method for reinforcement learning problems; however, it suffers from unstable training due to high-variance gradient estimates. A promising solution is to leverage natural policy gradient methods, which preconditions the gradient with the inverse of the Fisher-information matrix to restrict how much the model can change between training iterations.

For neural networks, which can have tens of millions of parameters, directly computing the inverse of the Fisher-information matrix is intractable since the Fisher-information matrix is an $n_{\theta} \times n_{\theta}$ matrix, where $n_{\theta}$ is the number of parameters in the model. This led to the research community developing new approximations for the inverse of the Fisher-information matrix which led to having to choose the most appropriate approximation method. Furthermore, to generate effective performance, setting the batch size and how to optimize the critic network are also important details....

We found that properly tuning the hyperparameters can lead to large improvements in performance and sample efficiency ranging up to +181% and +86% respectively across the MuJoCo control benchmarks and that TENGraD achieved the best performance out of all the approximations.

We also find that there is a fundamental trade-off between achieving high performance and maintaining stability throughout training, and that performance is positively correlated with sample efficiency. We hope this research helps expand our field's understanding of how different approximations and hyperparameters affects the natural policy gradient and helps practitioners efficiently leverage natural policy gradient methods for real-world reinforcement learning tasks.

Another hyperparameter is to improve the optimization of the critic network using the natural gradient. While some work investigated using clipped targets to stabilize training, ACKTR used the natural gradient to further improve the stability and showed improved performance using KFAC optimization for both the policy and the critic network.

Kronecker-factor Approximations (KFAC/EKFAC): Kronecker-factor approximations use a block-diagonal approximation of $F$ which assumes each layer is independent of the others. KFAC decomposes the Fisher-information matrix using the Kronecker product....
