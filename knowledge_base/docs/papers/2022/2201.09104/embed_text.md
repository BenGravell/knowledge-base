## Introduction

The policy gradient method is a popular optimization method for reinforcement learning problems; however, it suffers from unstable training due to high-variance gradient estimates. A promising solution is to leverage natural policy gradient methods, which preconditions the gradient with the inverse of the Fisher-information matrix to restrict how much the model can change between training iterations.

For neural networks, which can have tens of millions of parameters, directly computing the inverse of the Fisher-information matrix is intractable since the Fisher-information matrix is an $n_{\theta} \times n_{\theta}$ matrix, where $n_{\theta}$ is the number of parameters in the model. This led to the research community developing new approximations for the inverse of the Fisher-information matrix which led to having to choose the most appropriate approximation method. Furthermore, to generate effective performance, setting the batch size and how to optimize the critic network are also important details. To the best of the authors' knowledge, there has not been a study that has holistically investigated strategies for choosing these details to achieve high performance with natural policy gradient methods in a comprehensive and systematic manner.

In this paper, we study the effects of five different second-order approximations: Hessian-free optimization (HF), diagonal approximations (Diagonal), Kronecker-factored approximate curvature (KFAC), Eigenvalue-corrected Kronecker factorization approximate curvature (EKFAC), and Time-efficient natural gradient descent (TENGraD). Across these approximations, we investigate hyperparameters which aren't typically given importance in policy gradient research including, the effect of using different batch sizes and the effect of using different optimization methods on the critic network. We also study these approximations and hyperparameters across multiple reinforcement learning environments and record statistics on performance, training stability, sample efficiency, and computation time.

## Background

In this section, we first define the notation used throughout the paper, followed by a brief overview of the policy gradient method, the natural policy gradient method, and the five different second-order approximations which can be used to implement the natural policy gradient method.

We consider an infinite-horizon discounted Markov decision process, defined by the tuple ($\mathcal{S}$, $\mathcal{A}$, $p$, $r$, $\gamma$) which defines the state distribution $\mathcal{S}$, action distribution $\mathcal{A}$, state transition function $p$, reward function $r$, and discount factor $\gamma$. Specifically, at time $t$, an agent is in a state $s_{t} \in \mathcal{S}$ and samples an action $a_{t} \in \mathcal{A}$ from its policy, $\pi{(\left. a_{t} \middle| s_{t} \right.)}$. The environment then produces a reward $r{(a_{t},s_{t})}$ and a new state $s_{t + 1} \in \mathcal{S}$ according to the transition probability function $p{(\left. s_{t + 1} \middle| {a_{t},s_{t}} \right.)}$. Repeating this process $n$ times produces a trajectory, $\tau$, of length $n$.

### II-A Policy Gradient Methods

The policy gradient method parameterizes its policy with parameters $\theta$ and aims to minimize the negative expected reward of its trajectories:

where for each time step $t$ in the trajectory $\tau$: ${r{(\tau)}_{t}} = {\sum_{i = 0}^{\infty}{\gamma^{i}r{(a_{t + i},s_{t + i})}}}$ is the discounted cumulative reward after taking action $a_{t}$ in state $s_{t}$ and $\pi{( \cdot |\theta)}_{t} = \pi{(a_{t}|s_{t},\theta)}$ is the policy's probability of taking action $a_{t}$. In general, to optimize (II.1), the policy gradient method uses the following gradient:

where $\Psi$ is typically chosen as an advantage function, $A$, which has the general form of: ${A{(a_{t},s_{t})}} = {{r{(\tau)}_{t}} - {V{(s_{t})}}}$, where $V{(s_{t})}$ is the expected cumulative reward of the policy in state $s_{t}$. In our experiments, we set $\Psi$ to use the generalized advantage estimation method (GAE) which involves training a critic network to estimate $V{(s_{t})}$. While the policy gradient method directly optimizes (II.2), doing so often results in high-variance gradient estimates which leads to unstable training and poor performance.

### II-B Natural Policy Gradient Methods

To stabilize training, the natural policy gradient method restricts how much the policy can change across training iterations by adding a Kullback--Leibler divergence constraint ($D_{KL}$) between policy iterations:

where $\theta^{(k)}$ defines the parameters at optimization iteration $k$. To approximately solve (II.3), we use a first-order taylor-series approximation of $L$ around $\theta^{(k)}$, a second-order taylor-series approximation of $D_{KL}$, and solve for the optimum (see and for a full derivation). In doing so, we derive the natural policy gradient method,

