<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Forecasting the Past: Gradient-Based Distribution Shift Detection in Trajectory Prediction

Topics include Self-supervised learning, Datasets, Past.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory prediction models often fail in real-world automated driving due to distributional shifts between training and test conditions. Such distributional shifts, whether behavioural or environmental, pose a critical risk by causing the model to make incorrect forecasts in unfamiliar situations. We propose a self-supervised method that trains a decoder in a post-hoc fashion on the self-supervised task of forecasting the second half of observed trajectories from the first half. The L2 norm of the gradient of this forecasting loss with respect to the decoder's final layer defines a score to identify distribution shifts. Our approach, first, does not affect the trajectory prediction model, ensuring no interference with original prediction performance and second, demonstrates substantial improvements on distribution shift detection for trajectory prediction on the Shifts and Argoverse datasets. Moreover, we show that this method can also be used to early detect collisions of a deep Q-Network motion planner in the Highway simulator. Source code is available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Forecasting the movements of surrounding entities is critical for safe automated driving. However, state-of-the-art models often fail in real-world settings due to natural distribution shifts between training and test conditions. These shifts can occur in various forms: spatial, *e.g*., vehicles in unexpected locations, behavioural, *e.g*., erratic movements and traffic violations, and environmental, *e.g*., new weather conditions and unseen road layouts. Degradation in prediction performance creates severe safety risks as models may make overconfident wrong predictions in unfamiliar scenarios, which can lead to catastrophic failures during motion planning. Nevertheless, existing trajectory prediction research has largely focused on improving prediction accuracy, often neglecting crucial aspects of model robustness and reliability.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In trajectory prediction, detecting distribution shifts requires methods that can identify deviations in test data from training distributions, without access to ground truth labels during training. Prior work addresses the problem through three main paradigms: reconstruction-based methods \[chakraborty2023Structural, gao2024multitransmotion, hornauer2023heatmap\] that identify anomalous samples through high reconstruction error, one-class methods \[MAAD2021\] that learn boundaries around normal data, and uncertainty quantification approaches \[wiederer2023joint, marvi2025evidential\] that estimate model confidence using probabilistic estimation. However, these approaches have major limitations. Reconstruction-based methods struggle to distinguish input complexity from true anomalies. One-class methods require careful hyper-parameter tuning for high-dimensional trajectory data \[pmlr-v164-wiederer22a\]. Uncertainty quantification approaches depend on model calibration and often conflate different types of uncertainty \[Rhinehart2020Deep, filos2020can, holle2025uncertainty\].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these issues, we present a post-hoc method for distribution shift detection that operates without degrading the performance of pre-trained trajectory prediction models and hyper-parameter tuning. Our approach leverages the observation that the trajectory prediction loss produces distinct gradients for in-distribution and distribution shifted scenarios. However, as we don't have access of future trajectories at test time to compute this loss, we propose a self-supervised forecasting task, where a decoder predicts the second half of the historical trajectory given the first half. The method computes the L2 norm of the gradient of this self-supervised forecasting loss $\mathcal{L}_{\text{past}}$ with respect to the decoder final layer pre-activations as a score for distribution shift detection. Crucially, the pre-trained encoder remains frozen, ensuring no interference with the original model predictions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our experiments demonstrate substantial improvements: On the Shifts dataset \[malinin2021shifts\], we achieve 71.0% AUROC compared to 56.8% for existing methods, while on Argoverse \[Argoverse\] we consistently exceed 70% AUROC for detecting artificially removed trajectory patterns. Then we deploy our model in the interactive Highway simulator to monitor how our method behaves in an online reinforcement learning. The gradient-based score outperform other self-supervised approaches in detecting collisions one second it happens. The method successfully identifies diverse distribution shifts including environmental changes (new cities, weather conditions), behavioural anomalies (turning patterns, collisions), and velocity-based outliers.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present a post-hoc approach for detecting distribution shifts in pre-trained trajectory prediction models that does not affect performance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a self-supervised trajectory forecasting loss function to extract the gradient norm, which is then employed as an anomaly score at test time.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our experiments demonstrate that our approach can successfully be used for out-of-distribution and anomaly detection in driving environments. On the Shifts Vehicle Motion Prediction dataset \[malinin2021shifts\] we increase the ROC AUC score from 56% to 71%, showcasing the effectiveness of our method. On Argoverse \[Argoverse\], the method achieves AUROC over 70%. On the Highway simulator, the gradient-based score outperforms other self-supervised approaches on collision detection.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Trajectory Prediction", "weight": 1.0} -->

