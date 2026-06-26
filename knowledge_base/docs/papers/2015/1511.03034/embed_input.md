<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning with a Strong Adversary

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The robustness of neural networks to intended perturbations has recently attracted significant attention. In this paper, we propose a new method, learning with a strong adversary, that learns robust classifiers from supervised data. The proposed method takes finding adversarial examples as an intermediate step. A new and simple way of finding adversarial examples is presented and experimentally shown to be efficient. Experimental results demonstrate that resulting learning method greatly improves the robustness of the classification models produced.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep Neural Network (DNN) models have recently demonstrated impressive learning results in many visual and speech classification problems. One reason for this success is believed to be the expressive capacity of deep network architectures. Even though classifiers are typically evaluated by their misclassification rate, robustness is also a highly desirable property: intuitively, it is desirable for a classifier to be 'smooth' in the sense that a small perturbation of its input should not change its predictions significantly. An intriguing recent discovery is that DNN models do not typically possess such a robustness property. An otherwise highly accurate DNN model can be fooled into misclassifying typical data points by introducing a human-indistinguishable perturbation of the original inputs. We call such a perturbed data set 'adversarial examples'. An even more curious fact is that the same set of such adversarial examples is also misclassified by a diverse set of classification models, such as KNN, Boosting Tree, even if they are trained with different architectures and different hyperparameters.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since the appearance of Szegedy et al., increasing attention has been paid to the curious phenomenon of 'adversarial perturbation' in the deep learning community; see, for example. Goodfellow et al. suggest that one reason for the detrimental effect of adversarial examples lies in the implicit linearity of the classification models in high dimensional spaces. Additional exploration by Tabacof & Valle has demonstrated that, for image classification problems, adversarial images inhabit large "adversarial pockets" in the pixel space. Based on these observations, different ways of finding adversarial examples have been proposed, among which the most relevant to our study is that of, where a linear approximation is used to obviate the need for any auxiliary optimization problem to be solved. In this paper, we further investigate the role of adversarial training on classifier robustness and propose a simple new approach to finding 'stronger' adversarial examples. Experimental results suggest that the proposed method is more effective than previous approaches in the sense that the resulting DNN classifiers obtain worse performance under the same magnitude of perturbation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main achievement of this paper is a training method that is able to produce robust classifiers with high classification accuracy in the face of stronger data perturbation. The approach we propose differs from previous approaches in a few ways. First, Goodfellow et al. suggests using an augmented objective that combines the original training objective with an additional objective that is measured after after the training inputs have been perturbed. Alternatively, suggest, as a specialization of the method, to only use the objective defined on the perturbed data. However, there is no theoretical analysis to justify that classifiers learned in this way are indeed robust; both methods are proposed heuristically. In our proposed approach, we formulate the learning procedure as a min-max problem that forces the learned DNN model to be robust against adversarial examples, so that the learned classifier is inherently robust. In particular, we allow an adversary to apply perturbations to each data point in an attempt to maximize classification error, while the learning procedure attempts to minimize misclassification error against the adversary. We call this learning procedure 'learning with a strong adversary'.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Such min-max formulation has been discussed specifically, but emphasis is on its regularization effect particularly for logistic regression. Our setting is more general and applicable to different loss functions and different types of perturbations, and is the origin of our learning procedure.^11^1 Analysis of the regularization effect of such min-max formulation is postponed in the appendix, since it is not closly related to the main content of the paper. It turns out that an efficient method for finding such adversarial examples is required as an intermediate step to solve such a min-max problem, which is the first problem we address. Then we develop the full min-max training procedure that incorporates robustness to adversarially perturbed training data. The learning procedure that results turns out to have some similarities to the one proposed. Another min-max formulation is proposed in Miyato et al. but still with the interpretation of regularization. These approaches are based on significantly different understandings of this problem. Recently, a theoretical exploration of the robustness of classifiers suggests that, as expected, there is a trade-off between expressive power and robustness.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper can be considered as an exploration into this same trade-off from an engineering perspective.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows. First, we propose a new method for finding adversarial examples in Section 2. Section 3 is then devoted to developing the main method: a new procedure for learning with a stronger form of adversary. Finally, we provide an experimental evaluation of the proposed method on MNIST and CIFAR-10 in Section 4.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Notations", "weight": 1.0} -->

We denote the supervised training data by $\underset{¯}{Z} = {\{{(x_{1},y_{1})},\ldots,{(x_{N},y_{N})}\}}$. Let $K$ be the number of classes in the classification problem. The loss function used for training will be denoted by $\ell$. Given a norm $\parallel \cdot \parallel$, let $\parallel \cdot \parallel_{\ast}$ denote its dual norm, such that ${\| u\|}_{\ast} = {\max_{{\| v\|} \leq 1}{\langle u,v\rangle}}$. Denote the network by $\mathcal{N}$ whose last layer is a softmax layer ${g{(x)}} \triangleq \alpha = {(\alpha_{1},\ldots,\alpha_{K})}$ to be used for classification.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Notations", "weight": 1.0} -->

