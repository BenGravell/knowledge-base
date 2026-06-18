DriveGPT: Scaling Autoregressive Behavior Models for Driving

Topics include Autonomous driving, Transformers, Datasets, Planning, DriveGPT.

We present DriveGPT, a scalable behavior model for autonomous driving. We model driving as a sequential decision-making task, and learn a transformer model to predict future agent states as tokens in an autoregressive fashion. We scale up our model parameters and training data by multiple orders of magnitude, enabling us to explore the scaling properties in terms of dataset size, model parameters, and compute. We evaluate DriveGPT across different scales in a planning task, through both quantitative metrics and qualitative examples, including closed-loop driving in complex real-world scenarios. In a separate prediction task, DriveGPT outperforms state-of-the-art baselines and exhibits improved performance by pretraining on a large-scale dataset, further validating the benefits of data scaling.

## Introduction

Transformer-based foundation models have become increasingly prevalent in sequential modeling tasks across various machine learning domains. These models are highly effective in handling sequential data by capturing long-range dependencies and temporal relationships. Their success has been evident in natural language processing (Mann et al. Kaplan et al. Hoffmann et al., ), time-series forecasting, and speech recognition, where sequential patterns play a crucial role.

While scaling up model and dataset sizes has been critical for recent advances in sequential modeling for text prediction (Kaplan et al. Hoffmann et al., ), it remains unclear whether these scaling trends can be directly extended to behavior modeling, particularly in driving tasks, due to several unique challenges. First, driving tasks involve a wider range of input modalities, including agent trajectories and map information, unlike language tasks that rely solely on textual inputs. Second, behavior modeling demands spatial reasoning and an understanding of physical kinematics.

In our work, we present a comprehensive study of scaling up data sizes and model parameters in the context of behavior modeling for autonomous driving, which predicts future actions of traffic agents to support critical tasks such as planning and motion prediction. Specifically, we train a transformer-based autoregressive behavior model on over 100 million high-quality human driving examples, $\sim$`<!-- -->`{=html}50 times more than existing open-source datasets, and scale the model over 1 billion parameters, outsizing existing published behavior models.

We present DriveGPT, a large autoregressive behavior model for driving, by scaling up both model parameters and real-world training data samples.

## Conclusion

We introduced DriveGPT, an LLM-style autoregressive behavior model, to better understand the effects of model parameters and dataset size for autonomous driving. We systematically examined model performance as a function of both dataset size and model capacity, revealing LLM-like scaling laws for data and compute, as well as diminishing returns with increased model size. We showed the quantitative and qualitative benefits of scaling for planning in real-world driving scenarios.
