<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning

Topics include Imitation learning, Online learning, No-regret learning, Structured prediction, Policy learning, DAgger.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces DAgger, reducing imitation learning to no-regret online learning by repeatedly aggregating states visited by the learned policy and querying the expert there. The method directly addresses covariate shift between expert demonstrations and learner rollouts.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sequential prediction problems such as imitation learning, where future observations depend on previous predictions (actions), violate the common i.i.d. assumptions made in statistical learning. This leads to poor performance in theory and often in practice. Some recent approaches provide stronger guarantees in this setting, but remain somewhat unsatisfactory as they train either non-stationary or stochastic policies and require a large number of iterations. In this paper, we propose a new iterative algorithm, which trains a stationary deterministic policy, that can be seen as a no regret algorithm in an online learning setting. We show that any such no regret algorithm, combined with additional reduction assumptions, must find a policy with good performance under the distribution of observations it induces in such sequential settings. We demonstrate that this new approach outperforms previous approaches on two challenging imitation learning problems and a benchmark sequence labeling problem.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Sequence Prediction problems arise commonly in practice. For instance, most robotic systems must be able to predict/make a sequence of actions given a sequence of observations revealed to them over time. In complex robotic systems where standard control methods fail, we must often resort to learning a controller that can make such predictions. Imitation learning techniques, where expert demonstrations of good behavior are used to learn a controller, have proven very useful in practice and have led to state-of-the art performance in a variety of applications. A typical approach to imitation learning is to train a classifier or regressor to predict an expert's behavior given training data of the encountered observations (input) and actions (output) performed by the expert. However since the learner's prediction affects future input observations/states during execution of the learned policy, this violate the crucial i.i.d. assumption made by most statistical learning approaches.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Ignoring this issue leads to poor performance both in theory and practice. In particular, a classifier that makes a mistake with probability $\epsilon$ under the distribution of states/observations encountered by the expert can make as many as $T^{2}\epsilon$ mistakes in expectation over $T$-steps under the distribution of states the classifier itself induces. Intuitively this is because as soon as the learner makes a mistake, it may encounter completely different observations than those under expert demonstration, leading to a compounding of errors.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Recent approaches can guarantee an expected number of mistakes linear (or nearly so) in the task horizon $T$ and error $\epsilon$ by training over several iterations and allowing the learner to influence the input states where expert demonstration is provided (through execution of its own controls in the system). One approach learns a non-stationary policy by training a different policy for each time step in sequence, starting from the first step. Unfortunately this is impractical when $T$ is large or ill-defined. Another approach called SMILe, similar to SEARN and CPI, trains a stationary stochastic policy (a finite mixture of policies) by adding a new policy to the mixture at each iteration of training. However this may be unsatisfactory for practical applications as some policies in the mixture are worse than others and the learned controller may be unstable.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We propose a new meta-algorithm for imitation learning which learns a stationary deterministic policy guaranteed to perform well under its induced distribution of states (number of mistakes/costs that grows linearly in $T$ and classification cost $\epsilon$). We take a reduction-based approach that enables reusing existing supervised learning algorithms. Our approach is simple to implement, has no free parameters except the supervised learning algorithm sub-routine, and requires a number of iterations that scales nearly linearly with the effective horizon of the problem. It naturally handles continuous as well as discrete predictions. Our approach is closely related to no regret online learning algorithms (in particular *Follow-The-Leader*) but better leverages the expert in our setting. Additionally, we show that any no-regret learner can be used in a particular fashion to learn a policy that achieves similar guarantees.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We begin by establishing our notation and setting, discuss related work, and then present the DAgger (Dataset Aggregation) method. We analyze this approach using a no-regret and a reduction approach. Beyond the reduction analysis, we consider the sample complexity of our approach using online-to-batch techniques. We demonstrate DAgger is scalable and outperforms previous approaches in practice on two challenging imitation learning problems: 1) learning to steer a car in a 3D racing game (*Super Tux Kart*) and 2) and learning to play *Super Mario Bros.*, given input image features and corresponding actions by a human expert and near-optimal planner respectively. Following Daumé III et al. in treating structured prediction as a degenerate imitation learning problem, we apply DAgger to the OCR benchmark prediction problem achieving results competitive with the state-of-the-art using only single-pass, greedy prediction.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Supervised Approach to Imitation", "weight": 1.0} -->

