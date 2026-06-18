## Introduction

The study of stochastic systems with noise which multiplies with the state and input i.e. multiplicative noise has a long history in control theory, but is re-emerging in the context of complex networked systems and systems with learning-based control. In contrast with the well-known additive noise setting, multiplicative noise has the ability to capture dependence of the noise on the state and/or control input. This situation occurs in modern control systems as diverse as robotics with distance-dependent sensor errors, networked systems with noisy communication channels, modern power networks with high penetration of intermittent renewables, turbulent fluid flow, and neuronal brain networks. Linear systems with multiplicative noise are particularly attractive as a stochastic modeling framework because they remain simple enough to admit closed-form expressions for stability and stabilization via generalized Lyapunov equations (e.g. ), optimal control via the solution of generalized Riccati equations and state estimation. Additionally, recent results show that the optimal control of this class of systems can be learned strictly from sample data without constructing a model via the reinforcement learning technique of policy gradient. As a complementary perspective, here we tackle the problem from a model-based perspective where the goal is to learn and construct a model from sample data, which can then be used e.g. for optimal control design.

The first issue that must be addressed is that a complete multiplicative noise system model requires accurate estimates not only of the nominal linear system matrices, but also the noise covariance structure. This stands in stark contrast to the additive noise case where the noise covariance structure has no bearing on the control design and can thus be ignored during system identification. For the identification of a nominal linear system, recursive algorithms have been developed in the control literature, such as the recursive least-squares algorithm. These can be utilized for linear systems with multiplicative noise provided that certain assumptions on the noise and on system stability hold. For the estimation of noise covariances, both recursive and batch estimation methods have been proposed over the last few decades (see for a review), but these focus nearly exclusively on additive noise. In order to estimate multiplicative noise covariances, the maximum-likelihood approach was introduced in, and the Bayesian framework was utilized in, for example assuming Gaussian or known distributions with unknown parameters. These methods, however, require prior assumptions on the noise distributions whose incorrectness may worsen the performance of the concerned algorithms for optimal control. Our paper concentrates on jointly estimating the nominal system parameters and the multiplicative noise covariances without imposing any prior assumptions on the distribution of the noises, other than being independent and identically distributed (i.i.d.) with finite first and second moments, which complicates the problem. Both state- and control-dependent noise in the system leads to coupling, which also makes the identification task more difficult.

The second issue we address is that of performing system identification based on multiple state-input trajectory data rather than a single trajectory. Multiple trajectory data arises in two broad situations: 1) episodic tasks where a single system is reset to an initial state after a finite run time, as encountered in iterative learning control and reinforcement learning problems and 2) collecting data from multiple identical systems in parallel, for example, physical experiments and snapshots of social interaction processes. For multiple trajectory data the duration of each trajectory sample may be small, but a large sample size can be obtained by virtue of repetition in the case of episodic tasks and parallel execution in the case of multiple identical systems. Thus, there is a growing interest in system identification based on multiple trajectory data, along with their applications in machine learning literature.

In this paper we consider linear system identification with multiplicative noise from multiple trajectory data. Our contributions are two-fold:

We propose a least-squares estimation algorithm to jointly estimate the nominal system matrices and multiplicative noise covariances from sample averages of multiple finite-horizon trajectory rollouts (Algorithm 1). A two-stage algorithm based on first and second moment dynamics that separate the nominal parameters from the noise variances is utilized, where a stochastic input design, from Gaussian and Wishart distributions, is used for exciting the moment dynamics. The algorithm does not need prior knowledge for the multiplicative noise or stability conditions for the system, except that the noises are i.i.d. among different trajectories, with finite first and second moments so it may be applied to a wide range of scenarios.

Identifiability of the noise covariance matrices and asymptotic consistency of our proposed algorithm are demonstrated. First, it is shown that there exists an equivalent class of covariance structure that generates the same second moment dynamics. Then, it is verified that dynamics defined by the first and second moments of states can generate a well-defined closed-form expression of the parameters, provided sufficiently exciting input sequences and certain controllability conditions hold. Then by assuming the multiple trajectory data are i.i.d., the consistency of the estimator, i.e., convergence to the true value as the number of trajectory samples grows to infinity, is obtained by combining the former result and the law of large numbers.

The remainder of the paper is organized as follows: we formulate the problem in Section II, then in Section III the algorithm is introduced and theoretical results are given, numerical simulation results are presented in Section IV, and in Section V we conclude.

*Notation.* We denote the $n$-dimensional Euclidean space by ${\mathbb{R}}^{n}$, and the set of $n \times m$ real matrices by ${\mathbb{R}}^{n \times m}$. We use $\parallel \cdot \parallel$ to denote the Euclidean norm for vectors and the Frobenius norm for matrices. The expectation of a random vector $X$ is represented by ${\mathbb{E}}{\{ X\}}$. Denote the $n$-dimensional identity matrix by $I_{n} \in {\mathbb{R}}^{n \times n}$. The Kronecker product of two matrices $A \in {\mathbb{R}}^{m \times n}$ and $B \in {\mathbb{R}}^{p \times q}$ is represented by $A \otimes B$, and the vectorization of $A$ by ${{vec}{(A)}} = {({a_{11}a_{21}\cdotsa_{m1}a_{12}a_{22}\cdotsa_{mn}})}^{\intercal}$. For a block matrix

where $B_{ij} \in {\mathbb{R}}^{p \times q}$, we define the following matrix reshaping operator $F:{{\mathbb{R}}^{{{mp} \times n}q}\rightarrow{\mathbb{R}}^{{{mn} \times p}q}}$:

Then we have that $F{(A \otimes A,m,n,m,n)} = {vec}{(A)}{vec}{(A)}^{\intercal}$ for $A \in {\mathbb{R}}^{m \times n}$, which demonstrates the relation between the entries of $A \otimes A$ and those of ${vec}{(A)}{vec}{(A)}^{\intercal}$. Note when $p = q = 1$, $F{( \cdot )}$ degenerates to ${vec}{( \cdot )}$. One can also verify the below reshaping operator from ${vec}{(A)}{vec}{(A)}^{\intercal}$ to $A \otimes A$. That is, $G:{{\mathbb{R}}^{{{mn} \times p}q}\rightarrow{\mathbb{R}}^{{{mp} \times n}q}}$:

