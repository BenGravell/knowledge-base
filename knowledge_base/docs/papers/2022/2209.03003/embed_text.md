## Introduction

Compared with supervised learning, the shared difficulty of various forms of unsupervised learning is the lack of *paired* input/output data with which standard regression or classification tasks can be invoked. The gist of most unsupervised methods is to find, in one way or another, meaningful correspondences between points from two distributions. For example, generative models such as generative adversarial networks (GAN) and variational autoencoders (VAE) \e.g., seek to map data points to latent codes following a simple elementary (Gaussian) distribution with which the data can be generated and manipulated. Representation learning rests on the idea that if a sufficiently smooth function can map a structured data distribution to an elementary distribution, it can (likely) be endowed with certain semantically meaningful interpretation and useful for various downstream learning tasks. On the other hand, domain transfer methods find mappings to transfer points from two different data distributions, both observed empirically, for the purpose of image-to-image translation, style transfer, and domain adaption \e.g.,. All these tasks can be framed unifiedly as finding a transport map between two distributions:

The Transport Mapping Problem *Given empirical observations of two distributions ${X_{0} \sim \pi_{0}},{X_{1} \sim \pi_{1}}$ on ${\mathbb{R}}^{d}$, find a transport map $T:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ (hopefully nice or optimal in certain sense), such that $Z_{1} ≔ {T{(Z_{0})}} \sim \pi_{1}$ when $Z_{0} \sim \pi_{0}$, that is, $(Z_{0},Z_{1})$ is a coupling (a.k.a transport plan) of $\pi_{0}$ and $\pi_{1}$.*

Several lines of techniques have been developed depending on how to represent and train the map $T$. In traditional generative models, $T$ is parameterized as a neural network, and trained with either GAN-type minimax algorithms or (approximate) maximum likelihood estimation (MLE). However, GANs are known to suffer from numerically instability and mode collapse issues, and require substantial engineering efforts and human tuning, which often do not transfer well across different model architecture and datasets. On the other hand, MLE tends to be intractable for complex models, and hence requires approximate variational or Monte Carlo inference techniques such as those used in variational auto-encoders (VAE), or special model structures such as normalizing flow and auto-regressive models, to yield tractable likelihood, causing difficult trade-offs between expressive power and computational cost.

Recently, advances have been made by representing the transport plan *implicitly as a continuous time process*, such as flow models with neural ordinary differential equations (ODEs) \e.g., and diffusion models by stochastic differential equations (SDEs) \e.g. in these models, a neural network is trained to represent the drift force of the processes and a numerical ODE/SDE solver is used to simulate the process during inference. The key idea is that, by leveraging the mathematical structures of ODEs/SDEs, the continuous-time models can be trained efficiently without resorting to minimax or traditional approximate inference techniques. The most notable examples are the recent score-based generative models and denoising diffusion probabilistic models (DDPM), which we call denoising diffusion methods collectively. These methods allow us to train large-scale diffusion/SDE-based generative models that surpass GANs on image generation in both image quality and diversity, without the instability and mode collapse issues \e.g.,. The learned SDEs can be converted into deterministic ODE models for faster inference with the method of probability flow ODEs and DDIM.

However, compared with the traditional one-step models like GAN and VAE, a key drawback of continuous-times models is the high computational cost in inference time: drawing a single point (e.g., image) requires to solve the ODE/SDE with a numerical solver that needs to repeatedly call the expensive neural drift function. In addition, the existing denoising diffusion techniques require substantial hyper-parameter search in an involved design space and are still poorly understood both empirically and theoretically.

In existing approaches, generative modeling and domain transfer are typically treated separately. It often requires to extend or customize a generative learning techniques to solve domain transfer problems; see e.g., Cycle GAN and diffusion-based image-to-image translation \e.g.,. One framework that naturally unifies both domains is optimal transport (OT) \e.g. which endows a collection of techniques for finding optimal couplings with minimum transport costs of form ${\mathbb{E}}{\lbrack{c{({Z_{1} - Z_{0}})}}\rbrack}$ w.r.t. a cost function $c:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, yielding natural applications to both generative and transfer learning. However, the existing OT techniques are slow for problems with high dimensional and large volumes of data. Furthermore, as the transport costs do not perfectly align with the actual learning performance, methods that faithfully find the optimal transport maps do not necessarily have better learning performance.

Figure 1: The trajectories of rectified flows for image generation (π0: standard Gaussian noise, π1: cat faces, top two rows), and image transfer between human and cat faces (π0: human faces, π1: cat faces, bottom two rows), when simulated using Euler method with step size 1/N for N steps. The first rectified flow induced from the training data (1-rectified flow) yields good results with a very small number (e.g., ≥ 2) of steps; the straightened reflow induced from 1-rectified flow (denoted as 2-rectified flow) has nearly straight line trajectories and yield good results even with one discretization step.

### Contribution

We introduce *rectified flow*, a surprisingly simple approach to the transport mapping problem, which unifiedly solves both generative modeling and domain transfer. The rectified flow is an ODE model that transport distribution $\pi_{0}$ to $\pi_{1}$ by *following straight line paths as much as possible.* The straight paths are preferred both theoretically because it is the shortest path between two end points, and computationally because it can be exactly simulated without time discretization. Hence, flows with straight paths bridge the gap between one-step and continuous-time models.

Algorithmically, the rectified flow is trained with a simple and scalable unconstrained least squares optimization procedure, which avoids the instability issues of GANs, the intractable likelihood of MLE methods, and the subtle hyper-parameter decisions of denoising diffusion models. The procedure of obtaining the rectified flow from the training data has the attractive theoretical property of 1) yielding a coupling with non-increasing transport cost jointly for all convex cost $c$, and 2) making the paths of flow increasingly straight and hence incurring lower error with numerical solvers. Therefore, with a *reflow* procedure that iteratively trains new rectified flows with the data simulated from the previously obtained rectified flow, we obtain nearly straight flows that yield good results even with the coarsest time discretization, i.e., one Euler step. Our method is purely ODE-based, and is both conceptually simpler and practically faster in inference time than the SDE-based approaches of.

Empirically, rectified flow can yield high-quality results for image generation when simulated with a very few number of Euler steps (see Figure 1, top row). Moreover, with just one step of reflow, the flow becomes nearly straight and hence yield good results with a single Euler discretization step (Figure 1, the second row). This substantially improves over the standard denoising diffusion methods. Quantitatively, we claim a state-of-the-art result of FID (4.85) and recall (0.51) on for one-step fast diffusion/flow models. The same algorithm also achieves superb result on domain transfer tasks such as image-to-image translation (see the bottom two rows of Figure 1) and transfer learning.

## Method

We provide a quick overview of the method in Section 2.1, followed with some discussion and remarks in Section 2.2. We introduce a nonlinear extension of our method in Section 2.3, with which we clarify the connection and advantages of our method with the method of probability flow ODEs and DDIM.

Figure 2: (a) Linear interpolation of data input (X0,X1) ∼ π0 × π1. (b) The rectified flow Zt induced by (X0,X1); the trajectories are “rewired” at the intersection points to avoid the crossing. (c) The linear interpolation of the end points (Z0,Z1) of flow Zt. (d) The rectified flow induced from (Z0,Z1), which follows straight paths.

### Overview

### Rectified flow

Given empirical observations of ${X_{0} \sim \pi_{0}},{X_{1} \sim \pi_{1}}$, the rectified flow induced from $(X_{0},X_{1})$ is an ordinary differentiable model (ODE) on time $t \in {\lbrack 0,1\rbrack}$,

which converts $Z_{0}$ from $\pi_{0}$ to a $Z_{1}$ following $\pi_{1}$. The drift force $v:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ is set to drive the flow to follow the direction $({X_{1} - X_{0}})$ of the linear path pointing from $X_{0}$ to $X_{1}$ as much as possible, by solving a simple least squares regression problem:

where $X_{t}$ is the linear interpolation of $X_{0}$ and $X_{1}$. Naviely, $X_{t}$ follows the ODE of ${{dX_{t}} = {{({X_{1} - X_{0}})}dt}},$ which is non-causal (or anticipating) as the update of $X_{t}$ requires the information of the final point $X_{1}$. By fitting the drift $v$ with $X_{1} - X_{0}$, the rectified flow *causalizes* the paths of linear interpolation $X_{t}$, yielding an ODE flow that can be simulated without seeing the future.

In practice, we parameterize $v$ with a neural network or other nonlinear models and solve with any off-the-shelf stochastic optimizer, such as stochastic gradient descent, with empirical draws of $(X_{0},X_{1})$. See Algorithm 1. After we get $v$, we solve the ODE starting from $Z_{0} \sim \pi_{0}$ to transfer $\pi_{0}$ to $\pi_{1}$, backwardly starting from $Z_{1} \sim \pi_{1}$ to transfer $\pi_{1}$ to $\pi_{0}$. Specifically, for backward sampling, we simply solve ${d{\overset{\sim}{X}}_{t}} = {- {v{({\overset{\sim}{X}}_{t},t)}dt}}$ initialized from ${\overset{\sim}{X}}_{0} \sim \pi_{1}$ and set $X_{t} = {\overset{\sim}{X}}_{1 - t}$. The forward and backward sampling are equally favored by the training algorithm, because the objective in is *time-symmetric* in that it yields the equivalent problem if we exchange $X_{0}$ and $X_{1}$ and flip the sign of $v$.

### Flows avoid crossing

A key to understanding the method is the non-crossing property of flows: the different paths following a well defined ODE ${dZ_{t}} = {v{(Z_{t},t)}dt}$, whose solution exists and is unique, *cannot cross each other* at any time $t \in {\lbrack 0,1)}$. Specifically, there exists no location $z \in {\mathbb{R}}^{d}$ and time $t \in {\lbrack 0,1)}$, such that two paths go across $z$ at time $t$ along different directions, because otherwise the solution of the ODE would be non-unique. On the other hand, the paths of the interpolation process $X_{t}$ may intersect with each other (Figure 2a), which makes it non-causal. Hence, as shown in Figure 2b, the rectified flow *rewires* the individual trajectories passing through the intersection points to avoid crossing, while tracing out the same density map as the linear interpolation paths due to the optimization of. We can view the linear interpolation $X_{t}$ as building roads (or tunnels) to connect $\pi_{0}$ and $\pi_{1}$, and the rectified flow as traffics of particles passing through the roads in a myopic, memoryless, non-crossing way, which allows them to ignore the global path information of how $X_{0}$ and $X_{1}$ are paired, and rebuild a more deterministic pairing of $(Z_{0},Z_{1})$.

### Rectified flows reduce transport costs

