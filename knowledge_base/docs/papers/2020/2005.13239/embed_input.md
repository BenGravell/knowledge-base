<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MOPO: Model-based Offline Policy Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Offline reinforcement learning (RL) refers to the problem of learning policies entirely from a large batch of previously collected data. This problem setting offers the promise of utilizing such datasets to acquire policies without any costly or dangerous active exploration. However, it is also challenging, due to the distributional shift between the offline training data and those states visited by the learned policy. Despite significant recent progress, the most successful prior methods are model-free and constrain the policy to the support of data, precluding generalization to unseen states. In this paper, we first observe that an existing model-based RL algorithm already produces significant gains in the offline setting compared to model-free approaches. However, standard model-based RL methods, designed for the online setting, do not provide an explicit mechanism to avoid the offline setting's distributional shift issue. Instead, we propose to modify the existing model-based RL methods by applying them with rewards artificially penalized by the uncertainty of the dynamics. We theoretically show that the algorithm maximizes a lower bound of the policy's return under the true MDP. We also characterize the trade-off between the gain and risk of leaving the support of the batch data.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our algorithm, Model-based Offline Policy Optimization (MOPO), outperforms standard model-based RL algorithms and prior state-of-the-art model-free offline RL algorithms on existing offline RL benchmarks and two challenging continuous control tasks that require generalizing from data collected for a different task. The code is available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances in machine learning using deep neural networks have shown significant successes in scaling to large realistic datasets, such as ImageNet in computer vision, SQuAD in NLP, and RoboNet in robot learning. Reinforcement learning (RL) methods, in contrast, struggle to scale to many real-world applications, e.g., autonomous driving and healthcare, because they rely on costly online trial-and-error. However, pre-recorded datasets in domains like these can be large and diverse. Hence, designing RL algorithms that can learn from those diverse, static datasets would both enable more practical RL training in the real world and lead to more effective generalization.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While off-policy RL algorithms can in principle utilize previously collected datasets, they perform poorly without online data collection. These failures are generally caused by large extrapolation error when the Q-function is evaluated on out-of-distribution actions, which can lead to unstable learning and divergence. Offline RL methods propose to mitigate bootstrapped error by constraining the learned policy to the behavior policy induced by the dataset. While these methods achieve reasonable performances in some settings, their learning is limited to behaviors within the data manifold. Specifically, these methods estimate error with respect to out-of-distribution *actions*, but only consider *states* that lie within the offline dataset and do not consider those that are out-of-distribution. We argue that it is important for an offline RL algorithm to be equipped with the ability to leave the data support to learn a better policy for two reasons: the provided batch dataset is usually sub-optimal in terms of both the states and actions covered by the dataset, and the target task can be different from the tasks performed in the batch data for various reasons, e.g., because data is not available or hard to collect for the target task.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hence, the central question that this work is trying to answer is: can we develop an offline RL algorithm that generalizes beyond the state and action support of the offline data?

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To approach this question, we first hypothesize that model-based RL methods make a natural choice for enabling generalization, for a number of reasons. First, model-based RL algorithms effectively receive more supervision, since the model is trained on every transition, even in sparse-reward settings. Second, they are trained with supervised learning, which provides more stable and less noisy gradients than bootstrapping. Lastly, uncertainty estimation techniques, such as bootstrap ensembles, are well developed for supervised learning methods and are known to perform poorly for value-based RL methods. All of these attributes have the potential to improve or control generalization. As a proof-of-concept experiment, we evaluate two state-of-the-art off-policy model-based and model-free algorithms, MBPO and SAC, in Figure 1. Although neither method is designed for the batch setting, we find that the model-based method and its variant without ensembles show surprisingly large gains. This finding corroborates our hypothesis, suggesting that model-based methods are particularly well-suited for the batch setting, motivating their use in this paper.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite these promising preliminary results, we expect significant headroom for improvement. In particular, because offline model-based algorithms cannot improve the dynamics model using additional experience, we expect that such algorithms require careful use of the model in regions outside of the data support. Quantifying the risk imposed by imperfect dynamics and appropriately trading off that risk with the return is a key ingredient towards building a strong offline model-based RL algorithm. To do so, we modify MBPO to incorporate a *reward penalty* based on an estimate of the model error. Crucially, this estimate is model-dependent, and does not necessarily penalize all out-of-distribution states and actions equally, but rather prescribes penalties based on the estimated magnitude of model error. Further, this estimation is done both on *states* and *actions*, allowing generalization to both, in contrast to model-free approaches that only reason about uncertainty with respect to actions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The primary contribution of this work is an offline model-based RL algorithm that optimizes a policy in an uncertainty-penalized MDP, where the reward function is penalized by an estimate of the model's error. Under this new MDP, we theoretically show that we maximize a lower bound of the return in the true MDP, and find the optimal trade-off between the return and the risk. Based on our analysis, we develop a practical method that estimates model error using the predicted variance of a learned model, uses this uncertainty estimate as a reward penalty, and trains a policy using MBPO in this uncertainty-penalized MDP. We empirically compare this approach, model-based offline policy optimization (MOPO), to both MBPO and existing state-of-the-art model-free offline RL algorithms. Our results suggest that MOPO substantially outperforms these prior methods on the offline RL benchmark D4RL as well as on offline RL problems where the agent must generalize to out-of-distribution states in order to succeed.

