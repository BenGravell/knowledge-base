<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite overparameterization, deep networks trained via supervised learning are easy to optimize and exhibit excellent generalization. One hypothesis to explain this is that overparameterized deep networks enjoy the benefits of implicit regularization induced by stochastic gradient descent, which favors parsimonious solutions that generalize well on test inputs. It is reasonable to surmise that deep reinforcement learning (RL) methods could also benefit from this effect. In this paper, we discuss how the implicit regularization effect of SGD seen in supervised learning could in fact be harmful in the offline deep RL setting, leading to poor generalization and degenerate feature representations. Our theoretical analysis shows that when existing models of implicit regularization are applied to temporal difference learning, the resulting derived regularizer favors degenerate solutions with excessive "aliasing", in stark contrast to the supervised learning case. We back up these findings empirically, showing that feature representations learned by a deep network value function trained via bootstrapping can indeed become degenerate, aliasing the representations for state-action pairs that appear on either side of the Bellman backup.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To address this issue, we derive the form of this implicit regularizer and, inspired by this derivation, propose a simple and effective explicit regularizer, called DR3, that counteracts the undesirable effects of this implicit regularizer. When combined with existing offline RL methods, DR3 substantially improves performance and stability, alleviating unlearning in Atari 2600 games, D4RL domains and robotic manipulation from images.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep neural networks are overparameterized, with billions of parameters, which in principle should leave them vulnerable to overfitting. Despite this, supervised learning with deep networks still learn representations that generalize well. A widely held consensus is that deep nets find simple solutions that generalize due to various *implicit* regularization effects. We may surmise that using deep neural nets in reinforcement learning (RL) will work well for the same reason, learning effective representations that generalize due to such implicit regularization effects. But is this actually the case for value functions trained via bootstrapping?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we argue that, while implicit regularization leads to effective representations in supervised deep learning, it may lead to poor learned representations when training overparameterized deep network value functions. In order to rule out confounding effects from exploration and non-stationary data distributions, we focus on the offline RL setting -- where deep value networks must be trained from a static dataset of experience. There is already evidence that value functions trained via bootstrapping learn poor representations: value functions trained with offline deep RL eventually degrade in performance and this degradation is correlated with the emergence of low-rank features in the value network. Our goal is to understand the underlying cause of the emergence of poor representations during bootstrapping and develop a potential solution. Building on the theoretical framework developed by Blanc et al.; Damian et al., we characterize the implicit regularizer that arises when training deep value functions with TD learning. The form of this implicit regularizer implies that TD-learning would co-adapt feature representations at state-action tuples that appear on either side of a Bellman backup.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that this theoretically predicted aliasing phenomenon manifests in practice as feature co-adaptation, where the features of consecutive state-action tuples learned by the Q-value network become very similar in terms of their dot product (Section 3). This co-adaptation co-occurs with oscillatory learning dynamics, and training runs that exhibit feature co-adaptation typically converge to poorly performing solutions. Even when Q-values are not overestimated, prolonged training in offline RL can result in performance degradation as feature co-adaptation increases. To mitigate this co-adaptation issue, which arises as a result of implicit regularization, we propose an *explicit regularizer* that we call DR3 (Section 4). While exactly estimating and cancelling the effects of the theoretically derived implicit regularizer is computationally difficult, DR3 provides a simple and tractable theoretically-inspired approximation that mitigates the issues discussed above. In practice, DR3 amounts to regularizing the features at consecutive state-action pairs to be dissimilar in terms of their dot-product similarity.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Empirically, we find that DR3 prevents previously noted pathologies such as feature rank collapse, gives methods that train for longer and improves performance relative to the base offline RL method employed in practice.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our first contribution is the derivation of the implicit regularizer that arises when training deep net value functions via TD learning, and an empirical demonstration that it manifests as *feature co-adaptation* in the offline deep RL setting. Feature co-adaptation accounts at least in part for some of the challenges of offline deep RL, including degradation of performance with prolonged training. Second, we propose a simple and effective *explicit* regularizer for offline value-based RL, DR3, which minimizes the feature similarity between state-action pairs appearing in a bootstrapping update. DR3 is inspired by the theoretical derivation of the implicit regularizer, it alleviates co-adaptation and can be easily combined with modern offline RL methods, such as REM, CQL, and BRAC. Empirically, using DR3 in conjunction with existing offline RL methods provides about 60% performance improvement on the harder D4RL tasks, and 160% and 25% stability gains for REM and CQL, respectively, on offline RL tasks in 17 Atari 2600 games. Additionally, we observe large improvements on image-based robotic manipulation tasks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Implicit Regularization in Deep RL via TD-Learning", "weight": 1.0} -->