If is solved exactly, the pair $(Z_{0},Z_{1})$ of the rectified flow is guaranteed to be a valid coupling of $\pi_{0},\pi_{1}$ (Theorem 3.3), that is, $Z_{1}$ follows $\pi_{1}$ if $Z_{0} \sim \pi_{0}$. Moreover, $(Z_{0},Z_{1})$ guarantees to yield no larger transport cost than the data pair $(X_{0},X_{1})$ simultaneously for *all* convex cost functions $c$ (Theorem 3.5). The data pair $(X_{0},X_{1})$ can be an arbitrary coupling of $\pi_{0},\pi_{1}$, typically independent (i.e., ${(X_{0},X_{1})} \sim {\pi_{0} \times \pi_{1}}$) as dictated by the lack of meaningfully paired observations in practical problems. In comparison, the rectified coupling $(Z_{0},Z_{1})$ has a deterministic dependency as it is constructed from an ODE model. Denote by ${(Z_{0},Z_{1})} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(X_{0},X_{1})})}}$ the mapping from $(X_{0},X_{1})$ to $(Z_{0},Z_{1})$. Hence, ${\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{( \cdot )}$ converts an arbitrary coupling into a deterministic coupling with lower convex transport costs.

### Straight line flows yield fast simulation

Following Algorithm 1, denote by ${\mathbf{Z}} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{F}\mathtt{l}\mathtt{o}\mathtt{w}}{({(X_{0},X_{1})})}}$ the rectified flow induced from $(X_{0},X_{1})$. Applying this operator recursively yields a sequence of rectified flows ${\mathbf{Z}}^{k + 1} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{F}\mathtt{l}\mathtt{o}\mathtt{w}}{({(Z_{0}^{k},Z_{1}^{k})})}}$ with ${(Z_{0}^{0},Z_{1}^{0})} = {(X_{0},X_{1})}$, where ${\mathbf{Z}}^{k}$ is the $k$-th rectified flow, or simply *$k$-rectified flow*, induced from $(X_{0},X_{1})$.

This *reflow* procedure not only decreases transport cost, but also has the important effect of straightening paths of rectified flows, that is, making the paths of the flow more straight. This is highly attractive computationally as flows with nearly straight paths incur small time-discretization error in numerical simulation. Indeed, perfectly straight paths can be simulated exactly with a single Euler step and is effectively a one-step model. This addresses the very bottleneck of high inference cost in existing continuous-time ODE/SDE models.

Inputs: Draws from a coupling (X0,X1) of π0 and π1; velocity model vθ: ℝd → ℝd with parameter θ.
Training: ${\hat{\theta} = {{\underset{\theta}{\arg\min}{\mathbb{E}}}\left\lbrack \left. \parallel{X_{1} - X_{0} - {v{({{tX_{1}} + {{({1 - t})}X_{0}}},t)}}}\parallel \right.^{2} \right\rbrack}},$ with t ∼ Uniform ().
Sampling: Draw (Z0,Z1) following d Zt = vθ̂ (Zt,t) d t starting from Z0 ∼ π0 (or backwardly Z1 ∼ π1).
Reflow (optional): Zk + 1 = RectFlow ((Z0k,Z1k)), starting from (Z00,Z10) = (X0,X1).
Distill (optional): Learn a neural network T̂ to distill the k-rectified flow, such that Z1k ≈ T̂ (Z0k).
Algorithm 1 \Name Flow: Main Algorithm

### Main Results and Properties

We provide more in-depth discussions on the main properties of rectified flow. We keep the discussion informal to highlight the intuitions in this section and defer the full course theoretical analysis to Section 3.

First, for a given input coupling $(X_{0},X_{1})$, it is easy to see that the exact minimum of is achieved if

which is the expectation of the line directions $X_{1} - X_{0}$ that pass through $x$ at time $t$. We discuss below the property of rectified flow ${dZ_{t}} = {v^{X}{(Z_{t},t)}dt}$ with $Z_{0} \sim \pi_{0}$, assuming that the ODE has an unique solution.

### Marginal preserving property

\Theorem [3.3\] *The pair $(Z_{0},Z_{1})$ is a coupling of $\pi_{0}$ and $\pi_{1}$. In fact, the marginal law of $Z_{t}$ equals that of $X_{t}$ at every time $t$, that is, ${{{Law}{(Z_{t})}} = {{Law}{(X_{t})}}},{{\forall t} \in {\lbrack 0,1\rbrack}}$.*

Intuitively, this is because, by the definition of $v^{X}$ in, the expected amount of mass that passes through every infinitesmal volume at all location and time are equal under the dynamics of $X_{t}$ and $Z_{t}$, which ensures that they trace out the same marginal distributions:

On the other hand, the joint distributions of the whole trajectory of $Z_{t}$ and that of $X_{t}$ are different in general. In particular, $X_{t}$ is in general a non-causal, non-Markov process, with $(X_{0},X_{1})$ a stochastic coupling, and $Z_{t}$ *causalizes*, *Markovianizes* and *derandomizes* $X_{t}$, while preserving the marginal distributions at all time.

### Reducing transport costs

\Theorem [3.5\] *The coupling $(Z_{0},Z_{1})$ yields lower or equal convex transport costs than the input $(X_{0},X_{1})$ in that ${{\mathbb{E}}{\lbrack{c{({Z_{1} - Z_{0}})}}\rbrack}} \leq {{\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}}$ for any convex cost $c:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$.*