Accurate trajectory prediction is essential for autonomous driving systems, as prediction errors can lead to safety-critical planning failures. To advance performance on the benchmarks \[Caesar_2020_CVPR, Chang_2019_CVPR, wilson2023argoverse2generationdatasets, feng2025UniTraj, Ettinger_2021_ICCV, interactiondataset, agents-llm\], numerous approaches have been proposed, with recent progress driven by agent- and map-aware architectures based on graph neural networks and transformers \[Pazho_2024_CVPR, zhou2022hivt, wagner2024jointmotion, pmlr-v157-chen21a, liu2025dyttptrajectorypredictionnormalizationfree, Aydemir_2023_ICCV\]. For our distribution shift detection, we adopt the graph-based Hierarchical Vector Transformer (HiVT) from \[zhou2022hivt\] and Transformer \[vaswani2017attention\] as the architecture for our experiments, but our proposed method can be applied to any architecture.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Distribution Shift Detection in Trajectory Prediction", "weight": 1.0} -->

Although trajectory prediction models exhibit strong performance on standard benchmarks, they often degrade under distribution shifts. Long term established approaches broadly fall into three paradigms. Uncertainty quantification estimates model confidence, often using ensembles \[lakshminarayanan2017simple\] or Monte Carlo dropout \[malinin2021shifts, gal2016dropout\]. Reconstruction-based methods detect anomalies through high reconstruction error, for example with graph autoencoders \[pmlr-v164-wiederer22a\] or recurrent variational autoencoders \[chakraborty2023Structural\]. Representation-based approaches instead model the normal data distribution in latent space, such as Gaussian mixture models \[wiederer2023joint\] or diffusion models \[li2024difftad, yao2024trajoutofdistribution\]. While these paradigms evaluate the model output or latent space representations, they overlook the gradient magnitudes computed with respect to the network parameters. These gradients naturally distinguish in-distribution from distribution shifted scenarios without altering the pre-trained architecture.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Gradients for Distribution Shift Detection", "weight": 1.0} -->

While most of the literature in distribution shifts detection focuses on loss or feature space, recent works have explored gradient-based distribution shift detection across various domains. Huang et. al. \[huang2021importance\] demonstrate that gradient norms can serve as effective indicators for distribution shift samples in image classification, showing that distribution shift inputs tend to produce larger gradients due to increased model uncertainty. Similarly, \[liang2018enhancing\] propose using the magnitude of gradients computed from the softmax outputs as a confidence measure for detecting misclassified and distribution shift examples. More recently, \[zhang2025gradient\] proposes a gradient based method to address the problem of overconfident prediction of neural network. To the best of our knowledge, we are the first to apply gradient-based distribution shift detection specifically to trajectory prediction. Unlike previous methods that primarily focus on classification tasks, our approach addresses the unique challenges of sequential trajectory data by introducing a self-supervised forecasting task and using gradients from the latent representation space.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Proposed Method", "weight": 1.0} -->

Let $X_{past} = {\{ x_{1},x_{2},\ldots,x_{n}\}}$ be the observed past trajectory of an agent with $x_{i} \in {\mathbb{R}}^{2}$ corresponding to its 2D bird's-eye view coordinates over $n$ time steps, and let $c$ be the surrounding scene context. The primary task is to predict the future trajectory $X_{future} = {\{ x_{n + 1},\ldots,x_{N}\}}$, which is defined as the set of coordinates over $N$ future time steps. To this end, the method assumes access to a pre-trained trajectory prediction model, composed of an encoder $e_{\gamma}$ and decoder $d_{\eta}$. The encoder maps the past trajectory $X_{past}$ and scene context $c$ to the latent representation $z = {e_{\gamma}{(X_{past},c)}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Proposed Method", "weight": 1.0} -->

