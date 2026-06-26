<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Introduction to Zero-Order Optimization Techniques for Robotics

Topics include Trajectory optimization, Robotics, Optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Zero-order optimization techniques are becoming increasingly popular in robotics due to their ability to handle non-differentiable functions and escape local minima. These advantages make them particularly useful for trajectory optimization and policy optimization. In this work, we propose a mathematical tutorial on random search. It offers a simple and unifying perspective for understanding a wide range of algorithms commonly used in robotics. Leveraging this viewpoint, we classify many trajectory optimization methods under a common framework and derive novel competitive RL algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, zero-order (or derivative-free) optimization techniques have gained a lot of popularity in the robotics community. While zero-order optimization is a well-established field, its widespread deployment in robotics has only been made possible by recent advances in parallel computing and GPU hardware. These improvements have made it possible to deploy sampling-based Model Predictive Control (MPC) on complex robotic systems. In parallel, Reinforcement Learning (RL) has emerged as a powerful tool and has demonstrated state-of-the-art capabilities in locomotion or manipulation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

While these approaches may appear unrelated at first, they share a common property: they do not require access to the simulator's gradients. This characteristic allows them to optimize non-smooth objective functions, which typically arise in problems involving contact, such as locomotion or manipulation. Another benefit is that it avoids the tedious development of efficient gradient implementations. Furthermore, while deterministic gradient-based algorithms, such as gradient descent or Newton's method, are prone to getting stuck in local minima, zero-order techniques are mostly stochastic, which can help escape local minima.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Zero-order optimization has a long history. In its most generic form, zero-order optimization performs a random search by generating samples at random and updating an estimate of the optimal solution based on the performance of each sample. In the 1970s, Evolutionary Strategies (ES) gained popularity and later culminated with the CMA-ES algorithm. In TO, predictive sampling is a well-known and simple random search technique. Another popular algorithm is MPPI, which was initially derived using information-theoretic arguments. In RL, Reinforce was one of the first major algorithms proposed for continuous action space problems. These algorithms have since inspired many variations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While most of these algorithms have strong theoretical foundations, this is not always widely recognized within the robotics community. One reason for this is that these algorithms often lie at the intersection of many fields, such as optimization, statistics, machine learning, and control. By bringing together results from these areas, our goal is both to bring to light the theoretical properties of existing algorithms and to leverage this understanding to design novel algorithms for robotics.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, introduced Gaussian smoothing and understood random search from an optimization perspective. Inspired by this work, we propose a unified perspective to understand the zero-order optimization techniques that are popular in the robotics community. More specifically, we are interested in algorithms that can find solutions to the following problem: This formulation encompasses a wide range of problems encountered in robotics, such as TO and RL. Both of these techniques define a high-level goal through a cost function that has to be minimized (or a reward function that has to be maximized). However, they differ in the optimization space. TO optimizes directly over trajectories (i.e. a finite-dimensional sequence of vectors), whereas RL optimizes over policies (i.e. functions, which are infinite-dimensional objects). Furthermore, they differ in the way they are deployed. These algorithms can be used either online (i.e. executed at runtime) or offline. On one hand, TO can either be solved online in an MPC loop or solved offline to generate data to train a policy. On the other hand, recent RL successes relied heavily on offline training in simulation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

While these differences may seem fundamental, we show that the algorithms used to solve these problems share many conceptual similarities.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the trajectory optimization community, several works have studied derivative-free algorithms and established connections among them. For instance, first showed the similarities between MPPI and CMA-ES. Later, understood MPPI as an approximate gradient method and connected MPPI to diffusion models. Our work builds on these insights and proposes a unifying framework to understand these algorithms. In addition, we shed light on the connection between MPPI and recent results showcasing the benefits of the log-sum-exp transform. Lastly, we benchmark several state-of-the-art approaches on various robotic examples.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the RL community, first explored the use of random search in the parameter space of policies as an alternative to traditional RL algorithms. In this work, we instead investigate how random search techniques can explain the success of popular RL algorithms. More recently, drew the connection between policy gradient techniques and Nesterov's random search. However, these works used this insight to derive TO algorithms based on random search. In contrast, we study how to leverage this understanding to derive novel RL algorithms. Lastly, we refer the reader to for comprehensive surveys on the connection between RL and ES techniques.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Overall, a broad perspective connecting gradient-free approaches in TO and RL is missing. To bridge this gap, we propose a mathematical introduction to zero-order optimization algorithms used in robotics. This unified treatment provides a simple way to understand techniques such as MPPI, Covariance Matrix Adaptation (CMA), and RL policy gradient methods. In addition, we show how this unified view allows us to naturally derive novel competitive methods as a byproduct. Lastly, we discuss the theoretical concepts explaining why stochastic algorithms are well-suited to avoid getting stuck in local minima.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Section II introduces the main concepts of random search and sampling-based gradient approximation. Section III connects popular TO algorithms to random search. Section IV investigates the connections between Gaussian smoothing and RL. Section V discusses how to improve the sample efficiency of these algorithms by relying on a population of samples. Lastly, Section VI briefly reviews existing parallel computing libraries.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Random search", "weight": 1.0} -->

In this section, we introduce how a population of samples (or particles) can be used to search for global solutions. The algorithms presented here will serve as building blocks for the understanding of widely used TO and RL algorithms. Depending on the context, the samples may correspond to trajectories in TO or to policy parameters in RL.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Simple random search", "weight": 1.0} -->