While the "deadly-triad" suggests that training value function approximators with bootstrapping off-policy can lead to divergence, modern deep RL algorithms have been able to successfully combine these properties. However, making too many TD updates to the Q-function in offline deep RL is known to sometimes lead to performance degradation and unlearning, even for otherwise effective modern algorithms. Such unlearning is not typically observed when training overparameterized models via supervised learning, so what about TD learning is responsible for it? We show that one possible explanation behind this pathology is the implicit regularization induced by minimizing TD error on a deep Q-network. Our theoretical results suggest that this implicit regularization "co-adapts" the representations of state-action pairs that appear in a Bellman backup (we will define this more precisely below). Empirically, this typically manifests as "co-adapted" features for consecutive state-action tuples, even with specialized TD-learning algorithms that account for distributional shift, and this in turn leads to poor final performance both in theory and in practice.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Implicit Regularization in Deep RL via TD-Learning", "weight": 1.0} -->

We first provide empirical evidence of this co-adaptation phenomenon in Section 3.1 (additional evidence in Appendix A.1) and then theoretically characterize the implicit regularization in TD learning, and discuss how it can explain the co-adaptation phenomenon in Section 3.2.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Feature Co-Adaptation And How It Relates To Implicit Regularization", "weight": 1.0} -->

In this section, we empirically identify a *feature co-adaptation* phenomenon that appears when training value functions via bootstrapping, where the feature representations of consecutive state-action pairs exhibit a large value of the dot product $\phi{(\mathbf{s},\mathbf{a})}^{\top}\phi{(\mathbf{s}^{\prime},\mathbf{a}^{\prime})}$. Note that feature co-adaptation may arise because of high cosine similarity or because of high feature norms. Feature co-adaptation appears even when there is no explicit objective to increase feature similarity.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Feature Co-Adaptation And How It Relates To Implicit Regularization", "weight": 1.0} -->

Experimental setup. We ran supervised regression and three variants of approximate dynamic programming (ADP) on an offline dataset consisting of 1% of uniformly-sampled data from the replay buffer of DQN on two Atari games, previously used in Agarwal et al.. First, for comparison, we trained a Q-function via supervised regression to Monte-Carlo (MC) return estimates on the offline dataset to estimate the value of the behavior policy. Then, we trained variants of ADP which differ in the selection procedure for the action $\mathbf{a}^{\prime}$ that appears in the target value in $\mathcal{L}_{TD}{(\theta)}$ (Equation 1). The offline SARSA variant aims to estimate the value of the behavior policy, $Q^{\pi_{\beta}}$, and sets $\mathbf{a}^{\prime}$ to the actual action observed at the next time step in the dataset, such that ${(\mathbf{s}^{\prime},\mathbf{a}^{\prime})} \in \mathcal{D}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Feature Co-Adaptation And How It Relates To Implicit Regularization", "weight": 1.0} -->

The TD-learning variant also aims to estimate the value of the behavior policy, but utilizes the expectation of the target Q-value over actions $\mathbf{a}^{\prime}$ sampled from the behavior policy $\pi_{\beta}$, $\mathbf{a}^{\prime} \sim \pi_{\beta}{( \cdot |\mathbf{s}^{\prime})}$. We do not have access to the functional form of $\pi_{\beta}$ for the experiment shown in Figure 1 since the dataset corresponds to the behavior policy induced by the replay buffer of an online DQN, so we train a model for this policy using supervised learning. However, we see similar results comparing offline SARSA and TD-learning on a gridworld domain where we can access the exact functional form of the behavior policy in Appendix A.6.2. All of the methods so far estimate $Q^{\pi_{\beta}}$ using different target value estimators.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Feature Co-Adaptation And How It Relates To Implicit Regularization", "weight": 1.0} -->

We also train Q-learning, which chooses the action $\mathbf{a}^{\prime}$ to maximize the learned Q-function. While Q-learning learns a different Q-function, we can still compare the relative stability of these methods to gain intuition about the learning dynamics. In addition to feature dot products $\phi{(\mathbf{s},\mathbf{a})}^{\top}\phi{(\mathbf{s}^{\prime},\mathbf{a}^{\prime})}$, we also track the average prediction of the Q-network over the dataset to measure whether the predictions diverge or are stable in expectation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Feature Co-Adaptation And How It Relates To Implicit Regularization", "weight": 1.0} -->