where $B = {\lbrack{B_{1}^{\intercal}\cdotsB_{mn}^{\intercal}}\rbrack}^{\intercal}$ and ${vec}_{p \times q}^{- 1}{(x)} = {({vec}{(I_{q})}^{\intercal} \otimes I_{p})}{(I_{q} \otimes x)}$ for $x \in {\mathbb{R}}^{pq}$.

## Problem Formulation

We consider linear systems with multiplicative noise

where $x_{t} \in {\mathbb{R}}^{n}$ is the system state and $u_{t} \in {\mathbb{R}}^{m}$ is the control input to be designed. The dynamics are described by a nominal dynamics matrix $A \in {\mathbb{R}}^{n \times n}$ and nominal input matrix $B \in R^{n \times m}$ and incorporate multiplicative noise terms modeled by the i.i.d. and mutually independent random matrices ${\overline{A}}_{t}$ and ${\overline{B}}_{t}$ which have zero mean and covariance matrices $\Sigma_{A}:={\mathbb{E}}{\{{vec}{({\overline{A}}_{t})}{vec}{({\overline{A}}_{t})}^{T}\}} \in {\mathbb{R}}^{n^{2} \times n^{2}}$ and $\Sigma_{B}:={\mathbb{E}}{\{{vec}{({\overline{B}}_{t})}{vec}{({\overline{B}}_{t})}^{T}\}} \in {\mathbb{R}}^{{{nm} \times n}m}$. Note that if ${\overline{A}}_{t}$ has non-zero mean $\overline{A}$, then we can consider a system with nominal matrix $({A + \overline{A}},B)$, as well as noise terms ${\overline{A}}_{t} - \overline{A}$ and ${\overline{B}}_{t}$, which satisfies the above zero-mean assumption. This also holds for cases with ${\overline{B}}_{t}$ non-zero mean. The term multiplicative noise refers to the fact that noises ${\overline{A}}_{t}$ and ${\overline{B}}_{t}$ enter the system as multipliers of $x_{t}$ and $u_{t}$, rather than as additions. In the latter case, the noises are called additive ones, resulting in much simpler system dynamics.

As an example of system, consider the following system studied in the optimal control literature.

where $\{ p_{i,t}\}$ and $\{ q_{i,t}\}$ are mutually independent i.i.d. scalar random variables, with ${{\mathbb{E}}{\{ p_{i,t}\}}} = {{\mathbb{E}}{\{ q_{j,t}\}}} = 0$, ${{\mathbb{E}}{\{ p_{i,t}^{2}\}}} = \sigma_{i}^{2}$, and ${{\mathbb{E}}{\{ q_{j,t}^{2}\}}} = \delta_{j}^{2}$, ${{\forall i} \in {\lbrack 1,r\rbrack}},{{j \in {\lbrack 1,s\rbrack}},{t \geq 0}}$. It can be seen that ${\overline{A}}_{t} = {\sum_{i = 1}^{r}{A_{i}p_{i,t}}}$ and ${\overline{B}}_{t} = {\sum_{j = 1}^{s}{B_{j}q_{j,t}}}$ where $\sigma_{i}$ and $\delta_{j}$ are the eigenvalues of $\Sigma_{A}$ and $\Sigma_{B}$, and $A_{i}$ and $B_{j}$ are the reshaped eigenvectors of $\Sigma_{A}$ and $\Sigma_{B}$. These parameters are necessary for optimal controller design, as showed. However, for new systems with unknown parameters, the key problem is to identify them in the first place, stated as follows. Another example of system is interconnected systems, where the nominal part captures relations among different subsystems, and multiplicative noises characterize randomly varying topologies.

Problem. Suppose that the system parameters ${A,B,\Sigma_{A}},$ and $\Sigma_{B}$ are unknown, but state-input trajectories are available for system identification. Our goal in this paper is to estimate ${A,B,\Sigma_{A}},$ and $\Sigma_{B}$ based on multiple trajectory data $\{{{{x_{t}^{(k)},0} \leq t \leq \ell},{k \in {\mathbb{N}}^{+}}}\}$, by appropriately designing the input sequence $\{{{{u_{t}^{(k)},0} \leq t \leq {\ell - 1}},{k \in {\mathbb{N}}^{+}}}\}$ and initial states $x_{0}^{(k)}$, where $\{{{x_{t}^{(k)},0} \leq t \leq \ell}\}$, is the $k$-th trajectory sample, and $\ell$ is the final time-step for every trajectory.

## Least-Squares Algorithm Based on Multiple Trajectory Data

### III-A Algorithm Design

In this section, we propose our exploratory input sequence design and least-squares algorithm to estimate the system parameters from multiple trajectory data. We assume that the sampled trajectory data are collected independently, and refer to each trajectory sample as a *rollout*. Because every rollout is affected by the multiplicative noise, we will use least-squares on the first and second moment dynamics averaged over multiple trajectories to solve the system identification problem. Also, we assume inputs of arbitrary magnitude may be executed perfectly.

Taking the expectation of both sides of we obtain the first-moment dynamics of states, i.e., the dynamics of ${\mathbb{E}}{\{ x_{t}\}}$,

where $\mu_{t}:={{\mathbb{E}}{\{ x_{t}\}}}$ and $\nu_{t}:={{\mathbb{E}}{\{ u_{t}\}}}$.

Likewise, denote the vectorization of the instantaneous second moment matrices of state, state-input, and input at time $t$ by $X_{t}:={{vec}{({{\mathbb{E}}{\{{x_{t}x_{t}^{\intercal}}\}}})}}$, $W_{t}:={{vec}{({{\mathbb{E}}{\{{x_{t}u_{t}^{\intercal}}\}}})}}$, $W_{t}^{\prime}:={{vec}{({{\mathbb{E}}{\{{u_{t}x_{t}^{\intercal}}\}}})}}$, and $U_{t}:={{vec}{({{\mathbb{E}}{\{{u_{t}u_{t}^{\intercal}}\}}})}}$. Note that the second moment matrix we used here, namely ${\mathbb{E}}{\{{XY^{\intercal}}\}}$ for two random vectors $X$ and $Y$, is different from the covariance matrix, which is ${{\mathbb{E}}{\{{{({X - {{\mathbb{E}}{\{ X\}}}})}{({Y - {{\mathbb{E}}{\{ Y\}}}})}^{\intercal}}\}}} = {{{\mathbb{E}}{\{{XY^{\intercal}}\}}} - {{\mathbb{E}}{\{ X\}}{\mathbb{E}}{\{ Y\}}^{\intercal}}}$.