where $F$ is the Fisher-information matrix:

Figure 1: Diagram of the two hyperparameters introduced in this paper for natural policy gradient methods: tuning the batch size for performance and optimizing the critic method using the natural gradient. These strategies can be applied across all second-order approximations for any reinforcement learning environment.

## Second-Order Approximations

A key problem is that the Fisher-information matrix ($F$) is an $n_{\theta} \times n_{\theta}$ matrix, where $n_{\theta}$ is the number of parameters in the model. For neural networks which can have tens of millions of parameters, directly computing the inverse of the Fisher-information matrix is intractable. This has led to rising interest in the research community to develop new ways to approximate the inverse of the Fisher-information matrix for neural networks. However, most of these approximations have never been fully investigated in reinforcement learning (RL) tasks. Below, we review five of the most popular approximations and their related work in RL.

Diagonal Approximations (Diagonal): Diagonal approximations use a diagonal approximation of $F$. This makes storage and inversion easy, however, it ignores a large amount of curvature information. While some RL research indirectly use the diagonal approximation by using the Adam optimizer, there has not been any specific focus on understanding the fundamental trade-offs when using Diagonal approximations compared to other approximations when realizing the natural policy gradient.

Hessian-free Approximations (HF): Hessian-free approximations use matrix-vector products and the conjugate gradient method to approximately solve for $F^{- 1}{\nabla L}{(\theta)}$. However, computing the conjugate gradient at each iteration can be computationally expensive. One of the most popular implementations of the natural policy gradient which used the HF approximation is Trust region policy optimization (TRPO) which used a backtracking line search method to achieve state-of-the-art results in continuous control tasks at the time.

Kronecker-factor Approximations (KFAC/EKFAC): Kronecker-factor approximations use a block-diagonal approximation of $F$ which assumes each layer is independent of the others. KFAC decomposes the Fisher-information matrix using the Kronecker product. EKFAC uses a different approximation based on KFAC which showed improved results across computer vision experiments. In RL, Actor-critic using kronecker-factored trust region (ACKTR) used KFAC optimization and step-size clipping to realize the natural policy gradient and showed improved results compared to TRPO. EKFAC has never been investigated in the RL literature.

Woodbury Approximations (TENGraD): While EKFAC proposes an improved approximation to KFAC, TENGraD provides an exact block-diagonal approximation using the Woodbury identity. However, TENGraD requires constructing a $m \times m$ matrix where $m$ is the batch size which can be computationally expensive when using large batch sizes. TENGraD has never been investigated in the RL literature.

## Key Hyperparameters

In this section, we give a brief introduction to the hyperparameters we investigate. This includes batch size tuning and using the natural gradient to optimize the critic network. Figure 1 shows a diagram of the two hyperparameters.

### IV-A Batch Size Tuning

In the policy gradient setting, the batch size defines how many training examples to collect in the environment before using the collected data to update the model. Using a larger batch size will result in more examples, for a more stable update, but fewer model updates per environment step. Comparatively, using a smaller batch size will result in fewer examples, for a less stable update, but more updates per environment step. Although the importance of the batch size is not emphasized much in the literature, we find that tuning the batch size is a critical hyperparameter that can significantly affect the final performance and other metrics of the model (a similar result was found for Q-learning methods ).

To understand how a tuned batch size can improve the baseline performance, we tune the batch size of the baseline models based on the performance metric.

Figure 2: Average return vs the number of environment steps of five different second-order approximations across seven different MuJoCo environments using the baseline hyperparameters. All experiments are across 10 random seeds. The solid-colored line represents the mean value across the different seeds and the shaded region represents one standard deviation above and below the mean. TENGraD (red) achieves the best performance across most environments. HF is the most stable across seeds.

TABLE I: Mean metrics of five different approximations across seven different MuJoCo environments. The best result for each metric is in bold. Larger values are better. TENGraD achieves the best performance score; HF achieves the best stability score; KFAC achieves the best sample efficiency score, and Diagonal achieves the best computation time score.

### IV-B Natural Critic Optimization

Another hyperparameter is to improve the optimization of the critic network using the natural gradient. While some work investigated using clipped targets to stabilize training, ACKTR used the natural gradient to further improve the stability and showed improved performance using KFAC optimization for both the policy and the critic network.

While ACKTR investigated applying only KFAC optimization to both the policy network and the critic network, we investigate five different second-order approximations for the policy network and for each of these we investigate five second-order approximations for tuning the critic network. To achieve this, we leverage the models with a tuned batch size and use grid search to find the best approximation to optimize the critic network with. The results are shown in Section V-B.