The transport costs measure the expense of transporting the mass of one distribution to another following the assignment relation specified by the coupling and is a central topic in optimal transport \e.g.,. Typical examples are ${c{( \cdot )}} = \left. \parallel \cdot \parallel \right.^{\alpha}$ with $\alpha \geq 1$. Hence, ${\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{( \cdot )}$ yields a Pareto descent on the collection of all convex transport costs, without targeting any specific $c$. This distinguishes it from the typical optimal transport optimization methods, which are explicitly framed to optimize a given $c$. As a result, recursive application of ${\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{( \cdot )}$ does not guarantee to attain the $c$-optimal coupling for any given $c$, with the exception in the one-dimensional case when the fixed point of ${\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{( \cdot )}$ coincides with the unique monotonic coupling that simultaneously minimizes all non-negative convex costs $c$; see Section 3.4.

Intuitively, the convex transport costs are guaranteed to decrease because the paths of the rectified flow $Z_{t}$ is a rewiring of the straight paths connecting $(X_{0},X_{1})$. To give an illustration, consider the simple case of ${c{( \cdot )}} = \left. \parallel \cdot \parallel \right.$ when transport costs ${\mathbb{E}}{\lbrack\left. \parallel{X_{0} - X_{1}}\parallel \right.\rbrack}$ and ${\mathbb{E}}{\lbrack\left. \parallel{Z_{0} - Z_{1}}\parallel \right.\rbrack}$ are the expected length of the straight lines connecting the end points. The inequality can be proved graphically as follows:

where $\overset{(\ast)}{\leq}$ uses the triangle inequality, and $\overset{(\ast\ast)}{=}$ holds because the paths of $Z_{t}$ is a rewiring of the straight paths of $X_{t}$, following the construction of $v^{\mathbf{X}}$ in. For general convex $c$, a similar proof using Jensen's inequality is shown in Section 3.2.

### Reflow, straightening, fast simulation

As shown in Figure 3, when we recursively apply the procedure ${\mathbf{Z}}^{k + 1} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{F}\mathtt{l}\mathtt{o}\mathtt{w}}{({(Z_{0}^{k},Z_{1}^{k})})}}$, the paths of the $k$-rectified flow ${\mathbf{Z}}^{k}$ are increasingly straight, and hence easier to simulate numerically, as $k$ increases. This straightening tendency can be guaranteed theoretically.

(a)The 1st rectified flow Z1

(d) Transport cost, Straightness

Figure 3: (a)-(c) Samples of trajectories drawn from the reflows on a toy example (π0: purple dots, π1: red dots; the green and blue lines are trajectories connecting different modes of π0, π1). (d) The straightness and the relative L2 transport cost v.s. the reflow steps; the values are scaled into, so 0 corresponds to straight lines and L2 optimal transport; see Section 5.1 for more information. We use the non-parametric model in with bandwidth h = 0.1.

Specifically, we say that a flow ${dZ_{t}} = {v{(Z_{t},t)}dt}$ is straight if we have almost surely that $Z_{t} = {{tZ_{1}} + {{({1 - t})}Z_{0}}}$ for ${\forall t} \in {\lbrack 0,1\rbrack}$, or equivalently ${v{(Z_{t},t)}} = {Z_{1} - Z_{0}} = {const}$ following each path. (More precisely, "straight" here refers to straight with a constant speed.) Such straight flows are highly attractive computationally as it is effective a one-step model: a single Euler step update $Z_{1} = {Z_{0} + {v{(Z_{0},0)}}}$ calculates the exact $Z_{1}$ from $Z_{0}$. Note that the linear interpolation ${\mathbf{X}} = {\{ X_{t}\}}$ is straight by this definition but it is not a (causal) flow and hence can not be simulated without an oracle assess to draws of both $\pi_{0}$ and $\pi_{1}$. In comparison, it is non-trivial to make a flow ${dZ_{t}} = {v{(Z_{t},t)}dt}$ straight, because if so $v$ must satisfy the inviscid Burgers' equation ${{\partial_{t}v} + {{({\partial_{z}v})}v}} = 0$:

More generally, we can measure the straightness of any continuously differentiable process ${\mathbf{Z}} = {\{ Z_{t}\}}$ by

${S{({\mathbf{Z}})}} = 0$ means exact straightness. A flow whose $S{({\mathbf{Z}})}$ is small has nearly straight paths and hence can be simulated accurately using numerical solvers with a small number of discretization steps. Section 3.3 shows that applying rectification recursively provably decreases $S{({\mathbf{Z}})}$ towards zero.

*\Theorem [3.7 convergence rate ‣ 3.3 The Straightening Effect ‣ 3 Theoretical Analysis ‣ Flow Straight and Fast: Learning to Generate and Transfer Data with \Name Flow")\] Let $\mathbf{Z}^{k}$ be the $k$-th rectified flow induced from $(X_{0},X_{1})$. Then*

As shown Figure 1, applying one step of reflow can already provide nearly straight flows that yield good performance when simulated with a single Euler step. It is not recommended to apply too many reflow steps as it may accumulate estimation error on $v^{X}$.

### Distillation

After obtaining the $k$-th rectified flow ${\mathbf{Z}}^{k}$, we can further improve the inference speed by distilling the relation of $(Z_{0}^{k},Z_{1}^{k})$ into a neural network $\hat{T}$ to directly predict $Z_{1}^{k}$ from $Z_{0}^{k}$ without simulating the flow. Given that the flow is already nearly straight (and hence well approximated by the one-step update), and the distillation can be done efficiently. In particular, if we take ${\hat{T}{(z_{0})}} = {z_{0} + {v{(z_{0},0)}}}$, then the loss function for distilling ${\mathbf{Z}}^{k}$ is ${\mathbb{E}}\left\lbrack \left. \parallel{{({Z_{1}^{k} - Z_{0}^{k}})} - {v{(Z_{0}^{k},0)}}}\parallel \right.^{2} \right\rbrack$, which is the term in when $t = 0$.

We should highlight the difference between distillation and rectification: distillation attempts to faithfully approximate the coupling $(Z_{0}^{k},Z_{1}^{k})$ while rectification yields a different coupling $(Z_{0}^{k + 1},Z_{1}^{k + 1})$ with lower transport cost and more straight flow. Hence, distillation should be applied only in the final stage when we want to fine-tune the model for fast one-step inference.

### On the velocity field $v^{X}$

If $X_{0}$ yields a conditional density function $\rho{(\left. x_{0} \middle| x_{1} \right.)}$ when conditioned on ${X_{1} = x_{1}},$ then the optimal velocity field ${v^{X}{(z,t)}} = {{\mathbb{E}}{\lbrack{{X_{1} - \left. X_{0} \middle| X_{t} \right.} = z}\rbrack}}$ can be represented by

where the expectation ${\mathbb{E}}\lbrack \cdot \rbrack$ is taken w.r.t. $X_{1} \sim \pi_{1}$. This can be seen by noting that $X_{0} = \frac{z - {tX_{1}}}{1 - t}$ and ${X_{1} - X_{0}} = \frac{X_{1} - z}{1 - t}$, when conditioned on $X_{t} = z$. Hence, if $\rho$ is positive and continuous everywhere, then $v^{X}$ is well defined and continuous on ${\mathbb{R}}^{d} \times {\lbrack 0,1)}$. Further, if $\log\eta_{t}$ is continuously differentiable w.r.t. $z$, we can show that

Note that ${dZ_{t}} = {v^{X}{(Z_{t},t)}dt}$ is guaranteed to have a unique solution if $v^{X}$ is uniformly Lipschitz continuous on $\lbrack 0,a\rbrack$ for any $a < 1$.

If $\left. X_{0} \middle| X_{1} \right. = x_{1}$ does not yield a conditional density function, $v^{X}{(z,t)}$ may be undefined or discontinuous, making the ODE ${dZ_{t}} = {v^{X}{(Z_{t},t)}dt}$ ill-behaved. A simple fix is to add $X_{0}$ with a Gaussian noise $\xi \sim {\mathcal{N}{(0,{\sigma^{2}I})}}$ independent of $(X_{0},X_{1})$ to yield a smoothed variable ${\overset{\sim}{X}}_{0} = {X_{0} + \xi}$, and transfer ${\overset{\sim}{X}}_{0}$ to $X_{1}$ using rectified flow. This would effectively give a randomized mapping of form $T{({X_{0} + \xi})}$ transporting $\pi_{0}$ to $\pi_{1}$.

### Smooth function approximation

Following, we can *exactly* calculate $v^{X}$ if the conditional density function $\rho{( \cdot |x_{1})}$ exists and is known, and $\pi_{1}$ is the empirical measure of a finite number of points (whose expectation can be evaluated exactly). In this case, running the rectified flow forwardly would precisely recover the points in $\pi_{1}$. This, however, is not practically useful in most cases as it completely overfits the data. Hence, it is both necessary and beneficial to fit $v^{X}$ with a smooth function approximator such as neural network or non-parametric models, to obtain smoothed distributions with novel samples that are practically useful.

Deep neural networks are no doubt the best function approximators for large scale problems. For low dimensional problems, the following simple Nadaraya--Watson style non-parametric estimator of $v^{X}$ can yield a good approximation to the exact rectified flow without knowing the conditional density $\rho$:

where ${\omega_{h}{(X_{t},z)}} = \frac{\kappa_{h}{(X_{t},z)}}{{\mathbb{E}}\left\lbrack {\kappa_{h}{(X_{t},z)}} \right\rbrack}$, and $\kappa_{h}{(x,z)}$ is a smoothing kernel with a bandwith parameter $h > 0$ that measures the similarity between $z$ and $x$. Taking the Gaussian RBF kernel ${\kappa_{h}{(x,z)}} = {\exp{({- {{\left. \parallel{x - z}\parallel \right.^{2}/2}h^{2}}})}}$, then when $h\rightarrow 0^{+}$, it can be shown that $v^{X,h}{(z,t)}$ converges to ${v^{X}{(z,t)}} = {{\mathbb{E}}\left\lbrack {\left. \frac{X_{1} - z}{1 - t} \middle| X_{t} \right. = z} \right\rbrack}$ on points $z$ that can be attained by $X_{t}$ (i.e., the conditional expectation ${\mathbb{E}}\left\lbrack \cdot |X_{t} = z \right\rbrack$ exists. ). On points $z$ that $X_{t}$ can not attain, $v^{X,h}{(z,t)}$ extrapolates the value by finding the $X_{t}$ that is close to $z$. In practice, we replace the expectations in with empirical averaging. We find that $v^{X,h}$ performs well in practice because it is a mixture of linear functions that always point to a point in the support of $\pi_{1}$.

### Nonlinear Extension

We present a nonlinear extension of rectified flow in which the linear interpolation $X_{t}$ is replaced by any time-differentiable curve connecting $X_{0}$ and $X_{1}$. Such generalized rectified flows can still transport $\pi_{0}$ to $\pi_{1}$ (Theorem 3.3), but no longer guarantee to decrease convex transport costs, or have the straightening effect. Importantly, the method of probability flows and DDIM can be viewed (approximately) as special cases of this framework, allows us to clarify the connection with and the advantages over these methods.

Let ${\mathbf{X}} = {\{ X_{t}:{t \in {\lbrack 0,1\rbrack}}\}}$ be any time-differentiable random process that connects $X_{0}$ and $X_{1}$. Let ${\overset{˙}{X}}_{t}$ be the time derivative of $X_{t}$. The (nonlinear) rectified flow induced from $\mathbf{X}$ is defined as

We can estimate $v^{\mathbf{X}}$ by solving

where $w_{t}:{{}\rightarrow{(0,{+ \infty})}}$ is a positive weighting sequence ($w_{t} = 1$ by default). When using the linear interpolation $X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}$, we have ${\overset{˙}{X}}_{t} = {X_{1} - X_{0}}$ and with $w_{t} = 1$ reduces to. As we show in Theorem 3.3, the flow $\mathbf{Z}$ given by this method still preserves the marginal laws of $\mathbf{X}$, that is, ${{Law}{(Z_{t})}} = {{Law}{(X_{t})}}$, ${\forall t} \in {\lbrack 0,1\rbrack}$, and hence $(Z_{0},Z_{1})$ remains to be a coupling of $\pi_{0},\pi_{1}$. However, if $\mathbf{X}$ is not straight, $(Z_{0},Z_{1})$ no longer guarantees to decrease the convex transport costs over $(X_{0},X_{1})$. More importantly, the reflow procedure no longer straightens the paths of $Z_{t}$.

A simple class of interpolation processes is $X_{t} = {{\alpha_{t}X_{1}} + {\beta_{t}X_{0}}}$ where $\alpha_{t}$ and $\beta_{t}$ are two differentiable sequences that satisfy $\alpha_{1} = \beta_{0} = 1$ and $\alpha_{0} = \beta_{1} = 0$ to ensure that the process equals $X_{0},X_{1}$ at the starting and end points. In this case, we have ${\overset{˙}{X}}_{t} = {{{\overset{˙}{\alpha}}_{t}X_{1}} + {{\overset{˙}{\beta}}_{t}X_{0}}}$ in where ${\overset{˙}{\alpha}}_{t}$ and ${\overset{˙}{\beta}}_{t}$ are the time derivatives of $\alpha_{t}$ and $\beta_{t}$. The shape of the curve is controlled by the relation of $\alpha_{t}$ and $\beta_{t}$. If we take $\beta_{t} = {1 - \alpha_{t}}$ for all $t$, then $X_{t}$ have straight paths but does not travel at a constant speed; it can be viewed as a time-changed variant of the canonical case $X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}$ when $t$ is reparameterized to $\alpha_{t}$. When $\beta_{t} \neq {1 - \alpha_{t}}$, the paths of $X_{t}$ are not straight lines except some special cases (e.g., ${{\overset{˙}{\alpha}}_{t}X_{1}} = 0$ or ${{\overset{˙}{\beta}}_{t}X_{0}} = 0$, or $X_{1} = {aX_{1}}$ for some $a \in {\mathbb{R}}$).

### Probability Flow ODEs and DDIM

The probability flow ODEs (PF-ODEs) and denoising diffusion implicit models (DDIM) are methods for learning ODE-based generative models of $\pi_{1}$ from a spherical Gaussian initial distribution $\pi_{0}$, derived by converting a SDE learned by denoising diffusion methods to an ODE with equivalent marginal laws. In, three types of PF-ODEs are derived from three types of SDEs learned as score-based generative models, including variance-exploding (VE) SDE, variance-preserving (VP) SDE, and sub-VP SDE, which we denote by VE ODE, VP ODE, and sub-VP ODE, respectively. VP ODE is equivalent to the continuous time limit of DDIM, which is derived from the denoising diffusion probability model (DDPM). As the derivations of PF-ODEs and DDIM require advanced tools in stochastic calculus, we limit our discussion on the final algorithmic procedures suggested in, which we summarize in Section 3.5. The readers are referred to for the details.

*\Proposition [3.11\] All variants of PF-ODEs can be viewed as instances of when using $X_{t} = {{\alpha_{t}X_{1}} + {\beta_{t}\xi}}$ for some $\alpha_{t},\beta_{t}$ with ${\alpha_{1} = 1},{\beta_{1} = 0}$, where $\xi \sim {\mathcal{N}{(0,I)}}$ is a standard Gaussian random variable.*

Here we need to use introduce $\xi$ to replace $X_{0}$ because the choices of $\alpha_{t}$ and $\beta_{t}$ suggested in do not satisfy the boundary condition of $\alpha_{0} = 0$ and $\beta_{0} = 1$ at $t = 0$, and hence $X_{0} \neq \xi$. Instead, in these methods, the initial distribution $X_{0} \sim \pi_{0}$ is implicitly defined as $X_{0} = {{\alpha_{0}X_{1}} + {\beta_{0}\xi}}$, which is approximated by $X_{0} \approx {\beta_{0}\xi}$ by making ${\alpha_{0}X_{1}} \ll {\beta_{0}\xi}$. Hence, $\pi_{0}$ is set to be $\mathcal{N}{(0,{\beta_{0}^{2}I})}$ in these methods. Viewed through our framework, there is no reason to restrict $\xi$ to be $\mathcal{N}{(0,{\beta_{0}^{2}I})}$, or not set ${\alpha_{0} = 0},{\beta_{0} = 1}$ to avoid the approximation.

(αt in, $\beta_{t} = \sqrt{1 - \alpha_{t}^{2}}$)

1-Rectified Flow 2-Rectified Flow
1-Rectified Flow 2-Rectified Flow
1-Rectified Flow 2-Rectified Flow

Figure 4: Comparing rectified flow with VP ODE and sub-VP ODE when π0 = 𝒩 (0,I) (purple dots) and π1 is a low variance Gaussian mixture shown as the red dots. The linear rectified flow yields nearly straight trajectories with one step of reflow. But the trajectories of VP ODE and sub-VP ODE are curved and can not be straightened by reflowing.

VP ODE (const speed)

αt in, $\beta_{t} = \sqrt{1 - \alpha_{t}^{2}}$
αt = t, $\beta_{t} = \sqrt{1 - \alpha_{t}^{2}}$