From this latent vector, the decoder explicitly outputs the parameters of a Gaussian mixture model to predict the multi-modal distribution of future trajectories ${\hat{X}}_{future} = {d_{\eta}{(z)}}$. This distribution is defined as ${\hat{X}}_{future} \sim {\sum_{k = 1}^{K}{\pi_{k}\mathcal{N}_{k}{(\mu_{k},\Sigma_{k})}}}$ where $k$ is the number of mixture components, $\pi_{k}$ defines the component probabilities, and $\mu_{k}$ and $\Sigma_{k}$ are the respective means and variances.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Proposed Method", "weight": 1.0} -->

The objective of our method is to predict a distribution shift score $S$ for the observed traffic scene at test time, relying exclusively on the available inputs $X_{past}$ and $c$. A high score $S$ identifies unfamiliar scenes that deviate from the training distribution. Distributional shifts produce distinct gradient magnitudes within the network parameters. However, extracting gradients requires a loss formulation, and the standard trajectory forecasting loss depends on the unavailable future trajectory $X_{future}$. To extract the gradients at test time, the method introduces a self-supervised proxy task. The gradient of this proxy loss yields the target distribution shift score $S$, which directly serves safety-critical tasks such as anomaly detection and distribution shift filtering.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Forecasting the Past", "weight": 1.0} -->

Models trained on normal data exhibit different gradient magnitudes when processing inputs from a different distribution \[huang2021importance, chen2018gradnorm\]. Since the standard trajectory forecasting loss requires future trajectories $X_{future}$, which are unavailable, we introduce a surrogate task: Forecast the Past, i.e. predict the second half of the past trajectory, given the first half of the trajectory and the scene context. Figure 2 provides an overview of our approach.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Forecasting the Past", "weight": 1.0} -->

We utilize the feature representations from the pre-trained encoder $e_{\gamma}$ for a self-supervised forecasting task on the historical data. First, we partition the historical trajectory $X_{past}$ into two contiguous, equal-length segments: an early history $X_{{past},1} = {\{ x_{1},\ldots,x_{n/2}\}}$ and a later history $X_{{past},2} = {\{ x_{{n/2} + 1},\ldots,x_{n}\}}$ (Figure 3). To conform to the dimensional requirements of the pre-trained model, we resample both segments via linear interpolation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Forecasting the Past", "weight": 1.0} -->

Specifically, $X_{{past},1}$ is upsampled to the encoder's input length $n$, yielding ${\overset{\sim}{X}}_{{past},1}$, while $X_{{past},2}$ is resampled to the model's prediction horizon $N - n$, yielding ${\overset{\sim}{X}}_{{past},2}$. We then introduce a decoder, $d_{past}$, which is trained to predict the resampled later history from the latent representation of the early history, *i.e*. to map $z_{{past},1} = {e_{\gamma}{({\overset{\sim}{X}}_{{past},1})}}$ to ${\overset{\sim}{X}}_{{past},2}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Forecasting the Past", "weight": 1.0} -->

During training, the parameters of the pre-trained encoder $e_{\gamma}$ remain frozen. It processes the resampled early history ${\overset{\sim}{X}}_{{past},1}$ along with contextual information $c$ to produce a latent representation $z_{{past},1} = {e_{\gamma}{({\overset{\sim}{X}}_{{past},1},c)}}$. Similarly to the primary trajectory forecasting decoder $d_{\eta}$, the decoder $d_{past}$ is modelled as a Mixture Density Network.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Forecasting the Past", "weight": 1.0} -->

Next, we explain how to use $d_{past}$ to detect distributional shifts.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Gradient-Based Anomaly Score", "weight": 1.0} -->

Once the past forecasting decoder $d_{past}$ is trained with self-supervision, we can compute meaningful gradients at test time to detect distributional shifts. We define our distribution shift score using the gradient with respect to the pre-activation of the final layer of $d_{past}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Gradient-Based Anomaly Score", "weight": 1.0} -->

