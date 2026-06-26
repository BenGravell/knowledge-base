<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Label Noise SGD Provably Prefers Flat Global Minimizers

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In overparametrized models, the noise in stochastic gradient descent (SGD) implicitly regularizes the optimization trajectory and determines which local minimum SGD converges to. Motivated by empirical studies that demonstrate that training with noisy labels improves generalization, we study the implicit regularization effect of SGD with label noise. We show that SGD with label noise converges to a stationary point of a regularized loss L(theta) +lambdaR(theta), where L(theta) is the training loss, lambda is an effective regularization parameter depending on the step size, strength of the label noise, and the batch size, and R(theta) is an explicit regularizer that penalizes sharp minimizers. Our analysis uncovers an additional regularization effect of large learning rates beyond the linear scaling rule that penalizes large eigenvalues of the Hessian more than small ones. We also prove extensions to classification with general loss functions, SGD with momentum, and SGD with general noise covariance, significantly strengthening the prior work of Blanc et al. to global convergence and large learning rates and of HaoChen et al. to general models.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the central questions in modern machine learning theory is the generalization capability of overparametrized models trained by stochastic gradient descent (SGD). Recent work identifies the implicit regularization effect due to the optimization algorithm as one key factor in explaining the generalization of overparameterized models. This implicit regularization is controlled by many properties of the optimization algorithm including search direction, learning rate, batch size, momentum and dropout.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The parameter-dependent noise distribution in SGD is a crucial source of regularization. Blanc et al. initiated the study of the regularization effect of label noise SGD with square loss^11^1Label noise SGD computes the stochastic gradient by first drawing a sample $(x_{i},y_{i})$, perturbing $y_{i}' = {y_{i} + \epsilon}$ with $\epsilon \sim {\{{- \sigma},\sigma\}}$, and computing the gradient with respect to $(x_{i},y_{i}')$. by characterizing the local stability of global minimizers of the training loss.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

By identifying a data-dependent regularizer $R{(\theta)}$, Blanc et al. proved that label noise SGD locally diverges from the global minimizer $\theta^{\ast}$ if and only if $\theta^{\ast}$ is not a first-order stationary point of The analysis is only able to demonstrate that with sufficiently small step size $\eta$, label noise SGD initialized at $\theta^{\ast}$ locally diverges by a distance of $\eta^{0.4}$ and correspondingly decreases the regularizer by $\eta^{0.4}$. This is among the first results that establish that the noise distribution alters the local stability of stochastic gradient descent. However, the parameter movement of $\eta^{0.4}$ is required to be inversely polynomially small in dimension and condition number and is thus too small to affect the predictions of the model.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

HaoChen et al., motivated by the local nature of Blanc et al., analyzed label noise SGD in the quadratically-parametrized linear regression model. Under a well-specified sparse linear regression model and with isotropic features, HaoChen et al. proved that label noise SGD recovers the sparse ground-truth despite overparametrization, which demonstrated a global implicit bias towards sparsity in the quadratically-parametrized linear regression model.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work seeks to identify the global implicit regularization effect of label noise SGD. Our primary result, which supports Blanc et al., proves that label noise SGD converges to a stationary point of ${L{(\theta)}} + {\lambdaR{(\theta)}}$, where the regularizer $R{(\theta)}$ penalizes sharp regions of the loss landscape.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The focus of this paper is on label noise SGD due to its strong regularization effects in both real and synthetic experiments. Furthermore, label noise is used in large-batch training as an additional regularizer when the regularization from standard regularizers (e.g. mini-batch, batch-norm, and dropout) is not sufficient. Label noise SGD is also known to be less sensitive to initialization, as shown in HaoChen et al.. In stark contrast, mini-batch SGD remains stuck when initialized at any poor global minimizer. Our analysis demonstrates a global regularization effect of label noise SGD by proving it converges to a stationary point of a regularized loss ${L{(\theta)}} + {\lambdaR{(\theta)}}$, even when initialized at a zero error global minimum.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The learning rate and minibatch size in SGD are also known to be important sources of regularization. Our main theorem highlights the importance of learning rate and batch size as the hyperparameters that control the balance between the loss and the regularizer -- larger learning rate and smaller batch size leads to stronger regularization.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Section 2 reviews the notation and assumptions used throughout the paper. Section 2.4 formally states the main result and Section 3 sketches the proof. Section 4 presents experimental results which support our theory. Finally, Section 6 discusses the implications of this work.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Setup and Main Result", "weight": 1.0} -->

