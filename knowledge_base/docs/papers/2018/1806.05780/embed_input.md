<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Surprising Negative Results for Generative Adversarial Tree Search

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

While many recent advances in deep reinforcement learning (RL) rely on model-free methods, model-based approaches remain an alluring prospect for their potential to exploit unsupervised data to learn environment model. In this work, we provide an extensive study on the design of deep generative models for RL environments and propose a sample efficient and robust method to learn the model of Atari environments. We deploy this model and propose generative adversarial tree search (GATS) a deep RL algorithm that learns the environment model and implements Monte Carlo tree search (MCTS) on the learned model for planning. While MCTS on the learned model is computationally expensive, similar to AlphaGo, GATS follows depth limited MCTS. GATS employs deep Q network (DQN) and learns a Q-function to assign values to the leaves of the tree in MCTS. We theoretical analyze GATS vis-a-vis the bias-variance trade-off and show GATS is able to mitigate the worst-case error in the Q-estimate. While we were expecting GATS to enjoy a better sample complexity and faster converges to better policies, surprisingly, GATS fails to outperform DQN.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide a study on which we show why depth limited MCTS fails to perform desirably.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The earliest and best-publicized applications of deep RL involve Atari games and the board game of Go which are simulated environments and experiences are inexpensive. In such scenarios, model-free deep RL methods have been used to design suitable policies. But these approaches mainly suffer from high sample complexity and are known to be biased, making them less appropriate when the experiences are expensive. To mitigate the effect of the bias, one can deploy MCTS methods to enhance the quality of policies by rolling out on the simulated environment. But this approach, for problems with a long horizon, e.g., Go, becomes computationally expensive. As a remedy, Alpha Go propose to combine model free deep RL methods with model-based MCTS. They employ a depth-limited MCTS on the Go emulator and learn a Q-function to assign values to the leaf nodes. Despite advances in the Go game, this approach still does not fully address the sample complexity issue. Moreover, in real-world applications, such as robotics and dialogue systems, not only collecting experiences takes considerable effort, but also there is no such simulator for these environments.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, generative adversarial networks (GANs) have emerged as a prominent tool for synthesizing realistic-seeming data, especially for high-dimensional domains, e.g., images. Unlike previous approaches to image generation, which typically produced blurry images due to optimizing on L1 or L2 loss, GANs produces crisp images. GANs have been extended to conditional generation, e.g., generating images conditioned on labels or next frames of a video given a context window. Recently, the pix2pix approach propose to use U-Net architecture and has demonstrated impressive results on a range of image-to-image translation tasks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this study, we use Atari games in Arcade Learning Environment (ALE) as our testbed to design sample efficient deep RL algorithms. We propose generative adversarial tree search (GATS), a Deep RL algorithm that learns the model of the environment and performs depth-limited MCTS on the learned model for planning. GATS consists of three main components: 1) generative dynamics model (GDM), a deep generative model that leverages pix2pix GANs and efficiently learns the dynamics of the environments. GDM uses Wasserstein distance as the learning metric and deploys spectral normalization technique to stabilize the training. Condition on a state and a sequence of actions, GDM produces visually crisp successor frames that agree closely with the real frames of games. 2) reward predictor (RP), a classifiers that predict future rewards, clipped rewards of $$ in ALE, 3) a value based deep RL component to assign value to the leaf nodes of the depth limited trees in MCTS, Fig. 9. For this purpose, we use DQN and DDQN, but any other value-based deep RL approach is also suitable.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