Observing feature co-adaptation empirically. As shown in Figure 1 (right), the average dot product (top row) between features at consecutive state-action tuples continuously increases for both Q-learning and TD-learning (after enough gradient steps), whereas it flatlines and converges to a small value for supervised regression. We might at first think that this is simply a case of Q-learning failing to converge. However, the bottom row shows that the average Q-values do in fact converge to a stable value. Despite this, the optimizer drives the network towards higher feature dot products. There is no explicit term in the TD error objective that encourages this behavior, indicating the presence of some implicit regularization phenomenon. This *implicit* preference towards maximizing the dot products of features at consecutive state-action tuples is what we call "feature co-adaptation."

<!-- chunk {"id": "body-0016", "role": "body", "section": "Feature Co-Adaptation And How It Relates To Implicit Regularization", "weight": 1.0} -->

When does feature co-adaptation emerge? Observe in Figure 1 (right) that the feature dot products for offline SARSA converge quickly and are relatively flat, similarly to supervised regression. This indicates that utilizing a bootstrapped update alone is not responsible for the increasing dot-products and instability, because while offline SARSA uses backups, it behaves similarly to supervised MC regression. Unlike offline SARSA, feature co-adaptation emerges for TD-learning, which is surprising as TD-learning also aims to estimate the value of the behavior policy, and hence should match offline SARSA in expectation. The key difference is that while offline SARSA always utilizes actions $\mathbf{a}^{\prime}$ observed in the training dataset for the backup, TD-learning may utilize potentially unseen actions $\mathbf{a}^{\prime}$ in the backup, even though these actions $\mathbf{a}^{\prime} \sim \pi_{\beta}{( \cdot |\mathbf{s}^{\prime})}$ are *within* the distribution of the data-generating policy.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Feature Co-Adaptation And How It Relates To Implicit Regularization", "weight": 1.0} -->

This suggests that utilizing out-of-sample actions in the Bellman backup, even when they are not out-of-distribution, critically alters the learning dynamics. This is distinct from the more common observation in offline RL, which attributes training challenges to out-of-distribution actions, but not out-of-sample actions. The theoretical model developed in Section 3.2 will provide an explanation for this observation with a discussion about how feature co-adaption caused due to out-of-sample actions can be detrimental in offline RL.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Theoretically Characterizing Implicit Regularization in TD-Learning", "weight": 1.0} -->

Why does feature co-adaptation emerge in TD-learning and what do *out-of-sample* actions have to do with it? To answer this question, we theoretically characterize the implicit regularization effects in TD-learning. We analyze the learning dynamics of TD learning in the overparameterized regime, where there are many different parameter vectors $\theta$ that fully minimize the training set temporal difference error. We base our analysis of TD learning on the analysis of implicit regularization in supervised learning, previously developed by Blanc et al.; Damian et al..

<!-- chunk {"id": "body-0019", "role": "body", "section": "Theoretically Characterizing Implicit Regularization in TD-Learning", "weight": 1.0} -->

Background. When training an overparameterized $f_{\theta}{(\mathbf{x})}$ via supervised regression using the squared loss, denoted by $L$, many different values of $\theta$ will satisfy ${L{(\theta)}} = 0$ on the training set due to overparameterization, but Blanc et al. show that the dynamics of stochastic gradient descent will only find fixed points $\theta^{\ast}$ that additionally satisfy a condition which can be expressed as ${{\nabla_{\theta}R}{(\theta^{\ast})}} = 0$, along certain directions (that we will describe shortly). This function $R{(\theta)}$ is referred to as the implicit regularizer.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Theoretically Characterizing Implicit Regularization in TD-Learning", "weight": 1.0} -->

Any solution $\theta^{\ast}$ found by Equation 2 must satisfy ${{\nabla_{\theta}R}{(\theta^{\ast})}} = 0$ along directions $\mathbf{v} \in {\mathbb{R}}^{|\theta|}$ which lie in the null space of the Hessian of the loss ${\nabla_{\theta}^{2}L}{(\theta^{\ast})}$ at $\theta^{\ast}$, $\mathbf{v} \in {\text{Null}{({{\nabla_{\theta}^{2}L}{(\theta^{\ast})}})}}$. The intuition behind the implicit regularization effect is that along such directions in the parameter space, the Hessian is unable to contract $\theta_{k}$ when running noisy gradient updates (Equation 2).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Theoretically Characterizing Implicit Regularization in TD-Learning", "weight": 1.0} -->

