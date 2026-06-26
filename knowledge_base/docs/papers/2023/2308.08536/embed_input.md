<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Can Transformers Learn Optimal Filtering for Unknown Systems?

Topics include Transformers, Kalman filtering, State estimation, Dynamical systems, In-context learning, Unknown systems.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Tests whether transformers trained across families of dynamical systems can perform output estimation on unseen systems, sometimes matching Kalman-filter behavior without explicit model knowledge. The paper is a useful probe of in-context system adaptation and learned filtering rather than a new hand-derived estimator.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Transformer models have shown great success in natural language processing; however, their potential remains mostly unexplored for dynamical systems. In this work, we investigate the optimal output estimation problem using transformers, which generate output predictions using all the past ones. Particularly, we train the transformer using various distinct systems and then evaluate the performance on unseen systems with unknown dynamics. Empirically, the trained transformer adapts exceedingly well to different unseen systems and even matches the optimal performance given by the Kalman filter for linear systems. In more complex settings with non-i.i.d. noise, time-varying dynamics, and nonlinear dynamics like a quadrotor system with unknown parameters, transformers also demonstrate promising results. To support our experimental findings, we provide statistical guarantees that quantify the amount of training data required for the transformer to achieve a desired excess risk. Finally, we point out some limitations by identifying two classes of problems that lead to degraded performance, highlighting the need for caution when using transformers for control and estimation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many control problems such as model predictive control and safety analysis are built upon predictions of system's future trajectories. This prediction (or estimation) problem is well studied and dates back to the classical Kalman filter, which is optimal for linear systems with Gaussian noise. Methods are also developed for more complex setups, e.g. extended Kalman filter for nonlinear systems, particle filters when system dynamics can be sampled, and adaptive filters and adaptive filters for unknown systems. Existing methods typically require the knowledge of system dynamics, linearity, time-invariance, or Gaussian noise, which, for more challenging and realistic settings, may yield degraded performance.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prediction, on the other hand, in the domain of natural language processing, has witnessed recent success thanks to the transformer models, which are deep learning architectures that can generate text prediction after feeding into an input text sequence. In this work, we investigate the use of transformers in predicting dynamical system's outputs.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To begin, we assume a priori access to a collection of $M$ systems drawn from some distribution $\mathcal{D}_{sys}$ and their respective output trajectories $\{\mathbf{y}_{t}\}$. These are referred to as source systems and trajectories respectively. We then train a transformer using the source trajectories so that after feeding into past outputs $\mathbf{y}_{0:{t - 1}}$, the transformer is able to produce an estimate ${\hat{\mathbf{y}}}_{t}$ of the true output $\mathbf{y}_{t}$ (as in Fig 1). During test-time, given a previously unseen system from the same distribution $\mathcal{D}_{sys}$, we feed its observed trajectory to the trained transformer and evaluate its prediction performance. As discussed, in this setting transformer acts like a data-driven adaptive algorithm: given a system, the transformer is able to automatically adapt to it and make predictions by leveraging past data.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the remainder of this paper, we refer to a transformer trained in this way as meta-output-predictor (MOP).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related Work: Compared with earlier neural sequence models, transformers incorporate the *attention* mechanism that is able to better keep longer memories thus can handle longer input sequences. As a result, a transformer can be trained to perform a variety of tasks rather than a single task, which is known as in-context learning and serves as the foundation of MOP training in our work. Particularly, transformers are shown to be able to in-context learn linear functions; in-context reinforcement learning is studied. Recent work in studies theoretical properties of transformer-based in-context learning for both i.i.d. data and data with Markovian temporal dependencies (i.e., state trajectories), and provides guarantees in terms of excess risk and transfer risk. Compared, we (i) consider the system output prediction problem with data being non-Markovian, (ii) demonstrate the versatility of MOP through evaluations on several challenging scenarios, and (iii) study scenarios that can lead to degradations in MOP performance.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In terms of filtering/prediction for dynamical systems, there have been many recent advances. When the system dynamics is known, observer design for deterministic systems is studied in through contraction analysis. On the other hand, data-driven adaptive methods have received growing attention. For nonlinear system, techniques such as kernel methods and nonlinear splines are studied. Linear system setups allow for more principled methods such as online optimization, explicit or implicit system identification, and policy optimization. Given a class of systems, existing works typically propose algorithms, through which a predictor/filter is learned from data for a specific system. This is in contrast to the framework in our work: Training MOP with various source systems in a class empower MOP the generalizability to the whole class. In other words, the learned MOP is not a specific filter, but a prediction algorithm that can filter any system in the class. And as long as the source systems are representative for the system class, the transformer performance is guaranteed, which is no longer confined by common prerequisites such as dynamics linearity, noise Gaussianity, etc.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