<!-- chunk {"id": "body-0010", "role": "body", "section": "MOPO: Model-Based Offline Policy Optimization", "weight": 1.0} -->

Unlike model-free methods, our goal is to design an offline model-based reinforcement learning algorithm that can take actions that are not strictly within the support of the behavioral distribution. Using a model gives us the potential to do so. However, models will become increasingly inaccurate further from the behavioral distribution, and vanilla model-based policy optimization algorithms may exploit these regions where the model is inaccurate. This concern is especially important in the offline setting, where mistakes in the dynamics will not be corrected with additional data collection.

<!-- chunk {"id": "body-0011", "role": "body", "section": "MOPO: Model-Based Offline Policy Optimization", "weight": 1.0} -->

For the algorithm to perform reliably, it's crucial to balance the return and risk: 1. the potential gain in performance by escaping the behavioral distribution and finding a better policy, and 2. the risk of overfitting to the errors of the dynamics at regions far away from the behavioral distribution. To achieve the optimal balance, we first bound the return from below by the return of a constructed model MDP penalized by the uncertainty of the dynamics (Section 4.1). Then we maximize the conservative estimation of the return by an off-the-shelf reinforcement learning algorithm, which gives MOPO, a generic model-based off-policy algorithm (Section 4.2). We discuss important practical implementation details in Section 4.3.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Quantifying the uncertainty: from the dynamics to the total return", "weight": 1.0} -->

Our key idea is to build a lower bound for the expected return of a policy $\pi$ under the true dynamics and then maximize the lower bound over $\pi$. A natural estimator for the true return $\eta_{M}{(\pi)}$ is $\eta_{\hat{M}}{(\pi)}$, the return under the estimated dynamics. The error of this estimator depends, potentially in a complex fashion, the error of $\hat{M}$, which may compound over time. In this subsection, we characterize how the error of $\hat{M}$ influences the uncertainty of the total return. We begin by stating a lemma (adapted from ) that gives a precise relationship between the performance of a policy under dynamics $T$ and dynamics $\hat{T}$. (All proofs are given in Appendix B.)

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 4.2", "weight": 1.0} -->

As a direct corollary of Assumption 4.2 and equation, we have Concretely, option (i) above corresponds to $c = {r_{\max}/{({1 - \gamma})}}$ and $\mathcal{F} = {\{ f:{{\| f\|}_{\infty} \leq 1}\}}$, and option (ii) corresponds to $c = L_{v}$ and $\mathcal{F} = {\{ f:{f\text{~is 1-Lipschitz}}\}}$. We will analyze our framework under the assumption that we have access to an oracle uncertainty quantification module that provides an upper bound on the error of the model. In our implementation, we will estimate the error of the dynamics by heuristics (see sections 4.3 and D).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 4.3", "weight": 1.0} -->

Let $\mathcal{F}$ be the function class in Assumption 4.2. We say $u:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ is an admissible error estimator for $\hat{T}$ if ${d_{\mathcal{F}}{({\hat{T}{(s,a)}},{T{(s,a)}})}} \leq {u{(s,a)}}$ for all ${s \in \mathcal{S}},{a \in \mathcal{A}}$.^11^1The definition here extends the definition of admissible confidence interval in slightly to the setting of stochastic dynamics.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Policy optimization on uncertainty-penalized MDPs", "weight": 1.0} -->

Motivated, we optimize the policy on the uncertainty-penalized MDP $\overset{\sim}{M}$ in Algorithm 1.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Policy optimization on uncertainty-penalized MDPs", "weight": 1.0} -->

