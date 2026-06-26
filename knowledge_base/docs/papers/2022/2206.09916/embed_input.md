<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Fastest Linearly Converging Discrete-time Average Consensus Using Buffered Information

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this letter, we study the problem of accelerating reaching average consensus over connected graphs in a discrete-time communication setting. Literature has shown that consensus algorithms can be accelerated by increasing the graph connectivity or optimizing the weights agents place on the information received from their neighbors. In this letter instead of altering the communication graph, we investigate two methods that use buffered states to accelerate reaching average consensus over a given graph. In the first method, we study how convergence rate of the well-known first-order Laplacian average consensus algorithm changes with delayed feedback and obtain a sufficient condition on the ranges of delay that leads to faster convergence. In the second proposed method, we show how average consensus problem can be cast as a convex optimization problem and solved by first-order accelerated optimization algorithms for strongly-convex cost functions. We construct the fastest converging average consensus algorithm using the so-called Triple Momentum optimization algorithm. We demonstrate our results using an in-network linear regression problem, which is formulated as two average consensus problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the average consensus problem the objective is to enable a group of communicating agents $\mathcal{V} = {\{ 1,\cdots,N\}}$ to arrive at the average of their local input $\mathsf{r}^{i} \in$, i.e., to obtain $\mathsf{r}^{\text{avg}} = {\frac{1}{N}{\sum_{j = 1}^{N}\mathsf{r}^{j}}}$ using local interactions. The solution to this problem is of great importance in various multi-agent applications such as robot coordination, sensor fusion, distributed estimation and formation control. In these applications, reaching fast to the average consensus is of great interest to reduce the end-to-end delays and also the convergence error caused by premature termination of the algorithm because of time constraints.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The well-known solution for the average consensus problem is the first-order iterative algorithm where $a_{ij}$s are the adjacency weights. In this algorithm, each agent $i$ uses the agreement feedback $\sum_{j = 1}^{N}{a_{ij}{({{x^{j}{(t)}} - {x^{i}{(t)}}})}}$ to derive its local agreement state $x^{i}$ towards $\mathsf{r}^{\text{avg}}$. When the interaction topology of the agents is a connected undirected graph, see Fig. 1, shows that with a proper choice of stepsize $\delta = {t_{k + 1} - t_{k}}$, executing guarantees $x^{i}\rightarrow\mathsf{r}^{\text{avg}}$, $i \in \mathcal{V}$, as $k\rightarrow\infty$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our objective in this paper is to obtain accelerated average consensus algorithms that have a provably faster convergence rate than algorithm when the same stepsize $\delta$ is used. We consider two approaches: one using outdated agreement feedback in and the other by constructing alternative algorithms using the first-order accelerated optimization algorithms for strongly convex unconstrained optimization problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

