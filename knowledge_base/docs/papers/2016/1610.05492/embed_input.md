Federated Learning: Strategies for Improving Communication Efficiency

Topics include Low-rank models, Convolutional networks, Federated learning, Distributed systems, Learning, Sampling, Machine learning.

Federated Learning is a machine learning setting where the goal is to train a high-quality centralized model while training data remains distributed over a large number of clients each with unreliable and relatively slow network connections. We consider learning algorithms for this setting where on each round, each client independently computes an update to the current model based on its local data, and communicates this update to a central server, where the client-side updates are aggregated to compute a new global model. The typical clients in this setting are mobile phones, and communication efficiency is of the utmost importance. In this paper, we propose two ways to reduce the uplink communication costs: structured updates, where we directly learn an update from a restricted space parametrized using a smaller number of variables, e.g. either low-rank or a random mask; and sketched updates, where we learn a full model update and then compress it using a combination of quantization, random rotations, and subsampling before sending it to the server....

## Introduction

As datasets grow larger and models more complex, training machine learning models increasingly requires distributing the optimization of model parameters over multiple machines. Existing machine learning algorithms are designed for highly controlled environments (such as data centers) where the data is distributed among machines in a balanced and i.i.d. fashion, and high-throughput networks are available.

Recently, Federated Learning (and related decentralized approaches) have been proposed as an alternative setting: a shared global model is trained under the coordination of a central server, from a federation of participating devices. The participating devices (clients) are typically large in number and have slow or unstable internet connections. A principal motivating example for Federated Learning arises when the training data comes from users' interaction with mobile applications....

Finally, in Figure 5, we study the effect of number of clients we use in a single round on the convergence. We run the Federated Averaging algorithm for a fixed number of rounds ($500$ and $2500$) with varying number of clients per round, quantize updates to $1$ bit, and plot the resulting accuracy. We see that with sufficient number of clients per round, $1024$ in this case, we can reduce the fraction of subsampled elements down to $1\%$, with only minor drop in accuracy compared to $10\%$....

Figure 5: Effect of the number of clients used in training per round.

Improving the quantization by structured random rotations. The above 1-bit and multi-bit quantization approach work best when the scales are approximately equal across different dimensions.

Low rank. We enforce every update to local model $\mathbf{H}_{t}^{i} \in {\mathbb{R}}^{d_{1} \times d_{2}}$ to be a low rank matrix of rank at most $k$, where $k$ is a fixed number. In order to do so, we express $\mathbf{H}_{t}^{i}$ as the product of two matrices: $\mathbf{H}_{t}^{i} = {\mathbf{A}_{t}^{i}\mathbf{B}_{t}^{i}}$, where $\mathbf{A}_{t}^{i} \in {\mathbb{R}}^{d_{1} \times k}$, $\mathbf{B}_{t}^{i} \in {\mathbb{R}}^{k \times d_{2}}$. In subsequent computation, we generated $\mathbf{A}_{t}^{i}$ randomly and consider a constant during a local training procedure, and we optimize only $\mathbf{B}_{t}^{i}$....
