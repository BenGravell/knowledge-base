<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we focus on sensor placement in linear dynamic estimation, where the objective is to place a small number of sensors in a system of interdependent states so to design an estimator with a desired estimation performance. In particular, we consider a linear time-variant system that is corrupted with process and measurement noise, and study how the selection of its sensors affects the estimation error of the corresponding Kalman filter over a finite observation interval. Our contributions are threefold: First, we prove that the minimum mean square error of the Kalman filter decreases only linearly as the number of sensors increases. That is, adding extra sensors so to reduce this estimation error is ineffective, a fundamental design limit. Similarly, we prove that the number of sensors grows linearly with the system's size for fixed minimum mean square error and number of output measurements over an observation interval; this is another fundamental limit, especially for systems where the system's size is large.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Second, we prove that the logdet of the error covariance of the Kalman filter, which captures the volume of the corresponding confidence ellipsoid, with respect to the system's initial condition and process noise is a supermodular and non-increasing set function in the choice of the sensor set. Therefore, it exhibits the diminishing returns property. Third, we provide efficient approximation algorithms that select a small number sensors so to optimize the Kalman filter with respect to this estimation error - the worst-case performance guarantees of these algorithms are provided as well. Finally, we illustrate the efficiency of our algorithms using the problem of surface-based monitoring of CO2 sequestration sites studied in Weimer et al..

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we aim to monitor dynamic, interdependent phenomena, that is, phenomena with temporal and spatial correlations ---with the term "spatial" we refer to any kind of interdependencies between the phenomena. For example, the temperature at any point of an indoor environment depends across time ---temporal correlation--- on the temperatures of the adjacent points ---spatial correlation. Therefore, these correlations allow to monitor such phenomena using a reduced number of sensors; this is an important observation when operational constraints, such as limited bandwidth and communication power, necessitate the design of estimators using a small number of sensors. Hence, in this paper we consider to place a few sensors so to monitor this kind of phenomena. To this end, we also account for unknown interdependencies, disturbances and inputs in their dynamics, and so we consider the presence of process noise, i.e., noise that affects directly these dynamics. In addition, we account for noisy sensor measurements, and so we consider the presence of measurement noise.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, we consider phenomena modelled as a linear time-variant system that is corrupted with process and measurement noise, and study how the selection of its sensors affect the minimum mean square error of the corresponding Kalman filter. To this end, we consider that each of the sensors measures a single state of the system. Thereby, this study is an important distinction in the sensor placement literature in linear systems, since the Kalman filter is the optimal linear estimator ---in the minimum mean square sense--- given a sensor set. In particular, this is the first time that the minimum mean square error of the Kalman filter is studied in this literature, where the objective is to place a small number of sensors in a system so to design an estimator with a desired performance ---this objective is combinatorial and, as a result, also important for large-scale systems, since their size necessitates the design of estimators using a small number of sensors.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

First, we identify fundamental limits in the design of the Kalman filter with respect to its sensors. In particular, given a fixed number of output measurements over an observation interval, we prove among others that the number of sensors grows linearly with the system's size for fixed minimum mean square error ---this is a design limit, especially for complex systems where the system's size is large. Moreover, given a fixed number of sensors, we prove that the number of output measurements increases only logarithmically with the system's size for fixed estimation error ---the number of output measurements is proportional to the length of the observation interval, therefore the same result holds for the length of the observation interval as well. Notwithstanding, it also decreases logarithmically with the number of sensors for fixed system's size and estimation error. Overall, these results quantify the trade-off between the number of sensors and that of output measurements so to achieve a specified value for the estimation error.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

