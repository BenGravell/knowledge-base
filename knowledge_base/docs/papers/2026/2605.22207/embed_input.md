<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Kernel-Based Safe Exploration in Deep Reinforcement Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Safety has been a major concern when deploying deep reinforcement learning algorithms in the real world. A promising direction that ensures that the learned policy does not visit unsafe regions is to learn a barrier function along with the policy. A barrier is a function from states to reals that assigns low values to the initial states, high values to the unsafe states, and decreases in expectation on each transition; such a function can be used to bound the probability of reaching unsafe states. Previous attempts learned a barrier function directly from exploration data, but this required either large amounts of data or restrictions on the system dynamics. In this paper, we show how kernel embeddings can be used to learn barrier functions during deep reinforcement learning for stochastic systems with unknown dynamics. Our algorithm, kernel-based safe exploration (KBSE), learns an optimal policy and a barrier simultaneously during exploration. The barriers are computed iteratively, represented as conditional mean embeddings, and provide better probabilistic safety guarantees with more exploration. The exploration algorithm uses the learned barrier functions to identify safety violations. In the case of violation, it intervenes to modify the unsafe action to a safe action, thereby ensuring that the exploration is restricted to actions that bound the probability of reaching unsafe states.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We evaluate KBSE on several complex continuous control benchmarks. Experimental results establish our new algorithm to be suitable for synthesizing control policies that are probabilistically safe without degradation in reward accumulation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, many challenging problems in optimal policy synthesis, including solving Atari, Go, biped walking and Language Models (naveed24), have been solved using reinforcement learning (RL). This is attributed to RL's ability to maximize cumulative rewards through online exploration, without requiring a model of the underlying dynamics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For safety-critical, high-dimensional, control problems, an obstacle to deploying RL-based controllers is the possibility that a reward-maximizing controller may lead the system into unsafe states. Thus, a challenging research direction is to learn an optimal policy that is constrained by safety requirements. While there already exists a rich literature on this problem, existing solutions are still unsatisfactory: either because they do not provide certificates of correctness, or because they require data-intensive techniques, or because the learning process is subject to oscillations or high approximation errors.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose an online, kernel-based approach to learning safe control policies under unknown dynamics. Our algorithm, *kernel-based safe exploration (KBSE)*, learns an optimal policy and a barrier function simultaneously. The policy optimizes reward accumulation while being constrained by a barrier function. The barrier function (Prajna) provides a certificate that the system violates the safety specification with a bounded probability with high confidence (schon24). In particular, the exploration is constrained to use actions that do not violate the safety specification. Simultaneously, the exploration is used to update the barrier function to provide better safety guarantees over time.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Intuitively, a barrier function maps states to reals such that the function (a) assigns a low value to initial states, (b) assigns a high value to unsafe states, and (c) reduces in expectation on each step of the dynamics---the existence of such a function implies an upper bound on the probability that an unsafe state may be reached. The technical challenge in learning barrier functions is the conditional expectation in requirement (c). The key to our technique is the representation of barrier functions using conditional mean embeddings (CMEs) (Song2009CondEmbed; Klebanov2020RigorousCME) in reproducing kernel Hilbert spaces (RKHS) (scholkopf2002learning; Berlinet2004RKHSProbStat; Steinwart2008SVM). An RKHS is a Hilbert space of functions characterized by the property that pointwise evaluation is a continuous linear functional. This property renders RKHS a powerful framework for studying and manipulating functions in high-dimensional spaces. A CME embeds conditional probability distributions into an RKHS, allowing for the computation of conditional expectations via simple inner products.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, using CMEs, we can synthesize barrier functions using a simple linear optimization problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate KBSE on several challenging continuous control benchmarks available in the Gym (gym) classical control and Mujoco-based environments. For each of these benchmarks, we consider safety specifications with requirements more stringent than those used in Gym environments. Our approach generalizes the safety requirements by allowing the violation of safety constraints with a certain probability threshold. This enables us to study systems for which no policy exists to satisfy safety almost surely. We compare the performance of the control policy synthesized by KBSE against the most popular off-policy safe RL algorithms. Experimental results show that the KBSE algorithm is superior to the baseline algorithms in terms of reward accumulation and safety cost. In addition, KBSE also provides the safety probability for the learned control policies which is not possible in the case of baseline algorithms. We have relegated the proofs of statements and additional details to the supplementary material.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

For mathematical consistency, we restrict the unknown model of the system to a known function space. In particular, we assume that the CME of the probability kernel $\mathcal{T}$ lives in a vector-valued RKHS of functions from $S\times A$ to $\mathcal{H}_{k_{s}}$, denoted by $\mathcal{G}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

We utilize the above observation and empirical computation of the CME to provide a solution for Problem 1 ‣ 3 Preliminaries ‣ Kernel-Based Safe Exploration in Deep Reinforcement Learning"), as described in the next section.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Kernel-based Safe Exploration", "weight": 1.0} -->

