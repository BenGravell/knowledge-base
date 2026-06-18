<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Mode Clustering for Markov Jump Systems

Topics include Markov jump systems, Mode clustering, System identification, Singular value decomposition, k-means, Model reduction.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Studies how to cluster latent modes in Markov jump models using mode-sequence estimation, singular-value structure, and k-means. The paper frames model reduction for switching systems as a statistically analyzable clustering problem over transition behavior rather than only over output trajectories.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this work, we consider the problem of mode clustering in Markov jump models. This model class consists of multiple dynamical modes with a switching sequence that determines how the system switches between them over time. Under different active modes, the observations can have different characteristics. Given the observations only and without knowing the mode sequence, the goal is to cluster the modes based on their transition distributions in the Markov chain to find a reduced-rank Markov matrix that is embedded in the original Markov chain. Our approach involves mode sequence estimation, mode clustering and reduced-rank model estimation, where mode clustering is achieved by applying the singular value decomposition and k-means. We show that, under certain conditions, the clustering error can be bounded, and the reduced-rank Markov chain is a good approximation to the original Markov chain. Through simulations, we show the efficacy of our approach and the application of our approach to real world scenarios.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modeling dynamic systems has been a problem of great interest in the signal processing and control communities for decades. Many real-world phenomena cannot be described with one dynamical model, and so switched models wherein the dynamics transition between different system models have been studied and applied widely. In human-made systems, for example, a robot may have different dynamics under different battery levels or when different modules within the robot fail. In nature, the temperature and humidity level will have different fluctuations under different weather conditions; brain electricity signals will behave differently under different emotions of the test subject. Note that in all these examples, the modes can switch over time. To model this switching, one systematic and probabilistic way is to assume the mode switching follows a Markov chain where future modes do not depend on past modes given the most recent mode. This Markov jump model has been used in power systems, air traffic management, economics, and communication systems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key challenge for such models is the model compactness -- how does one represent such a complicated dynamical system with as simple a model as possible? For example, modes like weather conditions and human emotions have extremely complex underlying dynamics with strong correlations over time. To satisfy the Markov property, one may concatenate underlying modes into a single Markov state, and Markov chains built in this way will have a state space that grows exponentially with the number of modes concatenated in the sequence. The same exponential growth rate applies when one models human-made systems with multiple sub-modules that each have multiple behavior modes (normal/abnormal). Allowing the Markov model to get extremely large is computationally inefficient for analysis and control.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior work studying model reduction of Markov jump models does not consider reduction of discrete state space, i.e. (reduction of number of Markovian modes), and prior work in state space reduction of Markov chain does not further consider Markov jump models. There have been several works studying the aggregation of states for Markov chains, which mainly relies on assumptions such as strong/weak lumpability, or aggregatibility properties of a Markov chain. There is therefore significant potential in applying the abundant algorithms and theory in Markov chain aggregation to Markov jump systems. This can achieve model reduction from a new perspective and will benefit the analysis and control of, especially large, systems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The work presented here addresses this gap. We observe that often times certain modes have similar transition behaviors, and these correlations between the modes can be exploited to construct a reduced-order model. By doing so, one may gain more insight into the nature of the complex model. Moreover, we will have fewer parameters to estimate or fewer control variables to design when learning and controlling the model, thus this may significantly reduce the computation burden. We are interested in situations where the bottleneck is due to a large discrete state-space (i.e., large number of modes) and aim to cluster and aggregate the modes for reduction. We achieve this model aggregation by clustering the modes with similar transition distributions together. We assume the dynamics for each mode are known, but we have no knowledge of the true mode sequence. In our approach, we cluster based on a reduced-dimension representation of the empirical Markov transition matrix. We then re-estimate the empirical Markov matrix using this cluster information, giving us a final low-rank estimate. We discuss our method's computational advantage, and we show our approach has guaranteed performance in the sense that the clustering error and difference between reduced model and the true model can be upper bounded.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Experiments show the efficacy of our approach as well as how the performance scales with the problem complexity.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Prior Work", "weight": 1.0} -->

Previous work on Markov jump systems includes: analysis of stability and stabilization, analysis of system with time delays, optimal control, robust control, $\mathcal{H}_{\infty}$ filtering, etc. In the context of model reduction, prior work mainly focuses on the reduction of continuous state-space (or observation space): studies the $\mathcal{H}_{\infty}$ model reduction and derives conditions under which a reduced order system can be obtained via linear matrix inequalities; reduces the model order with the help of generalized dissipation inequalities and storage functions; proposes a balanced truncation algorithm to reduce model order and gives upper bound on approximation error. While, to the best of our knowledge, the reduction of discrete state-space (number of modes) for Markov jump systems has not been considered before.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We seek an $r$-aggregatable approximation of the original Markov matrix while preserving the clustering information in the underlying aggregatable Markov matrix. Given a Markov chain, one could use the power method to iteratively simulate the evolution of the state distribution or compute the stationary distribution. So, one motivation to solve the aforementioned problem is that, during the power method, it requires $O{(n^{2})}$ scalar multiplications in one iteration for $\mathbf{P}$ but only $O{({rn})}$ for the $r$-aggregatable $\overset{\sim}{\mathbf{P}}$. Meanwhile, the compromise in accuracy brought by the reduction of computation can be upper bounded with the following theorem.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Our Approach", "weight": 1.0} -->