GDM: Designing an efficient and robust GDM model for RL task, in particular for Atari games is significantly challenging. The recent studies on GANs are manly dedicated to generating samples from a fixed distribution, while neither fast convergence, fast adaption, nor continual learning is considered. Even in the case of fixed distributions, GANs are known to be unstable and hard to train. RL problems are entirely on the opposite side of the hardness spectra. For RL problems, we need a GDM with a proper model capacity that statistically adapts quickly to the distribution changes due to policy updates and exploration. Followed by the online nature of RL, we require a GDM that computationally converges fast in the presence of changes in the data distribution, e.g. learning a new skill. More importantly, we need a GDM that continually learns the environment dynamics without diverging or becoming unstable, even once, therefore being robust. These are the critical requirements for a useful GDM. Despite the high computation cost of such design study, we thoroughly and extensively study various image translation methods, various GAN-based losses, architectures, in both feed-forward and recurrent neural networks, to design a GDM, suitable for RL tasks.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a result of this study, we propose a GDM architecture and learning procedure that reasonably satisfy all the mentioned requirements. We test the performance of GDM visually, with L1 loss, L2 loss, and also by testing a Q function on generated and real samples.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Theoretical analysis: We analyze the components of error in the estimation of the expected return in GATS, including the bias and variance in the Q-function. We empirical study the error in the Q estimate of DQN/DDQN. Since GATS deploys the Q function in the leaf nodes of the MCTS, we show that the errors in the Q-estimation disappear exponentially fast as the depth of MCTS grows.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Domain change results: In order to thoroughly test the GDM and RP, we developed a new OpenAI gym-like interface for the latest *Arcade Learning Environment (ALE)* that supports different modes and difficulties of Atari games. We documented and open-sourced this package along with the codes for GDM, RP, and GATS. We study the sample complexity of GDM and RP in adapting and transfer from one domain (mode and difficulty in ALE) to another domain. We show that the GDM and RP surprisingly are even robust to mode changes, including some that destroy the DQN policy. They adapt to the new domain with order of thousands samples, while the Q-network requires significantly more, order of millions.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our initial empirical studies are conducted on Pong. The comparably low computation cost of Pong allows an extensive investigation of GATS. We study MCTS with depths at most 5, even for Pong, each run $5M$ time steps requires at least five weeks of GPU time. This is evidence of the massive computational complexity of GATS. We extend our study to four more popular Atari games.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Surprising negative results: Despite learning near-perfect environment model (GDM and RP) that achieves accuracy exceeding our expectations, GATS is unable to outperform its base model-free model DQN/DDQN on any Atari game besides Pong for which we deployed an extra substantial parameter tuning. To boost up GATS, we make an extensive and costly study with many different hyper-parameters and learning strategies, including several that uses the generated frames to train the Q-model, e.g., DynaQ Sutton,. We also develop various exploration strategies, including optimism-based strategy for which We use the errors in the GDM to navigate the exploration. The negative result persisted across all these innovations, and none of our developments helped to provide a modest improvement in GATS performance. Our initial hypothesis was that GATS helps to improve the performance of deep RL methods, but after the extensive empirical study and rigorous test of this hypothesis, we observe that GATS does not pass this test. We put forth a new hypothesis for why GATS, despite the outstanding performance of its components along with the theoretical advantages, might fail in short rollouts.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In fact, we show that GATS locally keeps the agent away from adverse events without letting the agent learn from them, resulting in faulty Q estimation. Holland et al. in fact, observe that it might require to make the depth up to the effective horizon in order to draw an improvement.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

To make our study concrete, we create a new environment, Goldfish and gold bucket. To exclude the effect of model estimation error, we provide GATS with the true model for the MCTS. We show that as long as the depth of the MCTS is not close to the full effective horizon of the game, GATS does not outperform DQN. This study results in a conclusion that combining MCTS with model-free Deep RL, as long as the depth of MCTS is not deep enough, might degrade the performance of RL agents. It is important to note that the theoretical justification does not contradict our conclusion. The theoretical analysis guarantees an improvement in the worse case error in Q estimation, but not in the average performance. It also does not state that following GATS would result in a better Q estimation; in fact, the above argument states that GATS might worsen the Q estimation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consider that all the known successes of MCTS involve tree depth in the hundreds, e.g., $300$ on Atari emulator. Such deep MCTS on GDM requires massive amounts of computation beyond the scale of academic research and the scope of this paper. Considering the broader enthusiasm for both model-based RL and GANs, we believe that this study, despite its failure to advance the leaderboard of deep RL, illuminates several important considerations for future work in combining model-based and model-free reinforcement learning.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Structure: This paper consists of a long study on GATS and concludes with a set of negative results. We dedicate the main body of this paper to present GATS and its components. We leave the detail of these our developments to the supplementary section and instead devote the rest to explain the negative results. We hope that the readers find this structure succinct, useful, and beneficial.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Generative Adversarial Tree Search", "weight": 1.0} -->

Bias-Variance Trade-Off: Consider an MDP $M=\langle\mathcal{X},\mathcal{A},T,R,\gamma\rangle$, with state space $\mathcal{X}$, action space $\mathcal{A}$, transition kernel $T$, reward distribution $R$ with $$-bounded mean, and discount factor $0\leq\gamma<1$. A policy $\pi$ is a mapping from state to action and $Q_{\pi}(x,a)$ denotes the expected return of action $a$ at state $x$, then following policy $\pi$. Following the Bellman equation, the agent can learn the Q function by minimizing the following loss over samples to improve its behavior: Since in RL we do not have access internal expectation, we instead minimize the Bellman residual which has been extensively used in DRL literature: This is the sum of Eq. 1 and an additional variance term, rustling in a biased estimation of Q function.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Generative Adversarial Tree Search", "weight": 1.0} -->

