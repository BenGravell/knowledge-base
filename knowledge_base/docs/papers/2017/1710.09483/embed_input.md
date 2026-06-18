Multimodal Probabilistic Model-Based Planning for Human-Robot Interaction

Topics include Multimodal, Probabilistic, Motion planning, Interaction-aware, Human, Robot, Model-based.

The paper puts together a few cool technologies, such as massively parallel trajectory sampling and evaluation on a GPU, as well as a CVAE neural network trained on actual human driving data for prediction of future driver response at robot inference time.

This paper presents a method for constructing human-robot interaction policies in settings where multimodality, i.e., the possibility of multiple highly distinct futures, plays a critical role in decision making. We are motivated in this work by the example of traffic weaving, e.g., at highway on-ramps/off-ramps, where entering and exiting cars must swap lanes in a short distance - a challenging negotiation even for experienced drivers due to the inherent multimodal uncertainty of who will pass whom. Our approach is to learn multimodal probability distributions over future human actions from a dataset of human-human exemplars and perform real-time robot policy construction in the resulting environment model through massively parallel sampling of human responses to candidate robot action sequences. Direct learning of these distributions is made possible by recent advances in the theory of conditional variational autoencoders (CVAEs), whereby we learn action distributions simultaneously conditioned on the present interaction history, as well as candidate future robot actions in order to take into account response dynamics....

## Introduction

Human behavior is inconsistent across populations, settings, and even different instants, with all other factors equal---addressing this inherent uncertainty is one of the fundamental challenges in human-robot interaction (HRI). Even when a human's broader intent is known, there are often multiple distinct courses of action they may pursue to accomplish their goals. For example, a driver signaling a lane change may throttle up aggressively to pass in front of a blocking car, or brake to allow the adjacent driver to pass first....

Figure 1: Left: Vires VTD driving simulation setup used to gather a dataset of 1105 pairwise human-human traffic weaving interactions (Right: drivers are required to swap lanes before the highway cutoff; who shall pass whom is ambiguous at the start). We use this dataset to learn a generative model of human driver actions, which is in turn used for exhaustive scoring and selection of candidate robot future action sequences. Our policy is validated on the same simulator for pairwise human-robot traffic weaving interactions.

## Conclusions

We have presented a robot policy construction framework for HRI that takes as input a dataset of human-human interaction trials, in order to learn an explicit, sampleable representation of human response behavior, and a cost function defined over a planning horizon, so that the desired robot behavior within the interaction model may be achieved through exhaustive action sequence evaluation applied in an MPC fashion....

In our model, the discrete latent variable $\mathbf{z}$ has the responsibility of representing high-level behavior modes, while a second level of multimodality within each such high-level behavior is facilitated by an autoregressive RNN sequence decoder (light purple cells, Fig. 2). The RNN maintains a hidden state to allow for drawing each future human action conditioned on the actions drawn at previous future times:

where $\gamma \in {\lbrack 0,1\rbrack}$ is a discount factor. Taking $N\rightarrow\infty$ recovers a classical infinite-horizon MDP formulation (although, we note that in this interpretation the state transition distribution is a function of the full state history due to ). In practice we take $N = 15$ (with time interval 0.1s) and iteratively solve, executing only the first action in an MPC fashion....
