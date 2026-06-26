<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs)

Topics include Activation functions, Exponential linear units, ReLU alternatives, Vanishing gradients, Bias shift, Neural networks, Classification, Generalization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

ELU introduces a negative saturating branch while preserving identity for positive inputs, aiming to reduce bias shift and improve optimization relative to ReLU-style activations. The experiments argue that ELUs can train faster and generalize better than ReLU and leaky ReLU baselines, including cases where batch normalization does not add further benefit.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce the "exponential linear unit" (ELU) which speeds up learning in deep neural networks and leads to higher classification accuracies. Like rectified linear units (ReLUs), leaky ReLUs (LReLUs) and parametrized ReLUs (PReLUs), ELUs alleviate the vanishing gradient problem via the identity for positive values. However, ELUs have improved learning characteristics compared to the units with other activation functions. In contrast to ReLUs, ELUs have negative values which allows them to push mean unit activations closer to zero like batch normalization but with lower computational complexity. Mean shifts toward zero speed up learning by bringing the normal gradient closer to the unit natural gradient because of a reduced bias shift effect. While LReLUs and PReLUs have negative values, too, they do not ensure a noise-robust deactivation state. ELUs saturate to a negative value with smaller inputs and thereby decrease the forward propagated variation and information. Therefore, ELUs code the degree of presence of particular phenomena in the input, while they do not quantitatively model the degree of their absence.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In experiments, ELUs lead not only to faster learning, but also to significantly better generalization performance than ReLUs and LReLUs on networks with more than 5 layers. On CIFAR-100 ELUs networks significantly outperform ReLU networks with batch normalization while batch normalization does not improve ELU networks. ELU networks are among the top 10 reported CIFAR-10 results and yield the best published result on CIFAR-100, without resorting to multi-view evaluation or model averaging. On ImageNet, ELU networks considerably speed up learning compared to a ReLU network with the same architecture, obtaining less than 10% classification error for a single crop, single model network.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Currently the most popular activation function for neural networks is the rectified linear unit (ReLU), which was first proposed for restricted Boltzmann machines and then successfully used for neural networks. The ReLU activation function is the identity for positive arguments and zero otherwise. Besides producing sparse codes, the main advantage of ReLUs is that they alleviate the vanishing gradient problem since the derivative of 1 for positive values is not contractive. However ReLUs are non-negative and, therefore, have a mean activation larger than zero.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Units that have a non-zero mean activation act as bias for the next layer. If such units do not cancel each other out, learning causes a bias shift for units in next layer. The more the units are correlated, the higher their bias shift. We will see that Fisher optimal learning, i.e., the natural gradient, would correct for the bias shift by adjusting the weight updates. Thus, less bias shift brings the standard gradient closer to the natural gradient and speeds up learning. We aim at activation functions that push activation means closer to zero to decrease the bias shift effect.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Centering the activations at zero has been proposed in order to keep the off-diagonal entries of the Fisher information matrix small. For neural network it is known that centering the activations speeds up learning. "Batch normalization" also centers activations with the goal to counter the internal covariate shift. Also the Projected Natural Gradient Descent algorithm (PRONG) centers the activations by implicitly whitening them.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

An alternative to centering is to push the mean activation toward zero by an appropriate activation function. Therefore $tanh$ has been preferred over logistic functions. Recently "Leaky ReLUs" (LReLUs) that replace the negative part of the ReLU with a linear function have been shown to be superior to ReLUs. Parametric Rectified Linear Units (PReLUs) generalize LReLUs by learning the slope of the negative part which yielded improved learning behavior on large image benchmark data sets. Another variant are Randomized Leaky Rectified Linear Units (RReLUs) which randomly sample the slope of the negative part which raised the performance on image benchmark datasets and convolutional networks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to ReLUs, activation functions like LReLUs, PReLUs, and RReLUs do not ensure a noise-robust deactivation state. We propose an activation function that has negative values to allow for mean activations close to zero, but which saturates to a negative value with smaller arguments. The saturation decreases the variation of the units if deactivated, so the precise deactivation argument is less relevant. Such an activation function can code the degree of presence of particular phenomena in the input, but does not quantitatively model the degree of their absence. Therefore, such an activation function is more robust to noise. Consequently, dependencies between coding units are much easier to model and much easier to interpret since only activated code units carry much information. Furthermore, distinct concepts are much less likely to interfere with such activation functions since the deactivation state is non-informative, i.e. variance decreasing.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Bias Shift Correction Speeds Up Learning", "weight": 1.0} -->