Figure 5: Trajectories of different methods when varying the number of discretization steps N (purple dots: π0; red dots: π1; orangle dots: intermediate steps; blue curves: flow trajectories). The rectified flow travels in straight lines and progresses uniformly in time; it generates the mean of π1 when simulated with a single Euler step, and quickly covers the whole distribution π1 with more steps (in this case N = 2 is sufficient). In comparison, VP ODE and sub-VP ODE travel in curves with non-uniform speed: they tend to be slow in the beginning and speed up in the later phase (much of the update happens when t ⪆ 0.5). The non-uniform speed can be avoided by setting αt = t (see the last column).

### VP ODE and sub-VP ODE

The VP ODE and sub-VP ODE of use the following shared $\alpha_{t}$:

where the default values of $a,b$ are chosen to match the continuous time limit of the shared training procedure of DDIM and DDPM. The difference of VP ODE and sub-VP ODE is on the choice of $\beta_{t}$, given as follows:

As $\beta_{0} \approx 1$ in both VP and sub-VP ODE, the $\pi_{0}$ in both cases are taken as $\mathcal{N}{(0,I)}$.

The choices of $\alpha_{t},\beta_{t}$ above are the consequence of the SDE-based derivation in. However, they are not well-motivated when we exam the path properties of the induced ODEs:

*$\bullet$ Non-straight paths:* Due to choices of $\beta_{t}$ in, the trajectories of VP ODE and sub-VP ODE are curved in general, and can not be straightened by the reflow procedure. We should choose $\beta_{t} = {1 - \alpha_{t}}$ to induce straight paths.

Figure 6: t vs. αt, βt of different methods.

*$\bullet$ Non-uniform speed:* The exponential form of $\alpha_{t}$ in is a consequence of using Ornstein--Uhlenbeck processes in the derivation of SDE models. However, there is no clear advantage of using for ODEs. As shown in Figure 5, the $\alpha_{t}$ and $\beta_{t}$ of VP and sub-VP ODE change slowly in the early phase ($t \lessapprox 0.5$). As a result, the flow also moves slowly in beginning and hence most of the updates are concentrated in the later phase. Such non-uniform update speed, in addition to the non-straight paths, make VP ODE and sub-VP ODE perform sub-optimally when using large step sizes, even for transport between simple spherical Gaussian distributions (see Figure 5). As we show in the last column of Figure 5, changing the exponential $\alpha_{t}$ to the linear function $\alpha_{t} = t$ in VP ODE allows us to get a uniform update speed while preserving the same continuous-time trajectories.

### VE ODE

The VE ODE of uses $\alpha_{t} = 1$ and $\beta_{t} = {\sigma_{\min}\sqrt{r^{2{({1 - t})}} - 1}}$ where $\sigma_{\min} = 0.01$ by default $r$ is set such that $\sigma_{\max} ≔ {r\sigma_{\min}}$ is as large as the maximum Euclidean distance between all pairs of training data points from $\pi_{1}$ (Technique 1 of ). Assume that $\sigma_{\max}^{2}$ is much larger than both $\sigma_{\min}^{2}$ and the variance of $X_{1}$, then $X_{0} = {X_{1} + {\beta_{0}\xi}} \approx {\sigma_{\max}\xi}$, and we can set the initial distribution to be $\pi_{0} \sim {\mathcal{N}{(0,{\sigma_{\max}^{2}I})}}$, which has much larger variance than $\pi_{1}$. Hence, VE ODE can not be applied to (and not shown in) the toys in Figure 4 and Figure 5. As the case of (sub-)VP ODE, the restriction on $\xi$ is in fact unnecessary and requirement that $\sigma_{\max}$ is unnatural viewed from our framework. On the other hand, the trajectories of $X_{t}$ in VE ODE are indeed straight lines, because the direction of ${\overset{˙}{X}}_{t} = {{\overset{˙}{\beta}}_{t}\xi}$ is always the same as $\xi$. However, the choice of $\beta_{t}$ causes a non-uniform speed issue similar to that of (sub-)VP ODE.

Following, a line of works have been proposed to improve the choices of $\alpha_{t},\beta_{t}$, but remain to be constrained by the basic design space from the SDE-to-ODE derivation; see for example.

To summarize, the simple nonlinear rectified flow framework in both simplifies and extends the existing framework, and sheds a number of importance insights:

$\bullet$ Learning ODEs can be considered directly and independently without resorting to diffusion/SDE methods;

$\bullet$ The paths of the learned ODEs can be specified by any smooth interpolation curve $X_{t}$ of $X_{0}$ and $X_{1}$;

$\bullet$ The initial distribution $\pi_{0}$ can be chosen arbitrarily, independent with the choice of the interpolation $X_{t}$.

$\bullet$ The canonical linear interpolation $X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}$ should be recommended as a default choice.

On the other hand, non-linear choices of $X_{t}$ can be useful when we want to incorporate certain non-Euclidan geometry structure of the variable, or want to place certain constraints on the trajectories of the ODEs. We leave this for future works.

## Theoretical Analysis

We present the theoretical analysis for rectified flow. The results are summarized as follows.

$\bullet$ \Section [3.1\] All nonlinear rectified flows with any interpolation $X_{t}$ preserve the marginal laws.

$\bullet$ \Section [3.2\] The rectified flow (with the canonical linear interpolation) reduces convex transport costs.

$\bullet$ \Section [3.3\] Reflow guarantees to straighten the (linear) rectified flows.

$\bullet$ \Section [3.4\] We clarify the relation between straight couplings and $c$-optimal couplings.

$\bullet$ \Section [3.5\] We establish PF-ODEs as instances of nonlinear rectified flows.

### The Marginal Preserving Property

The marginal preserving property that ${{Law}{(Z_{t})}} = {{Law}{(X_{t})}}$ for $\forall t$ is a general property of the nonlinear rectified flows in, regardless whether the interpolation $X_{t}$ is straight or not.

### Definition 3.1

For a path-wise continuously differentiable random process $\mathbf{X} = {\{ X_{t}:{t \in {\lbrack 0,1\rbrack}}\}}$, its expected velocity $v^{\mathbf{X}}$ is defined as

For $x \notin {{supp}{(X_{t})}}$, the conditional expectation is not defined and we set $v^{\mathbf{X}}$ arbitrarily, say ${v^{\mathbf{X}}{(x,t)}} = 0$.

### Definition 3.2

We call that $\mathbf{X}$ is rectifiable if $v^{\mathbf{X}}$ is locally bounded and the solution of the integral equation below exists and is unique:

In this case, $\mathbf{Z} = {\{ Z_{t}:{t \in {\lbrack 0,1\rbrack}}\}}$ is called the rectified flow induced from $\mathbf{X}$.

### Theorem 3.3

Assume $\mathbf{X}$ is rectifiable and $\mathbf{Z}$ is its rectified flow. Then ${{Law}{(Z_{t})}} = {{Law}{(X_{t})}}$ for ${\forall t} \in {\lbrack 0,1\rbrack}$.

### Proof

For any compactly supported continuously differentiable test function $h:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, we have

where we used ${v^{\mathbf{X}}{(X_{t},t)}} = {{\mathbb{E}}{\lbrack\left. {\overset{˙}{X}}_{t} \middle| X_{t} \right.\rbrack}}$. By definition, this is equivalent to that $\pi_{t} ≔ {{Law}{(X_{t})}}$ solves in the sense of distributions the continuity equation with drift $v_{t}^{\mathbf{X}} ≔ {v^{\mathbf{X}}{( \cdot,t)}}$:

To see the equivalence of and, we can multiply with $h$ and integrate both sides:

where we use integration by parts that ${\int{{h\nabla} \cdot {({v_{t}^{\mathbf{X}}\pi_{t}})}}} = {- {\int{{\nabla h^{\top}}{({v_{t}^{\mathbf{X}}\pi_{t}})}}}}$.

Because $Z_{t}$ is driven by the same velocity field $v^{\mathbf{X}}$, its marginal law ${Law}{(Z_{t})}$ solves the very same equation with the same initial condition ($Z_{0} = X_{0}$). Hence, the equivalence of ${Law}{(Z_{t})}$ and ${Law}{(X_{t})}$ follows if the solution of is unique, which is equivalent to the uniqueness of the solution of ${dZ_{t}} = {v^{\mathbf{X}}{(Z_{t},t)}}$ following Corollary 1.3 of Kurtz (see also Theorem 4.1 of Ambrosio and Crippa ). ∎

### Reducing Convex Transport Costs

The fact that $(Z_{0},Z_{1})$ yields no larger convex transport costs than $(X_{0},X_{1})$ is a consequence of using the special linear interpolation $X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}$ as the geodesic of Euclidean space.

### Definition 3.4

A coupling $(X_{0},X_{1})$ is called rectifiable if its linear interpolation process $\mathbf{X} = {\{{{tX_{1}} + {{({1 - t})}X_{0}}}:{t \in {\lbrack 0,1\rbrack}}\}}$ is rectifiable. In this case, the $\mathbf{Z} = {\{ Z_{t}:{t \in {\lbrack 0,1\rbrack}}\}}$ in is called the rectified flow of coupling $(X_{0},X_{1})$, denoted as $\mathbf{Z} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{F}\mathtt{l}\mathtt{o}\mathtt{w}}{({(X_{0},X_{1})})}}$, and $(Z_{0},Z_{1})$ is called the rectified coupling of $(X_{0},X_{1})$, denoted as ${{(Z_{0},Z_{1})} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(X_{0},X_{1})})}}}.$

### Theorem 3.5

Assume $(X_{0},X_{1})$ is rectifiable and ${(Z_{0},Z_{1})} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(X_{0},X_{1})})}}$. Then for any convex function $c:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, we have

### Proof

The proof is based on elementary applications of Jensen's inequality.

If $X_{t}$ is straight but with positive non-constant speed, that is, $X_{t} = {{\alpha_{t}X_{1}} + {\beta_{t}X_{0}}}$ with $\beta_{t} = {1 - \alpha_{t}}$ and ${\overset{˙}{\alpha}}_{t} \geq 0$, then we still have ${{\mathbb{E}}{\lbrack{c{({Z_{1} - Z_{0}})}}\rbrack}} \leq {{\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}}$ if $c$ is convex and $m$-homogeneous in that ${c{({ax})}} = {|a|^{m}c{(x)}}$ for ${{\forall a} \in {\mathbb{R}}},{x \in {\mathbb{R}}^{d}}$, with some constant $m \in {(0,1\rbrack}$.

### The Straightening Effect

A coupling $(X_{0},X_{1})$ is said to be straight (or fully rectified) if it is a fixed point of the ${\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{( \cdot )}$ mapping. It is desirable to obtain a straight coupling because its rectified flow is straight and hence can be simulated exactly with one step using numerical solvers. In this section, we first characterize the basic properties of straight couplings, showing that a coupling is straight iff its linear interpolation paths do not intersect with each other. Then, we prove that recursive rectification straightens the coupling and its related flow with a $O\left( {1/k} \right)$ rate, where $k$ is the number of rectification steps.

### Theorem 3.6

Assume $(X_{0},X_{1})$ is rectifiable. Let $X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}$ and $\mathbf{Z} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{F}\mathtt{l}\mathtt{o}\mathtt{w}}{({(X_{0},X_{1})})}}$. Then $(X_{0},X_{1})$ is a straight coupling iff the following equivalent statements hold.