From the independence of ${\overline{A}}_{t}$ and ${\overline{B}}_{t}$, as well as vectorization, the second moment dynamics of are

where we denote $\Sigma_{A}^{\prime} = {{\mathbb{E}}{\{{{\overline{A}}_{t} \otimes {\overline{A}}_{t}}\}}} \in {\mathbb{R}}^{n^{2} \times n^{2}}$ and $\Sigma_{B}^{\prime} = {{\mathbb{E}}{\{{{\overline{B}}_{t} \otimes {\overline{B}}_{t}}\}}} \in {\mathbb{R}}^{n^{2} \times m^{2}}$. The relation between $(\Sigma_{A},\Sigma_{B})$ and $(\Sigma_{A}^{\prime},\Sigma_{B}^{\prime})$ can be illustrated by ${F{(\Sigma_{A}^{\prime},n,n,n,n)}} = \Sigma_{A}$ and ${F{(\Sigma_{B}^{\prime},n,m,n,m)}} = \Sigma_{B}$, where the reshaping operator $F{( \cdot )}$ is defined in the notation subsection.

Before giving an estimation algorithm, it is necessary to talk more about the second moment dynamics (III-A). Since ${\mathbb{E}}{\{{x_{t}x_{t}^{\intercal}}\}}$ is symmetric, $X_{t}$ has ${n{({n - 1})}}/2$ pairs of identical entries, corresponding to the off-diagonal entries of ${\mathbb{E}}{\{{x_{t}x_{t}^{\intercal}}\}}$. For example, ${\mathbb{E}}{\{{x_{t,i}x_{t,j}}\}}$ and ${\mathbb{E}}{\{{x_{t,j}x_{t,i}}\}}$. Similarly, $U_{t}$ has ${m{({m - 1})}}/2$ pairs of identical entries corresponding to the off-diagonal entries of ${\mathbb{E}}{\{{u_{t}u_{t}^{\intercal}}\}}$.

We apply the following process to (III-A), to obtain a simplified version of it.

If there exist $i$ and $j$ such that $X_{t,i} = {{\mathbb{E}}{\{{x_{t,k}x_{t,l}}\}}}$ and $X_{t,j} = {{\mathbb{E}}{\{{x_{t,l}x_{t,k}}\}}}$, $1 \leq i < j \leq n^{2}$, for some $1 \leq l < k \leq n$, then add the $j$-th column of ${A \otimes A} + \Sigma_{A}^{\prime}$ to its $i$-th column. After that, remove the $j$-th column.

Remove the $j$-th entry of $X_{t + 1}$ and $X_{t}$, and also the $j$-th row of ${A \otimes A} + \Sigma_{A}^{\prime}$, ${B \otimes B} + \Sigma_{B}^{\prime}$, $A \otimes B$, and $B \otimes A$.

Return to step 1, until ${n{({n - 1})}}/2$ entries of $X_{t}$ are removed (corresponding to the upper-diagonal entries of ${\mathbb{E}}{\{{x_{t}x_{t}^{\intercal}}\}}$).

If there exist $i$ and $j$ such that $U_{t,i} = {{\mathbb{E}}{\{{u_{t,k}u_{t,l}}\}}}$ and $U_{t,j} = {{\mathbb{E}}{\{{u_{t,l}u_{t,k}}\}}}$, $1 \leq i < j \leq m^{2}$, for some $1 \leq l < k \leq m$, then add the $j$-th column of ${B \otimes B} + \Sigma_{B}^{\prime}$ to its $i$-th column, remove the $j$-th column, and remove the $j$-th entry of $U_{t}$.

Return to step 4, until ${m{({m - 1})}}/2$ entries of $U_{t}$ are removed (corresponding to the upper-diagonal entries of ${\mathbb{E}}{\{{u_{t}u_{t}^{\intercal}}\}}$).

In this way, we get a simplified version of (III-A),

where ${\overset{\sim}{X}}_{t} \in {\mathbb{R}}^{{n{({n + 1})}}/2}$ and ${\overset{\sim}{U}}_{t} \in {\mathbb{R}}^{{m{({m + 1})}}/2}$.

The above procedure can be written in a compact form by considering a linear transformation from ${\mathbb{R}}^{n^{2}}$ to ${\mathbb{R}}^{{n{({n + 1})}}/2}$, as given below. Let $I_{n^{2}}:={\lbrack{e_{1}\cdotse_{n^{2}}}\rbrack}$ be the $n^{2}$-dimensional identity matrix. Then define matrix $P_{1} \in {\mathbb{R}}^{{\lbrack{{n{({n + 1})}}/2}\rbrack} \times n^{2}}$ by removing the $\lbrack{{{({j - 1})}n} + i}\rbrack$-th row of $I_{n^{2}}$, define matrix $T_{1} \in {\mathbb{R}}^{n^{2} \times n^{2}}$ by replacing the $\lbrack{{{({j - 1})}n} + i}\rbrack$-th row of $I_{n^{2}}$ by $e_{{{({i - 1})}n} + j}^{\intercal}$, and define matrix $Q_{1} \in {\mathbb{R}}^{n^{2} \times {\lbrack{{n{({n + 1})}}/2}\rbrack}}$ by removing the $\lbrack{{{({j - 1})}n} + i}\rbrack$-th column of $T_{1}$, where $1 \leq i < j \leq n$. We can also define $P_{2} \in {\mathbb{R}}^{{\lbrack{{m{({m + 1})}}/2}\rbrack} \times m^{2}}$, $T_{2} \in {\mathbb{R}}^{m^{2} \times m^{2}}$, and $Q_{2} \in {\mathbb{R}}^{m^{2} \times {\lbrack{{m{({m + 1})}}/2}\rbrack}}$ by changing $n$ to $m$ in the above text.

It can be obtained that ${\overset{\sim}{X}}_{t} = {P_{1}X_{t}}$, ${\overset{\sim}{U}}_{t} = {P_{2}U_{t}}$, $X_{t} = {T_{1}X_{t}}$, $U_{t} = {T_{2}U_{t}}$, $T_{1} = {Q_{1}P_{1}}$, and $T_{2} = {Q_{2}P_{2}}$, by noticing that ${\mathbb{E}}{\{{x_{t,i}x_{t,j}}\}}$ is the $\lbrack{{{({j - 1})}n} + i}\rbrack$-th entry of $X_{t}$, ${1 \leq i},{j \leq n}$, and ${\mathbb{E}}{\{{u_{t,i}u_{t,j}}\}}$ is the $\lbrack{{{({j - 1})}m} + i}\rbrack$-th entry of $U_{t}$, ${1 \leq i},{j \leq m}$.