First, we study two basic random search approaches: global search and local search algorithms. Although rarely used in practice, their convergence guarantees help to understand more sophisticated algorithms.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A1 Pure (or Global) Random Search", "weight": 1.0} -->

The most naive random search approach consists of iteratively sampling points at random. If the sampled point has a value lower than the current best, it is kept as the new best guess; otherwise, it is discarded. This method, known as Pure Random Search, is summarized in Algorithm 1 Random Search ‣ II-A Simple random search ‣ II Random search ‣ An Introduction to Zero-Order Optimization Techniques for Robotics").

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A1 Pure (or Global) Random Search", "weight": 1.0} -->

2 while stopping criterion is not met do Algorithm 1 Pure Random Search Interestingly, the sampling distribution of Algorithm 1 Random Search ‣ II-A Simple random search ‣ II Random search ‣ An Introduction to Zero-Order Optimization Techniques for Robotics") ignores all the previous estimates. For this reason, it is sometimes referred to as a global algorithm. Under some mild conditions on the objective function, Algorithm 1 Random Search ‣ II-A Simple random search ‣ II Random search ‣ An Introduction to Zero-Order Optimization Techniques for Robotics") converges to a global minimum. Unfortunately, in practice, this method performs poorly as it is subject to the curse of dimensionality. That is to say, the number of function evaluations required to find a global solution grows exponentially with the dimension of the problem.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A2 Greedy Local Search", "weight": 1.0} -->

A common attempt to break the curse of dimensionality is to exploit problem-specific knowledge. For instance, exploiting previous information about the shape of the function can help design an empirically more efficient algorithm. This is called Greedy Local Search. The idea is to iteratively search around the previous estimate with additive Gaussian noise, for instance. Then, as in the previous algorithm, the sample is kept only if it improves the function value. Algorithm 2 summarizes the procedure.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A2 Greedy Local Search", "weight": 1.0} -->

2 while stopping criterion is not met do Algorithm 2 Greedy Local Search By design, Algorithm 2 depends on previous estimates. For that reason, it can be referred to as a local algorithm. However, this notion should not be confused with the concepts of local and global solutions. In fact, although the convergence guarantees of Algorithm 2 are more restrictive than those of Algorithm 1 Random Search ‣ II-A Simple random search ‣ II Random search ‣ An Introduction to Zero-Order Optimization Techniques for Robotics"), it is still possible to prove the convergence of Algorithm 2 to a global solution under some regularity conditions. Consequently, both local and global searches can have global convergence guarantees. However, while both are subject to the curse of dimensionality, local search techniques can be more effective empirically. In fact, as we show next, it is well known that local search techniques relying on gradient information can exhibit strong convergence rates and guarantees in convex settings.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Random search via gradient approximation", "weight": 1.0} -->

In this section, we present various ways to perform approximate gradient descent using only function evaluations. In later sections, we show how widely used algorithms in TO and RL can be derived from the basic principles introduced here. The class of methods under study is summarized in Algorithm 3.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Random search via gradient approximation", "weight": 1.0} -->

2 while stopping criterion is not met do Sample g approximating the gradient at x. // e.g. Eq., Eq., Eq or Eq Algorithm 3 Approximate Gradient Descent Here, $\alpha$ is the step size (or learning rate). There are many ways to estimate the gradient with multiple function evaluations. Among the most widely used techniques is the forward finite difference technique: where $e_{j}\in\mathbb{R}^{n}$ represents the $j^{th}$ canonical vector and where $\mu>0$ is a scalar. Alternatively, one may use central finite differences. While this estimate can be very effective, it requires $n+1$ function evaluations, which is a limitation in high-dimensional settings.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B1 Random Coordinate Descent", "weight": 1.0} -->

One way to avoid performing that many function evaluations is Random Coordinate Descent. As its name suggests, this method alternates descent steps on random coordinates. where $j$ can be chosen uniformly at random in $\{1,\dots,n\}$. Note that $g$ depends on $x$. In the convex setting and without finite-difference approximation (i.e. with the exact gradient), Random Coordinate Descent requires, on average, at most $n$ times more steps compared to classical gradient descent. In addition, for a certain class of functions, it can require as many steps as gradient descent while requiring $n$ times fewer function evaluations. Thus, this stochastic estimate offers the hope of matching the gradient's descent performance with a few samples. Random Coordinate Descent samples discrete coordinates, but it is also possible to sample along arbitrary directions.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B2 Simultaneous Perturbation Stochastic Approximation (SPSA)", "weight": 1.0} -->

In the 1990s, Spall introduced Simultaneous Perturbation Stochastic Approximation (SPSA). The main idea is to replace finite differences with the following stochastic estimate: where each component of $\Delta$ is equal to $\pm 1$ according to independent Bernoulli distributions. Note that Spall derived SPSA using central differentiation instead of the forward finite difference. Under reasonable assumptions, SPSA can achieve performance similar to that of finite differences while requiring $n$ times fewer samples. Hence, similarly to Random Coordinate Descent, this stochastic estimate offers the hope of matching the gradient's descent performance with a few samples.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B2 Simultaneous Perturbation Stochastic Approximation (SPSA)", "weight": 1.0} -->

While both approaches lead to effective algorithms, the next technique provides a more insightful interpretation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B3 Gaussian Smoothing", "weight": 1.0} -->