1:Dynamics model T̂ with admissible error estimator u (s, a); constant λ. 2:Define ${\overset{\sim}{r}{(s,a)}} = {{r{(s,a)}} - {\lambdau{(s,a)}}}$. Let $\overset{\sim}{M}$ be the MDP with dynamics T̂ and reward $\overset{\sim}{r}$. 3:Run any RL algorithm on $\overset{\sim}{M}$ until convergence to obtain $\hat{\pi} = {\text{argmax}_{\pi}\eta_{\overset{\sim}{M}}{(\pi)}}$ Algorithm 1 Framework for Model-based Offline Policy Optimization (MOPO) with Reward Penalty Theoretical Guarantees for MOPO. We will theoretical analyze the algorithm by establishing the optimality of the learned policy $\hat{\pi}$ among a family of policies.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Policy optimization on uncertainty-penalized MDPs", "weight": 1.0} -->

Let $\pi^{\star}$ be the optimal policy on $M$ and $\pi^{\text{B}}$ be the policy that generates the batch data. Define $\epsilon_{u}{(\pi)}$ as Note that $\epsilon_{u}$ depends on $\hat{T}$, but we omit this dependence in the notation for simplicity. We observe that $\epsilon_{u}{(\pi)}$ characterizes how erroneous the model is along trajectories induced by $\pi$. For example, consider the extreme case when $\pi = \pi^{\text{B}}$. Because $\hat{T}$ is learned on the data generated from $\pi^{\text{B}}$, we expect $\hat{T}$ to be relatively accurate for those ${(s,a)} \sim \rho_{\hat{T}}^{\pi^{\text{B}}}$, and thus $u{(s,a)}$ tends to be small.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Policy optimization on uncertainty-penalized MDPs", "weight": 1.0} -->

Thus, we expect $\epsilon_{u}{(\pi^{\text{B}})}$ to be quite small. On the other end of the spectrum, when $\pi$ often visits states out of the batch data distribution in the real MDP, namely $\rho_{T}^{\pi}$ is different from $\rho_{T}^{\pi^{\text{B}}}$, we expect that $\rho_{\hat{T}}^{\pi}$ is even more different from the batch data and therefore the error estimates $u{(s,a)}$ for those ${(s,a)} \sim \rho_{\hat{T}}^{\pi}$ tend to be large. As a consequence, we have that $\epsilon_{u}{(\pi)}$ will be large.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Policy optimization on uncertainty-penalized MDPs", "weight": 1.0} -->

For $\delta \geq \delta_{\min}:={{\min_{\pi}\epsilon_{u}}{(\pi)}}$, let $\pi^{\delta}$ be the best policy among those incurring model error at most $\delta$: The main theorem provides a performance guarantee on the policy $\hat{\pi}$ produced by MOPO.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Practical implementation", "weight": 1.0} -->

Now we describe a practical implementation of MOPO motivated by the analysis above. The method is summarized in Algorithm 2 in Appendix C, and largely follows MBPO with a few key exceptions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Practical implementation", "weight": 1.0} -->

