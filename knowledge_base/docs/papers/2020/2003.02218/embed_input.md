<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Large Learning Rate Phase of Deep Learning: The Catapult Mechanism

Topics include Gradient descent, Neural networks, Deep learning, Online algorithms, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The choice of initial learning rate can have a profound effect on the performance of deep networks. We present a class of neural networks with solvable training dynamics, and confirm their predictions empirically in practical deep learning settings. The networks exhibit sharply distinct behaviors at small and large learning rates. The two regimes are separated by a phase transition. In the small learning rate phase, training can be understood using the existing theory of infinitely wide neural networks. At large learning rates the model captures qualitatively distinct phenomena, including the convergence of gradient descent dynamics to flatter minima. One key prediction of our model is a narrow range of large, stable learning rates. We find good agreement between our model's predictions and training dynamics in realistic deep learning settings. Furthermore, we find that the optimal performance in such settings is often found in the large learning rate phase. We believe our results shed light on characteristics of models trained at different learning rates. In particular, they fill a gap between existing wide neural network theory, and the nonlinear, large learning rate, training dynamics relevant to practice.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep learning has shown remarkable success across a variety of machine learning tasks. At the same time, our theoretical understanding of deep learning methods remains limited. In particular, the interplay between training dynamics, properties of the learned network, and generalization remains a largely open problem.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work we take a step toward addressing these questions. We present a dynamical mechanism that allows deep networks trained using SGD to find flat minima and achieve superior performance. Our theoretical predictions agree well with empirical results in a variety of deep learning settings. In many cases we are able to predict the regime of learning rates where optimal performance is achieved. Figure 1 summarizes our main results. This work builds on several existing results, which we now review.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

\begin{overpic}[width=216.81pt,trim=0.0pt 158.5925pt 0.0pt 0.0pt,clip]{figures/fig1.pdf} \put(-1.0,2.0){\small(a)} \end{overpic} \begin{overpic}[width=216.81pt,trim=0.0pt -5.01874pt 0.0pt 158.5925pt,clip]{figures/fig1.pdf} \put(-1.0,2.0){\small(b)} \end{overpic} Figure 1: A summary of our main results. (a) A visualization of gradient descent dynamics derived in our theoretical setup. A 2D slice of parameter space is shown, where lighter color indicates higher loss and dots represents points visited during optimization. Initially, the loss grows rapidly while local curvature decreases. Once curvature is sufficiently low, gradient descent converges to a flat minimum. We call this the catapult effect. See Figures 2 and S1 for more details. (b) Confirmation of our theoretical predictions in a practical deep learning setting.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Line shows the test accuracy of a Wide ResNet trained on CIFAR-10 as a function of learning rate, each trained for a fixed number of steps. Dashed lines show our predictions for the boundaries of the large learning rate regime (the catapult phase), where we expect optimal performance to occur. Maximal performance is achieved between the dashed lines, confirming our predictions. See Section 3 for details.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Large learning rate SGD improves generalization", "weight": 1.0} -->

SGD training with large initial learning rates often leads to improved performance over training with small initial learning rates (see Li et al.; Leclerc & Madry; Xie et al.; Frankle et al.; Jastrzebski et al. for recent discussions). It has been suggested that one of the mechanisms underlying the benefit of large learning rates is that noise from stochastic gradient descent leads to flat minima, and that flat minima generalize better than sharp minima (though see Dinh et al. for discussion of some caveats). According to this suggestion, training with a large learning rate (or with a small batch size) can improve performance because it leads to more stochasticity during training.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Large learning rate SGD improves generalization", "weight": 1.0} -->

We will develop a connection between large learning rate and flatness of minima in models trained via SGD. Unlike the relationship explored in most previous work though, this connection is not driven by SGD noise, but arises solely as a result of training with a large initial learning rate, and holds even for full batch gradient descent.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The existing theory of infinite width networks is insufficient to describe large learning rates", "weight": 1.0} -->