For a multi-agent system with connected undirected communication graph, the convergence rate of the average consensus algorithm is tied to the connectivity of the graph and the spectral radius of matrix $({\mathbf{I} - {\delta\mathbf{L}}})$ where $\mathbf{L}$ is the Laplacian matrix of the graph. Given this connection, various studies such as optimal adjacency weight selection for a given topology by maximizing the smallest non-zero eigenvalue of the Laplacian matrix or rewiring the graph to create topologies such as small-world network with high connectivity are proposed in the literature. In this letter, instead of altering the communication graph, we investigate two methods that use buffered states to accelerate reaching average consensus over a given graph.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our first method is motivated by evidence in the literature on the positive effect of time delay on increasing stability margin and rate of convergence of continuous-time linear time-delayed systems and use of delayed agreement feedback to accelerate continuous-time Laplacian average consensus algorithm, see. Since the results obtained for the continuous-time Laplacian algorithm cannot be trivially extended to discrete-time communication setting, we investigate using out-dated feedback in to increase the convergence rate. More precisely, we explore for what values of non-zero $d$ in $i \in \mathcal{V}$, we can archive faster convergence than. Our contribution is to characterize fully the range of delay $d$ for which convergence is accelerated.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Even though our results show that for appropriate values of delay $d \in {\mathbb{Z}}_{> 0}$ in (I), convergence can be accelerated, this method has its own limitations because of restricting the structure of the algorithm to the first-order form of algorithm. This leaves one to wonder whether faster convergence can be achieved by using alternative forms. With such motivation, for example, proposes to improve the rate of convergence by predicting future state values using a weighted summation of current and previous states, denoted as the mixing parameter. However, it requires a complex parameter design procedure since significant improvements in the rate of convergence are usually achieved by values outside the identified range of the mixing parameter which also requires agents to know extra global information \[21, Equation \]. A simple and more effective approach, however, is reported, which casts average consensus problem as a convex optimization problem and uses the accelerated Nesterov's optimization method to design a fast-converging average consensus algorithm.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nesterov algorithms, one for convex (denoted here as NAG-C) and one for strongly-convex (denoted here as NAG-SC) cost functions, are gradient-based optimization methods that use the buffered one-step past gradient value to accelerate convergence. By casting the consensus algorithm as an optimization problem with the cost $\frac{1}{2}\mathbf{x}^{\top}{\mathbf{L}\mathbf{x}}$ where $\mathbf{x}$ is the aggregated agreement state of the agents, invokes NAG-C method to design its accelerated algorithm. The choice of NAG-C is because $\mathbf{L}$ of connected graphs is positive semi-definite and thus $\frac{1}{2}\mathbf{x}^{\top}{\mathbf{L}\mathbf{x}}$ is a convex function. In this letter, we show that with an alternative modeling approach, we can in fact use the NAG-SC to arrive at a faster converging average consensus algorithm.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach also opens the door for use of the so-called Triple Momentum (hereafter denoted as TM) algorithm which is the fastest known globally convergent gradient-based method for minimizing strongly convex functions. TM also uses the buffered one-step past gradient value, but has a provably faster convergence than the Nesterov algorithms.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Organization*: Notations and preliminaries including a brief review of the relevant properties of the time-delayed discrete-time systems and the graph theoretic definitions are given in Section II. Problem definitions and the objective statements are given in Section III, while the main results are given in Sections IV and V. Numerical simulations to illustrate our results are given in Section VI. Section VII summarizes our concluding remarks.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Notations and Preliminaries", "weight": 1.0} -->

We follow to define our graph related terminologies and notations. In a network of $N$ agents with undirected connected graph topology the graph is denoted by $\mathcal{G}{(\mathcal{V},\mathcal{E},{\mathbf{A}})}$ where $\mathcal{V} = {\{ 1,\cdots,N\}}$ is the node set, $\mathcal{E} \subset {\mathcal{V} \times \mathcal{V}}$ is the edge set and ${\mathbf{A}} = {\lbrack a_{ij}\rbrack}$ is the adjacency matrix of the graph. Recall that $a_{ii} = 0$, $a_{ij} \in_{> 0}$ if $j \in \mathcal{V}$ can send information to agent $i \in \mathcal{V}$, and zero otherwise.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Notations and Preliminaries", "weight": 1.0} -->

In an undirected graph the connection between the nodes is bidirectional and $a_{ij} = a_{ji}$ if ${(i,j)} \in \mathcal{E}$. Finally, an undirected graph is connected if there is a path from every agent to every other agent in the network (see e.g. Fig. 1). The Laplacian matrix of the graph is $\mathbf{L} = {{\text{Diag}{({{\mathbf{A}}\mathbf{1}_{N}})}} - {\mathbf{A}}}$. The Laplacian matrix of a connected undirected graph is a symmetric positive semi-definite matrix that has a simple $\lambda_{1} = 0$ eigenvalue, and the rest of its eigenvalues satisfy $\lambda_{1} = 0 < \lambda_{2} \leq \cdots \leq \lambda_{N}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Notations and Preliminaries", "weight": 1.0} -->

Consider the time-delayed discrete-time system where ${\mathbf{x}{(k)}} \in^{n}$ is the state variable at time step $k$, $\mathbf{A} \in^{n \times n}$ is the system matrix, ${\mathbf{ψ}}{(k)}$ is a ${\mathbb{Z}}\rightarrow{\mathbb{R}}$ function, and $d \in {\mathbb{Z}}_{> 0}$ denotes delay. The asymptotic stability of system (II) can be assessed by the roots of its characteristic equation $\mathcal{T}:{{\mathbb{C}}\rightarrow{\mathbb{C}}}$ described by The next theorem provides the stability condition of (II).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

