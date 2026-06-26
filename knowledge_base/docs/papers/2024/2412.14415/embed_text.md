## Introduction

Transformer-based foundation models have become increasingly prevalent in sequential modeling tasks across various machine learning domains. These models are highly effective in handling sequential data by capturing long-range dependencies and temporal relationships. Their success has been evident in natural language processing, time-series forecasting, and speech recognition, where sequential patterns play a crucial role. One of the key strengths of transformer-based models is their capacity to learn from large datasets including millions of training examples, enabling them to address complex tasks with increased model sizes, up to billions of model parameters.

Figure 1: Through data and model scaling, DriveGPT (red) handles complex real-world driving scenarios, such as lane changing in heavy traffic and yielding to a cyclist in the opposite lane, compared to a smaller baseline trained on less data (pink).

Table 1: DriveGPT is ∼3x larger and is trained on ∼50x more data sequences than existing published behavior models.

While scaling up model and dataset sizes has been critical for recent advances in sequential modeling for text prediction, it remains unclear whether these scaling trends can be directly extended to behavior modeling, particularly in driving tasks, due to several unique challenges. First, driving tasks involve a wider range of input modalities, including agent trajectories and map information, unlike language tasks that rely solely on textual inputs. Second, behavior modeling demands spatial reasoning and an understanding of physical kinematics. Such capabilities are typically beyond the scope of language models. Finally, the collection of large-scale driving datasets requires substantial effort and resources, making it far more challenging than gathering textual data. As a result, existing work is often constrained by the availability of training data or the scalability of the models, as summarized in Table 1.

In our work, we present a comprehensive study of scaling up data sizes and model parameters in the context of behavior modeling for autonomous driving, which predicts future actions of traffic agents to support critical tasks such as planning and motion prediction. Specifically, we train a transformer-based autoregressive behavior model on over 100 million high-quality human driving examples, $\sim$`<!-- -->`{=html}50 times more than existing open-source datasets, and scale the model over 1 billion parameters, outsizing existing published behavior models.

As we scale up the volume of training data and the number of model parameters, we observe improvements in both quantitative metrics and qualitative behaviors. More importantly, large models trained on extensive, diverse datasets can better handle rare or edge-case scenarios, which often pose significant challenges for autonomous vehicles, as shown in Fig. 1^11^1The baseline model is trained on $\sim$`<!-- -->`{=html}50 times less data and uses $\sim$`<!-- -->`{=html}50 times fewer parameters.. As a result, we see great potential in scaling up behavior models through data and model parameters to improve the safety and robustness of autonomous driving systems.

Figure 2: DriveGPT architecture, including a transformer encoder and a transformer decoder. The transformer encoder summarizes relevant scene context, such as target agent history, nearby agent history, and map information, into a set of scene embedding tokens. The transformer decoder follows an LLM-style architecture that takes a sequence of agent states as input and predicts a discrete distribution of actions at the next tick, conditioned on previous states.

Our main contributions are as follows: We present DriveGPT, a large autoregressive behavior model for driving, by scaling up both model parameters and real-world training data samples.

We determine empirical driving scaling laws for an autoregressive behavior model in terms of data size, model parameters, and compute. We validate the value of scaling up training data and compute, and observe better model scalability as training data increases, consistent with the language scaling literature.

We quantitatively and qualitatively compare models from our scaling experiments to validate their effectiveness in real-world driving scenarios. We present real-world deployment of our model through closed-loop driving in challenging conditions.

We demonstrate the generalizability of our model on the Waymo Open Motion Dataset, which outperforms prior state-of-the-art on the motion prediction task and achieves improved performance through large-scale pretraining.

## Related Work

### Behavior Modeling

Behavior modeling is a critical task in autonomous driving, which covers a broad spectrum of tasks including planning, prediction, and simulation. Taking multimodal inputs including agent history states and map information, behavior models predict the future states of these traffic agents by reasoning about agent dynamics, interactions, human intent, and driving environments.

