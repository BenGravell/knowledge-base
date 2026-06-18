A Notation for Markov Decision Processes

Topics include Markov decision process.

This paper specifies a notation for Markov decision processes. The arXiv record and abstract page provide no longer abstract for this item.

## Introduction

Many reinforcement learning (RL) research papers contain paragraphs that define Markov decision processes (MDPs). These paragraphs take up space that could otherwise be used to present more useful content. In this paper we specify a notation for MDPs that can be used by other papers. Declaring the use this notation using a single sentence can replace several paragraphs of notational specifications in other papers. Importantly, the notation that we define is a common foundation that appears in many RL papers, and is not meant to be a complete notation for an entire paper.

We refer to our notation as the Markov Decision Process Notation, version 1 or MDPNv1. It can be invoked in research papers with the sentence:

Some of the commands require a specific number of arguments that should be provided in the order indicated. For example \\T requires three arguments: the current state $s$, current action $a$ and next state $s^{\prime}$. So, \\T{s}{a}{s'} will produce $P{({s^{\prime} \mid {s,a}})}$.

Most of the commands allow usual modifications such as subscripts and superscripts. For example, \\pp (which denotes a parametrised policy) can be modified to \\pp\_{sub} to yield $\pi{({a \mid {s,{\mathbf{θ}}}})}_{sub}$.

Let $\gamma \in {\lbrack 0,1\rbrack}$ be the reward discount parameter, which may be used to discount rewards based on how far in the future they occur.

We use $t \in {\mathbb{N}}_{\geq 0}$ to denote the time step, where ${\mathbb{N}}_{\geq 0}$ denotes the natural numbers including zero.

Sometimes the set of actions that can be selected by the agent changes depending on the state of the environment. We do not include this in our notation because it is rarely used in the literature. If the author wishes to include this additional structure in an MDP, then we recommend using $\mathcal{A}{(s)}$ to denote the set of actions that can be chosen in the state $s$. However, this is not part of MDPNv1, and must be specified by the author.

> "We use the notational standard MDPNv1."

This sentence denotes that the notation specified in this document should be inserted at the current location. One challenge with this system is that any reasonably complete notation will define a large subset of the commonly used mathematical symbols, some of which an author may wish to use with a meaning other than that specified in MDPNv1....