For simplicity, it is assumed that the initial state $\mathbf{x}_{i,0} = 0$. These source systems may be obtained through pre-existing datasets or simulation environments. The target system under evaluation is denoted by $\mathcal{S}_{0}$, which is drawn from the same distribution $\mathcal{D}_{sys}$ and does not have to be contained within the source systems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Assumption 1 (Stability)", "weight": 1.0} -->

When the class of dynamical systems we are sampling from consists of linear systems with ${f_{i}{(\mathbf{x})}} = {\mathbf{A}_{i}\mathbf{x}}$, then Assumption 1 ‣ 2 Problem Setup ‣ Can Transformers Learn Optimal Filtering for Unknown Systems?") is satisfied when the spectral radius ${\rho{(\mathbf{A}_{i})}} < 1$ for all $i$. It is also satisfied by systems that are contracting or exponentially incrementally input-to-state stable with input $\mathbf{w}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 1 (Stability)", "weight": 1.0} -->

In this work, we seek to predict system output using a transformer, which is a deep sequence model $\text{TF}_{\theta}{( \cdot )}$ that maps system output sequences $\mathcal{Y}_{t}:=\mathbf{y}_{0:t}$ to ${\hat{\mathbf{y}}}_{t + 1}:={\text{TF}_{\theta}{(\mathcal{Y}_{t})}}$, an estimation of the true output $\mathbf{y}_{t + 1}$ at time $t + 1$. The trainable parameters of the transformer are denoted by $\theta \in \Theta$ for some parameter set $\Theta$. The transformer structure allows the sequence length $t$ to be varying.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 1 (Stability)", "weight": 1.0} -->

Assuming the access to $M$ length-$T$ output trajectories ${\{\mathbf{y}_{{i,0}:T}\}}_{i = 1}^{M}$ generated by each of the $M$ source systems, the goal in this work is to train a transformer model that, at each time $t$, can predict the output $\mathbf{y}_{0,{t + 1}}$ of the target system $S_{0}$ only using the past outputs $\mathbf{y}_{{0,0}:t}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1 (Stability)", "weight": 1.0} -->

Training a model as in where the data comes from a diversity of sources is also known as in-context learning. As a result of the training diversity, the transformer can achieve good performance on any of the source systems as well as demonstrate generalization ability for the unseen target system $\mathcal{S}_{0}$. Hence, we refer to the obtained transformer $\hat{\text{TF}}$ as meta-output-predictor (MOP).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1 (Stability)", "weight": 1.0} -->

In what follows, we first empirically demonstrate the performance of MOP in Section 3 under various setups, which is followed by theoretical analysis in Section 4.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we present the experimental results for the transformer-based MOP in different scenarios. In each scenario, during the training, we fix the number of source systems $M = 20000$ and training trajectory length $T = 50$. To evaluate the performance of MOP on different unseen test systems, for each experimental setup, we randomly generate $N = 1000$ systems and record the prediction error $\|{{\hat{\mathbf{y}}}_{t} - \mathbf{y}_{t}}\|$ over trajectories each with length $T = 50$, where ${\hat{\mathbf{y}}}_{t}$ denotes the prediction for $\mathbf{y}_{t}$. We use GPT-2 architecture with 12 layers, 8 attention heads and 256 embedding dimensions. In each experimental setup, the transformer model is trained for $10000$ training steps with batch size $64$. The $\ell_{2}$-norm is selected as the training loss function. The code we use to produce the figures and execute our algorithm can be accessed at