Our goal is to solve Problem 1 ‣ 3 Preliminaries ‣ Kernel-Based Safe Exploration in Deep Reinforcement Learning") by simultaneously learning an optimal policy and a barrier function using data from the unknown CMDP. However, learning the barrier function is a data-intensive process (kordabad2024control; salamati2024data; ) and estimating the conditional expectation in the condition (iii) of the barrier function is difficult. To tackle these challenges, we use RKHS and CME to learn a valid barrier function. We show in this section that the CME transforms the problem of finding a valid barrier function into a linear program which can be solved efficiently. We also show that the barrier function learned via the approximated CME converges to the true barrier function as the size of the dataset increases (cf. Theorem 3).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Kernel-based Safe Exploration", "weight": 1.0} -->

The overall algorithm, called *kernel-based Safe Exploration* (KBSE), learns a controller online in a Deep-RL setting for the CMDP $\mathcal{M}$ with an unknown probability kernel $\mathcal{T}$. In the following subsections, we describe the main steps of the KBSE algorithm in detail, with the algorithm included in Appendix A.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Data collection", "weight": 1.0} -->

We use data generated during exploration, denoted as $\mathcal{R}=\{\langle\hat{s}_{i},\hat{a}_{i},\hat{r}_{i},\hat{s}_{i}^{+}\rangle,i=1,2,\ldots,N\}$. We can also denote the dataset alternatively as $\mathcal{R}=(\hat{S},\hat{A},\hat{R},\hat{S}^{+})$, with where $\hat{r}_{i}=R(\hat{s}_{i})$ and $s_{i}^{+}\sim\mathcal{T}(\hat{s}_{i},\hat{a}_{i},\cdot)$ for all $i$. As an off-policy RL method that stores all the transitions collected during training in a replay buffer, we randomly sample from this buffer to generate independent and identically distributed (iid) samples.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Data collection", "weight": 1.0} -->

The function $\mathtt{sample_data}$ used in Algorithm A.1 in Appendix A implements the generation of iid samples from $\mathcal{R}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Generating a Valid Barrier Function", "weight": 1.0} -->

To get a valid barrier function, we learn a barrier function from the data and perform a validity check iteratively until a valid barrier function is generated.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Generating a Valid Barrier Function", "weight": 1.0} -->

Learning barrier function. We define the barrier $B$ as a linear combination of the RBF kernel functions, given as Using the safety specification $\varphi={\langle S_{u},T\rangle}$, we classify each state $\hat{s}_{i}\in S$ using a binary safe/unsafe label $Y$. We use linear regression with regularization (montgomery12) to solve for $\alpha$ as We compute $\eta=B(s_{0})$ and $\nu=\min_{s\in S_{u}}B(s)$. The function in satisfies the conditions (i) and (ii) of being a barrier function if $\nu>\eta$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Generating a Valid Barrier Function", "weight": 1.0} -->

Barrier function validation. In order to compute the constant $c$ in the condition (iii) of the barrier function and validate the function, we compute a data-driven empirical CME $\hat{\mu}(\cdot,s,a)$ for the CME $\mu$. ‣ 3 Preliminaries ‣ Kernel-Based Safe Exploration in Deep Reinforcement Learning")) applied to the probability kernel $\mathcal{T}$. Using data $\mathcal{R}=(\hat{S},\hat{A},\hat{R},\hat{S}^{+})$, the empirical CME is where $\lambda\geq 0$ is a regularization constant, $\mathbb{I}_{N}$ is the identity matrix with dimension $N$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Generating a Valid Barrier Function", "weight": 1.0} -->

Using the reproducing property, we have the following approximation for the conditional expectation: For simplicity, we denote The empirical CME $\hat{\mu}$ deviates from the true CME $\mu$ by at most $\epsilon$ in the $\mathcal{G}$-norm with probability $1-\zeta$, where the approximation precision $\epsilon$ is an error bound to represent the Maximum Mean Discrepancy (MMD) radius of the RKHS ambiguity set centered at the empirical CME. We therefore need the barrier condition to hold robustly over all CMEs within this $\epsilon$-ball. We define an ambiguity set $\mathcal{C}_{\epsilon}$, with MMD $\epsilon$, centered at the empirical CME $\hat{\mu}(\cdot,s,a)$ such that the true CME $\mu(\cdot,s,a)$ lies within the ambiguity set with probability at least $(1-\zeta)$, i.e.,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Finding the Safe Actions", "weight": 1.0} -->

Once we compute a valid barrier function, we use the inequalities of the barrier function to identify and reduce the number of safety violations. To handle these safety violations and guide locally the reinforcement learning towards safe states, we need the local dynamics of the system. We learn a local linear dynamics of the CMDP, represented by matrices $P$ and $Q$, using state transition data $\langle\hat{s}_{t},\hat{a}_{t},\hat{s}_{t+1}\rangle$. We use regression and solve the following optimization problem (montgomery12): where $H$ denotes the number of local transitions used to learn the matrices $P$ and $Q$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Finding the Safe Actions", "weight": 1.0} -->