A recent body of work has investigated the gradient descent dynamics of deep networks in the limit of infinite width. Of particular relevance is the work by Jacot et al. showing that gradient flow in the space of functions is governed by a dynamical quantity called the Neural Tangent Kernel (NTK) which is fixed at its initial value in this limit. Lee et al. showed this result is equivalent to training the linearization of a model around its initialization in parameter space. Finally, moving away from the strict limit of infinite width by working perturbatively, Dyer & Gur-Ari; Huang & Yau introduced an approach to computing the finite-width corrections to network evolution.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The existing theory of infinite width networks is insufficient to describe large learning rates", "weight": 1.0} -->

Despite this progress, it seems these results are insufficient to capture the full dynamics of deep networks, as well as their superior performance, in regimes applicable to practice. Prior work has focused on comparisons between various infinite-width kernels associated with deep networks and their finite-width, SGD-trained counterparts. Specific findings vary depending on precise choices for architecture and hyperparameters. However, dramatic performance gaps are consistently observed between non-linear CNNs and their limiting kernels, implying that the theory is not sufficient to explain the performance of deep networks in this realistic setup. Furthermore, some hyperparameter settings in finite-width models have no known analogue in the infinite width limit, and it is these settings that often lead to optimal performance.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The existing theory of infinite width networks is insufficient to describe large learning rates", "weight": 1.0} -->

In particular, finite width networks are often trained with large learning rates that would cause divergence for infinite width linearized models. Further, these large learning rates cause finite width networks to converge to flat minima. For infinite width linearized models, trained with MSE loss, all minima have the same curvature, and the notion of flat minima does not apply. We argue that the reduction in curvature during optimization, and support for learning rates that are infeasible for infinite width linearized models, may thus partially explain performance gaps observed between linear and non-linear models.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Our contribution: three learning rate regimes", "weight": 1.0} -->

In this work, we identify a dynamical mechanism which enables finite-width networks to stably access large learning rates. We show that this mechanism causes training to converge to flatter minima and is associated with improved generalization. We further show that this same mechanism can describe the behavior of infinite width networks, if training time is increased along with network width.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Our contribution: three learning rate regimes", "weight": 1.0} -->

This new mechanism enables a characterization of gradient descent training in terms of three learning rate regimes, or phases: the lazy phase, the catapult phase, and the divergent phase. In Section 2 we analytically derive the behavior in these three learning rate regimes for one hidden layer linear networks with large but finite width, trained with MSE loss. We confirm experimentally in Section 3 that these phases also apply to deep nonlinear fully- connected, convolutional, and residual architectures. In Section 4 we study additional predictions of the analytic solution.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Our contribution: three learning rate regimes", "weight": 1.0} -->

We now summarize all three phases, using $\eta$ to indicate the learning rate, and $\lambda_{0}$ to indicate the initial curvature (defined precisely in Section 2.1). The phase is determined by the curvature at initialization and by the learning rate, despite the fact that the curvature may change significantly during training. Based on the experimental evidence we expect the behavior described below to apply in typical deep learning settings, when training sufficiently wide networks using SGD.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Lazy phase: $\\eta < {2/\\lambda_{0}}$", "weight": 1.0} -->

For sufficiently small learning rate, the curvature $\lambda_{t}$ at training step $t$ remains constant during the initial part of training. The model behaves (loosely) as a model linearized about its initial parameters; this becomes exact in the infinite width limit, where these dynamics are sometimes called *lazy training*. For a discussion of trainability and the connection to the NTK in the lazy phase see Xiao et al..

<!-- chunk {"id": "body-0016", "role": "body", "section": "Catapult phase: ${2/\\lambda_{0}} < \\eta < \\eta_{\\max}$", "weight": 1.0} -->

In this phase, the curvature at initialization is too high for training to converge to a nearby point, and the linear approximation quickly breaks down. Optimization begins with a period of exponential growth in the loss, coupled with a rapid decrease in curvature, until curvature stabilizes at a value $\lambda_{final} < {2/\eta}$. Once the curvature drops below $2/\eta$, training converges, ultimately reaching a minimum that is flatter than those found in the lazy phase. This initial period lasts for a number of training steps that is of order $\log{(n)}$, where $n$ is the network width, and is therefore quite short for realistic networks (often lasting less than a single epoch). Optimal performance is often achieved when the initial learning rate is in this range. The gradient descent dynamics in this phase are visualized in SM Figure S1 and in Figure 1.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Catapult phase: ${2/\\lambda_{0}} < \\eta < \\eta_{\\max}$", "weight": 1.0} -->