<!-- chunk {"id": "body-0017", "role": "body", "section": "Linear Systems", "weight": 1.0} -->

We first consider the simplest setting with linear systems and i.i.d. Gaussian noise, i.e., ${f{(\mathbf{x})}} = {\mathbf{A}\mathbf{x}}$ and ${g{(\mathbf{x})}} = {\mathbf{C}\mathbf{x}}$. The state dimension is $n = 10$ and the output dimension is $m = 5$. For each source and test system, we generate matrix $\mathbf{A}$ with entries sampled uniformly between $\lbrack 0,1\rbrack$, which is then followed by scaling so that the largest eigenvalue is $0.95$. The $\mathbf{C}$ matrix is generated with entries sampled uniformly between $\lbrack 0,1\rbrack$. The noise covariance are $\sigma_{\mathbf{w}}^{2} = 0.01$ and $\sigma_{\mathbf{v}}^{2} = 0.01$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Linear Systems", "weight": 1.0} -->

Kalman filter and linear autoregressive predictor are used as baselines, where the latter is given by ${\hat{\mathbf{y}}}_{t + 1} = {{{\mathbf{α}}_{1}\mathbf{y}_{t}} + {{\mathbf{α}}_{2}\mathbf{y}_{t - 1}}}$ and the matrix parameters $({\mathbf{α}}_{1},{\mathbf{α}}_{2})$ are updated in an online fashion using the recursive least squares (RLS) with initial covariance taken to be identity. This essentially amounts to solving a regularized least squares problem. The results are presented in Fig. LABEL:fig_linSys. We see that after some burn-in time ($\sim$ 20 steps), MOP eventually matches the performance of Kalman filter.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Linear Systems", "weight": 1.0} -->

This is because the transformer needs to collect certain amount $({\mathcal{O}{({n + m})}})$ of data to implicitly learn the system dynamics, while Kalman filter, designed with the exact system knowledge, reaches optimality immediately.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Linear Systems", "weight": 1.0} -->

When applying the Kalman filter in this case, we disregard the fact that $\mathbf{w}_{t}$ and $\mathbf{v}_{t}$ each are temporally correlated and simply use the variances of $\mathbf{w}_{t}$ and $\mathbf{v}_{t}$ for prediction. We note that for non-i.i.d. noise Kalman filter is no longer optimal. Fig. LABEL:fig_noniid shows the results for this case. We can observe the advantage of MOP over Kalman filter as Kalman filter has lost its optimality whereas MOP has learned the non-i.i.d noise prior during training.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Linear Systems", "weight": 1.0} -->

Next, we evaluate the ability of MOP to adapt to run-time changes in the dynamics. Specifically, when generating the test trajectories, we change the underlying dynamics to a randomly generated new one at time $t = {T/2} = 50$. The results are presented in Fig. LABEL:fig_changingsys. We see that when dynamics changes occur, there are sudden jumps in prediction error for both MOP and the Kalman filter; as we collect more data from the new dynamics, MOP quickly adapts, and achieves the same performance as before at around $t = 100$. The convergence of MOP after dynamics changes is much slower than the one at the beginning because the prompt always contains data from the original system.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Planar Quadrotor Systems", "weight": 1.0} -->

We consider the underactuated 6D planar quadrotor systems as in with the following discrete-time dynamics: The mass, length and moment of inertia parameters $(m,l,J)$ are chosen uniformly from $\lbrack 0.5,2\rbrack$, $g$ is set to be constant 10. For each system a trajectory is generated by randomly sampled actions. The noise $w,v$ are sampled from $N{(0,0.01)}$. The discretization time $\tau = 0.1$. The matrix $\mathbf{C} \in {61{\mathbb{R}}^{3}{\mathbb{R}}^{3\mathsf{x}6}}$ has elements uniformly sampled in $\lbrack 0,1\rbrack$. The results are provided in Fig. 3. We see that MOP significantly outperforms the extended Kalman filter.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Theoretical Guarantees", "weight": 1.0} -->