To derive and analyze the bias shift effect mentioned in the introduction, we utilize the natural gradient. The natural gradient corrects the gradient direction with the inverse Fisher information matrix and, thereby, enables Fisher optimal learning, which ensures the steepest descent in the Riemannian parameter manifold and Fisher efficiency for online learning. The recently introduced Hessian-Free Optimization technique and the Krylov Subspace Descent methods use an extended Gauss-Newton approximation of the Hessian, therefore they can be interpreted as versions of natural gradient descent.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Bias Shift Correction Speeds Up Learning", "weight": 1.0} -->

Since for neural networks the Fisher information matrix is typically too expensive to compute, different approximations of the natural gradient have been proposed. Topmoumoute Online natural Gradient Algorithm (TONGA) uses a low-rank approximation of natural gradient descent. FActorized Natural Gradient (FANG) estimates the natural gradient via an approximation of the Fisher information matrix by a Gaussian graphical model. The Fisher information matrix can be approximated by a block-diagonal matrix, where unit or quasi-diagonal natural gradients are used. Unit natural gradients or "Unitwise Fisher's scoring" are based on natural gradients for perceptrons. We will base our analysis on the unit natural gradient.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Bias Shift Correction Speeds Up Learning", "weight": 1.0} -->

We restrict the Fisher information matrix to weights leading to unit $i$ which is the unit Fisher information matrix $\mathbf{F}$. $\mathbf{F}$ captures only the interactions of weights to unit $i$. Consequently, the unit natural gradient only corrects the interactions of weights to unit $i$, i.e. considers the Riemannian parameter manifold only in a subspace. The unit Fisher information matrix is Weighting the activations by $\delta^{2}$ is equivalent to adjusting the probability of drawing inputs $\mathbf{z}$. Inputs $\mathbf{z}$ with large $\delta^{2}$ are drawn with higher probability.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Bias Shift Correction Speeds Up Learning", "weight": 1.0} -->

For the row ${\mathbf{b}} = \left\lbrack {{\mathbf{F}}{({\mathbf{w}})}} \right\rbrack_{0}$ that corresponds to the bias weight, we have: The next Theorem 1") gives the correction of the standard gradient by the unit natural gradient where the bias weight is treated separately (see also Yang & Amari).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Exponential Linear Units (ELUs)", "weight": 1.0} -->

The exponential linear unit (ELU) with $0 < \alpha$ is The ELU hyperparameter $\alpha$ controls the value to which an ELU saturates for negative net inputs (see Fig. 1 ‣ Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs)")). ELUs diminish the vanishing gradient effect as rectified linear units (ReLUs) and leaky ReLUs (LReLUs) do. The vanishing gradient problem is alleviated because the positive part of these functions is the identity, therefore their derivative is one and not contractive. In contrast, $\tanh$ and sigmoid activation functions are contractive almost everywhere.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Exponential Linear Units (ELUs)", "weight": 1.0} -->

In contrast to ReLUs, ELUs have negative values which pushes the mean of the activations closer to zero. Mean activations that are closer to zero enable faster learning as they bring the gradient closer to the natural gradient (see Theorem 2") and text thereafter). ELUs saturate to a negative value when the argument gets smaller. Saturation means a small derivative which decreases the variation and the information that is propagated to the next layer. Therefore the representation is both noise-robust and low-complex. ELUs code the degree of presence of input concepts, while they neither quantify the degree of their absence nor distinguish the causes of their absence. This property of non-informative deactivation states is also present at ReLUs and allowed to detect biclusters corresponding to biological modules in gene expression datasets and to identify toxicophores in toxicity prediction. The enabling features for these interpretations is that activation can be clearly distinguished from deactivation and that only active units carry relevant information and can crosstalk.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Experiments Using ELUs", "weight": 1.0} -->

(a) Average unit activation (b) Cross entropy loss Figure 2: ELU networks evaluated at MNIST. Lines are the average over five runs with different random initializations, error bars show standard deviation. Panel (a): median of the average unit activation for different activation functions. Panel (b): Training set (straight line) and validation set (dotted line) cross entropy loss. All lines stay flat after epoch 25.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Experiments Using ELUs", "weight": 1.0} -->

In this section, we assess the performance of exponential linear units (ELUs) if used for unsupervised and supervised learning of deep autoencoders and deep convolutional networks. ELUs with $\alpha = 1.0$ are compared to (i) Rectified Linear Units (ReLUs) with activation ${f{(x)}} = {\max{(0,x)}}$, (ii) Leaky ReLUs (LReLUs) with activation ${f{(x)}} = {\max{({\alphax},x)}}$ ($0 < \alpha < 1$), and (iii) Shifted ReLUs (SReLUs) with activation ${f{(x)}} = {\max{({- 1},x)}}$. Comparisons are done with and without batch normalization.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Experiments Using ELUs", "weight": 1.0} -->