Among learning-based models, transformers have gained popularity due to their ability to fuse multimodal inputs as encoders and model long-range temporal relationships as decoders. Despite the success of transformers in behavior modeling, existing literature is often restricted by the size of model parameters due to limited training data, which fails to capture the full scaling potential of transformer-based models. In our work, we scale up our transformer models to include billions of parameters, by training on a large-scale dataset including more than 100M driving demonstrations, and validate the scalability of transformer-based models in the context of autonomous driving.

### Large Transformer Models

Large transformers have demonstrated great success in sequential modeling tasks, by scaling up model parameters and data sizes. These scaling laws have pushed the boundary of many sequential modeling tasks including natural language processing, time-series forecasting, and speech recognition.

Recent work has studied the scalability of behavior models in the context of motion prediction, planning, and simulation, yet these studies are either constrained by limited data size (up to a couple of million training examples), or focused on a few orders of magnitude in terms of data and model scaling, limiting the potential to draw statistically significant conclusions over a large scaling range.

In this paper, we study the scaling properties (in terms of data samples, model parameters, and compute) across a much larger range compared to prior work. More specifically, we target an autoregressive decoder architecture that has been proven to be both scalable (as in the LLM literature) and effective in generating accurate trajectories for traffic agents.

Beyond autonomous driving, there is limited relevant literature on building large transformer models for robotic tasks, which share a transformer architecture similar to our work. Robotics models often share different input features and dynamic models, and operate in different environments, making them difficult to apply directly to driving tasks.

## Behavior Model

We use a standard encoder-decoder architecture as our behavior model, as shown in Fig. 2. We use transformer-based models as our encoder and decoder backbones due to their scalability in related sequential modeling tasks.

### Problem Formulation

We model the problem as a sequential prediction task over the future positions of the target agent up to horizon $T$, by applying the chain rule at each step, conditioning on driving context information $\mathbf{c}$ and historical agent positions $\mathbf{s}$: The context information includes target agent history states $c_{\text{target}}$, nearby agent history states $c_{\text{nearby}}$, and map states $c_{\text{map}}$. The historical agent information includes agent positions from previous historical steps, i.e. $s_{0:{t - 1}}$ if we want to predict agent positions at step $t$.

We define "state" as a complete kinematic state including position, orientation, velocity, and acceleration, which is commonly available in agent history observations, and "position" as 2-D (x, y) coordinates to simplify the output space.

### Scene Encoder

The encoder follows a standard transformer encoder architecture that fuses all input modalities into a set of scene embedding tokens. It consumes raw input features, including target agent history states, nearby agent history states, and map states as a set of vectors, and normalizes all inputs to an agent-centric view. Each vector is mapped to a token embedding through a PointNet-like encoder as . At the end of the encoder, we apply a self-attention transformer to fuse all input context into a set of encoder embeddings, $\mathbf{c} \in {\mathbb{R}}^{n \times d}$, where $n$ is the number of vectors and $d$ is the token dimensions, that summarize the driving scene.

### LLM-Style Trajectory Decoder

Inspired by the LLM literature, we follow to use a transformer decoder architecture to predict the distribution of agent positions at each step in the future.

The decoder first tokenizes agent positions at all steps into embeddings with dimension $d$ through a linear layer, followed by a LayerNorm layer and a ReLU layer. At each step $t$, the decoder takes agent embeddings up to $t$, and cross attends them with the encoder embeddings $\mathbf{c}$ to predict the distribution of agent positions at the next step $t + 1$.

The output is a set of discrete actions $a$ represented as the Verlet action, as the second derivative of positions. We can apply the following equation to map Verlet actions to positions: where $a_{t}$ is the predicted Verlet action, and $({s_{t} - s_{t - 1}})$ assumes a constant velocity step. This representation helps predict smooth trajectories using a small set of actions.

### Training

To train a DriveGPT model, we follow teacher forcing by applying ground truth future positions as input to the trajectory decoder. This allows us to predict all future steps in parallel.

We use a single cross-entropy classification loss over the action space, where the target action is selected as the one that is closest to the ground truth future trajectories. We refer the reader to Appendix A for more training details.

### Inference

At inference time, we follow a standard LLM setup and roll out a trajectory over horizon $T$ autoregressively, by repeating the process of predicting the action distribution at the next step, sampling an action, and adding it back to the input sequence.