These results are the first to characterize the effect of the sensor set on the minimum mean square error of the Kalman filter. In particular the authors quantify only the trade-off between the total energy of the consecutive output measurements and the number of its selected sensors; that is, they study no estimator with respect to its sensors. Similarly the authors consider only the maximum-likelihood estimator for the system's initial condition and only for a special class of stable linear time-invariant systems. Moreover, they consider systems that are corrupted merely with measurement noise, which is white and Gaussian. Finally, they also assume an infinite observation interval, that is, infinite number of consecutive output measurements. On the other hand, we assume a finite observation interval and study the Kalman estimator both for the system's initial condition and for the system's state at the time of the last output measurement. In addition, we consider general linear time-variant systems that are corrupted with both process and measurement noise, of any distribution (with zero mean and finite variance).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Overall, our results are the first to characterize the effect of the sensor set on the minimum mean square error of the Kalman filter, that is, the optimal linear estimator.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, we identify properties for the $\log\det$ of the error covariance of the Kalman filter with respect to the system's initial condition and process noise as a sensor set function ---the design of an optimal Kalman filter with respect to the system's initial condition and process noise implies the design of an optimal Kalman filter with respect to the system's state. Specifically, we prove that it is a supermodular and non-increasing set function in the choice of the sensor set.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast the authors study sensor placement for monitoring static phenomena with only spatial correlations. To this end, they prove that the mutual information between the chosen and non-chosen locations is submodular. On the other hand, we consider dynamic phenomena with both spatial and temporal correlations. Although the temporal correlation can be translated to a spatial one (cf. Section II), this is a fundamental distinction: the temporal correlation is known, since it is governed by the dynamics of the phenomena. In particular, this extra knowledge allows for the characterization of a richer class of estimation performance metrics, beyond that of mutual information. Specifically, in this paper we prove that the $\log\det$ of the error covariance of the Kalman filter ---that is, the optimal linear estimator--- with respect to the phenomena's initial condition and process noise is supermodular.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the sensor scheduling literature, only the $\log\det$ of the error covariance of the Kalman filter with respect to the system's state has been studied: and, the authors prove that it is a supermodular set function for special cases of systems and for zero process noise. Instead, we consider non-zero process noise, and for any system we prove that the $\log\det$ of the error covariance of the Kalman filter with respect to the initial condition and process noise is supermodular. In addition, the sensor scheduling literature assumes that a sensor set is already placed, and its objective is at each time step to select a possibly different subset of the system's outputs so to optimize an estimation metric. However, in the context of sensor placement no sensor set is assumed already placed and, in particular, the objective is to select one that remains fixed over time and achieves a desired estimation performance. In this paper we select a fixed sensor set so to optimize the $\log\det$ of the error covariance of the Kalman filter with respect to the system's initial condition and process noise.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We prove it to be supermodular in the choice of the sensor set.^11^1In, the authors prove with a counterexample in the context of sensor scheduling that the minimum mean square error of the Kalman filter with respect to the system's state is not in general a supermodular set function. We can extend this counterexample in the context of minimal sensor placement as well: the minimum mean square error of the Kalman with respect to the system's state is not in general a supermodular set function with respect to the choice of the sensor set.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Third, we consider two problems of sensor placement for the design of an optimal Kalman estimator ---we refer to the $\log\det$ of the error covariance of the Kalman filter with respect to the system's initial condition and process noise as *$\log\det$ error*. First, we consider the problem of designing an estimator that guarantees a specified $\log\det$ error and uses a minimal number of sensors ---we refer to this problem as $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"). Second, we consider the problem of designing an estimator that uses at most $r$ sensors and minimizes the $\log\det$ error ---we refer to this problem as $\mathcal{P}_{2}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms").

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Naturally, $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") and $\mathcal{P}_{2}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") are combinatorial, and in particular, they involve the minimization of a supermodular set function, that is, the $\log\det$ estimation error of the Kalman filter with respect to the system's initial condition and process noise. Because the minimization of a general supermodular function is NP-hard, we provide efficient approximation algorithms for their general solution, along with their worst-case performance guarantees. Specifically, we first provide an efficient algorithm for $\mathcal{P}_{1}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") that returns a sensor set that satisfies the estimation guarantee of $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") and has cardinality up to a multiplicative factor from the minimum cardinality sensor sets that meet the same estimation bound. Moreover, this multiplicative factor depends only logarithmically on the problem's $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") parameters. And next, we provide an efficient algorithm for $\mathcal{P}_{2}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") that returns a sensor set of cardinality $l \geq r$ ---$l$ is chosen by the designer--- and achieves a near optimal value for increasing $l$. Specifically, for $l = r$, it achieves a worst-case approximation factor $1 - {1/e}$.^22^2Such algorithms, that involve the minimization of supermodular set functions, are also used in the machine learning, path planning for information acquisition, leader selection, sensor scheduling, actuator placement and sensor placement in static phenomena literature. Their popularity is due to their simple implementation ---they are greedy algorithms--- and provable worst-case approximation factors, that are the best one can achieve in polynomial time for several classes of functions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