This paper considers the static average consensus problem over a connected undirected graph $G{(\mathcal{V},\mathcal{E},{\mathbf{A}})}$. Algorithm is the well-known solution for the average consensus problem. According to, the admissible stepsize for algorithm over a connected graph should satisfy $\delta \in {(0,\frac{2}{\lambda_{N}})}$ so that algorithm converges exponentially fast to the average of the initial conditions of the agents. The convergence factor of average consensus according to (I) is $\mathsf{r}_{0} = {\max{\{{|{1 - {\delta\lambda_{2}}}|},{|{1 - {\delta\lambda_{N}}}|}\}}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

For $\delta \in {(0,\frac{1}{\lambda_{N}}\rbrack}$, given that $0 < \lambda_{2} \leq \lambda_{N}$, $\mathsf{r}_{0} = {|{1 - {\delta\lambda_{2}}}|}$. Given $\delta \in {(0,\frac{1}{\lambda_{N}})}$, if one wants to increase the rate of convergence of algorithm then the only possible mechanism is to decrease $\delta$, or in another word, increase the frequency of the communication between the agents. The objective in this paper is to investigate algorithms that can have provably faster convergence but using the same stepsize $\delta$. Our first approach is to investigate using out-dated feedback, i.e., using non-zero $d$ in (I). Our second approach is to cast the average consensus problem as a convex optimization problem and then seek faster converging algorithms using the first-order accelerated optimization algorithms.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Accelerated average algorithm via outdated agreement feedback", "weight": 1.0} -->

Such $\mathbf{T}$ always exists, since $\mathbf{L}$ of a connected undirected graph is a symmetric and real matrix whose normalized eigenvectors $v_{1} = {{\frac{1}{\sqrt{N}}\mathbf{1}_{N}},v_{2},\cdots,v_{N}}$ are mutually orthogonal. Evidently, here we have where $\mathbf{z}_{2:N} = {(z_{2},\cdots,z_{N})}^{\top}$. Therefore, the correctness and the convergence factor of the average consensus algorithm are determined, respectively, by asymptotic stability and the worst convergence factor of the scalar dynamics in (10b).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Accelerated average algorithm via outdated agreement feedback", "weight": 1.0} -->

The characteristic equation of the scalar dynamics in (10b) is given by The roots of are all simple except when $\lambda_{i} = \frac{d^{d}}{\delta{({d + 1})}^{d + 1}}$. It is shown in that the the roots of the characteristic equation lie inside the unit circle if and only if $\delta\lambda_{i}$ lies inside the region of complex plane enclosed by the curve Based on this observation and considering the asymptotic stability condition of Theorem II.1). ‣ II Notations and Preliminaries ‣ The fastest linearly converging discrete-time average consensus using buffered information"), derives the admissible range of delay for the average consensus algorithm as follows.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Accelerated average algorithm via first-order accelerated optimization algorithms", "weight": 1.0} -->

