<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Notation for Markov Decision Processes

Topics include Markov decision process.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper specifies a notation for Markov decision processes. The arXiv record and abstract page provide no longer abstract for this item.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many reinforcement learning (RL) research papers contain paragraphs that define Markov decision processes (MDPs). These paragraphs take up space that could otherwise be used to present more useful content. In this paper we specify a notation for MDPs that can be used by other papers. Declaring the use this notation using a single sentence can replace several paragraphs of notational specifications in other papers. Importantly, the notation that we define is a common foundation that appears in many RL papers, and is not meant to be a complete notation for an entire paper.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We refer to our notation as the Markov Decision Process Notation, version 1 or MDPNv1. It can be invoked in research papers with the sentence: > "We use the notational standard MDPNv1."

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This sentence denotes that the notation specified in this document should be inserted at the current location. One challenge with this system is that any reasonably complete notation will define a large subset of the commonly used mathematical symbols, some of which an author may wish to use with a meaning other than that specified in MDPNv1. To overcome this problem, definitions that occur after the sentence invoking MDPNv1 can modify or overwrite the definitions in MDPNv1.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example, an author may write "We assume that the state and action sets are finite," which overrules MDPNv1's more general definition of the state and action sets, or "Let $\mathcal{A}$ denote the set of all possible advantage functions," which overwrites the definition of $\mathcal{A}$ in MDPNv1 (where it is the set of possible actions). In general, MDPNv1 should serve as a notational foundation, which the author is free to build upon or remove from to best suit the needs of the paper.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper is not an introduction to RL. It assumes that the reader is already familiar with the basic concepts of RL, as covered by Sutton and Barto. Also, we try to minimize the number of assumptions that we make. This means that authors using our notation will have to specify their own assumptions, rather than specify which of our assumptions must be removed.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Billy Okal has provided a style file for MDPNv1 at Not only does this style file allow you to easily switch between the different notational variants defined below, but using it allows you to change the notation used in your paper by modifying the style file rather than by editing every equation individually.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Discrete and Continuous Random Variables", "weight": 1.0} -->

In general, the state, action, and reward at time $t$ can be discrete or continuous random variables, or even a mixture of both. A discrete random variable, $X$, that takes values in a set, $\mathcal{X}$, has a probability mass function (PMF), $f:{\mathcal{X}\rightarrow{\lbrack 0,1\rbrack}}$, such that ${f{(x)}} = {\Pr{({X = x})}}$ for all $x \in \mathcal{X}$. However, continuous random variables (and random variables that are a mixture of discrete and continuous) are not characterized by a PMF. Although measure theoretic probability offers a unified notation for discussing arbitrary random variables, its use is not commonplace in reinforcement learning literature, and so it may dilute the message of a paper and shrink a paper's audience.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Discrete and Continuous Random Variables", "weight": 1.0} -->

We therefore introduce an abuse of notation into MDPNv1: notationally, we treat the state, action, and reward as though they are discrete random variables, even though they may not be. That is, our expressions are written using PMFs for distributions over states, actions, and rewards, even if they should technically be written using probability measures. The author of a paper using MDPNv1 should ensure that all claims carry over to states, actions, and rewards that are arbitrary random variables, or should explicitly restrict the states, actions, and rewards to be discrete random variables or continuous random variables that have density functions.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Markov Decision Process Notation, Version 1 (MDPNv1)", "weight": 1.0} -->

Let a Markov decision process (MDP) be a tuple, $(\mathcal{S},\mathcal{A},\mathcal{R},P,R,d_{0},\gamma)$, where We use $t \in {\mathbb{N}}_{\geq 0}$ to denote the time step, where ${\mathbb{N}}_{\geq 0}$ denotes the natural numbers including zero. $\mathcal{S}$ is the set of possible states that the agent can be, and is called the state set. The state of the environment at time $t$ is a random variable that we denote by $S_{t}$. We will typically use $s$ to denote an element of the state set. $\mathcal{A}$ is the set of possible actions that the agent can select between, and is called the action set. The action chosen by the agent at time $t$ is a random variable that we denote by $A_{t}$. We will typically use $a$ to denote a specific element of the action set.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Markov Decision Process Notation, Version 1 (MDPNv1)", "weight": 1.0} -->

$\mathcal{R} \subseteq {{\mathbb{R}} \cup {\{{- \infty},\infty\}}}$ is the set of possible rewards that the agent can receive, and is called the reward set. The reward provided to the agent at time $t$ is a random variable that we denote by $R_{t}$. We will typically use $r$ to denote an element of the reward set. Let $r_{\text{min}}$ and $r_{\text{max}}$ be the infimum and supremum of $\mathcal{R}$, respectively. $P:{{\mathcal{S} \times \mathcal{A} \times \mathcal{S}}\rightarrow{\lbrack 0,1\rbrack}}$ is called the transition function.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Markov Decision Process Notation, Version 1 (MDPNv1)", "weight": 1.0} -->

