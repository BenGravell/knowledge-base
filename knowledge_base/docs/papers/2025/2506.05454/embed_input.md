<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Zeroth-Order Optimization Finds Flat Minima

Topics include Reinforcement learning, Language models, Classification, Optimization, Learning, TRACE.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Zeroth-order methods are extensively used in machine learning applications where gradients are infeasible or expensive to compute, such as black-box attacks, reinforcement learning, and language model fine-tuning. Existing optimization theory focuses on convergence to an arbitrary stationary point, but less is known on the implicit regularization that provides a fine-grained characterization on which particular solutions are finally reached. We show that zeroth-order optimization with the standard two-point estimator favors solutions with small trace of Hessian, which is widely used in previous work to distinguish between sharp and flat minima. We further provide convergence rates of zeroth-order optimization to approximate flat minima for convex and sufficiently smooth functions, where flat minima are defined as the minimizers that achieve the smallest trace of Hessian among all optimal solutions. Experiments on binary classification tasks with convex losses and language model fine-tuning support our theoretical findings.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are many emerging machine learning problems where gradients are not accessible or expensive to compute, hindering the application of gradient-based optimization algorithms. For example, fine-tuning large language models (LLMs), particularly at the scale of billions of parameters, faces significant memory bottlenecks, primarily because of the memory-intensive nature of backpropagation. Zeroth-order optimization offers a compelling alternative as it permits gradient estimation via finite differences of loss values. Malladi et al. reported that zeroth-order methods are capable of fine-tuning a 30-billion-parameter model using a single A100 GPU with 80 GiB memory, whereas gradient-based methods require 8 A100s. In addition to recent advances in fine-tuning LLMs, zeroth-order methods have also found numerous applications in black-box settings and nonsmooth optimization where gradient computation is often infeasible. They have further proven effective in reinforcement learning and distributed learning to reduce computation and communication costs.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To be more specific, for the optimization problem $\min_{x\in\mathbb{R}^{d}}f(x)$ with parameters $x\in\mathbb{R}^{d}$ and a loss function $f:\mathbb{R}^{d}\rightarrow\mathbb{R}$, zeroth-order optimization with the standard two-point gradient estimator (Algorithm 1) iteratively updates $x$ by substituting the computationally intractable gradient with where $u\sim\mathcal{N}(0,\mathrm{I}_{d})$ is a standard Gaussian random vector and $\lambda\in\mathbb{R}$ is a smoothing parameter. It is convenient to understand zeroth-order methods through a surrogate smoothed function defined as $f_{\lambda}(x):=\mathbb{E}_{u\sim\mathcal{N}(0,\mathrm{I}_{d})}[f(x+\lambda u)]$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since Eq. unbiasedly estimates the gradient of $f_{\lambda}(x)$, i.e., $\mathbb{E}[g_{\lambda}(x,u)]=\nabla f_{\lambda}(x)$, standard convergence analyses directly indicate that $f_{\lambda}(x)$ is minimized. Further noting that $f_{\lambda}(x)$ is close to $f(x)$ when $\lambda$ is small, the convergence of zeroth-order optimization can be established on the original loss $f(x)$. For example, when $f(x)$ is smooth and convex, zeroth-order methods guarantee that the average of the iterates, $\bar{x}_{T}$, after $T$ iterations satisfy $\mathbb{E}[f(\bar{x}_{T})-\min_{x\in\mathbb{R}^{d}}f(x)]\leq\mathcal{O}(d/T)$; see e.g.,.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, in the presence of multiple solutions, it remains unclear from the above arguments whether zeroth-order methods prefer certain minima. Our intuition to this question comes from revisiting the underexplored role of $f_{\lambda}(x)$. Using Taylor's theorem (with details in Eq.), one can find that This implies that zeroth-order optimization implicitly encodes an additive regularizer using the trace of Hessian, which is a widely adopted metric in the literature to differentiate sharp and flat minima. Existing works studying flat minima mostly centered around first-order methods. The work of empirically demonstrated that stochastic gradient descent (SGD) converges to solutions with small expected sharpness $\mathbb{E}_{u\sim\mathcal{N}(0,\mathrm{I}_{d})}[f(x+\lambda u)]-f(x)$ on a variety of vision tasks, which also implies small trace of Hessian according to Eq.. It was also shown that SGD with label noise provably decreases trace of Hessian as a regularization term for overparameterized models.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Wen et al. proved that sharpness-aware minimization (SAM), a method specifically designed for finding flat minima, minimizes trace of Hessian when the batch size is one. Further discussions on the relevance of flat minima, as well as the role of the trace of Hessian can be found in the recent work.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work formalizes the intuition above and initiates the study of the implicit regularization of zeroth-order optimization with the standard two-point estimator. Despite relying only on function evaluations of $f(x)$, we show that zeroth-order optimization converges to flat minima, which are typically characterized using second-order information such as the Hessian matrix $\nabla^{2}f(x)$. In particular, our contributions are summarized below. $\bullet$ We define flat minima as the minimizers that achieve the smallest trace of Hessian over the set of all minimizers; see Definition 3.1. ‣ 3 Complexity for Finding Flat Minima ‣ Zeroth-Order Optimization Finds Flat Minima"). Assuming the function is convex and three times continuously differentiable with Lipschitz-continuous gradient, Hessian, and third derivatives (Assumptions 3.3. ‣ 3 Complexity for Finding Flat Minima ‣ Zeroth-Order Optimization Finds Flat Minima") and 3.4.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