Section 2.1 describes our notation and the SGD with label noise algorithm. Section 2.2 ‣ 2 Problem Setup and Main Result ‣ Label Noise SGD Provably Prefers Flat Global Minimizers") introduces the explicit formula for the regularizer $R{(\theta)}$. Sections 2.3-Stationary Points ‣ 2 Problem Setup and Main Result ‣ Label Noise SGD Provably Prefers Flat Global Minimizers") and 2.4 formally state our main result.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 2 (Learning Rate Separation)", "weight": 1.0} -->

In addition, we make the following local Kurdyka-Łojasiewicz assumption (KL assumption) which ensures that there are no regions where the loss is very flat. The KL assumption is very general and holds for some $\delta > 0$ for any analytic function defined on a compact domain (see Lemma 17).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 3 (KL)", "weight": 1.0} -->

We assume ${L{(\theta^{\ast})}} = 0$ for any global minimizer $\theta^{\ast}$. Note that if $L$ satisfies 3. ‣ 2.1 Notation ‣ 2 Problem Setup and Main Result ‣ Label Noise SGD Provably Prefers Flat Global Minimizers") for some $\delta$ then it also satisfies 3. ‣ 2.1 Notation ‣ 2 Problem Setup and Main Result ‣ Label Noise SGD Provably Prefers Flat Global Minimizers") for any $\delta' < \delta$. 3. ‣ 2.1 Notation ‣ 2 Problem Setup and Main Result ‣ Label Noise SGD Provably Prefers Flat Global Minimizers") with $\delta = 1$ is equivalent to the much stronger Polyak-Łojasiewicz condition which is equivalent to local strong convexity.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 3 (KL)", "weight": 1.0} -->

We will use $O,\Theta,\Omega$ to hide any polynomial dependence on $\mu,\ell_{f},\rho_{f},\kappa_{f},\nu,{1/\sigma},n,d$ and $\overset{\sim}{O}$ to hide additional polynomial dependence on ${\log{1/\eta}},{\log B}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The Implicit Regularizer $R{(\\theta)}$", "weight": 1.0} -->

For $L,\sigma^{2},B,\eta$ as defined above, we define the implicit regularizer $R{(\theta)}$, the effective regularization parameter $\lambda$, and the regularized loss $\overset{\sim}{L}{(\theta)}$: [width=]tikz/regplot Figure 1: Comparison of regularization strength in one dimension for the implicit regularizer ${\lambdaR{(\theta)}} \propto {\log{({1 - \frac{\eta\ell}{2}})}}$ and its linear approximation around η = 0, ${\frac{\lambda}{4}{tr}{\nabla^{2}L}{(\theta)}} \propto {\eta\ell}$. Here ℓ = ∥∇2L (θ)∥2 measures the sharpness at θ.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The Implicit Regularizer $R{(\\theta)}$", "weight": 1.0} -->