The maximum learning rate is approximately given by $\eta_{\max} = {c_{{act}.}/\lambda_{0}}$, where $c_{{act}.}$ is an architecture-dependent constant. Empirically, we find that this constant depends strongly on the non-linearity but only weakly on other aspects of the architecture. For networks with ReLU non-linearity we find empirically that $c_{{act}.} \approx 12$. For the theoretical model, we show that $c_{{act}.} = 4$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Divergent phase: $\\eta > \\eta_{\\max}$", "weight": 1.0} -->

When the learning rate is above the maximum learning rate of the model, the loss diverges and the model does not train.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Theoretical results", "weight": 1.0} -->

We now present our main theoretical result, an analysis of gradient descent dynamics for a neural network with large but finite width.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Theoretical results", "weight": 1.0} -->

Given a network function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ with model parameters $\theta \in {\mathbb{R}}^{p}$, and a training set ${\{{(x_{\alpha},y_{\alpha})}\}}_{\alpha = 1}^{m}$, the MSE loss is The NTK $\Theta:{{{\mathbb{R}}^{d} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}}$ is defined by We denote by $\lambda$ the maximum eigenvalue of the kernel. In large width models, $\lambda$ provides a local measure of the loss landscape curvature that is similar to the top eigenvalue of the Hessian.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Theoretical results", "weight": 1.0} -->

In this section, we will consider a network with one hidden layer and linear activations, where the network function $f$ is given by Here $n$ is the width (number of neurons in the hidden layer), $v \in {\mathbb{R}}^{n}$ and $u \in {\mathbb{R}}^{n \times d}$ are the model parameters (collectively denoted $\theta$), and $x \in {\mathbb{R}}^{d}$ is the training input. At initialization, the weights are drawn from $\mathcal{N}{}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Warmup: a simplified model", "weight": 1.0} -->

Before analyzing the dynamics of the model, we analyze a simpler setting which captures the most important aspects of the full solution. Consider a dataset with 1D inputs, and with a single training sample $x = 1$ with label $y = 0$. The network function evaluated on this input is then $f = {n^{- {1/2}}v^{T}u}$, with ${u,v} \in {\mathbb{R}}^{n}$, and the loss is $L = {f^{2}/2}$. The gradient descent equations at training step $t$ are Next, consider the update equations in function space. These can be written in terms of the Neural Tangent Kernel. For this model, the kernel evaluated on the training set is a scalar which is equal to $\lambda$, its top eigenvalue, and is given by At initialization, both $f^{2}$ and $\lambda$ scale as $n^{0} = 1$ with width. The following update equations for $f$ and $\lambda$ at step $t$ can be derived.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Warmup: a simplified model", "weight": 1.0} -->

It is important to note that these are the exact update equations for this model, and that no higher-order terms were neglected. We now analyze these dynamical equations assuming the width $n$ is large. Two learning rates that will be important in the analysis are $\eta_{crit} = {2/\lambda_{0}}$ and $\eta_{\max} = {4/\lambda_{0}}$. In terms of the notation introduced above, the architecture-dependent constant that determines that maximum learning rate in this model is $c_{{act}.} = 4$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Lazy phase", "weight": 1.0} -->

Taking the strict infinite width limit, equations and become When $\eta < \eta_{crit}$, $\lambda$ remains constant throughout training. This is a special case of NTK dynamics, where the kernel is constant and the network evolves as a linear model. The function and the loss both shrink to zero because the multiplicative factor obeys ${|{1 - {\eta\lambda_{t}}}|} < 1$. This convergence happens in ${\mathcal{O}{(n^{0})}} = {\mathcal{O}{}}$ steps.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Catapult phase", "weight": 1.0} -->