propose another perspective. Instead of directly approximating the gradients of the original function, they propose studying a smoothed surrogate function where $\epsilon\sim\mathcal{N}(0,\Sigma)$. This is Gaussian smoothing, commonly referred to as randomized smoothing (RS). As $\mu$ approaches zero, $f_{\mu}$ tends to $f$. As a result, for small values of $\mu$, this surrogate only slightly changes the objective function (and therefore the minimum location) but adds smoothness. Importantly, the advantage of this surrogate is that its gradient can be evaluated via an average of function evaluations. To understand this, let's first define the constant: $\kappa=\sqrt{(2\pi)^{n}\det(\Sigma)}$, the normalization factor of the multivariate Gaussian distribution.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B3 Gaussian Smoothing", "weight": 1.0} -->

With a change of variables ($z=x+\mu\epsilon$), we can write: This allows differentiating $f_{\mu}$ without needing the gradient of the original function, $f$: With another change of variable ($\epsilon=\mu^{-1}(z-x)$), we have: Hence, the gradient of $f_{\mu}$ can be estimated using only function evaluations of the original function, $f$. However, this comes at the cost of approximating an expectation with samples. Note that the term $\mu^{-1}\Sigma^{-1}\epsilon$ is the gradient of the logarithm of the probability density function with respect to the mean; this is often called the log-likelihood trick. This is sometimes written: where $p_{m}$ is the density of the Gaussian distribution with mean $m$ and covariance $\Sigma$. This alternative view is useful for understanding the CMA algorithm, explained in Section III-C ‣ III Trajectory Optimization ‣ An Introduction to Zero-Order Optimization Techniques for Robotics").

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B3 Gaussian Smoothing", "weight": 1.0} -->

Lastly, since $\mathbb{E}\left[f(x)\Sigma^{-1}\epsilon\right]=0$, we can write: In the general case, the expectation is intractable. The idea is then to approximate the gradient of the original function with a stochastic estimate of the gradients of the surrogate. For instance, one can use the following estimate in Algorithm 3: While $\frac{1}{\mu}f(x+\mu\epsilon)\Sigma^{-1}\epsilon$ is a valid gradient estimate, it can be arbitrarily large. In contrast, the estimate is invariant to constant translations of the function. Intuitively, this reduces the variance of the estimate.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Alternatively, one may sample, $\epsilon$, from the surface of a unit sphere. This technique guarantees that the norm of the direction vectors is bounded.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In the convex setting, using the forward estimate (Eq. ) or the central estimate (Eq. ) as a gradient estimate requires at most $n$ times more iterations than the standard gradient method.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 1", "weight": 1.0} -->

To summarize, although the assumptions in vary, the underlying ideas are of the same nature; sampling along random directions may match the performance of gradient descent while requiring $n$ times fewer function evaluations.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-C Simulated Annealing", "weight": 1.0} -->

So far, we have seen that performing random approximate gradient descent can be sample efficient in the convex setting. However, one may ask whether these algorithms can converge to global solutions in nonconvex settings, as it is the case for the Greedy Local Search introduced in Algorithm 2. It is well known that, in its vanilla form, gradient descent is prone to local minima. However, additive Gaussian noise can lead to asymptotic global convergence guarantees. To understand why, we need to study the following Langevin dynamics: Here $p$ is a probability distribution, and $W_{t}$ is a Brownian motion. $\nabla_{x}\log p$ is the score function of the distribution. Note that the gradient is taken with respect to the input of $p$ (not with respect to the parameters of $p$ as in the log-likelihood trick of Gaussian smoothing). This Stochastic Differential Equation (SDE) has been extensively studied, and it can be shown that $X_{t}$ converges to the distribution defined by $p$. Consequently, this SDE can be used to sample from a distribution with probability density $p$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-C Simulated Annealing", "weight": 1.0} -->

One way to leverage this result in the context of global optimization is to choose the following probability distribution: where $\lambda>0$ is called the temperature. As $\lambda\rightarrow 0$, the distribution concentrates on the set of global minima of $f$. Furthermore, the score function of this distribution is proportional to the gradient of $f$: Then, this SDE can be discretized to derive a recursive algorithm. Following this idea, show that with an appropriate schedule of step sizes $\alpha_{k}$ and $\gamma_{k}$, the discretized Stochastic Langevin Gradient Dynamics, guarantees asymptotic convergence to global solutions. Here, $\epsilon_{k}$ is Gaussian noise and $g_{k}$ is of the form ${(\nabla f(x_{k})+\xi_{k})}$, with $\xi_{k}$ representing stochastic noise. Hence, $g_{k}$ can be interpreted as a noisy approximation of the gradient.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-C Simulated Annealing", "weight": 1.0} -->

Intuitively, the Gaussian noise $\epsilon_{k}$ helps to escape local minima. The step sizes $\alpha_{k}$ and $\gamma_{k}$ are chosen such that the corresponding SDE has a temperature $\lambda$ that tends slowly to zero. This is called Simulated Annealing. Intuitively, slowly decreasing the temperature guides the iterates towards a global solution.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-C Simulated Annealing", "weight": 1.0} -->

These results can be used to prove the global convergence of SPSA. More precisely, the iterative scheme in Equation with $g$ as the SPSA estimate defined in Equation (4 ‣ II-B Random search via gradient approximation ‣ II Random search ‣ An Introduction to Zero-Order Optimization Techniques for Robotics")) converges to a global minimum. In fact, in its default version (i.e. without additive noise), SPSA converges to a global minimum. This is because the noise of the estimate (i.e. $\xi_{k}$) is enough to escape local minima and achieve global convergence. We are not aware of such results in the context of randomized smoothing. However, we can conjecture that similar results may be valid.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-C Simulated Annealing", "weight": 1.0} -->