So $\mathcal{N}{(x)}$ is the predicted label for the sample $x$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Finding adversarial examples", "weight": 1.0} -->

Consider an example ${(x,y)} \in {\mathcal{X} \times {\{ 1,2,\ldots,K\}}}$ and assume that ${\mathcal{N}{(x)}} = y$, where $y$ is the true label for $x$. Our goal is to find a small perturbation $r \in \mathcal{X}$ so that ${\mathcal{N}{({X + r})}} \neq y$. This problem was originally investigated by Szegedy et al., who propose the following perturbation procedure: given $x$, solve The simple method we propose to find such a perturbation $r$ is based on the linear approximation of $g{(x)}$, ${\hat{g}{({x + r})}} = {{g{(x)}} + {Hr}}$, where $H = {\frac{\partial g}{\partial w}|}_{x}$ is the Jacobian matrix.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Finding adversarial examples", "weight": 1.0} -->

As an alternative, we consider the following question: for a fixed index $j \neq y$, what is the minimal $r_{(j)}$ satisfying ${\mathcal{N}{({x + r_{(j)}})}} = j$? Replacing $g$ by its linear approximation $\hat{g}$, one of the necessary conditions for such a perturbation $r$ is: where $H_{j}$ is the $j$-th row of $H$. Therefore, the norm of the optimal $r_{(j)}^{\ast}$ is greater than the following objective value: The optimal solution to this problem is provided in Proposition 1.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Toward Robust Neural Networks", "weight": 1.0} -->

We enhance the robustness of a neural network model by preparing the network for the worst examples by training with the following objective: where $g$ ranges over functions expressible by the network model $\mathcal{N}$ (i.e. ranging over all parameters in $\mathcal{N}$). In this formulation, the hyperparameter $c$ that controls the magnitude of the perturbation needs to be tuned. Note that when ${\ell{({g{({x_{i} + r^{(i)}})}},y_{i})}} = {\mathbb{I}}_{({{\max_{j}{({g{({x_{i} + r^{(i)}})}_{j}})}} \neq y_{i}})}$, the objective function is the misclassification error under perturbations. Often, $\ell$ is a surrogate for the misclassification loss that is differentiable and smooth.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Toward Robust Neural Networks", "weight": 1.0} -->

Let ${L_{i}{(g)}} = {{\max_{{\| r^{(i)}\|}_{2} \leq c}\ell}{({g{({x_{i} + r^{(i)}})}},y_{i})}}$. Thus the problem is to find $g^{\ast} = {{\arg\min_{g}}{\sum_{i}{L_{i}{(g)}}}}$. 1. When taking $\ell$ to be the logistic loss, $g$ to be a linear function, and the norm for perturbation to be $\ell_{\infty}$, then the inner max problem has analytical solution, and Equation matches the learning objective in Section 5 of.\2. Let $\ell$ be the negative log function and $g$ be the probability predicted by the model.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Toward Robust Neural Networks", "weight": 1.0} -->

Similarly, the objective function proposed in can be generalized as ${\alphaD_{KL}{({y_{i} \parallel p})}} + {{({1 - \alpha})}{\max_{r^{(i)}}D_{KL}}{({y_{i} \parallel \overset{\sim}{p}})}}$. Moreover, the one proposed in Miyato et al. can be interpreated as ${D_{KL}{({y_{i} \parallel p})}} + {D_{KL}{({p \parallel \overset{\sim}{p}})}}$. Experiments shows that our approach is able to achieve the best robustness while maintain high classification accuracy.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Toward Robust Neural Networks", "weight": 1.0} -->

To solve the problem using SGD, one needs to compute the derivative of $L_{i}$ with respect to (the parameters that define) $g$. The following preliminary proposition suggests a way of computing this derivative.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Computing the perturbation", "weight": 1.0} -->

We propose two different perturbation methods based on two different principles. The first proposed method, similar to that of, does not require the solution of an optimization problem. Experimental results show that this method, compared to the method proposed, is more effective in the sense that, under the same magnitude of perturbation, the accuracy reduction in the network is greater.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Likelihood Based Loss", "weight": 1.0} -->