When $\eta_{crit} < \eta < \eta_{\max}$, the loss diverges in the infinite width limit. Indeed, from we see that the kernel is constant in the limit, while $f$ receives multiplicative updates where ${|{1 - {\eta\lambda_{t}}}|} > 1$. This is the well known instability of gradient descent dynamics for linear models with MSE loss. However, the underlying model is not linear in its parameters, and finite width contributions turn out to be important. We therefore relax the infinite width limit and analyze equations for large but finite width, $n \gg 1$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Catapult phase", "weight": 1.0} -->

First, note that ${{\eta\lambda_{0}} - 4} < 0$ by assumption, and therefore the (additive) kernel updates are negative for all $t$. During early training, $|f_{t}|$ grows (as in the infinite width limit) while $\lambda_{t}$ remains constant up to small $\mathcal{O}{(n^{- 1})}$ updates. After $t \sim {\log{(n)}}$ steps, $|f_{t}|$ grows to order $n^{1/2}$. At this point, the kernel updates are no longer negligible because $f_{t}^{2}/n$ is of order $n^{0}$. The kernel $\lambda_{t}$ receives negative, non-negligible updates while both $f_{t}$ and the loss continue to grow (for now, we ignore the term in with an explicit $1/n$ dependence).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Catapult phase", "weight": 1.0} -->

This continues until the kernel is sufficiently small that the condition ${\eta\lambda_{t}} \lesssim 2$ is met.^11^1The bound is not exact because of the term we neglected. We call this curvature-reduction effect the catapult effect. Beyond this point, ${|{1 - {\eta\lambda_{t}}}|} < 1$ holds, $|f_{t}|$ shrinks, and the loss converges to a global minimum. The $n$ dependence of the steps until optimization converges is $\log{(n)}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Catapult phase", "weight": 1.0} -->

It remains to show that the term in with an explicit $n^{- 1}$ dependence does not affect these conclusions. Once $|f_{t}|$ grows to order $n^{1/2}$, this term is no longer negligible and can cause the multiplicative factor in front of $f_{t}$ to become smaller than 1 in absolute value, causing $|f_{t}|$ to start shrinking. However, once $|f_{t}|$ shrinks sufficiently this term again becomes negligible. Therefore, the loss will not converge to zero unless the curvature eventually drops below $2/\eta$. Conversely, notice that this term cannot cause $|f_{t}|$ to diverge for learning rates below $\eta_{\max}$. Indeed, if this were to happen then equation would drive $\lambda_{t}$ to negative values, leading to a contradiction. This completes the analysis in this phase.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Catapult phase", "weight": 1.0} -->

Let us make a few comments about the catapult phase.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Catapult phase", "weight": 1.0} -->

It is important for the analysis that we take a modified large width limit, in which the number of training steps grows like $\log{(n)}$ as $n$ becomes large. This is different than the large width limit commonly studied in the literature, in which the number of steps is kept fixed as the width is taken large. When using this modified limit, the analysis above holds even in the limit. Note as well that the catapult effect takes place over $\log{(n)}$ steps, and for practical networks will occur within the first 100 steps or so of training.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Catapult phase", "weight": 1.0} -->

In the catapult phase, the kernel at the end of training is smaller by an order $n^{0}$ amount compared with its value at initialization. The kernel provides a local measure of the loss curvature. Therefore, the minima that SGD finds in the catapult phase are flatter than those it finds in the lazy phase. Contrast this situation, in which the kernel receives non-negligible updates, with the conclusions of Jacot et al. where the kernel is constant throughout training. The difference is due to the large learning rate, which leads to a breakdown of the linearized approximation even at large width.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Divergent phase", "weight": 1.0} -->

Completing the analysis of this model, when $\eta > \eta_{\max}$ the loss diverges because the kernel receives positive updates, accelerating the rate of growth of the function. Therefore, $\eta_{\max} = {4/\lambda_{0}}$ is the maximum learning rate of the model.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Full model", "weight": 1.0} -->