To summarize, we have seen that stochasticity can help gradient descent algorithms reach global solutions. Although these results are highly relevant theoretically, they have limited practical impact, as they are only asymptotic.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 2", "weight": 1.0} -->

At first glance, it might be hard to relate the discretized Langevin update to the Greedy Local Search in Algorithm 2. However, following the observation, the *if* statement ensuring a strict decrease can be related to the Metropolis-Hastings algorithm. We refer the reader to Appendix A for more details.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Trajectory Optimization", "weight": 1.0} -->

In this section, we show how random search allows us to understand derivative-free optimization algorithms that are commonly used in robotics. In practice, Trajectory Optimization aims to solve Here $x$ denotes the state, $u$ the control variable, $(c_{t})_{t}$ the running cost functions, $c_{T}$ the terminal cost function, $T$ the time horizon, and $f_{\text{dyn}}$ the dynamics. Note that we abuse the notation by using $x$ to denote the state instead of the optimization variable. Importantly, the constraints are implicit; the optimization is performed only with respect to the control variables. Therefore, this problem is unconstrained and is referred to as the single shooting approach. Ultimately, it can be written in the form of Problem. The dimension of the search space is $n=Tn_{u}$, where $n_{u}$ denotes the dimension of the control inputs.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A Predictive sampling", "weight": 1.0} -->

In robotics, Predictive sampling is one of the simplest random search approaches. This method can be seen as a variation of the Greedy Local Search (Algorithm 2). Instead of sampling one search direction, it samples $K$ search directions and keeps the best. If no direction provides an improvement, the previous estimate is kept. Algorithm 4 summarizes the procedure.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A Predictive sampling", "weight": 1.0} -->

2 while stopping criterion is not met do Sample d1, …, dK // with independent centered Gaussian distributions Algorithm 4 Predictive Sampling Importantly, all the function evaluations can be performed in parallel. While this approach can be quite effective, recent sampling-based MPC demonstrations typically rely on more sophisticated algorithms.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B The log-sum-exp transform: MPPI", "weight": 1.0} -->

Model Predictive Path Integral (MPPI) is a derivative-free TO method initially derived from an information-theoretic perspective. MPPI iteratively samples around the current guess and updates it using a weighted exponential average. More specifically, given a current guess $x$, MPPI samples $K$ variables $x_{k}$ following independent Gaussian distributions centered in $x$ (i.e. $x_{k}\sim\mathcal{N}(x,\Sigma)$). Then, it performs an update according to the following rule: where $\rho=\min_{j}f(x_{j})$ (to prevent numerical stability issues). These weights, $w_{k}$, are called Exponential Average weights. Algorithm 5 describes the complete procedure.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-B The log-sum-exp transform: MPPI", "weight": 1.0} -->

2 while stopping criterion is not met do $x\leftarrow\sum\limits_{k=1}^{K}w_{k}x_{k}$ Algorithm 5 Model-Predictive Path Integral (MPPI) Let's see how this update rule can be interpreted as a variation of Gaussian smoothing. Instead of the surrogate function defined in Equation, let's consider the (continuous) log-sum-exp transform function. where $\epsilon\sim\mathcal{N}(0,\Sigma)$ and where $\lambda>0$ is a scalar called the temperature. As $\mu$ goes to zero, we recover $f$. Therefore, the gradients of this surrogate can be used to approximate the gradients of the original function, $f$. Furthermore, as $\lambda\rightarrow\infty,f_{\mu,\lambda}\rightarrow f_{\mu}$. Consequently, this surrogate can be seen as a generalization of Gaussian smoothing.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-B The log-sum-exp transform: MPPI", "weight": 1.0} -->

The gradient of the surrogate reads: In practice, both expectations can be approximated with $K$ samples $\epsilon_{1:K}$ following the distribution $\mathcal{N}(0,\Sigma)$. This leads to the following estimate: Similarly to the randomized smoothing case, this update is invariant to additive translation of the function $f$. Let's consider $\mu=1$. We show that MPPI follows a natural gradient step: where $\alpha$ is the step size, and where $F$ is the Fisher information matrix, which is equal to the inverse of the covariance matrix for Gaussian distributions. The idea of the natural gradient is to build an update step that is invariant to changes of variables. More details on the natural gradient are provided in Appendix B. If $\alpha=\frac{1}{\lambda}$, we have As $(x+\epsilon_{k})\sim\mathcal{N}(x,\Sigma)$, we recover the MPPI update.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-B The log-sum-exp transform: MPPI", "weight": 1.0} -->

Furthermore, if $\Sigma=\sigma^{2}I$, then $\frac{\sigma^{2}}{\lambda}\leq\frac{1}{L}$, where $L$ is the Lipschitz function of the surrogate function. Therefore, the step size chosen by MPPI can be interpreted as a conservative estimate of the standard optimal step size from convex optimization.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-B The log-sum-exp transform: MPPI", "weight": 1.0} -->