DQN deploys a target network to slightly mitigate this bias and minimizes: In addition to this bias, there are statistical biases due to limited network capacity, optimization, model mismatch, and max operator or the choice of $a^{\prime}$. Let $\widehat{\cdot}$ denote an estimate of a given quantity. Define the estimation error in Q function (bias+variance), the reward estimation $\widehat{r}$ by RP, and transition estimation $\widehat{T}$ by GDM as follows: $\forall x,{x}^{\prime},a\in\mathcal{X},\mathcal{A}$ For a rollout policy $\pi_{r}$, we compute the expected return using GDM, RP and $\widehat{Q}$ as follows: The agent can compute $\xi_{p}(\pi_{r},x)$ with no interaction with the environment.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experiments", "weight": 1.0} -->

We study the performance of GATS with depth of at most five on five Atari games; Pong, Asterix, Breakout, Crazy Climber and Freeway. For the GDM architecture, Fig. 11, we build upon the U-Net model of the image-to-image generator originally used in pix2pix. The GDM receives a state, sequence of actions, and a Gaussian noise vector and generates the next states.^11^ 1 See the Appendix for the detailed explanation on the architecture and optimization procedure. The RP is a simple model with 3 outputs, it receives the current state, action, and the successor state as an input and outputs a label, one for each possible clipped reward $\{-1,0,1\}$. We train GDM and RP using prioritized weighted mini-batches of size 128 (more weight on recent samples), and update the two networks every 16 decision steps (4 times less frequently than the Q update).^22^ 2 For the short lookhead in deterministic environment, we expand the whole tree.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our experiments show that with less than $100k$ samples the GDM learns the environment's dynamics and generalizes well to a test set (DQN requires around $5M$. We also observe that it adapts quickly even if we change the policy or the difficulty or the mode of the domain. Designing GDM model is critical and hard since we need a model which learns fast, does not diverge, is robust, and adapts fast. GAN models are known to diverge even in iid sample setting. It become more challenging, when the GDM is condition on past frames as well as future actions, and needs to predict future given its out generated samples. In order to develop our GDM, we experimented many different model architectures for the generator-discriminator, as well as different loss functions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experiments", "weight": 1.0} -->

Since the L1 and L2 losses are not good metrics for image generating models, we evaluated the performance of GDM visually also by applying Q function on generated test sample, Appendix. E.1, Fig. 12. We studied PatchGAN discriminator (patch sizes 1, 16, and 70) and $L1$ loss used in pix2pix, finding that this architecture takes approximately $10\times$ more training iterations to learn game dynamics for Pong than the current GDM. This is likely since learning the game dynamics such as ball position requires the entire frame for the discriminator, more than the patch-based texture loss given by PatchGAN. Previous works propose ACVP and train large models with L2 loss to predict long future trajectories of frames given actions. We empirically studied these methods. While GDM is much smaller, we observe that it requires significantly fewer iterations to converge to perceptually unidentifiable frames. We also observed significantly lower error for GDM when a Q function is applied to generated frames from both models. ACVP also struggles to produce meaningful frames in stochastic environments(Appendix E.2).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experiments", "weight": 1.0} -->

For the choice of the GAN loss, we first tried the original GAN-loss, which is based on Jensen--Shannon divergence. With this criterion, not only it is difficult to find the right parameters but also not stable enough for non-stationary domains. We did the experiments using this loss and trained for Pong while the resulting model was not stable enough for RL tasks. The training loss is sometimes unstable even for a given fixed data set. Since, Wasserstein metric provides Wasserstein distance criterion and propose a more general loss in GANs, we deployed W-GAN for our GDM. Because W-GAN requires the discriminator to be a bounded Lipschitz function, the authors adopt gradient clipping. Using W-GAN results in an improvement but still not sufficient for RL where fast and stable convergence is required.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experiments", "weight": 1.0} -->

In order to improve the learning stability, parameter robustness, and quality of frames, we also tried a follow-up work on improved-W-GAN, which adds a gradient penalty into the loss of discriminator in order to satisfy the bounded Lipschitzness. Even though it made the GDM more stable than before, it was still not sufficient due to the huge instability in the loss curve. Finally, we tried spectral normalization, a recent technique that not only provides high-quality frames but also converges quickly while the loss function stays smooth. We observed that this model, is stability, robustness to hyperparameter choices, and fast learning thank to spectral normalization combined with W-GAN in the presence of L1 and L2 losses. We deploy this approach in GDM. For the training, we trained GDM to predict the next frame and generate future frames given its own generated frames. We also trained it to predict multiple future frames. Moreover, we studied both feed-forward and recurrent version of it. Furthermore, we used both one step loss and multi-step loss.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