The traditional approach to imitation learning ignores the change in distribution and simply trains a policy $\pi$ that performs well under the distribution of states encountered by the expert $d_{\pi^{\ast}}$. This can be achieved using any standard supervised learning algorithm.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Forward Training", "weight": 1.0} -->

The forward training algorithm introduced by Ross and Bagnell trains a non-stationary policy (one policy $\pi_{t}$ for each time step $t$) iteratively over $T$ iterations, where at iteration $t$, $\pi_{t}$ is trained to mimic $\pi^{\ast}$ on the distribution of states at time $t$ induced by the previously trained policies $\pi_{1},\pi_{2},\ldots,\pi_{t - 1}$. By doing so, $\pi_{t}$ is trained on the actual distribution of states it will encounter during execution of the learned policy. Hence the forward algorithm guarantees that the expected loss under the distribution of states induced by the learned policy matches the average loss during training, and hence improves performance.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Forward Training", "weight": 1.0} -->

We here provide a theorem slightly more general than the one provided by Ross and Bagnell that applies to any policy $\pi$ that can guarantee $\epsilon$ surrogate loss under its own distribution of states. This will be useful to bound the performance of our new approach presented in Section 3.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Stochastic Mixing Iterative Learning", "weight": 1.0} -->

SMILe, proposed by Ross and Bagnell, alleviates this problem and can be applied in practice when $T$ is large or undefined by adopting an approach similar to SEARN where a stochastic stationary policy is trained over several iterations. Initially SMILe starts with a policy $\pi_{0}$ which always queries and executes the expert's action choice. At iteration $n$, a policy ${\hat{\pi}}_{n}$ is trained to mimic the expert under the distribution of trajectories $\pi_{n - 1}$ induces and then updates $\pi_{n} = {\pi_{n - 1} + {\alpha{({1 - \alpha})}^{n - 1}{({{\hat{\pi}}_{n} - \pi_{0}})}}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Stochastic Mixing Iterative Learning", "weight": 1.0} -->

This update is interpreted as adding probability $\alpha{({1 - \alpha})}^{n - 1}$ to executing policy ${\hat{\pi}}_{n}$ at any step and removing probability $\alpha{({1 - \alpha})}^{n - 1}$ of executing the queried expert's action. At iteration $n$, $\pi_{n}$ is a mixture of $n$ policies and the probability of using the queried expert's action is ${({1 - \alpha})}^{n}$. We can stop the algorithm at any iteration $N$ by returning the re-normalized policy ${\overset{\sim}{\pi}}_{N} = \frac{\pi_{N} - {{({1 - \alpha})}^{N}\pi_{0}}}{1 - {({1 - \alpha})}^{N}}$ which doesn't query the expert anymore.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Stochastic Mixing Iterative Learning", "weight": 1.0} -->

Ross and Bagnell showed that choosing $\alpha$ in $O{(\frac{1}{T^{2}})}$ and $N$ in $O{({T^{2}{\log T}})}$ guarantees near-linear regret in $T$ and $\epsilon$ for some class of problems.