The following benchmark datasets are used: (i) MNIST (gray images in 10 classes, 60k train and 10k test), (ii) CIFAR-10 (color images in 10 classes, 50k train and 10k test), (iii) CIFAR-100 (color images in 100 classes, 50k train and 10k test), and (iv) ImageNet (color images in 1,000 classes, 1.3M train and 100k tests).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Learning Behavior", "weight": 1.0} -->

We first want to verify that ELUs keep the mean activations closer to zero than other units. Fully connected deep neural networks with ELUs ($\alpha = 1.0$), ReLUs, and LReLUs ($\alpha = 0.1$) were trained on the MNIST digit classification dataset while each hidden unit's activation was tracked. Each network had eight hidden layers of 128 units each, and was trained for 300 epochs by stochastic gradient descent with learning rate $0.01$ and mini-batches of size 64. The weights have been initialized according to. After each epoch we calculated the units' average activations on a fixed subset of the training data. Fig. 2") shows the median over all units along learning. ELUs stay have smaller median throughout the training process. The training error of ELU networks decreases much more rapidly than for the other networks.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Learning Behavior", "weight": 1.0} -->

Section C") in the appendix compares the variance of median activation in ReLU and ELU networks. The median varies much more in ReLU networks. This indicates that ReLU networks continuously try to correct the bias shift introduced by previous weight updates while this effect is much less prominent in ELU networks.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Autoencoder Learning", "weight": 1.0} -->

To evaluate ELU networks at unsupervised settings, we followed Martens and Desjardins et al. and trained a deep autoencoder on the MNIST dataset. The encoder part consisted of four fully connected hidden layers with sizes 1000, 500, 250 and 30, respectively. The decoder part was symmetrical to the encoder. For learning we applied stochastic gradient descent with mini-batches of 64 samples for 500 epochs using the fixed learning rates ($10^{- 2},10^{- 3},10^{- 4},10^{- 5}$). Fig. 3") shows, that ELUs outperform the competing activation functions in terms of training / test set reconstruction error for all learning rates. As already noted by Desjardins et al., higher learning rates seem to perform better.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Comparison of Activation Functions", "weight": 1.0} -->

In this subsection we show that ELUs indeed possess a superior learning behavior compared to other activation functions as postulated in Section 3 ‣ Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs)"). Furthermore we show that ELU networks perform better than ReLU networks with batch normalization. We use as benchmark dataset CIFAR-100 and use a relatively simple convolutional neural network (CNN) architecture to keep the computational complexity reasonable for comparisons.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Comparison of Activation Functions", "weight": 1.0} -->

(b) Training loss (start) (c) Training loss (end) (e) Test error (start) (f) Test error (end) Figure 4: Comparison of ReLUs, LReLUs, and SReLUs on CIFAR-100. Panels (a-c) show the training loss, panels (d-f) the test classification error. The ribbon band show the mean and standard deviation for 10 runs along the curve. ELU networks achieved lowest test error and training loss.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Comparison of Activation Functions", "weight": 1.0} -->

(d) ELU - ReLU (end) (e) ELU - SReLU (end) (f) ELU - LReLU (end) Figure 5: Pairwise comparisons of ELUs with ReLUs, SReLUs, and LReLUs with and without batch normalization (BN) on CIFAR-100. Panels are described as in Fig. 4. ELU networks outperform ReLU networks with batch normalization.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Comparison of Activation Functions", "weight": 1.0} -->

The CNN for these CIFAR-100 experiments consists of 11 convolutional layers arranged in stacks of (${\lbrack{1 \times 192 \times 5}\rbrack},{\lbrack{1 \times 192 \times 1},{1 \times 240 \times 3}\rbrack},{\lbrack{1 \times 240 \times 1},{1 \times 260 \times 2}\rbrack},{\lbrack{1 \times 260 \times 1},{1 \times 280 \times 2}\rbrack},{\lbrack{1 \times 280 \times 1},{1 \times 300 \times 2}\rbrack},{\lbrack{1 \times 300 \times 1}\rbrack},{\lbrack{1 \times 100 \times 1}\rbrack}$) layers $\times$ units $\times$ receptive fields. 2$\times$`<!-- -->`{=html}2 max-pooling with a stride of 2 was applied after each stack.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Comparison of Activation Functions", "weight": 1.0} -->

