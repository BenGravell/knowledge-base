## Introduction

Figure 1: Left: Train and test error as a function of model size, for of varying width on CIFAR-10 with 15% label noise. Right: Test error, shown for varying train epochs. All models trained using Adam for 4K epochs. The largest model (width 64) corresponds to standard.

The *bias-variance trade-off* is a fundamental concept in classical statistical learning theory (e.g., Hastie et al. ). The idea is that models of higher complexity have lower bias but higher variance. According to this theory, once model complexity passes a certain threshold, models "overfit" with the variance term dominating the test error, and hence from this point onward, increasing model complexity will only *decrease* performance (i.e., increase test error). Hence conventional wisdom in classical statistics is that, once we pass a certain threshold, *"larger models are worse."*

However, modern neural networks exhibit no such phenomenon. Such networks have millions of parameters, more than enough to fit even random labels (Zhang et al. ), and yet they perform much better on many tasks than smaller models. Indeed, conventional wisdom among practitioners is that "larger models are better'' (Krizhevsky et al., Huang et al., Szegedy et al., Radford et al. ). The effect of training time on test performance is also up for debate. In some settings, "early stopping" improves test performance, while in other settings training neural networks to zero training error only improves performance. Finally, if there is one thing both classical statisticians and deep learning practitioners agree on is "more data is always better".

In this paper, we present empirical evidence that both reconcile and challenge some of the above "conventional wisdoms." We show that many deep learning settings have two different regimes. In the *under-parameterized* regime, where the model complexity is small compared to the number of samples, the test error as a function of model complexity follows the U-like behavior predicted by the classical bias/variance tradeoff. However, once model complexity is sufficiently large to *interpolate* i.e., achieve (close to) zero training error, then increasing complexity only *decreases* test error, following the modern intuition of "bigger models are better". Similar behavior was previously observed in Opper, Advani & Saxe, Spigler et al., and Geiger et al.. This phenomenon was first postulated in generality by Belkin et al. who named it "double descent", and demonstrated it for decision trees, random features, and 2-layer neural networks with $\ell_{2}$ loss, on a variety of learning tasks including MNIST and CIFAR-10.

Figure 2: Left: Test error as a function of model size and train epochs. The horizontal line corresponds to model-wise double descent–varying model size while training for as long as possible. The vertical line corresponds to epoch-wise double descent, with test error undergoing double-descent as train time increases. Right Train error of the corresponding models. All models are trained on CIFAR-10 with 15% label noise, data-augmentation, and Adam for up to 4K epochs.

### Main contributions

We show that double descent is a robust phenomenon that occurs in a variety of tasks, architectures, and optimization methods (see Figure 1 and Section 5; our experiments are summarized in Table A). Moreover, we propose a much more general notion of "double descent" that goes beyond varying the number of parameters. We define the *effective model complexity (EMC)* of a training procedure as the maximum number of samples on which it can achieve close to zero training error. The EMC depends not just on the data distribution and the architecture of the classifier but also on the training procedure---and in particular increasing training time will increase the EMC.

We hypothesize that for many natural models and learning algorithms, double descent occurs as a function of the EMC. Indeed we observe "epoch-wise double descent" when we keep the model fixed and increase the training time, with performance following a classical U-like curve in the underfitting stage (when the EMC is smaller than the number of samples) and then improving with training time once the EMC is sufficiently larger than the number of samples (see Figure 2). As a corollary, early stopping only helps in the relatively narrow parameter regime of critically parameterized models.

Figure 3: Test loss (per-token perplexity) as a function of Transformer model size (embedding dimension dm o d e l) on language translation (IWSLT‘14 German-to-English). The curve for 18k samples is generally lower than the one for 4k samples, but also shifted to the right, since fitting 18k samples requires a larger model. Thus, for some models, the performance for 18k samples is worse than for 4k samples.

### Sample non-monotonicity