Therefore, the only condition that the noisy gradient updates converge/stabilize at $\theta^{\ast}$ is given by the condition that ${{\nabla R}{(\theta^{\ast})}} = 0$. This model corroborates empirical findings about the solutions found by SGD with deep nets, which motivates our use of this framework.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Theoretically Characterizing Implicit Regularization in TD-Learning", "weight": 1.0} -->

Our setup. Following this framework, we analyze the fixed points of noisy TD-learning.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Theoretically Characterizing Implicit Regularization in TD-Learning", "weight": 1.0} -->

We use a deterministic policy $\mathbf{a}_{i}^{\prime} = {\pi{(\mathbf{s}_{i}^{\prime})}}$ to simplify exposition. Following Damian et al., we can set the noise model $M$ as $M = {\sum_{i}{{\nabla_{\theta}Q}{(\mathbf{s}_{i},\mathbf{a}_{i})}{\nabla_{\theta}Q}{(\mathbf{s}_{i},\mathbf{a}_{i})}^{\top}}}$, or utilize a different choice of $M$, but we will derive the general form first. Let $\theta^{\ast}$ denote a stationary point of the training TD error, such that the pseudo-gradient ${g{(\theta^{\ast})}} = 0$. Further, we denote the derivative of $g{(\theta)}$ w.r.t.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Theoretically Characterizing Implicit Regularization in TD-Learning", "weight": 1.0} -->

$\theta$ as the matrix ${G{(\theta)}} \in {\mathbb{R}}^{{|\theta|} \times {|\theta|}}$, and refer to it as the *pseudo-Hessian*: although $G{(\theta)}$ is not actually the second derivative of any well-defined objective, since TD updates are not proper gradient updates, as we will see it will play a similar role to the Hessian in gradient descent.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Theoretically Characterizing Implicit Regularization in TD-Learning", "weight": 1.0} -->

Assumptions. To simplify analysis, we assume that matrices $G$ and $M$ (i.e., the noise covariance matrix) span the same $n$-dimensional basis in $d$-dimensional space, where $d$ is the number of parameters and $n$ is the number of datapoints, and $n \ll d$ due to overparameterization. We also require $\theta^{\ast}$ to satisfy a technical criterion that requires approximate alignment between the eigenspaces of $G$ and the gradient of the Q-function, without which noisy TD may not be stable at $\theta^{\ast}$. We summarize all the assumptions in Appendix C, and present the resulting regularizer below.

<!-- chunk {"id": "body-0026", "role": "body", "section": "DR3: Explicit Regularization for Deep TD-Learning", "weight": 1.0} -->

Since the implicit regularization effects in TD-learning can lead to feature co-adaptation, which in turn is correlated with poor performance, can we instead derive an *explicit* regularizer to alleviate this issue? Inspired by the analysis in the previous section, we will propose an *explicit* regularizer that attempts to counteract the second term in Equation 3.1. ‣ 3.2 Theoretically Characterizing Implicit Regularization in TD-Learning ‣ 3 Implicit Regularization in Deep RL via TD-Learning ‣ DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization"), which would otherwise lead to co-adaptation and poor representations.

<!-- chunk {"id": "body-0027", "role": "body", "section": "DR3: Explicit Regularization for Deep TD-Learning", "weight": 1.0} -->

Note that we drop the stop gradient on $Q_{\theta}{(\mathbf{s}_{i}^{\prime},\mathbf{a}_{i}^{\prime})}$ in $\Delta{(\theta)}$, as it performs slightly better in practice (Table A.1), although as shown in that Table, the version with the stop gradient also significantly improves over the base method. The first term of $R_{TD}{(\theta)}$ corresponds to the regularizer from supervised learning. Our proposed method, DR3, simply combines approximations to $\Delta{(\theta)}$ with various offline RL algorithms.

<!-- chunk {"id": "body-0028", "role": "body", "section": "DR3: Explicit Regularization for Deep TD-Learning", "weight": 1.0} -->

For any offline RL algorithm, Alg, with objective $\mathcal{L}_{\text{Alg}}{(\theta)}$, the training objective with DR3 is given: ${\mathcal{L}{(\theta)}}:={{\mathcal{L}_{\text{Alg}}{(\theta)}} + {c_{0}\Delta{(\theta)}}}$, where $c_{0}$ is the DR3 coefficient. See Appendix E.3 for details on how we tune $c_{0}$ in this paper.