In this section, we use the first-order accelerated optimization framework to devise accelerated average consensus algorithms that have proven faster convergence than the well-known average consensus algorithm. The work in this section is inspired by the results. argued that the conventional average consensus algorithm can be viewed as the gradient descent algorithm with fixed stepsize $\delta \in {(0,\frac{2}{\lambda_{N}})} \subset_{> 0}$ where the cost function is the agreement potential ${f{(\mathbf{x})}} = {\frac{1}{2}\mathbf{x}^{\top}{\mathbf{L}\mathbf{x}}}$. Note here that $\mathbf{0} \leq {{\nabla^{2}f}{(\mathbf{x})}} = \mathbf{L} \leq {\lambda_{N}\mathbf{I}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Accelerated average algorithm via first-order accelerated optimization algorithms", "weight": 1.0} -->

The choice of coefficient $\frac{k + 1}{k + 3}$, which tends to one, is fundamental for the argument used by Nesterov to establish the following inverse quadratic convergence rate of ${{f{({\mathbf{x}{(k)}})}} - {f{(\mathbf{x}^{\star})}}} \leq {O\left(\frac{1}{\deltak^{2}} \right)}$, for any stepsize $0 < \delta \leq {1/\lambda_{N}}$, with the best step size being $\delta = \frac{1}{\lambda_{N}}$. Since the step size is dependent on $\lambda_{N}$, this algorithm requires all the agents to know this global piece of information.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

In this section, we investigate the numerical examples that show the effect of outdated feedback data and the implementation of accelerated first-order optimization methods. We use real data from to solve a linear regression problem by reformulating it as two average consensus problems. In the first example, the common Laplacian average consensus algorithm is compared with the proposed algorithm in (I) with different number of delays to analyze the effect of $d$ on convergence. In the second example, convergence of the proposed accelerated algorithms - are compared against (I) and the algorithm.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

The dataset in has a size of 50 points for the 50 states in the United States. The variables are $y$ which is year 2002 birth rate per 1000 females 15 to 17 years old, and $x$ which is the poverty rate (the percent of the state's population living in households with incomes below the federally defined poverty level). The objective is to find a linear relation between $x$ and $y$, i.e., solve the following problem: for $a$ and $b$. Since our goal is to study the effect of delay in convergence, we simplify the problem and assume to know the optimal value of $b$. Thus, we only solve for the variable $a$ as the slope of the fitted line. Here, $b = 4.267$. By taking a derivative from with respect to $a$, setting it to zero and substituting the value of $b$, we conclude that Let us now solve this problem while the dataset is distributed over a network of 5 agents where each agent has access to 10 arbitrary state data points.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Agents of the network communicate over a connected graph depicted in Fig. 1. This solution can be achieved by solving two average consensus problems for the nominator and the denominator, and computing the division. Let $\eta_{1}^{i}{(k)}$ and $\eta_{2}^{i}{(k)}$ denote agent $i$'s local estimate of the nominator and the denominator of, respectively.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

*Outdated feedback*: Let the agents implement algorithm (I) with three different values of $d = {\{ 1,5,10\}}$ and a delay-free case. Fig. 2a depicts the convergence error of agent's trajectories with respect to the optimal value, i.e., ${e{(k)}} = {\text{log}{\sum_{i = 1}^{N}{({{{\hat{a}}^{i}{(k)}} - a})}^{2}}}$. The Green line, representing the implementation of one step delay, as seen in the figure, converge faster than the delay-free case. By increasing $d$ and using further outdated feedback, faster convergence is achieved. This shows the effect of delay in our analysis. However, as mentioned previously, exceeding $\overline{d}$ may result in divergence or slower convergence. The Turquoise trajectories with $d = 10$ illustrate the fluctuation in convergence.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

*Accelerated consensus via first-order accelerated optimization algorithms*: Next, we compare the convergence rate of the accelerated algorithms, and with that of the accelerated algorithm proposed in and also algorithm (I). Let the agents of the network solve two average consensus problems to reach $a$ globally. Fig. 2b shows the convergence error trajectories ${e{(k)}} = {\text{log}{\sum_{i = 1}^{N}{({{{\hat{a}}^{i}{(k)}} - a})}^{2}}}$ reaching the agreement similar to the previous example. Algorithm (I) with $d = 5$ converges slower compared to others, while the TM algorithm converges the fastest. Despite using the optimal parameters for the algorithm of, still TM-based algorithm delivers the fastest convergence.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We examined the effect of time delay on the rate of convergence of a discrete linear time-delayed system. We showed that for this system, we can attain higher convergence rate by adding delayed feedback. The range of delay for faster convergence was then obtained. Next, we introduced an accelerated average consensus algorithm inspired by the NAG-SC and TM algorithms. We showed that the proposed algorithms have a better convergence rate compared to a similar approach in the literature. To study the results of this letter, we solved a distributed linear regression problem consisted of two average consensus problems. We showed that the time-delayed system converges faster for some ranges of delay than the delay-free case. It was also indicated that the TM algorithm achieves faster convergence compared to the algorithms presented in and. An important conclusion that can be drawn from our study is that restricting the structure of the average consensus algorithm to the Laplacian-based form (I) limits that benefits one can get from use of buffered information to achieve faster convergence. Relaxing the composition of the algorithm, allows us to arrive at faster average consensus algorithms using the well-established accelerated optimization algorithms.
