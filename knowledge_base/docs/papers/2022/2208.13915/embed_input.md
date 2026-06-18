<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Finite Sample Identification of Bilinear Dynamical Systems

Topics include Bilinear systems, System identification, Sample complexity, Martingale small-ball, Control-affine systems, Nonlinear dynamics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Gives finite-sample rates for learning bilinear dynamical systems from a single trajectory under a marginal mean-square stability condition. The analysis uses a martingale small-ball argument to obtain dimension- and trajectory-length-dependent rates without the instability penalties that simpler mixing arguments can introduce.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Bilinear dynamical systems are ubiquitous in many different domains and they can also be used to approximate more general control-affine systems. This motivates the problem of learning bilinear systems from a single trajectory of the system's states and inputs. Under a mild marginal mean-square stability assumption, we identify how much data is needed to estimate the unknown bilinear system up to a desired accuracy with high probability. Our sample complexity and statistical error rates are optimal in terms of the trajectory length, the dimensionality of the system and the input size. Our proof technique relies on an application of martingale small-ball condition. This enables us to correctly capture the properties of the problem, specifically our error rates do not deteriorate with increasing instability. Finally, we show that numerical experiments are well-aligned with our theoretical results.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Bilinear systems constitute an important class of nonlinear systems used in modeling systems in a variety of domains from engineering to biology. They also provide global approximators for more general nonlinear systems, and have recently been invoked in the study of Koopman operators for systems with control inputs. Due to the ubiquity of bilinear models, identification of such models from input-output data has also received interest in the literature both in continuous-time and discrete-time. However, a theoretical understanding of learning a bilinear model from a finite noisy trajectory, and in particular, how the accuracy of the learned model depends on the trajectory length is lacking. In this paper, we aim to answer this question for discrete-time bilinear models, learned from a single state-input trajectory using least squares.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is a growing body of literature on non-asymptotic properties and sample complexity of learning dynamical systems. For linear systems, the recent results include that establish that accuracy of the learned models improve at a rate ${\mathcal{O}{({1/\sqrt{T}})}},$ where $T$ is the trajectory length. These results are extended to certain classes of switched and nonlinear systems, where, with the exception of, mixing-time arguments are used to ease the statistical analysis. One shortcoming of such arguments is that while, in general, as the contraction rate or "stability" of the system decreases, the signal to noise ratio increases and identification gets better due to stronger excitation, mixing-time based arguments capture the opposite dependence. By adapting the martingale small-ball condition as, we show this shortcoming can also be avoided for bilinear system identification.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To summarize, we make the following contributions towards bilinear system identification: (i) For a bilinear system with state dimension $n$ and input dimension $m$, the system dynamics involve $m + 1$ matrices of size $n \times n$. We estimate these dynamics with an error rate $\mathcal{O}{(\sqrt{{n{({m + 1})}}/T})}$. Our error rate is optimal in terms of the trajectory length $T$ and the dimension of the unknown matrices. (ii) Recently, asked an important question, *"Is learning without mixing possible in situations beyond generalized linear models?"* We provide a positive answer to this by extending martingale small-ball argument to bilinear systems. (iii) We correctly capture the dependence of random input and noise on the identification of marginally mean-square stable bilinear systems. Finally, we perform numerical experiments to support our theoretical results.

<!-- chunk {"id": "body-0007", "role": "body", "section": "II-A Bilinear Dynamical Systems", "weight": 1.0} -->

In this paper, we consider the identification of bilinear dynamical systems which are governed by the following state equation,

<!-- chunk {"id": "body-0008", "role": "body", "section": "Assumption A1", "weight": 1.0} -->

Our primary goal in this paper is to estimate the unknown state matrices ${\{\mathbf{A}_{k}\}}_{k = 0}^{m}$ from finite samples obtained from a single trajectory of. For this purpose, we introduce the following concatenated matrix/vector notation,

<!-- chunk {"id": "body-0009", "role": "body", "section": "Assumption A1", "weight": 1.0} -->

Suppose we have access to a single finite trajectory ${\{{(\mathbf{u}_{t},\mathbf{x}_{t},\mathbf{x}_{t + 1})}\}}_{t = 0}^{T}$ of the bilinear dynamical system. Then, to carry out finite sample identification of $\mathbf{A}_{\star}$ using the method of linear least squares, we define the following concatenated matrices,

<!-- chunk {"id": "body-0010", "role": "body", "section": "Assumption A1", "weight": 1.0} -->

To estimate the dynamics, we solve the following least-squares problem,

<!-- chunk {"id": "body-0011", "role": "body", "section": "Assumption A1", "weight": 1.0} -->