However, in additional to the linear scaling rule, which is implicit in our definition of $\lambda$, our analysis uncovers an additional regularization effect of large learning rates that penalizes larger eigenvalues more than smaller ones (see Figure 1 ‣ 2 Problem Setup and Main Result ‣ Label Noise SGD Provably Prefers Flat Global Minimizers") and Section 6.1).

<!-- chunk {"id": "body-0017", "role": "body", "section": "The Implicit Regularizer $R{(\\theta)}$", "weight": 1.0} -->

The goal of this paper is to show that Algorithm 1 converges to a stationary point of the regularized loss $\overset{\sim}{L} = {L + {\lambdaR}}$. In particular, we will show convergence to an $(\epsilon,\gamma)$-stationary point, which is defined in the next section.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Local Coupling", "weight": 1.0} -->

Let $\Phi_{k}{(\cdot)}$ denote $k$ steps of gradient descent on the regularized loss $\overset{\sim}{L}$, i.e. where ${\overset{\sim}{L}{(\theta)}} = {{L{(\theta)}} + {\lambdaR{(\theta)}}}$ is the regularized loss defined in Equation 1 ‣ 2 Problem Setup and Main Result ‣ Label Noise SGD Provably Prefers Flat Global Minimizers").

<!-- chunk {"id": "body-0019", "role": "body", "section": "Comparison with Blanc et al", "weight": 1.0} -->

Like Blanc et al., Lemma 1 shows that $\theta$ locally follows the trajectory of gradient descent on an implicit regularizer $R{(\theta)}$. However, there are a few crucial differences: Because we do not assume we start near a global minimizer where $L = 0$, we couple to a regularized loss $\overset{\sim}{L} = {L + {\lambdaR}}$ rather than just the regularizer $R{(\theta)}$. In this setting there is an additional correction term to the Hessian (Proposition 1) that requires carefully controlling the value of the loss across reference points to prove convergence to a stationary point.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Comparison with Blanc et al", "weight": 1.0} -->

The analysis in Blanc et al. requires $\eta,\tau$ to be chosen in terms of the condition number of $\nabla^{2}L$ which can quickly grow during training as $\nabla^{2}L$ is changing. This makes it impossible to directly repeat the argument. We avoid this by precisely analyzing the error incurred by small eigenvalues, allowing us to prove convergence to an $(\epsilon,\gamma)$ stationary point of $\frac{1}{\lambda}\overset{\sim}{L}$ for fixed $\eta,\lambda$ even if the smallest nonzero eigenvalue of $\nabla^{2}L$ converges to $0$ during training.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Comparison with Blanc et al", "weight": 1.0} -->

Unlike in Blanc et al., we do not require the learning rate $\eta$ to be small. Instead, we only require that $\lambda$ scales with $\epsilon$ which can be accomplished either by decreasing the learning rate $\eta$ or increasing the batch size $B$. This allows for stronger implicit regularization in the setting when $\eta$ is large (see Section 6.1). In particular, our regularizer $R{(\theta)}$ changes with $\eta$ and is only equal to the regularizer in Blanc et al. in the limit $\eta\rightarrow 0$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

In order to prove convergence to an $(\epsilon,\gamma)$-stationary point of $\frac{1}{\eta}{\nabla\overset{\sim}{L}}$, we will define a sequence of reference points $\theta_{m}^{\ast}$ and coupling times $\{\tau_{m}\}$ and repeatedly use a version of Lemma 1 to describe the long term behavior of $\theta$. For notational simplicity, given a sequence of coupling times $\{\tau_{m}\}$, define $T_{m} = {\sum_{k < m}\tau_{k}}$ to be the total number of steps until we have reached the reference point $\theta_{m}^{\ast}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

To be able to repeat the local analysis in Lemma 1 with multiple reference points, we need a more general coupling lemma that allows the random process $\xi$ defined in each coupling to continue where the random process in the previous coupling ended.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

In order to test the ability of SGD with label noise to escape poor global minimizers and converge to better minimizers, we initialize Algorithm 1 at global minimizers of the training loss which achieve $100\%$ training accuracy yet generalize poorly to the test set. Minibatch SGD would remain fixed at these initializations because both the gradient and the noise in minibatch SGD vanish at any global minimizer of the training loss. We show that SGD with label noise escapes these poor initializations and converges to flatter minimizers that generalize well, which supports Theorem 1. We run experiments with two initializations: Full Batch Initialization: We run full batch gradient descent with random initialization until convergence to a global minimizer. We call this minimizer the full batch initialization. The final test accuracy of the full batch initialization was 76%.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

Adversarial Initialization: Following Liu et al., we generate an adversarial initialization with final test accuracy $48\%$ that achieves zero training loss by first teaching the network to memorize random labels and then training it on the true labels. See Appendix D for full details.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

Experiments were run with on without data augmentation or weight decay. The experiments were conducted with randomized label flipping with probability $0.2$ (see Appendix E for the extension of Theorem 1 to classification with label flipping), cross entropy loss, and batch size 256. Because of the difficulty in computing the regularizer $R{(\theta)}$, we approximate it by its lower bound ${tr}{\nabla^{2}L}{(\theta)}$. Figure 3 shows the test accuracy and ${tr}{\nabla^{2}L}$ throughout training.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

SGD with label noise escapes both zero training loss initializations and converges to flatter minimizers that generalize much better, reaching the SGD baseline from the fullbatch initialization and getting within $1\%$ of the baseline from the adversarial initialization. The test accuracy in both cases is strongly correlated with ${tr}{\nabla^{2}L}$. The strength of the regularization is also strongly correlated with $\eta$, which supports Theorem 1. See Figure 4 for experimental results for SGD with momentum.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Classification", "weight": 1.0} -->

We restrict $y_{i} \in {\{{- 1},1\}}$, let $l:{{\mathbb{R}}\rightarrow{\mathbb{R}}^{+}}$ be an arbitrary loss function, and $p \in {}$ be a smoothing factor. Examples of $l$ include logistic loss, exponential loss, and square loss (see Table 1). We define $\overline{l}$ to be the expected smoothed loss where we flip each label with probability $p$: We make the following mild assumption on the smoothed loss $\overline{l}$ which is explicitly verified for the logistic loss, exponential loss, and square loss in Section E.2:

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 4 (Quadratic Approximation)", "weight": 1.0} -->

Then we define the per-sample loss and the sample loss as: We will follow Algorithm 2: Input: θ0, step size η, smoothing constant p, batch size B, steps T, loss function l Sample batch ℬ(k) ∼ [n]B uniformly and sample σi(k) = 1, −1 with probability 1 − p, p respectively for i ∈ ℬ(k). Let ℓ̂i(k) (θ) = l [σi(k) yi fi (θ)] and ${\hat{L}}^{(k)} = {\frac{1}{B}{\sum_{i \in \mathcal{B}^{(k)}}{\hat{\ell}}_{i}^{(k)}}}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 4 (Quadratic Approximation)", "weight": 1.0} -->

Algorithm 2 SGD with Label Smoothing Now note that the noise per sample from label smoothing at a zero loss global minimizer $\theta^{\ast}$ can be written as so ${E{\lbrack\epsilon\rbrack}} = 0$ and which will determine the strength of the regularization in Theorem 2. Finally, in order to study the local behavior around $c$ we define $\alpha = {{\overline{l}}^{\operatorname{\prime\prime}}{(c)}} > 0$ by 4. ‣ 5.1 Classification ‣ 5 Extensions ‣ Label Noise SGD Provably Prefers Flat Global Minimizers"). Corresponding values for $c,\sigma^{2},\alpha$ for logistic loss, exponential loss, and square loss are given in Table 1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "SGD with Momentum", "weight": 1.0} -->

We consider heavy ball momentum with momentum $\beta$, i.e. we replace the update in Algorithm 1 with and as before ${\overset{\sim}{L}{(\theta)}} = {{L{(\theta)}} + {\lambdaR{(\theta)}}}$. Let represent gradient descent with momentum on $\overset{\sim}{L}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Sharpness and the Effect of Large Learning Rates", "weight": 1.0} -->

Various factors can control the strength of the implicit regularization in Theorem 1. Most important is the implicit regularization parameter $\lambda = \frac{\eta\sigma^{2}}{|B|}$. This supports the hypothesis that large learning rates and small batch sizes are necessary for implicit regularization, and agrees with the standard linear scaling rule which proposes that for constant regularization strength, the learning rate $\eta$ needs to be inversely proportional to the batch size $|B|$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Sharpness and the Effect of Large Learning Rates", "weight": 1.0} -->

However, our analysis also uncovers an additional regularization effect of large learning rates. Unlike the regularizer in Blanc et al., the implicit regularizer $R{(\theta)}$ defined in Equation 1 ‣ 2 Problem Setup and Main Result ‣ Label Noise SGD Provably Prefers Flat Global Minimizers") is dependent on $\eta$. It is not possible to directly analyze the behavior of $R{(\theta)}$ as $\eta\rightarrow{2/\lambda_{1}}$ where $\lambda_{1}$ is the largest eigenvalue of $\nabla^{2}L$, as in this regime ${R{(\theta)}}\rightarrow\infty$ (see Figure 1 ‣ 2 Problem Setup and Main Result ‣ Label Noise SGD Provably Prefers Flat Global Minimizers")). If we let $\eta = \frac{2 - \nu}{\lambda_{1}}$, then we can better understand the behavior of $R{(\theta)}$ by normalizing it by $\log{2/\nu}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Sharpness and the Effect of Large Learning Rates", "weight": 1.0} -->