‣ 3 Complexity for Finding Flat Minima ‣ Zeroth-Order Optimization Finds Flat Minima")), we prove that zeroth-order optimization with the standard two-point estimator (Algorithm 1) converges to $(\mathcal{O}(\epsilon/d^{2}),\epsilon)$-approximate flat minima, defined in Definition 3.2. ‣ 3 Complexity for Finding Flat Minima ‣ Zeroth-Order Optimization Finds Flat Minima"), after $T=\mathcal{O}(d^{4}/\epsilon^{2})$ iterations; see Corollary 2. ‣ 3.1 Convergence Analysis ‣ 3 Complexity for Finding Flat Minima ‣ Zeroth-Order Optimization Finds Flat Minima").

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

While standard convergence analysis directly treats $\lambda^{2}\textnormal{Tr}(\nabla^{2}f(x))$ as a bias term and controls it by choosing a sufficiently small $\lambda$, we provide a tighter and novel characterization in Section 3.1 of zeroth-order update dynamics to analyze convergence of $F(x):=f(x)+(\lambda^{2}/2)\textnormal{Tr}(\nabla^{2}f(x))$. This result is of independent and broader interest for advancing the understanding of zeroth-order optimization and naturally extends to analyzing convergence rates of first-order methods such as SAM and SGD on the smoothed loss towards flat minima (Remark 3.4). $\bullet$ We provide empirical evaluations to examine the behavior of the trace of Hessian under zeroth-order optimization across three settings: a test function (Figure 1), binary classification tasks using overparameterized SVMs and logistic regression (Figure 2), and language model fine-tuning tasks with RoBERTa (Figure 3).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consistent with our theoretical predictions, we observe that the trace of Hessian decreases when using zeroth-order optimization across all these settings. Note that we adopt an estimation of the trace of Hessian on language models for scalability purposes.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

To the best of our knowledge, this is the first work to prove that zeroth-order optimization converges to flat minima. Note that all results provided in this paper can be readily extended to zeroth-order optimization with other unbiased estimators of $\nabla f_{\lambda}(x)$ satisfying $\mathbb{E}[uu^{\top}]=\mathrm{I}_{d}$ such that Eq. holds, including the one-point estimator suggested, as well as gradient estimation using random vectors uniformly distributed on the Euclidean sphere.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Related Works", "weight": 1.0} -->