Finally, our results shed light on test performance as a function of the number of train samples. Since the test error peaks around the point where EMC matches the number of samples (the transition from the under- to over-parameterization), increasing the number of samples has the effect of shifting this peak to the right. While in most settings increasing the number of samples decreases error, this shifting effect can sometimes result in a setting where *more data is worse!* For example, Figure 3 demonstrates cases in which increasing the number of samples by a factor of $4.5$ results in worse test performance.

## Our results

To state our hypothesis more precisely, we define the notion of *effective model complexity*. We define a *training procedure* $\mathcal{T}$ to be any procedure that takes as input a set $S = {\{{(x_{1},y_{1})},\ldots,{(x_{n},y_{n})}\}}$ of labeled training samples and outputs a classifier $\mathcal{T}{(S)}$ mapping data to labels. We define the *effective model complexity* of $\mathcal{T}$ (w.r.t. distribution $\mathcal{D}$) to be the maximum number of samples $n$ on which $\mathcal{T}$ achieves on average $\approx 0$ *training error*.

### Definition 1 (Effective Model Complexity)

The *Effective Model Complexity* (EMC) of a training procedure $\mathcal{T}$, with respect to distribution $\mathcal{D}$ and parameter $\epsilon > 0$, is defined as:

where ${Error}_{S}{(M)}$ is the mean error of model $M$ on train samples $S$.

Our main hypothesis can be informally stated as follows:

### Hypothesis 1 (Generalized Double Descent hypothesis, informal)

For any natural data distribution $\mathcal{D}$, neural-network-based training procedure $\mathcal{T}$, and small $\epsilon > 0$, if we consider the task of predicting labels based on $n$ samples from $\mathcal{D}$ then:

: If ${EMC}_{\mathcal{D},\epsilon}{(\mathcal{T})}$ is sufficiently smaller than $n$, any perturbation of $\mathcal{T}$ that increases its effective complexity will decrease the test error.

: If ${EMC}_{\mathcal{D},\epsilon}{(\mathcal{T})}$ is sufficiently larger than $n$, any perturbation of $\mathcal{T}$ that increases its effective complexity will decrease the test error.

Critically parameterized regime.

: If ${{EMC}_{\mathcal{D},\epsilon}{(\mathcal{T})}} \approx n$, then a perturbation of $\mathcal{T}$ that increases its effective complexity might decrease or increase the test error.

Hypothesis 1 ‣ 2 Our results ‣ Deep Double Descent: Where Bigger Models and More Data Hurt") is informal in several ways. We do not have a principled way to choose the parameter $\epsilon$ (and currently heuristically use $\epsilon = 0.1$). We also are yet to have a formal specification for "sufficiently smaller" and "sufficiently larger". Our experiments suggest that there is a *critical interval* around the *interpolation threshold* when ${{EMC}_{\mathcal{D},\epsilon}{(\mathcal{T})}} = n$: below and above this interval increasing complexity helps performance, while within this interval it may hurt performance. The width of the critical interval depends on both the distribution and the training procedure in ways we do not yet completely understand.

We believe Hypothesis 1 ‣ 2 Our results ‣ Deep Double Descent: Where Bigger Models and More Data Hurt") sheds light on the interaction between optimization algorithms, model size, and test performance and helps reconcile some of the competing intuitions about them. The main result of this paper is an experimental validation of Hypothesis 1 ‣ 2 Our results ‣ Deep Double Descent: Where Bigger Models and More Data Hurt") under a variety of settings, where we considered several natural choices of datasets, architectures, and optimization algorithms, and we changed the "interpolation threshold" by varying the number of model parameters, the length of training, the amount of label noise in the distribution, and the number of train samples.