Our approach to solve the problem mentioned above is given in Algorithm 1.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Our Approach", "weight": 1.0} -->

Output: Partition {Ω̂1, …, Ω̂r} and matrix $\overset{\sim}{\mathbf{P}}$
Algorithm 1 Mode Clustering for Markov Jump Model

<!-- chunk {"id": "body-0013", "role": "body", "section": "Our Approach", "weight": 1.0} -->

In Line 1, we estimate the active mode at time $t$ by picking the mode whose dynamics gives the smallest residual error $|{y_{t} - {\mathbf{w}_{k}^{\intercal}\mathbf{\phi}_{t}}}|$. Then, in Line 10, based on the estimated mode sequence, we estimate $\mathbf{P}$ with the empirical Markov matrix $\hat{\mathbf{P}}$ in which the transition probability from mode $i$ to mode $j$ is estimated with the frequency of transition pair $(i,j)$ with respect to mode $i$. In Line 1, we take the SVD of $\hat{\mathbf{P}}$ and preserve the first $r$ singular value components.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Our Approach", "weight": 1.0} -->

This is essentially a denoising step that reduces the influence of perturbation $\mathbf{\Delta}$ and estimation error in $\hat{\mathbf{P}}$, and the obtained $\mathbf{U}_{r}$ is a dimension-reduced representation of $\hat{\mathbf{P}}$ that bears the low-rank structure in $\overline{\mathbf{P}}$. Then, we use k-means to estimate the clustering information in $\overline{\mathbf{P}}$. Finally, in Line 12, we compute $\overset{\sim}{\mathbf{P}}$ by taking modes within the same estimated cluster as a single mode and re-computing the empirical Markov matrix.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Our Approach", "weight": 1.0} -->

Note that if a certain mode does not show up at all in the trajectory, i.e. the denominators in Line 10 and Line 12 might be 0, then we simply assign uniform distribution to that mode, i.e. ${\hat{\mathbf{P}}{(i,j)}} = {1/n}$. We show in the proof that when the trajectory is long enough, every mode will show up with high probability.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Relevant Definitions", "weight": 1.0} -->

Before discussing theoretical guarantees of the proposed approach, we introduce some definitions that will be used later.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Main Results", "weight": 1.0} -->

Let $N^{\prime}:={\sum_{t = 0}^{N - 1}{\mathbb{1}{\{{{\hat{X}}_{t} \neq X_{t}}\}}}}$ denote the number of mistakes in the estimated mode sequence and $\eta:=\frac{N^{\prime}}{N}$ denote the mistake rate. In the following analyses, Lemma 2 gives conditions under which $N^{\prime} = 0$. Theorem 3 and Theorem 4 give the upper bounds on misclustering rate and approximation error.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Synthetic Data", "weight": 1.0} -->

We first study the performance of our approach with synthetic data. In the Markov jump model, we let ${n_{a} = 3},{n_{c} = 2}$ and number of modes $n = 50$. For each mode, the dynamics are generated by uniformly sampling its poles on $({- 1},1)$. We let input $u_{t} \sim {\mathcal{N}{}}$ and noise $n_{t} \sim {Unif{({- n_{\max}},n_{\max})}}$. The state space $\lbrack n\rbrack$ is partitioned into $r$ clusters $\Omega_{1:r}$ randomly such that every possible partition is sampled with equal probability. The mode transition probabilities $\overline{\mathbf{P}}{(\Omega_{k},:)}$ for every $k$ and initial mode distribution $\pi_{0}$ are sampled from uniform Dirichlet distribution.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Synthetic Data", "weight": 1.0} -->

The error metrics we evaluate are: (i) clustering error $\text{CE} = {n^{- 1}\min_{k \in \mathcal{K}}{\sum_{j = 1}^{r}{|{\{ i:{{i \in \Omega_{j}};{i \notin {\hat{\Omega}}_{k{(j)}}}}\}}|}}}$ where $\mathcal{K}$ is given in Definition 3. ‣ 4.1 Relevant Definitions ‣ 4 Theoretical Guarantees ‣ Mode Clustering for Markov Jump Systems N. Ozay and Z. Du were supported by ONR grant N00014-18-1-2501, L. Balzano and Z. Du were supported by AFOSR YIP award FA9550-19-1-0026, and L.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Synthetic Data", "weight": 1.0} -->