For all ${(s,a,s',t)} \in {\mathcal{S} \times \mathcal{A} \times \mathcal{S} \times {\mathbb{N}}_{\geq 0}}$, let ${P{(s,a,s')}} ≔ {\Pr{({S_{t + 1} = \left. s' \middle| S_{t} \right. = s},{A_{t} = a})}}$.^11^1Notice that we use $≔$ to denote "is defined to be". That is, $P$ characterizes the distribution over states at time $t + 1$ given the state and action at time $t$. We introduce a Markov assumption: the distribution over $S_{t + 1}$ is independent of all prior events given $S_{t}$ and $A_{t}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Markov Decision Process Notation, Version 1 (MDPNv1)", "weight": 1.0} -->

That is, the distribution over states at time $t + 1$ is fully determined by the state and action at time $t$, and this distribution is characterized by $P$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Markov Decision Process Notation, Version 1 (MDPNv1)", "weight": 1.0} -->

We allow three alternate notations for $P$. First, let ${P{(\left. s' \middle| {s,a} \right.)}} ≔ {P{(s,a,s')}}$. This form takes approximately the same amount of space, but makes it more clear that $P$ is a conditional distribution over the next state given the current state and action. Second, let ${P_{s}^{a}{(s')}} ≔ {P{(s,a,s')}}$. This notation moves terms into subscripts and superscripts in order to save some space. Third, let $P_{s,s'}^{a} ≔ {P{(s,a,s')}}$. This final form is particularly useful when space is limited. Although the author is allowed to select between the four notations for $P$, the use of $P$ should be consistent within each paper. $R$ is called the reward function.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Markov Decision Process Notation, Version 1 (MDPNv1)", "weight": 1.0} -->

Also notice that the reward function, $R$, has no subscripts or superscripts, unlike the visually similar reward at time $t$, $R_{t}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Markov Decision Process Notation, Version 1 (MDPNv1)", "weight": 1.0} -->

As with $P$, we allow for several alternate notations for $R$ that the author is free to select. Let ${R{(\left. r \middle| {s,a,s'} \right.)}} ≔ {R_{s,s'}^{a}{(r)}} ≔ R_{s,s'}^{a,r} ≔ {R{(s,a,s',r)}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Markov Decision Process Notation, Version 1 (MDPNv1)", "weight": 1.0} -->

Let $\gamma \in {\lbrack 0,1\rbrack}$ be the reward discount parameter, which may be used to discount rewards based on how far in the future they occur.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Markov Decision Process Notation, Version 1 (MDPNv1)", "weight": 1.0} -->

Let $\pi:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\lbrack 0,1\rbrack}}$ be called a policy. A policy specifies the distribution over $A_{t}$ given $S_{t}$, i.e., ${\pi{(s,a)}} ≔ {\Pr{({A_{t} = \left. a \middle| S_{t} \right. = s})}}$ for all ${(s,a,t)} \in {\mathcal{S} \times \mathcal{A} \times {\mathbb{N}}_{\geq 0}}$. All policies are assumed to be Markovian---the distribution of $A_{t}$ is independent of prior events given $S_{t}$. Let $\Pi$ be the set of all possible policies.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Markov Decision Process Notation, Version 1 (MDPNv1)", "weight": 1.0} -->

If there exists a state, $s \in \mathcal{S}$, and two unique actions, ${(a_{1},a_{2})} \in \mathcal{A}^{2}$, where $a_{1} \neq a_{2}$, and both $a_{1}$ and $a_{2}$ have non-zero probability in $s$, i.e., ${\pi{(s,a_{1})}} > 0$ and ${\pi{(s,a_{2})}} > 0$, then we refer to $\pi$ as a stochastic policy, and we refer to it as a deterministic policy otherwise. Let $\mu:{\mathcal{S}\rightarrow\mathcal{A}}$ be an alternate definition of a deterministic policy. We allow several additional shorthands: ${\pi{(\left.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Markov Decision Process Notation, Version 1 (MDPNv1)", "weight": 1.0} -->

An episode is one sequence of states, actions, and rewards, starting from $t = 0$ and continuing indefinitely. An MDP may have a state, $\overset{\infty}{s} \in \mathcal{S}$, called the terminal absorbing state. In the state $\overset{\infty}{s}$ only one action can be taken. Taking this action causes a transition back to $\overset{\infty}{s}$ and results in a reward of zero. Once the agent reaches $\overset{\infty}{s}$ the system has effectively terminated since there are no more decisions to be made or rewards to collect. If a state, $s \in \mathcal{S}$ always causes a transition to $\overset{\infty}{s}$ with a reward of zero, then we call $s$ a terminal state.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this section we discuss some of the decisions that we made regarding notation. In general, we use calligraphic capital letters for sets, e.g., $\mathcal{X}$. Elements of sets are lowercase letters that are typically similar to the set they belong to, e.g., $x \in \mathcal{X}$. Random variables are denoted by capital letters, e.g., $X$, and their instantiations by lowercase letters, e.g., $x$. Vectors are bold lowercase letters, like $\mathbf{x}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Discussion", "weight": 1.5} -->

Although we would have liked to use lowercase letters for real-valued functions, we use $P$ and $R$ to denote real-valued functions. This is for two different reasons. First, we use $P$ rather than $p$ because $p$ is a commonly used symbol that we would like to avoid defining (notice that we have not defined ${x,y,i,j,f,g,p},$ or $q$, all of which are commonly used symbols). Second, we use $R$ because $r$ is already used to denote an element of $\mathcal{R}$, and to preserve alliteration we do not want to use a different letter. Although $R$ is visually similar to $R_{t}$, it is typically clear from context which is intended, even if the reader does not notice the subscript or lack thereof.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Discussion", "weight": 1.5} -->

Sometimes the set of actions that can be selected by the agent changes depending on the state of the environment. We do not include this in our notation because it is rarely used in the literature. If the author wishes to include this additional structure in an MDP, then we recommend using $\mathcal{A}{(s)}$ to denote the set of actions that can be chosen in the state $s$. However, this is not part of MDPNv1, and must be specified by the author.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Discussion", "weight": 1.5} -->

Often MDPs are defined without explicitly defining the set of possible rewards, $\mathcal{R}$. We include $\mathcal{R}$ so that the author can write $\sum_{r \in \mathcal{R}}{f{(r)}}$ for some $f:{\mathcal{R}\rightarrow{\mathbb{R}}}$. This is useful because the two obvious choices for implicit definitions of $\mathcal{R}$ both have problems: $\sum_{r \in {\mathbb{R}}}$, while technically valid, may be confusing since the reals are typically integrated over, and $\sum_{r \in {\mathbb{Z}}}$ does not allow for rewards that are not integers.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Discussion", "weight": 1.5} -->

Although there are many other terms that we could include in MDPNv1, we have decided to only define the terms necessary to define an MDP. This both makes it easier for the reader to remember which terms are defined by MDPNv1 and avoids including controversial definitions. Furthermore, it avoids limiting the setting to only the discounted or average-reward setting (we could define symbols for both settings, but this would be unnecessarily complex).

<!-- chunk {"id": "body-0027", "role": "body", "section": "LaTeX Style File Usage", "weight": 1.0} -->

In this section we demonstrate how to use the style file accompanying this text.

<!-- chunk {"id": "body-0028", "role": "body", "section": "LaTeX Style File Usage", "weight": 1.0} -->

The package can be included using any of three options: alpha, beta, kappa. [⬇](data:text/plain;base64,ICAgICUgLi4uCiAgICBcdXNlcGFja2FnZVthbHBoYV17bWRwbn0gICUgTW9zdCB2ZXJib3NlCiAgICAlXHVzZXBhY2thZ2VbYmV0YV17bWRwbn0gICUgQ29tcHJlc3NlZAogICAgJVx1c2VwYWNrYWdlW2thcHBhXXttZHBufSAgJSBNb3N0IGNvbXByZXNzZWQKICAgICUgLi4u){download=""} 2 \\usepackage\[alpha\]{mdpn} % Most verbose 3 %\\usepackage\[beta\]{mdpn} % Compressed 4 %\\usepackage\[kappa\]{mdpn} % Most compressed You can use any of the defined commands in text as: [⬇](data:text/plain;base64,ICAgICUgLi4uCiAgICBTb21lIHRleHQgJFxjb21tYW5kJCwgZm9yIGV4YW1wbGUgJFxzc2V0JCBmb3Igc3RhdGUgc2V0CiAgICAlIC4uLg==){download=""} 2 Some text \$\\command\$, for example \$\\sset\$ for state set Some of the commands require a specific number of arguments that should be provided in the order indicated. For example \\T requires three arguments: the current state $s$, current action $a$ and next state $s'$. So, \\T{s}{a}{s'} will produce $P{({s' \mid {s,a}})}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "LaTeX Style File Usage", "weight": 1.0} -->

Most of the commands allow usual modifications such as subscripts and superscripts. For example, \\pp (which denotes a parametrised policy) can be modified to \\pp\_{sub} to yield $\pi{({a \mid {s,{\mathbf{θ}}}})}_{sub}$.