Hence, from (III-A),

As a result, $\overset{\sim}{A} = {P_{1}{({A \otimes A})}Q_{1}}$, ${\overset{\sim}{\Sigma}}_{A}^{\prime} = {P_{1}\Sigma_{A}^{\prime}Q_{1}}$, $\overset{\sim}{B} = {P_{1}{({B \otimes B})}Q_{2}}$, ${\overset{\sim}{\Sigma}}_{B}^{\prime} = {P_{1}\Sigma_{B}^{\prime}Q_{2}}$, $K_{BA} = {P_{1}{({B \otimes A})}}$, and $K_{AB} = {P_{1}{({A \otimes B})}}$.

Now with the following fact, we can restate the above relation between $(\Sigma_{A}^{\prime},\Sigma_{B}^{\prime})$ and $({\overset{\sim}{\Sigma}}_{A}^{\prime},{\overset{\sim}{\Sigma}}_{B}^{\prime})$ from an entry-wise perspective in Theorem 1.

&amp; \begin{matrix}
&amp; {{{({k - 1})}n} + l} &amp; &amp; {{{({l - 1})}n} + k} &amp;
\end{matrix} &amp; \begin{bmatrix}
&amp; \vdots &amp; &amp; \vdots &amp; \\
\cdots &amp; {{\mathbb{E}}{\{{{\overline{A}}_{t,{ik}}{\overline{A}}_{t,{jl}}}\}}} &amp; \cdots &amp; {{\mathbb{E}}{\{{{\overline{A}}_{t,{il}}{\overline{A}}_{t,{jk}}}\}}} &amp; \cdots \\
&amp; \vdots &amp; &amp; \vdots &amp; \\
\cdots &amp; {{\mathbb{E}}{\{{{\overline{A}}_{t,{jk}}{\overline{A}}_{t,{il}}}\}}} &amp; \cdots &amp; {{\mathbb{E}}{\{{{\overline{A}}_{t,{jl}}{\overline{A}}_{t,{ik}}}\}}} &amp; \cdots \\
&amp; \vdots &amp; &amp; \vdots &amp;

&amp; \begin{matrix}
&amp; {{{({k - 1})}m} + l} &amp; &amp; {{{({l - 1})}m} + k} &amp;
\end{matrix} &amp; \begin{bmatrix}
&amp; \vdots &amp; &amp; \vdots &amp; \\
\cdots &amp; {{\mathbb{E}}{\{{{\overline{B}}_{t,{ik}}{\overline{B}}_{t,{jl}}}\}}} &amp; \cdots &amp; {{\mathbb{E}}{\{{{\overline{B}}_{t,{il}}{\overline{B}}_{t,{jk}}}\}}} &amp; \cdots \\
&amp; \vdots &amp; &amp; \vdots &amp; \\
\cdots &amp; {{\mathbb{E}}{\{{{\overline{B}}_{t,{jk}}{\overline{B}}_{t,{il}}}\}}} &amp; \cdots &amp; {{\mathbb{E}}{\{{{\overline{B}}_{t,{jl}}{\overline{B}}_{t,{ik}}}\}}} &amp; \cdots \\
&amp; \vdots &amp; &amp; \vdots &amp;

### Lemma 1

$\Sigma_{A}^{\prime}$ and $\Sigma_{B}^{\prime}$ has structure in and respectively, where ${\overline{A}}_{t,{ij}}$ is the $(i,j)$-th entry of ${\overline{A}}_{t}$, $1 \leq i \neq j \leq n$, $1 \leq k \neq l \leq n$, and ${\overline{B}}_{t,{ij}}$ is the $(i,j)$-th entry of ${\overline{B}}_{t}$, $1 \leq i \neq j \leq n$, $1 \leq k \neq l \leq m$.

### Proof

The conclusions follow directly from properties of Kronecker products. ∎

### Theorem 1

The entries of ${\overset{\sim}{\Sigma}}_{A}^{\prime}$ consists of:\
${{{{\mathbb{E}}{\{{{\overline{A}}_{t,{ik}}{\overline{A}}_{t,{ik}}}\}}},1} \leq i},{k \leq n}$;\
${{{{\mathbb{E}}{\{{{\overline{A}}_{t,{ik}}{\overline{A}}_{t,{jk}}}\}}},i} < j},{{1 \leq {i,j}},{k \leq n}}$;\
${{{2{\mathbb{E}}{\{{{\overline{A}}_{t,{ik}}{\overline{A}}_{t,{il}}}\}}},k} < l},{{1 \leq {i,k}},{l \leq n}}$;\
${{{{{\mathbb{E}}{\{{{\overline{A}}_{t,{ik}}{\overline{A}}_{t,{jl}}}\}}} + {{\mathbb{E}}{\{{{\overline{A}}_{t,{il}}{\overline{A}}_{t,{jk}}}\}}}},1} \leq i < j \leq n},{1 \leq k < l \leq n}$.\
The entries of ${\overset{\sim}{\Sigma}}_{B}^{\prime}$ consists of:\
${{{{\mathbb{E}}{\{{{\overline{B}}_{t,{ik}}{\overline{B}}_{t,{ik}}}\}}},1} \leq i \leq n},{1 \leq k \leq m}$;\
${{{{\mathbb{E}}{\{{{\overline{B}}_{t,{ik}}{\overline{B}}_{t,{jk}}}\}}},1} \leq i < j \leq n},{1 \leq k \leq m}$;\
${{{2{\mathbb{E}}{\{{{\overline{B}}_{t,{ik}}{\overline{B}}_{t,{il}}}\}}},1} \leq i \leq n},{1 \leq k < l \leq m}$;\
${{{{{\mathbb{E}}{\{{{\overline{B}}_{t,{ik}}{\overline{B}}_{t,{jl}}}\}}} + {{\mathbb{E}}{\{{{\overline{B}}_{t,{il}}{\overline{B}}_{t,{jk}}}\}}}},1} \leq i < j \leq n},{1 \leq k < l \leq m}$.

### Proof

