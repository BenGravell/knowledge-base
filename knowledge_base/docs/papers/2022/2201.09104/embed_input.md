<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Understanding the Effects of Second-Order Approximations in Natural Policy Gradient Reinforcement Learning

Topics include Natural gradients, Policy gradients, Reinforcement learning, Stability analysis, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Natural policy gradient methods are popular reinforcement learning methods that improve the stability of policy gradient methods by utilizing second-order approximations to precondition the gradient with the inverse of the Fisher-information matrix. However, to the best of the authors' knowledge, there has not been a study that has investigated the effects of different second-order approximations in a comprehensive and systematic manner. To address this, five different second-order approximations were studied and compared across multiple key metrics including performance, stability, sample efficiency, and computation time. Furthermore, hyperparameters which aren't typically acknowledged in the literature are studied including the effect of different batch sizes and optimizing the critic network with the natural gradient. Experimental results show that on average, improved second-order approximations achieve the best performance and that using properly tuned hyperparameters can lead to large improvements in performance and sample efficiency ranging up to +181%. We also make the code in this study available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The policy gradient method is a popular optimization method for reinforcement learning problems; however, it suffers from unstable training due to high-variance gradient estimates. A promising solution is to leverage natural policy gradient methods, which preconditions the gradient with the inverse of the Fisher-information matrix to restrict how much the model can change between training iterations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

For neural networks, which can have tens of millions of parameters, directly computing the inverse of the Fisher-information matrix is intractable since the Fisher-information matrix is an $n_{\theta} \times n_{\theta}$ matrix, where $n_{\theta}$ is the number of parameters in the model. This led to the research community developing new approximations for the inverse of the Fisher-information matrix which led to having to choose the most appropriate approximation method. Furthermore, to generate effective performance, setting the batch size and how to optimize the critic network are also important details. To the best of the authors' knowledge, there has not been a study that has holistically investigated strategies for choosing these details to achieve high performance with natural policy gradient methods in a comprehensive and systematic manner.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we study the effects of five different second-order approximations: Hessian-free optimization (HF), diagonal approximations (Diagonal), Kronecker-factored approximate curvature (KFAC), Eigenvalue-corrected Kronecker factorization approximate curvature (EKFAC), and Time-efficient natural gradient descent (TENGraD). Across these approximations, we investigate hyperparameters which aren't typically given importance in policy gradient research including, the effect of using different batch sizes and the effect of using different optimization methods on the critic network. We also study these approximations and hyperparameters across multiple reinforcement learning environments and record statistics on performance, training stability, sample efficiency, and computation time.

<!-- chunk {"id": "body-0006", "role": "body", "section": "II-A Policy Gradient Methods", "weight": 1.0} -->

The policy gradient method parameterizes its policy with parameters $\theta$ and aims to minimize the negative expected reward of its trajectories: where for each time step $t$ in the trajectory $\tau$: ${r{(\tau)}_{t}} = {\sum_{i = 0}^{\infty}{\gamma^{i}r{(a_{t + i},s_{t + i})}}}$ is the discounted cumulative reward after taking action $a_{t}$ in state $s_{t}$ and $\pi{(\cdot |\theta)}_{t} = \pi{(a_{t}|s_{t},\theta)}$ is the policy's probability of taking action $a_{t}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "II-A Policy Gradient Methods", "weight": 1.0} -->

In general, to optimize (II.1), the policy gradient method uses the following gradient: where $\Psi$ is typically chosen as an advantage function, $A$, which has the general form of: ${A{(a_{t},s_{t})}} = {{r{(\tau)}_{t}} - {V{(s_{t})}}}$, where $V{(s_{t})}$ is the expected cumulative reward of the policy in state $s_{t}$. In our experiments, we set $\Psi$ to use the generalized advantage estimation method (GAE) which involves training a critic network to estimate $V{(s_{t})}$. While the policy gradient method directly optimizes (II.2), doing so often results in high-variance gradient estimates which leads to unstable training and poor performance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-B Natural Policy Gradient Methods", "weight": 1.0} -->