We now turn to analyzing the model presented at the beginning of this section, with $d$-dimensional inputs and $m$ training samples with general labels. The full analysis is presented in SM Section D.1; here we summarize the argument. The conclusions are essentially the same as those of the warmup model.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Full model", "weight": 1.0} -->

We introduce the notation $f_{\alpha}:={f{(x_{\alpha})}}$ for the function evaluated on a training sample, ${\overset{\sim}{f}}_{\alpha}:={f_{\alpha} - y_{\alpha}}$ for the error, and $\Theta_{\alpha\beta}:={\Theta{(x_{\alpha},x_{\beta})}}$ for the kernel elements. We will treat $f,\overset{\sim}{f}$ evaluated on the training set as vectors in ${\mathbb{R}}^{m}$, whose elements are $f_{\alpha},{\overset{\sim}{f}}_{\alpha}$. Consider the following update equation for the error, which can be derived from the update equations for the parameters. Note that this is the exact update equation for this model; no higher-order terms were neglected.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Full model", "weight": 1.0} -->

We again take the modified large width limit $n\rightarrow\infty$, allowing the number of steps to scale logarithmically in the width. At initialization, $f_{\alpha}$, ${\overset{\sim}{f}}_{\alpha}$, and $\Theta_{\alpha\beta}$ are all of order $n^{0}$. We now analyze the gradient descent dynamics as a function of the learning rate.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Full model", "weight": 1.0} -->

The maximum eigenvalue of the kernel at step $t$ is $\lambda_{t}$. When $\eta < \eta_{crit}$, the norm ${\|{\overset{\sim}{f}}^{t}\|}_{2}$ shrinks to zero in $\mathcal{O}{(n^{0})}$ time while the kernel receives $\mathcal{O}{(n^{- 1})}$ corrections. Therefore, in the limit the kernel remains constant until convergence. This is a special case of the NTK result, and the model evolves as a linear model.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Full model", "weight": 1.0} -->

We note in passing the similarity between these equations and,. We see that once ${\overset{\sim}{f}}^{\max}$ and $\zeta$ become of order $n^{1/2}$, $\lambda_{t}$ receives non-negligible negative corrections of order $n^{0}$. This evolution continues until $\lambda_{t} \lesssim {2/\eta}$, after which the error converges to zero. Finally, if $\eta > \eta_{\max}$, the error grows while $\lambda_{t}$ receives positive updates, and the loss diverges. This concludes the discussion of the theoretical model; further details can be found in Section 4 and in SM Section D.1.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experimental results", "weight": 1.0} -->

In this section we test the extent to which the behavior of our theoretical model describes the dynamics of deep networks in practical settings. The theoretical results of Section 2, describing distinct learning rate phases, are not guaranteed to hold beyond the model analyzed there. We treat these results as predictions to be tested empirically, including the values $\eta_{crit}$ and $\eta_{\max}$ of the learning rates that separate the three phases.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experimental results", "weight": 1.0} -->

In a variety of deep learning settings, we find clear evidence of the different phases predicted by the model. The experiments all use MSE loss, sufficiently wide networks, and SGD^22^2While our theoretical framework focused on (full-batch) gradient descent, we expect these the phases to happen at similar points for SGD as long as evolution is not noise dominated, in which case we expect all phases to be shifted towards smaller learning rates.. Parameters such as network architecture, choice of non-linearity, weight parameterization, and regularization, do not significantly affect this conclusion.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experimental results", "weight": 1.0} -->

In terms of the learning rates that determine the location of the transitions, the only modification needed to obtain good agreement with experiment is to replace the theoretical maximum learning rate, $4/\lambda_{0}$, with a 1-parameter function $\eta_{\max} = {c_{{act}.}/\lambda_{0}}$, where $c_{{act}.}$ is an architecture-dependent constant. We find that $c_{{act}.} \approx 12$ for all network that use ReLU non-linearity, and it seems this parameter depends only weakly on other details of the architecture. We find the level of agreement with the experiments surprising, given that our theoretical model involves a shallow network without non-linearities.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experimental results", "weight": 1.0} -->