In comparison, the related literature has focused either a) on the optimization of the $\log\det$ of the error covariance of the Kalman filter with respect to the system's state and only for special cases of systems or for zero process noise, or b) on heuristic algorithms that provide no worst-case performance guarantees, or c) on static phenomena. In particular the authors minimize the $\log\det$ of the error covariance of the Kalman filter with respect to the state for the case where there is no process noise in the system's dynamics ---to the contrary, in our framework we assume both process and measurement noise. Moreover, to this end they use convex relaxation techniques that provide no performance guarantees. Furthermore, in and, the authors design an $H_{2}$-optimal estimation gain with a small number of non-zero columns. To this end, they also use convex relaxation techniques that provide no performance guarantees. In addition the author designs an output matrix with a desired norm so to minimize the minimum mean square error of the corresponding Kalman estimator. Nevertheless, the resultant output matrix does not guarantee a small number of selected sensors.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally the authors consider the problem of sensor placement for monitoring static phenomena with spatial correlation. To this end, they place a small number of sensors so to minimize a worst-case estimation error of an aggregate function, such as the average. In contrast, we consider dynamic phenomena with both spatial and temporal correlations that, as mentioned in the preceding paragraphs, offer a richer information setting. In addition, by minimizing the $\log\det$ error of the Kalman filter with respect to the system's initial condition and process noise, we allow for the efficient estimation of any aggregate function. Overall, with this paper we are the first to optimize the $\log\det$ error of the Kalman filter in the general dynamic case using a small number of sensors and, at the same time, to provide worst-case performance guarantees.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. In Section II, we introduce the system, estimation and sensor placement framework, along with our sensor placement problems. In Section III, we provide a series of design and performance limits, and characterize the properties of the Kalman estimator with respect to its sensor set; in Section IV, we prove that the $\log\det$ estimation error of the Kalman filter with respect to the system's initial condition and process noise is a supermodular and non-increasing set function in the choice of the sensor set; and in Section V, we provide approximation algorithms for selecting a few sensors to design an optimal Kalman filter with respect to its $\log\det$ estimation error ---the worst-case performance guarantees of these algorithms are provided as well. Finally, in Section VI, we illustrate our analytical findings, and test the efficiency of our algorithms, using simulation results from an integrator chain network and the problem of surface-based monitoring of $CO_{2}$ sequestration sites studied. Section VII concludes the paper.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A System and Estimation Framework", "weight": 1.0} -->

For $k \geq k_{0}$, consider the linear time-variant system

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Sensor Placement Framework", "weight": 1.0} -->

In this paper, we study the effect of the selected sensors in on $\text{mmse}{(x_{0})}$ and $\text{mmse}{(x_{k})}$. Therefore, this translates to the following conditions on $C_{k}$, for all $k \geq 0$, in accordance with the minimal sensor placement literature.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2 ($C$ is a full row-rank constant zero-one matrix)", "weight": 1.0} -->