To stabilize training, the natural policy gradient method restricts how much the policy can change across training iterations by adding a Kullback--Leibler divergence constraint ($D_{KL}$) between policy iterations: where $\theta^{(k)}$ defines the parameters at optimization iteration $k$. To approximately solve (II.3), we use a first-order taylor-series approximation of $L$ around $\theta^{(k)}$, a second-order taylor-series approximation of $D_{KL}$, and solve for the optimum (see and for a full derivation). In doing so, we derive the natural policy gradient method, where $F$ is the Fisher-information matrix: Figure 1: Diagram of the two hyperparameters introduced in this paper for natural policy gradient methods: tuning the batch size for performance and optimizing the critic method using the natural gradient. These strategies can be applied across all second-order approximations for any reinforcement learning environment.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Second-Order Approximations", "weight": 1.0} -->

A key problem is that the Fisher-information matrix ($F$) is an $n_{\theta} \times n_{\theta}$ matrix, where $n_{\theta}$ is the number of parameters in the model. For neural networks which can have tens of millions of parameters, directly computing the inverse of the Fisher-information matrix is intractable. This has led to rising interest in the research community to develop new ways to approximate the inverse of the Fisher-information matrix for neural networks. However, most of these approximations have never been fully investigated in reinforcement learning (RL) tasks. Below, we review five of the most popular approximations and their related work in RL.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Second-Order Approximations", "weight": 1.0} -->

Diagonal Approximations (Diagonal): Diagonal approximations use a diagonal approximation of $F$. This makes storage and inversion easy, however, it ignores a large amount of curvature information. While some RL research indirectly use the diagonal approximation by using the Adam optimizer, there has not been any specific focus on understanding the fundamental trade-offs when using Diagonal approximations compared to other approximations when realizing the natural policy gradient.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Second-Order Approximations", "weight": 1.0} -->

Hessian-free Approximations (HF): Hessian-free approximations use matrix-vector products and the conjugate gradient method to approximately solve for $F^{- 1}{\nabla L}{(\theta)}$. However, computing the conjugate gradient at each iteration can be computationally expensive. One of the most popular implementations of the natural policy gradient which used the HF approximation is Trust region policy optimization (TRPO) which used a backtracking line search method to achieve state-of-the-art results in continuous control tasks at the time.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Second-Order Approximations", "weight": 1.0} -->

Kronecker-factor Approximations (KFAC/EKFAC): Kronecker-factor approximations use a block-diagonal approximation of $F$ which assumes each layer is independent of the others. KFAC decomposes the Fisher-information matrix using the Kronecker product. EKFAC uses a different approximation based on KFAC which showed improved results across computer vision experiments. In RL, Actor-critic using kronecker-factored trust region (ACKTR) used KFAC optimization and step-size clipping to realize the natural policy gradient and showed improved results compared to TRPO. EKFAC has never been investigated in the RL literature.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Second-Order Approximations", "weight": 1.0} -->

Woodbury Approximations (TENGraD): While EKFAC proposes an improved approximation to KFAC, TENGraD provides an exact block-diagonal approximation using the Woodbury identity. However, TENGraD requires constructing a $m \times m$ matrix where $m$ is the batch size which can be computationally expensive when using large batch sizes. TENGraD has never been investigated in the RL literature.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Key Hyperparameters", "weight": 1.0} -->

In this section, we give a brief introduction to the hyperparameters we investigate. This includes batch size tuning and using the natural gradient to optimize the critic network. Figure 1 shows a diagram of the two hyperparameters.

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-A Batch Size Tuning", "weight": 1.0} -->