<!-- chunk {"id": "body-0029", "role": "body", "section": "DR3: Explicit Regularization for Deep TD-Learning", "weight": 1.0} -->

Practical version of DR3. In order to practically instantiate DR3, we need to choose a particular noise model $M$. In general, it is not possible to know beforehand the "correct" choice of $M$ (Equation 3), even in supervised learning, as this is a complicated function of the data distribution, neural network architecture and initialization. Therefore, we instantiate DR3 with two heuristic choices of $M$: (i) $M$ induced by label noise studied in prior work for supervised learning and for which we need to run a computationally heavy fixed-point computation for $M$, and (ii) a simpler alternative that sets $\Sigma_{M}^{\ast} = I$. We find that both of these variants generally perform well empirically (Figure 6), and improve over the base offline RL method, and so we utilize (ii) in practice due to low computational costs.

<!-- chunk {"id": "body-0030", "role": "body", "section": "DR3: Explicit Regularization for Deep TD-Learning", "weight": 1.0} -->

Additionally, because computing and backpropagating through per-example gradient dot products is slow, we instead approximate $\Delta{(\theta)}$ with the contribution only from the last layer parameters (*i.e.*, $\sum_{i}{{\nabla_{\mathbf{w}}Q_{\theta}}{(\mathbf{s}_{i},\mathbf{a}_{i})}^{\top}{\nabla_{\mathbf{w}}Q_{\theta}}{(\mathbf{s}_{i}^{\prime},\mathbf{a}_{i}^{\prime})}}$), similarly to tractable Bayesian neural nets. As shown in Appendix A.5, the practical version of DR3 performs similarly to the label-noise version.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental Evaluation of DR3", "weight": 1.0} -->

Our experiments aim to evaluate the extent to which DR3 improves performance in offline RL in practice, and to study its effect on prior observations of rank collapse. To this end, we investigate if DR3 improves offline RL performance and stability on three offline RL benchmarks: Atari 2600 games with discrete actions, continuous control tasks from D4RL, and image-based robotic manipulation tasks.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experimental Evaluation of DR3", "weight": 1.0} -->

Following prior work, we evaluate DR3 in terms of final offline RL performance after a given number of iterations. Additionally, we report *training stability*, which is important in practice as offline RL does not admit cheap validation of trained policies for model selection. To evaluate stability, we train for a large number of gradient steps (2-3x longer than prior work) and either report the average performance over the course of training or the final performance at the end of training. We expect that a stable method that does not unlearn with more gradient steps, should have better average performance, as compared to a method that attains good peak performance but degrades with more training. See Appendix E for further details.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experimental Evaluation of DR3", "weight": 1.0} -->

Offline RL on Atari 2600 games. We compare DR3 to prior offline RL methods on a set of offline Atari datasets of varying sizes and quality, akin to Agarwal et al.; Kumar et al.. We evaluated on three datasets: 1% and 5% samples drawn uniformly at random from DQN replay; a dataset with more suboptimal data consisting of the first 10% samples observed by an online DQN. Following Agarwal et al., we report the interquartile mean (IQM) normalized scores across 17 games over the course of training in Figure 4 and report the IQM average performance in Table 1. Observe that combining DR3 with modern offline RL methods (CQL, REM) attains the best final and average performance across the 17 Atari games tested, directly improving upon prior methods across all the datasets. When DR3 is used in conjunction with REM, it prevents severe unlearning and performance degradation with more training. CQL + DR3 improves by 20% over CQL on final performance and attains 25% better average performance.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experimental Evaluation of DR3", "weight": 1.0} -->

While DR3 is not unequivocally "stable", as its performance also degrades relative to the peak it achieves (Figure 4), it is more stable relative to base offline RL algorithms. We also compare DR3 to the ${srank}{(\Phi)}$ penalty proposed to counter rank collapse. Directly taking median normalized score improvements reported by Kumar et al., CQL + DR3 improves by over 2x (31.5%) over naïve CQL relative to the srank penalty (14.1%), indicating DR3's efficacy.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experimental Evaluation of DR3", "weight": 1.0} -->

Offline RL on robotic manipulation from images. Next, we aim to evaluate the efficacy of DR3 on two image-based robotic manipulation tasks (visualized on the right) that require composition of skills (e.g., opening a drawer, closing a drawer, picking an obstructive object, placing an object, etc.) over extended horizons using only a sparse 0-1 reward. As shown in Figure 4, combining DR3 with COG not only improves over COG, but also learns faster and attains a better average performance.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experimental Evaluation of DR3", "weight": 1.0} -->