Following MBPO, we model the dynamics using a neural network that outputs a Gaussian distribution over the next state and reward^22^2If the reward function is known, we do not have to estimate the reward. The theory in Sections 4.1 and 4.2 applies to the case where the reward function is known. To extend the theory to an unknown reward function, we can consider the reward as being concatenated onto the state, so that the admissible error estimator bounds the error on $(s',r)$, rather than just $s'$.: ${{\hat{T}}_{\theta,\phi}{(s_{t + 1},\left. r \middle| {s_{t},a_{t}} \right.)}} = {\mathcal{N}{({\mu_{\theta}{(s_{t},a_{t})}},{\Sigma_{\phi}{(s_{t},a_{t})}})}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Practical implementation", "weight": 1.0} -->

The most important distinction from MBPO is that we use uncertainty quantification following the analysis above. We aim to design the uncertainty estimator that captures both the epistemic and aleatoric uncertainty of the true dynamics. Bootstrap ensembles have been shown to give a consistent estimate of the population mean in theory and empirically perform well in model-based RL. Meanwhile, the learned variance of a Gaussian probabilistic model can theoretically recover the true aleatoric uncertainty when the model is well-specified. To leverage both, we design our error estimator ${u{(s,a)}} = {\max_{i = 1}^{N}{\|{\Sigma_{\phi}^{i}{(s,a)}}\|}_{\text{F}}}$, the maximum standard deviation of the learned models in the ensemble. We use the maximum of the ensemble elements rather than the mean to be more conservative and robust.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Practical implementation", "weight": 1.0} -->

While this estimator lacks theoretical guarantees, we find that it is sufficiently accurate to achieve good performance in practice.^33^3Designing prediction confidence intervals with strong theoretical guarantees is challenging and beyond the scope of this work, which focuses on using uncertainty quantification properly in offline RL. Hence the practical uncertainty-penalized reward of MOPO is computed as ${\overset{\sim}{r}{(s,a)}} = {{\hat{r}{(s,a)}} - {\lambda{\max_{i = {1,\ldots,N}}{\|{\Sigma_{\phi}^{i}{(s,a)}}\|}_{\text{F}}}}}$ where $\hat{r}$ is the mean of the predicted reward output by $\hat{T}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Practical implementation", "weight": 1.0} -->

We treat the penalty coefficient $\lambda$ as a user-chosen hyperparameter. Since we do not have a true admissible error estimator, the value of $\lambda$ prescribed by the theory may not be an optimal choice in practice; it should be larger if our heuristic $u{(s,a)}$ underestimates the true error and smaller if $u$ substantially overestimates the true error.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

In our experiments, we aim to study the follow questions: How does MOPO perform on standard offline RL benchmarks in comparison to prior state-of-the-art approaches? Can MOPO solve tasks that require generalization to out-of-distribution behaviors? How does each component in MOPO affect performance?

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

Question is particularly relevant for scenarios in which we have logged interactions with the environment but want to use those data to optimize a policy for a different reward function. To study and challenge methods further, we construct two additional continuous control tasks that demand out-of-distribution generalization, as described in Section 5.2. To answer question, we conduct a complete ablation study to analyze the effect of each module in MOPO in Appendix D. For more details on the experimental set-up and hyperparameters, see Appendix G. For more details on the experimental set-up and hyperparameters, see Appendix G. The code is available online^44^4Code is released at We compare against several baselines, including the current state-of-the-art model-free offline RL algorithms. Bootstrapping error accumulation reduction (BEAR) aims to constrain the policy's actions to lie in the support of the behavioral distribution. This is implemented as a constraint on the average MMD between $\pi{(\cdot |s)}$ and a generative model that approximates $\pi^{\text{B}}{(\cdot |s)}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

Behavior-regularized actor critic (BRAC) is a family of algorithms that operate by penalizing the value function by some measure of discrepancy (KL divergence or MMD) between $\pi{(\cdot |s)}$ and $\pi^{\text{B}}{(\cdot |s)}$. BRAC-v uses this penalty both when updating the critic and when updating the actor, while BRAC-p uses this penalty only when updating the actor and does not explicitly penalize the critic.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Evaluation on the D4RL benchmark", "weight": 1.0} -->

To answer question, we evaluate our method on a large subset of datasets in the D4RL benchmark based on the MuJoCo simulator, including three environments (halfcheetah, hopper, and walker2d) and four dataset types (random, medium, mixed, medium-expert), yielding a total of 12 problem settings. We also perform empirical evaluations on non-MuJoCo environments in Appendix F. The datasets in this benchmark have been generated as follows: random: roll out a randomly initialized policy for 1M steps. medium: partially train a policy using SAC, then roll it out for 1M steps. mixed: train a policy using SAC until a certain (environment-specific) performance threshold is reached, and take the replay buffer as the batch. medium-expert: combine 1M samples of rollouts from a fully-trained policy with another 1M samples of rollouts from a partially trained policy or a random policy.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Evaluation on the D4RL benchmark", "weight": 1.0} -->

Results are given in Table 1. MOPO is the strongest by a significant margin on all the mixed datasets and most of the medium-expert datasets, while also achieving strong performance on all of the random datasets. MOPO performs less well on the medium datasets. We hypothesize that the lack of action diversity in the medium datasets make it more difficult to learn a model that generalizes well. Fortunately, this setting is one in which model-free methods can perform well, suggesting that model-based and model-free approaches are able to perform well in complementary settings.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Evaluation on tasks requiring out-of-distribution generalization", "weight": 1.0} -->

To answer question, we construct two environments halfcheetah-jump and ant-angle where the agent must solve a task that is different from the purpose of the behavioral policy. The trajectories of the batch data in the these datasets are from policies trained for the original dynamics and reward functions HalfCheetah and Ant in OpenAI Gym which incentivize the cheetach and ant to move forward as fast as possible. Note that for HalfCheetah, we set the maximum velocity to be $3$. Concretely, we train SAC for 1M steps and use the entire training replay buffer as the trajectories for the batch data. Then, we assign these trajectories with new rewards that incentivize the cheetach to jump and the ant to run towards the top right corner with a 30 degree angle. Thus, to achieve good performance for the new reward functions, the policy need to leave the observational distribution, as visualized in Figure 2. We include the exact forms of the new reward functions in Appendix G. In these environments, learning the correct behaviors requires leaving the support of the data distribution; optimizing solely within the data manifold will lead to sub-optimal policies.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Evaluation on tasks requiring out-of-distribution generalization", "weight": 1.0} -->

In Table 2, we show that MOPO significantly outperforms the state-of-the-art model-free approaches. In particular, model-free offline RL cannot outperform the best trajectory in the batch dataset, whereas MOPO exceeds the batch max by a significant margin. This validates that MOPO is able to generalize to out-of-distribution behaviors while existing model-free methods are unable to solve those challenges. Note that vanilla MBPO performs much better than SAC in the two environments, consolidating our claim that vanilla model-based methods can attain better results than model-free methods in the offline setting, especially where generalization to out-of-distribution is needed. The visualization in Figure 2 suggests indeed the policy learned MOPO can effectively solve the tasks by reaching to states unseen in the batch data. Furthermore, we test the limit of the generalization abilities of MOPO in these environments and the results are included in Appendix E.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we studied model-based offline RL algorithms. We started with the observation that, in the offline setting, existing model-based methods significantly outperform vanilla model-free methods, suggesting that model-based methods are more resilient to the overestimation and overfitting issues that plague off-policy model-free RL algorithms. This phenomenon implies that model-based RL has the ability to generalize to states outside of the data support and such generalization is conducive for offline RL. However, online and offline algorithms must act differently when handling out-of-distribution states. Model error on out-of-distribution states that often drives exploration and corrective feedback in the online setting can be detrimental when interaction is not allowed. Using theoretical principles, we develop an algorithm, model-based offline policy optimization (MOPO), which maximizes the policy on a MDP that penalizes states with high model uncertainty. MOPO trades off the risk of making mistakes and the benefit of diverse exploration from escaping the behavioral distribution.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In our experiments, MOPO outperforms state-of-the-art offline RL methods in both standard benchmarks and out-of-distribution generalization environments.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our work opens up a number of questions and directions for future work. First, an interesting avenue for future research to incorporate the policy regularization ideas of BEAR and BRAC into the reward penalty framework to improve the performance of MOPO on narrow data distributions (such as the "medium" datasets in D4RL). Second, it's an interesting theoretical question to understand why model-based methods appear to be much better suited to the batch setting than model-free methods. Multiple potential factors include a greater supervision from the states (instead of only the reward), more stable and less noisy supervised gradient updates, or ease of uncertainty estimation. Our work suggests that uncertainty estimation plays an important role, particularly in settings that demand generalization. However, uncertainty estimation does not explain the entire difference nor does it explain why model-free methods cannot also enjoy the benefits of uncertainty estimation. For those domains where learning a model may be very difficult due to complex dynamics, developing better model-free offline RL methods may be desirable or imperative.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Hence, it is crucial to conduct future research on investigating how to bring model-free offline RL methods up to the level of the performance of model-based methods, which would require further understanding where the generalization benefits come.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

MOPO achieves significant strides in offline reinforcement learning, a problem setting that is particularly scalable to real-world settings. Offline reinforcement learning has a number of potential application domains, including autonomous driving, healthcare, robotics, and is notably amenable to safety-critical settings where online data collection is costly. For example, in autonomous driving, online interaction with the environment runs the risk of crashing and hurting people; offline RL methods can significantly reduce that risk by learning from a pre-recorded driving dataset collected by a safe behavioral policy. Moreover, our work opens up the possibility of learning policies offline for new tasks for which we do not already have expert data.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

However, there are still risks associated with applying learned policies to high-risk domains. We have shown the benefits of explicitly accounting for error, but without reliable out-of-distribution uncertainty estimation techniques, there is a possibility that the policy will behave unpredictably when given a scenario it has not encountered. There is also the challenge of reward design: although the reward function will typically be under the engineer's control, it can be difficult to specify a reward function that elicits the desired behavior and is aligned with human objectives. Additionally, parametric models are known to be susceptible to adversarial attacks, and bad actors can potentially exploit this vulnerability. Advances in uncertainty quantification, human-computer interaction, and robustness will improve our ability to apply learning-based methods in safety-critical domains.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

Supposing we succeed at producing safe and reliable policies, there is still possibility of negative societal impact. An increased ability to automate decision-making processes may reduce companies' demand for employees in certain industries (e.g. manufacturing and logistics), thereby affecting job availability. However, historically, advances in technology have also created new jobs that did not previously exist (e.g. software engineering), and it is unclear if the net impact on jobs will be positive or negative.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

Despite the aforementioned risks and challenges, we believe that offline RL is a promising setting with enormous potential for automating and improving sequential decision-making in highly impactful domains. Currently, much additional work is needed to make offline RL sufficiently robust to be applied in safety-critical settings. We encourage the research community to pursue further study in uncertainty estimation, particularly considering the complications that arise in sequential decision problems.
