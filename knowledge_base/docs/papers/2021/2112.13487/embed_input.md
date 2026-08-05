<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Statistical Complexity of Interactive Decision Making

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A fundamental challenge in interactive learning and decision making, ranging from bandit problems to reinforcement learning, is to provide sample-efficient, adaptive learning algorithms that achieve near-optimal regret. This question is analogous to the classical problem of optimal (supervised) statistical learning, where there are well-known complexity measures (e.g., VC dimension and Rademacher complexity) that govern the statistical complexity of learning. However, characterizing the statistical complexity of interactive learning is substantially more challenging due to the adaptive nature of the problem. The main result of this work provides a complexity measure, the Decision-Estimation Coefficient, that is proven to be both necessary and sufficient for sample-efficient interactive learning. In particular, we provide: 1. a lower bound on the optimal regret for any interactive decision making problem, establishing the Decision-Estimation Coefficient as a fundamental limit. 2. a unified algorithm design principle, Estimation-to-Decisions (E2D), which transforms any algorithm for supervised estimation into an online algorithm for decision making. E2D attains a regret bound that matches our lower bound up to dependence on a notion of estimation performance, thereby achieving optimal sample-efficient learning as characterized by the Decision-Estimation Coefficient.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Taken together, these results constitute a theory of learnability for interactive decision making. When applied to reinforcement learning settings, the Decision-Estimation Coefficient recovers essentially all existing hardness results and lower bounds. More broadly, the approach can be viewed as a decision-theoretic analogue of the classical Le Cam theory of statistical estimation; it also unifies a number of existing approaches - both Bayesian and frequentist.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#3