To make the problem well-conditioned, we also need a stability guarantee on the bilinear system. This will make sure that the design matrix ${\overset{\sim}{\mathbf{X}}}_{T}$ has smaller condition number to help better estimation. However, because of the randomness in $\mathbf{u}_{t}$, the dynamical behavior of the bilinear system is also random. Therefore, it is common to define the stability of bilinear dynamical systems in the mean-square sense, which is the topic of our next subsection.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption A2", "weight": 1.0} -->

The bilinear system in is marginally mean-square stable, i.e., ${\rho{(\overset{\sim}{\mathbf{A}})}} \leq 1$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption A2", "weight": 1.0} -->

Using marginal mean-square stability, we can show that the second moment properties of the states ${\{\mathbf{x}_{t}\}}_{t = 0}^{\infty}$ can be bounded as follows.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Experiments", "weight": 1.0} -->

*Input strength:* In this experiment, we run Algorithm 1 with different values of $\sigma_{\mathbf{u}}$ and $T$, while setting the values of $n,m,{\rho{(\mathbf{A})}}$ and $\rho{(\mathbf{A}_{k})}$ as described above. We also set $\sigma_{\mathbf{w}} = 0.3$. The results of this experiment are plotted in Figure 1. As predicted by our theory, the estimation errors of ${\{\mathbf{A}_{k}\}}_{k = 0}^{m}$ converge to $0$ with the increasing trajectory length. Another important observation is that the estimation errors also decrease with increasing $\sigma_{\mathbf{u}}$. This is more prominent in the case of ${\{\mathbf{A}_{k}\}}_{k = 1}^{m}$, which is consistent with the message of Theorem 2.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Experiments", "weight": 1.0} -->

‣ III Bilinear System Identification ‣ Finite Sample Identification of Bilinear Dynamical Systems"). Furthermore, Table I shows that increasing $\sigma_{\mathbf{u}}$ results in an increase in the spectral radius of the augmented state matrix $\overset{\sim}{\mathbf{A}}$. This also implies that we cannot increase $\sigma_{\mathbf{u}}$ above a certain threshold. Otherwise, the bilinear system might become unstable and we might not be able to learn the dynamics ${\{\mathbf{A}_{k}\}}_{k = 0}^{m}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Experiments", "weight": 1.0} -->

*Noise level:* In this experiment, we run Algorithm 1 with different values of $\sigma_{\mathbf{w}}$ and $T$, while setting the values of $n,m,{\rho{(\mathbf{A})}}$ and $\rho{(\mathbf{A}_{k})}$ as described above. We also set $\sigma_{\mathbf{u}} = 1.5$. The results of this experiment are plotted in Figure 2. Larger trajectory length helps here as well. Interestingly, the estimation errors are independent of the noise strength $\sigma_{\mathbf{w}}$. This is as predicted by Theorem 2. ‣ III Bilinear System Identification ‣ Finite Sample Identification of Bilinear Dynamical Systems"). From Figure 2, we also see that, when the trajectory length is sufficiently large, the condition number of ${\overset{\sim}{\mathbf{X}}}_{T}$ is similar for different noise levels.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Experiments", "weight": 1.0} -->

When the trajectory length and the noise level are very small, ${\overset{\sim}{\mathbf{X}}}_{T}$ has larger condition number because of the random initialization of $\mathbf{x}_{0}$ and the decrease in Euclidean norm of $\mathbf{x}_{t}$ with time (see Figure 2 bottom left). If the noise is $0$ and the unknown bilinear system has ${\rho{(\overset{\sim}{\mathbf{A}})}} < 1$, then as shown in Lemma 1, the states will converge to $0$ exponentially fast. Therefore, most of the samples in the collected trajectory ${\{{(\mathbf{u}_{t},\mathbf{x}_{t},\mathbf{x}_{t + 1})}\}}_{t = 0}^{T}$ will be zero.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper, we provide finite sample analysis for learning discrete-time bilinear systems. We find that: (i) we can estimate the bilinear systems of the form with an error rate $\mathcal{O}{(\sqrt{{n{({m + 1})}}/T})}$, which is optimal in terms of trajectory length $T$ and the dimension of the unknown matrices, and (ii) the estimation gets better with increasing input variance $\sigma_{\mathbf{u}}^{2}$, whereas, it is independent of the noise variance $\sigma_{\mathbf{w}}^{2}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Conclusions", "weight": 1.0} -->

As future direction, it would be of interest to apply these results to learn more general nonlinear systems using bilinearization and Koopman operator techniques. This presents new challenges such as the need for jointly learning a proper lifting and the bilinear dynamics in the lifted space.