Zeroth-Order Optimization. Existing works primarily focused on convergence to a stationary point, while we prove the first result on convergence to flat minima. The development and early advances of zeroth-order optimization can be found. Nesterov and Spokoiny provided a convergence analysis of zeroth-order optimization across various settings. Their results for nonsmooth convex functions were refined, while improvements for nonsmooth nonconvex functions were made. Extensions to the stochastic setting were considered. Lower bounds were also provided, showing that the dimension dependence in the convergence guarantees of zeroth-order optimization is unavoidable without additional assumptions. Several recent works proved that such dimension dependence can be relaxed to a quantity related to the trace of Hessian. Zeroth-order optimization has been extended to minimax optimization, bilevel optimization, constrained optimization, and Riemannian optimization. It has also been integrated with coordinate descent, conditional gradient descent, SignSGD, and variance reduction techniques. A line of work established convergence to second-order stationary points, demonstrating that zeroth-order methods can also escape saddle points. The noisy function evaluation setting was studied, where higher-order smoothness assumptions were used to reduce bias in gradient estimates.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Related Works", "weight": 1.0} -->

The capability of zeroth-order methods for fine-tuning LLMs was first demonstrated by Malladi et al.. Following this work, several recent studies have introduced various improvements aimed at enhancing runtime efficiency and performance, including momentum, variance reduction, sparsification, use of Hessian information, and better sampling strategies.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Related Works", "weight": 1.0} -->

Sharpness-Aware Minimization. Prior studies of flat minima have mostly centered on first-order methods. Algorithms designed to find flat minima have achieved strong empirical success, including Entropy-SGD, stochastic weight averaging, and sharpness-aware minimization (SAM). Similar methods to SAM were proposed, and their efficiency and performance were further enhanced in e.g.,. Also inspired by the insights in Eq., Zhang et al. proposed a gradient-based method that effectively minimizes the smoothed loss. Several recent studies proposed modifying zeroth-order optimization and combining it with principles from SAM to explicitly promote flat minima. In contrast, our work focuses on understanding the implicit regularization effects inherent within the standard zeroth-order optimization. In addition to the trace of Hessian used in this work, other notions of sharpness have also been studied in the literature. One such example is the largest eigenvalue of the Hessian matrix, which has been shown to be implicitly penalized by (S)GD with large learning rates and SAM. Li et al. proved that SAM implicitly promotes balanced solutions on scale-invariant problems.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Related Works", "weight": 1.0} -->

A sharpness measure based on the largest gradient norm in a local neighborhood was proposed. Recently, Ahn et al. provided a formal definition of flat minima and studied the convergence complexity of finding them. A local concept of flat minima was used, defining them as local minima that are also stationary points of the trace of Hessian evaluated at limit points under gradient flow. Two gradient-based algorithms were proposed with convergence guarantees to flat local minima under the assumptions that the loss function is four times continuously differentiable, satisfies the local PL condition, and has a twice Lipschitz limit map under gradient flow. In this work, we adopt a global notion of flat minima and assume convexity of the function to show that zeroth-order optimization with the two-point estimator converges to flat global minima.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Related Works", "weight": 1.0} -->

0: Initialization x0 ∈ ℝd, number of iterations T, stepsize η > 0, smoothing parameter λ > 0. 2: Sample ut uniformly from the standard multivariate Gaussian distribution 𝒩(0, Id). 3: Construct the two-point gradient estimator $$g_{\lambda}(x_{t},u_{t})=\frac{f(x_{t}+\lambda u_{t})-f(x_{t}-\lambda u_{t})}{2\lambda}u_{t}.$$ 4: Update the parameter 4: xτ for τ sampled uniformly at random from {0, 1, ⋯, T − 1}. Algorithm 1 Zeroth-Order Optimization with the Two-Point Estimator

<!-- chunk {"id": "body-0018", "role": "body", "section": "Warm-up: Sharpness as Implicit Regularization", "weight": 1.0} -->

Throughout this paper, zeroth-order optimization refers specifically to the method described in Algorithm 1. As the two-point estimator in Eq. is an unbiased gradient estimator for the smoothed function $f_{\lambda}(x)=\mathbb{E}_{u\sim\mathcal{N}(0,\mathrm{I}_{d})}[f(x+\lambda u)]$, zeroth-order optimization directly minimizes $f_{\lambda}(x)$. Let $f(x)$ be twice continuously differentiable. By Taylor's theorem, we have that Taking expectation w.r.t. $u\sim\mathcal{N}(0,\mathrm{I}_{d})$, we obtain that The results suggest that the smoothed function introduces trace of Hessian as an additional regularization term. In the literature for sharpness-aware minimization, the trace of Hessian is often used to measure the sharpness of the solution.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Warm-up: Sharpness as Implicit Regularization", "weight": 1.0} -->