To the best of our knowledge, propose the first explanation of the success of MPPI from an optimization perspective. shows that the log-sum-exp smoothing can be interpreted as an interpolation between the default randomized smoothing and the Moreau envelope. The idea is that the Moreau envelope is a better approximation than RS but is harder to compute. MPPI elegantly trades off approximation quality and computational complexity. At the cost of more samples, relying on this surrogate can improve convergence rates. Intuitively, this estimator requires many samples because of the presence of the expectation in the denominator in Equation. With the progress of parallel computing, this requirement for multiple samples might not be a limitation at all. However, using many samples renders the update step essentially deterministic, which makes the algorithm prone to getting trapped in local minima.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 3", "weight": 1.0} -->

The log-sum-exp smoothing resembles the risk-seeking control formulation. We refer the reader to Appendix C for a discussion on the topic.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The log-sum-exp smoothing is reminiscent of the simulated annealing idea. Similarly to simulated annealing, as the temperature $\lambda$ approaches $0$, the surrogate concentrates around the global minima. In fact, Therefore, applying the Langevin update to the log-sum-exp surrogate function amounts to applying Gaussian smoothing to the probability distribution proportional to $e^{-\frac{1}{\lambda}f}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-C Covariance Matrix Adaptation (CMA)", "weight": 1.0} -->

So far, we have kept the covariance matrix $\Sigma$ fixed across various iterations. However, in practice, it is not necessarily clear how to choose this parameter according to the problem. In this section, we show how to derive a Covariance Matrix Adaptation (CMA) scheme. Interestingly, the optimization of the smooth surrogate function can be interpreted as an optimization in the space of Gaussian probability distributions. Indeed, optimizing Equation can be interpreted as a search over the mean of a Gaussian distribution. More specifically, we can write: Therefore, Gaussian smoothing can be seen as the search for a Gaussian distribution that minimizes the expectation of $f$ under that distribution. This distribution can be interpreted as the belief of where the global minimum of the function $f$ might be. A natural generalization is to not only optimize the mean but also the covariance. More specifically, one can apply gradient descent to the following problem: $J(\theta)$ is minimal when the distribution $\mathcal{N}(x,\Sigma)$ concentrates around the minima of $f$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-C Covariance Matrix Adaptation (CMA)", "weight": 1.0} -->

Note that this idea does not necessarily need to rely on Gaussian distributions. Similarly to the randomized smoothing case, we can use the log-likelihood trick: Here, the gradient of the probability distribution is taken with respect to both the mean and the covariance. shows that the natural gradient update, ${\Delta\theta=F(\theta)^{-1}\nabla J(\theta)}$, can be written: Similarly to the randomized smoothing case, this update step averages quantities that rely solely on function evaluations of the original function. Following the natural gradient is especially relevant in this setting, as it is crucial that the update does not depend on the choice of parameterization of the Gaussian distribution. We refer the reader to Appendix B for more details on the natural gradient. In practice, this update step can be approximated by samples $x_{k}\sim\mathcal{N}(x,\Sigma)$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-C Covariance Matrix Adaptation (CMA)", "weight": 1.0} -->

Denoting $w_{k}=f(x_{k})$, the approximate update with a step size $\alpha$ reads This allows us to recover the CMA scheme (see Algorithm 6 ‣ III Trajectory Optimization ‣ An Introduction to Zero-Order Optimization Techniques for Robotics")). Note that it is important to update the covariance matrix first, as the covariance update must rely on the old $x$ (i.e. the one used to sample). As with Gaussian smoothing, a constant can be subtracted from $f$ without changing the expectation in Equation (28 ‣ III Trajectory Optimization ‣ An Introduction to Zero-Order Optimization Techniques for Robotics")). Therefore, another choice of weights could be $w_{k}=f(x_{k})-f(x)$, as this renders the update invariant to translations of $f$. One could go further and design an algorithm invariant to any increasing transformation of the objective by replacing $f(x_{k})$ with arbitrary weights $w_{k}$ sorted so that their order matches that of the function values $f(x_{k})$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-C Covariance Matrix Adaptation (CMA)", "weight": 1.0} -->

As pointed out, this recovers the CMA-ES algorithm (without evolution path). provides a theoretical justification for this choice of weights.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Another choice of weight could be to assign $w_{k}=\frac{1}{K_{e}}$ to the best $K_{e}$ samples and $0$ to the others (by best, we mean samples with the lowest value $f(x_{k})$). As pointed out, this elitist weighting provides an interesting connection to the well-known Cross-Entropy Method (CEM). We refer the reader to Appendix D ‣ An Introduction to Zero-Order Optimization Techniques for Robotics") for more details.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 5", "weight": 1.0} -->

An important point that we overlooked is whether the covariance update rule in Equation (III-C ‣ III Trajectory Optimization ‣ An Introduction to Zero-Order Optimization Techniques for Robotics")) maintains the matrix positive definite. If $0\leq\eta<1$, $w_{i}\geq 0$, and the weights sum to one, then the covariance matrix is always positive definite, provided that we start with a positive definite matrix. However, in practice, there is no reason that the function $f$ would be such that the weights satisfy this property.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 5", "weight": 1.0} -->

One possible solution is to design an update that operates on exponential coordinates so that the covariance matrix naturally stays positive definite. This is the idea behind xNES. Thanks to the invariant properties of the natural gradient, both update rules align when the step size approaches zero.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Another approach could be to use the log-sum-exp transformation used for MPPI. Indeed, this transformation naturally maintains the weights positive and ensures that they sum to one. We omit the derivations as it is straightforward to show that applying the natural gradient to Equation yields the update rule from Equation (III-C ‣ III Trajectory Optimization ‣ An Introduction to Zero-Order Optimization Techniques for Robotics")) with the Exponential Average weights (Equation ). We refer to this algorithm as MPPI-CMA. Table I ‣ III Trajectory Optimization ‣ An Introduction to Zero-Order Optimization Techniques for Robotics") summarizes all the possible variations of the CMA algorithm, depending on the choice of weight.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 5", "weight": 1.0} -->