Building on the observed correlation between lower curvature and generalization performance, we conjecture that optimal performance occurs in the large learning rate (catapult) phase, where the loss converges to a flatter minimum. For a fixed amount of computational budget, we find that this conjecture holds in all cases we tried. Even when comparing different learning rates trained for a fixed amount of *physical time* $t_{phys} = {t \cdot \eta}$, we find that performance of models trained in the catapult phase either matches or exceeds that of models trained in the lazy phase.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Early time curvature dynamics", "weight": 1.0} -->

Our theoretical model makes detailed predictions for the gradient descent evolution of $\lambda$, the top eigenvalue of the NTK. Here we test these predictions against empirical results in a variety of deep learning models (see the Supplement for additional experimental results).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Early time curvature dynamics", "weight": 1.0} -->

For learning rates $\eta < \eta_{crit}$, we find that $\lambda$ is independent of the learning rate and constant throughout training, as expected in the lazy phase. For $\eta_{crit} < \eta < {4/\lambda_{0}}$ we find that $\lambda$ decreases during training to below $2/\eta$, matching the predicted behavior in the catapult phase (note that in the Wide ResNet example, $\lambda$ initially increases before reaching its stable value).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Early time curvature dynamics", "weight": 1.0} -->

The large learning rate behavior predicted by the model appears to persist up to the maximum learning rate, which is larger in these experiments than in the theoretical model. In these and other experiments involving ReLU networks, we find that $\eta_{\max} \approx {12/\lambda_{0}}$ is a good predictor of the maximum learning rate (in the SM C.4 we discuss other nonlinearities). We conjecture that this is the typical maximum learning rate of networks with ReLU non-linearities.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Generalization performance", "weight": 1.0} -->

We now consider the performance of trained models in the different phases discussed in this work. Keskar et al. observed a correlation between the flatness of a minimum found by SGD and the generalization performance (see Jiang et al. for additional empirical confirmation of this correlation). In this work, we showed that the minima SGD finds are flatter in the catapult phase, as measured by the top kernel eigenvalue. Our measure of flatness differs from that of Keskar et al., but we expect that these measures are correlated.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Generalization performance", "weight": 1.0} -->

We therefore conjecture that optimal performance is often obtained for learning rates above $\eta_{crit}$ and below the maximum learning rate.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Generalization performance", "weight": 1.0} -->

In this section we test this conjecture empirically. We find that performance in the large learning rate range always matches or exceeds the performance when $\eta < \eta_{crit}$. For a fixed compute budget, we find that the best performance is always found in the catapult phase.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Generalization performance", "weight": 1.0} -->

Next, Figure 5 shows the performance of a convolutional network and a Wide ResNet (WRN) trained on CIFAR-10. The experimental setup, which we now describe, was chosen to ensure a fair comparison of the performance across different learning rates. The network is trained with different initial learning rates, followed by a decay at a fixed physical time $t \cdot \eta$ to the same final learning rate. This schedule is introduced in order to ensure that all experiments have the same level of SGD noise toward the end of training.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Generalization performance", "weight": 1.0} -->

We present results using two different stopping conditions. In Figure 5a, 5c, all models were trained for a fixed number of training steps. We find a significant performance gap between small and large learning rates, with the optimal learning rate above $\eta_{crit}$ and close to $\eta_{\max}$. Beyond this learning rate, performance drops sharply.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Generalization performance", "weight": 1.0} -->

The fixed compute stopping condition, while of practical interest, biases the results in favor of large learning rates. Indeed, in the limit of small learning rate, training for a fixed number of steps will keep the model close to initialization. To control for this, in Figure 5b,5d models were trained for the same amount of physical time $t \cdot \eta$. For the CNN of figure 5b, decaying the learning rate does not have a significant effect on performance and we observe that performance is flat up to $\eta_{\max}$, and there is no correlation between our measure of curvature and generalization performance. Figure 5d shows the analogous experiment for WRN. When decaying the learning rate toward the end of training to control for SGD noise, we find that optimal performance is achieved above $\eta_{crit}$. In all these cases, $\eta_{\max}$ is a good predictor of the maximal learning rate, despite significant differences in the architectures.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Generalization performance", "weight": 1.0} -->