Balzano was supported by AFOSR YIP award FA9550-19-1-0026, NSF BIGDATA award IIS-1838179, and NSF CAREER award CCF-1845076."); (ii) ${\|{\overset{\sim}{\mathbf{π}} - {\mathbf{π}}}\|}_{1}$, i.e. the difference between $\overset{\sim}{\mathbf{P}}$ and $\mathbf{P}$ in terms of stationary distributions. For each parameter setup, we record the average of these two metrics over 100 experiments.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Without Perturbation ($\\mathbf{\\Delta} = 0$)", "weight": 1.0} -->

We first evaluate how the performance depend on number of clusters $r$ and noise magnitude $n_{\max}$. We set perturbation $\mathbf{\Delta} = 0$ for these test cases. The experiment results are given in Fig.(1a ‣ 5.1 Synthetic Data ‣ 5 Experiments ‣ Mode Clustering for Markov Jump Systems N. Ozay and Z. Du were supported by ONR grant N00014-18-1-2501, L. Balzano and Z. Du were supported by AFOSR YIP award FA9550-19-1-0026, and L. Balzano was supported by AFOSR YIP award FA9550-19-1-0026, NSF BIGDATA award IIS-1838179, and NSF CAREER award CCF-1845076.")-1d ‣ 5.1 Synthetic Data ‣ 5 Experiments ‣ Mode Clustering for Markov Jump Systems N. Ozay and Z. Du were supported by ONR grant N00014-18-1-2501, L. Balzano and Z.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Without Perturbation ($\\mathbf{\\Delta} = 0$)", "weight": 1.0} -->

Du were supported by AFOSR YIP award FA9550-19-1-0026, and L. Balzano was supported by AFOSR YIP award FA9550-19-1-0026, NSF BIGDATA award IIS-1838179, and NSF CAREER award CCF-1845076.")). We set $n_{\max} = 0.1$ in Fig.(1a ‣ 5.1 Synthetic Data ‣ 5 Experiments ‣ Mode Clustering for Markov Jump Systems N. Ozay and Z. Du were supported by ONR grant N00014-18-1-2501, L. Balzano and Z. Du were supported by AFOSR YIP award FA9550-19-1-0026, and L. Balzano was supported by AFOSR YIP award FA9550-19-1-0026, NSF BIGDATA award IIS-1838179, and NSF CAREER award CCF-1845076.")-1b ‣ 5.1 Synthetic Data ‣ 5 Experiments ‣ Mode Clustering for Markov Jump Systems N. Ozay and Z.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Without Perturbation ($\\mathbf{\\Delta} = 0$)", "weight": 1.0} -->

Du were supported by ONR grant N00014-18-1-2501, L. Balzano and Z. Du were supported by AFOSR YIP award FA9550-19-1-0026, and L. Balzano was supported by AFOSR YIP award FA9550-19-1-0026, NSF BIGDATA award IIS-1838179, and NSF CAREER award CCF-1845076.")) and $r = 6$ in Fig.(1c ‣ 5.1 Synthetic Data ‣ 5 Experiments ‣ Mode Clustering for Markov Jump Systems N. Ozay and Z. Du were supported by ONR grant N00014-18-1-2501, L. Balzano and Z. Du were supported by AFOSR YIP award FA9550-19-1-0026, and L.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Without Perturbation ($\\mathbf{\\Delta} = 0$)", "weight": 1.0} -->

Balzano was supported by AFOSR YIP award FA9550-19-1-0026, NSF BIGDATA award IIS-1838179, and NSF CAREER award CCF-1845076.")-1d ‣ 5.1 Synthetic Data ‣ 5 Experiments ‣ Mode Clustering for Markov Jump Systems N. Ozay and Z. Du were supported by ONR grant N00014-18-1-2501, L. Balzano and Z. Du were supported by AFOSR YIP award FA9550-19-1-0026, and L. Balzano was supported by AFOSR YIP award FA9550-19-1-0026, NSF BIGDATA award IIS-1838179, and NSF CAREER award CCF-1845076.")).

<!-- chunk {"id": "body-0025", "role": "body", "section": "With Perturbation ($\\mathbf{\\Delta} \\neq 0$)", "weight": 1.0} -->

In this test case, we fix ${n = 50},{{r = 6},{{n_{\max} = 0.05},{N = 10^{5}}}}$. The space of $\mathbf{\Delta}$ is a polytope which makes it difficult to sample uniformly, so instead for $i \in \Omega_{k}$, we sample $\mathbf{P}{(i,:)}$ from Dirichlet distribution with parameters $\alpha\mathbf{P}{(\Omega_{k},:)}$ and record $\mathbf{\Delta} = {\mathbf{P} - \overline{\mathbf{P}}}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "With Perturbation ($\\mathbf{\\Delta} \\neq 0$)", "weight": 1.0} -->