Assuming safety specification violation at the state $s_{t}$, we solve a quadratic optimization problem that modifies the current action $a_{t}$ to find the action $\bar{a}$ closest to $a_{t}$ leading to a safe state $s_{t+1}$, given as The above optimization ensures that we find the safe action $\bar{a}_{t}$ close to the action $a_{t}$ generated by the control policy. This ensures that the learning of the control policy $\pi_{\theta}$ by the reinforcement learning algorithm remains stable.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Finding the Safe Actions", "weight": 1.0} -->

The function $\mathtt{get_local_dynamics}$ in step A.1 of Algorithm A.1 in Appendix A solves the Equation. The function $\mathtt{get_safe_action}$ in line A.1 of Algorithm A.1 in Appendix A solves the Equation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Properties of KBSE", "weight": 1.0} -->

With more exploration, the estimate of the conditional expectation in condition (iii) of the barrier function improves. In the following theorem, we provide a bound on the convergence of the approximation of the conditional expectation in the barrier function to the true expectation as the sample size increases.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We now describe the setup and results for our experiments.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Experimental setup. All experiments are carried out on an.04 machine with Intel(R) Xeon(R) Gold 6226R $@2.90$ GHz$\times 16$ CPU, NVIDIA RTX A4000 32GB Graphics card, and 48 GB RAM using the OMNISAFE (omnisafe) framework.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Baseline for comparison. Since KBSE belongs to the class of off-policy safe RL algorithms, we consider the most popular off-policy safe RL algorithms as baseline for comparison, the Lagrangian and PID-Lagrangian approaches, i.e., DDPGLagrangian, SACLagrangian (Ray2019) and DDPGPID, SACPID (stooke20). We have not reported the comparison results with other safe RL algorithms such as CPO, PPO-Lag (Ray2019), or CUP as these are *on-policy* algorithms and are known to suffer from high variance and slow convergence compared to the off-policy methods (chung21a).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Benchmarks. Our experiments include classical and Gym-Mujoco benchmarks (gym) involving safety constraints. See Table 1 with the details of the benchmarks described in the supplementary material and the hyper-parameters in Appendix E.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Results", "weight": 1.0} -->

Training. The training time needed to learn the control policy and the number of safety violations encountered during training for the KBSE algorithm are presented in Table 1. The column $90^{th}\%ile$ provides the time-step by which $90\%$ of the total number of safety violations have occurred for the KBSE algorithm, as a percentage of the training horizon. This indicates that the number of safety violations decreases significantly in the later stages of training. Given that the baselines do not permit quantitative safety violations in their problem formulation, the metrics on safety violations (e.g., 90th percentile) are not applicable in these cases.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Results", "weight": 1.0} -->

We also observe that the training time for KBSE algorithm increases with increasing number of safety violations. This is most apparent in case of the SafetyAnt benchmark where the training time is twice than that of the baselines. The training time depends on the number of safety violations encountered during exploration (cf. Appendix D.3). This, in turn, depends on the shape of the barrier function - one with narrow "safe set" (i.e. stricter safety specifications) would cause more violations. The last column of Table 1 provides the lower bound on the safety probability guaranteed by the KBSE algorithm for each benchmark, a feature that is not integrated in the available safe RL algorithms.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Results", "weight": 1.0} -->

Testing. Table 2 compares the control policies learned by the KBSE algorithm w.r.t. the baselines. For testing policies, we use the metrics *Average Episodic Reward*, *Average Episodic Cost*, and *Average Episodic Length*. In general, the results demonstrate that the KBSE algorithm achieves higher reward and lower cost compared to the baselines. In benchmarks with high dimension, the KBSE algorithm shows superior performance that can be attributed to the larger exploration space for these high-dimensional benchmarks, providing a significant margin for improvement. On the other hand, in low-dimensional benchmarks such as SafetyPendulum and Safety-MountainCar, the performance of KBSE is similar to the baselines as the training occurs for a shorter duration and hence the margin of improvement is smaller.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Results", "weight": 1.0} -->

Further experimental results are available in the appendix, showing synthesized barrier functions (Appendix D.1), plots for $\epsilon$ and $\bar{B}$ (Appendix D.2), the relationship between training time and safety violations (Appendix D.3).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have proposed a novel safe exploration algorithm using online barrier functions constructed using kernel mean embeddings (CME). Our approach does not require knowledge of the system dynamics and uses barrier functions that involve chance constraints that allow the violation of the safety specification up to a given probability threshold. Future work includes enhancing the performance using sparse CME and considering temporal behaviors beyond safety.