## Experiments

In this section, we investigate the performance of the five second-order approximations and the effect of our hyperparameters. Furthermore, in doing so, we also investigate the performance of EKFAC and TENGraD approximations for natural policy gradient reinforcement learning for the first time in the literature. We compare each approximation across seven different MuJoCo environments: HalfCheetah-v2, Ant-v2, Hopper-v2, Humanoid-v2, Walker2d-v2, Reacher-v2, and Swimmer-v2. All experiments were run across 10 different random seeds.

Throughout the experiments, we study four metrics: Performance which is the maximum average return achieved by the policy across training; Stability which is the average standard deviation (across seeds) across training; Sample Efficiency which is the number of environment steps to achieve a specific performance threshold; and Computation Time which is the amount of time to take 100K environment steps while training. More information on these metrics is available in Appendix B.

For clarity purposes, to make all metrics correspond with 'larger is better', we flip the sign of the metrics where smaller values are better (i.e., Stability, Sample Efficiency, and Computation Time). For example, if two agents achieve an average standard deviation (across seeds) of 500 and 600 (where 500 is a smaller standard deviation and is thus more stable), we flip the signs to get -500 and -600, in which case the policy with the larger value of -500 is more stable and is therefore considered better. All hyperparameter information can be found in Appendix C.

### V-A Baseline

Figure 3: Normalized performance scores of all second-order approximations across four aggregate metrics with 95% stratified bootstrap confidence intervals. A larger score in the median, IQM, and mean aggregations and a smaller score in the optimality gap aggregation corresponds to better performance. We see TENGraD statistically outperforms all other approximations across IQM, mean, and the optimality gap aggregation metrics. The median aggregate metric shows a trend that newer second-order approximations lead to better median performance.

TABLE II: Performance of the Diagonal approximation across seven different environments with a tuned batch size and where the critic network is optimized with the natural gradient. The percentage improvement compared to the baseline is in brackets. The largest improvement for each metric is in bold. We see performance, stability and sample efficiency improvements up to +94%, +100%, and +10% with up to a +19% improvement in the speed score.

TABLE III: Performance of the HF approximation across seven different environments with a tuned batch size and where the critic network is optimized with the natural gradient. The percentage improvement compared to the baseline is in brackets. The largest improvement for each metric is in bold. We see performance, stability and sample efficiency improvements up to +65%, +89%, and +62% with at most a 12% decrease in the speed score.

TABLE IV: Performance of the KFAC approximation across seven different environments with a tuned batch size and where the critic network is optimized with the natural gradient. The percentage improvement compared to the baseline is in brackets. The largest improvement for each metric is in bold. We see performance, stability and sample efficiency improvements up to +65%, +85%, and +53% with at most a 1% decrease in the speed score.

TABLE V: Performance of the EKFAC approximation across seven different environments with a tuned batch size and where the critic network is optimized with the natural gradient. The percentage improvement compared to the baseline is in brackets. The largest improvement for each metric is in bold. We see EKFAC achieves improvements in performance, stability, and sample efficiency of up to +50%, +86%, and +38% respectively with at most a 1% decrease in the speed score.

TABLE VI: Performance of the TENGraD approximation across seven different environments with a tuned batch size and where the critic network is optimized with the natural gradient. The percentage improvement compared to the baseline is in brackets. The largest improvement for each metric is in bold. We see TENGraD achieves improvements in performance, stability, and sample efficiency of up to +181%, +60%, and +86% respectively with at most a 5% decrease in the speed score.

We first investigate each approximation's baseline performance using the same batch size and using SGD to optimize the critic network. The training curves of the different approximations are shown in Figure 2. The solid-colored line represents the mean value across the random seeds and the shaded region represents one standard deviation above and below the mean. We also show the mean metrics across the seven different environments in Table I.

Performance Since each environment has different reward scales, to weigh each environment's score equally, we normalize the performance scores in Table I and Figure 3.

Figure 2 shows that no approximation outperforms all other approximations across all environments and shows that the best approximation depends on the environment. Table I shows TENGraD achieves the best performance score across all approximations, followed by HF and EKFAC, followed by KFAC and lastly Diagonal. Table I also shows that improved approximations can lead to improved performance since TENGraD achieves the best mean performance score across all environments and is the most accurate approximation. We also see that the Diagonal achieves the lowest performance score and that in some environments (Ant-v2 and Reacher-v2 shown in Figure 2) it diverges near the end of the training; likely because it ignores a large amount of curvature leading to unstable updates.