There exists a strictly convex function $c:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, such that ${{\mathbb{E}}{\lbrack{c{({Z_{1} - Z_{0}})}}\rbrack}} = {{\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}}$.

$(X_{0},X_{1})$ is a fixed point of ${\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{( \cdot )}$, that is, ${(X_{0},X_{1})} = {(Z_{0},Z_{1})}$.

The rectified flow coincides with the linear interpolation process: ${\mathbf{X}} = {\mathbf{Z}}$.

The paths of the linear interpolation $\mathbf{X}$ do not intersect:

where ${V{({(X_{0},X_{1})})}} = 0$ indicates that ${X_{1} - X_{0}} = {{\mathbb{E}}{\lbrack{X_{1} - \left. X_{0} \middle| X_{t} \right.}\rbrack}}$ almost surely when $t \sim {\text{Uniform}{({\lbrack 0,1\rbrack})}}$, meaning that the lines passing through each $X_{t}$ is unique, and hence no linear interpolation paths intersect.

### Proof

$3\rightarrow 2\rightarrow 1$: Obvious.

$1\rightarrow 4$: If ${{\mathbb{E}}{\lbrack{c{({Z_{1} - Z_{0}})}}\rbrack}} = {{\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}}$, the two applications of Jensen's inequality in the proof of Theorem 3.5 are tight. Because $c$ is strictly convex, the second Jensen's inequality in the proof implies that ${X_{1} - X_{0}} = {{\mathbb{E}}{\lbrack{X_{1} - \left. X_{0} \middle| X_{t} \right.}\rbrack}}$ almost surely w.r.t. $X$ and ${t \sim {\text{Uniform}{({\lbrack 0,1\rbrack})}}},$ which implies that ${{V{({\mathbf{X}})}} = 0}.$

$4\rightarrow 3$: If ${V{({\mathbf{X}})}} = 0$, we have ${\int_{0}^{s}{{({X_{1} - X_{0}})}{dt}}} = {\int_{0}^{s}{{\mathbb{E}}{\lbrack{X_{1} - \left. X_{0} \middle| X_{t} \right.}\rbrack}{dt}}} = {\int_{0}^{s}{v^{X}{(X_{t},t)}{dt}}}$ for $s \in {(0,1\rbrack}$. Hence

Because $\mathbf{Z}$ satisfies the same equation, we have ${\mathbf{X}} = {\mathbf{Z}}$ by the uniqueness of the solution.

### $O\hspace{0pt}\left( {1/K} \right)$ convergence rate

We now show that as we apply rectification recursively, the rectified flows become increasingly straight and the linear interpolation of the couplings becomes increasingly non-intersecting.

### Theorem 3.7

Let $\mathbf{Z}^{k}$ the $k$-th rectified flow of $(X_{0},X_{1})$, that is, $\mathbf{Z}^{k + 1} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{F}\mathtt{l}\mathtt{o}\mathtt{w}}{({(Z_{0}^{k},Z_{1}^{k})})}}$ and ${(Z_{0}^{0},Z_{1}^{0})} = {(X_{0},X_{1})}$. Assume each $(Z_{0}^{k},Z_{1}^{k})$ is rectifiable for $k = {0,\ldots,K}$.

Hence, ${{\mathbb{E}}{\lbrack\left. \parallel{X_{1} - X_{0}}\parallel \right.^{2}\rbrack}} < {+ \infty}$, we have $\min_{k \leq K}{(S{({\mathbf{Z}}^{k})} + V{({(Z_{0}^{k},Z_{1}^{k})})} = O(1/K)}$.

### Proof

Taking ${c{(x)}} = \left. \parallel x\parallel \right.^{2}$ in the proof of Theorem 3.5, we can obtain that

Applying it to each rectification step yields

A telescoping sum on $k = {0,\ldots,K}$ gives the result.

### Straight vs. Optimal Couplings

A coupling $(X_{0},X_{1})$ is called $c$-optimal if it achieves the minimum of ${\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}$ among all couplings that share the same marginals. Understanding and computing the optimal couplings have been the main focus of optimal transport \e.g.,. Straight couplings is a different desirable property. In the following, we show that straightness is a necessary but not sufficient condition of being $c$-optimal for a strictly convex function $c$, except in the one dimensional case when the two concepts coincides. Hence, it is "easier" to find a straight coupling than a $c$-optimal couplings.

### Theorem 3.8

If a rectifiable coupling $(X_{0},X_{1})$ is $c$-optimal for some strictly convex cost function $c$, then $(X_{0},X_{1})$ is a straight coupling.

### Proof

Let ${(Z_{0},Z_{1})} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(X_{0},X_{1})})}}$. If $(X_{0},X_{1})$ is $c$-optimal, we must have ${{\mathbb{E}}{\lbrack{c{({Z_{1} - Z_{0}})}}\rbrack}} = {{\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}}$. This implies Statement 1 in Theorem 3.6 and hence that $(X_{0},X_{1})$ is straight. ∎

### 1D Case

For any $\pi_{0},\pi_{1}$ on $\mathbb{R}$, there exists an unique coupling $(X_{0}^{\ast},X_{1}^{\ast})$ that is simultaneously optimal for all non-negative convex cost functions $c$. This coupling is uniquely characterized by a monotonic property: for every $(x_{0},x_{1})$ and $(x_{0}^{\prime},x_{1}^{\prime})$ in the support of $(X_{0}^{\ast},X_{1}^{\ast})$, if $x_{0} < x_{0}^{\prime}$, then $x_{1} \leq x_{1}^{\prime}$. Furthermore, if $\pi_{0}$ is absolutely continuously w.r.t. the Lebesgue measure, then $(X_{0}^{\ast},X_{1}^{\ast})$ must be deterministic in that there exists a mapping $T:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ such that $X_{1}^{\ast} = {T{(X_{0}^{\ast})}}$. See.

In the following, we show that straight couplings on $\mathbb{R}$ coincides with the deterministic monotonic coupling $(X_{0}^{\ast},X_{1}^{\ast})$ and hence is unique and simultaneously optimal for all convex $c$ when $\pi_{0}$ is absolutely continuous. The idea is that, in $\mathbb{R}$, a coupling is monotonic iff its linear interpolation paths do not intersect, a characteristic feature of straight couplings.

### Lemma 3.9

A coupling on $\mathbb{R}$ is straight iff it is deterministic and monotonic.

### Theorem 3.10

For any $\pi_{0},\pi_{1}$ on $\mathbb{R}$, there exists either no straight coupling, or a unique straight coupling. Further, if exists, the unique straight coupling is deterministic and monotonic, and jointly optimal w.r.t. all convex cost functions $c:{{\mathbb{R}}^{d}\rightarrow{\lbrack 0,{+ \infty})}}$ for which the minimum value of ${\mathbb{E}}\left\lbrack {c{({X_{1} - X_{0}})}} \right\rbrack$ exists and is finite.

### Proof of Lemma 3.9

If $(X_{0},X_{1})$ on $\mathbb{R}$ is straight, then it coincides with its rectified coupling ${{(Z_{0},Z_{1})} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(X_{0},X_{1})})}}}.$ But because $(Z_{0},Z_{1})$ is induced from the rectified flow ${dZ_{t}} = {v^{X}{(Z_{t},t)}dt}$, it is obviously deterministic. It is also monotonic due to the non-crossing property of flows. Specifically, if $(Z_{0},Z_{1})$ is not monotonic, there exists $(z_{0},z_{1})$ and $(z_{0}^{\prime},z_{1}^{\prime})$ in the support of $(Z_{0},Z_{1})$ such that $z_{0} < z_{0}^{\prime}$ and $z_{1} > z_{1}^{\prime}$. If this happens, there must exists $t_{0} \in {}$, such that $z_{t_{0}} = z_{t_{0}}^{\prime}$. But by the uniqueness of the solution, we have $z_{t} = z_{t}$ for $t \geq t_{0}$, which is conflicting with $z_{1} > z_{1}^{\prime}$.

Assume $(X_{0},X_{1})$ is deterministic and monotonic. Due to the monotonicity, there exists no $x_{0}$ and $x_{0}^{\prime}$ in the support of $\pi_{0}$, such that $x_{0} \neq x_{0}^{\prime}$ and $x_{t_{0}} = x_{t_{0}}^{\prime}$ for some $t_{0} < 1$. This suggests that ${X_{1} - X_{0}} = {{\mathbb{E}}{\lbrack{X_{1} - \left. X_{0} \middle| X_{t} \right.}\rbrack}} = {v^{X}{(X_{t},t)}}$ for $t \in {}$, and hence ${dX_{t}} = {{({X_{1} - X_{0}})}dt} = {v^{X}{(X_{t})}dt}$, which is the ODE of the rectified flow. In addition, $X_{t}$ is obviously the unique solution of this ODE. Hence $(X_{0},X_{1})$ is rectifiable and straight following Statement 3 of Theorem 3.6. ∎

### Proof of Theorem 3.10

This is the result of Lemma 3.9 combined with the fact that the monotonic coupling is unique and jointly optimal for all convex $c$ for which the optimal coupling exists, following Lemma 2.8 and Theorem 2.9 of. ∎

### Multi-dimensional cases