Before analyzing the performance of MOP $\hat{\text{TF}}$, we first introduce a few notions and assumptions. The analysis in this section generalizes that, which studies a special case where state is observed (i.e., $g$ is known and equal to the identity map and there is no measurement noise).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

For a transformer $\text{TF} \in \mathcal{A}$, we define the following risk to evaluate its performance on the target system $S_{0}$ over the time horizon $T$ where the expectation is over the target system $S_{0}$ and noise terms $\{\mathbf{w}_{0,t},\mathbf{v}_{0,t}\}$. Let $\text{TF}^{\star} \in \mathcal{A}$ denote an optimal transformer that minimizes $\mathcal{L}{(\text{TF})}$. Define the excess risk for $\hat{\text{TF}}$ obtained via minimizing the loss in as Then, we have the following performance guarantees on $\hat{\text{TF}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Systems that are hard to learn in-context", "weight": 1.0} -->

In this section, we investigate two limitations of MOP, one explained by our theoretical guarantees, the other regarding the performance degradation in the face of distribution shifts.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Systems that are hard to learn in-context", "weight": 1.0} -->

To illustrate the first challenge, consider two distinct classes of linear systems. The first class employs the same generation procedure as described in Section 3.1. In the second class, we follow a similar generation procedure, except for the $\mathbf{A}$ matrices, which are generated as upper-triangular matrices. Here, the diagonal entries are sampled from the interval $\lbrack{- 0.95},0.95\rbrack$, while the upper triangular entries are sampled from the range $\lbrack{- 1},1\rbrack$. The experimental results, presented in Fig. 4, demonstrate that, compared with the densely generated $\mathbf{A}$ matrices, the upper-triangular $\mathbf{A}$ matrices make it harder for MOP to learn the optimal Kalman filter. As depicted in Fig. 4, the powers of the upper-triangular $\mathbf{A}$ matrices exhibit a slower decay rate and even initial overshoot in comparison to those of the dense $\mathbf{A}$ matrices.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Systems that are hard to learn in-context", "weight": 1.0} -->

Noticing that $\mathbf{y}_{t} = {{\sum_{i = 1}^{t}{{\mathbf{C}\mathbf{A}}^{i}\mathbf{w}_{t - i}}} + \mathbf{v}_{t}}$, this implies that upper triangular $\mathbf{A}$ establishes stronger and longer temporal correlation between $\mathbf{y}_{t}$ and past $\mathbf{y}$'s, i.e., slow mixing. This poses challenges to MOP but can be potentially mitigated by feeding MOP longer prompts, i.e. the time horizon $T$. Theoretically, the slow decay rate implies larger $L_{\rho}:={C_{\rho}/{({1 - \rho})}}$, which consequentially gives a looser risk upper bound in Theorem 1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Systems that are hard to learn in-context", "weight": 1.0} -->

In our experiments in Section 3, the distribution the source and target systems are drawn from is the same. Here we run an experiment to illustrate how MOP behaves if the target distribution is different than the source one. In particular, under the experimental setup of Section 3.1, we train the MOP with noise covariances $\sigma_{\mathbf{w}}^{2} = \sigma_{\mathbf{v}}^{2} = {0.1\mathbf{I}_{n}}$ and test on systems subject to a different noise covariance. As shown in Fig. 5, MOP's performance degrades when the target systems are subject to a different noise distribution, especially when the noise covariance increases.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In conclusion, this work has demonstrated the potential of transformers in addressing prediction problems for dynamical systems. The proposed MOP exhibits remarkable performance by adapting to unseen settings, non-i.i.d. noise, and time-varying dynamics.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work motivates new avenues for the application of transformers in continuous control and dynamical systems. Future work could extend the MOP approach to closed-loop control problems to meta-learn policies for problems such as the optimal quadratic control. It is also of interest to explore new training strategies to promote robustness (e.g., against distribution shifts) and safety of this approach in control problems.