For network regularization we used the following drop-out rate for the last layer of each stack ($0.0,0.1,0.2,0.3,0.4,0.5,0.0$). The $L2$-weight decay regularization term was set to $0.0005$. The following learning rate schedule was applied (${0 - {35k{\lbrack 0.01\rbrack}}},{{35k} - {85k{\lbrack 0.005\rbrack}}},{{85k} - {135k{\lbrack 0.0005\rbrack}}},{{135k} - {165k{\lbrack 0.00005\rbrack}}}$) (iterations \[learning rate\]). For fair comparisons, we used this learning rate schedule for all networks. During previous experiments, this schedule was optimized for ReLU networks, however as ELUs converge faster they would benefit from an adjusted schedule.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Comparison of Activation Functions", "weight": 1.0} -->

The momentum term learning rate was fixed to 0.9. The dataset was preprocessed as described in Goodfellow et al. with global contrast normalization and ZCA whitening. Additionally, the images were padded with four zero pixels at all borders. The model was trained on $32 \times 32$ random crops with random horizontal flipping. Besides that, we no further augmented the dataset during training. Each network was run 10 times with different weight initialization. Across networks with different activation functions the same run number had the same initial weights.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Comparison of Activation Functions", "weight": 1.0} -->

Mean test error results of networks with different activation functions are compared in Fig. 4"), which also shows the standard deviation. ELUs yield on average a test error of 28.75($\pm$`<!-- -->`{=html}0.24)%, while SReLUs, ReLUs and LReLUs yield 29.35($\pm$`<!-- -->`{=html}0.29)%, 31.56($\pm$`<!-- -->`{=html}0.37)% and 30.59($\pm$`<!-- -->`{=html}0.29)%, respectively. ELUs achieve both lower training loss and lower test error than ReLUs, LReLUs, and SReLUs. Both the ELU training and test performance is significantly better than for other activation functions (Wilcoxon signed-rank test with $p$-value$<$`<!-- -->`{=html}0.001).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Comparison of Activation Functions", "weight": 1.0} -->

Batch normalization improved ReLU and LReLU networks, but did not improve ELU and SReLU networks (see Fig. 5")). ELU networks significantly outperform ReLU networks with batch normalization (Wilcoxon signed-rank test with $p$-value$<$`<!-- -->`{=html}0.001).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Classification Performance on CIFAR-100 and CIFAR-10", "weight": 1.0} -->

The following experiments should highlight the generalization capabilities of ELU networks.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Classification Performance on CIFAR-100 and CIFAR-10", "weight": 1.0} -->