After these study, we observed that the feed-forward model which predicts the next state and trained on the loss of the next three frames generalizes to longer rollout and unseen data. More detailed study is left to Appendix. It is worth noting that the code to all these studies are publicly available (Appendix E).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

Fig. 3 shows the effectiveness of GDM and how accurate it can generate next $9$ frames just conditioning on the previous $4$ frames and a sequnce of actions. We train GDM using 100,000 frames and a 3-step loss, and evaluate its performance on 8-step roll-outs on unseen 10,000 frames. Moreover, we illustrate the tree constructed by MCTS in Figs. 13, 14. We also test a learned Q function on both generated and real frames and observed that the relative deviation is significantly small $(\mathcal{O}(10^{-2}))$. Furthermore, we constructed the tree in MCTS As deep RL methods are data hungry, we can re-use the data generated by GDM to train the Q-function even more. We also study ways we can incorporate the generated samples by GDM-RP to train the Q-function, similar to Dyna-Q Fig. 4.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Shift in Domain", "weight": 1.0} -->

We extend our study to the case where we change the game mode. In this case, change Pong game mode, the opponent paddle gets halved in size, resulting in much easier game. While we expect a trained DDQN agent to perform well on this easier game, surprisingly we observe that not only the agent breaks, but also it provides a score of -21, the most negative score possible. While mastering Pong takes $5M$ step from DDQN, we expected a short fine tuning would be enough for DDQN to adapt to this new domain. Again surprisingly, we observe that it take 5M times to step for this agent to adapt to this new domain. It means that DDQN clearly overfit to the original domain. While DDQN appears unacceptably brittle in this scenario, GDM and RP adapt to the new model dynamics in less than 3k samples, which is significantly smaller (Appendix E.1). As stated before, for this study, we wrote a Gym-style wrapper for the new version of ALE which supports different modes of difficulty levels. This package is publicly available.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our initial hypothesis was that GATS enhances model-free approaches. With that regard, we extensively studied GATS to provide an improvement. But, after more than a year of unsuccessful efforts by multiple researchers in pushing for improvement, we reevaluated GATS from the first principles and realized that this approach, despite near-perfect modeling, surprisingly might not even be capable of offering any improvement. We believe this negative result would help to shape the future study of model-based and model-free RL. In the following, we describe our efforts and conclude with our final hypothesis on the negative result, Table 1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Discussion", "weight": 1.5} -->

(i) Plain DQN (ii) Dyna-Q (i) Learning rate (ii) Mini-batch size (i) Leaf nodes (ii) Random samples from the tree (iii) Samples by following greedy Q (iv) Samples by following ε-greedy Q (v) Geometric distribution (i)W-loss (ii) exp(W-loss) (iii) L1+L2+W-distance (iv) exp(L1+L2+W-distance) Table 1: Set of approaches explored to improve GATS performance Replay Buffer: The agent's decision under GATS sometimes differs from the decision of the model-free component. To learn a reasonable Q-function, the Q-leaner needs to observe the outcome of its own decision. To address this problem, we tried storing the samples generated in the tree search and use them to further train the Q-model. We studied two scenarios: (i) using plain DQN with no generated samples and (ii) using Dyna-Q approach and train the Q function also on the generated samples in MCTS. However, these techniques did not improve the performance of GATS.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Discussion", "weight": 1.5} -->

Optimizer: Since GATS, specially in the presence of Dyna-Q is different approach from DQN, we deploy a further hyper parameter tuning on learning rate and mini-batch size.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Discussion", "weight": 1.5} -->

Sampling strategy: We considered a variety ways to exploit the samples generated in tree search for further learning the Q. (i) Since we use the Q-function at the leaf nodes, we further train the Q-function on generated experience at the leaf nodes. (ii) We randomly sampled generated experience in the tree to further learn the Q. (iii) We choose the generated experience following the greedy action of the Q-learner on the tree, the trajectory that we would have received by following the greedy decision of Q (counterfactual branch). We hypothesized that training the Q-function on its own decisions results in an improvement. (iv) We also considered training on the result of $\varepsilon$-greedy policy instead of the greedy. (v) Finally, since deeper in the tree has experiences with bigger shift the policy, we tried a variety of different geometric distributions to give more weight of sampling to the later part of the tree to see which one was most helpful.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Discussion", "weight": 1.5} -->