In this case, ${{\mathbb{E}}{\lbrack{\mathbf{P}{(i,:)}}\rbrack}} = {\mathbf{P}{(\Omega_{k},:)}}$ and $\alpha$ controls how much $\mathbf{P}{(i,:)}$ deviates from $\mathbf{P}{(\Omega_{k},:)}$. We sweep $\alpha$ and use scatter plots Fig.(1e ‣ 5.1 Synthetic Data ‣ 5 Experiments ‣ Mode Clustering for Markov Jump Systems N. Ozay and Z. Du were supported by ONR grant N00014-18-1-2501, L. Balzano and Z. Du were supported by AFOSR YIP award FA9550-19-1-0026, and L.

<!-- chunk {"id": "body-0027", "role": "body", "section": "With Perturbation ($\\mathbf{\\Delta} \\neq 0$)", "weight": 1.0} -->

Balzano was supported by AFOSR YIP award FA9550-19-1-0026, NSF BIGDATA award IIS-1838179, and NSF CAREER award CCF-1845076.")-1f ‣ 5.1 Synthetic Data ‣ 5 Experiments ‣ Mode Clustering for Markov Jump Systems N. Ozay and Z. Du were supported by ONR grant N00014-18-1-2501, L. Balzano and Z. Du were supported by AFOSR YIP award FA9550-19-1-0026, and L. Balzano was supported by AFOSR YIP award FA9550-19-1-0026, NSF BIGDATA award IIS-1838179, and NSF CAREER award CCF-1845076.")) to show how the error metrics vary with $\|\mathbf{\Delta}\|$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Practically Motivated Example---Patrol Robot", "weight": 1.0} -->

Now we consider a more realistic case involving Markov jump system that can possibly benefit from our approach. Assume in a region, we have $n$ stations each with position $p_{i} \in {\mathbb{R}}$ and at time $t$ there is only one active station $s_{t}$ that generates requests; the sequence of active stations $s_{0:t}$ follows a Markov chain $\mathbf{P}$. There is a robot with position $x_{t} \in {\mathbb{R}}$ at time $t$ aiming to reach the active station as fast and close as possible. Assuming the dynamics and control law of the robot are given by

<!-- chunk {"id": "body-0029", "role": "body", "section": "Practically Motivated Example---Patrol Robot", "weight": 1.0} -->

the closed-loop dynamics take the form

<!-- chunk {"id": "body-0030", "role": "body", "section": "Practically Motivated Example---Patrol Robot", "weight": 1.0} -->

which is a Markov jump model. In this setting, if the underlying Markov chain bears aggregatability property to some extent, we could use our approach to uncover the corresponding partition of modes as well as find an approximation of Markov transition matrix with stationary distribution that is easier to compute. Understanding the similarities between the stations' activation schedule can be useful to design improved control strategies for the robot.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Practically Motivated Example---Patrol Robot", "weight": 1.0} -->

In the experiment, we set ${n = 50},{{p_{i} = i},{{K = 0.7},{{n_{t} \sim {\mathcal{N}{(0,0.1)}}},{N = 10^{6}}}}}$ and sample $\overline{\mathbf{P}},\mathbf{P}$ same as 5.1.1 ‣ 5.1 Synthetic Data ‣ 5 Experiments ‣ Mode Clustering for Markov Jump Systems N. Ozay and Z. Du were supported by ONR grant N00014-18-1-2501, L. Balzano and Z. Du were supported by AFOSR YIP award FA9550-19-1-0026, and L. Balzano was supported by AFOSR YIP award FA9550-19-1-0026, NSF BIGDATA award IIS-1838179, and NSF CAREER award CCF-1845076.").

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conclusions & Future Work", "weight": 1.0} -->

In this paper, we consider the problem of model aggregation for Markov jump system from the perspective of clustering the modes based on their transition distributions. The proposed approach has guaranteed clustering error upper bound and exhibits decent performance in the experiments.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conclusions & Future Work", "weight": 1.0} -->

There are several interesting directions for future work: (i) we will see how lumpable Markov chain can help reformulate the model reduction problem; (ii) in the algorithm, after obtaining an estimate of the Markov transition matrix, one might use it to get a better estimate of the mode sequence, so several iterations between estimating switching sequence and Markov transition matrix may make both estimates more accurate; (iii) after the mode clustering, it is worth investigating if we could use a single mode to characterize the switching dynamics of all the modes within the cluster so that we could truly reduce the number of modes in the model.
