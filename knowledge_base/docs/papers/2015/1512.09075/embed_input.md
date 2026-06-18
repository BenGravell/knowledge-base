A Notation for Markov Decision Processes

Topics include Markov decision process.

This paper specifies a notation for Markov decision processes. The arXiv record and abstract page provide no longer abstract for this item.

## Introduction

Many reinforcement learning (RL) research papers contain paragraphs that define Markov decision processes (MDPs). These paragraphs take up space that could otherwise be used to present more useful content. In this paper we specify a notation for MDPs that can be used by other papers. Declaring the use this notation using a single sentence can replace several paragraphs of notational specifications in other papers. Importantly, the notation that we define is a common foundation that appears in many RL papers, and is not meant to be a complete notation for an entire paper.

We refer to our notation as the Markov Decision Process Notation, version 1 or MDPNv1.

> "We use the notational standard MDPNv1."

This paper is not an introduction to RL. It assumes that the reader is already familiar with the basic concepts of RL, as covered by Sutton and Barto. Also, we try to minimize the number of assumptions that we make. This means that authors using our notation will have to specify their own assumptions, rather than specify which of our assumptions must be removed.

## Discussion

In this section we discuss some of the decisions that we made regarding notation. In general, we use calligraphic capital letters for sets, e.g., $\mathcal{X}$. Elements of sets are lowercase letters that are typically similar to the set they belong to, e.g., $x \in \mathcal{X}$. Random variables are denoted by capital letters, e.g., $X$, and their instantiations by lowercase letters, e.g., $x$. Vectors are bold lowercase letters, like $\mathbf{x}$.

Although we would have liked to use lowercase letters for real-valued functions, we use $P$ and $R$ to denote real-valued functions. This is for two different reasons. First, we use $P$ rather than $p$ because $p$ is a commonly used symbol that we would like to avoid defining (notice that we have not defined ${x,y,i,j,f,g,p},$ or $q$, all of which are commonly used symbols). Second, we use $R$ because $r$ is already used to denote an element of $\mathcal{R}$, and to preserve alliteration we do not want to use a different letter.