Consider the simplifying procedure from (III-A) to (III-A). Step 1 generates columns of additions with form ${{\mathbb{E}}{\{{{\overline{A}}_{t,{ik}}{\overline{A}}_{t,{jl}}}\}}} + {{\mathbb{E}}{\{{{\overline{A}}_{t,{il}}{\overline{A}}_{t,{jk}}}\}}}$ for $1 \leq k < l \leq n$. Moreover, if $i = j$, then the corresponding term becomes $2{\mathbb{E}}{\{{{\overline{A}}_{t,{ik}}{\overline{A}}_{t,{il}}}\}}$. By removing the $\lbrack{{{({l - 1})}n} + k}\rbrack$-th row of $\Sigma_{A}^{\prime}$ in step 2, $1 \leq k < l \leq n$, these entries, ${{{{\mathbb{E}}{\{{{\overline{A}}_{t,{jk}}{\overline{A}}_{t,{il}}}\}}} + {{\mathbb{E}}{\{{{\overline{A}}_{t,{jl}}{\overline{A}}_{t,{ik}}}\}}}},1} \leq i < j \leq n$ are removed, for all $k < l$. This step also deletes the column consisting of ${\mathbb{E}}{\{{{\overline{A}}_{t,{il}}{\overline{A}}_{t,{jk}}}\}}$ and ${\mathbb{E}}{\{{\overline{A}}_{t,{jl}}{\overline{A}}_{t,{ik}}\}})$, ${1 \leq i},{j \leq n}$. The entries ${\mathbb{E}}{\{{{\overline{A}}_{t,{ik}}{\overline{A}}_{t,{ik}}}\}}$, ${1 \leq i},{k \leq n}$, remains the same during the process. Same argument for results of ${\overset{\sim}{\Sigma}}_{B}^{\prime}$. ∎

### Remark 1

The above discussion indicates that $X_{t}$ is in fact determined by parameter matrices $(A,B)$ and $({\overset{\sim}{\Sigma}}_{A}^{\prime},{\overset{\sim}{\Sigma}}_{B}^{\prime})$. It also shows that there exists a set of covariance matrices $(\Sigma_{A}^{\prime},\Sigma_{B}^{\prime})$ that are equivalent, i.e., $S_{\Sigma}^{+}:={\{{{(\Sigma_{1}^{\prime},\Sigma_{2}^{\prime})} \in {\mathbb{R}}^{n^{2} \times {({n^{2} + {nm}})}}}:{{{P_{1}\Sigma_{1}^{\prime}Q_{1}} = {\overset{\sim}{\Sigma}}_{A}^{\prime}},{{{P_{1}\Sigma_{2}^{\prime}Q_{2}} = {\overset{\sim}{\Sigma}}_{B}^{\prime}},{{{F{(\Sigma_{1}^{\prime},n,n,n,n)}} \succeq 0},{{F{(\Sigma_{2}^{\prime},n,m,n,m)}} \succeq 0}}}}\}}$, in the sense that they generate an identical second moment dynamic of. The last two terms in the set definition are due to the positive semi-definiteness of $\Sigma_{A}$ and $\Sigma_{B}$. Obviously, $S_{\Sigma}^{+}$ is not empty for $({\overset{\sim}{\Sigma}}_{A}^{\prime},{\overset{\sim}{\Sigma}}_{B}^{\prime})$ obtained in (III-A), since ${(\Sigma_{A}^{\prime},\Sigma_{B}^{\prime})} \in S_{\Sigma}^{+}$. From an entry-wise point of view, because of multiplicative noises, we cannot recover the exact value of ${\mathbb{E}}{\{{{\overline{A}}_{t,{ik}}{\overline{A}}_{t,{jl}}}\}}$ and ${\mathbb{E}}{\{{{\overline{A}}_{t,{il}}{\overline{A}}_{t,{jk}}}\}}$, if $i \neq j$ and $k \neq l$. One may only estimate the sum of these two entries instead out of $X_{t}$. Fortunately, some entries of $\Sigma_{A}^{\prime}$ and $\Sigma_{B}^{\prime}$ are identifiable, e.g., ${\mathbb{E}}{\{{{\overline{A}}_{t,{ik}}{\overline{A}}_{t,{ik}}}\}}$, which is the variance of ${\overline{A}}_{t,{ik}}$. This means that if we introduce more conditions for the covariance structure, then it can be obtained exactly. For example, if entries in ${\overline{A}}_{t}$ are mutually independent, then $\Sigma_{A}$ is diagonal, and all of its entries except ${\mathbb{E}}{\{{{\overline{A}}_{t,{ik}}{\overline{A}}_{t,{ik}}}\}}$, ${1 \leq i},{k \leq n}$, are zero.

### Example 1

Consider with $n = 2$ and $m = 1$, where $X_{t} = \left\lbrack {{\mathbb{E}}{\{{x_{t,1}x_{t,1}}\}}{\mathbb{E}}{\{{x_{t,2}x_{t,1}}\}}{\mathbb{E}}{\{{x_{t,1}x_{t,2}}\}}{\mathbb{E}}{\{{x_{t,2}x_{t,2}}\}}} \right\rbrack^{T}$. So ${\mathbb{E}}{\{{X_{t,2}X_{t,1}}\}}$ and ${\mathbb{E}}{\{{X_{t,1}X_{t,2}}\}}$ are identical and have the same update rule in (III-A). Under this situation,

According to the above simplification, from

where $\sigma_{a,{ij},{kl}} = {{\mathbb{E}}{\{{{\overline{A}}_{t,{ij}}{\overline{A}}_{t,{kl}}}\}}}$, $\sigma_{b,{ij}} = {{\mathbb{E}}{\{{\overline{B}}_{t,i},{\overline{B}}_{t,j}\}}}$, and

The first and second moment dynamics and (III-A) are linear in the dynamic model parameters to be estimated. It is natural to consider a two-stage least-squares procedure, where first the nominal system matrices ($A$,$B$) are estimated from, and then these estimates are plugged in to obtain estimates for the variances ($\Sigma_{A}$, $\Sigma_{B}$) from (III-A). If we had access to the exact first and second moment dynamics, this procedure would produce exact estimates. However, we must estimate the first and second moment dynamics from rollout data, and we propose to take a sample average over multiple independent rollouts. To obtain persistently exciting inputs, we randomly generate the first and second moment of the input sequence from standard Gaussian and Wishart^11^1The Wishart distribution $W_{p}{(V,n)}$ is the probability distribution of the matrix $X = {GG^{\intercal}}$ where each column of the matrix $G$ is drawn from the $p$-variate Gaussian distribution $\mathcal{N}_{p}{(0,V)}$. Clearly Wishart distributions are supported on the set of positive semidefinite matrices. distributions, respectively. Likewise, the initial states are assumed to be randomly drawn from a distribution $\mathcal{X}$ with finite second moment (see Sec. III-B2). The overall algorithm is shown in Algorithm 1, where the superscript $(k)$ represents the $k$-th rollout.

