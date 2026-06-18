The Implicit and Explicit Regularization Effects of Dropout

Dropout is a widely-used regularization technique, often required to obtain state-of-the-art for a number of architectures. This work demonstrates that dropout introduces two distinct but entangled regularization effects: an explicit effect (also studied in prior work) which occurs since dropout modifies the expected training objective, and, perhaps surprisingly, an additional implicit effect from the stochasticity in the dropout training update. This implicit regularization effect is analogous to the effect of stochasticity in small mini-batch stochastic gradient descent. We disentangle these two effects through controlled experiments. We then derive analytic simplifications which characterize each effect in terms of the derivatives of the model and the loss, for deep neural networks. We demonstrate these simplified, analytic regularizers accurately capture the important aspects of dropout, showing they faithfully replace dropout in practice.

## Introduction

Dropout is a commonly used regularization technique for neural nets. In NLP, dropout is the norm on both small and large models, as it is much more effective than methods such as $\ell_{2}$ regularization. In vision, dropout is often used to train extremely large models such as EfficientNet-B7.

At training time, dropout sets a random subset of activations to zero, perturbing the network output with a remarkable amount of noise. Testing is performed on the full model, and it is somewhat mysterious that dropout works so well despite this difference between train and test. The esoteric nature of dropout has inspired a large body of work studying its regularization effects: Wager et al.; Helmbold & Long; Cavazza et al.; Mianjy et al.; Mianjy & Arora study dropout for linear models, matrix factorization, and linearized networks; Arora et al. study deep networks with dropout only at the last layer....

In this work, we show that dropout actually introduces two entangled sources of regularization: an explicit one which modifies the expected objective, and an implicit one due to stochasticity in the updates. We empirically disentangle these regularizers and derive analytic simplifications which faithfully distill each regularization effect. We demonstrate that our simplified regularizers can replace dropout in practice. Our derivations show that dropout regularizes the stability of the model and loss around the training data.

More broadly, our analytic characterizations of dropout can provide intuition on what works and what doesn't for stability-based regularizers in deep learning. We hope that these intuitions can help inform and motivate the design of more principled regularizers for deep networks.

Thus, the loss derivatives with respect to model parameters can be expressed in terms of those with respect to the hidden layers.

Our proposed explanation for Figure 1 is that the gradient noise induced by dropout provides an implicit regularization effect. We verify this constructively by adding noise to the $\text{Dropout}_{k}$ updates in order to recover the performance of standard dropout. Let $\xi_{\text{drop}}$ denote the fluctuation of the stochastic dropout gradient around its mean:

Here ${\mu{(W)}},{\nu{(W)}}$ measure the Jacobians and Hessians of the loss and are defined by
