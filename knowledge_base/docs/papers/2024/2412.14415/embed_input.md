DriveGPT: Scaling Autoregressive Behavior Models for Driving

Topics include Autonomous driving, Transformers, Datasets, Planning, DriveGPT.

We present DriveGPT, a scalable behavior model for autonomous driving. We model driving as a sequential decision-making task, and learn a transformer model to predict future agent states as tokens in an autoregressive fashion. We scale up our model parameters and training data by multiple orders of magnitude, enabling us to explore the scaling properties in terms of dataset size, model parameters, and compute. We evaluate DriveGPT across different scales in a planning task, through both quantitative metrics and qualitative examples, including closed-loop driving in complex real-world scenarios. In a separate prediction task, DriveGPT outperforms state-of-the-art baselines and exhibits improved performance by pretraining on a large-scale dataset, further validating the benefits of data scaling.

## Introduction

Transformer-based foundation models have become increasingly prevalent in sequential modeling tasks across various machine learning domains. These models are highly effective in handling sequential data by capturing long-range dependencies and temporal relationships. Their success has been evident in natural language processing (Mann et al. Kaplan et al. Hoffmann et al., ), time-series forecasting, and speech recognition, where sequential patterns play a crucial role....

Figure 1: Through data and model scaling, DriveGPT (red) handles complex real-world driving scenarios, such as lane changing in heavy traffic and yielding to a cyclist in the opposite lane, compared to a smaller baseline trained on less data (pink).

## Conclusion

We introduced DriveGPT, an LLM-style autoregressive behavior model, to better understand the effects of model parameters and dataset size for autonomous driving. We systematically examined model performance as a function of both dataset size and model capacity, revealing LLM-like scaling laws for data and compute, as well as diminishing returns with increased model size. We showed the quantitative and qualitative benefits of scaling for planning in real-world driving scenarios....

Figure 4: Model scaling is more effective as training data increases. The validation loss improves up to ∼100M parameters when trained on the full dataset.

We use a single cross-entropy classification loss over the action space, where the target action is selected as the one that is closest to the ground truth future trajectories. We refer the reader to Appendix A for more training details.

We measure the planning performance on a comprehensive test set through a set of standard geometric metrics including minADE (mADE), minFDE (mFDE), and miss rate (MR). Additionally, we use semantic-based metrics including offroad rate (Offroad) that measures the ratio of trajectories that leave the road and collision rate (Collision) that measures the ratio of trajectories overlapping with traffic agents. We normalize these metrics across experiments to highlight relative performance changes.

Table 1: DriveGPT is ∼3x larger and is trained on ∼50x more data sequences than existing published behavior models.

While scaling up model and dataset sizes has been critical for recent advances in sequential modeling for text prediction (Kaplan et al....