Unlike related methods that rely primarily on feature space representations or loss magnitudes \[yao2024trajoutofdistribution, wiederer2023joint, pmlr-v164-wiederer22a, ahmadi2024curb\], this approach extracts the anomaly score from the gradient space. As demonstrated by ElAraby et al. \[elarabygrood\], the gradients capture richer discriminative information than raw feature distances or output confidence scores. By capturing the interaction between the loss landscape and the internal representation of the model (Eq. 3), the gradient encodes how strongly the network hidden representation must be updated to fit a given input. Consequently, anomalous samples induce distinctly larger and more erratic gradient responses compared to stable, in-distribution data. We show empirically in section 4.5 a direct comparison between gradient-based scores and output-based scores for distribution shift detection. Next, we discuss our experiments in more detail.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate our gradient-based distribution shift detection method on two datasets and in the simulator. The datasets benchmark different types of distribution shifts, *i.e*., the first contains environmental distribution shifts (weather, city, time of the day) while the second contains shifts in motion behaviour. In the simulator, we show that our method works in an online environment for monitoring failures of a planning policy.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

The following introduces the datasets and the evaluation protocol.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Datasets", "weight": 1.0} -->

We utilize the Shifts Vehicle Motion Prediction Dataset \[malinin2021shifts\], which is designed to evaluate trajectory prediction under distribution shifts for automated driving. This dataset contains $388\, 406\ a$nd $36\, 804\ s$equences for training and testing, respectively, collected across six locations (Moscow, Skolkovo, Innopolis, Ann Arbor, Modiin, and Tel Aviv), three seasons (Summer, Autumn, Winter), three times of day (Astronomical Night, Daylight, Twilight), and four weather conditions (No precipitation, Rain, Sleet, Snow). The distribution shifts are environmental, where the testing set contains cities that are unseen during training (*i.e*., Ann Arbor and Tel Aviv) and additional precipitation conditions (*i.e*., Rain, Sleet, Snow). Each scene spans 10 seconds, divided into 5 seconds of history and 5 seconds of ground truth future for prediction. Additionally, we adapt the Argoverse 1 motion forecasting dataset \[Argoverse\] for distribution shift detection by artificially creating behavioural out-of-distribution scenarios.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Datasets", "weight": 1.0} -->

Following the taxonomy of Schmidt et al. \[schmidt2022meat\], we remove specific trajectory manoeuvrers from the training set: left turns, right turns, and trajectories exceeding maximum velocity thresholds. We use the removed manoeuvres as the out-of-distribution scenarios during testing. The behaviour clustering methods are described in Sections 4.2.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Evaluation Protocol", "weight": 1.0} -->

For evaluation on Shifts \[malinin2021shifts\] (Figure 4), we compare our method with the baseline provided by the Shifts dataset, *i.e*. the RNN-based behavioral cloning network (RIP-BC) \[codevilla2018end\], the autoregressive flow--based deep imitative model (RIP-DIM) \[Rhinehart2020Deep\] and the latent Gaussian mixture model (lGMM) \[wiederer2023joint\]. To train our model, we take the pre-trained encoder-decoder network from \[wiederer2023joint\], and train our self-supervised decoder on top of the encoder. For the experiments on Argoverse \[Argoverse\], we use the HiVT trajectory prediction model \[zhou2022hivt\] as our encoder-decoder. We train individual HiVT predictors for each training set (turn left, turn right and max velocity) and evaluate their performance on the full Argoverse validation set.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Evaluation Protocol", "weight": 1.0} -->

We compare our approach with several baselines, including one-class support vector machine (OC-SVM), isolation forest (IF) and kernel density estimation (KDE), all of which trained on the latent space $z = {e_{\gamma}{(X_{past})}}$ of HiVT \[zhou2022hivt\].

