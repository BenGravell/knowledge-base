The Fastest Linearly Converging Discrete-time Average Consensus Using Buffered Information

In this letter, we study the problem of accelerating reaching average consensus over connected graphs in a discrete-time communication setting. Literature has shown that consensus algorithms can be accelerated by increasing the graph connectivity or optimizing the weights agents place on the information received from their neighbors. In this letter instead of altering the communication graph, we investigate two methods that use buffered states to accelerate reaching average consensus over a given graph. In the first method, we study how convergence rate of the well-known first-order Laplacian average consensus algorithm changes with delayed feedback and obtain a sufficient condition on the ranges of delay that leads to faster convergence. In the second proposed method, we show how average consensus problem can be cast as a convex optimization problem and solved by first-order accelerated optimization algorithms for strongly-convex cost functions. We construct the fastest converging average consensus algorithm using the so-called Triple Momentum optimization algorithm....

## Introduction

In the average consensus problem the objective is to enable a group of communicating agents $\mathcal{V} = {\{ 1,\cdots,N\}}$ to arrive at the average of their local input $\mathsf{r}^{i} \in$, i.e., to obtain $\mathsf{r}^{\text{avg}} = {\frac{1}{N}{\sum_{j = 1}^{N}\mathsf{r}^{j}}}$ using local interactions. The solution to this problem is of great importance in various multi-agent applications such as robot coordination, sensor fusion, distributed estimation and formation control....

The well-known solution for the average consensus problem is the first-order iterative algorithm

## Conclusion

We examined the effect of time delay on the rate of convergence of a discrete linear time-delayed system. We showed that for this system, we can attain higher convergence rate by adding delayed feedback. The range of delay for faster convergence was then obtained. Next, we introduced an accelerated average consensus algorithm inspired by the NAG-SC and TM algorithms. We showed that the proposed algorithms have a better convergence rate compared to a similar approach in the literature. To study the results of this letter, we solved a distributed linear regression problem consisted of two average consensus problems....

The characteristic equation of the scalar dynamics in (10b) is given by

For $d = 0$, \[10, Lemma S1\] shows that asymptotic stability of (II) is guaranteed for any

By virtue of (IV), Theorem IV.1). ‣ IV Accelerated average algorithm via outdated agreement feedback ‣ The fastest linearly converging discrete-time average consensus using buffered information") provides the range of delay in terms of the eigenvalues of the Laplacian matrix such that the algorithm (I) is guaranteed to have lower convergence factor in comparison to the delay-free algorithm, i.e., it converges faster than. Therefore, given the topology of the network, faster convergence can be achieved by using outdated feedback for a fixed value of stepsize. We also note here that the range of $d$ in....

where $a_{ij}$s are the adjacency weights. In this algorithm, each agent $i$ uses the agreement feedback $\sum_{j = 1}^{N}{a_{ij}{({{x^{j}{(t)}} - {x^{i}{(t)}}})}}$ to derive its local agreement state $x^{i}$ towards $\mathsf{r}^{\text{avg}}$. When the interaction topology of the agents is a connected undirected graph, see Fig....