For all $k \geq 0$, $C_{k} = C \in R^{c \times n}$, where $C$ is a zero-one constant matrix. Specifically, each row of $C$ has one element equal to one, and each column at most one, such that $C$ has rank $c$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2 ($C$ is a full row-rank constant zero-one matrix)", "weight": 1.0} -->

In particular, when for some $i$, $C_{ij}$ is one, the $j$-th state of $x_{k}$ is measured; otherwise, it is not. Therefore, the number of non-zero elements of $C$ coincides with the number of placed sensors.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C Sensor Placement Problems", "weight": 1.0} -->

We introduce three objectives, that we use to define the sensor placement problems we consider in this paper.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Objective 1 (Fundamental limits in optimal sensor placement)", "weight": 1.0} -->

Given an observation interval $\lbrack 0,k\rbrack$, $i \in {\{ 0,k\}}$ and a desired ${(x_{i})}$, identify fundamental limits in the design of the sensor set.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Objective 1 (Fundamental limits in optimal sensor placement)", "weight": 1.0} -->

As an example of a fundamental limit, we prove that the number of sensors grows linearly with the system's size for fixed estimation error $\text{mmse}{(x_{i})}$ ---this is clearly a major limitation, especially when the system's size is large. This result, as well as, the rest of our contributions with respect to Objective 1. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"), is presented in Section III.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Objective 2 ($\\log\\det$ estimation error as a sensor set function)", "weight": 1.0} -->

Given an observation interval $\lbrack 0,k\rbrack$, identify properties of the $\log{\det\left( \Sigma_{z_{k - 1}} \right)}$ as a sensor set function.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Objective 2 ($\\log\\det$ estimation error as a sensor set function)", "weight": 1.0} -->

We address this objective in Section IV, where we prove that $\log{\det\left( \Sigma_{z_{k - 1}} \right)}$ is a supermodular and non-increasing set function with respect to the choice of the sensor set ---the basic definitions of supermodular set functions are presented in that section as well.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Objective 3 (Algorithms for optimal sensor placement)", "weight": 1.0} -->

Given an observation interval $\lbrack 0,k\rbrack$, identify a sensor set $\mathcal{S}$ that solves either the *minimal sensor placement problem:*

<!-- chunk {"id": "body-0030", "role": "body", "section": "Objective 3 (Algorithms for optimal sensor placement)", "weight": 1.0} -->

or the *cardinality-constrained sensor placement problem for mi- nimum estimation error:*

<!-- chunk {"id": "body-0031", "role": "body", "section": "Objective 3 (Algorithms for optimal sensor placement)", "weight": 1.0} -->

$\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") designs an estimator that guarantees a specified error and uses a minimal number of sensors, and $\mathcal{P}_{2}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") an estimator that uses at most $r$ sensors and minimizes $\log{\det\left( \Sigma_{z_{k - 1}} \right)}$. The corresponding algorithms are provided in Section V.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Fundamental Limits in Optimal Sensor Placement", "weight": 1.0} -->

In this section, we present our contributions with respect to Objective 1. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"). In particular, given $i \in {\{ 0,k\}}$ and an observation interval $\lbrack 0,k\rbrack$, we prove that the number of sensors grows linearly with the system's size for fixed $\text{mmse}{(x_{i})}$. Moreover, given a sensor set of fixed cardinality, we prove that the length of the observational interval increases only logarithmically with the system's size for fixed $\text{mmse}{(x_{i})}$. Notwithstanding, it also decreases logarithmically with the number of sensors for fixed system's size and $\text{mmse}{(x_{i})}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Fundamental Limits in Optimal Sensor Placement", "weight": 1.0} -->

Overall, these novel results quantify the trade-off between the number of sensors and that of output measurements so to achieve a specified value for $\text{mmse}{(x_{i})}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Fundamental Limits in Optimal Sensor Placement", "weight": 1.0} -->