Assume the loss function ${\ell{(x,y)}} = {h{(\alpha_{y})}}$, where $h$ is a non-negative decreasing function. A typical example of such a loss would be the logistic regression loss. In fact, most of the network models use a softmax layer as the last layer and a cross-entropy objective function. Recall that we would like to find where $x_{i}$ could be the raw data or the output of $\mathcal{N}_{rep}$. Since $h$ is decreasing, $r^{\ast} = {{\arg{\min_{{\| r^{(i)}\|} \leq c}g}}{({x_{i} + r^{(i)}})}_{y_{i}}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Likelihood Based Loss", "weight": 1.0} -->

Note that the second item here is exactly the method suggested. $\ell_{2}$ norm is used in but with different objective function rather than negative log likelihood, as mentioned at the begining of this section.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Misclassification Based Loss", "weight": 1.0} -->

In the case that the loss function $\ell$ is a surrogate loss for the misclassification rate, it is reasonable to still use the misclassification rate as the loss function $\ell$ in Equation. In this case, the problem in Equation becomes finding a perturbation $r:{{\| r\|} \leq c}$ that forces the network $\mathcal{N}$ to misclassify $x_{i}$. In practice, for $\mathcal{N}$ to achieve a good approximation, $c$ needs to be chosen to have a small value, hence it might not be large enough to force a misclassification. One intuitive way to achieve this is to perturb by $r$ in the direction proposed in Section 2, since such direction is arguably the most damaging direction for the perturbation. Therefore, in this case, we use where $r_{I}^{\ast}$ is the output of Algorithm 1.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

To investigate the training method proposed above, in conjunction with the different approaches for determining perturbations, we consider the MNIST and CIFAR-10 data sets. The MNIST data set contains 28x28 grey scale images of handwritten digits. We normalize the pixel values into the range by dividing by 256. The CIFAR-10 dataset is a tiny nature image dataset. CIFAR-10 datasets contains 10 different classes images, each image is an RGB image in size of 32x32. Input images are subtracted by mean value 117, and randomly cropped to size 28x28. We also normalize the pixel value into the range (-1, 1) by dividing 256. This normalization is for evaluating perturbation magnitude by $L_{2}$ norm. For both datasets, we randomly choose 50,000 images for training and 10,000 for testing.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Finding adversarial examples", "weight": 1.0} -->

We tested a variety of different perturbation methods on MNIST, including: 1. Perturbation based on $\alpha$ using the $\ell_{2}$ norm constraint, as shown in Section 2 (Adv_Alpha); 2. Perturbation based on using a loss function with the $\ell_{2}$ norm constraint, as shown in Section 3.1 (Adv_Loss); 3. Perturbation based on using a loss function with the $\ell_{\infty}$ norm constraint, as shown in Section 3.1 (Adv_Loss_Sign). In particular, a standard 'LeNet' model is trained on MNIST, with training and validation accuracy being $100\%$ and $99.1\%$ respectively. Based on the learned network, different validation sets are then generated by perturbing the original data with different perturbation methods. The magnitudes of the perturbations range from $0.0$ to $4.0$ in $\ell_{2}$ norm.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Finding adversarial examples", "weight": 1.0} -->

An example of such successful perturbation is show in Table 1. The classification accuracies on differently perturbed data sets are reported in Figure 1.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Finding adversarial examples", "weight": 1.0} -->

Adv_Loss_Sign Table 1: An visual example of using different perturbations; The magnitude of all the perturbations are 1.5 in ℓ2 norm. The true label of the image is 8. The first perturbed image is still predicted to be 8, while the other 2 perturbed images are predicted to be 3.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Finding adversarial examples", "weight": 1.0} -->

The networks classification accuracy decreases with increasing magnitude of the perturbation. These results suggest that Adv_Alpha is consistently, but slightly, more effective than Adv_Loss, and these two method are significantly more effective than Adv_Loss_Sign.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Finding adversarial examples", "weight": 1.0} -->

*Drawback of using $\alpha$ to find perturbations*\Note that the difference in perturbation effectiveness between using $\alpha$ and using the loss function is small. On the other hand, to compute the perturbation using $\alpha$, one needs to compute $\frac{\partial\alpha}{\partial x}$, which is $K$ times more expensive than the method using the loss function, which only needs to compute $\frac{\partial\ell}{\partial x}$. (Recall that $K$ is the number of classes.) Due to time limit, during the training procedure we only use the adversarial examples generated from the loss function for our experiments.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Learning with an adversary", "weight": 1.0} -->

We tested our overall learning approach on both MNIST and CIFAR-10. We measure the robustness of each classifier on various adversarial sets. An adversarial set of the same type for each learned classifier is generated based on the targeted classifier. We generated 3 types of adversarial data sets for the above 5 classifiers corresponding to Adv_Alpha, Adv_Loss, and Adv_Loss_Sign. In addition, we also evaluated the accuracy of these 5 classifiers on a fixed adversarial set, which is generated based on the 'Normal' network using Adv_Loss. Finally, we also report the original validation accuracies of the different networks. We use $\ell_{2}$ norm for our method to train the network.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Learning with an adversary", "weight": 1.0} -->

We first test different training methods on a 2-hidden-layer neural network model. In particular, we considered: 1. Normal back-forward propagation training, $100 \times 100$ (Normal); 2. Normal back-forward propagation training with Dropout, $200 \times 200$ (Dropout ); 3. The method, $500 \times 500$ (Goodfellow's method); 4. Learning with an adversary on raw data, $500 \times 500$ (LWA); 5. Learning with an adversary at the representation layer, $200 \times 500$ (LWA_Rep). Here $n \times m$ denote that the network has $n$ nodes for the first hidden layer, and $m$ nodes for the second one. All of the results are tested under perturbations of with the $\ell_{2}$ norm constrained to at most $1.5$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Learning with an adversary", "weight": 1.0} -->

Adv_Loss_Sign Table 2: Classification accuracies for 2-hidden-layers neural network on MNIST: the best performance on each adversarial sets are shown in bold. The magnitude of perturbations are 1.5 in ℓ2 norm.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Learning with an adversary", "weight": 1.0} -->

We sumarize the results in Table 2. Note that the normal method can not afford any perturbation on the validation set, showing that it is highly non-robust. By training with dropout, both the accuracy and robustness of the neural network are improved, but robustness remains weak; for the adversarial set generated by Adv_Alpha in particular, the resulting classification accuracy is only $19.3\%$. Goodfellow's method improves the network's robustness greatly, compared to the previous methods. However, the best accuracy and the most robustness are both achieved by LWA. In particular, on the adversarial sets generated by our methods (Adv_Loss and Adv_Alpha), the performance is improved from $84.4\%$ to $86.7\%$, and from $83.6\%$ to $86.2\%$. The result of LWA_Rep is also reported for comparison. Overall, it achieves worse performance than Goodfellow's method and LWA, but still much more robust than Dropout.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Learning with an adversary", "weight": 1.0} -->

We also evaluated these learning methods on the LeNet model, which is more complex, including convolution layers. We use Dropout for Goodfellow's method and LWA. The resulting learning curves are reported in Figure 2. It is interesting that we do not observe the trade-off between robustness and accuracy once again; this phenomenon also occurred with the 2-hidden-layers neural network.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Learning with an adversary", "weight": 1.0} -->

The final result is summarized in Table 3, which shows the great robustness of LWA. We don't observe the superiority of perturbing the representation layer to perturbing the raw data. In the learned networks, a small perturbation on the raw data incurs a much larger perturbation on the representation layer, which makes LWA_Rep difficult to achieve both high accuracy and robustness. How to avoid such perturbation explosion in the representation network remains open for future investigation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Learning with an adversary", "weight": 1.0} -->

Adv_Loss_Sign Table 3: Classification accuracies for LeNet trained using LWA on MNIST. The magnitude of perturbations are 1.5 in ℓ2 norm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Learning with an adversary", "weight": 1.0} -->

CIFAR-10 is a more difficult task compared to MNIST. Inspired by VGG-D Network, we use a network formed by 6 convolution layers with 3 fully connected layers. Same to VGG-Network, we use ReLU as the activation function. For each convolution stage, we use three 3x3 convolution layers followed by a max-pooling layer with stride of 2. We use 128, 256 filters for each convolution stage correspondingly. For three fully connected layer, we use 2048, 2048, 10 hidden units. We also split this network in representation learner and classifier view: the last two fully connected layers with hidden units 2048 and 10 are classifier and other layers below formed a representation learner. We compare the following methods: 1. Normal training (Normal); 2. Normal training with Dropout (Dropout); 3. Goodfellow's method with Dropout (Goodfellow's method); 3. Learning with a strong adversary on raw data with Dropout (LWA); 4. Learning with a strong adversary at the representation layer with Dropout (LWA_Rep).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Learning with an adversary", "weight": 1.0} -->

We use batch normalization (BN) to stabilize the learning of LWA_Rep. We also test the performances of different methods with batch normalization (BN). The results are summarized in Table 4. Learning with a strong adversary again achieves better robustness, but we also observe a small decrease on their classification accuracies.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Learning with an adversary", "weight": 1.0} -->

Adv_Loss_Sign Table 4: Classification accuracies on CIFAR-10: the best performance on each adversarial sets are shown in bold. The magnitude of perturbations are 0.5 in ℓ2 norm.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We investigate the curious phenomenon of 'adversarial perturbation' in a formal min-max problem setting. A generic algorithm is developed based on the proposed min-max formulation, which is more general and allows to replace previous heuristic algorithms with formally derived ones. We also propose a more efficient way in finding adversarial examples for a given network. The experimental results suggests that learning with a strong adversary is promising in the sense that compared to the benchmarks in the literature, it achieves significantly better robustness while maintain high normal accuracy.