Recall that $\mathbb{E}[g_{\lambda}(x,u)]=\nabla f_{\lambda}(x)$, and thus zeroth-order optimization implicitly minimizes sharpness: This holds for any twice continuously differentiable function without further assumptions. It can be readily deduced from Eq. that when $x_{t}$ is close to optimal, i.e., with small gradient, the iterates move in expectation towards a direction that reduces trace of Hessian. Before formally establishing that Eq. leads to flat minima, we first illustrate this intuition through a concrete example.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 2.1", "weight": 1.0} -->

Consider the function $h(x)=(y^{\top}z-1)^{2}/2$, where $x=(y^{\top},z^{\top})^{\top}\in\mathbb{R}^{2d}$ for $y,z\in\mathbb{R}^{d}$. The optimal value is achieved when $y^{\top}z=1$, and the trace of Hessian is $\lVert y\rVert^{2}+\lVert z\rVert^{2}$. Among all optimal solutions, the smallest trace of Hessian is achieved when $y=z$ and $\lVert y\rVert=1$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Complexity for Finding Flat Minima", "weight": 1.0} -->

To formally study the convergence complexity of zeroth-order optimization with the two-point estimator towards flat minima, we first define the notion of flat minima that we are interested.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 3.3 (Smoothness)", "weight": 1.0} -->

We assume the function $f(x)$ is three times continuously differentiable and satisfies that $(a)$ $f(x)$ is $L_{1}$-smooth; $(b)$ $f(x)$ is second-order smooth with $L_{2}>0$, which implies that all third-order partial derivatives are bounded: $\lvert\partial^{3}f(x)/\partial x_{i}\partial x_{j}\partial x_{k}\rvert\leq L_{2}$, $\forall i,j,k\in[d]$ and $\forall x\in\mathbb{R}^{d}$; and, $(c)$ $f(x)$ is third-order smooth with $L_{3}>0$, which implies that $\forall x,y\in\mathbb{R}^{d}$, where

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 3.3 (Smoothness)", "weight": 1.0} -->

Since the characterization of flat minima already involves second-order information of $f(x)$, it is natural to require assumptions on higher-order information to establish convergence guarantees. Higher-order smoothness assumptions have been widely used to establish fast convergence rates, guarantee convergence to second-order stationary points, analyze implicit regularization, and study the complexity of finding flat minima. We emphasize that these assumptions on higher-order information are used solely for convergence analysis; Algorithm 1 requires only zeroth-order information. In order to prove global convergence, we also need the following convexity assumption. Although $f(x)$ is convex, $\textnormal{Tr}(\nabla^{2}f(x))$ is in general nonconvex. Seeking flat minima with lowest $\textnormal{Tr}(\nabla^{2}f(x))$ in the set of minimizers $\mathcal{X}^{*}$ is therefore a challenging task.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 3.4 (Convexity)", "weight": 1.0} -->

The function $f(x)$ is convex on $\mathbb{R}^{d}$, and thus $\textnormal{Tr}(\nabla^{2}f(x))\geq 0$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

We start with a brief recap of standard convergence analysis for zeroth-order optimization. We then explain the major theoretical contribution in this paper that leads to convergence towards flat minima. By the zeroth-order updates in Algorithm 1, we have that $\forall x\in\mathbb{R}^{d}$, Here, we use $\mathbb{E}[g_{\lambda}(x_{t},u_{t})]=\nabla f_{\lambda}(x_{t})$ and the property that $f_{\lambda}(x)$ is convex when $f(x)$ is convex. Standard analysis considers optimizing $f(x)$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

By selecting $x$ as one minimizer from the set $\mathcal{X}^{*}$ and setting $\eta=\mathcal{O}(1/d)$, we can rearrange Eq. to obtain Summing up from $t=0$ to $t=T-1$ and averaging by $T$ give $\mathbb{E}[f(\bar{x}_{T})-\min_{x\in\mathbb{R}^{d}}f(x)]\leq\mathcal{O}(d/T)$ with a small enough $\lambda$, where $\bar{x}_{T}$ is the average of iterates.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