The CNN architecture is more sophisticated than in the previous subsection and consists of 18 convolutional layers arranged in stacks of (${\lbrack{1 \times 384 \times 3}\rbrack},{\lbrack{1 \times 384 \times 1},{1 \times 384 \times 2},{2 \times 640 \times 2}\rbrack},{\lbrack{1 \times 640 \times 1},{3 \times 768 \times 2}\rbrack},{\lbrack{1 \times 768 \times 1},{2 \times 896 \times 2}\rbrack},{\lbrack{1 \times 896 \times 3},{2 \times 1024 \times 2}\rbrack},{\lbrack{1 \times 1024 \times 1},{1 \times 1152 \times 2}\rbrack},{\lbrack{1 \times 1152 \times 1}\rbrack},{\lbrack{1 \times 100 \times

<!-- chunk {"id": "body-0032", "role": "body", "section": "Classification Performance on CIFAR-100 and CIFAR-10", "weight": 1.0} -->

Initial drop-out rate, Max-pooling after each stack, $L2$-weight decay, momentum term, data preprocessing, padding, and cropping were as in previous section. The initial learning rate was set to 0.01 and decreased by a factor of 10 after 35k iterations. The mini-batch size was 100. For the final 50k iterations fine-tuning we increased the drop-out rate for all layers in a stack to ($0.0,0.1,0.2,0.3,0.4,0.5,0.0$), thereafter increased the drop-out rate by a factor of 1.5 for 40k additional iterations.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Classification Performance on CIFAR-100 and CIFAR-10", "weight": 1.0} -->

CIFAR-10 (test error %) CIFAR-100 (test error %) Table 1: Comparison of ELU networks and other CNNs on CIFAR-10 and CIFAR-100. Reported is the test error in percent misclassification for ELU networks and recent convolutional architectures like AlexNet, DSN, NiN, Maxout, All-CNN, Highway Network, and Fractional Max-Pooling. Best results are in bold. ELU networks are second best for CIFAR-10 and best for CIFAR-100.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Classification Performance on CIFAR-100 and CIFAR-10", "weight": 1.0} -->

ELU networks are compared to following recent successful CNN architectures: AlexNet, DSN, NiN, Maxout, All-CNN, Highway Network and Fractional Max-Pooling. The test error in percent misclassification are given in Tab. 1"). ELU-networks are the second best on CIFAR-10 with a test error of 6.55% but still they are among the top 10 best results reported for CIFAR-10. ELU networks performed best on CIFAR-100 with a test error of 24.28%. This is the best published result on CIFAR-100, without even resorting to multi-view evaluation or model averaging.

<!-- chunk {"id": "body-0035", "role": "body", "section": "ImageNet Challenge Dataset", "weight": 1.0} -->

Finally, we evaluated ELU-networks on the 1000-class ImageNet dataset. It contains about 1.3M training color images as well as additional 50k images and 100k images for validation and testing, respectively. For this task, we designed a 15 layer CNN, which was arranged in stacks of (${1 \times 96 \times 6},{3 \times 512 \times 3},{5 \times 768 \times 3},{3 \times 1024 \times 3},{{2 \times 4096 \times F}C},{{1 \times 1000 \times F}C}$) layers $\times$ units $\times$ receptive fields or fully-connected (FC). 2$\times$`<!-- -->`{=html}2 max-pooling with a stride of 2 was applied after each stack and spatial pyramid pooling (SPP) with 3 levels before the first FC layer. For network regularization we set the $L2$-weight decay term to $0.0005$ and used 50% drop-out in the two penultimate FC layers.

<!-- chunk {"id": "body-0036", "role": "body", "section": "ImageNet Challenge Dataset", "weight": 1.0} -->

Images were re-sized to 256$\times$`<!-- -->`{=html}256 pixels and per-pixel mean subtracted. Trained was on $224 \times 224$ random crops with random horizontal flipping. Besides that, we did not augment the dataset during training.

<!-- chunk {"id": "body-0037", "role": "body", "section": "ImageNet Challenge Dataset", "weight": 1.0} -->

(b) Top-5 test error (c) Top-1 test error Figure 6: ELU networks applied to ImageNet. The x-axis gives the number of iterations and the y-axis the (a) training loss, (b) top-5 error, and (c) the top-1 error of 5,000 random validation samples, evaluated on the center crop. Both activation functions ELU (blue) and ReLU (purple) lead for convergence, but ELUs start reducing the error earlier and reach the 20% top-5 error after 160k iterations, while ReLUs need 200k iterations to reach the same error rate.

<!-- chunk {"id": "body-0038", "role": "body", "section": "ImageNet Challenge Dataset", "weight": 1.0} -->

Fig. 6") shows the learning behavior of ELU vs. ReLU networks. Panel (b) shows that ELUs start reducing the error earlier. The ELU-network already reaches the 20% top-5 error after 160k iterations, while the ReLU network needs 200k iterations to reach the same error rate. The single-model performance was evaluated on the single center crop with no further augmentation and yielded a top-5 validation error below 10%.

<!-- chunk {"id": "body-0039", "role": "body", "section": "ImageNet Challenge Dataset", "weight": 1.0} -->

Currently ELU nets are 5% slower on ImageNet than ReLU nets. The difference is small because activation functions generally have only minor influence on the overall training time. In terms of wall clock time, ELUs require 12.15h vs. ReLUs with 11.48h for 10k iterations. We expect that ELU implementations can be improved, e.g. by faster exponential functions.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have introduced the exponential linear units (ELUs) for faster and more precise learning in deep neural networks. ELUs have negative values, which allows the network to push the mean activations closer to zero. Therefore ELUs decrease the gap between the normal gradient and the unit natural gradient and, thereby speed up learning. We believe that this property is also the reason for the success of activation functions like LReLUs and PReLUs and of batch normalization. In contrast to LReLUs and PReLUs, ELUs have a clear saturation plateau in its negative regime, allowing them to learn a more robust and stable representation. Experimental results show that ELUs significantly outperform other activation functions on different vision datasets. Further ELU networks perform significantly better than ReLU networks trained with batch normalization. ELU networks achieved one of the top 10 best reported results on CIFAR-10 and set a new state of the art in CIFAR-100 without the need for multi-view test evaluation or model averaging. Furthermore, ELU networks produced competitive results on the ImageNet in much fewer epochs than a corresponding ReLU network.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Given their outstanding performance, we expect ELU networks to become a real time saver in convolutional networks, which are notably time-intensive to train from scratch otherwise.