Figure 3 shows normalized performance scores across four aggregate metrics with 95% stratified bootstrap confidence intervals from including median, interquartile mean (IQM), mean, and the optimality gap across all approximations. A larger score in the median, IQM, and mean aggregations and a smaller score in the optimality gap aggregation corresponds to better performance.

We see TENGraD significantly outperforms the other approximations in terms of the IQM, mean, and optimality gap aggregation metrics because it achieves the best score and there is no overlap between its confidence intervals and the others. EKFAC and HF achieve the second-best scores however, their confidence intervals overlap which shows their performance is not significantly different from each other. Lastly, we see KFAC achieves the third-best score, followed by Diagonal with the worst score. Analyzing the median metrics in Figure 3 is not as straightforward due to a large amount of overlap in confidence intervals; this is not surprising since the median is a poor measure of overall performance. We see TENGraD is significantly better than all other approximations other than EKFAC; and that EKFAC is significantly better than Diagonal. Interestingly, the median aggregate metric shows a trend that newer second-order approximations lead to better median performance.

Stability HF achieves the best stability score, closely followed by KFAC, followed by TENGraD and EKFAC, and lastly, with a significantly lower score, Diagonal. HF achieves the best stability score, likely because it utilizes the conjugate gradient algorithm for its update. In contrast, Diagonal achieves the lowest score, likely because its approximation ignores a large amount of curvature leading to inaccurate gradient scaling. We see in the HalfCheetah-v2 and Reacher-v2 environments, Diagonal is unable to remain stable throughout training and diverges at the end of training.

Sample Efficiency KFAC achieves the best sample efficiency score, closely followed by EKFAC and TENGraD, followed by HF and Diagonal.

Computation Time Diagonal achieves the best computation time score, followed by HF, followed by KFAC and EKFAC, and lastly TENGraD. Diagonal achieves the best scores due to its simple and efficient implementation, only requiring an element-wise multiplication and division. Whereas, TENGraD achieves the lowest score due to it having to periodically compute the inverse of a very large $m \times m$ matrix where $m$ is the batch size.

### V-B Hyperparameters

We now investigate how we can leverage a performance-tuned batch size and use the natural gradient to optimize the critic network to achieve performance improvements across all approximations in Tables II - VI. For succinctness, we move the results of batch size tuning in Appendix A. In all the tables we show the percentage change compared to the baseline model in brackets and bold the largest improvement for each metric. If the policy is unable to achieve the sample efficiency threshold compared to the baseline we show 'NaN'.

Key Trends: Overall, we see tuning the batch size and using the natural gradient to optimize the critic network can lead to significant improvements in performance, training stability, sample efficiency, and speed in many reinforcement learning environments across all five natural gradient approximations. Specifically, we see TENGraD achieves improvements in performance, stability, and sample efficiency of up to +181%, +60%, and +86% respectively with at most a 5% decrease in the speed score. The results of applying the strategies across all the other approximations are summarized in their respective table captions.

Interestingly, we see that using the hyperparameters the metrics are usually improved in the HalfCheetah-v2, Ant-v2, Reacher-v2, and Swimmer-v2 environments, however, the other environments such as Hopper-v2, Humanoid-v2, and Walker2d-v2 see results decrease compared to the baseline. This may be because the strategies are tuned on the HalfCheetah-v2 environment which is much similar to the environments in which the policy performed well in and is not similar to the environments in which the policy performed poorly. We hypothesise that tuning the strategies on the poor performance environments can result in similar performance improvements seen in the other environments. We leave this for future research.

Another trend we see is that when the performance score is improved usually the stability score decreases; and when the performance score is improved, we see a similar improvement in the sample efficiency score.

## Conclusion

In this paper, we studied five different second-order approximations across multiple key metrics to better understand how each approximation affects the performance of the natural policy gradient. Furthermore, we investigated the effect of two different hyperparameters: the batch size and the optimization method for the critic network, and showed they have a large effect on the final performance, even though they aren't typically acknowledged in the literature.

We found that properly tuning the hyperparameters can lead to large improvements in performance and sample efficiency ranging up to +181% and +86% respectively across the MuJoCo control benchmarks and that TENGraD achieved the best performance out of all the approximations.

We also find that there is a fundamental trade-off between achieving high performance and maintaining stability throughout training, and that performance is positively correlated with sample efficiency. We hope this research helps expand our field's understanding of how different approximations and hyperparameters affects the natural policy gradient and helps practitioners efficiently leverage natural policy gradient methods for real-world reinforcement learning tasks.