To this end, given $i \in {\{ 0,k\}}$, we first determine a lower and upper bound for $\text{mmse}{(x_{i})}$.^44^4The extension of Theorem 1. ‣ III Fundamental Limits in Optimal Sensor Placement ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") to the case $\mu = 1$ is straightforward, yet notationally involved; as a result, we omit it.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Submodularity in Optimal Sensor Placement", "weight": 1.0} -->

In this section, we present our contributions with respect to Objective 2. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"). In particular, we first derive a closed formula for $\log{\det\left( \Sigma_{z_{k - 1}} \right)}$ and then prove that it is a supermodular and non-increasing set function in the choice of the sensor set ---to the best of our knowledge, this is the first result that relates supermodularity with the $\log\det$ error of the Kalman filter within the framework of sensor placement and for the general case. This implies that the greedy algorithms for the solution of $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") and $\mathcal{P}_{2}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Submodularity in Optimal Sensor Placement", "weight": 1.0} -->

‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") return efficient approximate solutions;. In Section V, we use this supermodularity result and known results from the literature on submodular function maximization to provide efficient algorithms for the solution of $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") and $\mathcal{P}_{2}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms").

<!-- chunk {"id": "body-0037", "role": "body", "section": "Submodularity in Optimal Sensor Placement", "weight": 1.0} -->

We now give the definition of a supermodular set function, as well as, that of an non-decreasing set function ---we follow for this material.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Submodularity in Optimal Sensor Placement", "weight": 1.0} -->

Denote as $2^{\lbrack n\rbrack}$ the power set of $\lbrack n\rbrack$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Algorithms for Optimal Sensor Placement", "weight": 1.0} -->

In this section, we present our contributions with respect to Objective 3. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"). $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") and $\mathcal{P}_{2}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") are combinatorial, and in particular, we proved in Section IV that they involve the minimization of a supermodular set function, that is, the $\log\det$ error. Therefore, because the minimization of a general supermodular function is NP-hard, in the following paragraphs we provide efficient approximation algorithms for the general solution of $\mathcal{P}_{1}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Algorithms for Optimal Sensor Placement", "weight": 1.0} -->

‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") and $\mathcal{P}_{2}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"), along with their worst-case performance guarantees.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Algorithms for Optimal Sensor Placement", "weight": 1.0} -->

Specifically, we first provide an efficient algorithm for $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") that returns a sensor set that satisfies the estimation bound of $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") and has cardinality up to a multiplicative factor from the minimum cardinality sensor sets that meet the same estimation bound. Moreover, this multiplicative factor depends only logarithmically on the problem's $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") parameters. Next, we provide an efficient algorithm for $\mathcal{P}_{2}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Algorithms for Optimal Sensor Placement", "weight": 1.0} -->

‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") that returns a sensor set of cardinality $l \geq r$ ---$l$ is chosen by the designer--- and achieves a near optimal value for increasing $l$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Algorithms for Optimal Sensor Placement", "weight": 1.0} -->

To this end, we first present a fact from the supermodular functions minimization literature that we use so to construct an approximation algorithm for $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") ---we follow for this material. In particular, consider the following problem, which is of similar structure to $\mathcal{P}_{1}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Algorithms for Optimal Sensor Placement", "weight": 1.0} -->

The following greedy algorithm has been proposed for its approximate solution, for which, the subsequent fact is true.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Algorithms for Optimal Sensor Placement", "weight": 1.0} -->

Approximate solution for 𝒫.
Algorithm 1 Approximation Algorithm for 𝒫.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Fact 1", "weight": 1.0} -->

Denote as $\mathcal{S}^{\star}$ a solution to $\mathcal{P}$ and as $\mathcal{S}_{0},\mathcal{S}_{1},\ldots$ the sequence of sets picked by Algorithm 1. Moreover, let $l$ be the smallest index such that ${h{(\mathcal{S}_{l})}} \leq R$. Then,