<!-- chunk {"id": "body-0029", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

Like the prior work \[malinin2021shifts, wiederer2023joint\], we report the area under the receiver operating characteristic curve (AUROC) as the metric for distribution shift detection.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Trajectory Segmentation", "weight": 1.0} -->

For the self supervised task we split the historical trajectory as follows: the first half $X_{{past},1}$ (12 timesteps for Shifts \[malinin2021shifts\] and 10 timesteps for Argoverse \[Argoverse\]) is used to train the self-supervised decoder $d_{past}$ and the second half $X_{{past},2}$ (13 timesteps for Shifts \[malinin2021shifts\] and 10 timesteps for Argoverse \[Argoverse\]) is used as ground truth trajectory. Before feeding the trajectories to the model, we expand $X_{{past},1}$ and $X_{{past},2}$ to the size of original trajectory $X_{past}$ (25 for Shifts and 20 for Argoverse) and $X_{forecast}$ (25 for Shifts and 30 Argoverse) using linear interpolation to keep dimensionality consistency with the original encoder $e_{\gamma}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Trajectory Manoeuvrer Clustering", "weight": 1.0} -->

For the Argoverse evaluation (Table 2) we cluster the trajectory orientation using a computational geometry technique.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Trajectory Manoeuvrer Clustering", "weight": 1.0} -->

where ${\Deltap_{i}} = {P_{i + 1} - P_{i}}$ and ${\Deltap_{i + 1}} = {P_{i + 2} - P_{i + 1}}$. Positive values indicate left turns, negative values indicate right turns, and zero indicates straight motion. The overall trajectory orientation is $\phi_{total} = {\sum_{i = 1}^{N - 2}\phi_{i}}$. For distribution shift detection, we remove trajectories with $\phi_{total} < 1$ from the training set in the experiment "turn_right" and $\phi_{total} > {- 1}$ in the experiment "turn_right". We choose these threshold values to ensure that the model learns a strong directional bias.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Trajectory Velocity Clustering", "weight": 1.0} -->

For the maximum velocity experiment in Argoverse \[Argoverse\], we compute velocity from the trajectory coordinates. The Argoverse dataset samples trajectory points at 10 Hz, providing consecutive positions $P_{i} = {(x_{i},y_{i})}$ and $P_{i + 1} = {(x_{i + 1},y_{i + 1})}$ with time interval ${\Deltat} = 0.1$ seconds.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Trajectory Velocity Clustering", "weight": 1.0} -->

The maximum velocity for a trajectory is $v_{max} = {\max_{i}v_{i}}$. For distribution shift detection, we remove trajectories with $v_{max} > v_{threshold}$ from the training set, where $v_{threshold}$ is set to the median of observed velocities in the training data.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Training and Architecture", "weight": 1.0} -->

For Argoverse \[Argoverse\] and Shifts \[safeshift\], we freeze the encoder trained on the forecasting and we train a decoder with the same architecture and hyper-parameters of the trajectory predictor. For the Highway simulator we train a Transformer \[vaswani2017attention\] encoder and MLP decoder for intersection and merge. We train all the models with Adam optimizer and learning rate ${1e} - 4$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Training and Architecture", "weight": 1.0} -->

(a) Shifts [malinin2021shifts] dataset gradient distributions.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Training and Architecture", "weight": 1.0} -->

Highway simulator gradient distributions.
Figure 7: Kernel density estimation (KDE) [chen2017tutorial] of the last-layer gradients in the Highway environment [highway-env] for the intersection driving task. We observed very distinct gradients between ID on OOD samples, leading to almost perfect collision detection.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Results Analysis", "weight": 1.0} -->

Our experimental results show different patterns in gradient-based distribution shift detection across different datasets.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Shifts Results", "weight": 1.0} -->

Table 1 demonstrates our method's substantial improvement on the Shifts dataset \[malinin2021shifts\], achieving $\sim$`<!-- -->`{=html}71.0% ROC AUC compared to the baseline's 56.8%. This significant performance gain indicates that our gradient-based approach effectively captures environmental distribution shifts such as new cities and weather conditions. As shown in Fig. 9, reconstruction-based methods cannot capture well anomalies, as the reconstruction loss focuses only on the reconstructed trajectory.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Argoverse Results", "weight": 1.0} -->

Table 2 shows strong performance across all behavioral anomaly detection tasks. The method achieves 71.3% and 70.3% AUROC for right and left turn detection, respectively, outperforming KDE (55.2-56.1%), OC-SVM (52.8-56.4%), and Isolation Forest (53.2-61.0%). The performance gap between turn directions is attributed to the skewness of the determinant distribution (Fig. 5(a) ‣ Figure 5 ‣ Trajectory Manoeuvrer Clustering ‣ 4.2 Implementation Details ‣ 4 Experiments ‣ Forecasting the Past: Gradient-Based Distribution Shift Detection in Trajectory Prediction")). For velocity-based anomalies, the method achieves 79.2% AUROC, exceeding the best baseline of 70.8% from KDE.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Gradient Pattern Analysis", "weight": 1.0} -->

On Argoverse, OOD samples often show lower gradient norms than ID samples. We hypothesize from our experiments that this failure is due to training failure convergence, since removing a large portion of trajectories lead to high loss function at the end of the training.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Stability of Results", "weight": 1.0} -->

Across repeated runs, the results on Shifts \[malinin2021shifts\] and Highway remain statistically stable, with consistent ranking and separation between ID and OOD samples. In contrast, Argoverse shows noticeably higher variance and less reliable estimates. We attribute this behavior to unstable training dynamics under the maneuver-filtered setup. The same effect is reflected in the inverted gradient-scale relation on Argoverse, where OOD samples can yield lower gradient norms than ID samples (Fig. 6), which indicates reduced robustness of the score in this setting.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Stability of Results", "weight": 1.0} -->

Last layer Highway [highway-env] Roundabout Inputs
Figure 8: t-SNE visualization of the decoder’s last layer inputs for the Highway [highway-env] Roundabout scenario. Safe (ID) and collision (OOD) trajectories form well-separated clusters, demonstrating the discriminative power of the learned representations.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Early-Detection of Planning Failures", "weight": 1.0} -->

To showcase the practicality of the approach, we evaluate it to identify planning failures in online simulation. We define multiple driving tasks (roundabout, merge, and intersection) in the Highway environment \[highway-env\] and train a reinforcement learning policy using proximal policy optimization (PPO) \[schulman2017proximal\] from Stable Baselines 3 \[stable-baselines3\] for each task. Operating at a control frequency of 5 Hz, the trained PPO policy generates a training dataset comprising 10,000 safe, collision-free episodes. Given this data, we train a predictive model to forecast the past i.e. predict the last 5 time-steps of the trajectory using the Transformer encoder and an MLP decoder architecture, inspired by HiVT \[zhou2022hivt\] and described in Section 4.2.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Early-Detection of Planning Failures", "weight": 1.0} -->

For the evaluation, we deploy the method in an online fashion to monitor the planning policy across a balanced test set of 1,000 safe and 1,000 collision episodes. We compute the distribution shift scores using the last-layer gradient as detailed in Section 3.2. Crucially, in the collision episodes, we capture the score one second before the actual impact occurs, testing the method's ability to provide an early warning. We compare the performance against standard self-supervised autoencoder, masked autoencoder, and IF baselines (Section 4.1) trained on the identical dataset. We omit KDE and OC-SVM baselines due to severe scalability bottlenecks related to kernel estimation during online operation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Detection Results", "weight": 1.0} -->

Table 4, along with Figure 8 and Figure 7, present the method performance in the interactive Highway \[highway-env\] environment across three planning tasks: merge, intersection, and roundabout. Baseline anomaly scoring functions are configured correctly so that higher scores target the collision class, resolving prior inverted AUROC results. The gradient-based method and reconstruction baselines (Autoencoder and Masked Autoencoder) achieve a near-perfect 99.9% AUROC on the merge scenario. This high accuracy occurs because the merge scenario presents distinct, easily separable driving patterns between normal and collision events. However, in more complex environments, the proposed gradient-based score substantially outperforms the baselines. On the intersection task, the gradient-based method achieves 96.1% AUROC, compared to 64.3% for the Autoencoder and 65.5% for the Masked Autoencoder. Similarly, the roundabout scenario yields 95.8% AUROC for the proposed method, exceeding the Autoencoder (85.1%) and Masked Autoencoder (85.8%).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Detection Results", "weight": 1.0} -->

While Isolation Forest also yields competitive results on the merge (99.1%) and roundabout (91.1%) tasks, the gradient-based score consistently surpasses all baselines across evaluated configurations.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Runtime evaluation", "weight": 1.0} -->

Since we are testing in an online simulator, we evaluate the computational cost of our approach. While the PPO policy inference requires $\sim 1$ ms per step, our method computes the anomaly score in $\sim 3$ ms using the Transformer encoder with MLP decoder, and $\sim 4$ ms with the full Transformer encoder-decoder. Although our implementation is unoptimized compared to the established Stable Baselines 3 \[stable-baselines3\] PPO implementation \[schulman2017proximal\], the runtime remains suitable for real-time monitoring. Theoretically, the computational overhead is minimal, as the method primarily involves a forward pass and a single gradient computation with respect to the last layer. Given a 10 Hz operating frequency (100 ms per cycle), this minimal overhead reserves the remaining 96 ms entirely for the upstream perception and localization modules.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Loss Function for Distribution Shift Detection", "weight": 1.0} -->

To prove the validity of our method we tested our Distribution Shift detection method on Shifts \[malinin2021shifts\] using the loss function value $L_{past}$ as score instead of the gradient of the function ${\|{\nabla_{h_{L}}\mathcal{L}_{past}}\|}_{2}$ w.r.t. the last hidden layer input $h_{L}$, as described in Sec. 3.2. As demonstrated in Fig. 9 and Table 3, using the loss function does not provide significant distribution shift information, yielding an AUROC of approximately 50%. In contrast, the gradient-based approach effectively captures variations in the loss landscape and performs significantly better for distribution shift detection. This confirms our hypothesis from Sec. 3.2 showing the superiority of the gradients in terms of Distribution Shifts detection versus the loss space.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Comparison with Other Self-Supervised Approaches", "weight": 1.0} -->

Table 3 compares standard self-supervised methods for distribution shift detection on the Shifts dataset \[malinin2021shifts\]: an Autoencoder (AE) that reconstructs the full trajectory, and a Masked Autoencoder (MAE) that predicts randomly masked trajectory states. Formally, the AE minimizes the mean squared error (MSE) of the full historical trajectory: $\mathcal{L}_{AE} = {(X_{past},{AE{(X_{past})}})}^{2}$. The MAE processes a masked input, ${\overline{X}}_{past} = {M \odot X_{past}}$, where $M$ is a random binary mask, and minimizes $\mathcal{L}_{MAE} = {({{({1 - M})} \odot X_{past}},{MAE{({\overline{X}}_{past})}})}^{2}$. Our method, forecasting the past, applies causal masking by estimating the trajectory's second half.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Comparison with Other Self-Supervised Approaches", "weight": 1.0} -->

For a fair comparison, the masked autoencoder also masks exactly 50% of the trajectory steps. We compute anomaly scores using the loss function magnitude (recon/pred error), and the L2 norm of the loss gradient with respect to all parameters (all), the latent space (latent), and the final layer (last). The results indicate that the loss magnitude poorly identifies distribution shifts, yielding approximately 50% AUROC across all models. Gradient-based scores consistently perform better. Notably, our causal forecasting method combined with the last layer gradient achieves 71.30% AUROC, outperforming reconstruction and random masking methods by over 20%.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented a post-hoc gradient-based method for distribution shift detection in trajectory prediction that does not affect the original model forecasting performance. A self-supervised decoder is trained to forecast the second half of the historical trajectory from the first half, providing a proxy task for computing gradients at test time. The L2 norm of this forecasting loss gradient with respect to the decoder final layer serves as the anomaly score, outperforming both loss-based and reconstruction-based baselines. On the Shifts dataset, the method achieves 71.0% AUROC compared to 56.8% for existing approaches, with consistent improvements on Argoverse and in the interactive Highway simulator for early detection of planning failures. The results establish gradient-based detection as a promising direction for robust trajectory prediction in autonomous driving.