In Alg. 1 and in the sequel, to ease notation, we omit the "$\overset{\sim}{}$" above $X_{t}$, $U_{t}$, $\Sigma_{A}^{\prime}$, and $\Sigma_{B}^{\prime}$, but readers should keep in mind that they are the simplified version of their counterparts in (III-A).

2: Generate νt and ${\overline{U}}_{t}$ independently from zero-mean Gaussian and Wishart distributions, respectively. Both νt and ${\overline{U}}_{t}$ are fixed after generation
5: Generate x0(k) independently from the distribution 𝒳
7: Generate ut(k) independently from the Gaussian distribution $\mathcal{N}{(\nu_{t},{\overline{U}}_{t})}$

${{{:=}\frac{1}{n_{r}}}{\sum\limits_{k = 1}^{n_{r}}x_{t}^{(k)}}},$

${{:=}{\frac{1}{n_{r}}{{vec}\left( {\sum\limits_{k = 1}^{n_{r}}{x_{t}^{(k)}{(x_{t}^{(k)})}^{\intercal}}} \right)}}},$

${{{:=}{\frac{1}{n_{r}}{{vec}\left( {\sum\limits_{k = 1}^{n_{r}}{x_{t}^{(k)}\nu_{t}^{\intercal}}} \right)}}} = {{vec}{({{\hat{\mu}}_{t}\nu_{t}^{\intercal}})}}},$

${{{:=}{\frac{1}{n_{r}}{{vec}\left( {\sum\limits_{k = 1}^{n_{r}}{\nu_{t}{}_{}^{(k)}}} \right)}}} = {{vec}{({\nu_{t}{\hat{\mu}}_{t}^{\intercal}})}}},$

${:=}{{vec}{({{\overline{U}}_{t} + {\nu_{t}\nu_{t}^{\intercal}}})}}$

15: ${({\hat{\Sigma}}_{A}^{\prime},{\hat{\Sigma}}_{B}^{\prime})} = {\text{argmin}_{(\Sigma_{A}^{\prime},\Sigma_{B}^{\prime})}{\left. \{{\frac{1}{2}\sum_{t = 0}^{\ell - 1}} \right\|{{\hat{X}}_{t + 1} - {{\lbrack{{\overset{\sim}{A}{\hat{X}}_{t}} + {K_{BA}{\hat{W}}_{t}} + {K_{AB}{\hat{W}}_{t}^{\prime}} + {\overset{\sim}{B}U_{t}} + {\Sigma_{A}^{\prime}{\hat{X}}_{t}} + {\Sigma_{B}^{\prime}U_{t}}}\rbrack}\parallel}_{2}^{2}}\}}}$

Multiple-trajectory averaging least-squares (MALS)

### III-B Theoretical Consistency Analysis

In this section we analyze the consistency of Algorithm 1 by investigating the moment dynamics and (III-A), which motivated the least-squares approach in Algorithm 1.

### III-B1 Moment Dynamics

Note again if we know $\mu_{t}$ and $X_{t}$, then it is possible to recover the parameters via least-squares as in lines $14$-$15$ in Algorithm 1. Let

where $C_{t} = {X_{t} - {\lbrack{{\overset{\sim}{A}X_{t - 1}} + {K_{BA}W_{t - 1}} + {K_{AB}W_{t - 1}^{\prime}} + {\overset{\sim}{B}U_{t - 1}}}\rbrack}}$, $1 \leq t \leq \ell$. Then closed-form solutions of the least-squares problems are

where $\mathbf{C}$, $\mathbf{D}$, $\mathbf{Y}$, and $\mathbf{Z}$ are defined in (LABEL:defLSMatrices) above, and the sign $\dagger$ represents the pseudoinverse. When the inverse matrices exist, the solutions are identical to true values, that is, ${(\hat{A},\hat{B})} = {(A,B)}$ and ${({\hat{\Sigma}}_{A}^{\prime},{\hat{\Sigma}}_{B}^{\prime})} = {(\Sigma_{A}^{\prime},\Sigma_{B}^{\prime})}$. Hence, the first question towards the consistency of the algorithm is whether the matrices ${\mathbf{Z}\mathbf{Z}}^{\intercal}$ and ${\mathbf{D}\mathbf{D}}^{\intercal}$ are invertible, which is necessary for the consistency of the algorithm. As to be shown, this invertibility can be obtained by designing a proper input sequence, if systems $(A,B)$ and $({\overset{\sim}{A} + \Sigma_{A}^{\prime}},{\overset{\sim}{B} + \Sigma_{B}^{\prime}})$ are controllable, and the final time-step $\ell$ is large enough. In fact, in this paper we randomly generalized the first and second moments of inputs to ensure the invertibility. As a consequence, we need to demonstrate the following results in a probability sense, intuitively saying that random generation of input statistics results in the expected invertibility.

### Theorem 2

Suppose that $\ell \geq {{\frac{1}{2}mn^{2}} + {\frac{1}{2}mn} + m + 1}$ and $(A,B)$ is controllable. The matrix $\mathbf{Z}$ has full row rank with probability one, and consequently ${\mathbf{Z}\mathbf{Z}}^{\intercal}$ is invertible, if the entries of $\nu_{t}$, $0 \leq t \leq {\ell - 1}$, are generated i.i.d. from a non-degenerate Gaussian distributions.

### Proof

### Remark 2

The above theorem shows that for large enough time step of each rollout, the full row rank condition of $\mathbf{Z}$ can be guaranteed with probability one if the mean of the input at each time step is generated randomly and independently. In the proof, the controllability of $(A,B)$ plays a key role. In addition, although the lower bound in the theorem is relatively small, one may conjecture that $\ell \geq {n + m}$ is a sharp lower bound for the invertibility of ${\mathbf{Z}\mathbf{Z}}^{\intercal}$, which will be a future work.

### Theorem 3