Optimism: We observed that parts of the state-action space that are novel to the GDM are often explored less and result in higher discriminator errors. We added (i) the $W$-loss and also (ii) its exponent as a notion of external reward to encourage exploration/exploitation. In (iii) and (iv) We did the same with the summation of different losses, e.g., L1, L2.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Discussion", "weight": 1.5} -->

Despite this extensive and costly study on GATS, we were not able to show that GATS, Fig. 1 benefits besides a limited improvement on Pong (Appendix C,D).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Hypothesis on negative results", "weight": 1.0} -->

In the following we reason why GATS with short depth might not boost the performance even with perfect modeling with GDM and RP, despite reducing local bias. Consider a toy example described in Fig. 2(a) where a fish starts with an initialization of the Q function such that the greedy action is represented in yellow arrows. We give the true model to GATS (no modeling error). If the fish follows DQN, it reaches the sharks quickly and receives a negative reward, update the Q function and learns the down action is not a good action. Now consider the depth 2 GATS with the same Q-function initialization. When the agent reaches the step above the sharks, the MCTS roll-out informs the agent that there is a negative reward of going down and the agent chooses action right, following the GATS action (red arrows). The agent keeps following the red arrows until it dies following $\varepsilon$-greedy. GATS locally avoid bad states, but does this information globally get propagated? Consider that this negative reward happens much later in the trajectory than for a DQN agent.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Hypothesis on negative results", "weight": 1.0} -->

Therefore, many more updates are required for the agent to learn that action down is not a good action while this negative signal may even vanish due to the long update lengths. This shows how GATS roll-outs can locally help to avoid (or reach) catastrophic (or good) events, but slow down global understanding.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Hypothesis on negative results", "weight": 1.0} -->

As we suggested in our negative results, this problem can be solved by also putting the generated experiences in the replay buffer following Dyna-Q. Fig. 2(b) illustrates the situation where the GATS action in the third row before the sharks is "right". Therefore, similar to the previous setting, the agent keeps avoiding the sharks, choosing action right over and over and do not experience the shark negative signal. In this case, two-step roll-outs do not see the sharks, and thus Dyna-Q does not speed up the learning. In practice, especially with limited memory of the replay buffer and limited capacity of the function classes, it can be also difficult to tune Dyna-Q to work well.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Hypothesis on negative results", "weight": 1.0} -->

To empirically test this hypothesis, we implemented the 10x10 version of Goldfish and gold bucket environment where the GATS agent has access to the true model of environment. We tested GATS with depths of 0 (i.e., the plain DQN), 1, 2, 4 and GATS $+$Dyna-Q with the depth of 1 and 2 (even for this simple environment GATS is computationally unpleasantly massive (two weeks of cpu machine for $\textsc{\small{GATS}}-4$)). We use a randomly initialized Q network to learn the Q function. Figure 2(c) represents the per episode return of different algorithms. Each episode has a maximum length of $100$ steps unless the agent either reaches the gold bucket (the reward of $+1$) or hit any of the sharks (the reward of $-1$). Here the discount factor is $0.99$ and cost of living is $0.05$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Hypothesis on negative results", "weight": 1.0} -->

As expected, GATS with the depth of 10 (the dimension of the grid) receives the highest return. We observe that GATS with nonzero depth locally saves the agent and initially result in higher returns than DQN. However, in the long run, GATS with short roll-outs (e.g. GATS-1 and GATS-2) degrade the performance, as seen in the later parts of the runs. Furthermore, we observe that the Dyna-Q approach also fails in improving performance. We train $\textsc{\small{GATS}}{+}$Dyna-Q with both executed experiences and predicted ones. We observe that $\textsc{\small{GATS}}{+}$Dyna-Q does not provide much benefit over GATS. Consider that generated samples in the tree and real samples in $\textsc{\small{GATS}}{+}$Dyna-Q are similar, resulting in repeated experiences in the replay buffer.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Hypothesis on negative results", "weight": 1.0} -->

Concolusion: For many complex applications, like hard Atari games, GATS may require significantly longer roll-out depths with sophisticated Dyna-Q in order to perform well, which is computationally in-feasible for this study. However, the insights in designing near-perfect modeling algorithms and the extensive study of GATS, highlight several key considerations and provide an important framework to effectively design algorithms for combining model-based and model-free reinforcement learning.