<!-- chunk {"id": "body-0005", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#1~*/}}}}}

<!-- chunk {"id": "body-0006", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#2}}

<!-- chunk {"id": "body-0007", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\newcommand{\jq}{{\color{brown} jq: [#1]}} \let\OldStatex\Statex \setlength\@tempdima{\algorithmicindent}% \OldStatex\hskip\dimexpr#1\@tempdima\relax} \newcommand{\ubar}{\underaccent{\bar}} \newcommand{\Fclass}{\mathscr{F}} \newcommand{\Var}{\mathrm{Var}} \newcommand{\reg}{\mathrm{reg}} \newcommand{\afstar}{a\_{\fstar}} \let\oldparagraph\paragraph \renewcommand{\paragraph}{\oldparagraph} \title{The Statistical Complexity of Interactive Decision Making} {\small\texttt{dylanfoster@microsoft.com}} {\small\texttt{sham@seas.harvard.edu}} {\small\texttt{jianqian@mit.edu}}

<!-- chunk {"id": "body-0008", "role": "body", "section": "Paper Body", "weight": 1.0} -->

{\small\texttt{rakhlin@mit.edu}} A fundamental challenge in interactive learning and decision making, ranging from bandit problems to reinforcement learning, is to provide sample-efficient, adaptive learning algorithms that achieve near-optimal regret.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This question is analogous to the classical problem of optimal (supervised) statistical learning, where there are well-known complexity measures (e.g., VC dimension and Rademacher complexity) that govern the statistical complexity of learning. However, characterizing the statistical complexity of interactive learning is substantially more challenging due to the adaptive nature of the problem. The main result of this work provides a complexity measure, the \emph{\CompText}, that is proven to be both \emph{necessary} and \emph{sufficient} for sample-efficient interactive learning. \item a lower bound on the optimal regret for \emph{any} interactive decision making problem, establishing the \CompText as a fundamental limit. \item a unified algorithm design principle, \emph{\AlgText} (\mainalg), which transforms any algorithm for supervised estimation into an online algorithm for decision making. \mainalg attains a regret bound that matches our lower bound up to dependence on a notion of estimation performance, thereby achieving optimal sample-efficient learning as characterized by the \CompText. Taken together, these results constitute a theory of learnability for interactive decision making.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Paper Body", "weight": 1.0} -->

When applied to reinforcement learning settings, the \CompText recovers essentially all existing hardness results and lower bounds. More broadly, the approach can be viewed as a decision-theoretic analogue of the classical Le Cam theory of statistical estimation; it also unifies a number of existing approaches---both Bayesian and frequentist.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We consider an interactive, data-driven decision making setting that encompasses (structured) bandits and reinforcement learning with function approximation, and introduce the \emph{\CompText}, % a new complexity measure that is both \emph{necessary} and \emph{sufficient} for sample-efficient learning. We provide: \item A lower bound on the optimal regret for \emph{any} interactive decision making problem, which establishes that the \CompText is a fundamental limit.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\item A unified algorithm design principle, \emph{\AlgText} (\mainalg), which transforms any algorithm for supervised estimation into an algorithm for decision making, and does so in an online fashion. \mainalg attains a regret bound matching our lower bound, thereby achieving sample-efficient learning whenever sample-efficient learning is possible. Taken together, our results constitute a theory of learnability for interactive decision making. When applied to reinforcement learning, the \CompText recovers essentially all existing hardness results and lower bounds, % and leads to new, computationally efficient algorithms. Conceptually, our approach can be viewed as a decision making analogue of classical Le Cam theory in statistical estimation, and unifies a number of existing % approaches---both Bayesian and frequentist.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\hypersetup{linkcolor=blue!60!black} \addtocontents{toc}{\protect\setcounter{tocdepth}{2}} \label{sec:intro} Over the last decade, algorithms for data-driven decision making (in particular, contextual bandits and reinforcement learning) have achieved impressive empirical results in application domains ranging from online personalization systems. Algorithm design and sample complexity for data-driven decision making have a relatively complete theory for problems with small state and action spaces or short horizon. However, many of the most compelling applications necessitate long-term planning in high-dimensional spaces, where function approximation is required, and where exploration, generalization, and sample efficiency remain major challenges. For real-world problems, where data is limited, it is critical that we bridge this gap and develop sample-efficient decision making methods capable of exploring large state and action spaces.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Paper Body", "weight": 1.0} -->

With a focus on reinforcement learning, a growing body of research identifies specific settings in which sample-efficient interactive decision making is possible, typically under conditions that control the interplay between system dynamics and function approximation While these results highlight a number of important special cases (e.g., linear function approximation), it is desirable from a practical perspective to develop algorithms that accommodate \emph{general-purpose} function approximation, similar to what one expects in supervised, statistical learning. This leads to significant \item \emph{Sample complexity and fundamental limits.} In statistical learning, the classical Vapnik-Chervonenkis (VC) theory provides complexity measures (e.g., VC dimension and Rademacher complexity) that upper bound the number of samples required to achieve a desired accuracy level, as well as fundamental decision making, we lack general tools that can be systematically applied to understand sample complexity for new problem domains. often far from obvious whether existing algorithms are optimal, or to what extent they can be improved. % \item \emph{Algorithmic principles.} Can we design general-purpose algorithms for data-driven decision making that can take any class of models or policies as input and produce accurate decisions out of the box?

<!-- chunk {"id": "body-0015", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In statistical universal algorithmic principles such as empirical risk minimization (taking the function or model that best fits the data) that can be applied to any problem. In data-driven decision making, algorithm design has largely proceeded on a case-by-case basis, and developing reliable, provable algorithms for even the simplest models often requires non-trivial mathematical insights. Toward a general theory, a recent line of research proposes structural conditions that attempt to unify existing approaches to sample-efficient reinforcement learning These conditions are not known to be necessary for learning, and they do not recover existing we do not yet have a unified understanding of sample complexity and algorithm design even for the basic bandit problem (that is, reinforcement learning with horizon one) when the action space is structured and high-dimensional.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We address issues and through a two-pronged approach. We introduce a general framework for interactive, online decision making, \emph{\Framework}, which subsumes structured (high-dimensional) bandits, reinforcement learning, partially observed Markov decision processes (POMDPs), and beyond. We provide a new complexity measure, the \emph{\CompText} (\CompAbbrev) and show that it is a fundamental limit that lower bounds the sample complexity for any interactive decision making problem. We complement this result with a universal algorithm design principle, \emph{\AlgText} (\mainalg), which achieves optimal sample complexity as characterized by the \CompText whenever a notion of ``estimation complexity'' for the problem under consideration is bounded. Together, these results provide the first theory of learnability for interactive decision making.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Framework: \Framework} We consider a general framework for interactive decision making, which we refer to as \emph{\Framework} (\FrameworkShort). The protocol proceeds in $T$ rounds, where for each round $t=1,\ldots,T$: \item The \learner selects a \emph{decision} $\act\ind{t}\in\Act$, where $\Act$ is the \emph{decision space}. \item Nature selects a \emph{reward} $r\ind{t}\in\RewardSpace$ and \emph{observation} $\obs\ind{t}\in\ObsSpace$ based on the decision, where $\RSpace\subseteq\bbR$ is the \emph{reward space} and $\ObsSpace$ is the \emph{observation space}. The reward and observation are then observed by the learner.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\looseness=-1 We focus on a stochastic variant of the \FrameworkShort framework: At each timestep, the pair $(r\ind{t}, \obs\ind{t})$ is drawn independently from an unknown distribution $\Mstar(\pi\ind{t})$, where $\Mstar:\Pi\to\Delta(\cR\times\cO)$ is a \emph{model} that maps decisions to distributions over outcomes. To facilitate the use of learning and function approximation, we assume the \learner has access to a \emph{model class} $\cM$ that attempts to capture the model problem domain, $\cM$ might consist of linear models, neural networks, other complex function approximators. We make the following standard realizability which asserts that $\cM$ is flexible enough to express the true model.% \begin{assumption}[Realizability] \label{ass:realizability} The model class $\cM$ contains the true model $\Mstar$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For a model $M\in\cM$, let $\Enm{M}{\pi}\brk*{\cdot}$ denote the expectation under Further, let $\fm(\pi)\ldef{}\Enm{M}{\pi}\brk*{r}$ denote the mean reward function and $\pim\ldef{}\argmax_{\act\in\Act}\fm(\act)$ denote the decision with the greatest expected reward. Finally, we define $\Pim\ldef\crl*{\pim\mid{}M\in\cM}$ as the induced set of (potentially) optimal decisions and define $\cFm\ldef{}\crl*{\fm\mid{}M\in\cM}$ as the induced class of mean reward functions.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We evaluate the \learner's performance in terms of \emph{regret} to the optimal decision for $\Mstar$: \ldef \sum\_{t=1}^{T}\En\_{\act\ind{t}\sim{}p\ind{t}}\brk*{\fstar(\pistar) - \fstar(\act\ind{t})}, where we abbreviate $\fstar=\fmstar$ and $\pistar=\pimstar$, and where $p\ind{t}\in\Delta(\Act)$ is the learner's distribution over decisions at round $t$.\footnote{ Our results are most conveniently stated in terms of this notion of regret, but immediately extend to the empirical regret $\sum_{t=1}^{T}r\ind{t}(\pistar)-r\ind{t}(\act\ind{t})$ via standard concentration arguments.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In spite of the apparent simplicity, the \FrameworkShort framework is general enough to capture most online decision making problems. We focus on two special cases: structured bandits and reinforcement learning. \begin{example}[Structured bandits] When there are no observations (i.e., $\ObsSpace=\crl*{\emptyset}$), the \FrameworkShort framework is equivalent to the well-known \emph{structured bandit} problem adopting standard terminology, $\act\ind{t}$ is referred to as an \emph{action} or \emph{arm} (rather than a decision), and $\Act$ is referred to as the \emph{action space}. The structured bandit problem is simplest special case of our framework, but is extremely rich, and includes the following \item The classical finite-armed bandit problem with $A$ actions, where $\Act=\crl{1,\ldots,A}$ and $\cFm=\bbR^{A}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\item The linear bandit problem, in which $\Act\subseteq\bbR^{d}$ and $\cFm$ is a class of linear \item Bandit convex optimization (or, zeroth order optimization), where $\Act\subseteq\bbR^{d}$ and $\cFm$ is a class of concave\footnote{Here, $\cFm$ is concave rather than convex because we work with rewards rather than losses.} functions. \item Nonparametric bandits, where $\cFm$ is a class of Lipschitz or \Holder functions over a metric space. Despite significant research effort, there is no general theory characterizing what properties of the action space and model class determine the minimax rates for the structured bandit problem. Outside of the asymptotic regime, progress has proceeded case by case.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Paper Body", "weight": 1.0} -->

A more challenging setting is reinforcement learning (with function \begin{example}[Online reinforcement learning] We consider an episodic finite-horizon reinforcement learning setting. With $H$ denoting the horizon, each model $M\in\cM$ specifies a non-stationary Markov decision process d\_1}$, where $\cS\_h$ is the state space for layer $h$, $\cA$ is the action space, $\Pm_h:\cS_h\times\cA\to\Delta(\cS_{h+1})$ is the probability transition kernel for layer $h$, $\Rm_h:\cS_h\times\cA\to\Delta(\bbR)$ is the reward distribution for layer $h$, and $d_1\in\Delta(\cS_1)$ is the initial state distribution.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We allow the reward distribution and transition kernel to vary across models in $\cM$, but assume for simplicity that the initial state distribution is fixed.\looseness=-1 For a fixed MDP $M\in\cM$, each episode proceeds under the At the beginning of the episode, the learner selects a randomized, non-stationary \emph{policy} $\pi=(\pi_1,\ldots,\pi_H)\in\PiRNS$, where $\pi_h:\cS_h\to\Delta(\cA)$ and $\PiRNS$ denotes the set of all such policies. The episode then evolves through the following process, beginning from $s_1\sim{}d_1$. For $h=1,\ldots,H$: \item $r_h\sim\Rm(s_h,a_h)$ and $s_{h+1}\sim{}P\sups{M}(\cdot\mid{}s_h,a_h)$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For notational convenience, we take $s_{H+1}$ to be a deterministic terminal state. The value for a policy $\pi$ under $M$ is given by $\fm(\pi)\ldef\Ens{M}{\pi}\brk[\big]{\sum_{h=1}^{H}r_h}$, where $\Ens{M}{\pi}\brk{\cdot}$ denotes expectation under the process above.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In the online reinforcement learning setting, we interact with an unknown MDP $\Mstar\in\cM$ for $T$ episodes. We now show how this setting can be captured in the DMSO framework, where we take the reward $r\ind{t}$ to be the cumulative reward in the episode and the observation $o\ind{t}$ to be the observed trajectory. In particular, for each episode $t=1,\ldots,T$, the learner selects a policy $\pi\ind{t}\in\PiRNS$. The policy is executed in the MDP $\Mstar$, and the learner observes the resulting $\tau\ind{t}=(s_1\ind{t},a_1\ind{t},r_1\ind{t}),\ldots,(s_H\ind{t},a_H\ind{t},r_H\ind{t})$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Online reinforcement learning has received extensive attention, in terms of both algorithms and sample complexity bounds for specific model classes (e.g., as well as general structural results there is currently no unified understanding of what properties of the class of MDPs $\cM$ determine the optimal regret.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This formulation, where the model class $\cM$ is taken as a given, may at first seem tailored to \emph{model-based} reinforcement learning, where the underlying transition dynamics are explicitly modeled. However, we can also express \emph{model-free} reinforcement learning problems---where we instead take a class of candidate value functions $\cQ$ as given and avoid directly learning the dynamics---by choosing $\cM$ to be the set of all MDPs that are consistent with the given value function class. As we show in \pref{sec:rl}, this perspective suffices to recover standard lower bounds for model-free RL, though our upper bounds are generally only tight for model-based settings.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Further examples} Beyond these examples, the \FrameworkShort framework captures many other canonical decision making problems, including (stochastic) contextual bandits, reinforcement learning in partially observable Markov decision processes (POMDPs) and reinforcement learning with a \subsection{The \CompText} We introduce a new complexity measure, the \emph{\CompText} (\CompShort), defined for a model class $\cM$ and nominal model $\Mbar$ as \inf\_{p\in\Delta(\Act)}\sup\_{M\in\cM}\En\_{\act\sim{}p}\biggl[\underbrace{\fm(\pim)-\fm(\pi)}\_{\text{regret -\gamma\cdot\underbrace{\Dhels{M(\act)}{\Mbar(\act)}}\_{\text{estimation error for obs.}} where $\gamma>0$ is a scale parameter and

<!-- chunk {"id": "body-0030", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The \CompText is the value of a game in which the learner (represented by the min player) aims to find a distribution over decisions such that for a worst-case problem instance (represented by the max player), the \emph{regret} of their decision is controlled by the \emph{estimation error} relative to the nominal model. Conceptually, $\Mbar$ should be thought of as a guess for the true model, and the learner (the min player) aims to---in the face of an unknown environment (the max player)---optimally balance the regret of their decision with the amount information they acquire. With enough information, the learner can confirm or rule out their guess $\Mbar$, and scale parameter $\gamma$ controls how much regret they are willing to Setting & \CompShort Lower Bound & Tight?

<!-- chunk {"id": "body-0031", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\\Multi-Armed Bandit & $\sqrt{AT}$ & \cmark \\Multi-Armed Bandit w/ gap & $A/\Delta$ & \cmark\\Linear Bandit & $\sqrt{dT}$ & ~~~~~~~~~~\xmark~~($d\sqrt{T}$) \\Lipschitz Bandit & $T^{\frac{d+1}{d+2}}$ & \cmark\\ReLU Bandit & $2^{d}$ & \cmark\\Tabular RL & $\sqrt{HSAT}$ & \cmark\\Linear MDP & $\sqrt{dT}$ & ~~~~~~~~~~\xmark~~($d\sqrt{T}$) \\RL w/ linear $\Qstar$ & $2^{d}$ & \cmark \\Deterministic RL w/ linear $\Qstar$ & $d$ & \cmark\\Lower bounds for bandits and reinforcement learning recovered by the \CompText, where

<!-- chunk {"id": "body-0032", "role": "body", "section": "Paper Body", "weight": 1.0} -->

See \pref{sec:examples,sec:bandit,sec:rl} for details. The ``Tight?'' column indicates whether the lower bound is tight up to logarithmic factors and dependence on episode horizon, with the optimal rate stated for \xmark{} cases. \label{table:lower} Let us give some intuition as to how the \CompText leads to both \emph{upper} and \emph{lower} bounds on the optimal regret for decision making. On the algorithmic side (upper bounds), the connection between decision making (where the learner's decisions influence what feedback is collected) and estimation (where data is collected passively) may not seem apparent a-priori. Here, the power of the \CompText is that it---\emph{by definition}---provides a bridge. One can select decisions by building an estimate for the model using all of the observations collected so far, then sampling from the distribution $p$ that solves \pref{eq:comp} with the estimated model plugged in for $\Mbar$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Boundedness of the \CompShort implies that at every round, any learner using this strategy either enjoys small regret or acquires information, with their total regret controlled by the cumulative error for (online/sequential) estimation. This strategy generalizes notable prior approaches---Bayesian and frequentist.\looseness=-1 Of course, the perspective above is only useful if the \CompShort is indeed bounded, which itself is not immediately apparent. However, we show that the \CompShort is not only bounded (e.g., for the finite-armed bandit problem where $\Act=\crl{1,\ldots,A}$, we have $\comp(\cM)\propto\frac{A}{\gamma}$), but---turning our focus to lower bounds---quantitatively necessary for sample-efficient learning.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Developing lower bounds for a setting as general as the \FrameworkShort framework is challenging because any complexity measure needs to capture both i) simple problems like the multi-armed bandit, where the mean rewards serve as a sufficient statistic, and ii) problems with rich, structured feedback (e.g., reinforcement learning), where observations, or even structure in the noise itself, can provide non-trivial information about the underlying problem instance. Here, the information-theoretic nature of the \CompShort plays a key role. In particular, taking a dual perspective, the \CompShort can be seen to certify a lower bound on the price (in terms of regret) that \emph{any algorithm} must pay to obtain enough information to distinguish a reference model from the least favorable alternative.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our main results show that the \CompText captures the statistical complexity of interactive decision making. % \item \textbf{A new fundamental limit and lower bound.} We establish (\pref{thm:lower\_main,thm:lower\_main\_expectation}) that the \CompText is a fundamental limit for interactive decision making: For any class of models, any algorithm must have \label{eq:lower\_informal} \RegDM \approxgeq \max\_{\gamma>0}\min\crl*{\complocshort(\cM)\cdot{}T, \gamma}, where $\complocshort(\cM)$ is a certain localized variant of the \CompShort (cf. \pref{sec:main\_lower}). This lower bound holds for \emph{any model class}, with no assumption on the structure.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Paper Body", "weight": 1.0} -->

When applied to bandits and reinforcement learning, it recovers standard minimax lower bounds for canonical problems classes (\pref{sec:bandit,sec:rl}), as well as strong impossibility results for sample-efficient reinforcement learning with linear function approximation; see \pref{table:lower} for highlights. In addition, the lower bound has an appealing conceptual interpretation as a decision making analogue of classical modulus of continuity techniques in statistical estimation \item \textbf{A unified meta-algorithm.} We provide (\pref{thm:upper\_main}) a unified meta-algorithm, \AlgText{} (\mainalg), which achieves the decision making lower bound in \pref{eq:lower\_informal} whenever estimation is possible.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We show that for any model class $\cM$, the regret of \mainalg is bounded as \label{eq:upper\_informal} \RegDM \approxleq \min\_{\gamma>0} \max\crl*{\complocshort(\cM)\cdot{}T, \gamma\cdot{}\est(\cM)}, where $\est(\cM)$ is a certain classical notion of statistical estimation complexity for the class $\cM$ (for example, $\est(\cM)=\log\abs{\cM}$ for finite classes). \mainalg is a universal reduction which transforms any algorithm for online estimation with the model class $\cM$ into an algorithm for decision making. The algorithm is computationally efficient whenever the minimax program \pref{eq:comp} can be solved efficiently. This result recovers classical and contemporary sample complexity guarantees for bandits and reinforcement learning, and leads to new algorithms for various classes of interest.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Together, these results provide a theory of learnability for interactive decision making: Whenever $\cM$ has non-trivial online estimation complexity $\est(\cM)$, sublinear regret for decision making is possible \emph{if and only if} $\comp(\cM)$ decays sufficiently quickly as $\gamma\to\infty$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Additional contributions} Notable additional features of our results include: \emph{Recovering existing frameworks.} Various works have proposed structural conditions that enable sample-efficient reinforcement learning, including Bellman Rank, Witness Rank, (Bellman-) Eluder Dimension Bilinear Classes. We show that the \CompShort subsumes each of these conditions and, importantly, provides the first such necessary condition.\footnote{While the \CompShort itself can be bounded in terms of each of these complexity measures, the regret bounds we provide are primarily limited to model-based settings.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Paper Body", "weight": 1.0} -->

See section \pref{sec:rl} for detailed discussion.} \item \emph{New perspectives on existing algorithms.} Our results tie together and generalize disparate algorithmic approaches across the literature on bandits and reinforcement learning, most notably posterior sampling and information-directed sampling and the information ratio, and inverse gap weighting approaches to bandits and contextual bandits \item \emph{Seamlessly incorporating contextual information.} Our algorithms immediately extend to provide regret bounds for a \emph{contextual} variant of the \FrameworkShort framework in which the learner observes side information in the form a context (or, covariate) $x\ind{t}$ before making their decision at each round (\pref{sec:contextual}). This leads to new oracle-efficient algorithms for contextual bandits with large action spaces contextual Markov decision processes.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The first part of the paper (\pref{sec:framework,sec:algorithm}) presents central results and tools, with preliminaries in \pref{sec:prelims}. \item \pref{sec:framework} contains our main results: a universal lower bound for interactive decision making based on the \CompText, and a nearly-matching upper bound via the \AlgText{} (\mainalg) meta-algorithm. Combining these results, we provide a characterization of learnability in the \FrameworkShort framework. This section also includes extensive discussion and interpretation of the main results. \item Building on this development, \pref{sec:algorithm} provides a toolkit for deriving regret bounds using the \mainalg algorithm, including background on online estimation, general-purpose regret bounds, a Bayesian variant of the \mainalg algorithm, and other extensions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In the second part of this paper (\pref{sec:examples,sec:bandit,sec:rl}), we apply our general tools to give efficient algorithms and regret bounds for specific examples of \item \pref{sec:examples} (Illustrative Examples) serves as a warm-up, and contains detailed examples for the basic multi-armed bandit problem and tabular reinforcement learning. For both settings, we carefully show how to upper and lower bound the \CompText and derive efficient algorithms. These examples highlight a number of basic techniques which find use in later \item \pref{sec:bandit} (Application to Bandits) applies our techniques to the structured bandit problem. We recover efficient algorithms and lower bounds for well-known problems (linear bandits, convex bandits, eluder dimension, and more), then derive new guarantees based on a parameter called the \emph{star \item \pref{sec:rl} (Application to Reinforcement Learning) applies our techniques to reinforcement learning with function approximation. Highlights here include new algorithms for reinforcement learning with bilinear classes, and lower bounds for learning with linearly realizable value functions.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We conclude with a contextual extension of the \mainalg algorithm (\pref{sec:contextual}), further related work (\pref{sec:related}), and discussion (\pref{sec:discussion}). All proofs are deferred to the appendix unless otherwise stated.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{sec:prelims} \paragraph{Probability spaces} We briefly formalize the probability spaces associated with the \FrameworkShort framework. Decisions are associated with a measurable space $(\Act,\Asig)$, rewards are associated with the space $(\Rspace,\Rsig)$, and observations are associated with the space $(\Obs,\Osig)$. Let $\hist\ind{t} =(\act\ind{1},r\ind{1},\obs\ind{1}),\ldots,(\act\ind{t},r\ind{t},\obs\ind{t})$ denote the history up to time $t$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Recall that for measurable spaces $(\cX,\scrX)$ and $(\cY,\scrY)$ a probability kernel $P(\cdot\mid{}\cdot)$ from $(\cX,\scrX)$ to $(\cY,\scrY)$ has the property that 1) For all $x\in\cX$, $P(\cdot\mid{}x)$ is a probability measure, and 2) for all $Y\in\scrY$, $x\mapsto{}P(Y\mid{}x)$ is measurable. If $P(\cdot\mid{}x)$ is a $\sigma$-finite measure rather than a probability measure, we instead call $P$ a kernel.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Formally, a model $M=M(\cdot,\cdot\mid\cdot)\in\cM$ is a probability kernel from $(\Act,\Asig)$ to $(\Rspace\times\Obs,\Rsig\otimes\Osig)$. An \emph{algorithm} for horizon $T$ is specified by a sequence of probability kernels $p\ind{1},\ldots,p\ind{T}$, where $p\ind{t}(\cdot\mid\cdot)$ is a probability kernel from $(\Hspace\ind{t-1},\Hsig\ind{t-1})$ to $(\Act,\Asig)$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We assume that there exists a common dominating kernel $\dom(\act)=\dom(\cdot,\cdot\mid{}\act)$ from $(\Act,\Asig)$ to $(\Rspace\times\Obs,\Rsig\otimes\Osig)$ such that $M(\act)\ll{}\dom(\act)$ for all $M\in\cM$, $\act\in\Act$. For each $\act\in\Act$ we let $m^{\sss{M}}(\cdot,\cdot\mid{}\pi)$ denote the density of $M(\cdot,\cdot\mid{}\pi)$ with respect to $\nu(\cdot,\cdot\mid{}\act)$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This assumption facilitates the use of density estimation for our upper bounds, but is not required by our For probability distributions $\bbP$ and $\bbQ$ over a measurable space $(\Omega,\filt)$ with a common dominating measure, we define the total variation distance as \Dtv{\bbP}{\bbQ}=\sup\_{A\in\filt}\abs{\bbP(A)-\bbQ(A)} = \frac{1}{2}\int\abs{d\bbP-d\bbQ}.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The notation in \pref{eq:hellinger} (and for other divergences) reflects that this quantity is invariant under the choice of $\nu$.} \Dhels{\bbP}{\bbQ}=\int\prn*{\sqrt{d\bbP}-\sqrt{d\bbQ}}^{2}, and the Kullback-Leibler divergence is defined as \Dkl{\bbP}{\bbQ} =\left\{ \int\log\prn[\big]{ \frac{d\bbP}{d\bbQ}}d\bbP,\quad{}&\bbP\ll\bbQ,\\+\infty,\quad&\text{otherwise.} \end{array}\right.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We let $\PiRNS$ denote the collection of randomized non-stationary policies. For $\pi=(\pi_1,\ldots,\pi_H)\in\PiRNS$, $\pi_h(s,a)$ denotes the probability that action $a$ is selected in state $s$, so that $\pi_h(s)\ldef\pi_h(s,\cdot)\in\Delta(\cA)$. For a pair of policies $\pi$, $\pi'$, we define $\pi\circ_h\pi'$ as the policy that selects actions $a_1,\ldots,a_{h-1}$ using $\pi$ and selects all subsequent actions For a transition distribution $P(\cdot\mid{}\cdot,\cdot)$, we define $\brk{Pf}(s,a) =\En_{s'\sim{}P(s,a)}\brk{f(s')}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Further notation} We adopt non-asymptotic big-oh notation: For functions $f,g:\cX\to\bbR_{+}$, we write $f=\bigoh(g)$ (resp. $f=\bigom(g)$) if there exists some constant $C>0$ such that $f(x)\leq{}Cg(x)$ (resp. $f(x)\geq{}Cg(x)$) for all $x\in\cX$. We write $f=\bigoht(g)$ if $f=\bigoh(g\cdot\mathrm{polylog}(T))$, $f=\bigomt(g)$ if $f=\bigom(g/\polylog(T))$, and $f=\bigthetat(g)$ if $f=\bigoht(g)$ and $f=\bigomt(g)$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Paper Body", "weight": 1.0} -->

% We use $f\propto g$ as shorthand for $f=\bigthetat(g)$. We use $\approxleq$ only in informal statements to highlight salient elements of an inequality.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For a vector $x\in\bbR^{d}$, we let $\nrm*{x}_{2}$ denote the euclidean norm and $\nrm*{x}_{\infty}$ denote the element-wise $\ell_{\infty}$ norm. We let $\mathbf{0}$ denote the all-zeros vector, with dimension clear from context. For an integer $n\in\bbN$, we let $[n]$ denote the set $\{1,\dots,n\}$. For a set $S$, we let $\unif(S)$ denote the uniform distribution over all the elements in $S$. For a set $\cX$, we let $\Delta(\cX)$ denote the set of all Radon probability measures over $\cX$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We let $\conv(\cX)$ denote the set of all finitely supported convex combinations of elements in $\cX$, and let $\starhull(\cX,x)=\bigcup_{x'\in\cX}\conv(\crl{x',x})$ denote the star hull. We use the convention $a\wedge{}b=\min\crl{a,b}$ and $a\vee{}b=\max\crl{a,b}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For a parameter $\mu\in\brk*{0,1}$, $\Ber(\mu)$ denotes a Bernoulli random variable with mean $\mu$. Likewise, for $\mu\in\brk{-1,+1}$, $\Rad(\mu)$ denotes a (biased) Rademacher random variable with mean $\mu$, which has $\bbP(+1) = \frac{1+\mu}{2}$ and $\bbP(-1)=\frac{1-\mu}{2}$. For an element $x$ in a measurable space, we let $\delta_{x}$ denote the delta distribution on $x$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Minimax Regret: Frequentist and Bayesian} \label{sec:minimax\_swap} The main goal of this paper is to characterize what properties of the model class $\cM$ determine the \emph{minimax regret}, defined via \label{eq:minimax\_regret} \MinimaxReg = \inf\_{p\ind{1},\ldots,p\ind{T}}\sup\_{\Mstar\in\cM}\Enm{\Mstar}{p}\brk*{\RegDM(T)}, where we write $\RegDM(T)$ to make the dependence on $T$ explicit, and recall that $p\ind{t}=p\ind{t}(\cdot\mid\hist\ind{t-1})$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Paper Body", "weight": 1.0} -->

While our focus is on this frequentist notion of regret, we establish certain results by considering the \emph{Bayesian} setting in which the underlying model $\Mstar$ is drawn from a prior $\mu\in\Delta(\cM)$ that is known to the learner.\footnote{Unless otherwise specified, we assume that $\cM$ is equipped with the discrete topology, so that $\Delta(\cM)$ contains the space of finitely supported probability measures.} We define the worst-case Bayesian regret via \label{eq:minimax\_regret\_bayes} \MinimaxRegBayes = \sup\_{\mu\in\Delta(\cM)}\inf\_{p\ind{1},\ldots,p\ind{T}}\En\_{\Mstar\sim\mu}\Enm{\Mstar}{p}\brk*{\RegDM(T)}.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Building on a long line of research in online learning and bandits one can show that under mild technical conditions (essentially, whenever the prerequisites for Sion's minimax theorem are satisfied), the minimax frequentist regret and Bayesian regret coincide. This allows us to deduce existence of algorithms for the frequentist setting by exhibiting algorithms for the Bayesian setting, which is---in some cases---a simpler task. In particular, we have the following result. \begin{restatable}{proposition}{minimaxregret} \label{prop:minimax\_swap} Suppose that $\Act$ is finite and $\Rspace$ is bounded, and that for all $M\in\cM$, $\bigcup_{\act\in\Act}\supp(M(\act))$ is countable. Then we have \label{eq:minimax\_swap} We emphasize that the condition in \pref{prop:minimax\_swap} was chosen for simplicity and concreteness.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We expect that the same conclusion can be proven under far weaker conditions, though we note that minimax theorems for learning with partial information are somewhat more subtle than for classical online learning; see, e.g., We refer ahead to \pref{sec:dual} for additional discussion of connections between the frequentist and Bayesian setting, and for an analogous Bayesian counterpart to the \CompText.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{A Theory of Learnability for Interactive Decision Making} \label{sec:framework} In this section we provide our main results: a universal lower bound for interactive decision making based on the \CompText, and a nearly-matching upper bound via the \AlgText{} The section is organized as follows: \item In \pref{sec:main\_lower}, we state our main lower bound on regret. We then walk through basic examples that give intuition as to how the \CompText captures the complexity of interactive decision making, and show how the lower bound behaves for each example. \item In \pref{sec:main\_upper}, we provide our main upper bound on regret and introduce the \mainalg algorithm, highlighting how these results complement the lower bound. \item Building on these results, in \pref{sec:learnability} we provide a characterization for learnability (i.e., achievability of non-trivial regret) based on the \CompText.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\item \pref{sec:main\_bayes} gives the last major result of the section: a refinement of the main upper bound with weaker dependence on model estimation complexity. We conclude the section by discussing gaps between the upper and lower bounds, opportunities for improvement, and subsequent work (\pref{sec:main\_discussion}). All proofs are deferred to \pref{app:framework}.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Lower Bound: The \CompText is a Fundamental Limit} \label{sec:main\_lower} We now present the main lower bound based on the \CompText. The result is proven using a decision-theoretic adaptation of the \emph{local minimax} method the proof uses the \CompShort to show that, for any nominal model $\Mbar\in\cM$, any algorithm must either experience large regret on $\Mbar$ or on a worst-case alternative model in the neighborhood of $\Mbar$. To state the result, we formalize the notion of a neighborhood via a \emph{localized} restriction of the class $\cM$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{definition}[Localized model class] For a model class $\cM$ and reference model $\Mbar\in\cM$, we define \cMloc[\veps](\Mbar) = \crl*{ M\in\cM: \fmbar(\pimbar) \geq{} \fm(\pim) - \veps as the neighborhood of $\Mbar$ at radius $\veps$. The localized model class is tailored to decision making and asserts that no alternative should have mean reward substantially larger than that of the nominal model, but otherwise does not place any restriction on the mean reward function or observation distribution.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our lower bound takes the worst case over all possible nominal models. We define the shorthand \comp(\cM)=\sup\_{\Mbar\in\cM}\comp(\cM,\Mbar) \mathand \comploc{\veps}(\cM)=\sup\_{\Mbar\in\cM}\comp(\cMloc[\veps](\Mbar),\Mbar).\label{eq:comp\_short} where $\comp(\cM,\Mbar)$ is defined in \pref{eq:comp}. We let $\abscont $ denote a bound on the density ratio over all models.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Precisely, we define $\abscont=\sup_{M,M'\in\cM}\sup_{\act\in\Act}\sup_{A\in{}\Rsig\otimes\Osig}\crl*{\frac{M(A\mid\act)}{M'(A\mid{}\act)}}\vee{}e$; finiteness of this quantity is not necessary, but leads to tighter guarantees.\footnote{We do not require that $\abscont<\infty$, but whenever this holds we can remove certain $\log(T)$ factors in \pref{thm:lower\_main,thm:lower\_main\_expectation} for tighter results.}\looseness=-1 The main lower bound is as follows.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Paper Body", "weight": 1.0} -->

$\abscont=\sup_{M,M'\in\cM}\sup_{\act\in\Act}\sup_{A\in{}\Rsig\otimes\Osig}\crl*{\frac{M(A\mid\act)}{M'(A\mid{}\act)}}\vee{}e$.\footnote{We do not require that $\abscont<\infty$, but whenever this holds we can remove certain $\log(T)$ factors in \pref{thm:lower\_main} for a tighter result.} The \begin{restatable}[Main lower bound]{theorem}{lowermain} \label{thm:lower\_main} Consider a model class $\cM$ with $\cF_{\cM}\subseteq(\Act\to\brk*{0,1})$, and let $\delta\in$ and $T\in\bbN$ be fixed.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\pref{thm:lower\_main} shows that for any model class, any $\RegDM\approxgeq{}\max_{\gamma\approxgeq\sqrt{T}}\min\crl[\big]{\compthmone\cdot{}T, \gamma}$ with moderate probability. The result serves as a converse to high-probability upper bounds we establish in the sequel, though in general it does not lead to optimal lower bounds on \emph{expected} regret. Our next result is a variant of \pref{thm:lower\_main} that provides stronger lower bounds on expected regret using a more restrictive notion of localization.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Define $\gm(\pi) \ldef \fm(\pim) - \fm(\pi)$ and \label{eq:localized\_infinity} \cMinf[\veps](\Mbar) = \crl*{ M\in\cM: \abs*{\gm(\pi) - \gmbar(\pi)}\leq\veps\;\;\forall{}\pi\in\Pi \begin{restatable}[Main lower bound---in-expectation version]{theorem}{lowermainexpectation} \label{thm:lower\_main\_expectation} Consider a model class $\cM$ with $\cF_{\cM}\subseteq(\Act\to\brk*{0,1})$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Let $T\in\bbN$ be fixed and define $\Ct\ldef{}2^{11}\log(2T\wedge{}\abscont)$ and $\vepslowg{}\ldef \Ct^{-1}\frac{\gamma}{T}$. Then for any algorithm, there exists a model in $\cM$ for which \label{eq:lower\_main\_expectation} \En\brk*{\RegDM}\geq{} 6^{-1}\cdot\max\_{\gamma>0}\sup\_{\Mbar\in\cM}\comp(\cMinf[\vepslowg](\Mbar),\Mbar)\cdot{}T.% Despite using a stronger $L_{\infty}$ notion of localization, this result suffice to derive the lower bounds in \pref{table:lower}.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In general, any lower bound based on the \CompShort must make use of localization, as there exist classes for which the global DEC is larger than the minimax rate. See \pref{sec:main\_discussion} for discussion.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Lower Bound and \CompText: Basic Properties and Intuition} \label{sec:intuition} \newcommand{\Mbaro}{\Mbar\_{\cO}}% \newcommand{\Mbarr}{\Mbar\_{\cR}}% To build intuition, we take this opportunity to highlight some basic properties of the \CompText and how these properties influence the behavior of our lower bounds. To keep the examples we consider as simple as possible, we only sketch the proof details. We refer ahead to \pref{sec:examples,sec:bandit,sec:rl} for examples with complete calculations. Additional technical aspects of the lower bound are discussed at the end of the section (\pref{sec:main\_discussion}).% \paragraph{Capturing the complexity of decision making with As a starting point, we consider the behavior of the \CompText and the lower bounds in \pref{thm:lower\_main,thm:lower\_main\_expectation} for bandit-type problems (of varying degrees of structure) in which only reward-based feedback is available.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Here, a basic property of the \CompText is that it reflects the amount of information that any given decision reveals about other possible decisions, thereby acting as a measure of intrinsic dimension. To illustrate this point, we focus on two problems at opposite ends of the bandit spectrum: Finite-armed bandits and bandits with full information.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{example}[Finite-armed bandits] \label{ex:bandit\_lower} For the classical multi-armed bandit problem, we have $\Act=\brk*{A}$, $\Rspace=\brk{0,1}$, and $\Obs=\NullObs$, and the model class $\cM=\crl*{M:M(\act)\in\Delta(\Rspace)}$ consists of all possible distributions over $\Rspace$. Let us sketch a lower bound on the \CompText for this setting.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Fix $\Delta\in(0,\nicefrac{1}{2})$ and define a sub-family of models $\cM'=\crl*{M_1,\ldots,M_A}\cup\crl*{\Mbar}$ via $M_i(\act)\ldef{}\Ber(\nicefrac{1}{2}+\Delta\indic\crl{\act=i})$ and $\Mbar(\act)\ldef\Ber(\nicefrac{1}{2})$. In other words, each model $M_i$ has $A-1$ arms with suboptimality gap $\Delta$ relative to the optimal arm $i$, while the model $\Mbar$ has identical rewards for all arms.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Paper Body", "weight": 1.0} -->

One can verify that $\Dhels{M_i(\act)}{\Mbar(\act)}\approxleq{}\Delta^{2}\cdot{}\indic\crl{\act=i}$ (cf. \pref{lem:divergence\_bernoulli}) $\fmi(\pimi)-\fmi(\pi)\geq{}\Delta\cdot{}\indic\crl{\act\neq{}i}$. In other words, for each model, only a single decision reveals information about the model's identity and leads to low regret.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{eq:example\_follow} Crucially, because the decisions that reveal information are disjoint, the negative contribution from the Hellinger divergence scales as $A^{-1}$. By choosing $\Delta\propto{}\frac{A}{\gamma}$, we conclude that $\comp(\cM',\Mbar)\approxgeq{}\frac{A}{\gamma}$, and with more care, we show in \pref{sec:examples} that this argument in fact implies that (i) $\cM'\subseteq\cMinf[\vepslowg](\Mbar)$ whenever $\gamma\approxgeq\sqrt{AT}$, and (ii) $\abscontp=\bigoh$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Plugging these values into \pref{thm:lower\_main\_expectation}, the lower bound in \pref{eq:lower\_main\_expectation} yields \En\brk*{\RegDM} \approxgeq{} \max\_{\gamma\approxgeq\sqrt{AT}}\crl*{\frac{A}{\gamma}} = \bigom\prn[\big]{\sqrt{AT}}, which matches the well-known minimax rate. In \pref{sec:examples} we provide a matching upper bound of the form $\comp(\cM)\leq\frac{A}{\gamma}$, which certifies that this lower bound on the \CompShort is optimal. The finite-armed bandit setting is completely unstructured in the sense that choosing a given arm $\act$ reveals no information about the others. The next example, \emph{bandits with full information}, lies at the opposite extreme.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Here, each arm reveals the rewards for all other arms, completely removing the need \begin{example}[Bandits with full information] \label{ex:full\_info\_lower} Consider a full-information variant of the bandit setting. We have $\Act=\brk{A}$ and $\cR=\brk{0,1}$, and for a given decision $\act$ we observe a reward $r$ as in \pref{ex:bandit\_lower}, but also receive an observation $o = (r(\pi'))_{\pi'\in\brk{A}}$ consisting of (counterfactual) rewards for every action.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For a given model $M$, let $\Mr(\pi)$ denote the distribution over the reward for $\pi$. Then for any decision $\pi$, since all rewards are observed, the data processing inequality implies that for all $\pi'$, \label{eq:hellinger\_full\_info} \Dhels{M(\pi)}{\Mbar(\pi)}\geq{} \Dhels{\Mr(\pi')}{\Mbarr(\pi')}. Using this property, we can show that $\comploc{\vepslowg}(\cM)\propto\frac{1}{\gamma}$. We sketch a proof of the upper bound; we find this to be more illuminating than the lower bound for this example because it directly highlights how extra information helps to shrink the \CompShort.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This certifies that for all $M\in\cM$, the choice for $p$ above satisfies \[\En\_{\act\sim{}p}\brk*{\fm(\pim)-\fm(\pi)-\gamma\cdot\Dhels{M(\act)}{\Mbar(\act)}}\approxleq{}\frac{1}{\gamma},\] so we have $\comp(\cM,\Mbar)\approxleq{}\frac{1}{\gamma}$. A matching lower bound follows by adapting \pref{ex:bandit\_lower}. Comparing to the finite-armed bandit, we see that the \CompShort for this example is independent of $A$, which reflects the information sharing. The final lower bound from \pref{thm:lower\_main\_expectation} takes the form \En\brk*{\RegDM} \geq \bigom\prn[\big]{\sqrt{T}}.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In \pref{sec:bandit} we consider structured bandit problems that lie between the extremes above, including linear and convex bandits. These problems typically have $\comp(\cM)\propto\frac{\mathsf{dim}}{\gamma}$, where---generalizing \pref{ex:bandit\_lower,ex:full\_info\_lower}---$\mathsf{dim}$ is a quantity that reflects the intrinsic problem dimension. In general, however, the \CompShort can exhibit slower decay as a function of $\gamma$, particularly for nonparametric problems where the optimal regret is large than $\sqrt{T}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\pref{ex:bandit\_lower,ex:full\_info\_lower} can be thought of as ``noise agnostic'' bandit problems, in the sense that the mean rewards serve as a sufficient statistic and the reward distribution is otherwise uninformative. However, any complexity measure which claims to characterize the complexity of decision making must account for degenerate problems, where seemingly irrelevant properties of the noise distribution encode non-trivial information about the problem instance. The following example highlights one such problem.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\pref{ex:bandit\_lower,ex:full\_info\_lower} can be thought of as bandit problems with ``problem-instance agnostic'' noise, in the sense that the mean rewards serve as a sufficient statistic, while the additive noise (in the reward distribution) is otherwise uninformative about the problem instance. However, any complexity measure which claims to characterize the complexity of decision making must account for more general (and possibly corner-case) problems, where seemingly irrelevant properties of the noise distribution can encode non-trivial information about the problem instance itself. The following example highlights one such problem.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{example}[Bandits: hiding information in lower order bits] \label{ex:lower\_bits} Consider a family of multi-armed bandit models with $\Act=\brk{A}$. Following \pref{ex:bandit\_lower}, fix $\Delta\in(0,\nicefrac{1}{2})$ and define $\cM=\crl*{M_1,\ldots,M_A}\cup\crl*{\Mbar}$ via $M_i(\act)\ldef{}\cN(\nicefrac{1}{2}+\Delta\indic\crl{\act=i}, 1)$ and $\Mbar(\act)\ldef{}\cN(\nicefrac{1}{2}, 1)$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Paper Body", "weight": 1.0} -->

As defined, this family has the same lower bound $\comp(\cM,\Mbar)\geq{}\frac{A}{\gamma}$ as in \pref{ex:bandit\_lower}, because $M_i$ and $\Mbar$ can only be distinguished by choosing $\act=i$, and the Hellinger distance for this arm scales as $\Delta^{2}$. Now, suppose we modify each model $M_i$ such that $M_i(\act)$ is unchanged for $\pi\neq{}i$, but for $\pi=i$, the reward $r$ is generated by sampling $r'\sim{}\cN(\nicefrac{1}{2}+\Delta, 1)$, then setting bits $N,\dots,N+\ceil{\log_2(A)}$ in the reward's infinite-precision binary representation to encode index $i$, where $N\in\bbN$ is a parameter.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In other words, if decision $i$ is chosen in model $M_i(\act)$, then the lower order bits of the infinite precision representation of the observed reward will reveal that $i$ is in fact the optimal arm. Taking $N$ large makes the mean reward $\fmi(i)$ arbitrarily close to $\nicefrac{1}{2}+\Delta$, \Dhels{M\_i(\act)}{\Mbar(\act)} \propto{}\indic\crl{\act=i} for all $\act$ when $A$ is sufficiently large.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Paper Body", "weight": 1.0} -->

That is, compared to \pref{ex:bandit\_lower}, the Hellinger distance does not scale with the gap $\Delta$ due to the auxiliary information encoded in bits $N,\dots,N+\ceil{\log_2(A)}$.\footnote{As $N$ and $A$ grow, the probability of observing any given string in the bits $N,\dots,N+\ceil{\log_2(A)}$ becomes arbitrarily small under $\Mbar$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This causes the total variation distance (and consequently Hellinger distance) to become constant.} Choosing $\Delta=1/2$ and adapting the argument in \pref{ex:bandit\_lower} (where we introduce the expectation over $i\sim\unif(\brk{A})$ as in \pref{eq:example\_follow}), \comp(\cM\_{1/2}(\Mbar),\Mbar) \approxgeq{} 1 - \gamma\cdot\frac{1}{A} \approxgeq{}\indic\crl{\gamma\leq{}A/2}, and \pref{thm:lower\_main\_expectation} yields \En\brk*{\RegDM} \geq \bigomt(\min\crl{A,T}).

<!-- chunk {"id": "body-0089", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This is seen to be optimal, since we can detect the index of the underlying instance with constant probability by enumerating over the arms a single time.% Note that for this example, working with Hellinger distance (or another information-theoretic divergence) is critical. A weaker divergence such as the squared distance $\Dsq{M_i(\act)}{\Mbar(\act)}\ldef{}(\fmi(\act)-\fmbar(\act))^2$ would miss the information hiding in the lower order bits. Further examples with a similar information-theoretic flavor include noiseless multi-armed bandits, as well as ``cheating code'' problems of the type considered, where a basic multi-armed bandit problem instance is equipped with auxiliary arms that---when queried---directly reveal the identity of the instance.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{From reward-based feedback to general observations} Generalizing \pref{ex:lower\_bits}, one can create structured bandit problems in which arbitrary auxiliary information is hidden in the reward The \FrameworkShort framework makes auxiliary information explicit via the observations in the process $(r,o)\sim{}M(\act)$, which we find to be more clear conceptually. Our last example considers a setting where accounting for such observations is crucial. \begin{example}[Importance of observations for reinforcement learning] In the tabular (finite state/action) reinforcement learning setting, the model class $\cM$ is the collection of all non-stationary MDPs with state space $\cS=\brk{S}$, action space $\cA=\brk{A}$, and horizon $H$; we have $\Act=\PiRNS$ (recall that $\PiRNS$ is the set of randomized non-stationary policies).

<!-- chunk {"id": "body-0091", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For a given MDP $M$, when $(r,o)\sim{}M(\pi)$, the reward signal $r$ is the total reward for an episode in which the policy $\pi$ is executed, and the observation $o$ is the resulting trajectory. Here, if only reward information were available, sample complexity $2^{\bigom(H)}$ would be unavoidable. However, because trajectories are observed, the problem admits polynomial sample complexity. We show (\pref{sec:examples}) that \comploc{\vepslowg}(\cM) \propto{} \frac{\poly(S,A,H)}{\gamma}, whenever $\gamma\geq{}\sqrt{\poly(S,A,H)\cdot{}T}$, which leads to $\sqrt{\poly(S,A,H)\cdot{}T}$ upper and lower bounds on regret. Similar discussion applies to essentially all non-trivial reinforcement learning problems, and highlights the necessity of learning from observations.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Because the Decision-Estimation Coefficient is able to account for bandit problems with auxiliary information in the reward signal, it incorporates additional observations seamlessly.\looseness=-1 \paragraph{Additional information-theoretic considerations} We conclude by briefly discussing some additional information-theoretic properties of the \CompText.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{example}[Filtering irrelevant information] Adding observations that are unrelated to the model under consideration never changes the value of the \CompText. In more detail, consider a model class $\cM$ with observation space $\cO_1$, and consider a class of conditional distributions $\cD$ over a secondary observation space $\cO_2$, where each $D\in\cD$ has the form $D(\pi)\in\Delta(\cO_2)$. For $M\in\cM$ and $D\in\cD$, let $(M\otimes{}D)(\pi)$ be the model that, given $\act\in\Act$, samples $(r,o_1)\sim{}M(\pi)$ and $o_2\sim{}D(\pi)$, then emits \cM\otimes\cD=\crl*{M\otimes{}D\mid{}M\in\cM,D\in\cD}.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Then for all $\Mbar\in\cM$ and $\Dbar\in\cD$, \comp(\cM\otimes\cD,\Mbar\otimes\Dbar) = \comp(\cM,\Mbar). This can be seen to hold by restricting the supremum in \pref{eq:comp} to range over models of the form $M\otimes\Dbar$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{example}[Data processing] Passing observations through a channel never decreases the \CompText. Consider a class of models $\cM$ with observation space $\cO$. Let $\rho:\cO\to\cO'$ be given, and define $\rho\circ{}M$ to be the model that, given decision $\pi$, samples $(r,o)\sim{}M(\pi)$, then emits $\rho\circ\cM\ldef{}\crl*{\rho\circ{}M\mid{}M\in\cM}$. Then for all $\Mbar\in\cM$, we have \comp(\cM,\Mbar) \leq{} \comp(\rho\circ{}\cM,\rho\circ\Mbar).

<!-- chunk {"id": "body-0096", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This is an immediate consequence of the data processing inequality for Hellinger distance, which implies that $\Dhels{\prn[\big]{\rho\circ{}M}(\act)}{\prn[\big]{\rho\circ\Mbar}(\act)}\leq{}\Dhels{M(\act)}{\Mbar(\act)}$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Paper Body", "weight": 1.0} -->

All of the properties we have discussed up to this point are essential for any complexity measure that aims to characterize the statistical complexity of general decision making problems. With this in mind, we proceed to sketch the proof of \pref{thm:lower\_main}; the proof for \pref{thm:lower\_main\_expectation} follows similar reasoning.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{\preft{thm:lower\_main}: Proof Sketch} The key idea behind \pref{thm:lower\_main} is to show that for any algorithm $p$ and nominal model $\Mbar$, the \CompText certifies a lower bound on the price (in terms of regret) that the algorithm must pay to obtain enough information to distinguish the nominal model from an adversarially chosen alternative.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In particular, we will prove that for any $\gamma\approxgeq{}\sqrt{T}$ (recall the constraints on $\gamma$ in \pref{thm:lower\_main}) and $\Mbar\in\cM$, for any $\veps>0$ sufficiently small (as a function model $M\in\cMloc[\veps](\Mbar)$ such that \label{eq:lower\_sketch0} \min\crl[\big]{\prn*{\comp(\cMloc[\veps](\Mbar),\Mbar)-\delta}\cdot{}T, \gamma} with probability at least $\Omega(\delta)$. From here, the result in \pref{eq:lower\_main} follows by maximizing over $\Mbar$ and $\gamma$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Let $T\in\bbN$, $\gamma>0$, and $\veps>0$ be fixed and consider an algorithm $p = \crl*{p\ind{t}(\cdot\mid\cdot)}_{t=1}^{T}$. Recall that $\Enm{M}{p}\brk{\cdot}$ denotes the expectation over the history $\hist\ind{T}$ when $M$ is the underlying problem instance and $p$ is the algorithm. For each model $M$, let \pmdist\ldef\Enm{M}{p}\brk*{\frac{1}{T}\sum\_{t=1}^{T}p\ind{t}(\cdot\mid{}\hist\ind{t-1})} denote the average (conditional) distribution over decisions under $M$. Fix a nominal model $\Mbar$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In particular, if $M\in\cMloc[\veps](\Mbar)$ attains the supremum above, then by rearranging we have \En\_{\act\sim\pmbar}\brk*{\fm(\pim) - \fm(\act)} \geq{} \gamma\cdot \En\_{\act\sim\pmbar}\brk*{\Dhels{M(\act)}{\Mbar(\act)}} + \comp(\cMloc[\veps](\Mbar),\Mbar).

<!-- chunk {"id": "body-0102", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{eq:lower\_sketch1} Note that due to the equality \frac{1}{T}\cdot{}\Enm{M}{p}\brk*{\RegDM}= \En\_{\act\sim{}\pmdist}\brk*{\fm(\pim) - \fm(\act)} % \label{eq:lower\_sketch2}, the result would be established if the left-hand side of \pref{eq:lower\_sketch1} were to be replaced by $\En_{\act\sim\pmdist}\brk*{\fm(\pim) - \fm(\act)}$ (recalling that $\Dhels{M(\act)}{\Mbar(\act)}$ is non-negative).

<!-- chunk {"id": "body-0103", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{eq:lower\_sketch2} The majority of the technical effort behind the proof is to use a change of measure argument to show that as long as the localization radius $\veps$ is sufficiently small as a function of $\gamma$ and $T$, \En\_{\act\sim\pmbar}\brk*{\fm(\pim) - \fm(\act)}\approxleq{}\En\_{\act\sim{}\pmdist}\brk*{\fm(\pim) - \En\_{\act\sim\pmbar}\brk*{\Dhels{M(\act)}{\Mbar(\act)}}.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Paper Body", "weight": 1.0} -->

because the change of measure argument above requires that $\RegDM\approxleq{}\gamma$ with high probability. \pref{eq:lower\_sketch0} by optimizing over $\Mbar$ and $\gamma$.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For \pref{thm:lower\_main\_expectation}, the main difference from the proof above is that the $L_{\infty}$ notion of localization in \pref{eq:localized\_infinity} allows for a stronger change of measure argument.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{\mainalgsection: A Unified Meta-Algorithm for Interactive Decision Making} \label{sec:main\_upper} With a fundamental limit based on the \CompText established, we now state the upper bound on regret that serves as its counterpart. Our main regret bound is achieved by the \emph{\AlgText} meta-algorithm (\mainalg), described in \pref{alg:main}. The algorithm is based on the primitive of an \emph{online estimation oracle}, which generalizes the notion of online regression oracle used in closely related work on the contextual bandit problem.\looseness=-1 An online estimation oracle, which we denote by $\AlgEst$, is an algorithm that attempts to estimate the underlying model $\Mstar$ from data in a sequential fashion (typically via density estimation), and can be thought of as an (implicit) input to \mainalg.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Paper Body", "weight": 1.0} -->

At each round $t$, given the observations and rewards collected so far, the estimation oracle produces an \Mhat\ind{t}=\AlgEst\ind{t}\prn*{ \crl*{(\act\ind{i}, r\ind{i},\obs\ind{i})}\_{i=1}^{t-1} } for the true model $\Mstar$. Using this estimate, the most basic variant of \mainalg (\optionone in \pref{alg:main}) proceeds by computing the distribution $p\ind{t}$ that achieves the value $\comp(\cM,\Mhat\ind{t})$ for the \CompText.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Paper Body", "weight": 1.0} -->

That is, defining \label{eq:game\_value} \En\_{\act\sim{}p}\biggl[\fm(\pim)-\fm(\pi) -\gamma\cdot\DhelsX{\big}{M(\act)}{\Mhat(\act)} \label{eq:algorithm\_argmin} p\ind{t} = \argmin\_{p\in\Delta(\Act)}\sup\_{M\in\cM} \gameval{\Mhat\ind{t}}(p, M). \mainalg then samples the decision $\act\ind{t}$ from this distribution and moves on to the next round. This approach, where we map an estimate to a decision in a simple per-round fashion, can be viewed as a generalization of the \squarecb algorithm of \optionone of \mainalg leads to regret bounds that scale with $\comp(\cM)$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We achieve a localized regret bound that matches the quantity $\comploc{\veps}(\cM)$ appearing in \pref{thm:lower\_main} using a more sophisticated variant of \mainalg (\optiontwo in \pref{alg:main}) augments the approach above by first restricting to a Hellinger confidence set $\cM\ind{t}\subseteq\cM$ based on the estimators $\crl[\big]{\Mhat\ind{i}}_{i=1}^{t-1}$, then solving the minimization problem in \pref{eq:algorithm\_argmin} using the restricted set $\cM\ind{t}$ rather than the whole model class. We state both variants (\optionone and \optiontwo) because the former is simpler and more efficient, yet suffices for essentially all applications we consider. \optiontwo---while important for matching \pref{thm:lower\_main} as closely as possible---is mainly of theoretical interest.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We show that \mainalg serves as a universal reduction from decision making to estimation. Whenever the online estimation algorithm $\AlgEst$ can accurately estimate the true model (with respect to Hellinger distance), \mainalg enjoys low regret for decision making, with the bound on regret determined by the \CompText. The process bears some similarity to the certainty equivalence principle in control, which also provides a conceptual separation of estimation and decision making. The main difference is that rather than simply selecting the optimal decision for the estimated model (which would have poor exploration), we solve the minimax program in \pref{eq:algorithm\_argmin} with the estimated model to balance exploration and exploitation.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Finite Model Classes} While our most general guarantees for \mainalg hold for any choice of the estimator $\AlgEst$, in this section we state specialized guarantees---first for finite, then general model classes---that allow for easy comparison with our lower bounds (\pref{thm:lower\_main,thm:lower\_main\_expectation}); general results are deferred to \pref{sec:algorithm}. To state the guarantees in the simplest form possible, we make the following basic regularity assumption.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{ass:localization\_constant} There exists a constant $\Cloc>1$ such that for all models $\Mbar$ and all $\gamma>0$, $\veps>0$, \[\comp(\cMloc[(\Cloc\cdot\veps)](\Mbar),\Mbar)\leq{}\Cloc\cdot{}\comp(\cMloc[\veps](\Mbar),\Mbar).\] Note that if $\comp(\cMloc[\veps](\Mbar),\Mbar)\propto\veps^{\rho}$ for $\rho\leq{}1$, this is assumption is satisfied for all $\Cloc>1$. \begin{restatable}[Main upper bound---finite class version]{theorem}{uppermain} \label{thm:upper\_main} Fix $\delta\in$.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Then \pref{alg:main}, appropriate choice for parameters and estimation oracle, ensures that with probability at least $1-\delta$, \label{eq:upper\_main} C\cdot{}\min\_{\gamma>0}\max\crl[\bigg]{\sup\_{\Mbar\in\conv(\cM)}\comp(\cMloc[\vepsupg](\Mbar),\Mbar)\cdot{}T,\; \gamma\cdot{}\log(\abs{\cM}/\delta)}.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\State \textbf{parameters}: \Statex Online estimation oracle $\AlgEst$. \Statex Exploration parameter $\gamma>0$. \Statex Confidence radius $R>0$. \algcommentlight{\optiontwo only.} \State Compute estimate $\Mhat\ind{t} = \AlgEst\ind{t}\prn[\Big]{ \crl*{(\act\ind{i}, r\ind{i},\obs\ind{i})}_{i=1}^{t-1} }$.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\caption{Estimation to Decision-Making Meta-Algorithm (\mainalg)} \label{alg:main} This theorem is a special case of a more general result, \pref{thm:upper\_general} in \pref{sec:algorithm}. The upper bound is seen to have a similar form to the lower bound in \pref{thm:lower\_main}.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The min-max and max-min above can be exchanged under mild conditions on $\comploc{\veps}(\cM)$. The most important difference between the rates is the presence of the term $\log\abs{\cM}$ in \pref{thm:upper\_main}, which serves as an upper bound on the complexity of statistical estimation for the model class $\cM$.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Paper Body", "weight": 1.0} -->

A secondary difference is that the upper bound in \pref{thm:upper\_main} uses the class $\conv(\cM)$, while the lower bound in \pref{thm:lower\_main} In terms of failure probability, the lower bound in \pref{thm:lower\_main} provides a meaningful converse to \pref{thm:upper\_main} in the moderate probability regime where $\delta\approxleq{}\compthmone$; setting $\delta\propto{}1/\sqrt{T}$ suffices for non-trivial classes.\footnote{We use the term ``non-trivial'' to refer to any class that embeds the two-armed bandit problem.} With this choice, the dependence on $\delta$ in the lower bound vanishes and the $\log(1/\delta)$ factor in the upper bound becomes $\log(T)$. We conclude that (up to the other differences discussed above), the upper bound cannot be improved beyond this logarithmic factor in this probability regime.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In addition, whenever the localized classes $\cMloc(\Mbar)$ and $\cMinf(\Mbar)$ have similar complexity (such is the case for all of the examples in \pref{table:lower}), \pref{thm:lower\_main\_expectation} provides an in-expectation lower bound of the same order.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Gaps between the upper and lower bounds are discussed in further detail in \pref{sec:main\_discussion}.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Achieving the localized result in \pref{thm:upper\_main} requires more effort, and relies on \optiontwo. The key idea is to use certain properties of the minimax program \pref{eq:algorithm\_argmin} to relate the value of the \CompText for the confidence sets $\cM\ind{t}$ to the value of the localized \CompShort appearing in \pref{eq:upper\_main}.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Infinite Model Classes} In order to incorporate rich, potentially nonparametric classes of models, we provide a generalization of \pref{thm:upper\_main} based on covering numbers. This extension is important in our applications to bandits and reinforcement learning (\pref{sec:bandit,sec:rl}).

<!-- chunk {"id": "body-0122", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{definition}[Model class covering number] A model class $\cM'\subseteq\cM$ is said to be an $\veps$-cover for \forall{}M\in\cM\quad\exists{}M'\in\cM'\quad\text{s.t.}\quad \sup\_{\act\in\Act}\Dhels{M'(\act)}{M(\act)}\leq{}\veps^{2}. We let $\cN(\cM,\veps)$ denote the size of the smallest such cover, and define \MComp \ldef{} \inf\_{\veps\geq{}0}\crl*{ \log\cN(\cM,\veps)+\veps^{2}T as a fundamental complexity parameter associated with $\cM$.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Basic examples include parametric models in $d$ dimensions (i.e., $\log\cN(\cM,\veps)\propto{}d\log(1/\veps)$) where $\MComp=\bigoht(d)$, and nonparametric models with $\log\cN(\cM,\veps)\propto\veps^{-\rho}$ for $\rho>0$, where $\MComp=\bigoh(T^{\frac{\rho}{2+\rho}})$.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Beyond requiring bounded covering numbers, we place a (fairly weak) regularity condition on the class of densities associated with the model class $\cM$, which is standard within the literature on density (cf. \pref{sec:prelims}) that $\densm(\cdot,\cdot\mid{}\cdot)$ denotes the conditional density for $M$ under the common conditional measure $\nu(\cdot,\cdot\mid{}\cdot)$. \begin{assumption}[Bounded densities] \label{ass:finite\_measure} There exists a constant $B\geq{}e$ such that: \item $\dom(\Rspace\times\Ospace\mid{}\act)\leq{}B$ for all $\act\in\Act$.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Paper Body", "weight": 1.0} -->

$\sup_{\act\in\Act}\sup_{(r,o)\in\Rspace\times\Ospace}\densm(r,o\mid{}\act)\leq{}B$ Our result scales with $\log(B)$, which is constant for bandit problems with bounded rewards, logarithmic for reinforcement learning problems with finite state/action spaces, and polynomial in dimension for continuous reinforcement learning problems. See \pref{sec:rl} for further discussion.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{restatable}[Main upper bound---general version]{theorem}{uppermaininfinite} \label{thm:upper\_main\_infinite} Let $\delta\in$ be given, and let $\Cloc$ be as in \pref{ass:localization\_constant}. Assume that $\Rspace\subseteq\brk*{0,1}$ and that \pref{ass:finite\_measure} holds. Define $C_1=\bigoh(\Cloc^2\log_{\Cloc}(T)\log^2(BT))$, $C_2=\bigoh(\log^2(BT))$, and $\vepsupg=C_2\prn[\big]{\frac{\gamma}{T}(\MComp +\log(\delta^{-1})) + \sup_{\Mbar\in\conv(\cM)}\comp(\cM,\Mbar) + \gamma^{-1}}$.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Then \pref{alg:main}, with an appropriate choice of parameters and estimation oracle, guarantees that with probability at least $1-\delta$, \label{eq:upper\_main\_infinite} C\_1\cdot{}\min\_{\gamma>0}\max\crl[\bigg]{\sup\_{\Mbar\in\conv(\cM)}\comp(\cMloc[\vepsupg](\Mbar),\Mbar)\cdot{}T,\; \gamma\cdot{}(\MComp +\log(\delta^{-1}))}.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{sec:learnability} In statistical learning and related settings, a long line of research on \emph{learnability} provides necessary and sufficient conditions under which a hypothesis class under consideration is \emph{learnable} in the sense that there exist algorithms with non-trivial sample complexity with our main upper and lower bounds, we use the \CompText to provide an analogous characterization of learnability (i.e., existence of algorithms with sublinear regret) in the \FrameworkShort framework.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our characterization of learnability applies to model classes $\cM$ that are i) convex, and ii) admit non-trivial estimation complexity. In addition, we make the following mild regularity assumption. \label{ass:mild} There exists $M_0\in\cM$ such that $f^{\sss{M_0}}$ is constant. This assumption is satisfied for all of the examples considered in this paper. The characterization is as follows. \begin{restatable}[Learnability]{theorem}{learnabilitymain} \label{thm:learnability\_main} Assume that $\Rspace\subseteq\brk*{0,1}$, and that \pref{ass:finite\_measure} and \pref{ass:mild} hold. Suppose that $\cM$ is convex and has $\MComp=\bigoht(T^{q})$ for some $q<1$.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Then: \item If there exists $\rho>0$ such that $\lim_{\gamma\to\infty} \comp(\cM)\cdot\gamma^{\rho}=0$, then there exists an algorithm \lim\_{T\to\infty}\frac{\MinimaxReg}{T^{p}}=0 \item If $\lim_{\gamma\to\infty}\comp(\cM)\cdot\gamma^{\rho}>0$ for all $\rho>0$, then any algorithm must have \lim\_{T\to\infty}\frac{\MinimaxReg}{T^{p}}=\infty \pref{thm:learnability\_main} shows that for any convex model class where the model estimation complexity $\MComp$ is sublinear, polynomial decay of the \CompText is sufficient to achieve sublinear regret. Conversely, if the \CompText does not decay polynomially, no algorithm can achieve sublinear regret.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We emphasize that the latter result (necessity of polynomial decay) applies to any model class, regardless of whether it admits low estimation complexity. Using results from follow-up work of, the assumption of convexity can be removed; see discussion in sec:main\_discussion.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Paper Body", "weight": 1.0} -->

It should be noted that learnability is---by definition---a coarse property, and is best thought of as a basic sanity check. As we show in \pref{sec:examples,sec:bandit,sec:rl}, our machinery is considerably more precise, and yields quantitative upper and lower bounds that accurately reflect problem-dependent parameters such as dimension.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Tighter Guarantees Based on Decision Space Complexity} \label{sec:main\_bayes} Up to this point, all of the upper bounds we have presented depend on the model estimation complexity $\MComp$. In general, low model estimation complexity is not required to achieve low regret for decision making. This is because our end goal is to make good \emph{decisions}, so we can give up on accurately estimating the model in regions of the decision space that do not help to distinguish the relative quality of decisions. Our final result for this section provides a tighter bound that replaces the model estimation complexity $\MComp$ with an analogous estimation complexity parameter for the decision space $\Pim$, albeit at the cost of removing the localization found in \pref{thm:upper\_main}. This result is non-constructive in nature, and is proven by using the minimax theorem to move to the Bayesian setting where the true model is drawn from a worst-case prior that is known to the learner (cf. \pref{sec:minimax\_swap}), then running \mainalg over a special model class constructed with knowledge of the prior.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We refer ahead to \pref{sec:dual} for more background on Our main upper bound---which applies to both finite and infinite classes---is stated in terms of the following, weaker notion of covering number, which is tailored to decision making. \begin{definition}[Decision space covering number] A decision set $\Act'\subseteq\Pim$ is an $\veps$-cover for $\Pim$ if \label{eq:action\_cover} \forall{}M\in\cM\quad\exists{}\act'\in\Act'\quad\text{s.t.}\quad \fm(\pim) - \fm(\act')\leq\veps.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We let $\cN(\Pim,\veps)$ denote the size of the smallest cover, and = \inf\_{\veps\geq{}0}\crl*{ \log\cN(\Pim,\veps) + \veps{}T}\label{eq:action\_complexity} as a fundamental complexity measure associated with $\Pim$. The result has the same structure as \pref{thm:upper\_main}, but replaces $\MComp$ with $\ActComp$.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Paper Body", "weight": 1.0} -->

There are some applications for which $\MComp$ correctly characterizes the precise minimax rate, but in general the estimation complexity for $\cM$ can be arbitrarily large relative to $\Pim$ (see \pref{sec:rl} for discussion in the context of reinforcement learning). On the other hand, for all of the applications we are aware of, $\ActComp$ has a smaller contribution to regret than the \CompText itself after balancing $\gamma$ (e.g., $\log{}A$ versus $A$ for the multi-armed bandit).

<!-- chunk {"id": "body-0137", "role": "body", "section": "Paper Body", "weight": 1.0} -->

As a result of \pref{thm:upper\_main\_bayes}, we obtain the following strengthening of \pref{thm:learnability\_main}.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{restatable}[Learnability---refined version]{theorem}{learnabilitymainbayes} \label{thm:learnability\_main\_bayes} Suppose that $\ActComp=\bigoht(T^{q})$ for some $q<1$, and that the conclusion of \pref{prop:minimax\_swap} holds, but place no assumption on $\MComp$. Then the conclusion of \pref{thm:learnability\_main} continues to hold.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Discussion and Subsequent Improvements} \label{sec:main\_discussion} We close by highlighting some gaps between our quantitative upper and lower bounds, and opportunities for improvement. We also discuss some gaps in our understanding of regret in the frequentist setting and Bayesian setting. Many of these issues are immaterial from the perspective of understanding learnability, but are important for understanding precise minimax rates. \subsubsection{When are the Upper and Lower Bounds Tight?} The lower and upper bounds from \pref{thm:lower\_main,thm:lower\_main\_expectation,thm:upper\_main} have a similar functional form, with the main differences involving localization, model estimation complexity, and convexity. In what follows, we discuss each of these gaps, highlight improvements obtained in follow-up work, and discuss further opportunities for improvement.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Paper Body", "weight": 1.0} -->

See sec:related for additional discussion of \paragraph{Localization and in-expectation lower bounds} Both \pref{thm:lower\_main} and \pref{thm:upper\_main} depend on the \CompText for the localized model class $\cMloc[\veps](\Mbar)$ rather than the full model class. The localization radius in the upper bound is larger than that of the lower bound, which can lead to looseness for some classes (see for an example).

<!-- chunk {"id": "body-0141", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The follow-up work of obtains matching upper and lower bounds that remove this issue by working with a ``constrained'' variant of the \CompShort.\footnote{Informally, the constrained DEC replaces the soft penalty term of $-\gamma \En_{\pi\sim p}\brk*{\Dhels{M(\pi)}{\Mbar(\pi)}}$ with a hard constraint of the form $\En\_{\pi\sim p}\brk*{\Dhels{M(\pi)}{\Mbar(\pi)}}\leq, the constrained DEC is equivalent to the form of the localized \CompShort appearing in thm:lower\_main under mild regularity conditions, indicating that this form of the \CompShort is fundamental, and thm:upper\_main can be tightened.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Next, let us discuss the connection between localization and in-expectation (versus in-probability) lower bounds. \pref{thm:lower\_main\_expectation} provides lower bounds based on the \CompShort for expected regret, but relies the $L_{\infty}$ notion of localization in \pref{eq:localized\_infinity}. While this notion suffices to derive the lower bounds in \pref{table:lower}, it is not difficult to construct examples where $L_{\infty}$-localization is too loose, where the lower bound cannot be achieved (in contrast to the weaker notion of localization in \pref{eq:localized}, which is achieved by \pref{alg:main}). The improvements obtained in lead to lower bounds that simultaneously obtain the favorable notion of localization in thm:lower\_main, yet hold in expectation.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Paper Body", "weight": 1.0} -->

More broadly, we do not yet fully understand what features of the class $\cM$ determine whether localization is needed to attain precise minimax rates. On one hand, it is not hard to construct examples for which localization can significantly improve regret, and hence is necessary for any lower bound. For example, if $\cM$ is large but there is a critical radius $\veps$ for which $\cMloc[\veps](\Mbar)=\crl{\Mbar}$, the regret bound in \pref{thm:upper\_general} (the general version of \pref{thm:upper\_main}) is constant. However, for all of the applications in bandits and reinforcement learning that we are aware of, localization seems to only lead to improvements in logarithmic factors. We refer interested readers to \pref{app:structural}, which shows that for certain ``reasonable'' model classes, the global and local \CompShort coincide up to constant factors. See for further (stylized) examples of classes in which localization is needed to attain tight rates.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Ignoring localization, the lower bounds in \pref{thm:lower\_main,thm:lower\_main\_expectation} scale with $\sup_{\Mbar\in\cM}\comp(\cM,\Mbar)$, while the upper bound in \pref{thm:upper\_main} scales $\sup_{\Mbar\in\conv(\cM)}\comp(\cM,\Mbar)$. That is, the upper bounds require evaluating the \CompShort with reference models in the convex hull of $\cM$, while the lower bounds do not. The follow-up work of strengthens our proof techniques to give lower bounds that scale with $\sup_{\Mbar\in\conv(\cM)}\comp(\cM,\Mbar)$, indicating that convexity for the reference model $\Mbar$ is fundamental.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Estimation error} The most notable distinction between our upper and lower bounds is the dependence on the complexity of estimation for $\cM$ ($\MComp$ for \pref{thm:upper\_main} and $\ActComp$ for \pref{thm:upper\_main\_bayes}). The correct dependence on the estimation complexity is a subtle issue which cannot be fully addressed without introducing additional complexity parameters. \item For the finite-armed bandit problem where $\Pim=\brk{A}$, we have $\ActComp=\log{}A$. As a result, \pref{thm:upper\_main\_bayes} gives an upper bound scaling with $\sqrt{AT\log{}A}$, while the lower bounds from \pref{thm:lower\_main,thm:lower\_main\_expectation} scale as $\sqrt{AT}$. In this case, the lower bound coincides with the minimax rate, and the upper bound can be improved by $\sqrt{\log{}A}$.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\item For linear bandits on the unit ball in $\bbR^{d}$, $\ActComp$ scales as $\bigoht(d)$. Here, \pref{thm:upper\_main\_bayes} gives regret $\bigoht(d\sqrt{T})$, while the lower bounds from \pref{thm:lower\_main,thm:lower\_main\_expectation} scale with $\sqrt{dT}$. In this case, the upper bound is tight, and the lower bound can be improved These observations highlight that fully resolving the correct dependence on estimation complexity requires additional problem complexity parameters. We leave this issue for future work, but we emphasize that for all the applications we are aware of, the decision space estimation complexity $\ActComp$ has a smaller contribution to regret than the \CompText itself (after balancing $\gamma$), and does not appear to be the deciding factor in whether a problem is learnable.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Finally, we mention in passing that the bound on the estimation complexity in \pref{thm:upper\_main\_infinite} depends on a rather coarse point-wise notion of model covering number, and it would be useful to improve this result to take advantage of refined (e.g., empirical or sequential) covering numbers; this is out of scope for the present work.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Other technical differences} \pref{thm:lower\_main} restricts to $\gamma>8e\sqrt{T}$, whereas \pref{thm:upper\_main} allows for any $\gamma>0$. This is essentially without loss of generality: Whenever $\compthmone\geq{}\gamma^{-1}$, which holds for any non-trivial class, the optimal choice for $\gamma$ satisfies $\gamma\geq{}\sqrt{T}$.\looseness=-1 \subsubsection{Regret Bounds: Frequentist vs. Bayesian and \label{sec:bayesian} Our localized upper bounds, \pref{thm:upper\_main} and \pref{thm:upper\_main\_infinite}, are proven directly in the \FrameworkShort framework described in \pref{sec:intro} (the ``frequentist'' \pref{alg:main} with a particular choice of estimation oracle.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\pref{thm:upper\_main\_bayes}, which replaces the model estimation complexity $\MComp$ with the decision space estimation complexity $\ActComp$, is proven non-constructively by exhibiting an upper bound on regret in the Bayesian setting (cf. \pref{sec:minimax\_swap}). Informally, working in the Bayesian setting is a powerful tool, because it allows one to ``average out'' models that agree on the optimal action, thereby reducing the estimation complexity. Follow-up work of provides a frequentist algorithm which achieves the same guarantee by exploiting a constructive analogue of this principle. See \pref{sec:related} for further An interesting question that remains is whether one can achieve the dependence on $\cN(\Pim,\veps)$ in \pref{thm:upper\_main\_bayes} and the localization in \pref{thm:upper\_main\_infinite} simultaneously.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{The \mainalgsection Meta-Algorithm: General Toolkit} \label{sec:algorithm} In this section we provide a general toolkit for deriving regret bounds and efficient algorithms using \mainalg meta-algorithm (\pref{alg:main}). We begin with a regret bound for \mainalg with generic online estimation oracles (\pref{sec:oracle}), then provide a dual Bayesian view of the \CompText and \mainalg algorithm (\pref{sec:dual}), and finally close with some simple extensions (\pref{sec:general\_distance}).

<!-- chunk {"id": "body-0151", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Guarantees for General Online Estimation Oracles} \label{sec:oracle} The \mainalg meta-algorithm can be applied with any user-specified estimation oracle $\AlgEst$. For general oracles, the decision making performance of \mainalg depends on the estimation performance of the oracle, which we measure via cumulative Hellinger error: \label{eq:hellinger\_error} \EstHel \ldef{} \sum\_{t=1}^{T}\En\_{\act\ind{t}\sim{}p\ind{t}}\brk*{\DhelsX{\Big}{\Mstar(\act\ind{t})}{\Mhat\ind{t}(\act\ind{t})}}. Our most general theorem shows that for any choice of oracle, \mainalg inherits the Hellinger estimation error as a bound on decision making regret, thereby bridging estimation and decision making.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To state the result, we define $\cMhat\ind{t}$ as any set such that $\Mhat\ind{t}\in\cMhat\ind{t}$ almost surely for all $t$, and define $\cMhat=\cup_{t\geq{}1}\cMhat\ind{t}$. To provide high probability guarantees, we make the following \label{ass:hellinger\_oracle} The estimation oracle $\AlgEst$ guarantees for any $T\in\bbN$ and $\delta\in$, with probability at least $1-\delta$, $\EstHel\leq{}\EstProbHel$, where $\EstProbHel$ is a known upper bound.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For example, as we show in the sequel, whenever $\cM$ is finite, Vovk's aggregating algorithm ensures that $\En\brk*{\EstHel}\leq{}\log\abs{\cM}$, and satisfies \pref{ass:hellinger\_oracle} with $\EstProbHel=2\log(\abs{\cM}/\delta)$.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{thm:upper\_general} \pref{alg:main} with \optionone and exploration parameter $\gamma>0$ guarantees \label{eq:upper\_general1} \sup\_{\Mbar\in\cMhat}\comp(\cM,\Mbar)\cdot{}T + \gamma\cdot\EstHel almost surely. Furthermore, when \pref{ass:hellinger\_oracle} holds, \pref{alg:main} with \optionone guarantees that for any $\delta\in$, with probability at least $1-\delta$, \label{eq:upper\_general2} \sup\_{\Mbar\in\cMhat}\comp(\cM,\Mbar)\cdot{}T + \gamma\cdot\EstProbHel. Finally, fix $\delta\in$ and consider \pref{alg:main} with \optiontwo and $R^{2}=\EstProbHel$.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Suppose that $\AlgEst$ has $\cMhat\ind{t}\subseteq\conv(\cM\ind{t})$ for all $t$, and that $\Rspace\subseteq\brk*{0,1}$.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Then for any fixed $T\in\bbN$ and $\gamma>0$, with probability at least $1-\delta$, \sum\_{t=1}^{T}\sup\_{\Mbar\in\conv(\cM)}\comp(\cMloc[\veps\_t](\Mbar),\Mbar) + \gamma\cdot{}\EstProbHel, \label{eq:upper\_general3} where $\veps_t\ldef{}6\frac{\gamma}{t}\EstProbHel + \sup_{\Mbar\in\conv(\cM)}\comp(\cM,\Mbar) The guarantees in \pref{eq:upper_general1} and \pref{eq:upper_general2} concern the simpler variant of \mainalg (\optionone), which is more practical to implement but does not achieve localization.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Paper Body", "weight": 1.0} -->

When invoked with Vovk's aggregating algorithm as described above, the regret for \optionone scales as roughly $\min\_{\gamma>0}\max\crl*{ \sup\_{\Mbar\in\cMhat}\comp(\cM,\Mbar)\cdot{}T,\; \gamma\cdot\log\abs{\cM}}$, which matches \pref{thm:upper_main} modulo localization. The guarantee in \pref{eq:upper_general3} concerns \optiontwo, and constitutes our most general regret guarantee bound on the localized \CompText.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Paper Body", "weight": 1.0} -->

When invoked with a variant of the aggregating algorithm designed to satisfy the requisite condition that $\cMhat\ind{t}\subseteq\conv(\cM\ind{t})$ (\pref{app:online}), this result recovers \pref{thm:upper_main} as a special \begin{remark}[Inexact minimizers] All of the results regarding \mainalg (\pref{alg:main}) are stated for the case where $p\ind{t}$ is chosen to exactly solve the minimax problem \argmin_{p\in\Delta(\Act)}\sup_{M\in\cM\ind{t}} \gameval{\Mhat\ind{t}}(p, M), for a model class $\cM\ind{t}$ and estimator $\Mhat\ind{t}$. This leads to regret bounds that scale with $\comp(\cM\ind{t},\Mhat\ind{t})$.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Paper Body", "weight": 1.0} -->

If we instead use a distribution $p\ind{t}$ that \emph{certifies an upper bound on the \CompShort} in the sense that \sup_{M\in\cM\ind{t}} \gameval{\Mhat\ind{t}}(p\ind{t}, M) \leq{} g_{\gamma}(\cM\ind{t},\Mhat\ind{t}) for some function $g_{\gamma}(\cdot,\cdot)$, then all of the main theorems (\pref{thm:upper_main,thm:upper_main_infinite,thm:upper_main_bayes,thm:upper_general,prop:bayes_basic,thm:upper_general_distance}) continue to hold, with occurrences of $\comp(\cM,\Mbar)$ replaced by $g_{\gamma}(\cM,\Mbar)$. We tacitly use this fact in later sections.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Online Estimation Oracles: Density Estimation and Examples} A topic we have not yet addressed is how to go about minimizing the Hellinger estimation error in \pref{eq:hellinger\_error}. Building on classical literature in statistical estimation, we show that this problem can generically be solved via \emph{online density estimation}.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For each example $(\act\ind{t}, r\ind{t}, \obs\ind{t})$, define the logarithmic loss for a model $M$ as\looseness=-1 \label{eq:log\_loss} \logloss\ind{t}(M) = \log\prn*{ \frac{1}{\densm(r\ind{t}, \obs\ind{t}\mid{}\act\ind{t})} where we recall that $\densm(\cdot,\cdot\mid{}\act)$ is the conditional density for $(r,\obs)$ under $M$ (cf. \pref{sec:prelims}).

<!-- chunk {"id": "body-0162", "role": "body", "section": "Paper Body", "weight": 1.0} -->

As an intermediate quantity, we consider regret under the logarithmic loss: \label{eq:log\_loss\_regret} = \sum\_{t=1}^{T}\logloss\ind{t}(\Mhat\ind{t}) - \inf\_{M\in\cM}\sum\_{t=1}^{T}\logloss\ind{t}(M). Regret minimization with the logarithmic loss (also known as \emph{sequential probability assignment}) is a fundamental problem in online learning. Efficient algorithms are known for model classes of interest and this is complemented by theory which provides minimax rates for generic model classes.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Canonical examples include finite classes, where Vovk's aggregating algorithm guarantees $\RegLog\leq\log\abs{\cM}$ for every sequence,\footnote{See \pref{app:online} for detailed guarantees.} and linear models (i.e., $M(r,o\mid{}\act)=\tri*{\phi(r,o,\act),\theta}$ for a fixed feature map in $\phi\in\bbR^{d}$), where algorithms with $\RegLog=\bigoh(d\log(T))$ are known algorithms satisfy $\cMhat=\conv(\cM)$.\footnote{In fact, even for improper estimators that do not satisfy $\cMhat=\conv(\cM)$, it is always possible to project $\Mhat\ind{t}$ onto $\conv(\cM)$ while maintaining the estimator's bound on $\En\brk{\EstHel}$.} We refer the reader to Chapter 9 of for further examples and The following result shows that

<!-- chunk {"id": "body-0164", "role": "body", "section": "Paper Body", "weight": 1.0} -->

a bound on the log-loss regret immediately yields a bound on the Hellinger estimation error.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Paper Body", "weight": 1.0} -->

% \label{prop:log\_loss\_hellinger} For any estimation algorithm $\AlgEst$, whenever \pref{ass:realizability} holds, \En\brk*{\EstHel} \leq{} \En\brk*{\RegLog}. Furthermore, for any $\delta\in$, with probability at least $1-\delta$, \EstHel \leq{} \RegLog + 2\log(\delta^{-1}). For a proof, refer to \pref{lem:logloss\_hellinger\_ol} in \pref{app:technical}, which gives a more general version of this result. Further examples of estimation oracles are given throughout \pref{sec:examples,sec:bandit,sec:rl}.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Dual Perspective and Connection to Posterior Sampling} \label{sec:dual} The \CompText \pref{eq:comp} is a min-max optimization problem, and can be interpreted as a game in which the learner (the ``min'' player) aims to find a decision distribution $p$ that optimally trades off regret and information acquisition in the face of an adversary (the ``max'' player) that selects a worst-case model in $\cM$.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We can define a natural \emph{dual} (or, max-min) analogue of the \CompShort via \label{eq:comp\_dual} \sup\_{\mu\in\Delta(\cM)}\inf\_{p\in\Delta(\Act)}\En\_{M\sim\mu}\En\_{\act\sim{}p}\biggl[\fm(\pim)-\fm(\pi) -\gamma\cdot\Dhels{M(\act)}{\Mbar(\act)} The dual \CompText has the following Bayesian interpretation. The adversary selects a \emph{prior} distribution $\mu$ over models in $\cM$, and the learner (with knowledge of the prior) finds a decision distribution $p$ that balances the tradeoff between regret and information acquisition when the underlying model is drawn from The connection between the primal and dual \CompShort is analogous to the connection between primal and dual regret (cf. \pref{sec:minimax\_swap}).

<!-- chunk {"id": "body-0168", "role": "body", "section": "Paper Body", "weight": 1.0} -->

As with regret, the primal and dual \CompShort can be shown to coincide under mild regularity conditions.\footnote{As with \pref{prop:minimax\_swap}, we expect that this result can be proven to hold under weaker conditions.} \begin{restatable}{proposition}{minimaxswapdec} \label{prop:minimax\_swap\_dec} Suppose that $\Act$ is finite and $\Rspace$ is bounded. Then for all \label{eq:minimax\_swap\_dec} \comp(\cM,\Mbar) = \compb(\cM,\Mbar). As a consequence, any bound on the dual \CompShort immediately yields a bound on the primal \CompShort. This perspective is useful because it allows us to bring existing tools for Bayesian bandits and reinforcement learning to bear on the primal \CompText.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For example, \emph{probability matching} is a well-known Bayesian strategy that---when applied to our setting---uses the distribution $p$ induced by sampling $M\sim\mu$ and selecting $\act_{\sss{M}}$. Using analysis, one can show that this strategy certifies \compb(\cM,\Mbar) \leq{} \frac{\abs{\Act}}{4\gamma} for the finite-armed bandit; see \pref{sec:examples} for a proof. Using more sophisticated analysis techniques, we use this approach to bound the \CompText for a general class of structured bandit problems with bounded \emph{star number} in \pref{sec:bandit}, and provide bounds for reinforcement learning in \pref{sec:rl}. In fact, many prior results for the Bayesian setting can be viewed as implicitly providing bounds on the dual \CompText cf. \pref{sec:related}.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider the Bayesian version of the \FrameworkShort framework from \pref{sec:minimax\_swap}, in which the underlying model $\Mstar$ is drawn from a known prior $\mu\in\Delta(\cM)$, and our objective is to minimize the Bayesian regret \En\_{\Mstar\sim\mu}\En\sups{\Mstar}\brk*{\RegDM}. For this setting, the celebrated \emph{posterior sampling} (or, Thompson applies the probability matching idea as follows. At each round $t$, we first compute the conditional law for $\Mstar$ given the observed history $\hist\ind{t-1}$, which we denote by $\mu\ind{t} = \mu\ind{t}(\cdot\mid{}\hist\ind{t-1})$. We then sample $M\sim{}\mu\ind{t}$ and play $\act\ind{t}=\pim$.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This algorithm leads to Bayesian regret bounds for basic problem settings such as finite-armed bandits, linear bandits, and tabular We provide a Bayesian analogue of the \mainalg algorithm (\pref{alg:bayes\_basic}), which may be viewed as a generalization of posterior sampling.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Paper Body", "weight": 1.0} -->

At each round, the algorithm computes an induced model $\Mbar\ind{t}(\act)=\En\brk*{\Mstar(\act)\mid\hist\ind{t-1}}$, and a distribution $\mu\ind{t}\in\Delta(\cM)$ which may be viewed as a coarsened version of the posterior distribution, then solves the optimization problem \argmin\_{p\in\Delta(\Act)}\En\_{M\sim\mu\ind{t}}\En\_{\act\sim{}p}\brk*{\fm(\pim)-\fm(\pi) -\gamma\cdot\Dhels{M(\act)}{\Mbar\ind{t}(\act)}}. \label{eq:bayes\_argmin} The algorithm then samples the decision $\act\ind{t}$ from the resulting distribution.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Paper Body", "weight": 1.0} -->

It is straightforward to show that this algorithm has the following guarantee, which specializes \pref{thm:upper\_main\_bayes}.\footnote{The proof of \pref{thm:upper\_main\_bayes} (see Eq. \pref{eq:upper\_main\_bayes\_quant}) extends this result to infinite classes, and is proven in \pref{app:upper\_main\_bayes}.} \begin{restatable}{theorem}{bayesbasic} \label{prop:bayes\_basic} For parameter $\gamma>0$, \pref{alg:bayes\_basic} guarantees that \label{eq:bayes\_basic} \En\_{\Mstar\sim\mu}\En\sups{\Mstar}\brk*{\RegDM} \leq{} \sup\_{\Mbar\in\conv(\cM)}\compb(\conv(\cM),\Mbar)\cdot{}T

<!-- chunk {"id": "body-0174", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This algorithm generalizes posterior sampling by replacing the naive probability matching strategy with the optimization problem in \pref{eq:bayes\_argmin}. It is also closely related to the \emph{information-directed sampling} algorithm of. However, \pref{alg:bayes\_basic} can be applied in settings where information directed-sampling fails. See sec:related for further discussion of connections to posterior sampling.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{General Divergences and Randomized Estimators} \label{sec:general\_distance} \State \textbf{parameters}: \Statex Online estimation oracle $\AlgEst$. \Statex Exploration parameter $\gamma>0$. \Statex Divergence $\Dgen{\cdot}{\cdot}$. \State Compute randomized estimate $\nu\ind{t} = \AlgEst\ind{t}\prn[\Big]{ \crl*{(\act\ind{i}, r\ind{i},\obs\ind{i})}_{i=1}^{t-1} }$.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\caption{\mainalg for General Divergences and Randomized Estimators} \label{alg:main\_generalized} In this section we give a generalization of the \mainalg algorithm that incorporates two extra features: \emph{general divergences} and \emph{randomized estimators}.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{General divergences} The \CompText measures estimation error via the Hellinger distance $\Dhels{M(\act)}{\Mbar(\act)}$. By providing a characterization for learnability (\pref{sec:learnability}), we show that the choice of Hellinger distance here is fundamental. Nonetheless, for specific applications and model classes, it can be useful to work with alternative distance measures and divergences.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For a general divergence $D:\conv(\cM)\times\conv(\cM)\to\bbR_{+}$, \label{eq:comp\_general} \inf\_{p\in\Delta(\Act)}\sup\_{M\in\cM}\En\_{\act\sim{}p}\biggl[\fm(\pim)-\fm(\pi) -\gamma\cdot\Dgen{M(\act)}{\Mbar(\act)} This variant of the \CompShort naturally leads to regret bounds in \paragraph{Randomized estimators} The basic version of \mainalg (\pref{alg:main}) assumes that at each round, the estimation algorithm $\AlgEst$ provides a point estimate $\Mhat\ind{t}$. In some settings, it useful to consider \emph{randomized estimators} that, at each round, produce a distribution $\nu\ind{t}$ over models.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For this setting, we further generalize the \CompShort by defining \label{eq:comp\_general\_randomized} \inf\_{p\in\Delta(\Act)}\sup\_{M\in\cM}\En\_{\act\sim{}p}\biggl[\fm(\pim)-\fm(\pi) -\gamma\cdot\En\_{\Mbar\sim\nu}\brk*{\Dgen{M(\act)}{\Mbar(\act)}} for distributions $\nu\in\Delta(\cM)$. A generalization of \mainalg that incorporates general divergences and randomized estimators is given in \pref{alg:main\_generalized}.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The algorithm is identical to \mainalg with \optionone, with the only differences being that i) we play the distribution that solves the minimax problem \pref{eq:comp\_general\_randomized} with the user-specified divergence $\Dgen{\cdot}{\cdot}$ rather than squared Hellinger distance, and ii) we use the randomized estimate $\nu\ind{t}$ rather than a point estimate.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our performance guarantee for this algorithm depends on the estimation performance of the oracle's randomized estimates $\nu\ind{1},\ldots,\nu\ind{T}$ with respect to the given divergence $D$, which we define as \label{eq:general\_error} \EstD \ldef{} \sum\_{t=1}^{T}\En\_{\act\ind{t}\sim{}p\ind{t}}\En\_{\Mhat\ind{t}\sim\nu\ind{t}}\brk*{\Dgen{\Mstar(\act\ind{t})}{\Mhat\ind{t}(\act\ind{t})}}. Let $\cMhat$ be any set for which $\Mhat\ind{t}\in\cMhat$ for all $t$ almost surely. We have the following guarantee.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{restatable}{theorem}{uppergeneraldistance} \label{thm:upper\_general\_distance} \pref{alg:main\_generalized} with exploration parameter $\gamma>0$ guarantees \label{eq:upper\_general\_distance} \sup\_{\nu\in\Delta(\cMhat)}\compgen(\cM,\nu)\cdot{}T + \gamma\cdot\EstD \paragraph{On the use of general divergences} In bandit problems, it is often convenient to work with the $\Dsq{M(\act)}{\Mbar(\act)}\ldef{}(\fm(\act)-\fmbar(\act))^2$, which uses the mean reward function as a sufficient statistic. With this choice of distance, the minimax problem in \pref{eq:comp\_general} recovers the action selection strategy used in the \squarecb contextual bandit algorithm.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This distance also recovers a generalization of \squarecb for infinite, linearly-structured action spaces given. Note that whenever $\cFm$ has range in $\brk*{0,1}$, one has $\compH(\cM,\Mbar)\leq{}\compSq(\cM,\Mbar)$,\footnote{Throughout the paper we abbreviate $\compH=\compgen[\Dhelshort]$, $\compKL=\compgen[\Dklshort]$, $\compSq=\compgen[\Dsqshort]$, and so.} and in general this inequality is strict, so working with this distance is not always sufficient. The advantage, however, is that for $\Dsqshort$ the estimation error in \pref{eq:general\_error} can be minimized directly using square loss estimation rather than density estimation, which can lead to simpler algorithms and tighter bounds.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For example, one can generically obtain $\EstSq\leq{}\log\abs{\cFm}$ for finite classes, which can be much tighter than the analogous bound $\EstHel\leq{}\log\abs{\cM}$ for Hellinger error. See for more background on square loss estimation oracles.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Another advantage of working with general distances is to simplify analysis of the minimax value. For example, some of our lower bounds on the \CompShort proceed by moving to KL divergence and lower $\compH(\cM,\Mbar)\geq\compKL(\cM,\Mbar)$.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We mention without proof that it is also possible to extend \optiontwo of \mainalg to accommodate general divergences. In this case, we require the additional assumption that the divergence $D$ is bounded, symmetric, and satisfies the triangle inequality up to a multiplicative constant.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{On the use of randomization} Subsequent work of shows that for Hellinger distance and other divergences satisfying mild technical assumptions, the randomized variant of the \CompShort in eq:comp\_general\_randomized is equal to $\sup_{\Mbar\in\conv(\cM)}\compgen(\cM,\Mbar)$ up to constants. We restate the result here. \label{lem:randomization\_doesnt\_help} For all reference models $\Mbar$ (not necessarily in $\cM$), we have that for all $\gamma>0$, \leq{} \sup\_{\nu\in\Delta(\cM)}\comp[\gamma/4]^{\mathrm{H}}(\cM,\nu).

<!-- chunk {"id": "body-0188", "role": "body", "section": "Paper Body", "weight": 1.0} -->

While working with randomization offers no improvement in statistically, in some cases a distribution $p\in\Delta(\Pi)$ that minimizes $\compgen(\cM,\nu)$ can be simpler to compute than a distribution that minimizes $\compgen(\cM,\Mbar)$ for $\Mbar\in\conv(\cM)$. We refer to the follow-up work of for concrete examples of randomized estimators.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Illustrative Examples} \label{sec:examples} In this section, we show how to bound the \CompText and efficiently instantiate the \mainalg meta-algorithm for two canonical problem settings: multi-armed bandits and tabular (finite state/action) reinforcement learning. Through the duality introduced in \pref{sec:dual}, we showcase the use of both frequentist and Bayesian approaches to bound the DEC. The proofs in this section illustrate key concepts and technical tools that prove useful when we consider richer, more structured settings in \pref{sec:bandit} and \pref{sec:rl}.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Multi-Armed Bandits} For the first example, we provide upper and lower bounds on the \CompText for the classical multi-armed bandit setting. Here, we have $\Act=\brk*{A}$, $\Rspace=\brk*{0,1}$, and $\Obs=\NullObs$, and the model class $\cM=\crl*{M:M(\act)\in\Delta(\Rspace)}$ consists of all possible distributions over $\Rspace$.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To derive upper bounds, it is simpler to work with the square loss variant of the \CompShort from \pref{sec:general\_distance}, \inf\_{p\in\Delta(\Pi)}\sup\_{M\in\cM}\En\_{\act\sim{}p}\brk*{\fm(\pim)-\fm(\pi) -\gamma\cdot(\fm(\act)-\fmbar(\act))^2}, which has $\comp(\cM,\Mbar)\leq\compSq(\cM,\Mbar)$ whenever rewards lie in $\brk*{0,1}$. Intuitively, the reason why working with this coarse notion of distance suffices is that---beyond the mean reward for each decision---the noise distribution provides little information about the underlying problem instance for this unstructured setting.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Regret upper bound} By plugging the bound on the \CompText from \pref{prop:posterior\_mab} into \pref{thm:upper\_main\_bayes} (and noting that $\conv(\cM)=\cM$), we conclude existence of an \leq{} 2\cdot\min\_{\gamma>0}\max\crl*{\frac{AT}{\gamma}, \gamma\log{}A} = 4\sqrt{AT\log{}A}.\label{eq:posterior\_mab} This matches the optimal rate for the multi-armed bandit problem up to the $\log{}A$ factor \pref{alg:bayes\_basic}, this approach provides an explicit algorithm for the Bayesian setting. \subsubsection{Frequentist Upper Bound via Inverse Gap Weighting} The Bayesian approach in the prequel does not lead to an explicit strategy that achieves the value of the frequentist \CompText.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We now give an explicit approach based on the \emph{inverse gap weighting} \label{prop:igw\_mab} Consider the multi-armed bandit setting with $\cR=\bbR$.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Conceptually, this result shows that \igwtext can be thought of as a frequentist counterpart to posterior sampling. \begin{proof}[\pfref{prop:igw\_mab}] Let $M\in\cM$ be fixed.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Regret upper bound} Applying \pref{thm:upper\_general\_distance} with the bound on the \CompShort above, we conclude that \mainalg with \igwtext ensures that for any \RegDM \leq{} \frac{AT}{\gamma} + \gamma\cdot\EstSq, \EstSq = \sum\_{t=1}^{T}\En\_{\act\ind{t}\sim{}p\ind{t}}\brk*{(\fmhatt(\act\ind{t})-\fmstar(\act\ind{t}))^2}. As a concrete example, following, we can estimate the rewards using the $\En\brk{\EstSq}\leq{}A\log(T)$. The resulting algorithm has $\En\brk*{\RegDM}\leq{}A\sqrt{T\log(T)}$, and runs in time $\bigoh(A)$ per round.

<!-- chunk {"id": "body-0196", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We mention in passing that with a more careful analysis, this approach can recover the $\sqrt{AT\log{}A}$ rate \pref{eq:posterior\_mab} derived through the Bayesian approach, but we do not pursue this here. \subsubsection{Lower Bound} We conclude this example by proving a lower bound on the \CompText which matches the upper bounds derived above. We use this example to illustrate a general strategy to lower bound the \CompShort, which is used extensively throughout \pref{sec:bandit,sec:rl}. The lower bound strategy is based on the following notion of a \emph{hard family of models}. \begin{definition}[\hardfamily] A reference model $\Mbar\in\cM$ and collection $\crl*{M_1,\ldots,M_N}$ with $N\geq{}2$ are said to be an \hardfamily if the following properties hold.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Informally, any \hardfamily leads to a difficult decision making problem when $N$ is large because a given action can have low regret or large information gain on at most one model in the family. The following lemma makes this idea precise. \label{lem:hard\_family} Let $\cM'=\crl*{M_1,\ldots,M_N}\subseteq\cM$ be an \hardfamily with respect to $\Mbar$. Then for all $\gamma>0$ \label{eq:hard\_family} \comp(\cM',\Mbar) \geq \compb(\cM',\Mbar) \geq \frac{\alpha}{2} - \gamma\prn*{\frac{\beta}{N}+\delta}. Choose $\mu=\unif(\crl{M_1,\ldots,M_N})$ as the uniform distribution over models in the family.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Paper Body", "weight": 1.0} -->

By choosing $\Delta=\frac{A}{12\gamma}$, this gives \geq{} ^{-1}\frac{A}{\gamma}. it is clear that $\cM'\subseteq\cMinf[\Delta](\Mbar)$, and that $\abscontp=\bigoh$ in \pref{thm:lower\_main,thm:lower\_main\_expectation} whenever $\Delta\leq1/4$; it suffices to restrict to $\gamma\geq{}A/3$.

<!-- chunk {"id": "body-0199", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Regret lower bound} Applying \pref{thm:lower\_main\_expectation} with the lower bound on the \CompShort from \pref{prop:mab\_lower}, we are guaranteed that\footnote{Recall that the sub-family of models constructed in \pref{prop:mab\_lower} $\abscontp=\bigoh$ for \pref{thm:lower\_main\_expectation}.} \geq{} c'\cdot{}\frac{AT}{\gamma}, so long as $\frac{A}{12\gamma}\leq\vepslowg=c''\frac{\gamma}{T}$, where $c,c',c''>0$ are numerical constants.

<!-- chunk {"id": "body-0200", "role": "body", "section": "Paper Body", "weight": 1.0} -->

If we choose $\gamma=C\cdot\sqrt{AT}$ for $C>0$ sufficiently large, we have \En\brk*{\RegDM} \geq{} \Omega(\sqrt{AT}), which matches the minimax rate for the problem Note that compared to specialized approaches tailored to the multi-armed bandit setting, the constants in this lower bound are rather loose. This is a consequence of the high generality of our framework.

<!-- chunk {"id": "body-0201", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Tabular Reinforcement Learning} \label{sec:tabular} As our second example, we show how to bound the \CompText and develop efficient algorithms for reinforcement learning in the tabular (or, finite state/action) setting. Here, $\cM$ is the collection of all non-stationary MDPs with state space $\cS=\brk{S}$, action space $\cA=\brk{A}$, and horizon $H$, and $\Act=\PiRNS$ is the collection of all randomized, non-stationary Markov policies (cf. \pref{ex:rl}). We assume that rewards are normalized such that $\sum_{h=1}^{H}r_h\in\brk*{0,1}$ almost surely, and take $\cR=\brk*{0,1}$.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The bound on the \CompText from \pref{prop:posterior\_tabular}, which scales with $\frac{H^{2}SA}{\gamma}$, is optimal in terms of dependence on $S$ and $A$, as we show below. The dependence on horizon can be improved from $H^{2}$ to $H$ for MDPs with time-homogeneous In \pref{sec:rl}, we generalize the decoupling idea used in this proof to MDPs with low Bellman rank and, more generally, any \emph{bilinear class}. Indeed, the only property of the tabular RL setting that is essential to the proof above is that the Bellman residuals have \subsubsection{Frequentist Upper Bound via Policy Cover Inverse Gap Weighting} \newcommand{\PiCov}{\Psi} \begin{algorithm}[htp] \State \textbf{parameters}: \Statex Estimated model $\Mbar\in\cM$. \Statex Exploration parameter $\eta>0$.

<!-- chunk {"id": "body-0203", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\State \textbf{return} $p$. \caption{Policy Cover Inverse Gap Weighting (\pcigw)} \label{alg:policy\_cover\_igw} We now provide an explicit, efficiently computable strategy which bounds the frequentist \CompText for tabular reinforcement learning. The strategy, which we call \emph{Policy Cover Inverse Gap Weighting}, is displayed in \pref{alg:policy\_cover\_igw}. As the name suggests, our approach combines the inverse gap weighting technique introduced in the multi-armed bandit setting with the notion of a \emph{policy cover}---that is, a collection of policies that ensures good coverage on every state.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\pref{alg:policy\_cover\_igw} consists of two steps. First, in \pref{eq:pc\_igw1}, we compute the collection of policies $\PiCov=\crl{\pi_{h,s,a}}_{h\in\brk{H},s\in\brk{S},a\in\brk{A}}$ that constitutes a policy cover for the estimated model $\Mbar\in\cM$. In prior work, this is accomplished by computing the policy $\pihsa=\argmax_{\pi\in\PiRNS}\dm{\Mbar}{\pi}_h(s,a)$ that maximizes the occupancy measure for $\Mbar$ for each $(h,s,a)$ tuple.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The main twist here is that we instead consider the policy \argmax\_{\pi\in\PiRNS}\frac{\dm{\Mbar}{\pi}\_h(s,a)}{2HSA + \eta(\fmbar(\pimbar)-\fmbar(\pi))} that maximizes the ratio of the occupancy measure and the regret gap under $\Mbar$. This \emph{inverse gap weighted policy cover} balances exploration and exploration by trading off coverage with suboptimality, and is critical to deriving a tight bound on the \CompShort that leads to $\sqrt{T}$-regret.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Paper Body", "weight": 1.0} -->

With the policy cover in hand, the second step of \pref{alg:policy\_cover\_igw} computes the exploratory distribution $p$ by simply applying inverse gap weighting to the elements of the cover and the greedy policy $\pimbar$.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The following result---proven in \pref{app:examples}---shows that the \pcigw strategy can be implemented efficiently. Briefly, the idea is to solve \pref{eq:pc\_igw1} by taking a dual approach and optimizing over occupancy measures rather than policies. With this parameterization, \pref{eq:pc\_igw1} becomes a linear-fractional program, which can then be transformed into a standard linear program using classical techniques. \begin{restatable}{proposition}{efficienttabular} \label{prop:efficient\_tabular} The \pcigw algorithm (\pref{alg:policy\_cover\_igw}) can be implemented in $\poly(H,S,A,\log(\eta))$ time via linear programming.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our bound on the \CompText for the \pcigw algorithm is as follows.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This result shows for the first time how to leverage the inverse gap weighting technique for provable exploration in reinforcement learning. In \pref{sec:rl}, we show to extend this approach to any family of MDPs with \emph{bilinear class} The proof of \pref{prop:igw\_tabular} follows the structure of the proof of \pref{prop:posterior\_tabular} closely; the main difference is that the decoupling step is replaced by an argument based on the inverse gap weighted policy cover in \pref{eq:pc\_igw1}.

<!-- chunk {"id": "body-0210", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proof}[\pfref{prop:igw\_tabular}]% \newcommand{\allpolicies}{\PiCov\cup\crl{\pimbar}}% \newcommand{\etaalt}{\eta'}% We first verify that the strategy in \pref{eq:pc\_igw2} is indeed well-defined, in the sense that a normalizing constant $\lambda\in[1, 2HSA]$ always exists. There is a unique choice for $\lambda>0$ such that $\sum_{\pi}p(\pi)=1$, and its value lies in $[1,2HSA]$. Let $f(\lambda)=\sum_{\pi}\frac{1}{\lambda + \eta(\fmbar(\pimbar)-\fmbar(\pi))}$.

<!-- chunk {"id": "body-0211", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We first observe that if $\lambda>2HSA$, then $f(\lambda)\leq{}\sum_{\pi}\frac{1}{\lambda}=\frac{HSA+1}{\lambda}<1.$ On the other hand for $\lambda\in$, $f(\lambda)\geq{}\frac{1}{\lambda + \eta(\fmbar(\pimbar)-\fmbar(\pimbar))} Hence, since $f(\lambda)$ is continuous and strictly decreasing over $(0,\infty)$, there exists a unique $\lambda^{\star}\in[1, 2HSA]$ such that $f(\lambda^{\star})=1$.

<!-- chunk {"id": "body-0212", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Regret Upper Bound} Using an approach in \pref{sec:rl\_bilinear\_estimation}, we can obtain an efficient online estimation algorithm for tabular MDPs which guarantees that \dfedit{$\Mhat\ind{t}\in\cM$} and \sum\_{t=1}^{T}\En\_{\act\ind{t}\sim{}p\ind{t}}\brk*{\Dhels{\Mstar(\act\ind{t})}{\Mhat\ind{t}(\act\ind{t})}} Combining this with the \pcigw strategy (\pref{prop:igw\_tabular}) and \mainalg (\pref{thm:upper\_general}), we obtain an efficient algorithm with \RegDM \leq \bigoht(\sqrt{H^{4}S^{3}A^2T}).

<!-- chunk {"id": "body-0213", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Regret bounds for tabular reinforcement learning have received extensive investigation, but this result is exciting because it represents a completely new algorithmic approach. In particular, this is the first frequentist reinforcement learning algorithm we are aware of that does not make use of confidence sets or Note that while this bound scales as $\sqrt{\poly(S,A,H)T}$ as desired, it does fall short of the minimax rate, which is $\sqrt{HSAT}$ for our setting (since we consider $\sum_{h=1}^{H}r_h\in\brk{0,1}$ and time-inhomogeneous dynamics). We emphasize that obtaining the tightest possible dependence on problem parameters is not the focus of this work, but it would be interesting to improve this approach to match the \subsubsection{Lower Bound} We close the tabular reinforcement learning example by complementing our upper bounds with a lower bound on the \CompText.

<!-- chunk {"id": "body-0214", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{prop:lower\_tabular} Let $\cM$ be the class of tabular MDPs with $S\geq{}2$ states, $A\geq{}2$ actions, and $\sum_{h=1}^{H}r_h\in\cR\ldef\brk*{0,1}$. If $H\geq{}2\log_2(S/2)$, then there exists $\Mbar\in\cM$ such that for all $\gamma\geq{}HSA/24$, \comp(\cMinf[\vepsg](\Mbar),\Mbar) \geq{} 2^{-9}\cdot\frac{HSA}{\gamma}, where $\vepsg=\frac{HSA}{96\gamma}$. As with the multi-armed bandit example, the proof of this result proceeds by constructing a hard family of models and appealing to \pref{lem:hard\_family}.

<!-- chunk {"id": "body-0215", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\newcommand{\wait}{\mathsf{wait}}% Assume without loss of generality that $S$ is a multiple of $2$.

<!-- chunk {"id": "body-0216", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Let $\Delta\in(0,1/2)$ be a parameter. We consider the following class of \item Define $H_1\ldef\log_2(S/2)$ and $H_2=H-H_1$. \item Let $S'\ldef{}S/2$. The state space $\cS$ is chosen to consist of a depth-$H_1$ binary tree (which has $S'$ leaves and $\sum_{i=0}^{\log_2(S/2)}2^{i}=S-1$ total states), along with a single terminal state $\term$. We let $\cS'$ denote the collection of leaf states. \item All MDPs $M$ in the family have the same (deterministic) dynamics $\Pm=P$. The agent begins at the root state in the tree, and for each $h < H_1$, there are two available actions, $\mathsf{left}$ and $\mathsf{right}$, which determine whether the next state is the left or right successor node in the tree.

<!-- chunk {"id": "body-0217", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For $h\geq{}H_1$, there are two cases: \item For $s\in\cS'$, the agent can choose to ``wait'' using action $\wait$, or choose an action from $\cA'\ldef\brk{A'}$, where $A'\ldef{}A-1$. The $\wait$ action causes the agent to stay in $s$ (i.e. $P(s\mid{}s,\wait)=1)\;\forall{}s\in\cS'$), while actions in $\brk{A'}$ cause the agent to immediately transit $P(\term\mid{}s,a)=1\;\forall{}s\in\cS',a\in\brk{A'}$). \item The terminal state $\term$ is self-looping and (i.e. $P(\term\mid{}\term,\cdot)=1$).

<!-- chunk {"id": "body-0218", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\item Let $\cH'=\crl{H_1,\ldots,H}$. For each $\hstar\in\cH', \sstar\in\cS', \astar\in\cA'$, we define an MDP $\Mhsastar$ which has the dynamics described above and the following reward functions: \item $\Rm_h(s,a)=0$ a.s. for all $h<H_1$. \item $\Rm_h(\term,\cdot)=0$ a.s. for all $h>H_1$ \item $\Rm_h(s,\wait)=0$ a.s.

<!-- chunk {"id": "body-0219", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We choose $\cM'=\crl*{M_{s,a}}_{h\in\cH',s\in\cS',a\in\cA'}$. Finally, we take the reference MDP $\Mbar=(P,\Rmbar)$ to have the same dynamics and rewards as above, except that $\Rmbar_h(s,a)=\Ber(1/2)$ for all $h\in\cH', s\in\cS', a\in\cA'$.

<!-- chunk {"id": "body-0220", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Regret lower bound} We apply \pref{thm:lower\_main\_expectation} with the lower bound on the \CompShort from \pref{prop:lower\_tabular}, which gives that for any $\gamma\geq{}c\sqrt{T}$, \geq{} c'\cdot\frac{HSAT}{\gamma}$, so long as $\frac{HSA}{96\gamma}\leq\vepslowg=c''\frac{\gamma}{T}$, where $c,c',c''>0$ are numerical constants.\footnote{As in the multi-armed bandit example, we have $\abscontp=\bigoh$ in \pref{thm:lower_main_expectation} for the MDP choose $\gamma=C\cdot\sqrt{AT}$ for sufficiently large $C>0$, we have \En\brk*{\RegDM} \geq{} \Omega(\sqrt{HSAT}).

<!-- chunk {"id": "body-0221", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We showed how to bound the \CompText for multi-armed bandits and tabular reinforcement learning via Bayesian approaches (posterior sampling) and frequentist approaches (inverse gap weighting). The analyses for both techniques parallel each other, and leverage decoupling and change of measure arguments. We build on these ideas in \pref{sec:bandit} and \pref{sec:rl} to derive algorithms and bounds for more complex settings.

<!-- chunk {"id": "body-0222", "role": "body", "section": "Paper Body", "weight": 1.0} -->

While we have considered posterior sampling (the most ubiquitous Bayesian approach) and inverse gap weighting (a somewhat more recent frequentist approach) and highlighted parallels, upper confidence bound-based approaches have been conspicuously absent up to this point, and do not appear to be sufficient to bound the \CompText. Informally, this is because the \CompShort considers estimation error under the \emph{learner's own distribution} (i.e., future estimation error after the learner commits to the exploration strategy), while UCB and other confidence-based approaches explore based on estimation error on historical data. Further research is required to better understand whether this distinction is fundamental.

<!-- chunk {"id": "body-0223", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Application to Bandits \label{sec:bandit} As a special case of our main results, we obtain algorithms and lower bounds for structured bandits with large action spaces section, we highlight some well-known instances of the structured bandit problem recovered by our results (\pref{sec:bandits\_familiar}), then provide a new guarantee based on a combinatorial parameter called the \emph{star number} (\pref{sec:bandits\_star}). The latter result improves upon previous regret bounds based on the eluder dimension.

<!-- chunk {"id": "body-0224", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Familiar Examples} \label{sec:bandits\_familiar} We consider three canonical structured bandit settings, linear bandits, convex bandits, and non-parametric bandits, and provide tight and lower bounds on the \CompText. We then provide additional lower bounds for bandits with ReLU rewards and for various bandit problems with gaps.

<!-- chunk {"id": "body-0225", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Throughout the section we assume $\cR\subseteq\brk*{0,1}$ unless otherwise specified. For a given function class $\cF\subseteq\prn{\Act\to\cR}$, we define $\cMf=\crl*{M: \fm\in\cF}$ as the induced class of models. We tacitly make use of the fact that all of the lower bound constructions $\cM'\subseteq\cM$ in this section satisfy $\abscontp=\bigoh$ for \pref{thm:lower\_main}.

<!-- chunk {"id": "body-0226", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Linear Bandits} \label{sec:linear} In the linear bandit setting, we set $\Act\subseteq\bbR^{d}$, define $\cF=\crl*{\act\mapsto\tri{\theta,\act}\mid{}\theta\in\Theta}$ for a parameter set $\Theta\subseteq\bbR^{d}$, then take $\cM=\cMf$ as the induced model class. The following recent result from gives an efficient algorithm that leads to upper bounds on the \CompText for this setting. \begin{proposition}[Upper bound for linear bandits] \label{prop:bandit\_upper\_linear} Consider the linear bandit setting with $\cR=\bbR$.

<!-- chunk {"id": "body-0227", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Combining this strategy with \pref{thm:upper\_main\_bayes}, we obtain $\En\brk{\RegDM}\leq{}\bigoh(\sqrt{dT\log\abs{\Act}})$ when $\abs{\Act}<\infty$, and for infinite action spaces we obtain $\En\brk{\RegDM}\leq\bigoht(d\sqrt{T})$ whenever $\Theta$ and $\Act$ have bounded diameter; both results are optimal. More generally, using this strategy within the \mainalg algorithm (\pref{thm:upper\_general}) yields $\En\brk{\RegDM}\leq\bigoh(\sqrt{dT\cdot{}\EstHel})$.

<!-- chunk {"id": "body-0228", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We now turn our attention to lower bounds. Note that if we take $\Theta$ to be the $\ls_{\infty}$-ball and $\Act$ to be the $\ls_{1}$-ball, a trivial lower bound on the \CompShort is $\frac{d}{\gamma}$, since this embeds the finite-armed bandit setting. The following result shows that the same lower bound holds under euclidean geometry. \begin{proposition}[Lower bound for linear bandits] \label{prop:bandit\_lower\_linear} Consider the linear bandit setting with $\cR=\brk{-1,+1}$, and let $\Act=\Theta=\crl*{v\in\bbR^{d}\mid{}\nrm*{v}_{2}\leq{}1}$.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Then for all $d\geq{}4$ and $\gamma\geq\frac{2d}{3}$, there exists $\Mbar\in\cM$ such that \comp(\cMinf[\vepsg](\Mbar),\Mbar) \geq{} \frac{d}{12\gamma}, where $\vepsg = \frac{d}{3\gamma}$. Combining this result with \pref{thm:lower\_main\_expectation} leads to a lower bound of the form $\En\brk*{\RegDM}\geq\bigom(\sqrt{dT})$.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Convex Bandits} The convex bandit problem is a generalization of the linear bandit. We take $\Act\subseteq\bbR^{d}$, define \cF=\crl*{f:\Act\to\brk{0,1}\mid{}\text{$f$ is concave and \] and take $\cM=\cMf$ as the induced model class.\footnote{We consider concave rather than concave functions because we work with rewards instead of losses.} The following recent result of provides a bound on the \CompText for this setting.\footnote{The statement presented here requires very slight modifications to the construction.

<!-- chunk {"id": "body-0231", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Namely, certain parameters that scale with $T$ in the original construction must be replaced by $\gamma$.} \begin{proposition}[Upper bound for convex bandits \label{prop:bandit\_upper\_convex} For the convex bandit setting with $\cR=\brk{0,1}$, we have \compSq(\cM,\Mbar) \leq{} \bigoh\prn*{ \frac{d^{4}}{\gamma}\cdot\polylog(d,\mathrm{diam}(\Act),\gamma) for all $\Mbar\in\conv(\cM)$ and $\gamma>0$. Since this setting has $\ActComp\leq\bigoht(d)$ whenever $\diam(\Act)=\bigoh$, combining the bound above with \pref{thm:upper\_main\_bayes} leads to regret $\En\brk{\RegDM}\leq{}\bigoht(d^{2.5}\sqrt{T})$.

<!-- chunk {"id": "body-0232", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We mention in passing that previous results in the line of work on Bayesian regret for convex bandits can also be interpreted as bounds on the \CompText. While the optimal dependence on $d$ for this setting is not yet understood, a lower bound of $\sqrt{dT}$ follows from the result for the linear setting.

<!-- chunk {"id": "body-0233", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Nonparametric Bandits} \newcommand{\met}{\rho} \newcommand{\Mcov}{\cN\_{\met}} For the next example, we consider a standard nonparametric bandit problem: Lipschitz bandits in metric spaces. We take $\Act$ to be a metric space equipped with metric $\met$, then take $\cM=\cMf$, where we define \cF = \crl*{f:\Act\to\brk{0,1} \mid{} \text{$f$ is $1$-Lipschitz w.r.t $\met$}}. Our results are stated in terms of covering numbers with respect to the metric $\rho$.

<!-- chunk {"id": "body-0234", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Let us say that $\Act'\subseteq\Act$ is an $\veps$-cover with \forall{}\act\in\Act\quad\exists{}\act'\in\Act'\quad\text{s.t.}\quad \met(\act,\act')\leq\veps, and let $\Mcov(\Act,\veps)$ denote the size of the smallest such cover. \begin{proposition}[Upper bound for Lipschitz bandits] \label{prop:bandit\_upper\_lipschitz} Consider the Lipschitz bandit setting with $\cR=\bbR$, and suppose that $\Mcov(\Act,\veps)\leq\veps^{-d}$ for $d>0$.

<!-- chunk {"id": "body-0235", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Let $\Mbar\in\conv(\cM)$ and $\gamma\geq{}1$ be given and consider the following algorithm: \item Let $\Act'\subseteq\Act$ witness the covering number $\Mcov(\Act,\veps)$ for a parameter $\veps>0$. \item Perform the inverse gap weighting strategy in \pref{eq:igw} By setting $\veps=\gamma^{-\frac{1}{d+1}}$, this strategy certifies that \compSq(\cM,\Mbar) \leq{} 2\gamma^{-\frac{1}{d+1}}. Since $\ActComp\leq\bigoht(d)$ for this setting, if we apply \pref{thm:upper\_main\_bayes} with this result we obtain \En\brk{\RegDM} \leq \bigoht(T^{\frac{d+1}{d+2}}) which matches the minimax rate derived.

<!-- chunk {"id": "body-0236", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We complement this with a lower bound. \begin{proposition}[Lower bound for Lipschitz bandits] \label{prop:bandit\_lower\_lipschitz} Consider the Lipschitz bandit setting with $\cR=\brk{0,1}$. Suppose that $\Mcov(\Act,\veps)\geq{}\veps^{-d}$ for $d\geq{}1$. Then for all $\gamma\geq{}1$, there exists $\Mbar\in\cM$ such that \comp(\cMinf[\vepsg](\Mbar),\Mbar) \geq{} 2^{-7}\gamma^{-\frac{1}{d+1}}, where $\vepsg=6^{-2}\gamma^{-\frac{1}{d+1}}$.

<!-- chunk {"id": "body-0237", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Plugging this guarantee into \pref{thm:lower\_main\_expectation}, we obtain a lower bound of the form $\En\brk*{\RegDM}\geq\bigomt(T^{\frac{d+1}{d+2}})$, which again recovers the minimax rate. Extending these upper and lower bounds on the \CompShort to accommodate other (e.g., \Holder) nonparametric bandit problems is straightforward. \subsubsection{ReLU Bandits} We now consider a bandit setting based on the well-known ReLU activation function $\relu(x)=\max\crl{x,0}$.

<!-- chunk {"id": "body-0238", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Note that since we work with rewards, this setting would be a special case of bandit convex optimization if we were to replace the $+\relu(\cdot)$ function in \pref{eq:relu} with $-\relu(\cdot)$, and in this case it would be possible to appeal to \pref{prop:bandit\_upper\_convex} to derive a $\sqrt{\poly(d)T}$ bound on regret. However, the $+\relu(\cdot)$ formulation in \pref{eq:relu} cannot be viewed as an instance of bandit convex optimization, and the following proposition shows that this setting is intractable.\looseness=-1 \begin{proposition}[Lower bound for ReLU bandits] \label{prop:bandit\_lower\_relu} Consider the ReLU bandit setting with $\cR=\brk*{-1,+1}$.

<!-- chunk {"id": "body-0239", "role": "body", "section": "Paper Body", "weight": 1.0} -->

By plugging this result into \pref{thm:lower\_main} and setting $\gamma=T$, we conclude that any algorithm must have \RegDM \geq \bigom(\min\crl{e^{\Omega(d)},T}) with constant probability, which further implies that $\En\brk*{\RegDM} \geq \bigom(\min\crl{e^{\Omega(d)},T})$. This recovers recent impossibility results \subsubsection{Gap-Dependent Lower Bounds} In multi-armed bandits, \emph{gap-dependent} regret bounds that adapt \Delm\ldef{}\min\_{\act\neq\pim}\crl*{\fm(\pim) - \fm(\act)} between the best and second-best action have been the subject of extensive guarantees in reinforcement learning with function approximation have also received recent interest as a means to bypass certain intractability results.

<!-- chunk {"id": "body-0240", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Here we prove lower bounds on the \CompText for finite-armed bandits and linear bandits when the class $\cM$ is constrained to have gap $\Delta$. These examples highlight that the \CompShort leads to meaningful lower bounds even for ``easy'' problems with low \begin{proposition}[Multi-armed bandits with gaps] \label{prop:bandit\_gap\_tabular} Let $\cM$ be the class of all multi-armed bandit problems over $\Act=\brk{A}$ with $\cR=\brk{0,1}$ and gap $\Delta>0$. For all $\Delta\in(0,1/8)$, there exists $\Mbar\in\cM$, such that \comp(\cMinf[\Delta](\Mbar),\Mbar)\geq{} \frac{\Delta}{4}\indic\crl*{ \gamma\leq\frac{A}{48\Delta} for all $\gamma>0$.

<!-- chunk {"id": "body-0241", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Since minimax regret is non-decreasing with $T$, this implies a lower bound of the form \label{eq:mab\_gap} \En\brk*{\RegDM} \geq \bigom\prn*{ \min\crl*{\Delta{}T, \frac{A}{\Delta}} Up to a $\log(T)$ factor, this matches the usual $\frac{A}{\Delta}$ scaling found in standard gap-dependent lower bounds when $T$ is sufficiently large. We caution however that these results are \emph{instance-dependent} in nature, and provide gap-dependent lower bounds on the regret for any particular problem instance, whereas \pref{eq:mab\_gap} is a minimax lower bound over the class of all possible models with gap $\Delta$. This is a consequence of the fact that the \CompText and our associated lower bounds capture minimax complexity for decision making, which is fundamentally different from instance-dependent complexity; see \pref{sec:related} for more discussion.

<!-- chunk {"id": "body-0242", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We proceed with an analogous lower bound for the linear setting in \pref{sec:linear}. \begin{proposition}[Linear bandits with gaps] \label{prop:bandit\_gap\_linear} For every $\Delta\in(0,1/4)$, there exists a collection $\cM$ of linear bandit models with $\cR=\brk{-1,+1}$, $\Act\subseteq\Theta=\crl*{v\in\bbR^{d}\mid{}\nrm*{v}_{2}\leq{}1}$, and gap $\Delta>0$, such that for some $\Mbar\in\cM$, \comp(\cMinf[\Delta](\Mbar),\Mbar) \geq{} \frac{\Delta}{4}\indic\crl*{ \gamma\leq\frac{d}{12\Delta} for all $\gamma>0$.

<!-- chunk {"id": "body-0243", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Using similar calculations to the multi-armed bandit example, we deduce that any algorithm must have \label{eq:linear\_gap} \En\brk*{\RegDM} \geq \bigom\prn*{ \min\crl*{\Delta{}T, \frac{d}{\Delta}} \subsection{Disagreement Coefficient, Star Number, and Eluder Dimension} \label{sec:bandits\_star} In this section we show that the \CompText can recover regret bounds for bandits based on a well-known combinatorial parameter called the \emph{eluder dimension} and then give a new bound based on a closely related but tighter parameter called the \emph{star number} We begin by defining the eluder dimension for a value function class $\cF$.

<!-- chunk {"id": "body-0244", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{def:eluder} Let $\cF:\Act\to\bbR$ be given, and define $\ElCheck(\cF,\Delta)$ as the length of the longest sequence of decisions $\act_1,\ldots,\act_s\in\Act$ such that for all $i$, there exists $f_i\in\cF$ such that \abs*{f\_i(\act\_i)}>\Delta,\quad\text{and}\quad\sum\_{j<i}f^2\_i(\act\_j)\leq\Delta^{2}. The eluder dimension is defined as $\El(\cF,\Delta)=\sup_{\Delta'\geq{}\Delta}\ElCheck(\cF,\Delta')\vee{}1$. The star number was originally introduced in the context of active learning with binary classifiers. We work with a scale-sensitive variant introduced, which can be thought of as a ``non-sequential'' analogue of the eluder dimension.

<!-- chunk {"id": "body-0245", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{def:star} Let $\cF:\Act\to\bbR$ be given, and define $\StarCheck(\cF,\Delta)$ as the length of the longest sequence of decisions $\act_1,\ldots,\act_s\in\Act$ such that for all $i$, there exists $f_i\in\cF$ such that \abs*{f\_i(\act\_i)}>\Delta,\quad\text{and}\quad\sum\_{j\neq{}i}f^{2}\_i(\act\_j)\leq\Delta^{2}. The star number is defined as $\Star(\cF,\Delta)=\sup_{\Delta'\geq{}\Delta}\StarCheck(\cF,\Delta')\vee{}1$. It is clear from this definition that $\StarDim(\cF,\Delta)\leq\ElDim(\cF,\Delta)$.

<!-- chunk {"id": "body-0246", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In general, the star number can be arbitrarily small compared to the eluder dimension.

<!-- chunk {"id": "body-0247", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The following result shows that boundedness of star number and eluder dimension always implies boundedness of the \CompText. \label{thm:eluder\_star} Consider any class $\cM$ with $\Rspace=\brk{0,1}$ and reference model $\Mbar$ (not necessarily in $\cM$) with $\fmbar\in\brk{0,1}$. Suppose the conclusion of \pref{prop:minimax\_swap\_dec} holds. Then for all $\gamma\geq{}e$, we have \label{eq:comp\_star} \compSq(\cM,\Mbar) \leq{} \bigoh\cdot\inf\_{\Delta>0}\crl*{\Delta + \frac{\sup\_{M\in\cM}\StarDim^{2}(\cFm-\fm,\Delta)\log^{2}(\gamma)}{\gamma}}.

<!-- chunk {"id": "body-0248", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{eq:comp\_eluder} \compSq(\cM,\Mbar) \leq{} \bigoh\cdot\inf\_{\Delta>0}\crl*{\Delta + \frac{\sup\_{M\in\cM}\El(\cFm-\fm,\Delta)\log^{2}(\gamma)}{\gamma}}. An upper bound in terms of the star number immediately implies an upper bound in terms of the eluder dimension, but we present separate bounds for each parameter because Eq. \pref{eq:comp\_star} has quadratic dependence on the star number, while Eq. \pref{eq:comp\_eluder} has linear dependence on the eluder dimension.

<!-- chunk {"id": "body-0249", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Abbreviating $\ElDim\equiv\sup_{f\in\cFm}\ElDim(\cFm-f,1/T)$ and $\StarDim\equiv\sup_{f\in\cFm}\Star(\cFm-f,1/T)$, this result recovers the $\bigoht(\sqrt{\ElDim{}T})$ regret bound derived in as a special case by appealing to \pref{thm:upper\_main\_bayes}, but also implies a regret bound of the form $\bigoht(\sqrt{\StarDim^2{}T})$, which can be arbitrarily tighter.

<!-- chunk {"id": "body-0250", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Compared to the earlier examples in this section, one should not expect to derive a matching lower bound on the \CompText. Unlike the \CompShort itself, the star number and eluder dimension only provide sufficient conditions for sample-efficient learning, and neither parameter plays a fundamental role in determining the minimax regret. For example, both parameters are exponential in the dimension for bandit convex optimization, while \pref{prop:bandit\_upper\_convex} shows that the \CompShort is polynomial.

<!-- chunk {"id": "body-0251", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\pref{thm:eluder\_star} is a corollary of a more general result that provides a \emph{prior-dependent} upper bound on the dual Bayesian \CompText when posterior sampling is applied. For a given prior $\mu\in\Delta(\cM)$ and distance $\Dgen{\cdot}{\cdot}$, define \label{eq:comp\_dual\_prior} \inf\_{p\in\Delta(\Act)}\En\_{M\sim\mu}\En\_{\act\sim{}p}\biggl[\fm(\pim)-\fm(\pi) -\gamma\cdot\Dgen{M(\act)}{\Mbar(\act)} $\compgendual(\cM,\Mbar)=\sup_{\mu\in\Delta(\cM)}\compgendual(\mu,\Mbar)$.

<!-- chunk {"id": "body-0252", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our result is stated in terms of a parameter called the (scale-sensitive) disagreement \label{def:disagreement} For a distribution $\rho\in\Delta(\Act)$, the disagreement coefficient is \sdis(\cF,\Delta\_0,\veps\_0;\rho) = \sup\_{\Delta\geq\Delta\_0,\veps\geq{}\veps\_0}\crl*{\frac{\Delta^{2}}{\veps^{2}}\cdot \bbP\_{\act\sim\rho}\prn*{ \exists f\in\cF: \abs*{f(\act)}>\Delta, \En\_{\act\sim\rho}\brk*{f^{2}(\act)}\leq\veps^{2} Our main result is as follows.

<!-- chunk {"id": "body-0253", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\pref{thm:disagreement} generalizes the decoupling argument used to prove the upper bound on the \CompText for multi-armed bandits in \pref{sec:examples}, with the disagreement coefficient providing a bound on the price of decoupling. \pref{thm:eluder\_star} follows immediately from this theorem, along with the following technical result \label{lem:disagreement\_to\_ratio} For all $\rho\in\Delta(\Act)$ and $\Delta,\veps>0$, we have $\sdis(\cF,\Delta,\veps;\rho)\leq{}4(\Star(\cF,\Delta))^{2}$ and $\sdis(\cF,\Delta,\veps;\rho)\leq{}4\El(\cF,\Delta)$.

<!-- chunk {"id": "body-0254", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Application to Reinforcement Learning} We now turn our focus to episodic reinforcement learning with function approximation (\pref{ex:rl}), providing upper and lower bounds on regret. Our main results are as follows. \item First, in \pref{sec:rl\_bilinear\_basic}, we show how to extend the techniques in \pref{sec:examples} (posterior sampling and the \pcigw method) to bound the \CompShort and obtain regret bounds for \emph{bilinear classes}, a large class of reinforcement learning problems which captures many settings where sample-efficient reinforcement learning is possible. Our results here are applicable when the class of models has moderate model estimation complexity. \item Next, in \pref{sec:rl\_bilinear\_refined}, we provide tighter guarantees for bilinear classes that scale only with the estimation complexity for the underlying class of value functions. This result recovers a broader set of sample-efficient learning guarantees, but is somewhat more specialized to the bilinear class framework.

<!-- chunk {"id": "body-0255", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\item Finally, in \pref{sec:rl\_lower}, we derive \emph{lower bounds} for reinforcement learning. As a highlight, we show that the \CompText recovers exponential lower bounds for reinforcement learning with linearly realizable function approximation. See \pref{table:frameworks} for a summary of the relationship between the \CompShort and other complexity measures in RL; precise results concerning Bellman-Eluder dimension are deferred to sec:bedim.

<!-- chunk {"id": "body-0256", "role": "body", "section": "Paper Body", "weight": 1.0} -->

All of the results in this section take $\Act = \PiGen$ and $\cR\subseteq\brk{0,1}$ (that is, $\sum_{h=1}^{H}r_h\in\brk{0,1}$) unless otherwise specified.

<!-- chunk {"id": "body-0257", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Reinforcement learning: Model-based, model-free, and beyond} Recall that for reinforcement learning, each model $M\in\cM$ consists of a collection of probability transition functions $\Pm_{1},\ldots,\Pm_{H}$ and reward distributions $\Rm_1,\ldots,\Rm_{H}$. This formulation can be viewed as an instance of \emph{model-based} reinforcement learning, where one uses function approximation to directly model the dynamics of the environment. What is perhaps less obvious is that this formulation also suffices to capture model-free methods and direct policy search \item For model-free (or, value function approximation) methods, one typically assumes that we are given a class of $Q$-value functions $\cQ=\cQ_1\times\cdots\times\cQ_H$ that is \emph{realizable} in the sense that it contains the optimal $Q$-function for every problem instance under consideration.

<!-- chunk {"id": "body-0258", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This is captured in the \FrameworkShort framework by taking \label{eq:model\_free} \cM\_{\cQ} = \crl*{ M \mid \Qmstar\_h \in\cQ\_h\;\;\forall{}h\in\brk{H}} as the induced class of models, and hence we can derive upper and lower bounds for this setting. A well-known special case is that of \emph{linearly realizable} function approximation, where each class $\cQ_h$ is linear; this setting is addressed in \pref{sec:rl\_lower}. Naturally, one can modify the definition in \pref{eq:model\_free} to incorporate commonly used additional assumptions such as low rank structure or completeness under \item Direct policy search methods do not model the dynamics or value functions, and instead work directly with a given class of policies $\Pi$ (specified via function approximation). Here, a natural notion of realizability (e.g.,) is to assume the policy class contains the optimal policy for all problem instances under consideration.

<!-- chunk {"id": "body-0259", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This is captured by taking \cM\_{\Pi} = \crl*{M \mid{} \pim\in\Pi} as the induced class of models. We do not focus on this setting here, as few positive results are known. From the perspective of lower bounds, this viewpoint is without loss of generality, though more care is required to derive tight upper bounds (cf. sec:rl\_bilinear\_refined), since our generic results in sec:framework scale with the model estimation complexity $\log\abs{\cM}$.

<!-- chunk {"id": "body-0260", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Bilinear Classes: Basic Results} \label{sec:rl\_bilinear\_basic} \includegraphics[width=.65\textwidth]{figures/rl\_frameworks} Relationship between \CompText and existing frameworks for generalization in reinforcement learning. An arrow indicates that the head framework is subsumed by the tail framework. \label{table:frameworks} In this section, we use the \mainalg algorithm to provide regret bounds for reinforcement learning with bilinear classes. The bilinear class framework generalizes a number of previous structural conditions, most notably Bellman rank, and captures most known settings where sample-efficient reinforcement learning is possible. The following is an adaptation of the definition.

<!-- chunk {"id": "body-0261", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{definition}[Bilinear class] \label{def:bilinear} A model class $\cM$ is said to be bilinear relative to reference model $\Mbar$ if: \item There exist functions $W_h(\cdot\midsem\Mbar):\cM\to\bbR^{d}$, $X_h(\cdot\midsem\Mbar):\cM\to\bbR^{d}$ such that for all \label{eq:bilinear\_residual} \abs*{\Enm{\Mbar}{\pim}\brk*{ \leq\abs{\tri{W\_h(M;\Mbar),X\_h(M;\Mbar)}}. We assume that $W_h(\Mbar;\Mbar)=0$. \item Let $z_h = (s_h, a_h, r_h, s_{h+1})$.

<!-- chunk {"id": "body-0262", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We let $\dimbi(\cM,\Mbar)$ denote the minimal dimension $d$ for which the bilinear class property holds relative to $\Mbar$, and define $\dimbifull=\sup_{\Mbar\in\cM}\dimbi(\cM,\Mbar)$. We let $\Lbi(\cM;\Mbar)\geq{}1$ denote any almost sure upper bound on $\abs{\lestm(M';z_h)}$ under $\Mbar$, and let $\Lbifull=\sup_{\Mbar\in\cM}\Lbi(\cM;\Mbar)$.

<!-- chunk {"id": "body-0263", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For the remainder of this section, we define concatenated factorizations $X(M;\Mbar),W(M;\Mbar)\in\bbR^{dH}$ via \label{eq:bilinear\_full} X(M;\Mbar) = (X\_1(M;\Mbar), \ldots,X\_H(M;\Mbar)),\mathand W(M;\Mbar) = (W\_1(M;\Mbar), \ldots,W\_H(M;\Mbar)). Basic examples of bilinear classes (cf.) include: \item Linear MDPs. \item Block MDPs and reactive POMDPs \item FLAMBE/feature selection in low rank MDPs. \item MDPs with Linear $Q^{\star}$ and $V^{\star}$. \item MDPS with Low Occupancy Complexity. \item Linear mixture MDPs \item Linear dynamical systems (LQR).

<!-- chunk {"id": "body-0264", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Further examples include $Q^{\star}$-irrelevant state aggregation and classes with low Bellman rank or Witness rank The results in this subsection are applicable to any bilinear class estimation complexity $\MComp$ is non-trivial. Guarantees under more general conditions are given in \pref{sec:rl\_bilinear\_refined}.

<!-- chunk {"id": "body-0265", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Bounding the \CompText: Posterior Sampling and \pcigw} \label{sec:rl\_bilinear\_dec} We now show how to bound the \CompText for reinforcement learning with bilinear classes. Our development here parallels that of the tabular setting in \pref{sec:tabular}. We first provide a bound on the Bayesian \CompShort via posterior sampling, then provide an efficient algorithm that leads to a bound on the frequentist \CompShort by adapting the inverse gap weighting technique.

<!-- chunk {"id": "body-0266", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Bounding the \CompShort with Posterior Sampling} For $\alpha\in$, let $\pialpham$ be the randomized policy that---for each $h$---plays $\pi_{\sss{M,h}}$ with probability $1-\alpha/H$ and $\piest_{\sss{M,h}}$ with probability $\alpha/H$. Our guarantee for (modified) posterior sampling is as follows.\looseness=-1 \begin{restatable}{theorem}{posteriorbilinear} \label{thm:posterior\_bilinear} Let $\cM$ be a bilinear class and let $\Mbar$ be an arbitrarily reference model. Let $\mu\in\Delta(\cM)$ be given, and consider the modified posterior sampling strategy that samples $M\sim\mu$ and plays $\pialpham$, where $\alpha\in$ is a parameter.

<!-- chunk {"id": "body-0267", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\item If $\piestm = \pim$ (i.e., estimation is on-policy), this strategy with $\alpha=0$ certifies that \compdual(\cM,\Mbar) \leq{} \frac{\jqedit{4}H^{2}\Lbifulls{}\jqedit{\dimbi(\cM)}}{\gamma} for all $\gamma>0$.

<!-- chunk {"id": "body-0268", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Focusing on dimension, the \CompShort bound in the on-policy case where $\piestm=\pim$ scales as $\frac{\dimbifull}{\gamma}$, which leads to regret \RegDM \approxleq \sqrt{\dimbifull{}\cdot{}T\cdot{}\EstHel} for any online estimation algorithm; recall that for finite classes, one can take $\EstHel\approxleq\log\abs{\cM}$. In the general case, the \CompShort bound scales as $\sqrt{\frac{\dimbifull}{\gamma}}$ due to the use of forced exploration, which leads to \RegDM \approxleq{} (\dimbifull\cdot\EstH)^{1/3}\cdot{}T^{2/3}. In terms of $T$ dependence, this matches the regret bound implied by the results, which also rely on forced exploration; algorithms with $\sqrt{T}$-regret for general bilinear classes are not currently known.

<!-- chunk {"id": "body-0269", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In both of these examples, the final regret bound depends on the estimation complexity for the class of models, which is not required. This is an instance of one of the main gaps between our generic upper and lower bounds discussed in \pref{sec:main\_discussion}. We give a specialized approach to remove this issue in the sequel.% See \pref{app:rl\_extensions} for an extension of thm:posterior\_bilinear which covers the closely related setting of \paragraph{Bounding the \CompShort with \pcigw} Our frequentist algorithm, \pcigwb (\pref{alg:igw\_bilinear}), is an adaptation of the \pcigw algorithm used in the tabular setting. The algorithm is based on the primitive of \emph{G-optimal design}, which we use to generalize the notion of policy cover (i.e., a collection of policies that maximizes the visitation probability for any given state-action pair) used in \pref{alg:policy\_cover\_igw}.

<!-- chunk {"id": "body-0270", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{definition}[G-optimal design] Let a set $\cX\subseteq\bbR^{d}$ be given. A distribution $p\in\Delta(\cX)$ is said to be a G-optimal design with approximation factor $\Copt\geq{}1$ if \label{eq:optimal\_design} \sup\_{x\in\cX}\tri*{\Sigma\_p^{\pinv}x,x}\leq{}\Copt\cdot{}d, where $\Sigma_p\ldef\En_{x\sim{}p}\brk*{xx^{\trn}}$. The following result guarantees existence of an exact optimal design with $\Copt=1$; we consider designs with $\Copt>1$ for computational reasons.

<!-- chunk {"id": "body-0271", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For any compact $\cX\subseteq\bbR^{d}$, there exists an optimal design The \pcigwb algorithm (\pref{alg:igw\_bilinear}) combines inverse gap weighting with optimal design. Let $\Mbar\in\cM$ be the estimated model. For each layer $h$, the algorithm computes an (approximate) G-optimal design for the collection of vectors $\crl{Y_h(M;\Mbar)}_{M\in\cM}$, where Y\_h(M;\Mbar) \ldef{} \frac{X\_h(M;\Mbar)}{\sqrt{1+\eta(\fmbar(\pimbar)-\fmbar(\pim))}. We denote resulting optimal design by $\qopt_h\in\Delta(\cM)$.

<!-- chunk {"id": "body-0272", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Analogous to the tabular setting, the optimal design for the unweighted factors $\crl*{X_h(M;\Mbar)}_{M\in\cM}$ would suffice to ensure good exploration, but the optimal design for the weighted factors $\crl*{Y_h(M;\Mbar)}_{M\in\cM}$ balances exploration and regret, and is critical for deriving $\sqrt{T}$-type regret bounds.

<!-- chunk {"id": "body-0273", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For the next step, we mix the optimal designs for each layer via $q\ldef{}\frac{1}{2H}\sum_{h=1}^{H}\qopt_h + \frac{1}{2}\delta_{\Mbar}$; we also mix in the estimated model $\Mbar$. Finally, we compute a distribution over policies via inverse gap weighting: p(\pialpham) = \frac{q(M)}{\lambda + \eta(\fmbar(\pimbar)-\fmbar(\pim))}. We use the mixed policies $\pialpham$ to allow for a small amount of forced exploration (controlled by the parameter $\alpha$) in the off-policy case where $\piestm\neq\pim$.

<!-- chunk {"id": "body-0274", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\pref{alg:igw\_bilinear} is efficient whenever i) we can compute an approximate optimal design for the factors $\crl*{Y_h(M;\Mbar)}_{M\in\cM}$ efficiently, and ii) the design has small support. The final guarantee for the algorithm scales linearly with the approximation factor $\Copt$. In sec:rl\_bilinear\_computational, we show that both desiderata can be achieved (with $\Copt=\bigoh(d)$) whenever the learner has access to a certain planning oracle, leading to an efficient algorithm.

<!-- chunk {"id": "body-0275", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The main guarantee for the \pcigwb algorithm is as follows.

<!-- chunk {"id": "body-0276", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{restatable}{theorem}{igwbilinear} \label{thm:igw\_bilinear} Let $\cM$ be a bilinear class. Let $\gamma>0$ and $\Mbar\in\cM$ be given, and consider the \pcigwb strategy in \pref{alg:igw\_bilinear}. Suppose the optimal design solver in \pref{line:approximate\_optimal\_design} has approximation factor \item If $\piestm = \pim$ (i.e., estimation is on-policy), this strategy with $\eta=\frac{\gamma}{3H^3\Copt\Lbifulls{}\dimbi(\cM,\Mbar)}$ and $\alpha=0$ certifies that \comp(\cM,\Mbar) \leq{} \frac{9H^{3}\Copt\Lbifulls{}\dimbi(\cM,\Mbar)}{\gamma}.

<!-- chunk {"id": "body-0277", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This guarantee matches the bound on the \CompShort for posterior sampling (\pref{thm:posterior\_bilinear}) up to a factor of $H$, though it requires that $\Mbar\in\cM$. We refer to sec:igw\_bilinear for an efficient implementation, as well as examples of online estimators that satisfy the conditions \Statex \algcomment{Exploration for bilinear classes via inverse gap weighting.} \State \textbf{parameters}: \Statex Model class $\cM$ and reference model $\Mbar\in\cM$ with bilinear dimension $d$. \Statex Learning rate $\eta>0$. \Statex Forced exploration parameter $\alpha>0$.

<!-- chunk {"id": "body-0278", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\State \multiline{For each $M\in\cM$, let $\pialpham$ be the randomized policy that for each $h$ plays $\pi_{\sss{M,h}}$ with probability $1-\alpha/H$ and $\piest_{\sss{M,h}}$ with probability \State For each $M\in\cM$ and $h\in\brk*{H}$, define \label{eq:bilinear\_reweighted} Y\_h(M;\Mbar) = \frac{X\_h(M;\Mbar)}{\sqrt{1+\eta(\fmbar(\pimbar)-\fmbar(\pim))} \Statex \algcommentlight{The distribution $\qopt_h$ is assumed to solve \pref{eq:optimal\_design} with approximation factor $\Copt$.} \State For each $h$, obtain $\qopt_h\in\Delta(\cM)$ from optimal design solver

<!-- chunk {"id": "body-0279", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\State \multiline{For each $M\in\supp(q)$, let p(\pialpham) = \frac{q(M)}{\lambda + \eta(\fmbar(\pimbar)-\fmbar(\pim))}, where $\lambda\in[1/2,1]$ is chosen such that \State \textbf{return} $p$. \label{alg:igw\_bilinear} \subsection{Bilinear Classes: Refined Guarantees} \label{sec:rl\_bilinear\_refined} We now use the \mainalg framework to give refined regret bounds that sharpen our results for bilinear classes in the prequel. Instead of scaling with the estimation error for the model class $\cM$, our results here scale only with the estimation complexity for the class of \cQm = \crl*{\Qmstar\mid{}M\in\cM}, which makes them better suited to model-free reinforcement learning settings.

<!-- chunk {"id": "body-0280", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our refined results require the following modifications to the basic bilinear class framework: \item We assume that for all $M\in\cM$, we have \item We assume that $\piestm=\pim$ for all $M\in\cM$ (i.e., estimation is on-policy), and replace Property 2 of \pref{def:bilinear} with the following condition: For all $M, M'\in\cM$, $h\in\brk{H}$ \label{eq:bilinear\_complete} \tri{X\_h(M;\Mbar), W\_h(M';\Mbar)}^2 \leq \Lbifulls\cdot{}\Enm{\Mbar}{\pim}\brk*{ \prn[\Big]{\brk{\cTm[M']\_h\Vmstar[M']\_{h+1}}(s\_h,a\_h) -

<!-- chunk {"id": "body-0281", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\brk{\cTm[\Mbar]\_h\Vmstar[M']\_{h+1}}(s\_h,a\_h)}^2 Finally, we make a Bellman completeness assumption.

<!-- chunk {"id": "body-0282", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The first two properties above are satisfied in most standard model-free settings, including Linear and Linear Bellman Complete MDPs, Low Occupancy Complexity MDPs, and Linear $Q^{\star}$/$V^{\star}$ MDPs. \pref{ass:completeness} is satisfied for Linear and Linear Bellman Complete MDPs, but in general may or may not be satisfied for the problem under consideration. One can extend the results we provide here to the off-policy estimation case and the case where \pref{ass:completeness} does not hold using similar arguments, at the cost of a more complicated analysis and worse dependence on $T$. We do not pursue this here, since our goal is only to give a taste for how the \mainalg framework can recover existing results.

<!-- chunk {"id": "body-0283", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We derive tighter guarantees for bilinear classes by replacing the Hellinger divergence found in the definition of $\comp(\cM,\Mbar)$ with the following divergence tailored to the bilinear class setting: \label{eq:divergence\_bilinear} \Dbi{M(\act)}{\Mbar(\act)} \ldef \sum\_{h=1}^{H}\tri*{X\_h(\pi;\Mbar),W\_h(M;\Mbar)}^{2}. This quantity is always upper bounded by Hellinger distance, but leads to tighter rates because it only depends on the models under consideration through their Bellman residuals.

<!-- chunk {"id": "body-0284", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Following the development for general divergences described in \pref{sec:general\_distance}, we consider a variant of \mainalgB (\pref{alg:bayes\_basic}) tailored to the bilinear divergence $\Dbi{\cdot}{\cdot}$. For each \item Compute posterior $\mu\ind{t}\in\Delta(\cM)$ given $\hist\ind{t-1}$.

<!-- chunk {"id": "body-0285", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The following result---which is proven using the same approach as \pref{thm:posterior\_bilinear}---shows that by moving to $\Dbi{\cdot}{\cdot}$, the \CompShort is bounded by the bilinear dimension. \begin{restatable}{proposition}{decbilinear} \label{prop:dec\_bilinear} Let $\cM$ be a bilinear class. Then for all $\gamma>0$ and \compbidual(\cM,\nu) \leq{} \frac{H\cdot{}\dimbi(\cM)}{\gamma}.

<!-- chunk {"id": "body-0286", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Equipped with a bound on the \CompText, we proceed to give a regret bound for the \mainalg variant above. Our regret bound depends on the following notion of estimation complexity for the value function class $\cQm$. Models $M_1,\ldots,M_N$ are said to be an $\veps$-cover for $\cQm$ if for all $M\in\cM$, there exists $i\in\brk{N}$ such that \max\_{h\in\brk*{H}}\sup\_{s\in\cS,a\in\cA}\abs*{\Qmstar[M\_i]\_h(s,a) - \Qmstar\_h(s,a)}\leq{}\veps.

<!-- chunk {"id": "body-0287", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Let $\cN(\cQm,\veps)$ denote the size of the smallest such cover, and define $\QComp=\inf_{\veps>0}\crl*{\log\cN(\cQm,\veps) + \veps^{2}T}$. Note that for any setting in which the optimal $Q$-functions are linear functions in dimension $d$ (e.g., Linear and Linear Bellman Complete MDPs, Linear $Q^{\star}/V^{\star}$), we have $\Qcomp=\bigoht(dH)$.

<!-- chunk {"id": "body-0288", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our refined regret bound for bilinear classes is as follows. \begin{restatable}{theorem}{bilinearrefined} \label{thm:bilinear\_refined} Suppose that \pref{ass:completeness} holds, and that estimation is on-policy (i.e., $\piestm=\pim$). Consider the \mainalgB algorithm with the optimization problem given in \pref{eq:comp\_argmin\_bilinear}.

<!-- chunk {"id": "body-0289", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This algorithm guarantees that for any prior $\mu\in\Delta(\cM)$ and $\gamma>0$, \En\_{\Mstar\sim\mu}\En\sups{\Mstar}\brk*{\RegDM} \leq{} \bigoht\prn*{ \sqrt{H^2\Lbifulls\cdot{}\dimbifulls{}\cdot{}T\cdot{}\Qcomp} Consequently, we have $\MinimaxReg\leq \bigoht\prn[\big]{ \sqrt{H^2\Lbifulls\cdot{}\dimbifulls{}\cdot{}T\cdot{}\Qcomp} As a concrete example, this leads to $\sqrt{\poly(d,H)\cdot{}T}$ regret for Linear and Linear Bellman Complete MDPs. The main idea behind the proof is as follows.

<!-- chunk {"id": "body-0290", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Using the definition of the \CompShort, we show that \approxleq{} \sup_{\nu\in\Delta(\cM)}\compbidual(\cM,\nu)\cdot{}T + \gamma\cdot\sum_{t=1}^{T}\En\brk*{\Dbi{\Mstar(\pi\ind{t})}{\Mhat\ind{t}(\pi\ind{t})}}. The first term above is bounded by \pref{prop:dec_bilinear}, and we bound the estimation error term involving $\Dbi{\cdot}{\cdot}$ using an argument based on the elliptic potential.

<!-- chunk {"id": "body-0291", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We emphasize that the results here are specialized to bilinear classes, and require modifications to the basic framework in \pref{sec:framework}. Deriving tighter regret bounds as a direct corollary of our general results is an important topic for further research. To this end, we refer the reader to the follow-up work of, which provides a general approach to deriving model-free reinforcement learning guarantees through the \CompShort framework; see also discussion in \pref{sec:related}.

<!-- chunk {"id": "body-0292", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Lower Bounds} \label{sec:rl\_lower} We close this section by complementing our upper bounds on the \CompText with lower bounds. We first give a basic lower bound for bilinear classes, then give lower bounds for learning with linearly \subsubsection{Lower Bound for Bilinear Classes} The upper bounds for bilinear classes in \pref{thm:posterior\_bilinear,thm:igw\_bilinear} scale with $\frac{d}{\gamma}$, where $d$ is the bilinear dimension. The following result shows that this dependence is unavoidable.

<!-- chunk {"id": "body-0293", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proof}[\pfref{prop:mdp\_lower\_linear}] Immediate consequence of \pref{prop:bandit\_lower\_linear}.

<!-- chunk {"id": "body-0294", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Invoking this result within \pref{thm:lower\_main\_expectation} leads to a lower bound on regret of the form $\En\brk*{\RegDM}\geq\bigom(\sqrt{dT})$, which matches the upper bound in \pref{sec:rl\_bilinear\_basic} in terms of \subsubsection{Lower Bound for Linearly Realizable MDPs} Learning with \emph{linearly realizable} function approximation is a well-studied problem in reinforcement learning.

<!-- chunk {"id": "body-0295", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Here, we are given a feature map $\phi(s,a)\in\bbR^{d}$ satisfying $\nrm*{\phi(s,a)}_2\leq{}1$, and consider a class of value functions $\cQ=\cQ_1\times\cdots\times\cQ_H$ \label{eq:linearly realizable} \cQ\_h = \crl*{(s,a)\mapsto\tri*{\theta,\phi(s,a)}\mid{}\theta\in\bbR^{d},\nrm*{\theta}\_2\leq{}1}. We assume that $\cQ$ is realizable in the sense that it contains the optimal $Q$-function for all problem instances under consideration, which corresponds to choosing $\cM$ to be \cM\_{\cQ} = \crl*{ M \mid{} \Qmstar\_h\in\cQ\_h\;\forall{}h}.

<!-- chunk {"id": "body-0296", "role": "body", "section": "Paper Body", "weight": 1.0} -->

provide an exponential lower bound which establishes that sample-efficient reinforcement learning is not possible in this setting, and show that this lower bound continues to hold even when the instances under consideration have constant suboptimality gap. The following result shows that the \CompText is exponential for this setting, thereby recovering these results.

<!-- chunk {"id": "body-0297", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{restatable}[Lower bound for linearly realizable MDPs]{proposition}{linearlyrealizable} \label{prop:linear\_qstar} For all $d\geq{}2^{9}$ and $H\geq{}2$, there exists a family of linearly realizable MDPs $\cM$ with $\cR=\brk{-1,+1}$ such that for all $\gamma>0$, there exists $\Mbar\in\cM$ for which \label{eq:linear\_qstar} \comp(\cM\_{1/2}(\Mbar),\Mbar) \geq{} \frac{1}{48}\indic\crl*{\gamma\leq{}2^{-9}\min\crl{2^{H},\exp(2^{-10}d)}}.

<!-- chunk {"id": "body-0298", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Using \pref{thm:lower\_main} with $\gamma\propto{}T\log(T)$, we conclude that any algorithm for the linearly realizable setting must \RegDM \geq{} \bigomt\prn*{ \min\crl*{2^{H}, 2^{\bigom(d)}, T} with constant probability, which in turn implies that $\En\brk*{\RegDM} \geq{} \bigomt\prn*{ \min\crl*{2^{H}, 2^{\bigom(d)}, T} \subsubsection{Lower Bound for Linearly Realizable MDPs with Deterministic Dynamics and Gap} While \pref{prop:linear_qstar} shows that linear realizability is not sufficient for sample-efficient reinforcement learning, it is known that linear realizability \emph{does} suffice if one restricts to deterministic dynamics and rewards.

<!-- chunk {"id": "body-0299", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In particular, provide an algorithm for this setting that has \RegDM \leq \bigoh(dH) whenever the feature dimension is $d$ and $\sum_{h=1}^{H}r_h\in\brk{0,1}$.\footnote{See for generalizations to various types of nearly-deterministic systems.} The following result provides a complementary lower bound.

<!-- chunk {"id": "body-0300", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{restatable}[Lower bound for deterministic linearly realizable MDPs]{proposition}{deterministiclinear} \label{prop:mdp_gap_linear} There exists a collection $\cM$ of linearly realizable MDPs $\cM$ with $\cR=\brk{0,1}$, $H=1$, constant suboptimality gap, and deterministic rewards and dynamics, such that for all $\gamma>0$, there exists $\Mbar\in\cM$ \comp(\cMinf[1/3](\Mbar),\Mbar) \geq{} \frac{1}{12}\indic\crl*{ \gamma\leq\frac{d}{48} By \pref{thm:lower_main}, this result implies that any algorithm for the linearly realizable setting with deterministic dynamics and rewards must have \RegDM \geq{} \bigomt\prn*{ with constant probability, which in turn implies that

<!-- chunk {"id": "body-0301", "role": "body", "section": "Paper Body", "weight": 1.0} -->

$\En\brk*{\RegDM} \geq \bigomt\prn*{ \section{Incorporating Contextual Information} \label{sec:contextual} In this section we consider a \emph{contextual} variant of the \Framework framework in which the learner is given additional side information (in the form of a covariate or context) before each decision is made.

<!-- chunk {"id": "body-0302", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This setting encompasses the well-studied contextual bandit problem as well, as well as various contextual reinforcement learning problems. We show that the \mainalg paradigm seamlessly extends to incorporate contextual information, leading to new, efficient algorithms.

<!-- chunk {"id": "body-0303", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Setting} In the contextual \FrameworkShort framework, we adopt the following protocol for $T$ rounds, where for each round $t=1,\ldots,T$: \item Nature provides the learner with a \emph{context} $\con\ind{t}\in\Cspace$, where $\Cspace$ is the \emph{context space}. \item The \learner selects a decision $\act\ind{t}\in\Act$. \item Nature selects a reward $r\ind{t}\in\RewardSpace$ and observation $\obs\ind{t}\in\ObsSpace$ based on the decision, which are then observed by the learner. We allow each context $x\ind{t}$ to be chosen in an arbitrary, potentially adaptive fashion but---following the development so far---assume that rewards and observations are stochastic.

<!-- chunk {"id": "body-0304", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We work with models of the form $M(\cdot,\cdot)$, where $M(x,\act)$ denotes the distribution over $(r,\obs)$ when $x$ is the context and decision $\act$ is selected. We assume that at each timestep, given $x\ind{t}$, the pair $(r\ind{t}, \obs\ind{t})$ is drawn independently from an unknown model $\Mstar(x\ind{t}, \pi\ind{t})$. As before, we assume access to a class of models $\cM$ that contains the true \label{ass:realizability\_contextual} The model class $\cM$ contains the true model $\Mstar$.

<!-- chunk {"id": "body-0305", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For each model $M\in\cM$, let $\fm(\con,\act)\ldef{}\En_{r\sim{}M(\con,\act)}\brk*{r(\pi)}$ denote the mean reward function and let $\cpolm(x)\ldef{}\argmax_{\act\in\Act}\fm(\con,\act)$ denote the decision-making policy with the greatest expected reward under $M$.

<!-- chunk {"id": "body-0306", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Finally, we define $\cFm=\crl*{\fm\mid{}M\in\cM}$ as the induced class of mean reward functions.\footnote{We use the notation $\cpolm$ (compared to $\pim$ in the non-contextual setting) to distinguish \emph{decisions} from \emph{policies that map contexts to decisions}.} We evaluate the \learner's performance in terms of regret to the optimal decision-making policy for $\Mstar$: \ldef \sum\_{t=1}^{T}\En\_{\act\ind{t}\sim{}p\ind{t}}\brk*{\fstar(\con\ind{t},\cpolstar(\con\ind{t})) - \fstar(\con\ind{t},\act\ind{t})}, where we abbreviate $\fstar=\fmstar$ and $\cpolstar=\cpolm[\Mstar]$.

<!-- chunk {"id": "body-0307", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The advantage of this formulation---which generalizes similar formulations for the contextual bandit problem that we accommodate arbitrarily generated sequences of contexts, which may correspond to, e.g., users arriving at a website as they please. Note that the fully stochastic contextual bandit problem, in which $x\ind{1},\ldots,x\ind{T}$ are \iid, is a special case of the basic \FrameworkShort framework in \pref{sec:intro} (with policies as decisions), and does not require dedicated treatment.

<!-- chunk {"id": "body-0308", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{The Contextual \mainalgsection Algorithm} \begin{algorithm}[htp] \State \textbf{parameters}: \Statex Online estimation oracle $\AlgEst$. \Statex Exploration parameter $\gamma>0$. \Statex Divergence $\Dgen{\cdot}{\cdot}$. \State Receive context $x\ind{t}$. \State Compute estimate $\Mhat\ind{t} = \AlgEst\ind{t}\prn[\Big]{ \crl*{(x\ind{i}, \act\ind{i}, r\ind{i},\obs\ind{i})}_{i=1}^{t-1} }$.

<!-- chunk {"id": "body-0309", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\caption{Contextual \mainalg} \label{alg:contextual} \pref{alg:contextual} is a contextual generalization of the \mainalg meta-algorithm. The algorithm has the same structure as the basic (non-contextual) \mainalg algorithm (\optionone), with the main difference being that we use the context $x\ind{t}$ to form the minimax problem solved at each step. Following \pref{sec:general\_distance}, the algorithm is stated in terms of an arbitrary user-specified divergence $\Dgen{\cdot}{\cdot}$ for added flexibility.

<!-- chunk {"id": "body-0310", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In more detail, at each time $t$, the algorithm first receives the context $x\ind{t}$, then obtains an estimated model $\Mhat\ind{t}(\cdot,\cdot)$ from the estimation oracle $\AlgEst$; here, unlike the non-contextual setting, the oracle can make use of previous contexts to form the estimate.

<!-- chunk {"id": "body-0311", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Given the estimator and context, the algorithm solves the optimization problem \label{eq:opt\_contextual} p\ind{t}=\argmin\_{p\in\Delta(\Act)}\sup\_{M\in\cM}\En\_{\act\sim{}p}\brk*{\fm(\con\ind{t},\cpolm(\con\ind{t}))-\fm(\con\ind{t},\act) -\gamma\cdot\Dgen{M(\con\ind{t},\act)}{\Mhat\ind{t}(\con\ind{t},\act)}}, which corresponds to the non-contextual optimization problem \pref{eq:comp\_general} applied to the projected class $\cMx[\con\ind{t}]$, where \cMx[\con] \ldef{} \crl*{M(\con,\cdot)\mid{}M\in\cM}.

<!-- chunk {"id": "body-0312", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Finally, the algorithm samples $\act\ind{t}\sim{}p\ind{t}$ and updates the estimation oracle with the example $(x\ind{t},\act\ind{t},r\ind{t},\obs\ind{t})$. Notably, the per-round computational complexity is exactly the same as in the non-contextual setting.

<!-- chunk {"id": "body-0313", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Conceptually, \pref{alg:contextual} can be interpreted as a universal generalization of the \squarecb algorithm of from finite-action contextual bandits to arbitrary contextual decision making problems. Rather than using the inverse gap weighting strategy in \squarecb, which is tailored to contextual bandits with finite actions, we simply solve the optimization problem that defines the \CompText for the current context, thereby accommodating any learnable contextual decision making problem.

<!-- chunk {"id": "body-0314", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The performance guarantee for the contextual \mainalg algorithm depends on the estimation performance of the oracle $\AlgEst$ with respect to the divergence $D$, on the \emph{observed sequence of contexts}: \label{eq:general\_error} \EstCD \ldef{} \sum\_{t=1}^{T}\En\_{\act\ind{t}\sim{}p\ind{t}}\brk*{\Dgen{\Mstar(\con\ind{t},\act\ind{t})}{\Mhat\ind{t}(\con\ind{t},\act\ind{t})}}. Let $\cMhat$ be any set such that $\Mhat\ind{t}\in\cMhat$ for all $t$ almost surely, and recall that in the non-contextual setting, $\compgen(\cM,\cMhat)\ldef\sup_{\Mbar\in\cMhat}\compgen(\cM,\Mbar)$.

<!-- chunk {"id": "body-0315", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We have the following regret bound, generalizing \pref{thm:upper\_general\_distance}. \begin{restatable}{theorem}{uppercontextual} \label{thm:upper\_contextual} \pref{alg:contextual} with exploration parameter $\gamma>0$ guarantees \label{eq:upper\_contextual} \sup\_{x\in\cX}\compgen(\cMx,\cMhatx)\cdot{}T + \gamma\cdot\EstCD This result shows that any interactive decision making problem that is learnable in the non-contextual setting is also learnable in the presence of arbitrarily selected contexts, as long as estimation is \subsection{Application to Contextual Bandits} The contextual bandit problem is the most basic special case of the contextual \FrameworkShort setting, and corresponds to the case in which there are no auxiliary observations (i.e., $\Ospace=\NullObs$).

<!-- chunk {"id": "body-0316", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The contextual bandit problem with finite actions is quite well-studied but contextual bandits with continuous, structured action spaces are comparatively under-explored. As a consequence of the bounds on the \CompText from \pref{sec:bandit}, we show that \pref{alg:contextual} leads to efficient contextual algorithms for structured action spaces. For each of these examples, we take $\cMhat=\conv(\cM)$. \item \emph{Finite actions.} In the finite-action setting where $\Act=\brk{A}$, we $\sup_{x\in\cX}\compSq(\cMx,\cMhatx)\leq\frac{A}{\gamma}$, and this is achieved efficiently through the inverse gap weighting strategy (cf. \pref{prop:igw\_mab}).

<!-- chunk {"id": "body-0317", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In this case, \pref{alg:contextual} reduces to the \squarecb algorithm of \RegCDM \leq{} \bigoh\prn[\big]{\sqrt{AT\cdot\EstSq}} after tuning $\gamma$. For finite classes where $\abs{\cFm}<\infty$ and $\Rspace=\brk{0,1}$, this leads to $\RegCDM \leq \bigoh\prn[\big]{\sqrt{AT\log\abs{\cFm}}}$ for an appropriate choice of estimation oracle.

<!-- chunk {"id": "body-0318", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\item \emph{Linear action spaces.} Suppose actions are linearly structured in the sense that $\Act\subseteq\bbR^{d}$, and each $\fm\in\cFm$ factorizes as \fm(\con, \act)=\tri{\gm(\con),\act} for some $\gm:\Cspace\to\bbR^{d}$. Here, we can efficiently achieve $\sup_{x\in\cX}\compSq(\cMx,\cMhatx)\leq\frac{d}{\gamma}$ using the strategy from \pref{prop:bandit\_upper\_linear}. In this case, \pref{alg:contextual} provides an efficient algorithm with \RegCDM \leq{} \bigoht\prn[\big]{\sqrt{dT\cdot\EstSq}} after tuning $\gamma$. This recovers the result.

<!-- chunk {"id": "body-0319", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\item \emph{Continuous actions with concave rewards.} If $\Act\subseteq\bbR^{d}$ and the function $\act\mapsto\fm(\con,\act)$ is concave for all $\con\in\Cspace$ and $M\in\cM$, \pref{prop:bandit\_upper\_convex} implies that $\sup_{x\in\cX}\compSq(\cMx,\cMhatx)\leq\bigoht(\frac{\poly(d)}{\gamma})$, so that \pref{alg:contextual} enjoys \RegCDM \leq{} \bigoht\prn[\big]{\sqrt{\smash[t]{\poly(d)}T\cdot\EstSq}}. This yields the first oracle-efficient algorithm for contextual bandits with continuous actions and concave (resp.

<!-- chunk {"id": "body-0320", "role": "body", "section": "Paper Body", "weight": 1.0} -->

convex) rewards, though we emphasize that more research is required to understand when the optimization problem \pref{eq:opt\_contextual} can be solved efficiently for this setting.

<!-- chunk {"id": "body-0321", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Beyond these examples, the appeal of \pref{alg:contextual} is that it allows one to immediately translate any future bounds on the \CompText for structured bandit problems into oracle-efficient algorithms for contextual bandits with structured action spaces.

<!-- chunk {"id": "body-0322", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Application to Contextual Reinforcement Learning} Contextual reinforcement learning (sometimes referred to as the contextual MDP problem) is setting that generalizes both contextual bandits and reinforcement learning. At each time, the learner receives a context $x\ind{t}$, selects a policy $\act\ind{t}$, then executes the policy in an (unknown) finite-horizon MDP and observes a trajectory. Formally, this setting is simply a special case of the contextual \FrameworkShort framework in which $M(x,\cdot)$ is a finite-horizon MDP for all $M\in\cM$ and $x\in\cX$. Similar to the contextual bandit problem, the underlying MDP changes from round based on the context, so it is essential to---via modeling and function approximation---generalize across similar contexts.

<!-- chunk {"id": "body-0323", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Example: Contextual reinforcement learning with finite states and actions} The most basic and well-studied contextual reinforcement learning problem is the setting where, given the context $x$, each model $M(x,\cdot)$ is a finite state/action MDP with $\cS=\brk{S}$ and we can apply the \pcigw strategy (\pref{alg:policy\_cover\_igw}) which, via \pref{prop:igw\_tabular}, certifies that \sup\_{x\in\cX}\comp(\cMx,\cMhatx)\leq\bigoh\prn*{\frac{H^{3}SA}{\gamma}}, as long as $\cMhatx$ is a tabular MDP for all $x\in\cX$.

<!-- chunk {"id": "body-0324", "role": "body", "section": "Paper Body", "weight": 1.0} -->

With this choice, the contextual \mainalg algorithm guarantees that for any estimation oracle $\AlgEst$, \RegCDM \leq{} \bigoh\prn*{\sqrt{H^{3}SAT\cdot\EstSq}}, after tuning $\gamma$. This result is computationally efficient---beyond updating the estimation oracle, the only computational overhead at each round is to run the \pcigw algorithm with the estimated model---and constitutes the first universal reduction from contextual reinforcement learning to supervised online learning.

<!-- chunk {"id": "body-0325", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Note that while we require that each MDP has finite states and actions, we place no assumption on the context space $\Cspace$, and no assumption on how each model $x\mapsto{}M(x,\cdot)$ varies as a function of the context. In particular, one can leverage rich, flexible function approximation (e.g., neural networks or kernels) to learn the mapping from contexts to MDPs by simply choosing an appropriate estimation oracle $\AlgEst$. In constrast, previous approaches are limited to linear or generalized linear function approximation.

<!-- chunk {"id": "body-0326", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Additional Related Work and Follow-Up Work} \label{sec:related} We now highlight some relevant lines of research not already covered \subsection{Statistical Estimation} Our results build on a long line of work on minimax lower bounds for the seminal work of shows that for a large class of nonparametric estimation problems, the local (and in some cases, global) minimax rates are characterized by a local \emph{modulus of continuity} with respect to Hellinger distance, defined via: \label{eq:hellinger\_modulus} \omega\_{\veps}(\cM,\Mbar)\ldef{}\sup\_{M\in\cM}\crl*{ \nrm*{f^{\sss{M}}-f^{\sss{\Mbar}}}: \Dhels{M}{\Mbar}\leq\veps^{2} for an appropriate norm $\nrm{\cdot}$.

<!-- chunk {"id": "body-0327", "role": "body", "section": "Paper Body", "weight": 1.0} -->

An important special case concerns parametric models, where---under mild regularity conditions---the modulus of continuity \pref{eq:hellinger\_modulus} asymptotically coincides with the One can view the \CompText \pref{eq:comp} as an interactive decision making analogue of the modulus of continuity.

<!-- chunk {"id": "body-0328", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To make the connection more apparent, consider a regularized (as opposed to constrained) variant of \pref{eq:hellinger\_modulus}: \label{eq:hellinger\_modulus2} \omega\_{\gamma}(\cM,\Mbar)\ldef{}\sup\_{M\in\cM}\crl*{ \nrm*{f^{\sss{M}}-f^{\sss{\Mbar}}} - \gamma\cdot\Dhels{M}{\Mbar} Like the \CompText, the modulus of continuity \pref{eq:hellinger\_modulus2} captures a worst-case tradeoff between risk and information gain relative to a reference model $\Mbar$, with the scale parameter $\gamma>0$ controlling the tradeoff.

<!-- chunk {"id": "body-0329", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The key difference is that because the classical estimation setting is purely passive, the modulus of continuity \pref{eq:hellinger\_modulus2} does not involve decisions made by the learner, and hence is expressed as a ``max'' rather than a ``min-max''.

<!-- chunk {"id": "body-0330", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Instance-Dependent Complexity for Structured Bandits} An important special case of our general decision making framework is the problem of structured bandits with large action spaces (\pref{sec:bandit}). The pioneering work of gives a characterization for the optimal asymptotic instance-dependent rates for this problem, as well as a broader class of problems called \emph{controlled Markov chains}.

<!-- chunk {"id": "body-0331", "role": "body", "section": "Paper Body", "weight": 1.0} -->

show that for every problem instance $\Mstar$, any ``uniformly consistent'' algorithm must incur regret $(1-o)\cdot{}\glcomp(\cM,\Mstar)\log(T)$ asymptotically, and that regret $(1+o)\cdot{}\glcomp(\cM,\Mstar)\log(T)$ is asymptotically more recent line of work attempts to achieve this fundamental limit extends these results to the reinforcement learning setting under strong ergodicity assumptions.

<!-- chunk {"id": "body-0332", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The Graves-Lai complexity measure \pref{eq:graves\_lai} has evident structural similarities to the \CompText, which can be made especially clear by considering the following regularized variant: \label{eq:graves\_lai2} \glcomp\_{\gamma}(\cM,\Mbar) \ldef{} \inf\_{w\in\bbR^{\Act}\_{+}}\sup\_{M\in\cC(\cM,\Mbar)}\crl*{ \sum\_{\act\in\Act}w\_{\act}(\fmbar(\pimbar)-\fmbar(\act)) - \gamma\cdot{}\prn*{\sum\_{\act\in\Act}w\_{\act}\kl{\Mbar(\pi)}{M(\pi)}- Note that $w\in\bbR^{\Act}_{+}$ may be interpreted as an unnormalized distribution over decisions.

<!-- chunk {"id": "body-0333", "role": "body", "section": "Paper Body", "weight": 1.0} -->

With this perspective, the most important difference between this complexity measure and the \CompText is that \pref{eq:graves\_lai2} only considers regret under the nominal model $\Mbar$, while the \CompShort considers regret under a worst-case model selected by nature. We believe this difference is a fundamental consequence of considering minimax regret under finite samples rather than asymptotic instance-dependent regret. In particular, all existing results that provide finite-sample guarantees based on the Graves-Lai complexity require strong assumptions on the problem structure (e.g., finite actions) in order to control the error incurred by evaluating \pref{eq:graves\_lai} with a plug-in estimator for the true model $\Mstar$. This highlights that \pref{eq:graves\_lai} alone is not be sufficient to capture optimal instance-dependent guarantees with finite samples. In contrast, we avoid similar assumptions because the \CompShort incorporates uncertainty in a stronger fashion. We refer to the follow-up work of discussion and background.

<!-- chunk {"id": "body-0334", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Posterior Sampling and the Information Ratio} For structured bandits in the Bayesian framework, introduce a parameter measure known as the \emph{information ratio} which bounds the Bayesian regret for posterior sampling and a related strategy called information-directed sampling. For a given distribution $\mu\in\Delta(\cM)$ (typically the posterior distribution at a given round), estimator $\Mbar$, and action distribution $p$, the information ratio is given by \frac{\prn*{\En\_{\act\sim{}p}\En\_{M\sim\mu}\brk*{\fm(\act)-\fm(\pim)}}^2}{ \En\_{\act\sim{}p}\En\_{M\sim\mu}\brk*{\Dkl{M(\act)}{\Mbar(\act)}}}.

<!-- chunk {"id": "body-0335", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Note that we consider the original definition, which uses KL divergence, but the concept of information ratio readily extends to other divergences such as Hellinger distance (a-la \pref{sec:general\_distance}). show that when the distribution $p$ is chosen sampling (i.e., sample $M'\sim\mu$ and follow $\pi\subs{M'}$), the information ratio is bounded by $\ActSize$ for finite-armed bandits; similar bounds hold for linear bandits.

<!-- chunk {"id": "body-0336", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To relate these concepts and techniques to our own results, we consider a natural ``worst-case'' complexity measure for the Bayesian setting based on the information ratio: \label{eq:information\_ratio\_bayes} \InfB(\cM,\Mbar) = \max\_{\mu\in\Delta(\cM)}\min\_{p\in\Delta(\Act)}\frac{\prn*{\En\_{\act\sim{}p}\En\_{M\sim\mu}\brk*{\fm(\act)-\fm(\pim)}}^2}{ \En\_{\act\sim{}p}\En\_{M\sim\mu}\brk*{\Dkl{M(\act)}{\Mbar(\act)}}}. We show that boundedness of this parameter implies boundedness of the KL divergence variant of the \CompText.

<!-- chunk {"id": "body-0337", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{restatable}{proposition}{informationratiodec} \label{prop:information\_ratio\_bound} For all $\Mbar\in\cM$ and $\gamma>0$, \compKLdual(\cM,\Mbar) \leq{} \frac{\InfB(\cM,\Mbar)}{4\gamma}. $\InfB(\cM)=\sup_{\Mbar\in\cM}\InfB(\cM,\Mbar)$, the results of imply that information-directed sampling attains $\bigoh\prn[\big]{\sqrt{\InfB(\conv(\cM))\cdot{}T\log\ActSize}}$.

<!-- chunk {"id": "body-0338", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The proof of \pref{prop:information\_ratio\_bound} shows that the information ratio and the \CompShort are closely related, and suggests that the information ratio might be thought of as a parameter-free analogue of the dual Bayesian \CompShort.

<!-- chunk {"id": "body-0339", "role": "body", "section": "Paper Body", "weight": 1.0} -->

However, the following proposition shows that in general, the information ratio can be arbitrarily large compared to \begin{restatable}{proposition}{informationratiobayes} \label{prop:information\_ratio\_bayes\_lower} Consider the Lipschitz bandit problem in which $\Act=\brk*{0,1}^{d}$, $\cFm=\crl[\big]{f:\brk*{0,1}^{d}\to\brk*{0,1} \mid{} \abs{f(x)-f(y)}\leq{}\nrm{x-y}_{\infty}}$, $\Obs=\NullObs$, and $\cM=\crl[\big]{\act\mapsto\cN(f(\act),1)\mid{}f\in\cFm}$.

<!-- chunk {"id": "body-0340", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For this setting, the information ratio is infinite for all $d\geq{}1$: On the other hand, we have $\comp(\cM)\leq\bigoht(\gamma^{-\frac{1}{d+1}})$, and consequently \pref{thm:upper\_main\_bayes} recovers the optimal regret bound $\En\brk*{\RegDM}\leq{}\bigoht(T^{\frac{d+1}{d+2}})$. This result continues to hold if the KL divergence in $\InfB(\cM)$ is replaced by squared error, TV distance, or Hellinger distance. The proof of the result indicates that ratios---which inherently suffer from boundedness issues and numerical instability---may not lead to fundamental complexity measures.

<!-- chunk {"id": "body-0341", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We note that in spite of this limitation, the information ratio was an important influence on the present work.% Beyond the issues highlighted above, the information ratio is tied to the Bayesian bandit setting, and does not immediately yield algorithms for the frequentist setting that is the focus of this paper. To address this issue, one might consider the following \InfF(\cM,\Mbar)\ldef{}\min\_{p\in\Delta(\Act)}\max\_{\mu\in\Delta(\cM)}\frac{\prn*{\En\_{\act\sim{}p}\En\_{M\sim\mu}\brk*{\fm(\act)-\fm(\pim)}}^2}{ \En\_{\act\sim{}p}\En\_{M\sim\mu}\brk*{\Dkl{M(\act)}{\Mbar(\act)}}}.

<!-- chunk {"id": "body-0342", "role": "body", "section": "Paper Body", "weight": 1.0} -->

While it always holds that \InfB(\cM,\Mbar) \leq \InfF(\cM,\Mbar), we show that this inequality is strict in general: even for the multi-armed bandit, the frequentist information ratio $\InfF(\cM,\Mbar)$ can be arbitrarily large compared to the \begin{restatable}{proposition}{informationratiofreq} \label{prop:information\_ratio\_separation} Consider the multi-armed bandit setting with $\Act=\brk{A}$ and $\cM=\crl[\big]{M(\act)\ldef{}\cN(f(\act),1/2): f\in\brk*{0,1}^{A}}$.

<!-- chunk {"id": "body-0343", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For any $\Mbar\in\cM$ for which $\fmbar\in\mathrm{int}(\brk{0,1}^{A})$ and $\min_{\act\neq\pimbar}\crl{\fmbar(\act)-\fmbar(\pimbar)}>0$, we have \InfF(\cM,\Mbar)=+\infty. On the other hand, this example has $\comp(\cM)\leq{}\InfB(\cM)\leq\bigoh\prn*{A/\gamma}$ for all $\gamma>0$. This result should be contrasted with the situation for the \CompShort, where the ``min-max'' and ``max-min'' variants coincide under mild regularity conditions (cf. \pref{sec:dual}).

<!-- chunk {"id": "body-0344", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Further results} works have generalized their information-theoretic approach to provide minimax regret bounds for various settings, including bandit convex optimization and parallel, a line of work develops \emph{frequentist} regret bounds for structured bandits and partial monitoring based on an elegant algorithm design principle known as \emph{exploration-by-optimization}. Notably, ``parameterized'' form of the information ratio which can overcome the obvious pathologies highlighted in the prequel, and shows that this quantity acts as a lower bound on the minimax rate for general partial monitoring problems in an adversarial setting.\footnote{\dfedit{The lower bounds in are loose by $\poly(\abs{\Pi})$ factors, and hence cannot meaningfully reflect dependence on problem-dependent parameters in the same fashion as our results.}} Follow-up work of shows that the parameterized information ratio coincides with the ``convexified'' \CompText given by $\comp(\conv(\cM))$, and hence can only give tight guarantees for convex classes, not for general models.

<!-- chunk {"id": "body-0345", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We mention in passing the works of give frequentist algorithms inspired by information-directed sampling and the information ratio. These works rely on notions of information gain tailored to linear function approximation, and it is not clear whether they extend to more general settings.

<!-- chunk {"id": "body-0346", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Additional Follow-Up Work} We close this section by highlighting relevant related work published in the time since the initial arXiv preprint of this paper became available.

<!-- chunk {"id": "body-0347", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Tighter guarantees based on the \CompShort} The follow-up work of provides guarantees that improve upon our main upper and lower bounds by working with a constrained variant of the \CompShort.

<!-- chunk {"id": "body-0348", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Working with this variant of the \CompShort allows one to remove all but one of the gaps discussed sec:main\_discussion: the lower bounds 1) hold in expectation, and 2) allow the reference to belong to $\conv(\cM)$, while the upper bounds enjoy a localization radius that matches the lower bound. To our knowledge, this work offers the only subsequent improvement to our core results. For the special case of reinforcement learning, give model-free guarantees that improve upon those in sec:rl by combining the \CompText with a technique known as \emph{optimistic estimation}; see \paragraph{Generalizations of the \CompShort framework} A number of follow-up works generalize the \CompText, as well as our upper and lower bound techniques, to more general settings, including 1) PAC decision making, 2) decision making with adversarial outcomes, and 3) multi-agent decision making.

<!-- chunk {"id": "body-0349", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Optimistic estimation and posterior sampling} Concurrent work of provides frequentist regret bounds for contextual bandits and linearly-structured reinforcement learning settings based on a posterior sampling-like algorithm referred to as \emph{Feel-Good Thompson Sampling}. This approach makes use of randomized online estimation algorithms in the vein of eq:general\_error, but augments the estimation objective with a ``feel-good'' bonus that biases the estimator toward over-estimating the optimal value (we refer to this technique as \emph{optimistic estimation}). When combined with posterior sampling, optimistic estimation leads to frequentist regret bounds that match other well-known approaches. A number of subsequent works extend this approach to more general reinforcement learning settings also using posterior sampling as the exploration mechanism. Subsequent work of highlights that for general decision making settings, posterior sampling may lead to arbitrary sub-optimal guarantees, and hence the complexity measures studied in these works do not lead to lower bounds on optimal regret for the general settings considered in this paper.

<!-- chunk {"id": "body-0350", "role": "body", "section": "Paper Body", "weight": 1.0} -->

However, show that the optimistic estimation principle can be combined with the \CompText (acting as a more general mechanism for exploration), leading to guarantees for model-free reinforcement learning that improve upon those in sec:rl; we refer to this work for additional discussion and background.

<!-- chunk {"id": "body-0351", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Further general-purpose complexity measures} Since the initial preprint of this paper became available, a number of subsequent works have proposed other complexity measures that lead to upper bounds on sample complexity for general reinforcement learning settings. Compared to the \CompText, these complexity measures are sufficient but not \emph{necessary} for low sample complexity, and do not lead to lower bounds in general. As such, they are best thought of as further generalizations of other sufficient conditions such as Bellman Rank and Bellman-Eluder dimension.

<!-- chunk {"id": "body-0352", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{sec:discussion} We have developed a theory of learnability and unified algorithm design principle for reinforcement learning and interactive decision making. Our results provide a solid foundation on which to build the theory of data-driven decision making going forward, and we are excited about many directions for future research. \item \emph{Computation.} While \mainalg{} provides a unified algorithm design principle for decision making, we have mainly focused on statistical rather than computational aspects of the algorithm in this paper, outside of special cases. Going forward, we intend to fully explore when and how the algorithm can be implemented efficiently, which we believe to have strong practical implications.

<!-- chunk {"id": "body-0353", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\item \emph{Beyond reinforcement learning.} The examples in this paper focus on bandits and reinforcement learning, but the \FrameworkShort{} framework is substantially more general, and encompasses rich settings such as POMDPs. It remains to fully understand the implications of our results for these settings. Beyond these questions, we anticipate many natural extensions to our framework and results, including adaptive or instance-dependent guarantees, and incorporating constraints such as safety.

<!-- chunk {"id": "body-0354", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We close by mentioning some technical questions. First, while our upper bounds generally achieve polynomial sample complexity whenever this is achievable, more work is required to understand to what extent the estimation complexity in our bounds can be tightened or removed, and to achieve the sharpest possible guarantees. Second, a natural question is whether our algorithmic results can be extended to support offline oracles for estimation, in the same vein We thank Ayush Sekhari and Karthik Sridharan for helpful discussions, and thank Zak Mhammedi for useful comments and feedback. AR acknowledges support from the ONR through awards N00014-20-1-2336 and N00014-20-1-2394, from the NSF through award DMS-2031883, and from the ARO through award W911NF-21-1-0328.

<!-- chunk {"id": "body-0355", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Technical Tools} \label{app:technical} In this section of the appendix we provide a collection of basic technical results used throughout the paper: Tail bounds for sequences of random variables (\pref{app:tail}), inequalities for information-theoretic divergences (\pref{app:information}), and regret bounds for online learning (\pref{app:online}).

<!-- chunk {"id": "body-0356", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{lemma}[Lemma 4 of \protect\footnote{This result is stated in in terms of densities, but the variant here is an immediate consequence.}] \label{lem:kl\_hellinger} Let $\bbP$ and $\bbQ$ be probability distributions over a measurable space $\sup_{F\in\filt}\frac{\bbP(F)}{\bbQ(F)}\leq{}V$, then \Dkl{\bbP}{\bbQ}\leq{}(2+\log(V))\Dhels{\bbP}{\bbQ}.

<!-- chunk {"id": "body-0357", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Next, we state a ``multiplicative'' variant of Pinsker's inequality, which provides faster rates at the cost of multiplicative rather than additive error.

<!-- chunk {"id": "body-0358", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The inequality in \pref{eq:mp\_min} follows by applying the AM-GM inequality to \pref{eq:mp\_min\_sqrt} and rearranging.

<!-- chunk {"id": "body-0359", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Finally, we provide an approximate chain rule-type inequality for the squared Hellinger distance, which allows the distance between two joint distributions to be decomposed into a sum of distances between conditional distributions.

<!-- chunk {"id": "body-0360", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Online Learning} \label{app:online} \newcommand{\Xsig}{\mathscr{X}} \newcommand{\Ysig}{\mathscr{Y}} \newcommand{\Xpair}{(\Xspace,\Xsig)} \newcommand{\Ypair}{(\Yspace,\Ysig)} \newcommand{\Kclass}{\cK(\Xspace,\Yspace)} \newcommand{\gstar}{g\_{\star}} \newcommand{\istar}{i^{\star}} \newcommand{\jstar}{j^{\star}} \newcommand{\hstar}{h\_{\jstar}} \newcommand{\indt}{\indic\_t} In this section, we provide results for online learning in a conditional density estimation setting. The setup is as follows.

<!-- chunk {"id": "body-0361", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Let $\Xpair$ be the \emph{covariate/context space} and $\Ypair$ be the \emph{outcome space}. Let $\dom$ be an unnormalized kernel from $\Xpair$ to $\Ypair$ (i.e., for every $A\in\Ysig$, $x\mapsto{}\nu(A\mid{}x)$ is $\Xsig$-measurable, and for all $x\in\Xspace$, $\nu(\cdot\mid{}x)$ is a $\sigma$-finite measure; cf. \pref{sec:prelims}), and let $\Kclass$ denote the collection of all regular conditional densities with respect to $\dom$. That is, each $g\in\Kclass$ is a jointly measurable map $g:\Xspace\times\Yspace\to\bbR_{+}$ such that is a probability density with respect to $\dom(\cdot\mid{}x)$.

<!-- chunk {"id": "body-0362", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Online Learning, Regret, and Estimation Error} We consider the following online learning process: For $t=1,\ldots,T$: \item Learner predicts $\ghat\ind{t}\in\Kclass$. \item Nature reveals $x\ind{t}\in\Xspace$ and $y\ind{t}\in\Yspace$ and learner suffers loss \logloss\ind{t}(\ghat\ind{t})\ldef{}\log\prn*{ \frac{1}{\ghat\ind{t}(y\ind{t}\mid{}x\ind{t})} Define $\hist\ind{t}=(x\ind{1},y\ind{1}),\ldots,(x\ind{t},y\ind{t})$ and let $\filt\ind{t}=\sigma(\hist\ind{t})$. Let $\Iset$ be an abstract ``index'' set.

<!-- chunk {"id": "body-0363", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We consider a so-called \emph{expert setting} in which we are given a class of history-dependent functions \cG=\crl*{g\_{\idx}}\_{\idx\in\Iset}, where each ``expert'' $g_{\idx} = (g_{\idx}\ind{1},\ldots,g\ind{T}_{\idx})$ is a sequence of functions of the form g\_{\idx}\ind{t}(\cdot\mid\cdot\midsem \hist\ind{t-1})\in\Kclass. Each such function can be thought of as a conditional density that becomes known to the learner after observing the history $\hist\ind{t-1}$ (i.e., at the beginning of round $t$).

<!-- chunk {"id": "body-0364", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We occasionally overload the density $g_i\ind{t}(x)\equiv{}g_i\ind{t}(\cdot\mid{}x)$ with its induced We define regret to the expert class $\cG$ via \RegLog = \sum\_{t=1}^{T}\logloss\ind{t}(\ghat\ind{t}) - \inf\_{\idx\in\Iset}\sum\_{t=1}^{T}\logloss\ind{t}(g\ind{t}\_{\idx}). For the main results in this section, we make the following realizability assumption.

<!-- chunk {"id": "body-0365", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The following lemma shows that minimizing the log-loss regret \pref{eq:regret\_ol} suffices to minimize the Hellinger estimation error. \label{lem:logloss\_hellinger\_ol} For any estimation algorithm, whenever \pref{ass:realizability\_ol} holds, \label{eq:logloss\_hellinger\_ol1} \En\brk*{\EstHel} \leq{} \En\brk*{\RegLog}. Furthermore, for any $\delta\in$, with probability at least $1-\delta$, \label{eq:logloss\_hellinger\_ol2} \EstHel \leq{} \RegLog + 2\log(\delta^{-1}). Finally, consider a sequence of $\crl*{0,1}$-valued random variables $(\indt)_{t\leq{}T}$, where $\indt$ is $\filt\ind{t-1}$-measurable.

<!-- chunk {"id": "body-0366", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consequently, we have $\En\brk*{\EstHel}\leq{}\log\abs{\cG}$ and $\EstHel \leq{} \log\abs{\cG} + 2\log(\delta^{-1})$ with probability at \subsubsection{Infinite Classes} We now provide results for infinite expert classes based on covering \label{def:g\_cover} We say that $\Jset\subseteq\Iset$ is an $\veps$-cover for $\cG$ if \forall{}\idx\in\Iset\quad\exists{}\jdx\in\Jset\quad\text{s.t.}\quad

<!-- chunk {"id": "body-0367", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We let $\cN(\cG,\veps)$ denote the size of the smallest such cover and define \GComp \ldef \inf\_{\veps\geq{}0}\crl*{ \log\cN(\cG,\veps)+\veps^{2}T as an associated complexity parameter.

<!-- chunk {"id": "body-0368", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{lem:vovk\_infinite\_fast} Suppose \pref{ass:finite\_measure\_ol} holds. Then the algorithm above, with an appropriate setting for $\alpha$ and $\veps$, guarantees that \label{eq:vovk\_infinite\_fast\_expectation} \leq{}34\cdot{}\inf\_{\veps>0}\crl*{\Bconst{}\cdot\veps^{2}T + \log\cN(\cG,\veps)} = \bigoh(\Bconst\cdot{}\GComp), where $\Bconst\ldef{}\log(2B^2T)$. Furthermore, the algorithm satisfies $\ghat\ind{t}\in\conv(\cG\ind{t})$.

<!-- chunk {"id": "body-0369", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\newcommand{\cGcheck}{\check{\cG}} \renewcommand{\hbar}{\bar{h}} \newcommand{\gbar}{\bar{g}} We now add an additional twist to the setting in considered in the prequel At each timestep $t$, we receive a subset $\Iset\ind{t}\subseteq\Iset$, which is a measurable function of $\hist\ind{t-1}$, and we are required to respect the constraint that $\ghat\ind{t}\in\conv\prn*{\crl{g\ind{t}_{\idx}}_{\idx\in\Iset}}$.

<!-- chunk {"id": "body-0370", "role": "body", "section": "Paper Body", "weight": 1.0} -->

$\Iset\ind{t}$ may be thought of as a set of ``available'' experts. In particular, we use the results in this section to prove \pref{thm:upper\_main}, where $\cI\ind{t}$ corresponds to a subset of models in a confidence set constructed based on the data observed so far. Here, satisfying the $\ghat\ind{t}\in\conv\prn*{\crl{g\ind{t}_{\idx}}_{\idx\in\Iset}}$ allows us to appeal to the regret bound in Eq. \pref{eq:upper\_general3} of \pref{thm:upper\_general}. in the previous section, we give a result for arbitrary, infinite expert classes based on covering numbers. We give algorithm that builds on the algorithm for infinite classes in \pref{lem:vovk\_infinite\_fast}, but incorporates tricks from the \emph{sleeping experts} literature.

<!-- chunk {"id": "body-0371", "role": "body", "section": "Paper Body", "weight": 1.0} -->

With parameters $\veps>0$, $\alpha\in$, we proceed as follows: \item Let $\Jset\subseteq\Iset$ witness the covering number $\cN(\cG,\veps)$. Let $\cov:\Iset\to\Jset$ be any function that maps an index $i\in\Iset$ to a covering element $\cov(i)$ such that $\Dhels{g\ind{t}_{\idx}(x;\hist\ind{t-1})}{g\ind{t}_{\cov(\idx)}(x;\hist\ind{t-1})}\leq{}\veps^{2}$ for all $x$, $\hist\ind{t-1}$.

<!-- chunk {"id": "body-0372", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Furthermore, since $\Iset\ind{t}$ is a measurable function of $\hist\ind{t-1}$, the $\cGcheck=\crl*{\gcheck\ind{t}_j}_{j\in\cJ}$ is itself a valid time-varying expert class.

<!-- chunk {"id": "body-0373", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\item For each $j\in\Jset$, define $h\ind{t}_j(y\mid{}x)=(1-\alpha)\gcheck\ind{t}_j(y\mid{}x) + \item Let $q\ind{t}$ denote the distribution produced by running the aggregating algorithm on the expert class $\crl*{\hbar\ind{t}_j}_{j\in\Jset}$, which we define inductively \item $q\ind{t}(j) \propto \exp\prn*{ -\sum\_{i=1}^{t-1}\logloss\ind{t}(\hbar\ind{i}) \item Define $\qbar\ind{t}(j) \ldef

<!-- chunk {"id": "body-0374", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{\CompText: Structural Results} \label{app:structural} \newcommand{\fmp}{f\sups{M'}} \newcommand{\fmbarp}{f\sups{\Mbar'}} \newcommand{\fmnot}{f\sups{M\_0}} In this section we provide conditions under which one can lower bound the localized \CompText by the global version.

<!-- chunk {"id": "body-0375", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Next, we prove a stronger local-to-global lemma from a \emph{structured Gaussian bandit} setting in which there are no observations (i.e., $\Ospace=\NullObs$), and rewards are Gaussian in the sense that $M(\act)= \cN(\fm(\act), \sigma^2)$ for all $M\in\cM$. We place no assumption on structure of the mean reward function class itself.

<!-- chunk {"id": "body-0376", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For most of the applications considered in this paper, $\comp(\cM)\propto\frac{C}{\gamma}$, where $C$ is a problem-dependent parameter such as dimension. In this case, the dependence on $\veps$ on the right-hand side of \pref{eq:local\_to\_global\_gaussian} vanishes, and we are left with \sup\_{\Mbar\in\cM}\comp(\cM\_{\veps}(\Mbar),\Mbar) \geq{} \frac{1}{4e}\cdot\sup\_{\Mbar\in\cM}\comp[\gamma](\cM,\Mbar).

<!-- chunk {"id": "body-0377", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\newcommand{\klfg}{\Dhels{\PM}{\PMbar}} \newcommand{\Pfdot}{\PMbar(\cdot)} \newcommand{\Pgdot}{\PM(\cdot)} \begin{proof}[\pfref{thm:lower\_main}]We will prove the following slightly more refined result: For any $\gamma>\sqrt{\Ct{}T}$ and nominal model $\Mbar\in\cM$ and any algorithm, there exists a model $M\in\cMloc[\vepslowg{}](\Mbar)$ such that \label{eq:lower\_main\_local} (6\Ct)^{-1}\cdot\min\crl[\bigg]{\prn*{\comp(\cMloc[\vepslowg{}](\Mbar),\Mbar)-15\delta}\cdot{}T, \gamma} with probability at least $\delta/2$.

<!-- chunk {"id": "body-0378", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The result in \pref{eq:lower\_main} is an Let $T\in\bbN$ be fixed, and let $\veps=c_1\frac{\gamma}{T}$, where $c_1$ is a free parameter to be specified later. Let $\gamma\geq{}\sqrt{T}/c_2$ be given, where $c_2$ is another free parameter.

<!-- chunk {"id": "body-0379", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider a fixed algorithm $p = \crl*{p\ind{t}(\cdot\mid\cdot)}_{t=1}^{T}$. Recall that $\Prm{M}{p}$ is the law of $\hist\ind{T}$ when $M$ is the underlying model and $p$ is the algorithm. We abbreviate this to $\bbP\sups{M}$, and let $\Em\brk*{\cdot}$ denote the corresponding expectation.

<!-- chunk {"id": "body-0380", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Since $\pmbar\in\Delta(\Act)$, the definition of $\comp(\cMloc[\veps](\Mbar),\Mbar)$ guarantees that \sup\_{M\in\cM\_{\veps}(\Mbar)} \En\_{\act\sim\pmbar}\brk*{\fm(\pim) - \fm(\act) -\gamma\cdot\Dhels{M(\act)}{\Mbar(\act)}} \geq{} \comp(\cMloc[\veps](\Mbar),\Mbar). Let $M\in\cMloc[\veps](\Mbar)$ attain the supremum above.\footnote{If the supremum is not attained, one can consider a limit sequence.

<!-- chunk {"id": "body-0381", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We omit the details.} Then, rearranging, we have \En\_{\act\sim\pmbar}\brk*{\fm(\pim) - \fm(\act)} \geq{} \gamma\cdot \En\_{\act\sim\pmbar}\brk*{\Dhels{M(\act)}{\Mbar(\act)}} + \comp(\cMloc[\veps](\Mbar),\Mbar). \label{eq:lower\_basic} For the remainder of the proof, we abbreviate $\comp{}\equiv\comp{}(\cM_{\veps}(\Mbar),\Mbar)$.

<!-- chunk {"id": "body-0382", "role": "body", "section": "Paper Body", "weight": 1.0} -->

With this notation, we can rewrite \pref{eq:lower\_basic} as \Embar\brk*{\delm} \geq{} \gamma\cdot \Embar\brk*{\En\_{\act\sim\phat}\brk*{\Dhels{M(\act)}{\Mbar(\act)}}} \label{eq:minimax\_g\_aux} Let $c_3>0$ be a final free parameter. We consider two cases. First, if either $\PM(\delm>c_3\frac{\gamma}{T})>\delta$ or $\PMbar(\delmbar>c_3\frac{\gamma}{T})>\delta$, the main result is implied whenever $c_3$ is sufficiently large, since $\delm$ is equal in law to $\frac{1}{T}\RegDM$ when $M$ is the underlying problem instance.

<!-- chunk {"id": "body-0383", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The strategy for the remainder of the proof is as follows. Given the assumption that $\PMbar\brk{\cEmbar},\PM\brk{\cEm}\geq{}1-\delta$, we will prove a lower bound on the regret for model $M$ in terms of $\comp$, using the lower bound in \pref{eq:minimax\_g\_aux} as a starting point. The main challenge is to relate the quantity $\Embar\brk{\delm}$ on the left-hand side of \pref{eq:minimax\_g\_aux} to the quantity $\Em\brk{\delm}$, which corresponds to regret when actions are selected under the law induced by $M$. We address this issue using change of measure arguments, which take advantage of the localization property and the assumption that $\PMbar\brk{\cEmbar},\PM\brk{\cEm}\geq{}1-\delta$.

<!-- chunk {"id": "body-0384", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Proof of \pref{thm:lower\_main\_expectation}} \begin{proof}[\pfref{thm:lower\_main\_expectation}]% \newcommand{\Epim}{\En\_{\pi\sim\pm}}% \newcommand{\Epimbar}{\En\_{\pi\sim\pmbar}}% This proof follows the same structure as \pref{thm:lower\_main}, with the main difference being that the stronger notion of localization allows for a stronger (as well as simpler) change of measure argument.

<!-- chunk {"id": "body-0385", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Applying \pref{lem:localization\_simple} and simplifying for the respective values for $R$ yields both theorems.

<!-- chunk {"id": "body-0386", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\caption{\mainalgB for Infinite Classes} \label{alg:main\_bayes} \begin{proof}[\pfref{thm:upper\_main\_bayes}] Per the discussion in \pref{sec:minimax\_swap}, it suffices to prove the regret bound for the Bayesian setting in which $\Mstar\sim\mu$, where $\mu\in\Delta(\cM)$ is a known prior.

<!-- chunk {"id": "body-0387", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We will show that the regret bound on the right-hand side of \pref{eq:upper\_main\_bayes} holds uniformly for all choices of prior: \label{eq:upper\_main\_bayes\_quant} \En\_{\Mstar\sim\mu}\En\sups{\Mstar}\brk*{\RegDM} \leq{} 2\cdot\min\_{\gamma>0}\max\crl*{\comp(\conv(\cM))\cdot{}T,\;\; \inf\_{\veps\geq{}0}\crl*{\gamma\cdot\log\ActCov +\veps\cdot{}T}}. This implies that the there exists an algorithm with the same regret bound for the frequentist setting whenever the conclusion of \pref{prop:minimax\_swap} holds.

<!-- chunk {"id": "body-0388", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Going forward, we use $\En\brk*{\cdot}$ to denote expectation with respect to the joint law over $(\Mstar,\hist\ind{T})$ when $\Mstar\sim\mu$.

<!-- chunk {"id": "body-0389", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We consider the Bayesian variant of \mainalg described in \pref{alg:main\_bayes}. The algorithm begins by building with a cover $\Rho$ that witnesses the covering number $\ActCov$. Let $\cov:\Pim\to\Rho$ be any fixed map that takes $\pi\in\Pim$ to a corresponding $\veps$-covering element in $\Rho$ (in the sense of \pref{eq:action\_cover}). We let $\rhostar\ldef\cov(\pimstar)$ denote the covering element for the optimal decision $\pimstar$, which is a random variable.

<!-- chunk {"id": "body-0390", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Proofs for Learnability Results} \begin{proof}[Proof of \pref{thm:learnability\_main} and \pref{thm:learnability\_main\_bayes}] The proofs for \pref{thm:learnability\_main} and \pref{thm:learnability\_main\_bayes} differ only in how we derive the upper bound on regret.

<!-- chunk {"id": "body-0391", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Proofs from \preft{sec:algorithm}} \label{app:algorithm} \subsection{Proofs from \preft{sec:oracle}} In this section we prove \pref{thm:upper\_general}. We prove the localized regret bound \pref{eq:upper\_general3} in \pref{thm:upper\_general} under the following, slightly more general, version of \pref{ass:hellinger\_oracle}, which will be useful for applications.

<!-- chunk {"id": "body-0392", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{ass:hellinger\_oracle\_generalized} The online estimation algorithm $\AlgEst$ guarantees that for a given $\delta\in$, with probability at least \sum\_{t=1}^{T}\En\_{\act\ind{t}\sim{}p\ind{t}}\brk*{\Dhels{\Mstar(\actt)}{\Mhat\ind{t}(\actt)}}\indic\crl{\Mstar\in\cM\ind{t}} \leq{} \EstProbHelT,\label{eq:hellinger\_oracle\_generalized} where $\EstProbHelT$ is a known upper bound. We further assume that $\Mhatt\in\conv(\cM\ind{t})$.

<!-- chunk {"id": "body-0393", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Localized upper bound (\pref{thm:upper\_general2})} We now prove the localized regret bound in \pref{eq:upper\_general4} under \pref{ass:hellinger\_oracle\_generalized}. Let $\Event$ denote the high-probability event in \pref{ass:hellinger\_oracle\_generalized}. Recall that we set the confidence radius used by \pref{alg:main} to $R^{2}=\EstProbHelT$. We first prove that under $\Event$, the confidence sets contain $\Mstar$ and the Hellinger error is controlled.

<!-- chunk {"id": "body-0394", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Proofs from \preft{sec:dual}} \newcommand{\weakstar}{weak$^{\star}$\xspace} \newcommand{\radon}{\Delta} \begin{proof}[\pfref{prop:minimax\_swap\_dec}] We follow the approach. Since $\compb(\cM,\Mbar) \leq \comp(\cM,\Mbar)$ by definition, it suffices to prove the opposite direction of the inequality.

<!-- chunk {"id": "body-0395", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Recall that for a topological space $\topspace{}$, let $\radon(\topspace{})$ denotes the space of Radon probability measures over $\topspace$ when $\topspace{}$ is equipped with the Borel $\sigma$-algebra. In addition, recall that the \weakstar topology on $\radon(\topspace{})$ is the coarsest topology such that the function $\mu\mapsto \int f d\mu$ is continuous for all bounded, continuous functions $f:\topspace{}\to \bbR$.

<!-- chunk {"id": "body-0396", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Let $\Act$ be equipped with the discrete topology, and recall that $\cM$ is equipped with the discrete topology as well. Since $\Act$ is finite, it is compact with respect to the discrete topology. Hence, Theorem 8.9.3 of, $\radon(\Act)$ is \weakstar-compact; $\radon(\Act)$ is also convex.

<!-- chunk {"id": "body-0397", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Let $\cQ$ be the space of finitely supported probability measures on $\cM$, which is a convex subset of $\radon(\cM)$ when $\cM$ is equipped with the discrete topology. We equip $\cQ$ with the \weakstar-topology.

<!-- chunk {"id": "body-0398", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Proofs from \preft{sec:bandit}} \label{app:bandit} \subsection{Proofs from \preft{sec:bandits\_familiar}} \subsubsection{Linear Bandits} \begin{proof}[\pfref{prop:bandit\_lower\_linear}] Let $\Delta\in\brk{0,1}$ be a parameter. We construct a hard family of models $\cM'=\crl{M_i}_{i\in\brk{d}}$ as follows. First, define $\theta_i = \Delta{}\cdot{}e_i$, where $e_i$ denotes the standard basis vector, then let $M_i(\act) = \Rad(\tri{\theta_i,\act})$; this construction has $\fmi(\act)=\tri{\theta_i,\act}$.

<!-- chunk {"id": "body-0399", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Then, take $\Mbar(\act)=\Rad(\tri{\mathbf{0},\act})=\Rad$ as the reference model.

<!-- chunk {"id": "body-0400", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proof}[\pfref{prop:bandit\_lower\_lipschitz}] Let $\veps\in(0,1/2)$ be fixed, and let $N=\Mcov(\Act,2\veps)$. By the duality of packing and covering, there exists a packing $\act_1,\ldots,\act_N$ \met(\act\_i,\act\_j)>2\veps\quad\text{for all $i\neq{}j$}. We define a class of models $\cM'=\crl*{M_1,\ldots,M_N}$ based on this packing as follows. First, define $h(x) = \max\crl*{1-x, f_i(\act) = \frac{1}{2} + \veps{}h(\met(\act,\act_i)/\veps).

<!-- chunk {"id": "body-0401", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We have $f_i(\act)\in[1/2,1)$, and since $\met$ is a metric, \abs{f_i(\act)-f_i(\act')} \veps\abs{h(\met(\act,\act_i)/\veps)-h(\met(\act',\act_i)/\veps)} \leq{} \abs{\met(\act,\act_i)-\met(\act',\act_i)} \leq \met(\act,\act'), so $f_i$ is $1$-Lipschitz. Finally, we define M_i(\act) = \Ber(f_i(\act)), and define the reference model $\Mbar$ via \Mbar(\act) = \Ber(\nicefrac{1}{2}).

<!-- chunk {"id": "body-0402", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Gap-Dependent Lower Bounds} \begin{proof}[\pfref{prop:bandit\_gap\_tabular}] This proof is almost the same as that of \pref{prop:mab\_lower}. The only difference is that we change the construction so that $\Mbar$ has a gap, which leads to worse constants.

<!-- chunk {"id": "body-0403", "role": "body", "section": "Paper Body", "weight": 1.0} -->

It follows that this is a $(\Delta,5\Delta^2,0)$-family, so \pref{lem:hard\_family} implies that for any $\gamma>0$, \geq{} \frac{\Delta}{2} - \gamma\frac{12\Delta^{2}}{A}. In particular, whenever $\gamma\leq{}\frac{A}{48\Delta}$, we have $\comp(\cM',\Mbar) \geq \frac{\Delta}{4}$. Furthermore, since we may take $\abscontp=\bigoh$ in \pref{thm:lower\_main,thm:lower\_main\_expectation}.

<!-- chunk {"id": "body-0404", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proof}[\pfref{prop:bandit\_gap\_linear}] This proof is a simple modification to \pref{prop:bandit\_lower\_linear} to ensure that $\Mbar$ has gap $\Delta$.

<!-- chunk {"id": "body-0405", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Proofs from \preft{sec:bandits\_star}} This section is organized as follows. First, we prove a generic decoupling-type lemma which holds for a slightly more general setting than what is described in \pref{sec:bandits\_star}. We then prove \pref{thm:eluder\_star} and \pref{thm:disagreement} as consequences.

<!-- chunk {"id": "body-0406", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Proof of \pref{thm:eluder\_star} and \pref{thm:disagreement}} \begin{proof}[\pfref{thm:eluder\_star}] By the minimax theorem (cf. \pref{prop:minimax\_swap\_dec}), it suffices to bound the dual \CompText $\compSqdual(\cM,\Mbar)=\sup_{\mu\in\Delta(\cM)}\compSqdual(\mu,\Mbar)$. The bound on this quantity is an immediate consequence of \pref{thm:disagreement} and \pref{lem:disagreement\_to\_ratio}.

<!-- chunk {"id": "body-0407", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Proofs from \preft{sec:rl\_bilinear\_basic}} In this section of the appendix we prove \pref{thm:posterior\_bilinear} and \pref{thm:igw\_bilinear}. Before proving the results, we state and prove a helper lemma.

<!-- chunk {"id": "body-0408", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proof}[\pfref{thm:igw\_bilinear}] We first verify that the strategy in \pref{eq:pc\_igw2} is indeed well-defined, in the sense that a normalizing constant $\lambda\in[1, 2HSA]$ always exists. There is a unique choice for $\lambda>0$ such that $\sum_{M\in\cM}p(\pialpham)=1$, and its value lies in $[1/2,1]$.\looseness=-1 Let $f(\lambda)=\sum_{M\in\cM}\frac{q(M)}{\lambda + \eta(\fmbar(\pimbar)-\fmbar(\pim))}$.

<!-- chunk {"id": "body-0409", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We observe that if $\lambda>1$, then $f(\lambda)\leq{}\sum_{M\in\cM}\frac{q(M)}{\lambda}=\frac{1}{\lambda}<1.$ On the other hand for $\lambda\in(0,1/2)$, $f(\lambda)\geq{}\frac{q(\Mbar)}{\lambda + \eta(\fmbar(\pimbar)-\fmbar(\pimbar))} Hence, since $f(\lambda)$ is continuous and strictly decreasing over $(0,\infty)$, there exists unique $\lambda^{\star}\in[1/2, 1]$ such that $f(\lambda^{\star})=1$.

<!-- chunk {"id": "body-0410", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We now show that \pcigwb achieves the stated bound on the \CompShort. Let $M\in\cM$ and $\gamma>0$ be given. We focus on bounding the quantity \En\_{\pi\sim{}p}\brk*{\fm(\pim) - \fmbar(\act)}. Throughout the proof we will overload notation and write $M\sim{}p$ and $\pialpham\sim{}p$ interchangeably.

<!-- chunk {"id": "body-0411", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To finish the construction, we define a reference model $\Mbar$. As $d_1=\mathrm{unif}(\brk*{m})$. The stationary transition kernel $\Pbar\equiv\Pmbar$ is given by &\Pbar(\term\mid{}\term,\cdot)=1,\\&\Pbar(\term\mid{}\cdot,\term)=1,\\&\Pbar(\cdot\mid{}s,a)=\left\{ \term: 1-(\tri{v\_{s},v\_{a}} + 2\Delta) \right.\quad\forall{}s\neq\term, a\notin{}\crl{s,\term}. We define the nonstationary reward function $\Rbar\equiv\Rmbar$ for the reference model as follows.

<!-- chunk {"id": "body-0412", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Our lower bound is based on the family of models $\cM'\ldef\crl*{M_{a}}_{a\in\brk{m}}\cup\crl*{\Mbar}$. We first show that this class is indeed linearly realizable; proofs for this and all subsequent lemmas are deferred to the end of the main proof.

<!-- chunk {"id": "body-0413", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To show ensure $\Mbar$ is linearly realizable, we consider the expanded feature map feature map $\phi'(s,a)\in\bbR^{d+1}$ given by \[\phi'(s,a) = \prn{\phi(s,a), -2\Delta(\tri{v\_s,v\_a}+2\Delta)\indic\crl{s\neq\term,a\notin\crl{s,\term}}}.\] \label{lem:qbar\_linear} We have $\Qmbara_h(s,a)=\tri{\phi'(s,a),(\mb{0},1)}=0$ for all $h<H$ and $\Qmbara_H(s,a)=\tri{\phi'(s,a),\mb{0}}$. This establishes that $\cM'$ is linearly realizable with the feature map $\phi'$.

<!-- chunk {"id": "body-0414", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Note that $\nrm*{\phi'(s,a)}_2\leq{}1$ whenever $\Delta\leq{}1/6$, and that all of the weight parameters for the $Q$-functions defined above have norm at most $1$ as well.

<!-- chunk {"id": "body-0415", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Next, we show that $\cM'$ is localized around $\Mbar$. \begin{lemma}[Local property] \label{prop:linq\_local} For all $\astar\in\brk{m}$, $\fmbar(\pimbar) \geq{} f\sups{\Mastar}(\piastar) - 3\Delta^{2}$, so that $\cM'\subseteq\cM_{3\Delta^{2}}(\Mbar)$.

<!-- chunk {"id": "body-0416", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To proceed, we state three lemmas which will be used to prove that $\cM'$ is a hard sub-family of models.% \label{prop:terminal\_probability} For all $M\in\cM'$, and $h\in\brk{H}$, $\sup_{\pi\in\PiRNS}\Prm{M}{\pi}(s_{h}\neq\term)\leq{}(3\Delta)^{h-1}$.

<!-- chunk {"id": "body-0417", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Proofs for Auxiliary Lemmas (\pref{prop:linear\_qstar})} \begin{proof}[\pfref{lem:linear\_family}] Let $\astar$ be fixed, and let us abbreviate $Q\equiv\Qastar$ and We begin by noting that in the terminal state, $Q_h(\term,\cdot)=V_h(\term,\cdot)=0$, so that $Q_h(\term,a)=\tri{\phi(\term,a),v_{\astar}}$. Similarly, for any state $s$, $Q_h(s,\term)=0=\tri{\phi(s,\term),v_{\astar}}$. We proceed to prove the result for non-terminal states and actions.

<!-- chunk {"id": "body-0418", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proof}[\pfref{lem:qbar\_linear}] Let us abbreviate $Q\equiv{}\Qmstar[\Mbar]$ and $V\equiv{}\Vmstar[\Mbar]$. The claim that $Q_H(s,a)=0$ follows immediately from the definition of $\Rbar_H$. For $h<H$, we prove the result under the inductive hypothesis that $V_{h+1}(s)=0$, which is clearly satisfied at layer $H$.

<!-- chunk {"id": "body-0419", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proof}[\pfref{prop:linq\_local}] \pref{lem:linear\_family} proves that for all $\astar\in\brk{m}$, $Q\ind{\astar}_h(s,a) = \tri{\phi(s,a),v_{\astar}}\leq{}3\Delta^{2}$ for all $h$. It follows that $\max_{\pi}f\sups{\Mastar}(\pi)\leq{}3\Delta^{2}$. On the other hand, \pref{lem:qbar\_linear} shows that \subsubsection{Proof of \pref{prop:mdp\_gap\_linear}} \begin{proof}[\pfref{prop:mdp\_gap\_linear}] As with \pref{prop:mdp\_lower\_linear}, we consider a bandit problem with no state, which is a special case of the reinforcement learning setting with $H=1$.

<!-- chunk {"id": "body-0420", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The proof is a small modification to \pref{prop:bandit\_gap\_linear}, with the only difference being that rewards are no longer stochastic.

<!-- chunk {"id": "body-0421", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Additional Results: Efficient Implementation and Estimation for \pcigwb} \label{sec:igw\_bilinear} This section of the appendix contains additional results concerning the \pcigwb algorithm (alg:igw\_bilinear). sec:rl\_bilinear\_computational gives an approach to efficient implementation, and sec:rl\_bilinear\_estimation gives an approach to online estimation that can applied with thm:igw\_bilinear.

<!-- chunk {"id": "body-0422", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Efficient Implementation of \pcigwb} \label{sec:rl\_bilinear\_computational} In this section, we show that it is possible to efficiently implement the optimal design step required by \pcigw (\pref{alg:igw\_bilinear}) whenever we have access to an efficient oracle for planning with a fixed model. For the results in this subsection, we assume that for all $\Mbar\in\cM$, each set $\crl*{X_h(M;\Mbar)}_{M\in\cM}$ is compact and has full dimension. We adopt the convention that for a collection of vectors $x_1,\ldots,x_d\in\bbR^{d}$, $\det(x_1,\ldots,x_d)$ denotes the determinant of the matrix $(x_1,\ldots,x_d)\in\bbR^{d\times{}d}$.

<!-- chunk {"id": "body-0423", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Oracle and assumptions} Our main computational primitive is as follows. \begin{definition}[Bilinear planning oracle] \label{def:bilinear\_planning} For a bilinear class $\cM$, a bilinear planning oracle takes as input a model $\Mbar\in\cM$ with bilinear dimension $d$ and vector $\theta\in\bbR^{dH}$ with $\nrm{\theta}_{2}\leq{}1$ and returns \label{eq:bilinear\_oracle} \oracle(\theta;\Mbar) = \argmax\_{M\in\cM}\tri*{X(M;\Mbar), \theta}. Informally, the planning oracle \pref{def:bilinear\_planning} asserts that we can efficiently perform linear optimization when the underlying model $\Mbar$ is held fixed.

<!-- chunk {"id": "body-0424", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For intuition recall that for most bilinear classes, we have $X_h(M;\Mbar) = X_h(\pim;\Mbar)$, and that $X_h(\pim;\Mbar)$ typically represents a sufficient statistic for the roll-in distribution induced by running $\pim$ in $\Mbar$. In this case, the bilinear planning oracle precisely corresponds to planning (i.e., maximizing a known reward function) with a known model.

<!-- chunk {"id": "body-0425", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The following models admit efficient bilinear planning oracles: \item For Linear MDPs, Linear Bellman Complete MDPs, Block MDPs, FLAMBE/Feature Selection, and MDPs with Linear $Q^{\star}/V^{\star}$, the oracle $\oracle$ can be implemented efficiently whenever we can efficiently plan with known dynamics in $\cM$ and any linear \item For the Low Occupancy Complexity setting, $\oracle$ can be implemented efficiently whenever we can efficiently plan with known dynamics in $\cM$ and an arbitrary reward function.\footnote{For low occupancy complexity, we require that the feature map has $\mathrm{dim}(\crl{\phi(s,a)}_{s\in\cS,a\in\cA})=d$.} Beyond a planning oracle, we require a (mild) additional assumption on the bilinear representation for $\cM$.

<!-- chunk {"id": "body-0426", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{ass:bilinear\_reward} For all $\Mbar\in\cM$, there exists $\thetambar\in\bbR^{dH}$ such that for all $M\in\cM$, \fmbar(\pim) = \tri*{X(M;\Mbar),\thetambar} This assumption implies that the bilinear planning oracle can be used to find an optimal policy when the model is known to the learner, which is a fairly minimal requirement if one wishes to develop efficient algorithms when the dynamics are \emph{unknown}.

<!-- chunk {"id": "body-0427", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The following models satisfy \pref{ass:bilinear\_reward}: Linear/Linear Bellman Complete MDPs,\footnote{For the Linear Bellman Complete setting, we require that the all-zero function is contained in the value function class of interest.} Block MDPs, FLAMBE/Feature Selection, Linear $Q^{\star}$/$V^{\star}$, Low Occupancy Complexity, and Linear Mixture MDPs.\footnote{For linear mixture MDPs, we must artificially expand the bilinear class construction in from dimension $d$ to dimension $2d$.} \paragraph{Algorithm} The algorithm we consider, \igwspanner (\pref{alg:igw\_spanner}), is an adaptation of an algorithm for contextual bandits with linearly structured actions from concurrent work by a subset of the authors. The idea behind the algorithm is to replace the notion of optimal design with that of a \emph{barycentric spanner}.

<!-- chunk {"id": "body-0428", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{definition}[Barycentric spanner] For a set $\cX\subseteq\bbR^{d}$, a subset $\cC=\crl{x_1,\ldots,x_d}\subseteq\cX$ is said to be a \emph{$C$-approximate barycentric spanner} (for $C\geq{}1$) if every element $x\in\cX$ can be expressed as a linear combination of elements in $\cC$ with coefficients in $\brk*{-C,C}$. The following well-known result shows that any barycentric spanner yields a $d$-approximate optimal design. Let $\cC=\crl*{x_1,\ldots,x_d}$ be a $C$-approximate barycentric spanner for $\cX\subseteq\bbR^{d}$. Then $p\ldef{}\unif(\cC)$ is a $C\cdot{}d$-approximate optimal design.

<!-- chunk {"id": "body-0429", "role": "body", "section": "Paper Body", "weight": 1.0} -->

show that for any compact set $\cX\subseteq\bbR^{d}$, one can efficiently find a $2$-approximate barycentric spanner using $\bigoh(d^2\log(d))$ calls to a linear optimization oracle capable of solving $\argmax_{x\in\cX}\tri*{x,\theta}$ for any $\nrm*{\theta}_2\leq{}1$. \pref{alg:igw\_spanner} is an adaptation of their algorithm. The key challenge in applying this technique is that the bilinear planning oracle (\pref{def:bilinear\_planning}) can solve $\argmax_{M\in\cM}\tri*{X_h(M;\Mbar),\theta}$, but our aim is to find a bayrcentric spanner for the reweighted factors $\crl*{Y_h(M;\Mbar)}_{M\in\cM}$.

<!-- chunk {"id": "body-0430", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Implementing a linear optimization oracle for the reweighted factors entails solving \label{eq:reweighted\_argmax} \argmax\_{M\in\cM}\frac{\tri*{X\_h(M;\Mbar),\theta}}{\sqrt{1+\eta(\fmbar(\pimbar) which is not a linear function and hence cannot be solved by $\oracle$ directly. To overcome this challenge, \pref{alg:igw\_spanner} appeals to a subroutine, \igwargmax (\pref{alg:igw\_argmax}), which uses binary search to reduce the optimization problem in \pref{eq:reweighted\_argmax} to a series of linear subproblems which can be solved by the bilinear planning oracle. In total, $\bigoht(d)$ oracle calls are required to implement \pref{eq:reweighted\_argmax}. The final guarantee for the algorithm is as follows.

<!-- chunk {"id": "body-0431", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\algblockdefx{MyRepeat}{EndRepeat}{\textbf{repeat}}{} \Statex \algcomment{Find barycentric spanner for collection $\crl*{\frac{X_h(M;\Mbar)}{\sqrt{1+\eta(\fmbar(\pimbar)-\fmbar(\pim))}}}_{M\in\cM}$ using bilinear planning oracle.} \State \textbf{parameters}: \Statex Class $\cM$ and reference model $\Mbar\in\cM$ with \Statex Layer $h\in\brk{H}$. \Statex Learning rate $\eta>0$.

<!-- chunk {"id": "body-0432", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\State \textbf{break} \State \textbf{return} $\unif(M_1,\ldots{}M_d)$ \hfill\algcommentlight{$2d$-approximate optimal design.} \label{alg:igw\_spanner} \Statex \algcomment{Approximately solve $\argmax_{M\in\cM}\frac{\abs{\tri{X_h(M;\Mbar),\theta}}}{\sqrt{1+\eta(\fmbar(\pimbar)-\fmbar(\pim))}}$ with bilinear planning oracle (by grid search).} \State \textbf{parameters}: \Statex Bilinear planning oracle $\oracle$ for $\cM$. \hfill\algcommentlight{See \pref{eq:bilinear\_oracle}.} \Statex Parameter $\theta\in\bbR^{d}$. \Statex Reference model $\Mbar\in\cM$.

<!-- chunk {"id": "body-0433", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\State \textbf{return} $\argmax_{M\in\cMhat}\frac{\abs{\tri{X_h(M;\Mbar),\theta}}}{\sqrt{1+\eta(\fmbar(\pimbar)-\fmbar(\pim))}}$. \hfill\algcommentlight{Enumeration over $\bigoht(d)$ candidates.} \label{alg:igw\_argmax} \begin{theorem}[Efficiency of \igwspanner] \label{thm:igw\_spanner} Let $\cM$ have bilinear dimension $d$ relative to $\Mbar\in\cM$, and \pref{ass:bilinear\_reward} hold.

<!-- chunk {"id": "body-0434", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Then \pref{alg:igw\_spanner} computes a $2$-approximate barycentric spanner (and consequently a $2d$-approximate optimal design) for the collection $\crl*{Y_h(M;\Mbar)}_{M\in\cM}$ using $\bigoh(d^{3}\log(d/r)\log(\eta/r))$ calls to the bilinear planning Applying this result, we can implement \pcigwb using $\bigoht(\dimbifulls)$ calls to the bilinear planning oracle, at the cost an extra $\dimbifull$ factor on the \CompShort bound due to the approximation factor paid by the barycentric spanner. For example, the final bound on the \CompText is \comp(\cM,\Mbar) \approxleq{}\frac{\dimbifulls}{\gamma} in the on-policy case.

<!-- chunk {"id": "body-0435", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Online Estimation for \pcigwb} \label{sec:rl\_bilinear\_estimation} In order to apply the \mainalg algorithm (via \pref{thm:upper\_general}), we need to bound $\comp(\cM,\Mhat\ind{t})$ for the sequence of estimators $\Mhat\ind{1},\ldots,\Mhat\ind{T}$ produced by the online estimation oracle $\AlgEst$. The bound on the \CompText attained through posterior sampling in \pref{thm:posterior\_bilinear} holds for arbitrary reference models $\Mbar$, and hence can be applied with any estimator, but the bounds on the \CompShort attained by \pcigw in thm:igw\_bilinear are proven under the assumption that $\Mbar$ belongs to the class $\cM$.

<!-- chunk {"id": "body-0436", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This limits the immediate application of \pcigw, because most online estimation algorithms are improper and produce estimates in $\conv(\cM)$.\footnote{Recall that an estimation algorithm is said to be proper if it produces estimates that lie inside $\cM$.} To address this issue, and derive efficient end-to-end algorithms based on \pcigw, we sketch an approach based on layer-wise estimators.\footnote{This issue can be addressed more directly under various technical conditions, but we leave this for a future version of this work.} Suppose for simplicity that rewards are known, and let $\cP_h=\crl*{\Pm_h\mid{}M\in\cM}$ be the class of transition kernels for layer $h$. We make the following assumption. \label{ass:layerwise} The class $\cM$ has product structure $\cM_1\times\cdots\times\cM_H$.

<!-- chunk {"id": "body-0437", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Moreover, each layer-wise class Instead of directly working with an estimator for the entire model $M$, we assume access to layer-wise estimators $\AlgEsth,\ldots,\AlgEsth[H]$. At each round $t$, given the history $\crl*{(\act\ind{i}, r\ind{i},\obs\ind{i})}_{i=1}^{t-1}$, the layer-$h$ estimator $\AlgEsth[h]$ produces an estimate $\Phat\ind{t}_h$ for the true transition kernel $\Pmstar_h$.

<!-- chunk {"id": "body-0438", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We measure performance of the estimator via layer-wise Hellinger error: \label{eq:layerwise\_hellinger} \EstHelh \ldef{}\sum\_{t=1}^{T}\En\_{\act\ind{t}\sim{}p\ind{t}}\Enm{\Mstar}{\pi\ind{t}}\brk*{\Dhels{\Pmstar\_h(s\_h,a\_h)}{\Phat\ind{t}\_h(s\_h,a\_h)}}. We obtain an estimation algorithm $\AlgEst$ for the full model by taking $\Mhat\ind{t}$ as the MDP that has $\Phat_h\ind{t}$ as the transition kernel for each layer $h$. This algorithm has the following guarantee.

<!-- chunk {"id": "body-0439", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{prop:layerwise\_estimator} The estimator $\AlgEst$ described above has \EstHel \leq \bigoh(\log(H))\cdot{}\sum\_{h=1}^{H}\EstHelh[h]. Moreover, if $\Phat\ind{t}\in\conv(\cP_h)$ for all $h$ and \pref{ass:layerwise} is satisfied, then $\Mhat\ind{t}\in\cM$. Immediate consequence of \pref{lem:hellinger\_chain\_rule}.

<!-- chunk {"id": "body-0440", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For example, whenever \pref{ass:layerwise} is satisfied, we can use this reduction with the tools in \pref{app:online} to generically provide proper estimators with \EstHel\leq\bigoht(H\cdot{}\max\_{h}\PComph), where $\PComph$ is the covering number-based complexity measure introduced in \pref{def:g\_cover}.

<!-- chunk {"id": "body-0441", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{example}[Linear MDP] In the linear MDP setting, all $M\in\cM$ have $\Pm_h(s'\mid{}s,a)=\tri*{\phi_h(s,a),\mum_h(s')}$, where $\phi_h(s,a)\in\bbR^{d}$ is a known feature map and $\mum_h(s)\in\bbR^{d}$ is a model-dependent feature map; we assume $\nrm*{\phi_h(s,a)}_2,\nrm*{\mum(s')}_2\leq{}1$. In addition, the reward distribution $\Rm_h(s,a)$ is assumed to have mean $\tri*{\phi(s,a),\wm_h}$. This setting has $\dimbifull=d$, $\Lbifull=1$, and $\piestm=\pim$.

<!-- chunk {"id": "body-0442", "role": "body", "section": "Paper Body", "weight": 1.0} -->

One can verify that the bilinear planning oracle is equivalent to planning in a linear MDP with fixed dynamics and rewards, which is computationally efficient, and that \pref{ass:bilinear\_reward} is satisfied. As a result, \pcigwb with the \igwspanner subroutine is efficient, and certifies that \comp(\cM,\Mbar) \leq \bigoh\prn*{\frac{H^3d^2}{\gamma}}, and---when used within the \mainalg algorithm---ensures that \RegDM \leq \bigoh\prn[\big]{\sqrt{H^{3}d^2T\cdot\EstHel}}. Since this class has the layer-wise structure in \pref{ass:layerwise}, we can obtain $\EstHel\leq{}\bigoht(H\max_h\PComph)$.

<!-- chunk {"id": "body-0443", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Additional Results: Bellman Representability and Bellman-Eluder Dimension} \label{app:rl\_extensions} \label{sec:bedim} In this section we provide a nonlinear generalization of the bilinear class property which we refer to as \emph{Bellman representability}, and give a bound on the \CompText based on this property. The results here recover the Bellman-eluder dimension as a special case. Throughout the section, we assume that $\sum_{h=1}^{H}r_h\in\brk*{0,1}$. \begin{definition}[Bellman representability] \label{def:bellman\_representable} Let $\cM$ and $\Mbar$ be given.

<!-- chunk {"id": "body-0444", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Let $\cGmbar=\cGmbar_1,\ldots,\cGmbar_H$ be a collection of a function classes of the form $\cGmbar_h=\crl*{\gmmbar_h:\cM\to\brk*{-1,+1}}_{M\in\cM}$. We say that $\cGmbar$ is a Bellman representation for $\cM$ (relative to \item Fo all $h$ and $M\in\cM$: \label{eq:bilinear\_residual} \abs*{\Enm{\Mbar}{\pim}\brk*{ \leq\abs{\gmmbar\_h(M)}. We assume that $\gmmbar[\Mbar]_h(M)=0$ for all $M\in\cM$. \item Let $z_h = (s_h, a_h, r_h, s_{h+1})$.

<!-- chunk {"id": "body-0445", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The following result generalizes \pref{thm:posterior\_bilinear}. Recall that $\pialpham$ denotes a randomized policy that, for each $h$, plays $\pi_{\sss{M,h}}$ with probability $1-\alpha/H$ and $\piest_{\sss{M,h}}$ with probability \label{thm:posterior\_bilinear\_representable} Let $\cM$ be a bilinear class and let $\Mbar$ be an arbitrary reference model (not necessarily in $\cM$). Abbreviate \El(\cM,\Delta)=\max\_{h}\sup\_{M\in\cM}\El(\cG\sups{M}\_h,\Delta),\mathand \Star(\cM,\Delta)=\max\_{h}\sup\_{M\in\cM}\Star(\cG\sups{M}\_h,\Delta).

<!-- chunk {"id": "body-0446", "role": "body", "section": "Paper Body", "weight": 1.0} -->

$\mu\in\Delta(\cM)$ be given, and consider the modified posterior sampling strategy that samples $M\sim\mu$ and plays $\pialpham$ for $\alpha\in$. \item If $\piestm = \pim$ (i.e., estimation is on-policy), this strategy with $\alpha=0$ certifies that \compdual(\cM,\Mbar) \leq{} \bigoh(H^{2}\Lbrfulls)\cdot{}\inf\_{\Delta>0}\crl*{ \frac{\min\crl{\El(\cM,\Delta),\Star^{2}(\cM,\Delta)}\log^{2}(\gamma)}{\gamma}}. for all $\gamma\geq{}e$.

<!-- chunk {"id": "body-0447", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\item For general estimation policies, this strategy (with an appropriate choice of $\alpha$) certifies that \comp(\cM,\Mbar) \leq{} \bigoh(H^{3/2}\Lbrfull)\cdot{}\inf\_{\Delta>0}\prn*{ \frac{\min\crl{\El(\cM,\Delta),\Star^{2}(\cM,\Delta)}\log^{2}(\gamma)}{\gamma}}^{1/2}, whenever $\gamma\geq{}e$ is sufficiently large.

<!-- chunk {"id": "body-0448", "role": "body", "section": "Paper Body", "weight": 1.0} -->

On the other hand, the notion of Bellman representability goes well beyond the Bellman-eluder dimension, since it recovers the usual Bilinear class definition as a special case. Interestingly \pref{thm:posterior\_bilinear\_representable} shows that the Bellman-eluder dimension can be replaced by a weaker parameter we call the \emph{Bellman-star number}, which, in general, can be arbitrarily small compared to the former quantity.

<!-- chunk {"id": "body-0449", "role": "body", "section": "Paper Body", "weight": 1.0} -->

From here, following the same steps as in \pref{thm:posterior\_bilinear} and tuning $\eta$ and $\alpha$ \section{Additional Proofs} \label{app:additional} \subsection{Proofs from \preft{sec:intro}} \label{app:intro} \newcommand{\algo}{\Algo}% \newcommand{\Ena}{\En^{\sss}} \newcommand{\Pra}{\bbP^{\sss}} \begin{proof}[\pfref{prop:minimax\_swap}]% We first state a minimax theorem for \emph{finitely supported} models, which is a straightforward adaptation of Theorem 1. \label{lem:finite\_support\_minimax\_swap} Suppose $\cM$ is finitely supported in the sense that $\abs*{\bigcup_{\act\in \Act} \supp(M(\act)) } < \infty$ for all $M\in\cM$.

<!-- chunk {"id": "body-0450", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In addition, assume that $\Act$ is finite and $\Rspace$ is bounded. Then we have We prove \pref{prop:minimax\_swap} by arguing that any countably supported model class can be approximated by a finitely supported class, then applying \pref{lem:finite\_support\_minimax\_swap} to the approximating class.

<!-- chunk {"id": "body-0451", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\MinimaxReg \leq \mathfrak{M}(\cM\_\veps,T) + \bigoht(T^{3/2}\veps^{1/2}) = \underbar{\mathfrak{M}}(\cM\_{\veps},T) + \bigoht(T^{3/2}\veps^{1/2}) \leq \MinimaxRegBayes + \bigoht(T^{3/2}\veps^{1/2}), where the equality holds due to \pref{lem:finite\_support\_minimax\_swap}. Finally, since neither $\MinimaxReg$ nor $\MinimaxRegBayes$ depends on $\veps$, we can take $\veps\to 0$ to finish the proof.

<!-- chunk {"id": "body-0452", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proof}[\pfref{lem:finite\_support\_minimax\_swap}]% This proof follows. Since $ \MinimaxRegBayes \leq \MinimaxReg$ by definition, it suffices to prove the opposite direction of the inequality.

<!-- chunk {"id": "body-0453", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Per the discussion, rather than representing the learner's algorithm as a sequence of mappings, $p\ind{1},\ldots,p\ind{T}$, where $p\ind{t}(\cdot\mid\cdot)$ is a probability kernel from $(\Hspace\ind{t-1},\Hsig\ind{t-1})$ to $(\Act,\Asig)$, it suffices to instead represent the learner's algorithm as a single distribution over deterministic mappings. In more detail, a deterministic algorithm $\algo=(\algo\ind{1},\ldots,\algo\ind{T})$ is a sequence of mappings $\algo\ind{t}: \Hspace\ind{t-1}\to{}\Act$. We let $\Aspace$ denote the set of all such deterministic algorithms, and represent the learner's algorithm as a distribution $\algdist\in\Delta(\Aspace)$.

<!-- chunk {"id": "body-0454", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Let $\Act$ and $\Hspace$. Since $\Act$ is finite, it is compact with respect to the discrete topology, and by Tychonoff's Theorem, we have $\Aspace$ is compact in product topology. Thus by Theorem 8.9.3 of, the space $\Delta(\Aspace)$ is \weakstar-compact. Note that $\Delta(\Aspace)$ is also convex.

<!-- chunk {"id": "body-0455", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Next, let $\cQ$ be the space of finitely supported probability measures on $\cM$, which is a convex subset of $\Delta(\cM)$; recall that $\cM$ has the discrete topology. Let $\cQ$ be equipped with the \weakstar-topology.

<!-- chunk {"id": "body-0456", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider any function $g: \Delta(\Aspace) \times \cQ \to \bbR$ that is linear and continuous with respect to both arguments (in their respective topologies). Since $\Delta(\Aspace)$ is \weakstar-compact, Sion's minimax theorem implies that, \min\_{\algdist\in \Delta(\Aspace)}\sup\_{\mu\in\cQ} g(\algdist,\mu) = \sup\_{\mu\in\cQ}\min\_{\algdist\in \Delta(\Aspace)} g(\algdist,\mu).

<!-- chunk {"id": "body-0457", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For continuity, since we consider the \weakstar-topology for both spaces, we only need to show that the function (\Algo,M) \mapsto \Ena{M}{\Algo} \brk*{\fm(\pim)-\fm(\Algo\ind{t}(\hist\ind{t-1})) } = \fm(\pim) - \Ena{M}{\Algo} \brk*{ \fm(\Algo\ind{t}(\hist\ind{t-1})) } is continuous with respect to $\Algo$ and $M$ individually. The continuity of $M$ follows because $\cM$ is equipped with discrete topology.

<!-- chunk {"id": "body-0458", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We proceed to establish continuity of the function $\Algo\mapsto{}\Ena{M}{\Algo} \brk*{\fm(\Algo\ind{t}(\hist\ind{t-1}))}$. Let $M$ be fixed. From the definition of the product topology, for any history $\hist\ind{t}$, $\Algo \mapsto \Algo\ind{t}(\hist\ind{t})$ is continuous. Since the decision space $\Pi$ is finite, we have that for any history $\hist\ind{t}$ and any decision $\act$, the function $\Algo\mapsto \indic \crl*{\Algo\ind{t}(\hist\ind{t}) = \act} $ is continuous.

<!-- chunk {"id": "body-0459", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We show inductively that for any history $\hist\ind{t}$, the map $\Algo\mapsto\Pra{M}{\Algo}_t(\hist\ind{t})$ is continuous, where $\Pra{M}{\Algo}_t(\cdot)$ denotes the law of $\hist\ind{t}$ under $M$ and $\Algo$. For the base case, $\Algo \mapsto \Pra{M}{\Algo}_0(\emptyset) = 1 $ is a constant map, and thus continuous.

<!-- chunk {"id": "body-0460", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Now, observe since $M$ is finitely supported, there can be only finite many possible trajectories $\hist\ind{t-1}$. Hence the function under consideration is actually a finite sum of continuous maps: \Ena{M}{\Algo} \brk*{ \fm(\Algo\ind{t}(\hist\ind{t-1})) } = \sum\_{\hist\ind{t-1}: (r\ind{i}, \obs\ind{i})\in \bigcup\_{\act} \supp(M(\act)) \;\forall{}i<t} \fm(\Algo\ind{t}(\hist\ind{t-1}))\cdot{} \Pra{M}{\Algo}\_{t-1}(\hist\ind{t-1}). This establishes continuity for $\Algo$.

<!-- chunk {"id": "body-0461", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{propmod}{prop:efficient\_tabular}{a} \label{prop:efficient\_tabular2} Let $\Mbar\in\cM$ and $\eta\geq{}e$ be given. Suppose there exists $\delta\in$ such that i) the initial distribution has $d_1(s)\geq \delta $ for all $s$, and ii) for all $(s,a,s')$ and $h\in\brk{H}$, $\Pmbar_h(s'|s,a) \geq \delta$.

<!-- chunk {"id": "body-0462", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Then an approximate version \pcigw algorithm (\pref{alg:policy\_cover\_igw}) which satisfies \sup\_{M\in\cM}\En\_{\act\sim{}p}\brk*{\fm(\pim)-\fm(\pi) -\gamma\cdot\Dhels{M(\act)}{\Mbar(\act)}} \leq{} 175\frac{H^3SA}{\gamma}. $\poly(H,S,A,\log(\eta/\delta))$ time with high probability via linear programming. \pref{prop:efficient\_tabular2} requires the additional assumption that the initial state probabilities and transition probabilities are lower bounded by a constant $\delta$. This assumption is fairly mild because the runtime scales with $\log(\delta^{-1})$.

<!-- chunk {"id": "body-0463", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In fact, when \pref{alg:policy\_cover\_igw} is invoked within \mainalg, where $\Mbar$ represents an estimator, one can always modify $\Mbar$ such that $\delta=1/\poly(T)$, without worsening the regret by more than a constant factor; we omit the details.

<!-- chunk {"id": "body-0464", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To proceed, we formulate \pref{eq:efficient\_tabular0} as a linear-fractional program and solve it.

<!-- chunk {"id": "body-0465", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Formulating the problem as a linear-fractional program} Let $(\hbar,\sbar,\abar)$ be fixed. We adopt a standard dual approach (e.g.,) and---rather than optimizing over policies directly---optimize over occupancy measures, from which an optimal policy $\pi_{\bar h,\bar s,\bar a}$ can extracted. Let $\vr \ldef \prn[\big]{\En_{r_h\sim{}\Rmbar_h(s,a)}\brk{r_h}}_{(h,s,a)\in\brk{H}\times\cS\times\cA}$ be the vector of average rewards for $\Mbar$.

<!-- chunk {"id": "body-0466", "role": "body", "section": "Paper Body", "weight": 1.0} -->

d\_{h,s,a} \Pmbar\_h(s'|s,a) = \sum\limits\_{a} d\_{h+1,s',a}, & \forall h\in\brk{H-1}, s'\in\cS. This is a linear-fractional program of $HSA$ decision variables with $HSA + HS $ constraints. We let $\optlfp$ denote the value of the program.

<!-- chunk {"id": "body-0467", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Applying the Charnes-Cooper transformation} Next, we apply the Charnes-Cooper transformation to transform the linear-fractional program above into a linear pogram wth $HSA+1$ decision variables and $HSA + HS +2$ constraints.

<!-- chunk {"id": "body-0468", "role": "body", "section": "Paper Body", "weight": 1.0} -->

w\_{h,s,a} \Pmbar\_h(s'|s,a) = \sum\limits\_{a} &\sum\limits\_{a} w\_{1,s,a} = t d\_1(s), & \forall s \in \cS,\\&1\geq w\_{h,s,a} \geq 0, & \forall h\in\brk{H}, s\in\cS, a\in\cA, \\Let $\optlp$ denote the value of this program, which has the following properties: \item Value is preserved: $\optlfp = \optlp$.

<!-- chunk {"id": "body-0469", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\item For feasible point $(\vw, t)$ for \pref{eq:linear-program}, the corresponding solution $\vd = \vw/t$ is feasible to the linear-fractional program \item If $\vd$ is feasible for \pref{eq:linear-fractional-program}, then the variables $(\vw,t)$ given by w\_{h,s,a} &= \frac{d\_{h,s,a}}{2HSA + \eta\prn*{ \fmbar(\pimbar) - \tri*{\vd, \vr} } } \leq \frac{1}{HSA} \leq 1, \\t &= \frac{1}{2HSA + \eta\prn*{ \fmbar(\pimbar) - \tri*{\vd, \vr} } }\leq \frac{1}{HSA} \leq 1. are feasible for \pref{eq:linear-program}.

<!-- chunk {"id": "body-0470", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\paragraph{Solving the linear program} To deduce the final runtime bound, we appeal to a standard linear program solver for \pref{eq:linear-program}.

<!-- chunk {"id": "body-0471", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proposition}[, Theorem 1\protect\footnote{Theorem 1 in is stated with constant probability, but the high probability result here trivially follows via confidence boosting.}] \label{prop:lpsolve} Let $\opt$ denote the value of the linear program \maximize\_{x} \quad& \tri{c,x}, &\\\textrm{\textnormal{subject to}}\quad & G^\trn x= b, & \\& l\_i \leq x\_i \leq u\_i, & \forall i\in [m], where $G \in \bbR^{m\times n}$, $b\in \bbR^n$, $c\in \bbR^m$ and $l_i\in \bbR\cup\set{-\infty}, u_i\in \bbR\cup\set{\infty}$ are given $x\in\bbR^{m}$ is the decision variable.

<!-- chunk {"id": "body-0472", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Suppose the following technical conditions hold: \item $G^\top$ has full row-rank, i.e., no constraints are linearly dependent (this implies that $m\geq n$). \item For each $i\in\brk{m}$, $\mathrm{dom}(x_i) \ldef \set{x: l_i < x <u_i}$ is neither the empty set nor the entire real line. \item The interior $\Omega \ldef \set{x\in R^m:G^\top x = b, l_i < x_i < u_i }$ is not empty.

<!-- chunk {"id": "body-0473", "role": "body", "section": "Paper Body", "weight": 1.0} -->

There exists a randomized algorithm $\lpsolve$ which, for any $\veps>0$, $\alpha>0$, and initial point $x^0\in \Omega$, outputs a point $x\in \Omega$ for which $c^\top x \geq \opt - \veps $ with probability at least $1-\alpha$, and does so using at most \bigoh(n^{1.5}m^2 \log^{13}m \cdot \log(mU/\veps)\log(1/\alpha)) steps, where $U \ldef{} \max \set{1/\nrm{u-x^0}_\infty, 1/\nrm{x^0-l}_\infty, \nrm{u-l}_\infty, \nrm{c}_\infty }$.

<!-- chunk {"id": "body-0474", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We now address the technical conditions required to apply $\lpsolve$ \item \emph{No constraints are linearly dependent.} This can be achieved by applying Gaussian elimination to remove dependent constraints, which takes no more than $\bigoh(H^3S^3A^3)$ steps. \item \emph{The domain of each decision variable is neither the empty set or the entire real line.} This is trivially satisfied, since $1\geq t,\vw\geq 0$. \item \emph{The interior of the polytope is not empty.} Below we construct an initial point $x^{0}\in\Omega$, certifies that the \emph{Finding an initial point.} We construct an interior point $x^{0} = (\vw^0,t^0)\in\Omega$ by first finding an interior point $\vd^0$ of the linear-fractional program \pref{eq:linear-fractional-program}, and then applying the Charnes-Cooper transformation to obtain $(\vw^0,t^0)$.

<!-- chunk {"id": "body-0475", "role": "body", "section": "Paper Body", "weight": 1.0} -->

First, note that under the assumption in \pref{prop:efficient\_tabular2} we have that for any policy $\pi$, $\sum_{a} \dm{\Mbar}{\pi}_h(s,a) \geq \delta$ for all $h\in\brk{H}$, $s\in\cS$.

<!-- chunk {"id": "body-0476", "role": "body", "section": "Paper Body", "weight": 1.0} -->

It follows that the interior of \pref{eq:linear-program} is non-empty, and that by initializing with $x^0=(\vw^0, t^0)$, we have U \leq{} \max \crl*{ \prn*{1-\tfrac{1}{HSA}}^{-1}, \prn*{\tfrac{\delta}{2A(HSA + \eta)} - 0}^{-1}, 1, 1} \leq 2A(HSA+\eta)/\delta.

<!-- chunk {"id": "body-0477", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proof}[Proof sketch for \pref{prop:approximate\_igw\_tabular}] We show that the proof of \pref{prop:igw\_tabular} goes through essentially as-is under the condition in \pref{eq:pcigw\_approx}.

<!-- chunk {"id": "body-0478", "role": "body", "section": "Paper Body", "weight": 1.0} -->

As a result, Eq. \pref{eq:pcigw\_multiplicative} in the proof of \pref{prop:igw\_tabular} continues to hold up to a factor of $2$, and changing the parameters $\eta$ and $\eta'$ accordingly yields the result.

<!-- chunk {"id": "body-0479", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Proofs from \preft{sec:related}} \label{app:related} \begin{proof}[\pfref{prop:information\_ratio\_bayes\_lower}]% For the upper bound on the \CompShort, refer to \pref{sec:bandit}. We focus on proving the lower bound on the information ratio. We consider the case $d=1$, since this immediately implies a lower bound for higher dimensions.

<!-- chunk {"id": "body-0480", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider any $p\in\Delta(\Act)$. Recall that $\Delta\ldef{}\min_{\act\neq\pimbar}\crl{\fmbar(\act)-\fmbar(\pimbar)}>0$ and $\min\fbar>0$ (since $\fbar\in\mathrm{int}(\brk{0,1}^{A})$). We consider two cases. First, if some $\actstar\in\Act$ has $p_{\actstar}=0$, we can choose the vector $f$ in the supremum in \pref{eq:info\_ratio\_freq\_lb} to have $f(\act)=\fbar(\act)$ for $\act\neq\actstar$ and $f(\actstar)=0$.

<!-- chunk {"id": "body-0481", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In this case, for any fixed $\eta$, the value in \pref{eq:info\_ratio\_freq\_lb} is 2\eta\sum\_{\act\neq\actstar}p\_{\act}\fbar(\act)\geq{}2\eta\cdot{}\min\_{\act}\fbar(\act). Hence, if $\min\fbar>0$, the value is $+\infty$, since we can take $\eta$ to be arbitrarily large.

<!-- chunk {"id": "body-0482", "role": "body", "section": "Paper Body", "weight": 1.0} -->

For the second case, suppose that $p\in\mathrm{int}(\Delta(\Act))$ and let $\eta$ and $\actstar$ be fixed. The first-order conditions for optimality imply that the maximizer for $f$ in \pref{eq:info\_ratio\_freq\_lb} is given by $f(\act) = \fbar(\act) + \frac{1}{\eta}$ for $\act\neq\actstar$ and $f(\actstar)=\fbar(\actstar)- \frac{(1-p_{\actstar})}{\eta{}p_{\actstar}}$; the feasibility of this choice will be verified shortly.

<!-- chunk {"id": "body-0483", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Since $p\in\mathrm{int}(\Delta(\Act))$, we have $(1-p_{\afbar})>0$, and hence we can drive the value to $+\infty$ by choosing $\eta$ arbitrarily large. Furthermore, since $\fbar\in\mathrm{int}(\brk{0,1}^{A})$, we have $f\in\brk*{0,1}^{A}$ as required once $\eta$ is sufficiently large.