Going beyond the classical analysis and targeting at flat minima, we take inspiration from Eq. and instead focus on the regularized loss In this way, we do not treat $\textnormal{Tr}(\nabla^{2}f(x))$ as a bias to be controlled but instead view the term as an objective to be optimized. Indeed, the $\mathcal{O}(\lambda^{2})$ error term in the standard analysis mostly comes from bounding $\lambda^{2}\textnormal{Tr}(\nabla^{2}f(x))$ from above by $\lambda^{2}L_{1}d$ when $f(x)$ is $L_{1}$-smooth.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

To proceed, we need to control the difference between $F(x)$ and $f_{\lambda}(x)$, as well as to bound $\mathbb{E}\lVert g_{\lambda}(x_{t},u_{t})\rVert^{2}$ by the term $\lVert\nabla F(x)\rVert^{2}$ to establish convergence on $F(x)$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

Our convergence guarantees require that $f(x)$ is three times continuously differentiable and satisfies first-, second-, and third-order smoothness assumptions. In Appendix C, we explain how the first- and third-order smoothness assumptions can be relaxed, at the cost of slower convergence rates; see Table 1 for a summary.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

We focus on the convex setting in this work, but the analysis extends to cases where the objective is locally convex in a neighborhood. When initialized in this region, zeroth-order optimization identifies local minima with the smallest trace of Hessian among all local minimizers in the neighborhood. When $f(x)$ is generally nonconvex, the current definition of flat minima is not theoretically tractable without additional assumptions. We leave for future work a detailed study on the definition of computationally feasible flat minima and the assumptions required to understand the complexity of finding them in the nonconvex setting.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

Our proof framework can be extended to understand the complexity of first-order methods towards flat minima. For example, a gradient-based method, $x_{t+1}\leftarrow x_{t}-\eta\nabla f(x_{t}+\lambda u_{t})$ with $u_{t}\sim\mathcal{N}(0,\mathrm{I}_{d})$, that uses a gradient evaluated at the perturbed point as the descent direction also minimizes the smoothed loss $f_{\lambda}(x)$ in the expectation. By upper bounding $\mathbb{E}\lVert\nabla f(x+\lambda u)\rVert^{2}$ with the term $\lVert\nabla F(x)\rVert^{2}$, convergence guarantees on $F(x)$ and thus to flat minima can be established. The same framework provides new insights on how SAM can be analyzed as well. Our primary focus is on zeroth-order methods, and extensions to first-order methods are deferred to future.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

We provide empirical results on binary classification tasks with convex losses and language model fine-tuning tasks. Our code is available at Binary Classification with SVMs and Logistic Regression. We start empirical evaluations using support vector machines (SVMs) and logistic regression. Given a training dataset $\{a_{i},b_{i}\}_{i=1}^{N}$ with feature vectors $a_{i}\in\mathbb{R}^{d}$ and binary labels $b_{i}$, we consider an overparameterized regime where each $a_{i}\in\mathbb{R}^{d}$ is mapped to $\phi(a_{i})=Wa_{i}\in\mathbb{R}^{D}$ via a random matrix $W\in\mathbb{R}^{D\times d}$ with $W_{ij}\sim\mathcal{N}$ and $D>N>d$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

We use two standard binary classification benchmarks from the LIBSVM library: a5a ($N=6,414$, $d=123$) and w5a ($N=9,888$, $d=300$), and set $D=10,000$ to overparameterize. This ensures a higher-dimensional solution set with increased diversity, enabling a meaningful study of implicit regularization to investigate the solutions selected by the algorithm. We consider SVMs with the squared hinge loss and $b_{i}\in\{-1,1\}$, that is, For $\sigma(z)=1/(1+\exp(-z))$ and $b_{i}\in\{0,1\}$, logistic regression minimizes the loss These two models can be viewed as linear probing on a two‐layer neural network with a frozen first layer and an identity activation. In the SVMs case, the second layer uses an identity activation and is trained with the squared hinge loss, while logistic regression applies a sigmoid activation and minimizes the cross‐entropy loss.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

