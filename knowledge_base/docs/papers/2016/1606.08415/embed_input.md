Gaussian Error Linear Units (GELUs)

Topics include Activation functions, Gaussian error linear units, ReLU alternatives, Exponential linear units, Natural language processing, Computer vision, Speech recognition.

GELU replaces hard ReLU gating with a smooth probability-weighted gate, multiplying x by the standard Gaussian CDF at x. Its later importance comes from becoming a standard transformer activation, but the paper itself frames GELU as a broadly useful smooth alternative evaluated across vision, language, and speech tasks.

We propose the Gaussian Error Linear Unit (GELU), a high-performing neural network activation function. The GELU activation function is xPhi(x), where Phi(x) the standard Gaussian cumulative distribution function. The GELU nonlinearity weights inputs by their value, rather than gates inputs by their sign as in ReLUs (x1_x > 0). We perform an empirical evaluation of the GELU nonlinearity against the ReLU and ELU activations and find performance improvements across all considered computer vision, natural language processing, and speech tasks.

## Introduction

Early artificial neurons utilized binary threshold units. These hard binary decisions are smoothed with sigmoid activations, enabling a neuron to have a "firing rate" interpretation and to train with backpropagation. But as networks became deeper, training with sigmoid activations proved less effective than the non-smooth, less-probabilistic ReLU which makes hard gating decisions based upon an input's sign. Despite having less of a statistical motivation, the ReLU remains a competitive engineering solution which often enables faster and better convergence than sigmoids.

In this work, we introduce a new nonlinearity, the Gaussian Error Linear Unit (GELU). It relates to stochastic regularizers in that it is the expectation of a modification to Adaptive Dropout. This suggests a more probabilistic view of a neuron's output. We find that this novel nonlinearity matches or exceeds models with ReLUs or ELUs across tasks from computer vision, natural language processing, and automatic speech recognition.

## Discussion

Across several experiments, the GELU outperformed previous nonlinearities, but it bears semblance to the ReLU and ELU in other respects. For example, as $\sigma\rightarrow 0$ and if $\mu = 0$, the GELU becomes a ReLU. More, the ReLU and GELU are equal asymptotically. In fact, the GELU can be viewed as a way to smooth a ReLU. To see this, recall that $\text{ReLU} = {\max{(x,0)}} = {x\mathbb{1}{({x > 0})}}$ (where $\mathbb{1}$ is the indicator function), while the GELU is $x\Phi{(x)}$ if ${\mu = 0},{\sigma = 1}$.

However, the GELU has several notable differences. This non-convex, non-monotonic function is not linear in the positive domain and exhibits curvature at all points. Meanwhile ReLUs and ELUs, which are convex and monotonic activations, are linear in the positive domain and thereby can lack curvature. As such, increased curvature and non-monotonicity may allow GELUs to more easily approximate complicated functions than can ReLUs or ELUs.

## Conclusion

For the numerous datasets evaluated in this paper, the GELU exceeded the accuracy of the ELU and ReLU consistently, making it a viable alternative to previous nonlinearities.