Notice that by tuning the learning rate to the catapult phase, we are able to achieve performance using MSE loss, and without momentum, that is competitive with the best reported results for this model.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Generalization performance", "weight": 1.0} -->

In SM B.1, we present additional results for WRN on CIFAR-100, with similar conclusions as those for WRN on CIFAR-10.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Additional properties of the model", "weight": 1.0} -->

So far we have focused on the generalization performance and curvature of the large learning rate phase. Here we investigate additional predictions made by our model.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Restoration of linear dynamics", "weight": 1.0} -->

One striking prediction of the model is that after a period of excursion, the logit differences settle back to $\mathcal{O}{}$ values, the NTK stops changing, and evolution is again well approximated by a linear model with constant kernel at large width.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Restoration of linear dynamics", "weight": 1.0} -->

We speculate that the return to linearity and constancy of the kernel may hold asymptotically in width for more general models for a range of learning rates above $\eta_{crit}$. We test this by evolving the model for order $\log{(n)}$ steps until the catapult effect is over, linearizing the model, and comparing the evolution of the two models beyond this point. Figure 6 shows an example of this. At fixed width, the accuracy of the linear and non-linear networks match for a range of learning rates above the transition up to $4/\lambda_{0}$. We present additional evidence for this asymptotic linearization behavior in the Supplement.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Non-perturbative phase transition", "weight": 1.0} -->

The large width analysis of the small learning rate phase has been the subject of much work. In this phase, at infinite width, the network map evolves as a linear random features model, $f_{t + 1}^{} = {f_{t}^{} - {\Thetaf_{t}^{}}}$, where $f^{}$ is the function of the linearized model. At large but finite width, corrections to this linear evolution can be systematically incorporated via a perturbative expansion (Taylor expansion) around infinite width.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Non-perturbative phase transition", "weight": 1.0} -->

The evolution equations and of the solvable model are an example of this. At large width and in the small learning rate phase, the $O{(n^{- 1})}$ terms are suppressed for all times. In contrast, the leading order dynamics of $f_{t}^{}$ diverge when $\eta > \eta_{crit}$, and so the true evolution cannot be described by the linear model. Indeed, the logits grow to $\mathcal{O}{(n^{1/2})}$ and thus all terms in and are of the same order. Similarly, the growth observed empirically in the catapult phase for more general models cannot be described by truncating the series at any order, because the terms all become comparable.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this work we took a step toward understanding the role of large learning rates in deep learning. We presented a dynamical mechanism that allows deep networks to be trained at larger learning rates than those accessible to their linear counterparts. For MSE loss, linear model training diverges when the learning rate is above the critical value $\eta_{crit} = {2/\lambda_{0}}$, where $\lambda_{0}$ is the curvature at initialization. We showed that deep networks can train for larger learning rates by navigating to an area of the landscape that has sufficiently low curvature. Perhaps counterintuitively, training in this regime involves an initial period during which the loss increases before converging to its final, small value. We call this the catapult effect.

<!-- chunk {"id": "body-0059", "role": "body", "section": "A tractable model illustrating catapult dynamics", "weight": 1.0} -->

These observations are made concrete in our theoretical model, where we fully analyze the gradient descent dynamics as a function of the learning rate. The analysis involves a modified large width limit, in which both the width and training time are taken to be large. Sweeping the learning rate from small to large, and working in the limit, we find sharp transitions from a lazy phase where linearized model training is stable, to a catapult phase in which only the full model converges, and finally to a divergent phase in which training is unstable. These transitions have the hallmarks of phase transitions that commonly appear in physical systems such as ferromagnets or water, as one changes parameters such as temperature. In particular, these transitions are non-perturbative: a Taylor series expansion of the linearized model that takes into account finite width corrections is not sufficient to describe the behavior beyond the critical learning rate.