$R{(\theta)}$ can therefore be seen as interpolating between ${tr}{\nabla^{2}L}{(\theta)}$, when $\eta \approx 0$, and ${\|{{\nabla^{2}L}{(\theta)}}\|}_{2}$ when $\eta \approx {2/\lambda_{1}}$. This also suggests that SGD with large learning rates may be more resilient to the edge of stability phenomenon observed in Cohen et al. as the implicit regularization works harder to control eigenvalues approaching $2/\eta$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Sharpness and the Effect of Large Learning Rates", "weight": 1.0} -->

The sharpness-aware algorithm (SAM) of is also closely related to $R{(\theta)}$. SAM proposes to minimize ${\max_{{\|\delta\|}_{2} \leq \epsilon}L}{({\theta + \delta})}$. At a global minimizer of the training loss, The SAM algorithm is therefore explicitly regularizing the spectral norm of ${\nabla^{2}L}{(\theta)}$, which is closely connected to the large learning rate regularization effect of $R{(\theta)}$ when $\eta \approx {2/\lambda_{1}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Generalization Bounds", "weight": 1.0} -->

The implicit regularizer $R{(\theta)}$ is intimately connected to data-dependent generalization bounds, which measure the Lipschitzness of the network via the network Jacobian. Specifically, Wei and Ma propose the all-layer margin, which bounds the $\text{generalization error} \lesssim {\frac{\sum_{l = 1}^{L}\mathcal{C}_{l}}{\sqrt{n}}\sqrt{\frac{1}{n}{\sum_{i = 1}^{n}\frac{1}{m_{F}{(x_{i},y_{i})}^{2}}}}}$, where $\mathcal{C}_{l}$ depends only on the norm of the parameters and $m_{F}$ is the all-layer margin. The norm of the parameters is generally controlled by weight decay regularization, so we focus our discussion on the all-layer margin.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Generalization Bounds", "weight": 1.0} -->

Ignoring higher-order secondary terms, Wei and Ma \[30, Heuristic derivation of Lemma 3.1\] showed for a feed-forward network ${f{(\theta;x)}} = {\theta_{L}\sigma{({\theta_{L - 1}\ldots\sigma{({\theta_{1}x})}})}}$, the all-layer margin satisfies^33^3The output margin is defined as ${\min_{i}f_{i}}{(\theta)}y_{i}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Generalization Bounds", "weight": 1.0} -->

The following uses Equation (3.3) and the first-order approximation provided Wei and Ma and the chain rule $\frac{\partial f}{\partial\theta_{l}} = {\frac{\partial f}{\partial h_{l}}\frac{\partial h_{l}}{\partial\theta_{l - 1}}} = {\frac{\partial f}{\partial h_{l}}h_{l - 1}^{\top}}$.: as $R{(\theta)}$ is an upper bound on the squared norm of the Jacobian at any global minimizer $\theta$. We emphasize this bound is informal as we discarded the higher-order terms in controlling the all-layer margin, but it accurately reflects that the regularizer $R{(\theta)}$ lower bounds the all-layer margin $m_{F}$ up to higher-order terms. Therefore SGD with label noise implicitly regularizes the all-layer margin.