Model-wise Double Descent. In Section 5, we study the test error of models of increasing size, for a fixed large number of optimization steps. We show that "model-wise double-descent" occurs for various modern datasets (CIFAR-10, CIFAR-100, IWSLT'14 de-en, with varying amounts of label noise), model architectures (CNNs, ResNets, Transformers), optimizers (SGD, Adam), number of train samples, and training procedures (data-augmentation, and regularization). Moreover, the peak in test error systematically occurs at the interpolation threshold. In particular, we demonstrate realistic settings in which *bigger models are worse*.

Epoch-wise Double Descent. In Section 6, we study the test error of a fixed, large architecture over the course of training. We demonstrate, in similar settings as above, a corresponding peak in test performance when models are trained just long enough to reach $\approx 0$ train error. The test error of a large model first decreases (at the beginning of training), then increases (around the critical regime), then decreases once more (at the end of training)---that is, *training longer can correct overfitting.*

Sample-wise Non-monotonicity. In Section 7, we study the test error of a fixed model and training procedure, for varying number of train samples. Consistent with our generalized double-descent hypothesis, we observe distinct test behavior in the "critical regime", when the number of samples is near the maximum that the model can fit. This often manifests as a long plateau region, in which taking significantly more data might not help when training to completion (as is the case for CNNs on CIFAR-10). Moreover, we show settings (Transformers on IWSLT'14 en-de), where this manifests as a peak---and for a fixed architecture and training procedure, *more data actually hurts.*

Remarks on Label Noise. We observe all forms of double descent most strongly in settings with label noise in the train set (as is often the case when collecting train data in the real-world). However, we also show several realistic settings with a test-error peak even without label noise: ResNets (Figure 4(a)) and CNNs (Figure 20) on CIFAR-100; Transformers on IWSLT'14 (Figure 8). Moreover, all our experiments demonstrate distinctly different test behavior in the critical regime--- often manifesting as a "plateau" in the test error in the noiseless case which develops into a peak with added label noise. See Section 8 for further discussion.

## Related work

Model-wise double descent was first proposed as a general phenomenon by Belkin et al.. Similar behavior had been observed in Opper, Advani & Saxe, Spigler et al., and Geiger et al.. Subsequently, there has been a large body of work studying the double descent phenomenon. A growing list of papers that theoretically analyze it in the tractable setting of linear least squares regression includes Belkin et al.; Hastie et al.; Bartlett et al.; Muthukumar et al.; Bibas et al.; Mitra; Mei & Montanari. Moreover, Geiger et al. provide preliminary results for model-wise double descent in convolutional networks trained on CIFAR-10. Our work differs from the above papers in two crucial aspects: First, we extend the idea of double-descent beyond the number of parameters to incorporate the training procedure under a unified notion of "Effective Model Complexity", leading to novel insights like epoch-wise double descent and sample non-monotonicity. The notion that increasing train time corresponds to increasing complexity was also presented in Nakkiran et al.. Second, we provide an extensive and rigorous demonstration of double-descent for modern practices spanning a variety of architectures, datasets optimization procedures. An extended discussion of the related work is provided in Appendix C.

## Experimental Setup

We briefly describe the experimental setup here; full details are in Appendix B ^11^1The raw data from our experiments are available at: [https://gitlab.com/harvard-machine-learning/double-descent/tree/master](https://gitlab.com/harvard-machine-learning/double-descent/tree/master). We consider three families of architectures: ResNets, standard CNNs, and Transformers. ResNets: We parameterize a family of (He et al. ) by scaling the width (number of filters) of convolutional layers. Specifically, we use layer widths $\lbrack k,{2k},{4k},{8k}\rbrack$ for varying $k$. The standard corresponds to $k = 64$. Standard CNNs: We consider a simple family of 5-layer CNNs, with 4 convolutional layers of widths $\lbrack k,{2k},{4k},{8k}\rbrack$ for varying $k$, and a fully-connected layer. For context, the CNN with width $k = 64$, can reach over $90\%$ test accuracy on CIFAR-10 with data-augmentation. Transformers: We consider the 6 layer encoder-decoder from Vaswani et al., as implemented by Ott et al.. We scale the size of the network by modifying the embedding dimension $d_{\text{model}}$, and setting the width of the fully-connected layers proportionally ($d_{\text{ff}} = {4 \cdot d_{\text{model}}}$). For ResNets and CNNs, we train with cross-entropy loss, and the following optimizers: Adam with learning-rate $0.0001$ for 4K epochs; SGD with learning rate $\propto \frac{1}{\sqrt{T}}$ for 500K gradient steps. We train Transformers for 80K gradient steps, with 10% label smoothing and no drop-out.

### Label Noise

In our experiments, label noise of probability $p$ refers to training on a samples which have the correct label with probability $({1 - p})$, and a uniformly random incorrect label otherwise (label noise is sampled only once and not per epoch). Figure 1 plots test error on the noisy distribution, while the remaining figures plot test error with respect to the clean distribution (the two curves are just linear rescaling of one another).

## Model-wise Double Descent

(a) CIFAR-100. There is a peak in test error even with no label noise.

(b) CIFAR-10. There is a “plateau” in test error around the interpolation point with no label noise, which develops into a peak for added label noise.

Figure 4: Model-wise double descent for. Trained on CIFAR-100 and CIFAR-10, with varying label noise. Optimized using Adam with LR 0.0001 for 4K epochs, and data-augmentation.

In this section, we study the test error of models of increasing size, when training to completion (for a fixed large number of optimization steps). We demonstrate model-wise double descent across different architectures, datasets, optimizers, and training procedures. The critical region exhibits distinctly different test behavior around the interpolation point and there is often a peak in test error that becomes more prominent in settings with label noise.

For the experiments in this section (Figures 4, 5, 7, 7, 8), notice that all modifications which increase the interpolation threshold (such as adding label noise, using data augmentation, and increasing the number of train samples) also correspondingly shift the peak in test error towards larger models. Additional plots showing the early-stopping behavior of these models, and additional experiments showing double descent in settings with no label noise (e.g. Figure 19) are in Appendix E.2. We also observed model-wise double descent for adversarial training, with a prominent robust test error peak even in settings without label noise. See Figure 26 in Appendix E.2.

(a) Without data augmentation.

(b) With data augmentation.

Figure 5: Effect of Data Augmentation. 5-layer CNNs on, with and without data-augmentation. Data-augmentation shifts the interpolation threshold to the right, shifting the test error peak accordingly. Optimized using SGD for 500K steps. See Figure 27 for larger models.

Figure 6: SGD vs. Adam. 5-Layer CNNs on CIFAR-10 with no label noise, and no data augmentation. Optimized using SGD for 500K gradient steps, and Adam for 4K epochs.

Figure 7: Noiseless settings. 5-layer CNNs on CIFAR-100 with no label noise; note the peak in test error. Trained with SGD and no data augmentation. See Figure 20 for the early-stopping behavior of these models.

Figure 8: Transformers on language translation tasks: Multi-head-attention encoder-decoder Transformer model trained for 80k gradient steps with labeled smoothed cross-entropy loss on IWSLT‘14 German-to-English (160K sentences) and WMT‘14 English-to-French (subsampled to 200K sentences) dataset. Test loss is measured as per-token perplexity.

### Discussion

Fully understanding the mechanisms behind model-wise double descent in deep neural networks remains an important open question. However, an analog of model-wise double descent occurs even for linear models. A recent stream of theoretical works analyzes this setting (Bartlett et al.; Muthukumar et al.; Belkin et al.; Mei & Montanari; Hastie et al. ). We believe similar mechanisms may be at work in deep neural networks.

Informally, our intuition is that for model-sizes at the interpolation threshold, there is effectively only one model that fits the train data and this interpolating model is very sensitive to noise in the train set and/or model mis-specification. That is, since the model is just barely able to fit the train data, forcing it to fit even slightly-noisy or mis-specified labels will destroy its global structure, and result in high test error. (See Figure 28 in the Appendix for an experiment demonstrating this noise sensitivity, by showing that ensembling helps significantly in the critically-parameterized regime). However for over-parameterized models, there are many interpolating models that fit the train set, and SGD is able to find one that "memorizes" (or "absorbs") the noise while still performing well on the distribution.

The above intuition is theoretically justified for linear models. In general, this situation manifests even without label noise for linear models (Mei & Montanari ), and occurs whenever there is *model mis-specification* between the structure of the true distribution and the model family. We believe this intuition extends to deep learning as well, and it is consistent with our experiments.

## Epoch-wise Double Descent

In this section, we demonstrate a novel form of double-descent with respect to training epochs, which is consistent with our unified view of effective model complexity (EMC) and the generalized double descent hypothesis. Increasing the train time increases the EMC---and thus a sufficiently large model transitions from under- to over-parameterized over the course of training.

Figure 9: Left: Training dynamics for models in three regimes. Models are on with 20% label noise, trained using Adam with learning rate 0.0001, and data augmentation. Right: Test error over (Model size × Epochs). Three slices of this plot are shown on the left.

As illustrated in Figure 9, sufficiently large models can undergo a "double descent" behavior where test error first decreases then increases near the interpolation threshold, and then decreases again. In contrast, for "medium sized" models, for which training to completion will only barely reach $\approx 0$ error, the test error as a function of training time will follow a classical U-like curve where it is better to stop early. Models that are too small to reach the approximation threshold will remain in the "under parameterized" regime where increasing train time monotonically decreases test error. Our experiments (Figure 10) show that many settings of dataset and architecture exhibit epoch-wise double descent, in the presence of label noise. Further, this phenomenon is robust across optimizer variations and learning rate schedules (see additional experiments in Appendix E.1). As in model-wise double descent, the test error peak is accentuated with label noise.

(c) 5-layer CNN on CIFAR 10.

Figure 10: Epoch-wise double descent for and CNN (width=128). ResNets trained using Adam with learning rate 0.0001, and CNNs trained with SGD with inverse-squareroot learning rate.

Conventional wisdom suggests that training is split into two phases: In the first phase, the network learns a function with a small generalization gap In the second phase, the network starts to over-fit the data leading to an increase in test error. Our experiments suggest that this is not the complete picture---in some regimes, the test error decreases again and may achieve a lower value at the end of training as compared to the first minimum (see Fig 10 for 10% label noise).

## Sample-wise Non-monotonicity

In this section, we investigate the effect of varying the number of train samples, for a fixed model and training procedure. Previously, in model-wise and epoch-wise double descent, we explored behavior in the critical regime, where ${{EMC}_{\mathcal{D},\epsilon}{(\mathcal{T})}} \approx n$, by varying the EMC. Here, we explore the critical regime by varying the number of train samples $n$. By increasing $n$, the same training procedure $\mathcal{T}$ can switch from being effectively over-parameterized to effectively under-parameterized.

We show that increasing the number of samples has two different effects on the test error vs. model complexity graph. On the one hand, (as expected) increasing the number of samples shrinks the area under the curve. On the other hand, increasing the number of samples also has the effect of "shifting the curve to the right" and increasing the model complexity at which test error peaks.

(a) Model-wise double descent for 5-layer CNNs on CIFAR-10, for varying dataset sizes. Top: There is a range of model sizes (shaded green) where training on 2× more samples does not improve test error. Bottom: There is a range of model sizes (shaded red) where training on 4× more samples does not improve test error.

(b) Sample-wise non-monotonicity. Test loss (per-word perplexity) as a function of number of train samples, for two transformer models trained to completion on IWSLT’14. For both model sizes, there is a regime where more samples hurt performance. Compare to Figure 3, of model-wise double-descent in the identical setting.

Figure 11: Sample-wise non-monotonicity.

These twin effects are shown in Figure 11(a). Note that there is a range of model sizes where the effects "cancel out"---and having $4 \times$ more train samples does not help test performance when training to completion. Outside the critically-parameterized regime, for sufficiently under- or over-parameterized models, having more samples helps. This phenomenon is corroborated in Figure 12, which shows test error as a function of both model and sample size, in the same setting as Figure 11(a).

Figure 12: Left: Test Error as a function of model size and number of train samples, for 5-layer CNNs on CIFAR-10 + 20% noise. Note the ridge of high test error again lies along the interpolation threshold. Right: Three slices of the left plot, showing the effect of more data for models of different sizes. Note that, when training to completion, more data helps for small and large models, but does not help for near-critically-parameterized models (green).

In some settings, these two effects combine to yield a regime of model sizes where more data actually hurts test performance as in Figure 3 (see also Figure 11(b)). Note that this phenomenon is not unique to DNNs: more data can hurt even for linear models (see Appendix D).

## Conclusion and Discussion

We introduce a generalized double descent hypothesis: models and training procedures exhibit atypical behavior when their Effective Model Complexity is comparable to the number of train samples. We provide extensive evidence for our hypothesis in modern deep learning settings, and show that it is robust to choices of dataset, architecture, and training procedures. In particular, we demonstrate "model-wise double descent" for modern deep networks and characterize the regime where bigger models can perform worse. We also demonstrate "epoch-wise double descent," which, to the best of our knowledge, has not been previously proposed. Finally, we show that the double descent phenomenon can lead to a regime where training on more data leads to worse test performance. Preliminary results suggest that double descent also holds as we vary the amount of regularization for a fixed model (see Figure 22).

We also believe our characterization of the critical regime provides a useful way of thinking for practitioners---if a model and training procedure are just barely able to fit the train set, then small changes to the model or training procedure may yield unexpected behavior (e.g. making the model slightly larger or smaller, changing regularization, etc. may hurt test performance).

### Early stopping

We note that many of the phenomena that we highlight often do not occur with optimal early-stopping. However, this is consistent with our generalized double descent hypothesis: if early stopping prevents models from reaching $0$ train error then we would not expect to see double-descent, since the EMC does not reach the number of train samples. Further, we show at least one setting where model-wise double descent can still occur even with optimal early stopping (ResNets on CIFAR-100 with no label noise, see Figure 19). We have not observed settings where more data hurts when optimal early-stopping is used. However, we are not aware of reasons which preclude this from occurring. We leave fully understanding the optimal early stopping behavior of double descent as an important open question for future work.

### Label Noise

In our experiments, we observe double descent most strongly in settings with label noise. However, we believe this effect is not fundamentally about label noise, but rather about *model mis-specification*. For example, consider a setting where the label noise is not truly random, but rather pseudorandom (with respect to the family of classifiers being trained). In this setting, the performance of the Bayes optimal classifier would not change (since the pseudorandom noise is deterministic, and invertible), but we would observe an identical double descent as with truly random label noise. Thus, we view adding label noise as merely a proxy for making distributions "harder"--- i.e. increasing the amount of model mis-specification.

### Other Notions of Model Complexity

Our notion of *Effective Model Complexity* is related to classical complexity notions such as Rademacher complexity, but differs in several crucial ways: EMC depends on the *true labels* of the data distribution, and EMC depends on the training procedure, not just the model architecture.

Other notions of model complexity which do not incorporate features and would not suffice to characterize the location of the double-descent peak. Rademacher complexity, for example, is determined by the ability of a model architecture to fit a randomly-labeled train set. But Rademacher complexity and VC dimension are both insufficient to determine the model-wise double descent peak location, since they do not depend on the distribution of labels--- and our experiments show that adding label noise shifts the location of the peak.

Moreover, both Rademacher complexity and VC dimension depend only on the model family and data distribution, and not on the training procedure used to find models. Thus, they are not capable of capturing train-time double-descent effects, such as "epoch-wise" double descent, and the effect of data-augmentation on the peak location.