We sample multiple trajectories in batch to approximate the distribution and then subsample to the desired number of modes using $K$-Means, as .

## Scaling Experiments

The goal of our scaling experiments is to determine the effect of data and model size on behavior prediction performance. Quantifying scaling laws similar to those seen in LLMs can help prioritize the value of data and compute for future research directions in behavior modeling. We focus our effort on exploring the next frontier of data and model size -- over an order of magnitude beyond previously published work.

### Large-scale driving dataset

From millions of miles of high-quality real-world human driving demonstrations, we curate a small subset of 120M segments for an internal research dataset. The dataset is carefully curated and balanced to represent diverse geographic regions across multiple cities and countries, including the United States, Japan, and the UAE. Data collection is evenly distributed between daytime and nighttime and is conducted primarily in urban environments. The dataset captures a wide range of challenging driving scenarios, such as lane changes, intersections, double-parked vehicles, construction zones, and close interactions with pedestrians and cyclists.

We extracted map information, target agent states, and nearby agent states into vectorized representation, as customary in behavior modeling literature.

### Scaling overview

We scale the model size across three orders of magnitude, from 1.5 million to 1.4 billion parameters, by increasing the embedding dimension in both encoder and decoder transformers. For each model size, we explore multiple learning rate schedules using a cosine decay over the full training steps and select the maximum learning rate that yields the best performance. Table. 2 summarizes the optimal learning rate for each model size. Consistent with practices in large language model scaling, each model is trained for a single epoch.

Hidden Dimension (dmodel) Table 2: We vary the model size over three orders of magnitude through hidden dimensions. For each model size, we report the optimal learning rate, which decreases as the model size increases, matching the observations in the LLM scaling literature.

We evaluate model performance using validation loss, computed on a comprehensive validation set of 10 million samples drawn from the same distribution as the training data, with no overlap. This set remains fixed across all scaling experiments to ensure consistency. We use validation loss as a proxy to measure model performance, following standard practices in scaling studies. This loss, calculated as cross-entropy on next-action prediction, serves as our primary performance metric. Additional driving-specific metrics are reported in Sec. 5.1.

### Data Scaling

Figure 3: Performance increases with dataset size across a range of model parameters, indicating that data is a limiting factor. Both axes are on a log scale. An exponential fit was applied to all data points except for the 1.5M curve, resulting in the following relationship: log (L) = −0.102log (D) + 2.663 with an R2 value of 0.986, where L is the validation loss and D is the number of unique training samples.

Data scaling results are summarized in Fig. 3. The smallest dataset of 2.2M samples mimics the size of Waymo Open Motion Dataset (WOMD), a large open-source dataset for behavior modeling ($\sim$`<!-- -->`{=html}44k scenarios with multiple target agents per scenario). We select a few subsets of our internal research dataset to study data scaling across different orders of dataset sizes. Our experiments use $\sim$`<!-- -->`{=html}50x more data than WOMD, exploring a new region of the design space.

The results indicate that as the model is trained on more unique data samples, the performance improves, regardless of model size. Extrapolating from the scaling law in Fig. 3, to improve the best loss by another $10\%$, we would need to include $350$M more training examples. A $20\%$ improvement would require about $1.4$B more examples. As a result, we find that data remains the bottleneck for further improving driving performance.

Lastly, the scaling results remain relatively consistent across model sizes. This consistency indicates that data scaling comparisons can be done on reasonably small model sizes beyond 10M parameters.

### Model Scaling

Figure 4: Model scaling is more effective as training data increases. The validation loss improves up to ∼100M parameters when trained on the full dataset.

We now study model sizes across three orders of magnitude (1.5M to 1.4B parameters), as listed in Table 2. We increase model size by increasing the hidden dimensions of transformers for simplicity. We notice that modifying other parameters such as number of attention heads and hidden dimensions per head does not lead to noticeable changes in the results, as studied in Appendix B.

Training larger models is sensitive to learning rates, as observed in other scaling studies. For each model size, we run multiple experiments at different learning rates to select the one with the optimal performance, as summarized in Table. 2.