<!-- chunk {"id": "body-0060", "role": "body", "section": "A tractable model illustrating catapult dynamics", "weight": 1.0} -->

We derive the learning rates at which these transitions occur as a function of the curvature at initialization. We then treat these theoretical results as predictions, to be tested beyond the regime where they are guaranteed to hold, and find good quantitative agreement with empirical results across a variety of realistic deep learning settings.

<!-- chunk {"id": "body-0061", "role": "body", "section": "A tractable model illustrating catapult dynamics", "weight": 1.0} -->

We find it striking that a relatively simple theoretical model can correctly predict the behavior of realistic deep learning models. In particular, we conjecture that the maximum learning rate is typically a simple function of the curvature at initialization, with a single parameter $c_{{act}.}$ that seems to depend only on the non-linearity. For ReLU networks, we conjecture that the maximum learning rate is approximately $12/\lambda_{0}$, which we confirm in many cases.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Reducing misalignment of activations and gradients", "weight": 1.0} -->

The catapult dynamics for the simplified model in Section 2.1 reduce curvature by shrinking the component of the first layer weights $u$ which is orthogonal to the second layer weights $v$, and shrinking the component of the second layer weights $v$ which is orthogonal to the first layer weights $u$. We can rewrite the simplified model in terms of a hidden layer $h = {ux}$, where ${f{(x)}} = {n^{- {1/2}}v^{\top}h}$. The gradient with respect to this hidden layer is $\frac{\partial L}{\partial h} = {n^{- {1/2}}f{(x)}v}$. These hidden layer gradients $\frac{\partial L}{\partial h}$ thus point in the same direction as $v$, while the hidden activations $h$ point in the same direction as $u$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Reducing misalignment of activations and gradients", "weight": 1.0} -->

An alternative interpretation of the catapult dynamics is then that they reduce the components of $h$ and $\frac{\partial L}{\partial h}$ which are orthogonal to each other. The catapult dynamics thus serve, in this simplified model, to reduce the misalignment between feedforward activations $h$, and backpropagated gradients $\frac{\partial L}{\partial h}$. We hypothesize that this reduction of misalignment between activations and gradients may be a feature of large learning rates and catapult dynamics in deep, as well as shallow, networks. We further hypothesize that it may play a directly beneficial role in generalization, for instance by making the model output less sensitive to orthogonal, out-of-distribution, perturbations of activations.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Catapult dynamics often improve generalization", "weight": 1.0} -->

Our results shed light on the regularizing effect of training at large learning rates. The effect presented here is independent of the regularizing effect of stochastic gradient noise, which has been studied extensively. Building on previous works, we noted the observed correlation between flatness and generalization performance. Based on these observations, we expect the optimal performance to often occur for learning rates larger than $\eta_{crit}$, where the linearized model is unstable. Observing this effect required controlling for several confounding factors that affect the comparison of performance between different learning rates. Under a fair comparison, and also for a fixed compute budget, we find that this expectation holds in practice.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Beyond infinite linear models", "weight": 1.0} -->

One outcome of our work is to address the performance gap between ordinary neural networks, and linear models inspired by the theory of wide networks. Optimal performance is often obtained at large learning rates which are inaccessible to linearized models. In such cases, we expect the performance gap to persist even at arbitrarily large widths. We hope our work can further improve the understanding of deep learning methods.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Other open questions", "weight": 1.0} -->

There are several remaining open questions. While the model predicts a maximum learning rate of $4/\lambda_{0}$, for models with ReLU activations we find that the maximum learning rate is consistently higher. This may be due to a separate dynamical curvature-reduction mechanism that relies on ReLU. In addition, we do not explore the degree to which our results extend to softmax classification. While we expect qualitatively similar behavior there, the non-constant Hessian of the softmax cross entropy makes controlled experiments more challenging. Similarly, behavior for other optimizers such as SGD with momentum may differ. For example, the maximum learning rate when training a linear model is larger for gradient descent with momentum than for vanilla gradient descent, and therefore the transition to the catapult phase (if it exists) will occur at a higher learning rate. We leave these questions to future work.