When dealing with TO, it is often preferred to design algorithms that can achieve linear complexity with respect to the time horizon $T$ (Equation ). This is typically achieved by exploiting the problem's structure. One way to do so is to use a block-diagonal covariance matrix (with $T$ blocks of size $n_{u}$, where $n_{u}$ is the dimension of the control input), i.e. $\Sigma=\operatorname{blockdiag}(\Sigma_{1},\dots\Sigma_{T})$. Clearly, this makes the update rules of Predictive Sampling and MPPI easily implementable with linear complexity with respect to the time horizon.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 5", "weight": 1.0} -->

However, this is less straightforward in the case of the CMA update. Specifically, Equation (III-C ‣ III Trajectory Optimization ‣ An Introduction to Zero-Order Optimization Techniques for Robotics")) does not necessarily maintain the block-diagonal structure of the covariance matrix. This is because $\Sigma$ is not the appropriate representation to work. Instead of applying the natural gradient descent to the full matrix $\Sigma$, one can apply it to each block $\Sigma_{t}$. By construction, this approach maintains the overall covariance matrix block-diagonal. Intuitively, the natural gradient update for each block matches Equation (III-C ‣ III Trajectory Optimization ‣ An Introduction to Zero-Order Optimization Techniques for Robotics")). We refer to this approach as block-diagonal CMA and leave a formal proof of this claim for future work. Importantly, this formulation allows the CMA update to be implemented in a sequential way, ensuring linear computational complexity with respect to the time horizon $T$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 6", "weight": 1.0} -->

MPPI with block-diagonal CMA is the same as $\text{PI}^{2}$-CMA without temporal averaging.

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-D Numerical experiments", "weight": 1.0} -->

We introduce four TO benchmark problems based on Hydrax: Cartpole, DoubleCartPole, PushT, and Humanoid. Control bounds are enforced with a penalty term in the cost function. All results are averaged over six seeds. More details about the cost functions and additional visualizations are available online ^11^1 We compare the performance of Predictive Sampling, randomized smoothing, MPPI, and MPPI-CMA. All algorithms use $2048$ samples per iteration. For MPPI and MPPI-CMA, we use a temperature of $\lambda=0.1$. For the CMA update, we use a full covariance as we did not observe that this was a computational bottleneck. Nevertheless, we provide results with block-diagonal CMA in Appendix E. Furthermore, we find that MPPI-CMA performs significantly better when using a separate step size for the mean update and the covariance update. For completeness, results using a shared step size are provided in Appendix E.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Policy optimization", "weight": 1.0} -->

One of the main limitations of TO is that it is not always straightforward to use it to derive a controller. Indeed, performing MPC implies solving TO problems online, which can be extremely challenging due to limited compute time. Even though recent works were able to achieve impressive zero-order MPC demonstrations, these performances have not yet matched those obtained by RL. The main strength of current RL approaches is that they rely solely on policy evaluation at runtime. All the computations are moved offline, where the goal is to search for a policy that maximizes performance across all possible initial conditions. This can be written: where the expectation is taken over initial states $s$ and where $J(\theta,s)$ is the cost of the trajectory with initial state $s$ and with the controller $\pi_{\theta}$: $\theta$ denotes the parameters of the policy (e.g. the weights of a neural network). $r$ is the reward, $a$ is the control action. Note that we follow the RL formalism by trading the minimization of a cost function for the maximization of a reward.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Policy optimization", "weight": 1.0} -->

Furthermore, in contrast to TO, the optimization for each trajectory is done with an infinite horizon and a discount factor $\gamma$. We do not consider stochastic dynamics for simplicity, as most robotic models are deterministic (e.g. locomotion or manipulation). However, the ideas presented in this section should extend to the stochastic dynamics case. Because the policy is deterministic, RL algorithms aiming to solve formulation are called Deterministic Policy Gradient (DPG) algorithms.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 7", "weight": 1.0} -->

The formulation in Equation can easily be extended to encompass domain randomization by taking the expectation across multiple parameters of the environment.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 7", "weight": 1.0} -->

Most RL algorithms rely on stochastic policies, therefore DPG algorithms are often introduced as a special case. While stochastic policies can be relevant in the context of games or partially observable settings, most robotic applications, such as locomotion or manipulation, can be solved with deterministic policies. In fact, in practice, many works that rely on RL algorithms derived with stochastic policies generally deploy a deterministic policy on the robot. Therefore, we chose to first introduce the deterministic case and then investigate how stochastic formulations can be understood as a random search aimed at solving the deterministic case.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 7", "weight": 1.0} -->

There are two main sampling approaches to maximize. The first one is to directly rely on the zero-order techniques, which implies sampling in the parameter space of a neural network, similarly to. The second approach, used in RL, is to leverage the structure of the problem to sample from the action space. In this work, we are interested in the latter one.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-A Deterministic Policy Gradient", "weight": 1.0} -->