Both SVMs and logistic regression have convex objective functions, and the trace of Hessian can be efficiently computed. Figure 2 shows the optimization trajectories of gradient descent and zeroth-order optimization. In all cases, gradient descent and zeroth-order optimization achieve comparable training loss and test accuracy; however, zeroth-order optimization consistently reduces the trace of Hessian and converges to flatter solutions. Detailed experimental setups and additional results can be found in Appendix D.2.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

Fine-Tuning Language Models on Text Classification Tasks. We also evaluate the behaviors of zeroth-order optimization on nonconvex language model fine-tuning tasks. Following Malladi et al., we consider few-shot fine-tuning on RoBERTa-Large (355M parameters) with $K=32$ and $K=256$ examples per class on three sentence classification datasets: SST-2 and SST-5 for sentiment classification, and TREC for topic classification. All experiments are tested on a single NVIDIA H100 GPU with 80 GiB memory. To mitigate the effect of mini-batch noise on reducing the trace of Hessian, we use full-batch training for both gradient descent and zeroth-order optimization, which is feasible in the few-shot setting.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

As the exact computation of the trace of Hessian is intractable due to the large model size, we adopt the widely-used expected sharpness $(2/\delta^{2})\lvert\mathbb{E}_{u\sim\mathcal{N}(0,\mathrm{I}_{d})}[f(x+\delta u)]-f(x)\rvert$ as an approximation, where $f(x)$ denotes the training loss evaluated at model weights $x\in\mathbb{R}^{d}$. We set $\delta=10^{-4}$ and estimate the expectation by averaging over 100 samples. The performance of gradient descent and zeroth-order optimization is presented in Figure 3. In this setting, both methods are observed to decrease the trace of Hessian. It is conjectured that the behavior in gradient descent results from the implicit regularization associated with large learning rates. Meanwhile, the observed decrease in zeroth-order optimization matches our theoretical insights. Detailed setups and additional results are deferred to Appendix D.3.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

In classical optimization theory, the convergence rates of zeroth-order methods scale with the dimension $d$, limiting their applicability to problems with large $d$ such as language model fine-tuning. Previous work explaining why zeroth-order methods still achieve reasonable performance on language model fine-tuning tasks has relaxed the dependence on $d$ to a term related to the trace of Hessian, $\textnormal{Tr}(\nabla^{2}f(x))$. Assuming $\textnormal{Tr}(\nabla^{2}f(x))\ll dL_{1}$ when $f(x)$ is $L_{1}$-smooth, zeroth-order optimization achieves dimension-independent rates and remains effective even in high-dimensional settings. Our experimental results show that the trace of Hessian decreases and attains values much smaller than the actual dimension, thereby supporting the assumption made in prior work to explain the empirical success of zeroth-order optimization.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Motivated by the observation that zeroth-order optimization with the two-point estimator (Algorithm 1) inherently minimizes $\textnormal{Tr}(\nabla^{2}f(x))$, we initiate a formal study of this implicit regularization. Specifically, we analyze its convergence to flat minima, defined as the ones with the lowest trace of Hessian among all minimizers. For convex and sufficiently smooth (Assumptions 3.3. ‣ 3 Complexity for Finding Flat Minima ‣ Zeroth-Order Optimization Finds Flat Minima")) functions, we prove that Algorithm 1 guarantees $(\mathcal{O}(\epsilon/d^{2}),\epsilon)$-approximate flat minima (Definition 3.2. ‣ 3 Complexity for Finding Flat Minima ‣ Zeroth-Order Optimization Finds Flat Minima")) after $T=\mathcal{O}(d^{4}/\epsilon^{2})$ iterations. This is the first work showing that zeroth-order optimization converges to flat minima.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Experiments on binary classification tasks using SVMs and logistic regression, as well as language model fine-tuning tasks on RoBERTa support our theoretical findings.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Theoretical and empirical performance of zeroth-order methods is often limited by the high variance in gradient estimation. A promising direction is to combine zeroth-order and first-order methods to leverage the strengths of both. We only examine zeroth-order optimization using the standard two-point estimator. Exploring whether the convergence complexity can be further improved with possible modifications and additional algorithmic designs remains an interesting line of work. The current theoretical results require convexity and higher-order smoothness assumptions of the function. Investigation into nonconvex functions with relaxed assumptions is left for future work.