Results in Fig. 4 demonstrate that increasing the amount of training data enhances the effectiveness of model scaling. Specifically, when the dataset size is up to 21M, the impact on the validation loss is barely noticeable across a large range of model sizes. Beyond 21M samples, validation losses improve with larger models -- up to 12M parameters when trained on the 42M dataset and up to 94M parameters when trained on the 120M dataset -- before reaching a plateau and eventually overfitting. These findings further reinforce that data is the primary bottleneck for scaling models, aligning with observations in the LLM scaling literature. We leave further exploration of scaling behavior with larger datasets to future work.

Figure 5: Relationship between (smoothed) training loss and FLOPs. Each curve represents an experiment corresponding to a specific model size, and the “min bound” indicates the best performance possible for a given FLOP budget.

Figure 6: Performance as a function of model size for fixed compute budgets. The solid gray line connects the best result from each compute budget.

### Compute Scaling

In Fig. 5, we examine how compute affects training loss, where compute is measured by Floating Point Operations (FLOPs). We identify a monotonically decreasing "min-bound" boundary, which shows the lowest training loss observed up to the current compute value. As we increase compute, training loss generally decreases. Initially, this decrease is quite steep, but it gradually slows down at higher FLOPs values. This trend is consistent with observations in the LLM scaling literature, such as those reported , covering a subset of the full FLOP range explored in these studies.

Next, we investigate whether there is an optimal combination of data size and model parameters for a fixed compute budget. Given the large computational expense for training models at the scales we are exploring, it is important to make the best use of our data. In this study, we fixed the compute budget in different FLOP groups. For a fixed compute budget, we can allocate resources either to model parameters or data samples, keeping their product constant.

Fig. 6 plots the performance with different compute budgets. The trend clearly shows that a larger compute budget leads to better performance, with optimal model size increasing accordingly, as indicated by the "best" gray line. The results further reveal that data is the main bottleneck, as the smallest model outperforms others in the three largest FLOP groups.

### Ablation Study on Decoder Architecture

We scale up two different model architectures by two orders of magnitude: our autoregressive decoder and a one-shot decoder. For the one-shot decoder, we follow to use a transformer decoder that takes a set of learned queries and cross attends them with scene embeddings to produce trajectory samples. This decoder is referred to as "one-shot" because it generates the full trajectory rollout at once, where an autoregressive decoder follows an LLM-style to produce trajectories one step at a time.

The results are summarized in Fig. 7, where we use minFDE at 6 seconds as a proxy to measure the model performance because of different loss definitions between two decoder architectures. Despite worse performance at small-scale parameters, our autoregressive decoder achieves better scalability and outperforms the one-shot baseline beyond 8M parameters. While we find it harder to scale the one-shot decoder, we confirm that our autoregressive decoder scales up to 100M parameters in terms of prediction accuracy, and defer further scalability study on the one-shot decoder as future work.

Figure 7: DriveGPT achieves better scalability in terms of minFDE, by adopting an autoregressive architecture compared to a one-shot architecture.

## Planning and Prediction Experiments

In this section, we show detailed results of DriveGPT in a planning task using our internal research dataset and a motion prediction task using an external dataset. The results here further explore the impact of scaling from Section 4 and help ground those results in driving tasks and metrics.

### Internal Evaluation: AV Planning

For the planning task, we train our model using our internal research dataset, composed of millions of high-quality human driving demonstrations, and generate AV trajectories by autoregressively predicting the next action, as described in Sec. 3.5.

We approximate the distribution by oversampling trajectories in batch and subsampling to 6 trajectories as . While the AV must ultimately select a single trajectory for planning, returning multiple samples helps better understand multimodal behavior and aligns with motion prediction metrics.