In the deterministic setting, the gradient can be estimated with the DPG theorem: where the $Q$-function is defined as Note that we follow the formalism of and express the policy gradient as an expectation over entire trajectories rather than making the $\gamma$-discounted state distribution explicit. Unfortunately, this formula cannot be directly implemented in an algorithm because of the presence of the $Q$-function. Indeed, the $Q$-function cannot be computed analytically. One solution is to estimate it with function approximation at each gradient descent step. Algorithms relying on this mechanism are called actor-critics. The actor refers to the policy, while the critic refers to the $Q$-function. In practice, the $Q$-function is learned in a self-supervised way via the Bellman equation. There exist many techniques to estimate the critic efficiently between gradient updates of the actor; we refer the reader to for a comprehensive treatment of the subject.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 8", "weight": 1.0} -->

A key distinction between TO and policy optimization lies in the objective function: the policy optimization objective is averaged across various initial conditions. As a result, the objective cannot be computed analytically and must instead be estimated through sampling. Consequently, gradient estimates are inherently noisy and introduce stochasticity into the optimization process. In light of our discussion on Langevin dynamics, this inherent stochasticity of RL algorithms could explain their empirical ability to avoid poor local minima.

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-B Gaussian smoothing on the $Q$-function", "weight": 1.0} -->

DDPG originally proposed to learn the $Q$-function with a neural network and directly differentiate it to obtain $\partial_{a}Q(s_{k},a_{k})$. This idea led to state-of-the-art RL algorithms such as TD3. In light of the success of randomized smoothing, a natural idea is to use Gaussian smoothing to estimate the gradient of the Q-function and to use the following estimate for the gradient of the cost: where the expectation is taken with respect to both the initial condition and the Gaussian random variables $\epsilon_{k}$. This provides us with a simple variation of actor-critics based on the DPG theorem. Algorithm summarizes the procedure.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-B Gaussian smoothing on the $Q$-function", "weight": 1.0} -->

1 while stopping criterion is not met do 4 Update the actor θ ← θ + α(Q(s, a + ϵ) − Q(s, a))∂θπθ(s)Σ−1ϵ 5 Update the critic, Q Algorithm 7 Randomized smoothing - Actor-Critic We deliberately omit the rollout logic, as well as the interplay between the actor update and the critic update. This is because our focus is solely on modifying the actor's gradient update in DPG algorithms. We do not aim to provide a novel actor-critic logic. As shown in the experimental section, this simple change can lead to competitive algorithms. An interesting variation of Algorithm 7 is to use the log-sum-exp transform and use exponential average weights in the actor update.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 9", "weight": 1.0} -->

One way to understand this algorithm is to interpret the partial derivative of the policy $\partial_{\theta}\pi_{\theta}(s)$ as a linear mapping from the action space to the policy parameter space. Consequently, the algorithm can be understood as a way to map samples from the action space into samples from the policy parameter space.

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-C Numerical experiments", "weight": 1.0} -->

In this section, we investigate the benefits of estimating the gradient of the $Q$-function in DPG algorithms such as DDPG and TD3. Our implementation relies on CleanRL and only modifies the actor's update rule. Specifically, we investigate two smoothing approaches, the default randomized smoothing (RS) and the one relying on the log-sum-exp (LSE) transform. Consequently, we benchmark DDPG and TD3 against their smoothed counterparts: RS-DDPG, LSE-DDPG, RS-TD3, and LSE-TD3. The performances are evaluated in seven MuJoCo environments. For the sampling, we use 10 samples per update, with sampling noise following a Gaussian distribution with a standard deviation of $0.1$ (the covariance matrix is proportional to the identity matrix). Our implementation is available online ^22^2 Five runs are performed for each test problem. Figure 3 presents the normalized score across all runs. The episodic return for each environment is provided in Appendix F. The results indicate that both RS-DDPG and LSE-DDPG significantly outperform DDPG, which demonstrates the benefits of smoothing.

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-C Numerical experiments", "weight": 1.0} -->

For TD3, the improvements are not as clear. This could be explained by the fact that TD3 is already a very strong algorithm and that the margin for improvement on those benchmarks is limited. Additionally, our modifications were restricted to the actor's update; achieving state-of-the-art performance would most likely require extensive hyperparameter tuning of the actor-critic mechanism. Nevertheless, the results show that deterministic policy gradient algorithms can benefit from smoothing.

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-D Connection to the Reinforce algorithm", "weight": 1.0} -->

One may ask how the update rule introduced in Equation compares to the classical Reinforce algorithm. First, let's recall how this algorithm is derived. In its most general form, Reinforce relies on the gradient of the following formulation: The policy is no longer a deterministic function but a parameterized distribution over the space of possible actions. Note that the expectation is taken over random actions. We now use capitalized letters for actions and states to emphasize their stochastic nature. The stochastic policy gradient theorem states that Note that the definition of the $Q$-function is no longer the same as in the deterministic case. It is now defined as the expectation of stochastic rollouts starting at state $s$ with action $a$. In practice, in most RL algorithms, the actions are sampled from a Gaussian probability distribution with mean $\pi_{\theta}(s)$ where $\pi_{\theta}$ is a neural network. While it is possible to also optimize the parameters of the covariance, we consider, for simplicity, a Gaussian distribution with a fixed covariance $\Sigma$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-D Connection to the Reinforce algorithm", "weight": 1.0} -->