On the other hand, on ${\mathbb{R}}^{d}$ with $d \geq 2$, the different cost functions $c$ do not share a common optimal coupling in general, and a straight coupling is not guaranteed to optimize a specific $c$; this is expected because the ${\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{( \cdot )}$ procedure does not depend on a particular choice of $c$. Hence, one must modify the ${\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{( \cdot )}$ procedure to tailor it to a specific $c$ of interest.

In a recent work, it was conjectured that the couplings $(Z_{0},Z_{1})$ induced from VP ODE (equivalently DDIM) yields an optimal coupling w.r.t. the quadratic loss, which was proved to be false in. Here we show that even straight couplings are not guaranteed to be optimal, not to mention that VP ODE does not follow straight paths by design.

We explore this in a separate work that is devoted to modifying rectified flow to find $c$-optimal couplings; a result from that can be easily stated is that the optimal coupling w.r.t. the quadratic cost ${c{( \cdot )}} = \left. \parallel \cdot \parallel \right.^{2}$ can be achieved as the fixed point of ${\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{( \cdot )}$ if $v$ is restricted to be a gradient field of form ${v{(x,t)}} = {{\nabla f}{(x,t)}}$ when solving. Restricting $v$ to be a gradient field removes the rotational component of the velocity field $v^{\mathbf{X}}$ that causes sub-optimal transport cost.

### Denoising Diffusion Models and Probability Flow ODEs

We prove that the probability flow ODEs (PF-ODEs) of can be viewed as nonlinear rectified flows in with ${X_{t} = {{\alpha_{t}X_{1}} + {\beta_{t}\xi}}}.$ We start with introducing the algorithmic procedures of the denoising diffusion models and PF-ODEs, and refer the readers to the original works for the theoretical derivations.

The denoising diffusion methods learn to generative models by constructing an SDE model driven by a standard Brownian motion $W_{t}$:

where $\sigma_{t}:{{\lbrack 0,1\rbrack}\rightarrow{\lbrack 0,{+ \infty})}}$ is a (typically) fixed diffusion coefficient, $b$ is a trainable neural network, and the initial distribution $\pi_{0}$ is restricted to a spherical Gaussian distribution determined by hyper-parameter setting of the algorithm. The idea is to first collapse the data into an (approximate) Gaussian distribution using a diffusion process, mostly an Ornstein-Uhlenbeck (OU) process, and then estimate the generative diffusion process as the time reversal \e.g., of the collapsing process.

Without diving into the derivations, the training loss of the VE, VP, sub-VP SDEs for $b$ in can be summarized as follows:

where $\xi_{t}$ is a diffusion process satisfying $\xi_{t} \sim {\mathcal{N}{(0,I)}}$, and $\eta_{t},\sigma_{t}$ are the hyper-parameter sequences of the algorithm, and $\alpha_{t},\beta_{t}$ are determined by $\eta_{t},\sigma_{t}$ via

The relation in is derived to make ${\overset{\sim}{V}}_{t} = V_{1 - t} = {{\alpha_{1 - t}X_{1}} + {\beta_{1 - t}\xi_{t}}}$ follow the Ornstein-Uhlenbeck (OU) processes ${d{\overset{\sim}{V}}_{t}} = {{\eta_{1 - t}{\overset{\sim}{V}}_{t}dt} + {\sigma_{1 - t}dW_{t}}}$.

VE SDE, which is equivalent to SMLD in, takes $\eta_{t} = 0$ and hence has $\alpha_{t} = 1$. (sub-)VP SDE takes $\eta_{s}$ to be a linear function of $s$, yielding the exponential $\alpha_{t}$ in. VP SDE (which is equivalent to DDPM ) takes $\eta_{t} = {- {\frac{1}{2}\sigma_{t}^{2}}}$ which yields that ${\alpha_{t}^{2} + \beta_{t}^{2}} = 1$ as shown in. In DDPM, it was suggested to write ${b{(x,t)}} = {{- {\eta_{t}x}} - {\frac{\sigma_{t}^{2}}{\beta_{t}}\epsilon{(x,t)}}}$, and estimate $\epsilon$ as a neural network that predicts $\xi_{t}$ from $(V_{t},t)$.

Theoretically, the SDE in with $b$ solving is ensured to yield ${{Law}{(U_{1})}} = {{Law}{(X_{1})}} = \pi_{1}$ when initialized from $U_{0} = {{\alpha_{0}X_{1}} + {\beta_{0}\xi_{0}}}$, which can be approximated by $U_{0} \approx {\beta\xi_{0}}$ when ${\alpha_{0}X_{1}} \ll {\beta_{0}\xi_{0}}$.

By using the properties of Fokker-Planck equations, it was observed in that the SDE in with $b$ trained in can be converted into an ODE that share the same marginal laws:

Equivalently, we can regard $\overset{\sim}{b}$ as the solution of

which defers from only by a factor of $1/2$ in the second term of $Y_{t}$. This simple equivalence holds only when and use the special initialization of $Z_{0} = U_{0} = {{\alpha_{0}X_{1}} + {\beta_{0}\xi_{0}}}$.

In the following, we are ready to prove that is can be viewed as the nonlinear rectified flow objective in using $X_{t} = {{\alpha_{t}X_{1}} + {\beta_{t}\xi}}$ with $\xi \sim {\mathcal{N}{(0,I)}}$. We mainly need to show that ${\overset{\sim}{Y}}_{t}$ is equivalent to ${\overset{˙}{X}}_{t}$ by eliminating $\eta_{t}$ and $\sigma_{t}$ using the relation in.

### Proposition 3.11

Assume hold. Then is equivalent to with $X_{t} = {{\alpha_{t}X_{1}} + {\beta_{t}\xi}}$.

### Proof

First, note that we can take $\xi_{t} = \xi$ for all time $t$, as the correlation structure of $\xi_{t}$ does not impact the result. Hence, we have $V_{t} = X_{t} = {{\alpha_{t}X_{1}} + {\beta_{t}\xi}}$. To show the equivalence of and, we just need to verify that ${\overset{˙}{X}}_{t} = {\overset{\sim}{Y}}_{t}$.

where in $\overset{(\ast)}{=}$ we used that $\eta_{t} = {- \frac{{\overset{˙}{\alpha}}_{t}}{\alpha_{t}}}$ and $\sigma_{t}^{2} = {2\beta_{t}^{2}\left( {\frac{{\overset{˙}{\alpha}}_{t}}{\alpha_{t}} - \frac{{\overset{˙}{\beta}}_{t}}{\beta_{t}}} \right)}$ which can be derived from. ∎

## Related Works and Discussion

### Learning one-step models

GANs, VAEs, and (discrete-time) normalizing flows have been three classical approaches for learning deep generative models. GANs have been most successful in terms of generation qualities (for images in particular), but suffer from the notorious training instability and mode collapse issues due to use of minimax updates. VAEs and normalizing flows are both trained based on the principle of maximum likelihood estimation (MLE) and need to introduce constraints on the model architecture and/or special approximation techniques to ensure tractable likelihood computation: VAEs typically use a conditional Gaussian distribution in addition to the variational approximation of the likelihood; normalizing flows require to use specially designed invertible architectures and need to copy with calculating expensive Jacobian matrices.

The reflow+distillation approach in this work provides another promising approach to training one-step models, avoiding the minimax issues of GANs and the intractability issues of the likelihood-based methods.

### Learning ODEs: MLE and PF-ODEs

There are two major approaches for learning neural ODEs: the PF-ODEs/DDIM approach discussed in Section 2.3, and the more classical MLE based approach of.

*$\bullet$ The MLE approach.* In, neural ODEs are trained for learning generative models by maximizing the likelihood of the distribution of the ODE outcome $Z_{1}$ at time $t = 1$ under the data distribution $\pi_{1}$. Specifically, with observations from $\pi_{1}$, it estimates a neural drift $v$ of an ODE ${dZ_{t}} = {v{(Z_{t},t)}dt}$ by

where ${\mathbb{D}}{( \cdot; \cdot )}$ denotes KL divergence (or other discrepancy measures), and $\rho^{v,\pi_{0}}$ is the density of $Z_{1}$ following ${dZ_{t}} = {v{(Z_{t},t)}dt}$ from $Z_{0} \sim \pi_{0}$; the density of $\pi_{0}$ should be known and tractable to calculate.

By using an instantaneous change of variables formula, it was observed in that the likelihood of neural ODEs are easier to compute than the discrete-time normalizing flow without constraints on the model structures. However, this MLE approach is still computationally expensive for large scale models as it requires repeated simulation of the ODE during each training step. In addition, as the optimization procedure of MLE requires to backpropagate through time, it can easily suffer the gradient vanishing/exploding problem unless proper regularization is added.

Another fundamental problem is that the MLE of neural ODEs is theoretically under-specified, because MLE only concerns matching the law of the final outcome $Z_{1}$ with the data distribution $\pi_{1}$, and there are infinitely many ODEs to achieve the same output law of $Z_{1}$ while traveling through different paths. A number of works have been proposed to remedy this by adding regularization terms, such as these based on transport costs, to favor shorter paths; see. With a regularization term, the ODE learned by MLE would be implicitly determined by the initialization and other hyper-parameters of the optimizer used to solve.

*$\bullet$ Probability Flow ODEs.* The method of PF-ODEs and DDIM provides a different approach to learning ODEs that avoids the main disadvantages of the MLE approach, including the expensive likelihood calculation, training-time simulation of the ODE models, and the need of backpropagation through time. However, because PF-ODEs and DDIM were derived as the side product of learning the mathematically more involved diffusion/SDE models, their theories and algorithm forms were made unnecessarily restrictive and complicated. The nonlinear rectified flow framework shows that the learning of ODEs can be approached directly in a very simple way, allowing us to identify the canonical case of linear rectified flow and open the door of further improvements with flexible and decoupled choices of the interpolation curves $X_{t}$ and initial distributions $\pi_{0}.$

Viewed through the general non-linear rectified flow framework, the computational and theoretical drawbacks of MLE can be avoided because we can simply pre-determines the "roads" that the ODEs should travel through by specifying the interpolation curve $X_{t}$, rather than leaving it for the algorithm to figure out implicitly. It is theoretically valid to pre-specify any interpolation $X_{t}$ because the neural ODE is highly over-parameterized as a generative model: when $v$ is a universal approximator and $\pi_{0}$ is absolutely continuous, the distribution of $Z_{1}$ can approximate any distribution given any fixed interpolation curve $X_{t}$. The idea of rectified flow is to the simplest geodesic paths for $X_{t}$.

### Learning SDEs with denoising diffusion

Although the scope of this work is limited to learning ODEs, the score-based generative models and denoising diffusion probability models (DDPM) are of high relevance as the basis of PF-ODEs and DDIM. The diffusion/SDE models trained with these methods have been found outperforming GANs in image synthesis in both quality and diversity. Notably, thanks to the stable and scalable optimization-based training procedure, the diffusion models have successfully used in huge text-to-image generation models with astonishing results \e.g.,. It has been quickly popularized in other domains, such as video \e.g. music, audio \e.g. and text, and more tasks such as image editing. A growing literature has been developed for improving the inference speed of denoising diffusion models, an example of which is the PF-ODEs/DDIM approach which gains speedup by turning SDEs into ODEs. We provide below some examples of recent works, which is by no mean exhaustive.

*$\bullet$ Improved training and inference.* A line of works focus on improving the inference and sampling procedure of denoising diffusion models. For example, presents a few simple modifications of DDPM to improve the likelihood, sampling speed, and generation quality. systematic exams the design space of diffusion generative models with empirical studies and identifies a number of training and inference recipes for better generative quality with fewer sampling steps. proposes a diffusion exponential integrator sampler for fast sampling of diffusion models. provides a customized high order solver for PF-ODEs. provides an analytic estimate of the optimal diffusion coefficient.

*$\bullet$ Combination with other methods.* Another direction is to speed up diffusion models by combining them with GANs and other generative models. DDPM Distillation accelerates the inference speed by distilling the trajectories of a diffusion model into a series of conditional GANs. The truncated diffusion probabilistic model (TDPM) of trains a GAN model as $\pi_{0}$ so that the diffusion process can be truncated to improve the speed; the similar idea was explored in, and provides an analysis on the optimal truncation time. learns a denoising diffusion model in the latent spaces and combines it with variational auto-encoders. These methods can be potentially applied to rectified flow to gain similar speedups for learning neural ODEs.

*$\bullet$ Unpaired Image-to-Image translation.* The standard denoising diffusion and PF-ODEs methods focus on the generative task of transferring a Gaussian noise ($\pi_{0}$) to the data ($\pi_{1}$). A number of works have been proposed to adapt it to transferring data between arbitrary pairs of source-target domains. For example, SDEdit synthesizes realistic images guided by an input image by first adding noising to the input and then denoising the resulting image through a pre-trained SDE model. proposes a method to guide the generative process of DDPM to generate realistic images based on a given reference image. leverages two two PF-ODEs for image translation, one translating source images to a latent variable, and the other constructing the target images from the latent variable. proposes an energy-guided approach that employs an energy function pre-trained on the source and target domains to guide the inference process of a pretrained SDE for better image translation. In comparison, our framework shows that domain transfer can be achieved by essentially the same algorithm as generative modeling, by simply setting $\pi_{0}$ to be the source domain.

*$\bullet$ Diffusion bridges.* Some recent works show that the design space of denoising diffusion models can be made highly flexible with the assistant of diffusion bridge processes that are pinned to a fixed data point at the end time. This reduces the design of denoising diffusion methods to constructing a proper bridge processes. The bridges in Song et al. are constructed by a time-reversal technique, which can be equivalently achieved by Doob's $h$-transform as shown in, and more general construction techniques are discussed in. Despite the significantly extended design spaces, an unanswered question is what type of diffusion bridge processes should be preferred. This question is made challenging because the presence of diffusion noise and the need of advanced stochastic calculus tools make it hard to intuit how the methods work. By removing the diffusion noise, our work makes it clear that straight paths should be preferred. We expect that the idea can be extended to provide guidance on designing optimal bridge processes for learning SDEs.

*$\bullet$ Schrodinger bridges.* Another body of works leverages Schrodinger bridges (SB) as an alternative approach to learning diffusion generative models. These approaches are attractive theoretically, but casts significant computational challenges for solving the Schrodinger bridge problem.

### Re-thinking the role of diffusion noise

The introduction of diffusion noise was consider essential due to the key role it plays in the derivations of the successful methods. However, as rectified flow can achieve better or comparable results with a ODE-only framework, the role of diffusion mechanisms should be re-examed and clearly decoupled from the other merits of denoising diffusion models. The success of the denoising diffusion models may be mainly attributed to the simple and stable optimization-based training procedure that allows us to avoid the instability issues and the need of case-by-case tuning of GANs, rather than the presence of diffusion noises.

Because our work shows that there is no need to invoke SDE tools if the goal is to learn ODEs, the remaining question is whether we should learn an ODE or an SDE for a given problem. As already argued by a number of works, ODEs should be preferred over SDEs in general. Below is a detailed comparison between ODEs and SDEs.

$\bullet$ *Conceptual simplicity and numerical speed.* SDEs are more mathematically involved and are more difficult to understand. Numerical simulation of ODEs are simpler and faster than SDEs.

$\bullet$ *Time reversibility.* It is equally easy to solve the ODEs forwardly and backwardly. In comparison, the time reversal of SDEs \e.g., is more involved theoretically and may not be computationally tractable.

$\bullet$ *Latent spaces.* The couplings $(Z_{0},Z_{1})$ of ODEs are deterministic and yield low transport cost in the case of rectified flows, hence providing a good latent space for representing and manipulating outputs. Introducing diffusion noises make $(Z_{0},Z_{1})$ more stochastic and hence less useful. In fact, the $(Z_{0},Z_{1})$ given by DDPM and the SDEs of and hence useless for latent presentation.

$\bullet$ *Training difficulty.* There is no reason to believe that training an ODE is harder, if not easier, than training an SDE sharing the same marginal laws: the training loss of both cases would share the distributions of covariant and differ only on the targets. In the setting of, the two loss functions and are equivalent upto a linear reparameterization.

$\bullet$ *Expressive power.* As every SDE can be converted into an ODE that has the same marginal distribution using the techniques in (see also ), ODEs are as powerful as SDEs for representing marginal distributions, which is what needed for the transport mapping problems considered in this work. On the other hand, SDEs may be preferred if we need to capture richer time-correlation structures.

$\bullet$ *Manifold data.* When equipped with neural network drifts, the outputs of ODEs tend to fall into a smooth low dimensional manifold, a key inductive for structured data in AI such as images and text. In comparison, when using SDEs to model manifold data, one has to carefully anneal the diffusion noise to obtain smooth outcomes, which causes slow computation and a burden of hyperparameter tuning. SDEs might be more useful in for modeling highly noisy data in areas like finance and economics, and in areas that involve diffusion processes physically, such as molecule simulation.

### Optimal vs. straight transport

Optimal transport has been extensively explored in machine learning as a powerful way to compare and transfer between probability measures. For the transport mapping problem considered in this work, a natural approach is to finding the optimal coupling $(Z_{0},Z_{1})$ that minimizes a transport cost ${\mathbb{E}}{\lbrack{c{({Z_{1} - Z_{0}})}}\rbrack}$ for a given $c$. The most common choice of $c$ is the quadratic cost ${c{( \cdot )}} = \left. \parallel \cdot \parallel \right.^{2}$.

However, finding the optimal couplings, especially for high dimensional continuous measures, is highly challenging computationally and is the subject of active research; see for example. In addition, although the optimal couplings are known to have nice smoothness and other regularity properties, it is not necessary to accurately find the optimal coupling because the transport cost do not exactly align with the learning performance of individual problems; see e.g.,.

In comparison, our reflow procedure finds a straight coupling, which is not optimal w.r.t. a given $c$ (see Section 3.4). From the perspective of fast inference, all straight couplings are equally good because they all yield straight rectified flows and hence can be simulated with one Euler step.

## Experiments

We start by studying the impact of reflow on toy examples. After that, we demonstrate that with multiple times of reflow, rectified flow achieves state-of-the-art performance on CIFAR-10. Moreover, it can also generate high-quality images on high-resolution image datasets. Going beyond unconditioned image generation, we apply our method to unpaired image-to-image translation tasks to generate visually high-quality image pairs.

### Algorithm

We follow the procedure in Algorithm 1. We start with drawing ${(X_{0},X_{1})} \sim {\pi_{0} \times \pi_{1}}$ and use it to get the first rectified flow ${\mathbf{Z}}^{1}$ by minimizing. The second rectified flow ${\mathbf{Z}}^{2}$ is obtained by the same procedure except with the data replaced by the draws from $(Z_{0}^{1},Z_{1}^{1})$, obtained by simulating the first rectified flow ${\mathbf{Z}}^{1}$. This process is repeated for $k$ times to get the *$k$-rectified flow* ${\mathbf{Z}}^{k}$. Finally, we can further distill the *$k$-rectified flow* ${\mathbf{Z}}^{k}$ into a one step model $z_{1} = {z_{0} + {v{(z_{0},0)}}}$ by fitting it on draws from $(Z_{0}^{k},Z_{1}^{k})$.

By default, the ODEs are simulated using the vanilla Euler method with constant step size $1/N$ for $N$ steps, that is, ${\hat{Z}}_{t + {1/N}} = {{\hat{Z}}_{t} + {{v{({\hat{Z}}_{t},t)}}/N}}$ for $t \in {{\{ 0,\ldots,N\}}/N}$. We use the Runge-Kutta method of order 5 from Scipy, denoted as, which adaptively decide the step size and number of steps $N$ based on user-specified relative and absolute tolerances. In our experiments, we stick to the same parameters as.

### Toy Examples

To accurately illustrate the theoretical properties, we use the non-parametric estimator $v^{X,h}{(z,t)}$ in in the toy examples in Figure 2, 3, 4, 5. In practice, we approximate the expectation in an nearest neighbor estimator: given a sample ${\{ x_{0}^{(i)},x_{1}^{(i)}\}}_{i}$ drawn from $(X_{0},X_{1})$, we estimate $v^{X}$ by

where ${knn}{(z,m)}$ denotes the top $m$ nearest neighbors of $z$ in ${\{ x_{t}^{(i)}\}}_{i}$. We find that the results are not sensitive to the choice of $m$ and the bandwidth $h$ (see Figure 7). We use $h = 1$ and $m = 100$ by default. The flows are simulated using Euler method with a constant step size of $1/N$ for $N$ steps. We use $N = 100$ steps unless otherwise specified.

Alternatively, $v^{X}$ can be parameterized as a neural network and trained with stochastic gradient descent or Adam. Figure 7 shows an example of when $v^{X}$ is parameterized as an 2-hidden-layer fully connected neural network with 64 neurons in both hidden layers. We see that the neural networks fit less perfectly with the linear interpolation trajectories (which should be piece-wise linear in this toy example). As shown in Figure 7, we find that enhancing the smoothness of the neural networks (by increasing the L2 regularization coefficient during training) can help straighten the flow, in addition to the rectification effect.

Figure 7: Rectified flows fitted with neural networks trained with different L2 penalty (left), and kernel estimator with different bandwidth h (right). π0: red dots; π1: purple dots.

In Figure 3 of Section 2.2, the straightness is calculated as the empirical estimation of based on the simulated trajectories. The relative transport cost is calculated based on ${\{ z_{0}^{(i)},z_{1}^{(i)}\}}_{i = 1}^{n}$ drawn from $(Z_{0},Z_{1})$ by simulating the flow, as ${\frac{1}{n}{\sum_{i = 1}^{n}\left. \parallel{z_{1}^{(i)} - z_{0}^{(i)}}\parallel \right.^{2}}} - \left. \parallel{z_{1}^{(i^{\ast})} - z_{0}^{(i)}}\parallel \right.^{2}$, where $z_{1}^{(i^{\ast})}$ is the optimal L2 assignment of $z_{0}^{(i)}$ obtained by solving the discrete L2 optimal transport problem between $\{ z_{0}^{(i)}\}$ and $\{ z_{1}^{(i)}\}$. We should note that this metric is only useful in low dimensions, as it tends to be identically zero in high dimensional cases even $v^{X}$ is set to be a random neural network. This misleading phenomenon is what causes to make the false hypothesis that DDIM yields L2 optimal transport.

### Unconditioned Image Generation

We test rectified flow for unconditioned image generation on CIAFR-10 and a number of high resolution datasets. The methods are evaluated by the quality of generated images by Fréchet inception distance (FID) and inception score (IS), and the diversity of the generated images by the recall score following.

### Experiment settings

For the purpose of generative modeling, we set $\pi_{0}$ to be the standard Gaussian distribution and $\pi_{1}$ the data distribution. Our implementation of rectified flow is modified upon the open-source code of. We adopt the U-Net architecture of DDPM++ for representing the drift $v^{X}$, and report in Table 1 (a) and Figure 8 the results of our method and the (sub)-VP ODE from using the same architecture. Other recent results using different network architectures are shown in Table 1 (b) for reference. More detailed settings can be found in the Appendix.

One-Step Generation (Euler solver, N=1)

1-Rectified Flow (+Distill)

2-Rectified Flow (+Distill)

3-Rectified Flow (+Distill)

sub-VP ODE (+Distill)

Full Simulation (Runge–Kutta (), Adaptive N)

GAN with U-Net

Denoising Diffusion GAN (T=1)

One Step Generation (Euler solver, N=1)

NCSN++ (VE ODE) (+Distill)

Full Simulation (Runge–Kutta (), Adaptive N)

Full Simulation (Euler solver)

(a) Results using the DDPM++ architecture.
(b) Recent results with different architectures reported in literature.

Table 1: Results on unconditioned image generation. Fréchet Inception Distance (FID) and Inception Score (IS) measure the quality of the generated images, and recall score measures diversity. The number of function evaluation (NFE) denotes the number of times we need to call the main neural network during inference. It coincides with the number of discretization steps N for ODE and SDE models.

(a) FID and Recall vs. Number of Euler discretization steps N
(b) FID and Recall vs. Training Iterations

Figure 8: (a) Results of rectified flows and (sub-)VP ODE on with different number N of Euler discretization steps. (b) The FID and recall during different reflow and training steps. In (a), k-Distilled refers to the one-step model distilled from k-Rectified Flow for k = 1, 2, 3.

### Results

*$\bullet$ Results of fully solved ODEs.* As shown in Table 1 (a), the 1-rectified flow trained on the DDPM++ architecture, solved with, yields the lowest FID ($2.58$) and highest recall ($0.57$) among all the ODE-based methods. In particular, the recall of 0.57 yields a substantial improvement over existing ODE and GAN methods. Using the same ODE solver, rectified flows require fewer steps to generate the images compared with VE, VP, sub-VP ODEs. The results are comparable to the fully simulated (sub-)VP SDE, which yields simulation cost.

Figure 9: The straightening effect on. Left: the straightness measure on different reflow steps and training iterations. Right: trajectories of randomly sampled pixels following 1- and 2-rectified flow.

*$\bullet$ Results on few and single step generation.* As shown in Figure 8, the reflow procedure substantially improves both FID and recall in the small step regime (e.g., $N \lessapprox 80$), even though it worsens the results in the large step regime due to the accumulation of error on estimating $v^{x}$. Figure 8 (b) show that each reflow leads to a noticeable improvement in FID and recall. For one-step generation $({N = 1})$, the results are further boosted by distillation (see the stars in Figure 8 (a)). Overall, the distilled $k$-Rectified Flow with $k = {1,2,3}$ yield one-step generative models beating all previous ODEs with distillation; they also beat the reported results of one-step models with similar U-net type architectures trained using GANs (see the *GAN with U-Net* in Table 1 (b)).

In particular, the distilled 2-rectified flow achieves an FID of $4.85$, beating the best known one-step generative model with U-net architecture, $8.91$ (TDPM, Table 1 (b)). The recalls of both 2-rectified flow ($0.50$) and 3-rectified flow ($0.51$) outperform the best known results of GANs ($0.49$ from StyleGAN2+ADA) showing an advantage in diversity. We should note that the reported results of GANs have been carefully optimized with special techniques such as adaptive discriminator augmentation (ADA), while our results are based on the vanilla implementation of rectified flow. It is likely to further improve rectified flow with proper data augmentation techniques, or the combination of GANs such as those proposed by TDPM and denoising diffusion GAN.

*$\bullet$ Reflow straightens the flow.* Figure 9 shows the reflow procedure decreases improves the straightness of the flow on. In Figure 10 visualizes the trajectories of 1-rectified flow and 2-rectified flow on the AFHQ cat dataset: at each point $z_{t}$, we extrapolate the terminal value at $t = 1$ by ${\hat{z}}_{1}^{t} = {z_{t} + {{({1 - t})}v{(z_{t},t)}}}$; if the trajectory of ODE follows a straight line, ${\hat{z}}_{1}^{t}$ should not change as we vary $t$ when following the same path. We observe that ${\hat{z}}_{1}^{t}$ is almost independent with $t$ for 2-rectified flow, showing the path is almost straight. Moreover, even though 1-rectified flow is not straight with ${\hat{z}}_{1}^{t}$ over time, it still yields recognizable and clear images very early ($t \approx 0.1$). In comparison, it is need $t \approx 0.6$ to get a clear image from the extrapolation of sub-VP ODE.

### High-resolution image generation

Figure 11 shows the result of 1-rectified flow on image generation on high-resolution ($256 \times 256$) datasets, including LSUN Bedroom, LSUN Church, CelebA HQ to AFHQ Cat. We can see that it can generate high quality results across the different datasets. Figure 1 & 10 show that 1-(2-)rectified flow yields good results within one or few Euler steps.

Figure 12 shows a simple example of image editing using 1-rectified flow: We first obtain an unnatural image $z_{1}$ by stitching the upper and lower parts of two natural images, and then run 1-rectified flow backwards to get a latent code $z_{0}$. We then modify $z_{0}$ to increase its likelihood under $\pi_{0}$ (which is $\mathcal{N}{(0,I)}$) to get more naturally looking variants of the stitched image.

Figure 10: Sample trajectories zt of different flows on the AFHQ Cat dataset, and the extrapolation ẑ1t = zt + (1−t) v (zt,t) from different zt. The same random seed is adopted for all three methods. The ẑ1t of 2-rectified flow is almost independent with t, indicating that its trajectory is almost straight.

Figure 11: Examples of 256 × 256 images generated by 1-rectified flow.

Figure 12: An example of image editing using 1-rectified flow. Here, we stitch the images of a white cat and a black cat into an unnatural image (denoted as z1). We simulate the ODE reversely from z1 to get the latent code z0. Because z1 is not a natural image, z0 should have low likelihood under π0 = 𝒩 (0,I). Hence, we move z0 towards the high probability region of π0 to get z0′ and solve the ODE forwardly to get a more realistically looking image z1′. The modification can be done deterministically by improving the π0-likelihood via z0′ = α z0 with α ∈, or stochastically by Langevin dynamics, which yields a formula of $z_{0}^{\prime} = {{\alphaz_{0}} + {\sqrt{1 - \alpha^{2}}\xi}}$ with ξ ∼ 𝒩 (0,I).

(A) Cat → Wild Animals
(B) Wild Animals → Cat
(C) MetFace → CelebA Face
(D) CelebA Face → MetFace

Figure 13: Samples of 1-rectified flow simulated with N = 100 Euler steps between different domains.

Figure 14: Samples of results of 1- and 2-rectified flow simulated with N = 1 and N = 100 Euler steps.

### Image-to-Image Translation

Assume we are given two sets of images of different styles (a.k.a. domains), whose distributions are denoted by $\pi_{0},\pi_{1}$, respectively. We are interested in transferring the style (or other key characteristics) of the images in one domain to the other domain, in the absence of paired examples. A classical approach to achieving this is cycle-consistent adversarial networks (a.k.a. CycleGAN), which jointly learns a forward and backward mapping $F,G$ by minimizing the sum of adversarial losses on the two domains, regularized by a cycle consistency loss to enforce ${F{({G{(x)}})}} \approx x$ for all image $x$.

By constructing the rectified flow of $\pi_{0}$ and $\pi_{1}$, we obtain a simple approach to image translation that requires no adversarial optimization and cycle-consistency regularization: training the rectified flow requires a simple optimization procedure and the cycle consistency is automatically in flow models satisfied due to reversibility of ODEs.

As the main goal here is to obtain good visual results, we are not interested in faithfully transferring $X_{0} \sim \pi_{0}$ to an $X_{1}$ that exactly follows $\pi_{1}$. Rather, we are interested in transferring the image styles while preserving the identity of the main object in the image. For example, when transferring a human face image to a cat face, we are interested in getting a unrealistic face of human-cat hybrid that still "looks like" the original human face.

To achieve this, let $h{(x)}$ be a feature mapping of image $x$ representing the styles that we are interested in transferring. Let $X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}$. Then $H_{t} = {h{(X_{t})}}$ follows an ODE of ${{dH_{t}} = {{\nabla h}{(X_{t})}^{\top}{({X_{1} - X_{0}})}dt}}.$ Hence, to ensure that the style is transferred correctly, we propose to learn $v$ such that $H_{t}^{\prime} = {h{(Z_{t})}}$ with ${dZ_{t}} = {v{(Z_{t},t)}dt}$ approximates $H_{t}$ as much as possible. Because ${dH_{t}^{\prime}} = {{\nabla h}{(Z_{t})}^{\top}v{(Z_{t},t)}dt}$, we propose to minimize the following loss:

In practice, we set $h{(x)}$ to be latent representation of a classifier trained to distinguish the images from the two domains $\pi_{0},\pi_{1}$, fine-tuned from a pre-trained ImageNet model. Intuitively, ${\nabla_{x}h}{(x)}$ serves as a saliency score and re-weights coordinates so that the loss in focuses on penalizing the error that causes significant changes on $h$.

(a) 1-rectified flow between different domains
(b) 1- and 2-rectified flow for MetFace → Cat.

Figure 15: (a) Samples of trajectories zt of 1- and 2-rectified flow for transferring between different domains.

### Experiment settings

We set the domains $\pi_{0},\pi_{1}$ to be pairs of the AFHQ, MetFace and CelebA-HQ dataset. For each dataset, we randomly select $80\%$ as the training data and regard the rest as the test data; and the results are shown by initializing the trained flows from the test data. We resize the image to $512 \times 512$. The training and network configurations generally follow the experiment settings in Section 5.2. See the appendix for detailed descriptions.

### Results

Figure 1, 13, 14, 15 show examples of results of 1- and 2-rectified flow simulated with Euler method with different number of steps $N$. We can see that rectified flows can successfully transfer the styles and generate high quality images. For example, when transferring cats to wild animals, we can generate diverse images with different animal faces, e.g., fox, lion, tiger and cheetah. Moreover, with one step of reflow, 2-rectified flow returns good results with a single Euler step ($N = 1$). See more examples in Appendix.

### Domain Adaptation

A key challenge of applying machine learning to real-world problems is the domain shift between the training and test datasets: the performance of machine learning models may degrade significantly when tested on a novel domain different from the training set. Rectified flow can be applied to transfer the novel domain ($\pi_{0}$) to the training domain ($\pi_{1}$) to mitigate the impact of domain shift.

### Experiment settings

We test the rectified flow for domain adaptation on a number of datasets. DomainNet is a dataset of common objects in six different domain taken from DomainBed. All domains from DomainNet include 345 categories (classes) of objects such as Bracelet, plane, bird and cello. Office-Home is a benchmark dataset for domain adaptation which contains 4 domains where each domain consists of 65 categories. To apply our method, first we map both the training and testing data to the latent representation from final hidden layer of the pre-trained model, and construct the rectified flow on the latent representation. We use the same DDPM++ model architecture for training. For inference, we set the number of steps of our flow model as $100$ using uniform discretization. The methods are evaluated by the prediction accuracy of the transferred testing data on the classification model trained on the training data.

### Results

As demonstrated in Table 2, the 1-rectified flow shows state-of-the-art performance on both DomainNet and OfficeHome. It is better or on par with the previous best approach (Deep CORAL ), while sustainably improve over all other methods.

Table 2: The accuracy of the transferred testing data using different methods, on the OfficeHome and DomainNet dataset. Higher accuracy means the better performance.