In the policy gradient setting, the batch size defines how many training examples to collect in the environment before using the collected data to update the model. Using a larger batch size will result in more examples, for a more stable update, but fewer model updates per environment step. Comparatively, using a smaller batch size will result in fewer examples, for a less stable update, but more updates per environment step. Although the importance of the batch size is not emphasized much in the literature, we find that tuning the batch size is a critical hyperparameter that can significantly affect the final performance and other metrics of the model (a similar result was found for Q-learning methods ).

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A Batch Size Tuning", "weight": 1.0} -->

To understand how a tuned batch size can improve the baseline performance, we tune the batch size of the baseline models based on the performance metric.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-B Natural Critic Optimization", "weight": 1.0} -->

Another hyperparameter is to improve the optimization of the critic network using the natural gradient. While some work investigated using clipped targets to stabilize training, ACKTR used the natural gradient to further improve the stability and showed improved performance using KFAC optimization for both the policy and the critic network.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-B Natural Critic Optimization", "weight": 1.0} -->

While ACKTR investigated applying only KFAC optimization to both the policy network and the critic network, we investigate five different second-order approximations for the policy network and for each of these we investigate five second-order approximations for tuning the critic network. To achieve this, we leverage the models with a tuned batch size and use grid search to find the best approximation to optimize the critic network. The results are shown in Section V-B.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we investigate the performance of the five second-order approximations and the effect of our hyperparameters. Furthermore, in doing so, we also investigate the performance of EKFAC and TENGraD approximations for natural policy gradient reinforcement learning for the first time in the literature. We compare each approximation across seven different MuJoCo environments: HalfCheetah-v2, Ant-v2, Hopper-v2, Humanoid-v2, Walker2d-v2, Reacher-v2, and Swimmer-v2. All experiments were run across 10 different random seeds.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experiments", "weight": 1.0} -->

Throughout the experiments, we study four metrics: Performance which is the maximum average return achieved by the policy across training; Stability which is the average standard deviation (across seeds) across training; Sample Efficiency which is the number of environment steps to achieve a specific performance threshold; and Computation Time which is the amount of time to take 100K environment steps while training. More information on these metrics is available in Appendix B.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experiments", "weight": 1.0} -->

For clarity purposes, to make all metrics correspond with 'larger is better', we flip the sign of the metrics where smaller values are better (i.e., Stability, Sample Efficiency, and Computation Time). For example, if two agents achieve an average standard deviation (across seeds) of 500 and 600 (where 500 is a smaller standard deviation and is thus more stable), we flip the signs to get -500 and -600, in which case the policy with the larger value of -500 is more stable and is therefore considered better. All hyperparameter information can be found in Appendix C.

<!-- chunk {"id": "body-0022", "role": "body", "section": "V-A Baseline", "weight": 1.0} -->

We first investigate each approximation's baseline performance using the same batch size and using SGD to optimize the critic network. The training curves of the different approximations are shown in Figure 2. The solid-colored line represents the mean value across the random seeds and the shaded region represents one standard deviation above and below the mean. We also show the mean metrics across the seven different environments in Table I.

<!-- chunk {"id": "body-0023", "role": "body", "section": "V-A Baseline", "weight": 1.0} -->

Performance Since each environment has different reward scales, to weigh each environment's score equally, we normalize the performance scores in Table I and Figure 3.

<!-- chunk {"id": "body-0024", "role": "body", "section": "V-A Baseline", "weight": 1.0} -->

We see TENGraD significantly outperforms the other approximations in terms of the IQM, mean, and optimality gap aggregation metrics because it achieves the best score and there is no overlap between its confidence intervals and the others. EKFAC and HF achieve the second-best scores however, their confidence intervals overlap which shows their performance is not significantly different from each other. Lastly, we see KFAC achieves the third-best score, followed by Diagonal with the worst score. Analyzing the median metrics in Figure 3 is not as straightforward due to a large amount of overlap in confidence intervals; this is not surprising since the median is a poor measure of overall performance. We see TENGraD is significantly better than all other approximations other than EKFAC; and that EKFAC is significantly better than Diagonal. Interestingly, the median aggregate metric shows a trend that newer second-order approximations lead to better median performance.