<!-- chunk {"id": "body-0015", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

We now present DAgger (Dataset Aggregation), an iterative algorithm that trains a deterministic policy that achieves good performance guarantees under its induced distribution of states.

<!-- chunk {"id": "body-0016", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

In its simplest form, the algorithm proceeds as follows. At the first iteration, it uses the expert's policy to gather a dataset of trajectories $\mathcal{D}$ and train a policy ${\hat{\pi}}_{2}$ that best mimics the expert on those trajectories. Then at iteration $n$, it uses ${\hat{\pi}}_{n}$ to collect more trajectories and adds those trajectories to the dataset $\mathcal{D}$. The next policy ${\hat{\pi}}_{n + 1}$ is the policy that best mimics the expert on the whole dataset $\mathcal{D}$. In other words, DAgger proceeds by collecting a dataset at each iteration under the current policy and trains the next policy under the aggregate of all collected datasets. The intuition behind this algorithm is that over the iterations, we are building up the set of inputs that the learned policy is likely to encounter during its execution based on previous experience (training iterations).

<!-- chunk {"id": "body-0017", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

This algorithm can be interpreted as a *Follow-The-Leader* algorithm in that at iteration $n$ we pick the best policy ${\hat{\pi}}_{n + 1}$ in hindsight, i.e. under all trajectories seen so far over the iterations.

<!-- chunk {"id": "body-0018", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

To better leverage the presence of the expert in our imitation learning setting, we optionally allow the algorithm to use a modified policy $\pi_{i} = {{\beta_{i}\pi^{\ast}} + {{({1 - \beta_{i}})}{\hat{\pi}}_{i}}}$ at iteration $i$ that queries the expert to choose controls a fraction of the time while collecting the next dataset. This is often desirable in practice as the first few policies, with relatively few datapoints, may make many more mistakes and visit states that are irrelevant as the policy improves.

<!-- chunk {"id": "body-0019", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

We will typically use $\beta_{1} = 1$ so that we do not have to specify an initial policy ${\hat{\pi}}_{1}$ before getting data from the expert's behavior. Then we could choose $\beta_{i} = p^{i - 1}$ to have a probability of using the expert that decays exponentially as in SMILe and SEARN. We show below the only requirement is that $\{\beta_{i}\}$ be a sequence such that ${\overline{\beta}}_{N} = {\frac{1}{N}{\sum_{i = 1}^{N}\beta_{i}}}\rightarrow 0$ as $N\rightarrow\infty$. The simple, parameter-free version of the algorithm described above is the special case $\beta_{i} = {I{({i = 1})}}$ for $I$ the indicator function, which often performs best in practice (see Section 5). The general DAgger algorithm is detailed in Algorithm 3.1.

<!-- chunk {"id": "body-0020", "role": "body", "section": "DATASET AGGREGATION", "weight": 1.0} -->

Initialize π̂1 to any policy in Π.
Sample T-step trajectories using πi.
Get dataset 𝒟i = {(s,π* (s))} of visited states by πi and actions given by expert.
Return best π̂i on validation.
Algorithm 3.1 DAgger Algorithm.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Finite Sample Results", "weight": 1.0} -->

In the finite sample case, suppose we sample $m$ trajectories with $\pi_{i}$ at each iteration $i$, and denote this dataset $D_{i}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "THEORETICAL ANALYSIS", "weight": 1.0} -->

The theoretical analysis of DAgger only relies on the no-regret property of the underlying *Follow-The-Leader* algorithm on strongly convex losses which picks the sequence of policies ${\hat{\pi}}_{1:N}$. Hence the presented results also hold for *any* other no regret online learning algorithm we would apply to our imitation learning setting. In particular, we can consider the results here a reduction of imitation learning to no-regret online learning where we treat mini-batches of trajectories under a single policy as a single online-learning example. We first briefly review concepts of online learning and no regret that will be used for this analysis.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Online Learning", "weight": 1.0} -->

In online learning, an algorithm must provide a policy $\pi_{n}$ at iteration $n$ which incurs a loss $\ell_{n}{(\pi_{n})}$. After observing this loss, the algorithm can provide a different policy $\pi_{n + 1}$ for the next iteration which will incur loss $\ell_{n + 1}{(\pi_{n + 1})}$. The loss functions $\ell_{n + 1}$ may vary in an unknown or even adversarial fashion over time.

<!-- chunk {"id": "body-0024", "role": "body", "section": "No Regret Algorithms Guarantees", "weight": 1.0} -->

Now we show that no-regret algorithms can be used to find a policy which has good performance guarantees under its own distribution of states in our imitation learning setting. To do so, we must choose the loss functions to be the loss under the distribution of states of the current policy chosen by the online algorithm: ${\ell_{i}{(\pi)}} = {{\mathbb{E}}_{s \sim d_{\pi_{i}}}{\lbrack{\ell{(s,\pi)}}\rbrack}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "No Regret Algorithms Guarantees", "weight": 1.0} -->

For our analysis of DAgger, we need to bound the total variation distance between the distribution of states encountered by ${\hat{\pi}}_{i}$ and $\pi_{i}$, which continues to call the expert.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Finite Sample Case", "weight": 1.0} -->

The previous results hold if the online learning algorithm observes the infinite sample loss, i.e. the loss on the true distribution of trajectories induced by the current policy $\pi_{i}$. In practice however the algorithm would only observe its loss on a small sample of trajectories at each iteration. We wish to bound the true loss under its own distribution of the best policy in the sequence as a function of the regret on the finite sample of trajectories.

<!-- chunk {"id": "body-0027", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

To demonstrate the efficacy and scalability of DAgger, we apply it to two challenging imitation learning problems and a sequence labeling task (handwriting recognition).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Super Tux Kart", "weight": 1.0} -->

Super Tux Kart is a 3D racing game similar to the popular Mario Kart. Our goal is to train the computer to steer the kart moving at fixed speed on a particular race track, based on the current game image features as input (see Figure 1). A human expert is used to provide demonstrations of the correct steering (analog joystick value in ) for each of the observed game images.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Super Tux Kart", "weight": 1.0} -->

For all methods, we use a linear controller as the base learner which updates the steering at 5Hz based on the vector of image features^44^4Features $x$: LAB color values of each pixel in a 25x19 resized image of the 800x600 image; output steering: $\hat{y} = {{w^{T}x} + b}$ where $w$, $b$ minimizes ridge regression objective: ${L{(w,b)}} = {{\frac{1}{n}{\sum_{i = 1}^{n}{({{{w^{T}x_{i}} + b} - y_{i}})}^{2}}} + {\frac{\lambda}{2}w^{T}w}}$, for regularizer $\lambda = 10^{- 3}$..

<!-- chunk {"id": "body-0030", "role": "body", "section": "Super Tux Kart", "weight": 1.0} -->

We compare performance on a race track called Star Track. As this track floats in space, the kart can fall off the track at any point (the kart is repositioned at the center of the track when this occurs). We measure performance in terms of the average number of falls per lap. For SMILe and DAgger, we used 1 lap of training per iteration ($\sim$`<!-- -->`{=html}1000 data points) and run both methods for 20 iterations. For SMILe we choose parameter $\alpha = 0.1$ as in Ross and Bagnell, and for DAgger the parameter $\beta_{i} = {I{({i = 1})}}$ for $I$ the indicator function. Figure 2 shows 95% confidence intervals on the average falls per lap of each method after 1, 5, 10, 15 and 20 iterations as a function of the total number of training data collected.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Super Tux Kart", "weight": 1.0} -->

We first observe that with the baseline supervised approach where training always occurs under the expert's trajectories that performance does not improve as more data is collected. This is because most of the training laps are all very similar and do not help the learner to learn how to recover from mistakes it makes. With SMILe we obtain some improvements but the policy after 20 iterations still falls off the track about twice per lap on average. This is in part due to the stochasticity of the policy which sometimes makes bad choices of actions. For DAgger, we were able to obtain a policy that never falls off the track after 15 iterations of training. Though even after 5 iterations, the policy we obtain almost never falls off the track and is significantly outperforming both SMILe and the baseline supervised approach. Furthermore, the policy obtained by DAgger is smoother and looks qualitatively better than the policy obtained with SMILe. A video available on YouTube shows a qualitative comparison of the behavior obtained with each method.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Super Mario Bros", "weight": 1.0} -->

Super Mario Bros. is a platform video game where the character, Mario, must move across each stage by avoiding being hit by enemies and falling into gaps, and before running out of time. We used the simulator from a recent Mario Bros. AI competition which can randomly generate stages of varying difficulty (more difficult gaps and types of enemies). Our goal is to train the computer to play this game based on the current game image features as input (see Figure 3). Our expert in this scenario is a near-optimal planning algorithm that has full access to the game's internal state and can simulate exactly the consequence of future actions. An action consists of 4 binary variables indicating which subset of buttons we should press in $\{$left,right,jump,speed$\}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Super Mario Bros", "weight": 1.0} -->

For all methods, we use 4 independent linear SVM as the base learner which update the 4 binary actions at 5Hz based on the vector of image features^55^5For the input features $x$: each image is discretized in a grid of 22x22 cells centered around Mario; 14 binary features describe each cell (types of ground, enemies, blocks and other special items); a history of those features over the last 4 images is used, in addition to other features describing the last 6 actions and the state of Mario (small,big,fire,touches ground), for a total of 27152 binary features (very sparse). The $k^{th}$ output binary variable ${\hat{y}}_{k} = {I{({{{w_{k}^{T}x} + b_{k}} > 0})}}$, where $w_{k},b_{k}$ optimizes the SVM objective with regularizer $\lambda = 10^{- 4}$ using stochastic gradient descent..

<!-- chunk {"id": "body-0034", "role": "body", "section": "Super Mario Bros", "weight": 1.0} -->

We compare performance in terms of the average distance travelled by Mario per stage before dying, running out of time or completing the stage, on randomly generated stages of difficulty 1 with a time limit of 60 seconds to complete the stage. The total distance of each stage varies but is around 4200-4300 on average, so performance can vary roughly. Stages of difficulty 1 are fairly easy for an average human player but contain most types of enemies and gaps, except with fewer enemies and gaps than stages of harder difficulties. We compare performance of DAgger, SMILe and SEARN^66^6We use the same cost-to-go approximation in Daumé III et al.; in this case SMILe and SEARN differs only in how the weights in the mixture are updated at each iteration. to the supervised approach (Sup). With each approach we collect 5000 data points per iteration (each stage is about 150 data points if run to completion) and run the methods for 20 iterations. For SMILe we choose parameter $\alpha = 0.1$ (Sm0.1) as in Ross and Bagnell.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Super Mario Bros", "weight": 1.0} -->

For DAgger we obtain results with different choice of the parameter $\beta_{i}$: 1) $\beta_{i} = {I{({i = 1})}}$ for $I$ the indicator function (D0); 2) $\beta_{i} = p^{i - 1}$ for all values of $p \in {\{ 0.1,0.2,\ldots,0.9\}}$. We report the best results obtained with $p = 0.5$ (D0.5). We also report the results with $p = 0.9$ (D0.9) which shows the slower convergence of using the expert more frequently at later iterations. Similarly for SEARN, we obtain results with all choice of $\alpha$ in $\{ 0.1,0.2,\ldots,1\}$. We report the best results obtained with $\alpha = 0.4$ (Se0.4). We also report results with $\alpha = 1.0$ (Se1), which shows the unstability of such a pure policy iteration approach.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Super Mario Bros", "weight": 1.0} -->

Figure 4 shows 95% confidence intervals on the average distance travelled per stage at each iteration as a function of the total number of training data collected.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Super Mario Bros", "weight": 1.0} -->

Again here we observe that with the supervised approach, performance stagnates as we collect more data from the expert demonstrations, as this does not help the particular errors the learned controller makes. In particular, a reason the supervised approach gets such a low score is that under the learned controller, Mario is often stuck at some location against an obstacle instead of jumping over it. Since the expert always jumps over obstacles at a significant distance away, the controller did not learn how to get unstuck in situations where it is right next to an obstacle. On the other hand, all the other iterative methods perform much better as they eventually learn to get unstuck in those situations by encountering them at the later iterations. Again in this experiment, DAgger outperforms SMILe, and also outperforms SEARN for all choice of $\alpha$ we considered. When using $\beta_{i} = 0.9^{i - 1}$, convergence is significantly slower could have benefited from more iterations as performance was still improving at the end of the 20 iterations. Choosing $0.5^{i - 1}$ yields slightly better performance then with the indicator function.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Super Mario Bros", "weight": 1.0} -->

This is potentially due to the large number of data generated where mario is stuck at the same location in the early iterations when using the indicator; whereas using the expert a small fraction of the time still allows to observe those locations but also unstucks mario and makes it collect a wider variety of useful data. A video available on YouTube also shows a qualitative comparison of the behavior obtained with each method.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Handwriting Recognition", "weight": 1.0} -->

Finally, we demonstrate the efficacy of our approach on a structured prediction problem involving recognizing handwritten words given the sequence of images of each character in the word. We follow Daumé III et al. in adopting a view of structured prediction as a degenerate form of imitation learning where the system dynamics are deterministic and trivial in simply passing on earlier predictions made as inputs for future predictions. We use the dataset of Taskar et al. which has been used extensively in the literature to compare several structured prediction approaches. This dataset contains roughly 6600 words (for a total of over 52000 characters) partitioned in 10 folds. We consider the large dataset experiment which consists of training on 9 folds and testing on 1 fold and repeating this over all folds. Performance is measured in terms of the character accuracy on the test folds.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Handwriting Recognition", "weight": 1.0} -->

We consider predicting the word by predicting each character in sequence in a left to right order, using the previously predicted character to help predict the next and a linear SVM^77^7Each character is 8x16 binary pixels (128 input features); 26 binary features are used to encode the previously predicted letter in the word. We train the multiclass SVM using the all-pairs reduction to binary classification., following the greedy SEARN approach in Daumé III et al.. Here we compare our method to SMILe, as well as SEARN (using the same approximations used in Daumé III et al. ). We also compare these approaches to two baseline, a non-structured approach which simply predicts each character independently and the supervised training approach where training is conducted with the previous character always correctly labeled. Again we try all choice of $\alpha \in {\{ 0.1,0.2,\ldots,1\}}$ for SEARN, and report results for $\alpha = 0.1$, $\alpha = 1$ (pure policy iteration) and the best $\alpha = 0.8$, and run all approaches for 20 iterations.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Handwriting Recognition", "weight": 1.0} -->

Figure 5 shows the performance of each approach on the test folds after each iteration as a function of training data.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Handwriting Recognition", "weight": 1.0} -->

The baseline result without structure achieves 82% character accuracy by just using an SVM that predicts each character independently. When adding the previous character feature, but training with always the previous character correctly labeled (supervised approach), performance increases up to 83.6%. Using DAgger increases performance further to 85.5%. Surprisingly, we observe SEARN with $\alpha = 1$, which is a pure policy iteration approach performs very well on this experiment, similarly to the best $\alpha = 0.8$ and DAgger. Because there is only a small part of the input that is influenced by the current policy (the previous predicted character feature) this makes this approach not as unstable as in general reinforcement/imitation learning problems (as we saw in the previous experiment). SEARN and SMILe with small $\alpha = 0.1$ performs similarly but significantly worse than DAgger. Note that we chose the simplest (greedy, one-pass) decoding to illustrate the benefits of the DAGGER approach with respect to existing reductions. Similar techniques can be applied to multi-pass or beam-search decoding leading to results that are competitive with the state-of-the-art.

<!-- chunk {"id": "body-0043", "role": "body", "section": "FUTURE WORK", "weight": 1.5} -->

We show that by batching over iterations of interaction with a system, no-regret methods, including the presented DAgger approach can provide a learning reduction with strong performance guarantees in both imitation learning and structured prediction. In future work, we will consider more sophisticated strategies than simple greedy forward decoding for structured prediction, as well as using base classifiers that rely on Inverse Optimal Control techniques to learn a cost function for a planner to aid prediction in imitation learning. Further we believe techniques similar to those presented, by leveraging a cost-to-go estimate, may provide an understanding of the success of online methods for reinforcement learning and suggest a similar data-aggregation method that can guarantee performance in such settings.