<!-- chunk {"id": "body-0047", "role": "body", "section": "Fact 1", "weight": 1.0} -->

For several classes of submodular functions, this is the best approximation factor one can achieve in polynomial time. Therefore, we use this result to provide the approximation Algorithm 2 for $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"), where we make explicit the dependence of $\log{\det\left( \Sigma_{z_{k - 1}} \right)}$ on the selected sensor set $\mathcal{S}$. Moreover, its performance is quantified with Theorem 3. ‣ V Algorithms for Optimal Sensor Placement ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms").

<!-- chunk {"id": "body-0048", "role": "body", "section": "Fact 1", "weight": 1.0} -->

For h (𝒮) = log det (Σzk − 1,𝒮), where 𝒮 ⊆ [n], Algorithm 2 is the same as Algorithm 1.
Algorithm 2 Approximation Algorithm for 𝒫1.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Fact 2", "weight": 1.0} -->

Thus, Algorithm 3 constructs a solution of cardinality $l$ instead of $r$ and achieves an approximation factor $1 - e^{- {l/r}}$ instead of $1 - {1/e}$. For example, for $l = r$, ${1 - {1/e}} \cong.63$, while for $l = {5r}$, ${1 - e^{- {l/r}}} \cong.99$; that is, for $l = {5r}$, Algorithm 3 returns an approximate solution that although violates the cardinality constraint $r$, it achieves a value for $h$ that is near to the optimal one.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Fact 2", "weight": 1.0} -->

Moreover, for several classes of submodular functions, this is the best approximation factor one can achieve in polynomial time. Therefore, we use this result to provide the approximation Algorithm 4 for $\mathcal{P}_{2}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"), where we make explicit the dependence of $\log{\det\left( \Sigma_{z_{k - 1}} \right)}$ on the selected sensor set $\mathcal{S}$. Theorem 4. ‣ V Algorithms for Optimal Sensor Placement ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") quantifies its performance.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Fact 2", "weight": 1.0} -->

For h (𝒮) = log det (Σzk − 1,𝒮), where 𝒮 ⊆ [n], Algorithm 4 is the same as Algorithm 3.
Algorithm 4 Approximation Algorithm for 𝒫2.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-A Integrator Chain Network", "weight": 1.0} -->

We first illustrate the mechanics and efficiency of Algorithms 2 and 4 using the integrator chain in Fig. 1, where for all $i \in {\lbrack 5\rbrack}$, $A_{ii}$ is minus one, $A_{{i + 1},i}$ one, and the rest of the elements of $A$ are zero.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VI-A Integrator Chain Network", "weight": 1.0} -->

Therefore, any singleton set does not satisfy the bound $R$, while $\{ 3,5\}$ not only satisfies it but also achieves the smallest $\log\det$ error among all other sets of cardinality two; hence, $\{ 3,5\}$ is the optimal minimal sensor set to achieve the error bound $R$. Similarly, Algorithm 2 returned the optimal minimal sensor set for every other value of $R$ in the feasible region of $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"), $\lbrack\log\det{(\Sigma_{z_{4}},{\lbrack 5\rbrack})},$ $\log\det{(\Sigma_{z_{4}},\varnothing)}\rbrack$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-A Integrator Chain Network", "weight": 1.0} -->

We also run Algorithm 4 for $k\leftarrow 5$, ${\mathbb{C}}{(x_{0})}$, ${\mathbb{C}}{(w_{k^{\prime}})}$, ${\mathbb{C}}{(v_{k^{\prime}})}$ $\leftarrow I$, for all $k^{\prime} \in {\lbrack 0,k\rbrack}$, and $r$ being equal to $1,2,\ldots,5$, respectively; for all values of $r$ the chosen set coincided with the one of the same size that also minimizes $\log{\det{(\Sigma_{z_{4}}, \cdot )}}$; that is, we again observe optimal performance from our algorithms.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-A Integrator Chain Network", "weight": 1.0} -->