Hence, we have: The baseline $V(S_{k})$ can be subtracted because the random variable $A_{k}-\pi_{\theta}(S_{k})$ has a zero-mean conditioned on the state. Similarly to the randomized smoothing case, this induces invariance to translation by a constant of the reward function. Interestingly, we recover a formula very similar to Equation. The only difference is that the rollouts are now stochastic. This changes two things. The first one is that the $Q$-function and the partial derivatives are now evaluated at $S_{k}$ (instead of $s_{k}$ in Equation). The second is that the definition of the $Q$-function has changed. In Equation, the $Q$-function denotes deterministic rollouts. In contrast, it is now an expectation of the outcome of stochastic rollouts.

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-D Connection to the Reinforce algorithm", "weight": 1.0} -->

The additional stochasticity in Equation (IV-D) (as compared to Equation ) can be understood as exploration noise. One formal justification could be to understand the stochastic policy in Equation as a smoothing operating in action space. Similarly to Gaussian smoothing, the smoothing allows one to derive the gradient of the cost with only $Q$-function evaluation. Consequently, the policy gradient theorem is analogous to the log-likelihood trick of Gaussian smoothing.

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-D Connection to the Reinforce algorithm", "weight": 1.0} -->

In the end, Reinforce can be seen as a way to solve the deterministic formulation introduced in Equation without the simulator's gradients by sampling in the action space. Interestingly, the smoothing of the Reinforce formulation introduces additional stochasticity as compared to Equation. It would be interesting to understand whether this extra stochasticity, which can be interpreted as exploration noise, is useful in practice. Intuitively, smoothing helps to simplify the problem, but adding too much noise might render the surrogate too different from the initial problem. Future work could explore connections to other popular stochastic policy gradient algorithms, such as TRPO or PPO.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Population based algorithms", "weight": 1.0} -->

Theoretically, sampling-based algorithms based on Langevin dynamics can generate samples from any target probability distribution. However, when applied to challenging multimodal distributions, the samples may fail to mix well and can exhibit strong autocorrelation. A natural approach to mitigate this issue is to explore algorithms that consider multiple starting points.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Population based algorithms", "weight": 1.0} -->

Thus far, all the algorithms that we have considered, either in TO or RL, have been local search techniques based on the simple greedy local search from Algorithm 2. It would be worth deriving algorithms that combine local search concepts with global ones, in the spirit of Algorithm 1 Random Search ‣ II-A Simple random search ‣ II Random search ‣ An Introduction to Zero-Order Optimization Techniques for Robotics").

<!-- chunk {"id": "body-0076", "role": "body", "section": "Population based algorithms", "weight": 1.0} -->

The most naive way to combine local and global search is to perform multiple local searches with diverse initial starting points. This is also known as Random Restart. Algorithm 8 summarizes the procedure.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Population based algorithms", "weight": 1.0} -->

2 while stopping criterion is not met do 4 x̃ ← Greedy Local Search(x̄) Algorithm 8 Random Restarts A more sophisticated approach is to perform several local searches in parallel. One way to do this is to maintain a population of $N$ samples, generate a new population by applying local search, and then select the $N$ best samples. This procedure, called $(N+\lambda)$-ES, is one of the most popular Evolutionary Strategy (ES) algorithms. Algorithm 9 summarizes this procedure. Interestingly, there are two special cases: (1 + 1)-ES is equivalent to Greedy Local Search (Algorithm 2) and (1 + $\lambda$)-ES is equivalent to Predictive sampling (Algorithm 4).

<!-- chunk {"id": "body-0078", "role": "body", "section": "Population based algorithms", "weight": 1.0} -->

Input: Initial population of N values: x1, …, xN 1 while Stopping criterion is not met do 4 x← Sample uniformly from {x1, …, xN} 5 d← Sample a centered Gaussian 8 {x1, …, xN}← the N elements in D with smallest f(x) A potential limitation of this type of approach is that many greedy local searches may converge to the same local minimum. Ideally, samples should coordinate with one another. An intuitive idea is to avoid having particles that are too close to one another. One way to do so is to perform Stein Variational Gradient Descent (SVGD). This formulation naturally encompasses a repulsion term to maintain a certain distance between particles. Although SVGD requires gradients, it is natural to use the concepts covered in the previous Sections to derive a gradient-free variation. For instance, derive a gradient-free SVGD based on CMA-ES.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Parallel computing", "weight": 1.0} -->

A common feature of zero-order TO and RL is that both require numerous function evaluations. To improve computational efficiency, a typical strategy is to parallelize these evaluations. In the machine learning community, parallel computing is well established with libraries such as JAX and PyTorch. However, in robotics, these libraries cannot be used directly, as each function evaluation relies on a simulator. Indeed, the function evaluation in Equation or Equation involves propagating the system dynamics forward in time. For this reason, parallel simulators such as MuJoCo XLA (MJX) and Isaac Sim have been developed to support massively parallel rollouts on GPUs, which makes them especially suitable for sampling-based TO and RL.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Parallel computing", "weight": 1.0} -->

On the algorithmic side, Evosax provides implementations of random search and popular ES algorithms based on JAX. These can then be used for zero-order MPC with Hydrax. Finally, CleanRL offers simple and efficient implementations of widely used RL algorithms.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we have demonstrated how random search provides a unifying perspective on zero-order algorithms commonly used in robotics. We also discussed theoretical concepts that help explain why sampling-based zero-order techniques can escape local minima. Leveraging this understanding, we proposed novel and competitive RL algorithms. These algorithms are only examples of the potential outcomes enabled by this unified viewpoint. In the future, we hope this tutorial will help the robotics community tackle open challenges such as constrained zero-order optimization and the search for global solutions.