Offline RL on D4RL tasks. Finally, we evaluate DR3 in conjunction with CQL on the antmaze-v2 domain in D4RL. To assess if DR3 is stable and able to prevent unlearning that eventually appears in CQL, we trained CQL+DR3 for 9x longer: 2M and 3M steps with 3x higher learning rate. This is different from prior works that report performance at the end of 1M steps. Observe in Table 2, that CQL + DR3 outperforms CQL (statistical significance shown in Appendix A.8), indicating that DR3 significantly improves CQL. We also evalute DR3 on kitchen domains in D4RL in Appendix A.8, where we also find that DR3 improves CQL.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experimental Evaluation of DR3", "weight": 1.0} -->

Finally, we also compare CQL+DR3 and CQL in terms of performance and stability on MuJoCo tasks previously studied in Kumar et al. in Appendix A.3. These tasks are constructed by uniformly subsampling transitions from the full-replay-v2 MuJoCo datasets in D4RL and are much harder than the typical Gym-MuJoCo tasks from Fu et al. because succeeding on these tasks critically relies on estimating accurate Q-values for out-of-sample actions and all actions at certain states are out-of-sample. As shown in Appendix A.3, CQL+DR3 is significantly more stable, and does not unlearn with more training, unlike CQL whose performance degrades very quickly. We also evaluate DR3 in conjunction with BRAC, a policy constraint method, and find that BRAC+DR3 improves over BRAC in 13.8 median normalized performance (Table F.2).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experimental Evaluation of DR3", "weight": 1.0} -->

To summarize, these results indicate that DR3 is a versatile explicit regularizer that improves performance and stability of a wide range of offline RL methods, including conservative methods (e.g, CQL, COG), policy constraint methods (e.g., BRAC) and ensemble-based methods (e.g., REM).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experimental Evaluation of DR3", "weight": 1.0} -->

DR3 does not suffer from rank collapse. Prior work has shown that implicit regularization can lead to a rank collapse issue in TD-learning, preventing Q-networks from using full capacity. To see if DR3 addresses the rank collapse issue, we follow Kumar et al. and plot the effective rank of learned features with DR3 in Figure 5 (DQN, REM in Appendix A.4). While the value of the effective rank decreases during training with naïve bootstrapping, we find that rank of DR3 features typically does not collapse, despite no explicit term encouraging this. Finally, we test the robustness/sensitivity of each layer in the learned Q-network to re-initialization during training and find that DR3 alters the features to behave similarly to supervised learning (Figure A.2).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experimental Evaluation of DR3", "weight": 1.0} -->

Comparing explicit regularizers for different choices of noise covariance $M$. Finally, we investigate the behavior of different implicit regularizers derived via two choices of $M$ in Equation 3.1. ‣ 3.2 Theoretically Characterizing Implicit Regularization in TD-Learning ‣ 3 Implicit Regularization in Deep RL via TD-Learning ‣ DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization") and the corresponding explicit regularizers. While the explicit regularizer we use in practice is a simplifying choice that works well, another choice of $M$ is the covariance matrix induced by label noise, which requires explicit computation of $\Sigma_{M}^{\ast}$. Observe in Figure 6 that the explicit regularizer for our simplifying choice is not worse than the different choice of $M$. This justifies utilizing our simplified, heuristic choice of setting $\Sigma_{M}^{\ast} = I$ in practice. Results on five Atari games are shown in Appendix A.5.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion", "weight": 1.5} -->

We characterized the implicit preference of TD-learning towards solutions that maximally co-adapt gradients (or features) at consecutive state-action tuples that appear in Bellman backup. This regularization effect is exacerbated when out-of-sample state-action samples are used for the Bellman backup and it can lead to poor policy performance. Inspired by the theory, we propose a practical explicit regularizer, DR3 that aims to counteracts this implicit regularizer. DR3 yields substantial improvements in stability and performance on a wide range of offline RL problems. We believe that understanding the learning dynamics of deep Q-learning and the induced implicit regularization will lead to more robust and stable deep RL algorithms. Furthermore, this understanding can help us to predict the instability issues in value-based RL methods in advance, which can inspire cross-validation and model selection strategies, an important, open challenge in offline RL, for which existing off-policy evaluation techniques are not practically sufficient. We also note that our analysis does not consider the online RL setting with non-stationary data distributions, and extending our theory and DR3 to online RL is an interesting avenue for future work.