We measure the planning performance on a comprehensive test set through a set of standard geometric metrics including minADE (mADE), minFDE (mFDE), and miss rate (MR). Additionally, we use semantic-based metrics including offroad rate (Offroad) that measures the ratio of trajectories that leave the road and collision rate (Collision) that measures the ratio of trajectories overlapping with traffic agents. We normalize these metrics across experiments to highlight relative performance changes. $\hat{\text{mADE}} \downarrow$ $\hat{\text{mFDE}} \downarrow$ $\hat{\text{MR}} \downarrow$ $\hat{\text{Offroad}} \downarrow$ $\hat{\text{Collision}} \downarrow$ Table 3: As we scale up more training data, DriveGPT produces better AV trajectories as measured across all metrics. Metrics are normalized to highlight relative performance.

Figure 8: By training on 50x more data, DriveGPT (red) is able to produce high-quality trajectories in red that keep a safe lateral distance from a jaywalker (top) and go around two double-parked vehicles (bottom).

### Data Scaling Results

We compare a DriveGPT model at 26M parameters trained on datasets of different sizes. The baseline dataset (2.2M) is selected to mimic the size of a typical behavior modeling dataset such as WOMD.

The results are presented in Table 3, where we see that training on more data samples significantly improves the quality of the predicted AV trajectories, in terms of critical semantics metrics in driving including offroad rate and collision rate, as well as geometric metrics. These improvements are consistent with Sec. 4.1.

We further present two qualitative examples in Fig. 8 to illustrate the value of training on more data. In these examples, red trajectories represent DriveGPT trained on 120M samples, and pink trajectories are from the same model trained on 2.2M samples. The examples show that our method produces map-compliant and collision-free trajectories when trained on more data, successfully handling complicated interactions involving a jaywalking pedestrian and two double-parked vehicles.

### Model Scaling Results

$\hat{\text{mADE}} \downarrow$ $\hat{\text{mFDE}} \downarrow$ $\hat{\text{MR}} \downarrow$ $\hat{\text{Offroad}} \downarrow$ $\hat{\text{Collision}} \downarrow$ Table 4: As we scale up more model parameters, all metrics improve up to 94M. Collision rate continues to improve at 163M. Metrics are normalized to highlight relative performance.

Figure 9: By training with 12x more parameters, DriveGPT (red) produces realistic trajectories that obey lane boundaries when performing a right turn into traffic.

We train four models using our 120M internal research dataset, and select the 8M model as the baseline. The baseline represents a reasonable size at which our model starts to outperform one-shot decoders, as shown in Sec. 4.4.

The results are presented in Table 4, where all metrics improve as the model size increases up to 94M parameters, with further gains in the collision metric at 163M parameters (see Sec. D.1 for qualitative examples). Although validation loss shows diminishing returns beyond 94M in Fig. 4, driving metrics continue to improve with increased model capacities, highlighting the potential benefits of introducing more parameters for enhanced driving performance.

We present a qualitative example in Fig. 9, where a larger DriveGPT including 94M parameters produces better trajectory samples in red that stay within the road boundary, compared to a smaller version including 8M parameters, in a right turn scenario.

### Closed-Loop Driving

We demonstrate the effectiveness of DriveGPT as a real-time motion planner deployed in a closed-loop setting. The model takes input features from an industry-level perception system that outputs agent states and map information. We used the 8M DriveGPT model, trained on the full dataset, to drive the car, achieving a latency of under 50ms on a single onboard GPU.

In Fig. 10, we present a challenging example in dense urban traffic where there are two double-parked vehicles blocking the path forward along with other oncoming vehicles. DriveGPT generates smooth and safe trajectories, bypassing the blocking vehicles and moving back to the original lane afterward. More examples are presented in the supplementary video at where DriveGPT alone is responsible for driving in real time.

Figure 10: Example of DriveGPT running as a closed-loop planner in real time in dense urban traffic. It first produces a forward trajectory (top), updates it to bypass double-parked vehicles (middle), and drives back to the original lane at the end (bottom).

### External Evaluation: Motion Prediction

To directly compare with published results, we evaluate DriveGPT on the WOMD motion prediction task. Additionally, we explore the benefits of scale by pretraining on our internal research dataset and finetuning on the significantly smaller WOMD dataset.

Table 5: On the WOMD test set, DriveGPT achieves better results in geometric metrics without any ensembling, and improved performance after pretraining. Results are averaged over three agent types (vehicle, pedestrian, cyclist) and three prediction horizons (3s, 5s, 8s). The best metric is highlighted in bold and the second best is underlined. † denotes ensemble.