Finally, by increasing $r$ from $0$ to $5$, the corresponding minimum value of $\log{\det{(\Sigma_{z_{4}}, \cdot )}}$ decreases only linearly from $0$ to approximately $- 31$; this is in agreement with the quantitative result of Theorem 1. ‣ III Fundamental Limits in Optimal Sensor Placement ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"), since for any $M \in {\mathbb{R}}^{m \times m}$, ${\log{\det{(M)}}} \leq {{\text{tr}{(M)}} - m}$ (Lemma 6, Appendix D in ), and as a result, for $M$ equal to $\Sigma_{z_{k - 1}}$,

<!-- chunk {"id": "body-0056", "role": "body", "section": "VI-B $CO_{2}$ Sequestration Sites", "weight": 1.0} -->

We now illustrate the efficiency of Algorithms 2 and 4 using the problem of surface-based monitoring of $CO_{2}$ sequestration sites; these sites are used so to reduce the emissions of $CO_{2}$ from the power generation plans that burn fossil fuels. In particular, the problem of monitoring $CO_{2}$ sequestration sites becomes important due to potential leaks. In addition, since these sites cover large areas, power and communication constrains necessitate the minimal sensor placement for monitoring these leaks, as we undertake in this section.

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-B $CO_{2}$ Sequestration Sites", "weight": 1.0} -->

Specifically, following, we consider a) that the sequestration sites form an $9 \times 9$ grid (81 possible sensor locations), and b) the onset of constant unknown leaks. Then, for all $k \geq 0$, the $CO_{2}$ concentration between the sequestration sites is described with the linear time-variant system

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-B $CO_{2}$ Sequestration Sites", "weight": 1.0} -->

where $x_{k} \equiv {(d_{k}^{\top},l_{k}^{\top})}^{\top}$, $d_{k} \in {\mathbb{R}}^{81}$ is the vector of the $CO_{2}$ concentrations in the grid, and $l_{k} \in {\mathbb{R}}^{81}$ is the vector of the corresponding leaks rates; $A_{k}$ describes the dependence of the $CO_{2}$ concentrations among the adjacent sites in the grid, and with relation to the occurring leaks ---it is constructed as in the Appendix C of; and finally, $C \in {\mathbb{R}}^{81 \times 81}$ is as in Assumption 2. ‣ II-B Sensor Placement Framework ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms").

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-B $CO_{2}$ Sequestration Sites", "weight": 1.0} -->

Hence, next we run Algorithms 2 and 4 so to efficiently estimate the initial condition $x_{0}$ of ---and as a result, detect the constant leaks among the sequestration sites.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-B $CO_{2}$ Sequestration Sites", "weight": 1.0} -->

The corresponding number of sensors that Algorithm 2 achieved with respect to $R$ is shown in the left plot of Fig. 2: as $R$ increases the number of sensors decreases, as one would expect when the estimation error bound of $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") is relaxed.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-B $CO_{2}$ Sequestration Sites", "weight": 1.0} -->

For the same values for $k$, ${\mathbb{C}}{(x_{0})}$ and ${\mathbb{C}}{(v_{k^{\prime}})}$, for all $k^{\prime} \in {\lbrack 0,k\rbrack}$, we also run Algorithm 4 for $r$ that ranged from $0$ to $81$ with step size ten. The corresponding achieved values for Problem $\mathcal{P}_{2}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-B $CO_{2}$ Sequestration Sites", "weight": 1.0} -->

‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") with respect to $r$ are found in the right plot of Fig. 2: as the number of available sensors $r$ increases the minimum achieved value also decreases, as expected by the monotonicity and supermodularity of $\log{\det{(\Sigma_{z_{99}}, \cdot )}}$ ---since in the process noise is zero, $z_{99} = x_{0}$. At the same plot, we compare these values with the minimums achieved over a random sample of $80,000$ sensor sets for the various $r$ ---$10,000$ distinct sets for each $r$, where $r$ ranged from $0$ to $81$ with step size ten. Evidently, the achieved minimum random values coincide with those of Algorithm 4.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-B $CO_{2}$ Sequestration Sites", "weight": 1.0} -->