<!-- chunk {"id": "body-0025", "role": "body", "section": "V-A Baseline", "weight": 1.0} -->

Stability HF achieves the best stability score, closely followed by KFAC, followed by TENGraD and EKFAC, and lastly, with a significantly lower score, Diagonal. HF achieves the best stability score, likely because it utilizes the conjugate gradient algorithm for its update. In contrast, Diagonal achieves the lowest score, likely because its approximation ignores a large amount of curvature leading to inaccurate gradient scaling. We see in the HalfCheetah-v2 and Reacher-v2 environments, Diagonal is unable to remain stable throughout training and diverges at the end of training.

<!-- chunk {"id": "body-0026", "role": "body", "section": "V-A Baseline", "weight": 1.0} -->

Sample Efficiency KFAC achieves the best sample efficiency score, closely followed by EKFAC and TENGraD, followed by HF and Diagonal.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-A Baseline", "weight": 1.0} -->

Computation Time Diagonal achieves the best computation time score, followed by HF, followed by KFAC and EKFAC, and lastly TENGraD. Diagonal achieves the best scores due to its simple and efficient implementation, only requiring an element-wise multiplication and division. Whereas, TENGraD achieves the lowest score due to it having to periodically compute the inverse of a very large $m \times m$ matrix where $m$ is the batch size.

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-B Hyperparameters", "weight": 1.0} -->

We now investigate how we can leverage a performance-tuned batch size and use the natural gradient to optimize the critic network to achieve performance improvements across all approximations in Tables II - VI. For succinctness, we move the results of batch size tuning in Appendix A. In all the tables we show the percentage change compared to the baseline model in brackets and bold the largest improvement for each metric. If the policy is unable to achieve the sample efficiency threshold compared to the baseline we show 'NaN'.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-B Hyperparameters", "weight": 1.0} -->

Key Trends: Overall, we see tuning the batch size and using the natural gradient to optimize the critic network can lead to significant improvements in performance, training stability, sample efficiency, and speed in many reinforcement learning environments across all five natural gradient approximations. Specifically, we see TENGraD achieves improvements in performance, stability, and sample efficiency of up to +181%, +60%, and +86% respectively with at most a 5% decrease in the speed score. The results of applying the strategies across all the other approximations are summarized in their respective table captions.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-B Hyperparameters", "weight": 1.0} -->

Interestingly, we see that using the hyperparameters the metrics are usually improved in the HalfCheetah-v2, Ant-v2, Reacher-v2, and Swimmer-v2 environments, however, the other environments such as Hopper-v2, Humanoid-v2, and Walker2d-v2 see results decrease compared to the baseline. This may be because the strategies are tuned on the HalfCheetah-v2 environment which is much similar to the environments in which the policy performed well in and is not similar to the environments in which the policy performed poorly. We hypothesise that tuning the strategies on the poor performance environments can result in similar performance improvements seen in the other environments. We leave this for future research.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-B Hyperparameters", "weight": 1.0} -->

Another trend we see is that when the performance score is improved usually the stability score decreases; and when the performance score is improved, we see a similar improvement in the sample efficiency score.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we studied five different second-order approximations across multiple key metrics to better understand how each approximation affects the performance of the natural policy gradient. Furthermore, we investigated the effect of two different hyperparameters: the batch size and the optimization method for the critic network, and showed they have a large effect on the final performance, even though they aren't typically acknowledged in the literature.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We found that properly tuning the hyperparameters can lead to large improvements in performance and sample efficiency ranging up to +181% and +86% respectively across the MuJoCo control benchmarks and that TENGraD achieved the best performance out of all the approximations.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We also find that there is a fundamental trade-off between achieving high performance and maintaining stability throughout training, and that performance is positively correlated with sample efficiency. We hope this research helps expand our field's understanding of how different approximations and hyperparameters affects the natural policy gradient and helps practitioners efficiently leverage natural policy gradient methods for real-world reinforcement learning tasks.