Table 6: DriveGPT achieves better geometric metrics across a diverse set of agent types. Results are averaged over 3 prediction horizons.

### Open-Source Encoder

For our external evaluation, we use the open-source MTR encoder. This encoder is similar to the one described in Sec. 3.2. We make this change to improve the reproducibility of our results and take advantage of MTR's open-source dataloading code for WOMD. We use the same autoregressive decoder as described in Sec. 3.3.

### Pretraining Setup

We made a couple of minor modifications to DriveGPT to be compatible with the WOMD dataset. First, we modify our map data to include the same semantics as in WOMD. Second, we modify our agent data to include the same kinematic features for traffic agents as in WOMD.

We pretrain DriveGPT by training on our internal research dataset for one epoch (as in Sec. 4). We load the pretrained checkpoint and finetune the model using the same training setup as in the MTR codebase, where we train the model for 30 epochs using a weighted decay learning rate scheduler.

### Results

We measure model performance via a set of standard WOMD metrics, including minADE, minFDE, miss rate, and soft mAP. Each metric is measured on the test set and computed over three different time horizons.

We present two variants of our method to validate its effectiveness on the motion prediction task, including DriveGPT-WOMD that is trained on WOMD, and DriveGPT-Finetune that is pretrained on our 120M internal research dataset and finetuned on WOMD. For baselines, we use a set of representative state-of-the-art models.

We report results on the WOMD test set^22^2Metrics are sourced from and WOMD leaderboard. in Table 5. The results demonstrate that our method outperforms existing state-of-the-art non-ensemble models in terms of geometric metrics. Compared to Wayformer and MotionLM that use ensembles of up to 8 replicas, our model achieves the best minADE and minFDE metrics and the second-best miss rate metric without any ensembling.

While we prioritize geometric metrics that emphasize the recall of predicted trajectory samples (i.e. not missing the critical trajectory), our model shows lower soft mAP scores due to suboptimal probability estimates. These estimates suffer from accumulated noises over time, as they are computed by compounding the action probabilities over a long sequence (as described in Eq. ), resulting in less accurate sample probabilities and reduced soft mAP, which relies on accurate probability assignments across predicted samples. Consequently, we notice that the gap in soft mAP grows as the prediction horizon increases. This reveals a limitation of using an autoregressive decoder for accurate probability estimation, as also noted in the LLM literature. We defer improving the probability estimates of autoregressive models for behavior modeling as future work. One potential direction is to train an additional probability prediction head for each sample, which could enhance probability estimates and lead to improved soft mAP scores.

We observe up to 3% additional gains by pretraining on our internal dataset, despite a large distribution shift between our internal dataset and the public WOMD dataset, in terms of trajectory distributions, feature noises, and differences in semantic definitions.

Diving deeper into agent-specific results in Table 6, we see consistent improvements across all agent types, compared to MTR that shares the same encoder as ours. This further validates the generalizability of our method, in addition to vehicle behavior modeling results described in Sec. 5.1.

### Qualitative Comparison

We present two qualitative comparisons in Fig. 11, where DriveGPT produces better trajectories in terms of diversity (covering more distinct outcomes) and accuracy (matching with the ground truth future) compared to MTR. This improvement is evident in challenging scenarios with limited agent history information (top row) and multiple future modalities (bottom row).

Figure 11: Compared to MTR (left), DriveGPT (right) produces more accurate and diverse trajectories in complex intersections. Blue represents ground truth future trajectories.

## Conclusion

We introduced DriveGPT, an LLM-style autoregressive behavior model, to better understand the effects of model parameters and dataset size for autonomous driving. We systematically examined model performance as a function of both dataset size and model capacity, revealing LLM-like scaling laws for data and compute, as well as diminishing returns with increased model size. We showed the quantitative and qualitative benefits of scaling for planning in real-world driving scenarios. Additionally, we demonstrated our method on a public motion prediction benchmark, where DriveGPT outperformed state-of-the-art baselines and achieved improved performance through pretraining on a large-scale dataset.