In addition, to compare the outputs of Algorithms 2 and 4, for error bounds $R$ larger than minus twenty, Algorithm 2 returns a sensor set that solves $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"), yet does not minimize the $\log{\det{(\Sigma_{z_{99}}, \cdot )}}$; notwithstanding, the difference in the achieved value with respect to the corresponding output of Algorithm 4 is small. Moreover, for error bounds $R$ less than minus twenty, Algorithm 2 returns a sensor set that not only satisfies the bound $R$; it also minimizes $\log{\det{(\Sigma_{z_{99}}, \cdot )}}$. Overall, with respect also to our comments in the preceding paragraph, both Algorithms 2 and 4 outperform the theoretical guarantees of Theorems 3.

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-B $CO_{2}$ Sequestration Sites", "weight": 1.0} -->

‣ V Algorithms for Optimal Sensor Placement ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") and 4. ‣ V Algorithms for Optimal Sensor Placement ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"), respectively.

<!-- chunk {"id": "body-0065", "role": "body", "section": "VI-B $CO_{2}$ Sequestration Sites", "weight": 1.0} -->

Finally, as in the example of Section VI-A, the minimum value of $\log{\det{(\Sigma_{z_{99}}, \cdot )}}$ ---right plot of Fig. 2--- decreases only linearly from $0$ to approximately $- 62$ as the number of sensors $r$ increases from $0$ to $81$; this is in agreement with the quantitative result of Theorem 1. ‣ III Fundamental Limits in Optimal Sensor Placement ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"), in relation to and the fact that $z_{99} = x_{0}$ ---since in the process noise is zero. Both the integrator chain example of Section VI-A and the application example of this section exemplify this fundamental design limit presented in Theorem 1. ‣ III Fundamental Limits in Optimal Sensor Placement ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"): the estimation error of the optimal linear estimator ---the Kalman filter--- decreases only linearly as the number of sensors increases.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

We considered a linear time-variant system and studied the properties of its Kalman estimator given an observation interval $\lbrack 0,k\rbrack$ and a sensor set $\mathcal{S}$. Our contributions were threefold. First, in Section III we presented several design and performance limits. For example, we proved that the cardinality of the selected sensors $\mathcal{S}$ grows linearly with the system's size for fixed minimum mean square estimation error and $k$. Second, in Section IV we proved that the $\log\det$ estimation error of the system's initial condition and process noise is a supermodular and non-increasing set function with respect to the choice of the sensor set for any $k$. Then, third, in Section V, we used this result to provide efficient approximation algorithms for the solution of $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms") and $\mathcal{P}_{2}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"), along with their worst-case performance guarantees. For example, for $\mathcal{P}_{1}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"), we provided an efficient algorithm that returns a sensor set that has cardinality up to a multiplicative factor from that of the corresponding optimal solutions; moreover, this factor depends only logarithmically on the problem's parameters. And for $\mathcal{P}_{2}$. ‣ II-C Sensor Placement Problems ‣ II Problem Formulation ‣ Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms"), we provided an efficient algorithm that returns a sensor set of cardinality $l \geq r$ and achieves a near optimal value for increasing $l$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

Finally, in Section VI, we illustrated our analytical findings, and tested the efficiency of our algorithms, using simulation results from an integrator chain network and the problem of surface-based monitoring of $CO_{2}$ sequestration sites studied in ---another application that fits the context of minimal sensor placement for effective monitoring is that of thermal control of indoor environments, such as large offices and buildings. Our future work is focused on extending the results of this paper to the problem of minimal sensor placement for sensor scheduling.
