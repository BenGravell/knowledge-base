The Implicit and Explicit Regularization Effects of Dropout

Dropout is a widely-used regularization technique, often required to obtain state-of-the-art for a number of architectures. This work demonstrates that dropout introduces two distinct but entangled regularization effects: an explicit effect (also studied in prior work) which occurs since dropout modifies the expected training objective, and, perhaps surprisingly, an additional implicit effect from the stochasticity in the dropout training update. This implicit regularization effect is analogous to the effect of stochasticity in small mini-batch stochastic gradient descent. We disentangle these two effects through controlled experiments. We then derive analytic simplifications which characterize each effect in terms of the derivatives of the model and the loss, for deep neural networks. We demonstrate these simplified, analytic regularizers accurately capture the important aspects of dropout, showing they faithfully replace dropout in practice.

## Introduction

Dropout is a commonly used regularization technique for neural nets. In NLP, dropout is the norm on both small and large models, as it is much more effective than methods such as $\ell_{2}$ regularization. In vision, dropout is often used to train extremely large models such as EfficientNet-B7.

At training time, dropout sets a random subset of activations to zero, perturbing the network output with a remarkable amount of noise. Testing is performed on the full model, and it is somewhat mysterious that dropout works so well despite this difference between train and test. The esoteric nature of dropout has inspired a large body of work studying its regularization effects: Wager et al.; Helmbold & Long; Cavazza et al.; Mianjy et al.; Mianjy & Arora study dropout for linear models, matrix factorization, and linearized networks; Arora et al. study deep networks with dropout only at the last layer.

A large body of recent work has studied implicit, or algorithmic regularization in deep learning, defined to be a regularization effect imposed by the training algorithm, not by the objective (see for example and references therein). One notable example of this is in comparing the generalization performance of SGD vs GD: the implicit regularization effect of stochasticity in SGD has been empirically studied in the context of small v.s.

This

## Conclusion

In this work, we show that dropout actually introduces two entangled sources of regularization: an explicit one which modifies the expected objective, and an implicit one due to stochasticity in the updates. We empirically disentangle these regularizers and derive analytic simplifications which faithfully distill each regularization effect. We demonstrate that our simplified regularizers can replace dropout in practice. Our derivations show that dropout regularizes the stability of the model and loss around the training data.

More broadly, our analytic characterizations of dropout can provide intuition on what works and what doesn't for stability-based regularizers in deep learning. We hope that these intuitions can help inform and motivate the design of more principled regularizers for deep networks.
