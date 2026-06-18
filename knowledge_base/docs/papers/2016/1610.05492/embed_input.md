Federated Learning: Strategies for Improving Communication Efficiency

Topics include Low-rank models, Convolutional networks, Federated learning, Distributed systems, Learning, Sampling, Machine learning.

Federated Learning is a machine learning setting where the goal is to train a high-quality centralized model while training data remains distributed over a large number of clients each with unreliable and relatively slow network connections. We consider learning algorithms for this setting where on each round, each client independently computes an update to the current model based on its local data, and communicates this update to a central server, where the client-side updates are aggregated to compute a new global model. The typical clients in this setting are mobile phones, and communication efficiency is of the utmost importance. In this paper, we propose two ways to reduce the uplink communication costs: structured updates, where we directly learn an update from a restricted space parametrized using a smaller number of variables, e.g. either low-rank or a random mask; and sketched updates, where we learn a full model update and then compress it using a combination of quantization, random rotations, and subsampling before sending it to the server.

## Introduction

As datasets grow larger and models more complex, training machine learning models increasingly requires distributing the optimization of model parameters over multiple machines. Existing machine learning algorithms are designed for highly controlled environments (such as data centers) where the data is distributed among machines in a balanced and i.i.d. fashion, and high-throughput networks are available.

Recently, Federated Learning (and related decentralized approaches) have been proposed as an alternative setting: a shared global model is trained under the coordination of a central server, from a federation of participating devices. The participating devices (clients) are typically large in number and have slow or unstable internet connections. A principal motivating example for Federated Learning arises when the training data comes from users' interaction with mobile applications.

A subset of existing clients is selected, each of which downloads the current model.

Each client in the subset computes an updated model based on their local data.

Outline and summary. The goal of increasing communication efficiency of Federated Learning is to reduce the cost of sending $\mathbf{H}_{t}^{i}$ to the server, while learning from data stored across large number of devices with limited internet connection and availability for computation. We propose two general classes of approaches, structured updates and sketched updates. In the Experiments section, we evaluate the effect of these methods in training deep neural networks.
