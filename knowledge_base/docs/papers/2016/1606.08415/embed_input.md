Gaussian Error Linear Units (GELUs)

Topics include Activation functions, Gaussian error linear units, ReLU alternatives, Exponential linear units, Natural language processing, Computer vision, Speech recognition.

GELU replaces hard ReLU gating with a smooth probability-weighted gate, multiplying x by the standard Gaussian CDF at x. Its later importance comes from becoming a standard transformer activation, but the paper itself frames GELU as a broadly useful smooth alternative evaluated across vision, language, and speech tasks.

We propose the Gaussian Error Linear Unit (GELU), a high-performing neural network activation function. The GELU activation function is xPhi(x), where Phi(x) the standard Gaussian cumulative distribution function. The GELU nonlinearity weights inputs by their value, rather than gates inputs by their sign as in ReLUs (x1_x > 0). We perform an empirical evaluation of the GELU nonlinearity against the ReLU and ELU activations and find performance improvements across all considered computer vision, natural language processing, and speech tasks.

## Introduction

Early artificial neurons utilized binary threshold units. These hard binary decisions are smoothed with sigmoid activations, enabling a neuron to have a "firing rate" interpretation and to train with backpropagation. But as networks became deeper, training with sigmoid activations proved less effective than the non-smooth, less-probabilistic ReLU which makes hard gating decisions based upon an input's sign. Despite having less of a statistical motivation, the ReLU remains a competitive engineering solution which often enables faster and better convergence than sigmoids....

Deep nonlinear classifiers can fit their data so well that network designers are often faced with the choice of including stochastic regularizer like adding noise to hidden layers or applying dropout, and this choice remains separate from the activation function. Some stochastic regularizers can make the network behave like an ensemble of networks, a pseudoensemble, and can lead to marked accuracy increases. For example, the stochastic regularizer dropout creates a pseudoensemble by randomly altering some activation decisions through zero multiplication....

## Conclusion

For the numerous datasets evaluated in this paper, the GELU exceeded the accuracy of the ELU and ReLU consistently, making it a viable alternative to previous nonlinearities.

Figure 4: MNIST Autoencoding Results. Each curve is the median of three runs. Left are loss curves for a learning rate of 10−3, and the right figure is for a 10−4 learning rate. Light, thin curves correspond to test set log losses.

## GELU Experiments

Our next challenge is phone recognition with the TIMIT dataset which has recordings of 680 speakers in a noiseless environment. The system is a five-layer, 2048-neuron wide classifier as in with 39 output phone labels and a dropout rate of 0.5 as in. This network takes as input 11 frames and must predict the phone of the center frame using 26 MFCC, energy, and derivative features per frame. We tune over the learning rates $\{ 10^{- 3},10^{- 4},10^{- 5}\}$ and optimize with Adam....

In this work, we introduce a new nonlinearity, the Gaussian Error Linear Unit (GELU). It relates to stochastic regularizers in that it is the expectation of a modification to Adaptive Dropout. This suggests a more probabilistic view of a neuron's output....