Suppose that $\ell \geq {{\frac{1}{2}m^{2}n^{4}} + {\frac{1}{2}m^{2}n^{2}} + m^{2} + 1}$ and $({\overset{\sim}{A} + \Sigma_{A}^{\prime}},{\overset{\sim}{B} + \Sigma_{B}^{\prime}})$ is controllable. The matrix $\mathbf{D}$ has full row rank with probability one, and consequently ${\mathbf{D}\mathbf{D}}^{\intercal}$ is invertible, if $\nu_{t}$ have been fixed and the entries of ${\overline{U}}_{t}$ are generated i.i.d. from a non-degenerate Wishart distributions, $0 \leq t \leq {\ell - 1}$, where ${\overline{U}}_{t}$ is defined in line 2 of Algorithm 1.

### Proof

### Remark 3

The controllability condition in Theorem 3 reflects the nature of the multiplicative noise, i.e., coupling between ${\overline{A}}_{t}$ and $x_{t}$, and that between ${\overline{B}}_{t}$ and $u_{t}$. It also indicates that a controllability condition on (III-A), the dynamics of the second moments of states, is necessary to ensure the successful identification of $\Sigma_{A}^{\prime}$ and $\Sigma_{B}^{\prime}$.

### Corollary 1

Suppose that $\ell \geq {{\frac{1}{2}m^{2}n^{4}} + {\frac{1}{2}m^{2}n^{2}} + m^{2} + 1}$, and both $(A,B)$ and $({\overset{\sim}{A} + \Sigma_{A}^{\prime}},{\overset{\sim}{B} + \Sigma_{B}^{\prime}})$ are controllable. The matrices ${\mathbf{Z}\mathbf{Z}}^{\intercal}$ and ${\mathbf{D}\mathbf{D}}^{\intercal}$ are invertible, if first the entries of $\nu_{t}$ are generated i.i.d. from a non-degenerate Gaussian distribution and then ${\overline{U}}_{t}$ is generated i.i.d. from a non-degenerate Wishart distribution, $0 \leq t \leq {\ell - 1}$, where ${\overline{U}}_{t}$ is defined in line 2 of Algorithm 1.

### Remark 4

From the proof of Theorems 2 and 3, we know that the existence of the inverses of ${\mathbf{Z}\mathbf{Z}}^{\intercal}$ and ${\mathbf{D}\mathbf{D}}^{\intercal}$ can in fact be guaranteed with probability one, as long as $\nu_{t}$ and ${\overline{U}}_{t}$, the mean and vectorized second moment matrix of the input at time $t$, are generated independently from a distribution that is absolutely continuous with respect to Lebesgue measure. Also note the random generation of the first and second moments of inputs leads to non-stationarity of the input sequence. Critically this provides sufficient excitation of both the first and second moments of the state and makes it possible to estimate all model parameters in the presence of multiplicative noise.

### III-B2 Consistency

After the discussion in the previous section, we now assume that the means and second moments of the input sequences have been generated in Algorithm 1, and both ${\mathbf{Z}\mathbf{Z}}^{\intercal}$ and ${\mathbf{D}\mathbf{D}}^{\intercal}$ have been designed to be invertible. The closed-form estimates generated by Algorithm 1 are

and ${\hat{C}}_{t} = {{\hat{X}}_{t} - {\lbrack{{\hat{\overset{\sim}{A}}{\hat{X}}_{t - 1}} + {{\hat{K}}_{BA}{\hat{W}}_{t - 1}} + {{\hat{K}}_{AB}{\hat{W}}_{t - 1}^{\prime}} + {\hat{\overset{\sim}{B}}U_{t - 1}}}\rbrack}}$, $1 \leq t \leq \ell$. Here $\hat{\overset{\sim}{A}}$, $\hat{\overset{\sim}{B}}$, ${\hat{K}}_{AB}$, and ${\hat{K}}_{BA}$ are estimates of $\overset{\sim}{A}$, $\overset{\sim}{B}$, $K_{AB}$, and $K_{BA}$, obtained by using $\hat{A}$ and $\hat{B}$ from Algorithm 1. The estimates above depend on the number of rollouts $n_{r}$, but we omit it for convenience. Before stating the consistency result, we present the following assumption for the system and data:

### Assumption 1

For all rollouts, the below conditions hold.\
(i) The final time-step is fixed to be $\ell \geq {{\frac{1}{2}m^{2}n^{4}} + {\frac{1}{2}m^{2}n^{2}} + m^{2} + 1}$.\
(ii) The initial state $x_{0}^{(k)}$, $1 \leq k \leq n_{r}$, is generated independently from the same distribution with ${{\mathbb{E}}{\{{\| x_{0}^{(k)}\|}^{2}\}}} < \infty$, and is independent of the subsequent process.\
(iii) $\{{{{\overline{A}}_{t}^{(k)},0} \leq t \leq \ell}\}$ and $\{{{{\overline{B}}_{t}^{(k)},0} \leq t \leq \ell}\}$, $1 \leq k \leq n_{r}$, have zero mean and finite second moments, i.e., ${{\mathbb{E}}{\{{\overline{A}}_{t}\}}} = {{\mathbb{E}}{\{{\overline{B}}_{t}\}}} = \mathbf{0}$ and ${{\|\Sigma_{A}\|},{\|\Sigma_{B}\|}} < \infty$. Also, these sequences are i.i.d. and mutually independent.\
(iv) The input signals are generated by Line 6 of Algorithm 1 and are such that both ${\mathbf{Z}\mathbf{Z}}^{\intercal}$ and ${\mathbf{D}\mathbf{D}}^{\intercal}$ are invertible.

Under Assumption 1 the rollouts $x_{0}^{(k)},\ldots,x_{l}^{(k)}$, $1 \leq k \leq n_{r}$, are i.i.d., so consistency can be established from Kolmogorov's strong law of large numbers.

### Theorem 4

(Consistency) Suppose that Assumption 1 holds, then the estimators - are asymptotically consistent, i.e.,

with probability one as the number of rollouts $n_{r}\rightarrow\infty$.

### Proof

### Remark 5

This theorem indicates that despite the relatively small final time-step for each trajectory, an increasing number of rollouts compensates for this deficiency and guarantees asymptotic estimation performance.

From the estimates of ${\overset{\sim}{\Sigma}}_{A}^{\prime}$ and ${\overset{\sim}{\Sigma}}_{B}^{\prime}$ (note that in Theorem 4 we omit the notation "$\overset{\sim}{}$" for simplicity), explicit forms of covariance structure $\Sigma_{A}$ and $\Sigma_{B}$ can be given as follows:

with $I_{n^{2}} = {\lbrack{e_{1}\cdotse_{n^{2}}}\rbrack}$, $I_{m^{2}} = {\lbrack{f_{1}\cdotsf_{m^{2}}}\rbrack}$, ${\alpha_{{ij},{kl}},\beta_{{ij},{pq}}} \in {\mathbb{R}}$, $1 \leq i < j \leq n$, $1 \leq k < l \leq n$, $1 \leq p < q \leq m$, and $Q_{1}$ is defined after (III-A). In addition, $Q_{3} = {D_{n}Q_{1}}$ and $Q_{4} = {D_{m}Q_{2}}$, where $D_{n}$ is an $n^{2}$-dimensional diagonal matrix with $\lbrack{{{({i - 1})}n} + j}\rbrack$-th diagonal entry being $1/2$ and the rest being $1$, $1 \leq i \neq j \leq n$, and $D_{m}$ is an $m^{2}$-dimensional diagonal matrix with $\lbrack{{{({i - 1})}m} + j}\rbrack$-th diagonal entry being $1/2$ and the rest being $1$, $1 \leq i \neq j \leq m$.

## Numerical Simulations

To empirically validate our theoretical consistency result, we simulated our least-squares estimator on two example systems. The first is a simple 2-state, 1-input system where we use a large amount of data to show asymptotic trends, while the second is an 8-state, 8-input system representing lossy diffusion dynamics on a network for a more practical application. Python code which implements the algorithms and performs the simulated experiments described here is available on GitHub at https://github.com/TSummersLab/sysid-multinoise

### IV-A Simple example

We consider a simple example system with $n = 2$, $m = 1$, ${{A = \begin{bmatrix}
\end{bmatrix}},{B = \begin{bmatrix}
\end{bmatrix}}},$ and noise covariances

Figure 1: Consistency of Alg. 1.

According to the reshaping operator $G$ defined in the notation subsection and Example 1, we have

We performed a simulated experiment where rollout data of length $\ell = {{\frac{1}{2}m^{2}n^{4}} + {\frac{1}{2}m^{2}n^{2}} + m^{2} + 1} = 12$. We used control inputs distributed as $u_{t} \sim {\mathcal{N}{(\nu_{t},{\overline{U}}_{t})}}$, where $\nu_{t}$ and ${\overline{U}}_{t}$ are generated from $\mathcal{N}{(0,I_{n})}$ and $\mathcal{W}_{n}{({0.1I_{n}},n)}$, respectively, and then are fixed. Model estimates were computed at 100 increasing logarithmically spaced numbers of rollouts between $1$ and $n_{r}$. The result is plotted in Fig. 1, indicating the consistency of the proposed algorithm.

### IV-B Network example

Many practical networked systems can be approximated by diffusion dynamics with loss; examples include heat flow through uninsulated pipes, hydraulic flow through leaky pipes, information flow between processors with packet loss, electrical power flow between generators with resistant electrical power lines, etc. These dynamics in continuous-time act on an undirected graph with no self-loops with symmetric weighted adjacency matrix $A_{c}$, degree matrix $D_{c} = {\text{diag}{({A_{c}\text{1}_{n \times 1}})}}$, graph Laplacian $L = {D_{c} - A_{c}}$, diagonal loss matrix $F_{c}$, and diagonal input matrix $B_{c}$:

Discretizing these dynamics using the forward Euler method with a step size $T$ yields $x_{t + 1} = {{Ax_{t}} + {Bu_{t}}}$ where $A = {I - {T{({L_{c} + F_{c}})}}}$ and $B = {TB_{u}}$. Uncertainty on an edge weight of the graph i.e. on entry $(j,k)$ of $A_{c}$ manifests as a noise matrix with entries

Uncertainty on an input strength i.e. entry $(k,k)$ of $B_{u}$ manifests as a noise matrix with entries

For computational tractability we estimated only the noise variances while giving the estimator knowledge of the noise directions $A_{i}$ and $B_{j}$. To formulate this setting mathematically it is easier to work with the eigendecomposition of the noises as in. The least-squares estimation for this case is a simple modification to the full covariance estimator:

where $({\hat{\sigma}}^{2},{\hat{\delta}}^{2})$ are vectors of the noise variances,

${\overset{\sim}{A}}_{i}$ and ${\overset{\sim}{B}}_{j}$, $1 \leq i \leq r$, $1 \leq j \leq s$, are defined in the same way as $\overset{\sim}{A}$ and $\overset{\sim}{B}$ in (III-A) respectively, and ${\hat{C}}_{t} = {{\hat{X}}_{t} - {\lbrack{{\hat{\overset{\sim}{A}}{\hat{X}}_{t - 1}} + {{\hat{K}}_{BA}{\hat{W}}_{t - 1}} + {{\hat{K}}_{AB}{\hat{W}}_{t - 1}^{\intercal}} + {\hat{\overset{\sim}{B}}U_{t - 1}}}\rbrack}}$, $1 \leq t \leq \ell$.

We chose a network with $n = 8$ nodes and edges placed via the Erdos-Renyi random graph generation with random integer weights. The graph was selected to be connected so that the system would be controllable. We used rollout data of length $\ell = {{\frac{1}{2}m^{2}n^{4}} + {\frac{1}{2}m^{2}n^{2}} + m^{2} + 1} = 133185$ and collected 7 rollouts; more rollouts could be used, but empirically this amount of data was sufficient to give good estimates. Table I shows the averages and maximums of the normalized noise variance estimation errors

$\frac{1}{r}{\sum_{i}^{r}{\overline{\sigma}}_{i}^{2}}$
$\text{max}_{i}{\overline{\sigma}}_{i}^{2}$
$\frac{1}{s}{\sum_{j}^{s}{\overline{\delta}}_{j}^{2}}$
$\text{max}_{j}{\overline{\delta}}_{j}^{2}$

TABLE I: Estimation error averages and maximums.

## Conclusions

In this paper we proposed a system identification scheme for linear systems with multiplicative noise based on multiple trajectory data. By designing appropriate persistently exciting input signals, a least-squares algorithm was proposed for the joint estimation of nominal system and multiplicative noise covariances. The asymptotic consistency of the algorithm was proved, and illustrated by numerical simulations. Ongoing and future research directions include studying the convergence rate and non-asymptotic behavior of the proposed algorithm, problems of optimal input design, identification from single-trajectory data, and sparsity-promoting regularization for identification of networked systems with prior knowledge of sparsity levels.
