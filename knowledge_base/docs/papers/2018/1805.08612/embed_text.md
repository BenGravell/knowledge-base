<!-- arxiv-full-text:v1 {"arxiv_id": "1805.08612", "source": "arxiv-html"} -->

## Introduction

TimSort is a sorting algorithm designed in 2002 by Tim Peters, for use in the Python programming language. It was thereafter implemented in other well-known programming languages such as Java. The algorithm includes many implementation optimizations, a few heuristics and some refined tuning, but its high-level principle is rather simple: The sequence $S$ to be sorted is first decomposed greedily into monotonic runs (i.e. nonincreasing or nondecreasing subsequences of $S$ as depicted on Figure 1), which are then merged pairwise according to some specific rules. $S=(~\underbrace{12,10,7,5}_{\text{first run}},~\underbrace{7,10,14,25,36}_{\text{second run}},~\underbrace{3,5,11,14,15,21,22}_{\text{third run}},~\underbrace{20,15,10,8,5,1}_{\text{fourth run}}~)$ Figure 1: A sequence and its run decomposition computed by TimSort: for each run, the first two elements determine if it is increasing or decreasing, then it continues with the maximum number of consecutive elements that preserves the monotonicity.

The idea of starting with a decomposition into runs is not new, and already appears in Knuth's NaturalMergeSort, where increasing runs are sorted using the same mechanism as in MergeSort. Other merging strategies combined with decomposition into runs appear in the literature, such as the MinimalSort of (see also for other considerations on the same topic). All of them have nice properties: they run in $\mathcal{O}(n\log n)$ and even $\mathcal{O}(n+n\log\rho)$, where $\rho$ is the number of runs, which is optimal in the model of sorting by comparisons, using the classical counting argument for lower bounds. And yet, among all these merge-based algorithms, TimSort was favored in several very popular programming languages, which suggests that it performs quite well in practice.

TimSort running time was implicitly assumed to be $\mathcal{O}(n\log n)$, but our unpublished preprint contains, to our knowledge, the first proof of it. This was more than ten years after TimSort started being used instead of QuickSort in several major programming languages. The growing popularity of this algorithm invites for a careful theoretical investigation. In the present paper, we make a thorough analysis which provides a better understanding of the inherent qualities of the merging strategy of TimSort. Indeed, it reveals that, even without its refined heuristics,^11^ 1 These heuristics are useful in practice, but do not improve the worst-case complexity of the algorithm. this is an effective sorting algorithm, computing and merging runs on the fly, using only local properties to make its decisions.

We first propose in Section 3 ‣ On the Worst-Case Complexity of TimSort") a new pedagogical and self-contained exposition that TimSort runs in time $\mathcal{O}(n+n\log n)$, which we want both clear and insightful. In fact, we prove a stronger statement: on an input consisting of $\rho$ runs of respective lengths $r_{1},\ldots,r_{\rho}$, we establish that TimSort runs in $\mathcal{O}(n+n\mathcal{H})\subseteq\mathcal{O}(n+n\log\rho)\subseteq\mathcal{O}(n+n\log n)$, where $\mathcal{H}=H(r_{1}/n,\ldots,r_{\rho}/n)$ and $H(p_{1},\ldots,p_{\rho})=-\sum_{i=1}^{\rho}p_{i}\log_{2}(p_{i})$ is the binary Shannon entropy.

We then refine this approach, in Section 4, to derive precise bounds on the worst-case running time of TimSort, and we prove that it is equal to $1.5n\mathcal{H}+\mathcal{O}(n)$. This answers positively a conjecture of. Of course, the first result follows from the second, but since we believe that each one is interesting on its own, we devote one section to each of them.

To introduce our last contribution, we need to look into the evolution of the algorithm: there are actually not one, but two main versions of TimSort. The first version of the algorithm contained a flaw, which was spotted : while the input was correctly sorted, the algorithm did not behave as announced (because of a broken invariant). This was discovered by De Gouw and his co-authors while trying to prove formally the correctness of TimSort. They proposed a simple way to patch the algorithm, which was quickly adopted in Python, leading to what we consider to be the real TimSort. This is the one we analyze in Sections 3 ‣ On the Worst-Case Complexity of TimSort") and 4. On the contrary, Java developers chose to stick with the first version of TimSort, and adjusted some tuning values (which depend on the broken invariant; this is explained in Sections 2 and 5) to prevent the bug exposed . Motivated by its use in Java, we explain in Section 5 how, at the expense of very complicated technical details, the elegant proofs of the Python version can be twisted to prove the same results for this older version. While working on this analysis, we discovered yet another error in the correction made in Java. Thus, we compute yet another patch, even if we strongly agree that the algorithm proposed and formally proved in (the one currently implemented in Python) is a better option.

## TimSort core algorithm

Input: A sequence S to sort Result: The sequence S is sorted into a single run, which remains on the stack. Note: The function merge_force_collapse repeatedly pops the last two runs on the stack $\runstack$, merges them and pushes the resulting run back on the stack. 1 $\rundecomp\leftarrow$ a run decomposition of S 2 $\runstack\leftarrow$ an empty stack 3 while $\rundecomp\neq\emptyset$ do // main loop of TimSort 4 remove a run r from $\rundecomp$ and push r onto $\runstack$ 5 merge_collapse($\runstack$) 6 if $\height(\runstack)\neq 1$ then // the height of $\runstack$ is its number of runs 7 merge_force_collapse($\runstack$) Algorithm 1 TimSort (Python 3.6.5) The idea of TimSort is to design a merge sort that can exploit the possible "non randomness" of the data, without having to detect it beforehand and without damaging the performances on random-looking data. This follows the ideas of adaptive sorting (see for a survey on taking presortedness into account when designing and analyzing sorting algorithms).

The first feature of TimSort is to work on the natural decomposition of the input sequence into maximal runs. In order to get larger subsequences, TimSort allows both nondecreasing and decreasing runs, unlike most merge sort algorithms.

Then, the merging strategy of TimSort (Algorithm 1) is quite simple yet very efficient. The runs are considered in the order given by the run decomposition and successively pushed onto a stack. If some conditions on the size of the topmost runs of the stack are not satisfied after a new run has been pushed, this can trigger a series of merges between pairs of runs at the top or right under. And at the end, when all the runs in the initial decomposition have been pushed, the last operation is to merge the remaining runs two by two, starting at the top of the stack, to get a sorted sequence. The conditions on the stack and the merging rules are implemented in the subroutine called merge_collapse detailed in Algorithm 2. This is what we consider to be TimSort core mechanism and this is the main focus of our analysis.

Input: A stack of runs $\runstack$ Result: The invariant of Equations and is established. Note: The runs on the stack are denoted by $\runstack\dots\runstack[\height(\runstack)]$, from top to bottom. The length of run $\runstack$[i] is denoted by ri. The blue highlight indicates that the condition was not present in the original version of TimSort (this will be discussed in section 5). 1 while $\height(\runstack)>1$ do 2 $n\leftarrow\height(\runstack)-2$ 3 if (n > 0 and r3 ≤ r2 + r1) or (n > 1 and r4 ≤ r3 + r2) then 5 merge runs $\runstack$ and $\runstack$ on the stack 6 else merge runs $\runstack$ and $\runstack$ on the stack 8 merge runs $\runstack$ and $\runstack$ on the stack Algorithm 2 The merge_collapse procedure (Python 3.6.5) Another strength of TimSort is the use of many effective heuristics to save time, such as ensuring that the initial runs are not to small thanks to an insertion sort or using a special technique called "galloping" to optimize the merges. However, this does not interfere with our analysis and we will not discuss this matter any further.

Let us have a closer look at Algorithm 2 which is a pseudo-code transcription of the merge_collapse procedure found in the latest version of Python (3.6.5). To illustrate its mechanism, an example of execution of the main loop of TimSort (lines 1-1 of Algorithm 1) is given in Figure 2. As stated in its note, Tim Peter's idea was that: > "The thrust of these rules when they trigger merging is to balance the run lengths as closely as possible, while keeping a low bound on the number of runs we have to remember."

To achieve this, the merging conditions of merge_collapse are designed to ensure that the following invariant^22^ 2 Actually,, the invariant is only stated for the 3 topmost runs of the stack. is true at the end of the procedure: This means that the runs lengths $\mathsf{r}_{i}$ on the stack grow at least as fast as the Fibonacci numbers and, therefore, that the height of the stack stays logarithmic (see Lemma 10 ‣ On the Worst-Case Complexity of TimSort"), section 3 ‣ On the Worst-Case Complexity of TimSort")).

Note that the bound on the height of the stack is not enough to justify the $\mathcal{O}(n\log n)$ running time of TimSort. Indeed, without the smart strategy used to merge the runs "on the fly", it is easy to build an example using a stack containing at most two runs and that gives a $\Theta(n^{2})$ complexity: just assume that all runs have size two, push them one by one onto a stack and perform a merge each time there are two runs in the stack.

We are now ready to proceed with the analysis of TimSort complexity. As mentioned earlier, Algorithm 2 does not correspond to the first implementation of TimSort in Python, nor to the current one in Java, but to the latest Python version. The original version will be discussed in details later, in Section 5.

Figure 2: The successive states of the stack $\runstack$ (the values are the lengths of the runs) during an execution of the main loop of TimSort (Algorithm 1), with the lengths of the runs in $\rundecomp$ being. The label #1 indicates that a run has just been pushed onto the stack. The other labels refer to the different merges cases of merge_collapse as translated in Algorithm 3.

## TimSort runs in $\mathcal{O}(n\log n)$

At the first release of TimSort, a time complexity of $\mathcal{O}(n\log n)$ was announced with no element of proof given. It seemed to remain unproved until our recent preprint, where we provide a confirmation of this fact, using a proof which is not difficult but a bit tedious. This result was refined later , where the authors provide lower and upper bounds, including explicit multiplicative constants, for different merge sort algorithms.

Our main concern is to provide an insightful proof of the complexity of TimSort, in order to highlight how well designed is the strategy used to choose the order in which the merges are performed. The present section is more detailed than the following ones as we want it to be self-contained once TimSort has been translated into Algorithm 3 ‣ On the Worst-Case Complexity of TimSort") (see below).

Input: A sequence to S to sort Result: The sequence S is sorted into a single run, which remains on the stack. Note: At any time, we denote the height of the stack $\runstack$ by h and its ith top-most run (for 1 ≤ i ≤ h) by Ri. The size of this run is denoted by ri. 1 $\rundecomp\leftarrow$ the run decomposition of S 2 $\runstack\leftarrow$ an empty stack 3 while $\rundecomp\neq\emptyset$ do // main loop of TimSort 4 remove a run r from $\rundecomp$ and push r onto $\runstack$ // #1 6 if h ≥ 3 and r1 > r3 then merge the runs R2 and R3 // #2 7 else if h ≥ 2 and r1 ≥ r2 then merge the runs R1 and R2 // #3 8 else if h ≥ 3 and r1 + r2 ≥ r3 then merge the runs R1 and R2 // #4 9 else if h ≥ 4 and r2 + r3 ≥ r4 then merge the runs R1 and R2 // #5 11 while h ≠ 1 do merge the runs R1 and R2 Algorithm 3 TimSort: translation of Algorithm 1 and Algorithm 2 As our analysis is about to demonstrate, in terms of worst-case complexity, the good performances of TimSort do not rely on the way merges are performed. Thus we choose to ignore their many optimizations and consider that merging two runs of lengths $r$ and $r^{\prime}$ requires both $r+r^{\prime}$ element moves and $r+r^{\prime}$ element comparisons. Therefore, to quantify the running time of TimSort, we only take into account the number of comparisons performed.

In particular, aiming at computing precise bounds on the running time of TimSort, we follow and define the *merge cost* for merging two runs of lengths $r$ and $r^{\prime}$ as $r+r^{\prime}$, i.e., the length of the resulting run. Henceforth, we will identify the time spent for merging two runs with the merge cost of this merge.

### Theorem 1

Let $\mathcal{C}$ be the class of arrays of length $n$, whose run decompositions consist of $\rho$ monotonic runs of respective lengths $r_{1},\ldots,r_{\rho}$. Let $H(p_{1},\ldots,p_{\rho})=-\sum_{i=1}^{\rho}p_{i}\log_{2}(p_{i})$ be the binary Shannon entropy, and let $\mathcal{H}=H(r_{1}/n,\ldots,r_{\rho}/n)$.

The running time of TimSort on arrays in $\mathcal{C}$ is $\mathcal{O}(n+n\mathcal{H})$.

From this result, we easily deduce the following complexity bound on TimSort, which is less precise but more simple.

### Theorem 2

The running time of TimSort on arrays of length $n$ that consist of $\rho$ monotonic runs is $\mathcal{O}(n+n\log\rho)$, and therefore $\mathcal{O}(n\log n)$.

### Proof

The function $f:x\mapsto-x\ln(x)$ is concave on the interval $\mathbb{R}_{>0}$ of positive real numbers, since its second derivative is $f^{\prime\prime}(x)=-1/x$. Hence, when $p_{1},\ldots,p_{\rho}$ are positive real numbers that sum up to one, we have $H(p_{1},\ldots,p_{\rho})={\textstyle\sum_{i=1}^{\rho}f(p_{i})/\ln}\leqslant\rho f(1/\rho)/\ln=\log_{2}(\rho)$. In particular, this means that $\mathcal{H}\leqslant\log_{2}(\rho)$, and therefore that TimSort runs in time $\mathcal{O}(n+n\log\rho)$. Since $\rho\leqslant n$, it further follows that $\mathcal{O}(n+n\log\rho)\subseteq\mathcal{O}(n+n\log n)=\mathcal{O}(n\log n)$, which completes the proof. ∎ Before proving Theorem 1 ‣ On the Worst-Case Complexity of TimSort"), we first show that it is optimal up to a multiplicative constant, by recalling the following variant of a result from \[2, Theorem 2\].

### Proposition 3

For every algorithm comparing only pairs of elements, there exists an array in the class $\mathcal{C}$ whose sorting requires at least $n\mathcal{H}-3n$ element comparisons.

### Proof

In the comparison model, at least $\log_{2}(|\mathcal{C}|)$ element comparisons are required for sorting all arrays in $\mathcal{C}$. Hence, we prove below that $\log_{2}(|\mathcal{C}|)\geqslant n\mathcal{H}-3n$.

Let $\pi=(\pi_{1},\ldots,\pi_{\rho})$ be a partition of the set $\{1,\ldots,n\}$ into $\rho$ subsets of respective sizes $r_{1},\ldots,r_{\rho}$; we say that $\pi$ is *nice* if $\max\pi_{i}>\min\pi_{i+1}$ for all $i\leqslant\rho-1$. Let us denote by $\mathcal{P}$ the set of partitions $\pi$ of $\{1,\ldots,n\}$ such that $|\pi_{i}|=r_{i}$ for all $i\leqslant\rho$, and by $\mathcal{N}$ the set of nice partitions.

Let us transform every partition $\pi\in\mathcal{P}$ into a nice partition as follows. First, by construction of the run decomposition of an array, we know that $r_{1},\ldots,r_{\rho-1}\geqslant 2$, and therefore that $\min\pi_{i}<\max\pi_{i}$ for all $i\leqslant\rho-1$. Then, for all $i\leqslant\rho-1$, if $\max\pi_{i}<\min\pi_{i+1}$, we exchange the partitions to which belong $\max\pi_{i}$ and $\min\pi_{i+1}$, i.e., we move $\max\pi_{i}$ from the set $\pi_{i}$ to $\pi_{i+1}$, and $\min\pi_{i+1}$ from $\pi_{i+1}$ to $\pi_{i}$. Let $\pi^{\ast}$ be the partition obtained after these exchanges have been performed.

Observe that $\pi^{\ast}$ is nice, and that at most $2^{\rho-1}$ partitions $\pi\in\mathcal{P}$ can be transformed into $\pi^{\ast}$. This proves that $2^{\rho-1}|\mathcal{N}|\geqslant|\mathcal{P}|$. Let us further identify every nice partition $\pi^{\ast}$ with an array in $\mathcal{C}$, which starts with the elements of $\pi^{\ast}_{1}$ (listed in increasing order), then of $\pi^{\ast}_{2},\ldots,\pi^{\ast}_{\rho}$. We thereby define an injective map from $\mathcal{N}$ to $\mathcal{C}$, which proves that $|\mathcal{C}|\geqslant|\mathcal{N}|$.

Finally, variants of the Stirling formula indicate that $(k/e)^{k}\leqslant k!\leqslant e\sqrt{k}(k/e)^{k}$ for all $k\geqslant 1$. This proves that By concavity of the function $x\mapsto\log_{2}(x)$, it follows that $\textstyle\sum_{i=1}^{\rho}\log_{2}(r_{i})\leqslant\rho\log_{2}(n/\rho)$. One checks easily that the function $x\mapsto x\log_{2}(n/x)$ takes its maximum value at $x=n/e$, and since $n\geqslant\rho$, we conclude that $\log_{2}(|\mathcal{C}|)\geqslant n\mathcal{H}-(1+\log_{2}(e)+\log_{2}(e)/e)n\geqslant n\mathcal{H}-3n$. ∎ We focus now on proving Theorem 1 ‣ On the Worst-Case Complexity of TimSort"). The first step consists in rewriting Algorithm 1 and Algorithm 2 in a form that is easier to deal. This is done in Algorithm 3 ‣ On the Worst-Case Complexity of TimSort").

### Claim 4

For any input, Algorithms 1 and 3 ‣ On the Worst-Case Complexity of TimSort") perform the same comparisons.

### Proof

The only difference is that Algorithm 2 was changed into the while loop of lines 5 to 10 in Algorithm 3 ‣ On the Worst-Case Complexity of TimSort"). Observing the different cases, it is straightforward to verify that merges involving the same runs take place in the same order in both algorithms. Indeed, if $r_{3}<r_{1}$, then $r_{3}\leqslant r_{1}+r_{2}$, and therefore line 5 is triggered in Algorithm 2, so that both algorithms merge the $2$^nd^ and $3$^rd^ runs. On the contrary, if $r_{3}\geqslant r_{1}$, then both algorithms merge the $1$^st^ and $2$^nd^ runs if and only if $r_{2}\leqslant r_{1}$ or $r_{3}\leqslant r_{1}+r_{2}$ (or $r_{4}\leqslant r_{2}+r_{3}$). ∎

### Remark 5

Proving Theorem 2 ‣ On the Worst-Case Complexity of TimSort") only requires analyzing the *main loop* of the algorithm (lines 3 to 10). Indeed, computing the run decomposition (line 1) can be done on the fly, by a greedy algorithm, in time linear in $n$, and the *final loop* (line 11) might be performed in the main loop by adding a fictitious run of length $n+1$ at the end of the decomposition.

In the sequel, for the sake of readability, we also omit checking that $h$ is large enough to trigger the cases #2 to #5. Once again, such omissions are benign, since adding fictitious runs of respective lengths $8n$, $4n$, $2n$ and $n$ (in this order) at the beginning of the decomposition would ensure that $h\geqslant 4$ during the whole loop.

We sketch now the main steps of our proof, i.e., the amortized analysis of the main loop. A first step is to establish the invariant and, ensuring an exponential growth of the run lengths within the stack.

Elements of the input array are easily identified by their starting position in the array, so we consider them as well-defined and distinct entities (even if they have the same value). The *height* of an element in the stack of runs is the number of runs that are below it in the stack: the elements belonging to the run $R_{i}$ in the stack $\mathcal{S}=(R_{1},\ldots,R_{h})$ have height $h-i$, and we recall that the length of the run $R_{i}$ is denoted by $r_{i}$.

### Lemma 6

At any step during the main loop of TimSort, we have $r_{i}+r_{i+1}<r_{i+2}$ for all $i\in\{3,\ldots,h-2\}$.

### Proof

We proceed by induction. The proof consists in verifying that, if the invariant holds at some point, then it still holds when an update of the stack occurs in one of the five situations labeled #1 to #5 in the algorithm. This can be done by a straightforward case analysis. We denote by $\overline{\mathcal{S}}=(\overline{R}_{1},\ldots,\overline{R}_{\overline{h}})$ the new state of the stack after the update: If Case #1 just occurred, a new run $\overline{R}_{1}$ was pushed. This implies that none of the conditions of Cases #2 to #5 hold in $\mathcal{S}$, otherwise merges would have continued. In particular, we have $r_{2}+r_{3}<r_{4}$. As $\overline{r}_{i}=r_{i-1}$ for all $i\geqslant 2$, and since the invariant holds for $\mathcal{S}$, it also holds for $\overline{\mathcal{S}}$.

If one of the Cases #2 to #5 just occurred, $\overline{r}_{i}=r_{i+1}$ for all $i\geqslant 3$. Since the invariant holds for $\mathcal{S}$, it must also hold for $\overline{\mathcal{S}}$.

### Corollary 7

During the main loop of TimSort, whenever a run is about to be pushed onto the stack, we have $r_{i}\leqslant 2^{(i+1-j)/2}r_{j}$ for all integers $i\leqslant j\leqslant h$.

### Proof

Since a run is about to be pushed, none of the conditions of Cases #2 to #5 hold in the stack $\mathcal{S}$. Hence, we have $r_{1}<r_{2}$, $r_{1}+r_{2}<r_{3}$ and $r_{2}+r_{3}<r_{4}$, and Lemma 6 ‣ On the Worst-Case Complexity of TimSort") further proves that $r_{i}+r_{i+1}<r_{i+2}$ for all $i\in\{3,\ldots,h-2\}$. In particular, for all $i\leqslant h-2$, we have $r_{i}<r_{i+1}$, and thus $2r_{i}\leqslant r_{i}+r_{i+1}\leqslant r_{i+2}$. It follows immediately that $r_{i}\leqslant 2^{-k}r_{i+2k}\leqslant 2^{-k}r_{i+2k+1}$ for all integers $k\geqslant 0$, which is exactly the statement of Corollary 7 ‣ On the Worst-Case Complexity of TimSort"). ∎ Corollary 7 ‣ On the Worst-Case Complexity of TimSort") will be crucial in proving that the main loop of TimSort can be performed for a merge cost $\mathcal{O}(n+n\mathcal{H})$. However, we do not prove this upper bound directly. Instead, we need to distinguish several situations that may occur within the main loop.

Consider the sequence of Cases #1 to #5 triggered during the execution of the main loop of TimSort. It can be seen as a word on the alphabet $\{\#1,\ldots,\#5\}$ that starts with #1, which completely encodes the execution of the algorithm. We split this word at every #1, so that each piece corresponds to an iteration of the main loop. Those pieces are in turn split into two parts, at the first occurrence of a symbol #3, #4 or #5. The first half is called a *starting sequence* and is made of a #1 followed by the maximal number of #2's. The second half is called an *ending sequence*, it starts with #3, #4 or #5 (or is empty) and it contains no occurrence of #1 (see Figure 3 ‣ On the Worst-Case Complexity of TimSort") for an example). $\underbrace{\#1\;\#2\;\#2\;\#2}_{\text{starting seq.}}~~\underbrace{\#3\;\#2\;\#5\;\#2\;\#4\;\#2}_{\text{ending seq.}}~~~\underbrace{\#1\;\#2\;\#2\;\#2\;\#2\;\#2}_{\text{starting seq.}}~~\underbrace{\#5\;\#2\;\#3\;\#3\;\#4\;\#2}_{\text{ending seq.}}$ Figure 3: The decomposition of the encoding of an execution into starting and ending sequences.

We bound the merge cost of starting sequences first, and will deal with ending sequences afterwards.

### Lemma 8

The cost of all merges performed during the starting sequences is $\mathcal{O}(n)$.

### Proof

More precisely, for a stack $\mathcal{S}=(R_{1},\ldots,R_{h})$, we prove that a starting sequence beginning with a push of a run $R$ of size $r$ onto $\mathcal{S}$ uses at most $\gamma r$ comparisons in total, where $\gamma$ is the real constant $2\sum_{j\geqslant 1}j/2^{j/2}$. After the push, the stack is $\overline{\mathcal{S}}=(R,R_{1},\ldots,R_{h})$ and, if the starting sequence contains $k\geqslant 1$ letters, i.e. $k-1$ occurrences of #2, then this sequence amounts to merging the runs $R_{1}$, $R_{2}$,..., $R_{k}$. Since no merge is performed if $k=1$, we assume below that $k\geqslant 2$.

More precisely, the total cost of these merges is The last occurrence of Case #2 ensures that $r>r_{k}$, hence applying Corollary 7 ‣ On the Worst-Case Complexity of TimSort") to the stack $\mathcal{S}=(R_{1},\ldots,R_{h})$ shows that $r\geqslant r_{k}\geqslant 2^{(k-1-i)/2}r_{i}$ for all $i=1,\ldots,k$. It follows that This concludes the proof, since each run is the beginning of exactly one starting sequence, and the sum of their lengths is $n$. ∎ Now, we must take care of run merges that take place during ending sequences. The cost of merging two runs will be taken care of by making run elements pay tokens: whenever two runs of lengths $r$ and $r^{\prime}$ are merged, $r+r^{\prime}$ tokens are paid (not necessarily by the elements of those runs that are merged). In order to do so, and to simplify the presentation, we also distinguish two kinds of tokens, the $\diamondsuit$-tokens and the $\heartsuit$-tokens, which can both be used to pay for comparisons.

Two $\diamondsuit$-tokens and one $\heartsuit$-token are credited to an element when its run is pushed onto the stack or when its height later decreases *because of a merge that took place during an ending sequence*: in the latter case, all the elements of $R_{1}$ are credited when $R_{1}$ and $R_{2}$ are merged, and all the elements of $R_{1}$ and $R_{2}$ are credited when $R_{2}$ and $R_{3}$ are merged. Tokens are spent to pay for comparisons, depending on the case triggered: Case #2: every element of $R_{1}$ and $R_{2}$ pays 1 $\diamondsuit$. This is enough to cover the cost of merging $R_{2}$ and $R_{3}$, because $r_{1}>r_{3}$ in this case, and therefore $r_{2}+r_{1}\geqslant r_{2}+r_{3}$.

Case #3: every element of $R_{1}$ pays 2 $\diamondsuit$. In this case $r_{1}\geqslant r_{2}$, and the cost is $r_{1}+r_{2}\leqslant 2r_{1}$.

Cases #4 and #5: every element of $R_{1}$ pays 1 $\diamondsuit$ and every element of $R_{2}$ pays 1 $\heartsuit$. The cost $r_{1}+r_{2}$ is exactly the number of tokens spent.

### Lemma 9

The balances of $\diamondsuit$-tokens and $\heartsuit$-tokens of each element remain non-negative throughout the main loop of TimSort.

### Proof

In all four cases #2 to #5, because the height of the elements of $R_{1}$ and possibly the height of those of $R_{2}$ decrease, the number of credited $\diamondsuit$-tokens after the merge is at least the number of $\diamondsuit$-tokens spent. The $\heartsuit$-tokens are spent in Cases #4 and #5 only: every element of $R_{2}$ pays one $\heartsuit$-token, and then belongs to the topmost run $\overline{R}_{1}$ of the new stack $\overline{\mathcal{S}}=(\overline{R}_{1},\ldots,\overline{R}_{h-1})$ obtained after merging $R_{1}$ and $R_{2}$. Since $\overline{R}_{i}=R_{i+1}$ for $i\geqslant 2$, the condition of Case #4 implies that $\overline{r}_{1}\geqslant\overline{r}_{2}$ and the condition of Case #5 implies that $\overline{r}_{1}+\overline{r}_{2}\geqslant\overline{r}_{3}$: in both cases, the next modification of the stack $\overline{\mathcal{S}}$ is another merge, which belongs to the same ending sequence.

This merge decreases the height of $\overline{R}_{1}$, and therefore decreases the height of the elements of $R_{2}$, who will regain one $\heartsuit$-token without losing any, since the topmost run of the stack never pays with $\heartsuit$-tokens. This proves that, whenever an element pay one $\heartsuit$-token, the next modification is another merge during which it regains its $\heartsuit$-token. This concludes the proof by direct induction. ∎ Finally, consider some element belonging to a run $R$. Let $\mathcal{S}$ be the stack just before pushing the run $R$, and let $\overline{S}=(\overline{R}_{1},\ldots,\overline{R}_{h})$ be the stack just after the starting sequence of the run $R$ (i.e., the starting sequence initiated when $R$ is pushed onto $\mathcal{S}$) is over. Every element of $R$ will be given at most $2h$ $\diamondsuit$-tokens and $h$ $\heartsuit$-tokens during the main loop of the algorithm.

### Lemma 10

The height of the stack when the starting sequence of the run $R$ is over satisfies the inequality $h\leqslant 4+2\log_{2}(n/r)$.

### Proof

Since none of the runs $\overline{R}_{3},\ldots,\overline{R}_{h}$ has been merged during the starting sequence of $R$, applying Corollary 7 ‣ On the Worst-Case Complexity of TimSort") to the stack $\mathcal{S}$ proves that $\overline{r}_{3}\leqslant 2^{2-h/2}\overline{r}_{h}\leqslant 2^{2-h/2}n$. The run $R$ has not yet been merged either, which means that $r=\overline{r}_{1}$. Moreover, at the end of this starting sequence, the conditions of case #2 do not hold anymore, which means that $\overline{r}_{1}\leqslant\overline{r}_{3}$. It follows that $r=\overline{r}_{1}\leqslant\overline{r}_{3}\leqslant 2^{2-h/2}n$, which entails the desired inequality. ∎ Collecting all the above results is enough to prove Theorem 1 ‣ On the Worst-Case Complexity of TimSort"). First, as mentioned in Remark 5 ‣ On the Worst-Case Complexity of TimSort"), computing the run decomposition can be done in linear time. Then, we proved that the starting sequences of the main loop have a merge cost $\mathcal{O}(n)$, and that the ending sequences have a merge cost $\mathcal{O}(\sum_{i=1}^{\rho}(1+\log(n/r_{i}))r_{i})=\mathcal{O}(n+n\mathcal{H})$. Finally, the additional merges of line 11 may be taken care of by Remark 5 ‣ On the Worst-Case Complexity of TimSort"). This concludes the proof of the theorem.

## Refined analysis and precise worst-case complexity

The analysis performed in Section 3 ‣ On the Worst-Case Complexity of TimSort") proves that TimSort sorts arrays in time $\mathcal{O}(n+n\mathcal{H})$. Looking more closely at the constants hidden in the $\mathcal{O}$ notation, we may in fact prove that the cost of merges performed during an execution of TimSort is never greater than $6n\mathcal{H}+\mathcal{O}(n)$. However, the lower bound provided by Proposition 3 ‣ On the Worst-Case Complexity of TimSort") only proves that the cost of these merges must be at least $n\mathcal{H}+\mathcal{O}(n)$. In addition, there exist sorting algorithms whose merge cost is exactly $n\mathcal{H}+\mathcal{O}(n)$.

Hence, TimSort is optimal only up to a multiplicative constant. We focus now on finding the least real constant $\kappa$ such that the merge cost of TimSort is at most $\kappa n\mathcal{H}+\mathcal{O}(n)$, thereby proving a conjecture of.

### Theorem 11

The merge cost of TimSort on arrays in $\mathcal{C}$ is at most $\kappa n\mathcal{H}+\mathcal{O}(n)$, where $\kappa=3/2$. Furthermore, $\kappa=3/2$ is the least real constant with this property.

The rest of this Section is devoted to proving Theorem 11. The theorem can be divided into two statements: one that states that TimSort is asymptotically optimal up to a multiplicative constant of $\kappa=3/2$, and one that states that $\kappa$ is optimal. The latter statement was proved . Here, we borrow their proof for the sake of completeness.

### Proposition 12

There exist arrays of length $n$ on which the merge cost of TimSort is at least $3/2n\log_{2}(n)+\mathcal{O}(n)$.

### Proof

The dynamics of TimSort when sorting an array involves only the lengths of the monotonic runs in which the array is split, not the actual array values. Hence, we identify every array with the sequence of its run lengths. Therefore, every sequence of run lengths $\langle r_{1},\ldots,r_{\rho}\rangle$ such that $r_{1},\ldots,r_{\rho-1}\geqslant 2$, $r_{\rho}\geqslant 1$ and $r_{1}+\ldots+r_{\rho}=n$ represents at least one possible array of length $n$.

We define inductively a sequence of run lengths $\mathcal{R}(n)$ as follows: where the concanetation of two sequences $s$ and $t$ is denoted by $s\cdot t$.

Then, let us apply the main loop of TimSort on an array whose associated monotonic runs have lengths $\mathbf{r}=\langle r_{1},\ldots,r_{\rho}\rangle$, starting with an empty stack. We denote the associated merge cost by $c(\mathbf{r})$ and, if $\overline{\mathcal{S}}=(\overline{R}_{1},\ldots,\overline{R}_{\overline{h}})$ is the stack obtained after the main loop has been applied, we denote by $s(\mathbf{r})$ the sequence $\langle\overline{r}_{1},\ldots,\overline{r}_{\overline{h}}\rangle$.

An immediate induction shows that, if $r_{1}\geqslant r_{2}+\ldots+r_{\rho}+1$, then $c(\mathbf{r})=c(\langle r_{2},\ldots,r_{\rho}\rangle)$ and $s(\mathbf{r})=\langle r_{1}\rangle\cdot s(\langle r_{2},\ldots,r_{\rho}\rangle)$. Similarly, if $r_{1}\geqslant r_{2}+\ldots+r_{\rho}+1$ and $r_{2}\geqslant r_{3}+\ldots+r_{\rho}+1$, then $c(\mathbf{r})=c(\langle r_{3},\ldots,r_{\rho}\rangle)$ and $s(\mathbf{r})=\langle r_{1},r_{2}\rangle\cdot s(\langle r_{3},\ldots,r_{\rho}\rangle)$.

Consequently, and by another induction on $n$, it holds that $s(\mathcal{R}(n))=\langle n\rangle$ and that Let $u_{x}=c(\mathcal{R}(\lfloor x\rfloor))$ and $v_{x}=(u_{x-4}-15/2)/x-3\log_{2}(x)/2$. An immediate induction shows that $c(\mathcal{R}(n))\geqslant c(\mathcal{R}(n+1))$ for all integers $n\geqslant 0$, which means that $x\mapsto u_{x}$ is non-decreasing. Then, we have $u_{n}=u_{n/2}+u_{(n-3)/2}+\lceil 3n/2\rceil$ for all integers $n\geqslant 6$, and therefore $u_{x}\geqslant 2u_{x/2-2}+3(x-1)/2$ for all real numbers $x\geqslant 6$. Consequently, for $x\geqslant 11$, it holds that This proves that $v_{x}\geqslant v_{x/2}$, from which it follows that $v_{x}\geqslant\inf\{v_{t}\,:\,11/2\leqslant t<11\}$. Since $v_{t}=-15/(2t)-3\log_{2}(t)/2\geqslant-15/11-3\log_{2}/2\geqslant-7$ for all $t\in11/2,11)$, we conclude that $v_{x}\geqslant-7$ for all $x\geqslant 11$, and thus that thereby proving Proposition [12. ∎ It remains to prove the first statement of Theorem 11. Our initial step towards this statement consists in refining Lemma 6 ‣ On the Worst-Case Complexity of TimSort"). This is the essence of Lemmas 13 to 16.

### Lemma 13

At any step during the main loop of TimSort, if $h\geqslant 4$, we have $r_{2}<r_{4}$ and $r_{3}<r_{4}$.

### Proof

We proceed by induction. The proof consists in verifying that, if the invariant holds at some point, then it still holds when an update of the stack occurs in one of the five situations labeled #1 to #5 in the algorithm. This can be done by a straightforward case analysis. We denote by $\mathcal{S}=(R_{1},\ldots,R_{h})$ the stack just before the update, and by $\overline{\mathcal{S}}=(\overline{R}_{1},\ldots,\overline{R}_{\overline{h}})$ the new state of the stack after the update: If Case #1 just occurred, a new run $\overline{R}_{1}$ was pushed. This implies that the conditions of Cases #2 and #4 did not hold in $\mathcal{S}$, otherwise merges would have continued. In particular, we have $\overline{r}_{2}=r_{1}<r_{3}=\overline{r}_{4}$ and $\overline{r}_{3}=r_{2}<r_{1}+r_{2}<r_{3}=\overline{r}_{4}$.

If one of the Cases #2 to #5 just occurred, it holds that $\overline{r}_{2}\leqslant r_{2}+r_{3}$, that $\overline{r}_{3}=r_{4}$ and that $\overline{r}_{4}=r_{5}$. Since Lemma 6 ‣ On the Worst-Case Complexity of TimSort") proves that $r_{3}+r_{4}<r_{5}$, it follows that $\overline{r}_{2}\leqslant r_{2}+r_{3}<r_{3}+r_{4}<r_{5}=\overline{r}_{4}$ and that $\overline{r}_{3}=r_{4}<r_{3}+r_{4}<r_{5}=\overline{r}_{4}$.

### Lemma 14

At any step during the main loop of TimSort, and for all $i\in\{3,\ldots,h\}$, it holds that $r_{2}+\ldots+r_{i-1}<\phi\,r_{i}$.

### Proof

Like for Lemmas 6 ‣ On the Worst-Case Complexity of TimSort") and 13, we proceed by induction and verify that, if the invariant holds at some point, then it still holds when an update of the stack occurs in one of the five situations labeled #1 to #5 in the algorithm. Let us denote by $\mathcal{S}=(R_{1},\ldots,R_{h})$ the stack just before the update, and by $\overline{\mathcal{S}}=(\overline{R}_{1},\ldots,\overline{R}_{\overline{h}})$ the new state of the stack after the update: If Case #1 just occurred, then we proceed by induction on $i\geqslant 3$. First, for $i=3$, since the conditions for Cases #3 and #4 do not hold in $\mathcal{S}$, we know that $\overline{r}_{2}=r_{1}<r_{2}=\overline{r}_{3}$ and that $\overline{r}_{2}+\overline{r}_{3}=r_{1}+r_{2}<r_{3}=\overline{r}_{4}$. Then, for $i\geqslant 5$, Lemma 6 ‣ On the Worst-Case Complexity of TimSort") states that $r_{i-2}+r_{i-1}<r_{i}$, and therefore if $\overline{r}_{i-1}\leqslant\phi^{-1}\,\overline{r}_{i}$, then $\overline{r}_{2}+\ldots+\overline{r}_{i-1}<(\phi+1)\overline{r}_{i-1}=\phi^{2}\overline{r}_{i-1}\leqslant\phi\overline{r}_{i}$, and if $\overline{r}_{i-1}\geqslant\phi^{-1}\,\overline{r}_{i}$, then $\overline{r}_{i-2}\leqslant(1-\phi^{-1})\ \overline{r}_{i}=\phi^{-2}\,\overline{r}_{i}$, and thus $\overline{r}_{2}+\ldots+\overline{r}_{i-1}<(\phi+1)\,\overline{r}_{i-2}+\overline{r}_{i-1}\leqslant\phi\,\overline{r}_{i-2}+\overline{r}_{i}\leqslant(\phi^{-1}+1)\overline{r}_{i}=\phi\,\overline{r}_{i}$.

Hence, in that case, it holds that $\overline{r}_{2}+\ldots+\overline{r}_{i-1}<\phi\,\overline{r}_{i}$ for all $i\in\{3,\ldots,h\}$.

If one of the Cases #2 to #5 just occurred, it holds that $\overline{r}_{2}\leqslant r_{2}+r_{3}$ and that $\overline{r}_{j}=r_{j+1}$ for all $j\geqslant 3$. It follows that $\overline{r}_{2}+\ldots+\overline{r}_{i-1}\leqslant r_{2}+\ldots+r_{i}<\phi\,r_{i+1}=\overline{r}_{i}$.

### Remark 15

We could also have derived directly Lemma 13 from Lemma 14, by noting that $\phi^{2}\,r_{2}=(\phi+1)r_{2}<\phi\,r_{2}+\phi\,r_{3}<\phi^{2}\,r_{4}$.

### Lemma 16

After every merge that occurred during an ending sequence, we have $r_{1}<\phi^{2}r_{2}$.

### Proof

Once again, we proceed by induction. We denote by $\mathcal{S}=(R_{1},\ldots,R_{h})$ the stack just before an update occurs, and by $\overline{\mathcal{S}}=(\overline{R}_{1},\ldots,\overline{R}_{\overline{h}})$ the new state of the stack after after the update: If Case #2 just occurred, then this update is not the first one within the ending sequence, hence $\overline{r}_{1}=r_{1}<\phi^{2}\,r_{2}<\phi^{2}(r_{2}+r_{3})=\phi^{2}\,\overline{r}_{2}$.

If one of the Cases #2 to #5 just occurred, then $r_{1}\leqslant r_{3}$ and Lemma 14 proves that $r_{2}<\phi\,r_{3}$, which proves that $\overline{r}_{1}=r_{1}+r_{2}<(\phi+1)r_{3}=\phi^{2}\,\overline{r}_{2}$.

### Lemma 17

After every merge triggered by Case $\#2$, we have $r_{2}<\phi^{2}r_{1}$.

### Proof

We denote by $\mathcal{S}=(R_{1},\ldots,R_{h})$ the stack just before an update triggered by Case #2 occurs, and by $\overline{\mathcal{S}}=(\overline{R}_{1},\ldots,\overline{R}_{\overline{h}})$ the new state of the stack after after the update. It must hold that $r_{1}>r_{3}$ and Lemma 14 proves that $r_{2}<\phi\,r_{3}$. It follows that $\overline{r}_{2}=r_{2}+r_{3}<(\phi+1)r_{3}=\phi^{2}\,r_{3}<\phi^{2}\,r_{1}=\phi^{2}\,\overline{r}_{1}$. ∎ Our second step towards proving the first statement of Theorem 11 consists in identifying which sequences of merges an ending sequence may be made of. More precisely, in the proof of Lemma 9 ‣ On the Worst-Case Complexity of TimSort"), we proved that every merge triggered by a case $\#4$ or $\#5$ must be followed by another merge, i.e., it cannot be the final merge of an ending sequence.

We present now a variant of this result, which involves distinguishing between merges triggered by a case $\#2$ and those triggered by a case $\#3$, $\#4$ or $\#5$. Hence, we denote by #X every $\#3$, $\#4$ or $\#5$.

### Lemma 18

No ending sequence contains two conscutive $\#2$'s, nor does it contain a subsequence of the form $\#$X $\#$X $\#2$.

### Proof

Every ending sequence starts with an update $\#$X, where $\#$X is equal to #3, #4 or #5. Hence, it suffices to prove that no ending sequence contains a subsequence $\mathbf{t}$ of the form $\#$X $\#$X #2 or $\#$X #2 #2.

Indeed, for the sake of contradiction, assume that it does, and let $\mathcal{S}=(R_{1},\ldots,R_{h})$ be the stack just before $\mathbf{t}$ starts. We distinguish two cases, depending on the value of $\mathbf{t}$: If $\mathbf{t}$ is the sequence #X #$\textsc{X}\;\#2$, it must hold that $r_{1}+r_{2}<r_{4}$ and that $r_{1}+r_{2}+r_{3}\geqslant r_{5}$, as illustrated in Figure 4 (top). Since Lemma 6 ‣ On the Worst-Case Complexity of TimSort") proves that $r_{3}+r_{4}<r_{5}$, it follows that $r_{1}+r_{2}+r_{3}\geqslant r_{5}>r_{3}+r_{4}>r_{1}+r_{2}+r_{3}$, which is impossible.

If $\mathbf{t}$ is the sequence \#$\textsc{X}\;\#2\;\#2$, it must hold that $r_{1}<r_{3}$ and that $r_{1}+r_{2}\geqslant r_{5}$, as illustrated in Figure 4 (bottom). Since Lemmas 6 ‣ On the Worst-Case Complexity of TimSort") and 13 prove that $r_{3}+r_{4}<r_{5}$ and that $r_{2}<r_{4}$, it comes that $r_{1}+r_{2}\geqslant r_{5}>r_{3}+r_{4}>r_{1}+r_{2}$, which is also impossible.

Figure 4: Applying successively merges #X #2 #2 or #X #X #2 to a stack is impossible.

Our third step consists in modifying the cost allocation we had chosen in Section 3 ‣ On the Worst-Case Complexity of TimSort"), which is not sufficient to prove Theorem 11. Instead, we associate to every run $R$ its *potential*, which depends only on the length $r$ of the run, and is defined as $\mathsf{pot}(r)=3r\log_{2}(r)/2$. We also call *potential* of a set of runs the sum of the potentials of the runs it is formed of, and *potential variation* of a (sequence of) merges the increase in potential caused by these merge(s).

We shall prove that the potential variation of every ending sequence dominates its merge cost, up to a small error term. In order to do this, let us study more precisely individual merges. Below, we respectively denote by $\Delta_{\mathsf{pot}}(\mathbf{m})$ and $\textbf{c}(\mathbf{m})$ the potential variation and the merge cost of a merge $\mathbf{m}$. Then, we say that $\mathbf{m}$ is a *balanced* merge if $\textbf{c}(\mathbf{m})\leqslant\Delta_{\mathsf{pot}}(\mathbf{m})$.

In the next Lemmas, we prove that most merges are balanced or can be grouped into sequences of merges that are balanced overall.

### Lemma 19

Let $\mathbf{m}$ be a merge between two runs $R$ and $R^{\prime}$. If $\phi^{-2}\,r\leqslant r^{\prime}\leqslant\phi^{2}\,r$, then $\mathbf{m}$ is balanced.

### Proof

Let $x=r/(r+r^{\prime})$: we have $\Phi<x<1-\Phi$, where $\Phi=1/(1+\phi^{2})$. Then, observe that $\Delta(\mathbf{m})=3(r+r^{\prime})H(x)/2$, where $H(x)=-x\log_{2}(x)-(1-x)\log_{2}(x)$ is the binary Shannon entropy of a Bernoulli law of parameter $x$. Moreover, the function $z\mapsto H(z)=H(1-z)$ is increasing on $[0,1/2]$. It follows that $H(x)\geqslant H(\Phi)\approx 0.85>2/3$, and therefore that $\Delta(\mathbf{m})>r+r^{\prime}=\textbf{c}(\mathbf{m})$. ∎

### Lemma 20

Let $\mathbf{m}$ be a merge that belongs to some ending sequence. If $\mathbf{m}$ is a merge $\#2$, then $\mathbf{m}$ is balanced and, if $\mathbf{m}$ is followed by another merge $\mathbf{m}^{\prime}$, then $\mathbf{m}^{\prime}$ is also balanced.

### Proof

Lemma 18 ensures that $\mathbf{m}$ was preceded by another merge $\mathbf{m}^{\star}$, which must be a merge $\#$X. Denoting by $\mathcal{S}=(R_{1},\ldots,R_{h})$ the stack just before the merge $\mathbf{m}^{\star}$ occurs, the update $\mathbf{m}$ consists in merging the runs $R_{3}$ and $R_{4}$. Then, it comes that $r_{1}\leqslant r_{3}$ and that $r_{1}+r_{2}>r_{4}$, while Lemma 13 and 14 respectively prove that $r_{3}<r_{4}$ and that $r_{2}<\phi\,r_{3}$. Hence, we both have $r_{3}<r_{4}$ and $r_{4}<r_{1}+r_{2}<(1+\phi)r_{3}=\phi^{2}\,r_{3}$, and Lemma 20 proves that $\mathbf{m}$ is balanced.

Then, if $\mathbf{m}$ is followed by another merge $\mathbf{m}^{\prime}$, Lemma 18 proves that $\mathbf{m}^{\prime}$ is also a merge $\#$X, between runs of respective lengths $r_{1}+r_{2}$ and $r_{3}+r_{4}$. Note that $r_{1}\leqslant r_{3}$ and that $r_{1}+r_{2}>r_{4}$. Since Lemma 13 proves that $r_{2}<r_{4}$ and that $r_{3}<r_{4}$, it follows that $2(r_{1}+r_{2})>2r_{4}>r_{3}+r_{4}>r_{1}+r_{2}$ and, using the fact that $2<1+\phi=\phi^{2}$, Lemma 20 therefore proves that $\mathbf{m}$ is balanced. ∎

### Lemma 21

Let $\mathbf{m}$ be a merge $\#$X between two runs $R_{1}$ and $R_{2}$ such that $r_{1}<\phi^{-2}\,r_{2}$. Then, $\mathbf{m}$ is followed by another merge $\mathbf{m}^{\prime}$, and $\textbf{c}(\mathbf{m})+\textbf{c}(\mathbf{m}^{\prime})\leqslant\Delta_{\mathsf{pot}}(\mathbf{m})+\Delta_{\mathsf{pot}}(\mathbf{m}^{\prime})$.

### Proof

Let $\mathbf{m}^{\star}$ be the update the immediately precedes $\mathbf{m}$. Let also $\mathcal{S}^{\star}=(R^{\star}_{1},\ldots,R^{\star}_{h^{\star}})$, $\mathcal{S}=(R_{1},\ldots,R_{h})$ and $\mathcal{S}^{\prime}=(R^{\prime}_{1},\ldots,R^{\prime}_{h^{\prime}})$ be the respective states of the stack just before $\mathbf{m}^{\star}$ occurs, just before $\mathbf{m}$ occurs and just after $\mathbf{m}$ occurs.

Since $r_{1}<\phi^{-2}\,r_{2}$, Lemma 17 proves that $\mathbf{m}^{\star}$ is either an update #1 or a merge $\#$X. In both cases, it follows that $r_{2}<r_{3}$ and that $r_{2}+r_{3}<r_{4}$. Indeed, if $\mathbf{m}^{\star}$ is an update #1, then we must have $r_{2}=r^{\star}_{1}<r^{\star}_{2}=r_{3}$ and $r_{2}+r_{3}=r^{\star}_{1}+r^{\star}_{2}<r^{\star}_{3}=r_{4}$, and if $\mathbf{m}^{\prime}$ is a merge $\#$X, then Lemmas 6 ‣ On the Worst-Case Complexity of TimSort") and 13 respectively prove that $r_{2}+r_{3}=r^{\star}_{3}+r^{\star}_{4}<r^{\star}_{5}=r_{4}$ and that $r_{2}=r^{\star}_{3}<r^{\star}_{4}=r_{3}$.

Then, since $\mathbf{m}$ is a merge $\#$X, we also know that $r_{1}\leqslant r_{3}$. Since $r_{1}<\phi^{-2}\,r_{2}$ and $r_{2}+r_{3}<r_{4}$, this means that $r_{1}+r_{2}\geqslant r_{3}$. It follows that $r^{\prime}_{2}=r_{3}\leqslant r_{1}+r_{2}=r^{\prime}_{1}$ and that $r^{\prime}_{1}=r_{1}+r_{2}\leqslant r_{2}+r_{3}<r_{4}=r^{\prime}_{3}$. Consequently, the merge $\mathbf{m}$ must be followed by a merge $\mathbf{m}^{\prime}$, which is triggered by case #3.

Finally, let $x=r_{1}/(r_{1}+r_{2})$ and $y=(r_{1}+r_{2})/(r_{1}+r_{2}+r_{3})$. It comes that $\textbf{c}(\mathbf{m})+\textbf{c}(\mathbf{m}^{\prime})=(r_{1}+r_{2}+r_{3})(1+y)$ and that $\Delta_{\mathsf{pot}}(\mathbf{m})+\Delta_{\mathsf{pot}}(\mathbf{m}^{\prime})=3(r_{1}+r_{2}+r_{3})\left(yH(x)+H(y)\right)\!/2$, where we recall that $H$ is the binary Shannon entropy function, with $H(t)=-t\log_{2}(t)-(1-t)\log_{2}(t)$. The above inequalities about $r_{1}$, $r_{2}$ and $r_{3}$ prove that $0\leqslant 2-1/y\leqslant x\leqslant 1/(1+\phi^{2})$. Since $H$ is increasing on the interval $[0,1/2]$, and since $1+\phi^{2}\geqslant 2$, it follows that $\Delta_{\mathsf{pot}}(\mathbf{m})+\Delta_{\mathsf{pot}}(\mathbf{m}^{\prime})\geqslant 3(r_{1}+r_{2}+r_{3})\left(yH(2-1/y)+H(y)\right)\!/2$.

Hence, let $F(y)=3\left(yH(2-1/y)+H(y)\right)\!/2-(1+y)$. We shall prove that $F(y)\geqslant 0$ for all $y\geqslant 0$ such that $0\leqslant 2-1/y\leqslant 1/(1+\phi^{2})$, i.e., such that $1/2\leqslant y\leqslant(1+\phi^{2})/(1+2\phi^{2})$. To that mean, observe that $F^{\prime\prime}(y)=3/\!\left((1-y)(1-2y)\ln\right)<0$ for all $y\in(1/2,1)$. Thus, $F$ is concave on $(1/2,1)$. Since $F(1/2)=0$ and $F(3/4)=1/2$, it follows that $F(y)\geqslant 0$ for all $y\in[1/2,3/4]$. Checking that $(1+\phi^{2})/(1+2\phi^{2})<3/4$ completes the proof. ∎

### Lemma 22

Let $\mathbf{m}$ be the first merge of the ending sequence associated with a run $R$. Let $R_{1}$ and $R_{2}$ be the runs that $\mathbf{m}$ merges together. If $r_{1}>\phi^{2}\,r_{2}$, it holds that $\textbf{c}(\mathbf{m})\leqslant\Delta_{\mathsf{pot}}(\mathbf{m})+r$.

### Proof

By definition of $\mathbf{m}$, we have $R=R_{1}$, and thus $r=r_{1}\geqslant r_{2}$. Hence, it follows that $\Delta_{\mathsf{pot}}(\mathbf{m})=r\log((r+r_{2})/r)+r_{2}\log((r+r_{2})/r_{2})\geqslant r_{2}\log((r+r_{2})/r_{2})\geqslant r_{2}=\textbf{c}(\mathbf{m})-r$. ∎

### Proposition 23

Let $\mathbf{s}$ be the ending sequence associated with a run $R$, and let $\Delta_{\mathsf{pot}}(\mathbf{s})$ and $\textbf{c}(\mathbf{s})$ be its potential variation and its merge cost. It holds that $\textbf{c}(\mathbf{s})\leqslant\Delta_{\mathsf{pot}}(\mathbf{s})+r$.

### Proof

Let us group the merges of $\mathbf{s}$ as follows: if $\mathbf{m}$ is an unbalanced merge $\#$X between two runs $R_{1}$ and $R_{2}$ such that $r_{1}<r_{2}$, then $\mathbf{m}$ is followed by another merge $\mathbf{m}^{\prime}$, and we group $\mathbf{m}$ and $\mathbf{m}^{\prime}$ together; otherwise, and if $\mathbf{m}$ has not been grouped with its predecessor, it forms its own group.

In case, Lemma 22 ensures that $\mathbf{m}^{\prime}$ itself cannot be grouped with another merge. This means that our grouping is unambiguous.

Then, let $\mathbf{g}$ be such a group, with potential variation $\Delta_{\mathsf{pot}}(\mathbf{g})$ and merge cost $\textbf{c}(\mathbf{g})$. Lemmas 19 to 22 prove that $\textbf{c}(\mathbf{g})\leqslant\Delta_{\mathsf{pot}}(\mathbf{g})+r$ if $\mathbf{g}$ is formed of the first merge of $\mathbf{s}$ only, and that $\textbf{c}(\mathbf{g})\leqslant\Delta_{\mathsf{pot}}(\mathbf{g})$ in all other cases. Proposition 23 follows. ∎ Collecting all the above results is enough to prove Theorem 11. First, like in Section 3 ‣ On the Worst-Case Complexity of TimSort"), computing the run decomposition and merging runs in starting sequences has a cost $\mathcal{O}(n)$, and the final merges of line 11 may be taken care of by Remark 5 ‣ On the Worst-Case Complexity of TimSort"). Second, by Proposition 23, ending sequences have a merge cost dominated by $\Delta_{\mathsf{pot}}+n$, where $\Delta_{\mathsf{pot}}$ is the total variation of potential during the algorithm. Observing that $\Delta_{\mathsf{pot}}=-3/2\sum_{i=1}^{\rho}r_{i}\log_{2}(r_{i}/n)=-3n\mathcal{H}/2$ concludes the proof of the theorem.

## About the Java version of TimSort

Figure 5: Execution of the main loop of Java’s TimSort (Algorithm 3, without merge case #5, at line 3), with the lengths of the runs in $\rundecomp$ being. When the second to last run (of length 8) is pushed onto the stack, the while loop of line 3 stops after only one merge, breaking the invariant (in red), unlike what we see in Figure 2 using the Python version of TimSort.

Algorithm 2 (and therefore Algorithm 3 ‣ On the Worst-Case Complexity of TimSort")) does not correspond to the original TimSort. Before release 3.4.4 of Python, the second part of the condition (in blue) in the test at line 2 of merge_collapse (and therefore merge case #5 of Algorithm 3 ‣ On the Worst-Case Complexity of TimSort")) was missing. This version of the algorithm worked fine, meaning that it did actually sort arrays, but the invariant given by Equation did not hold. Figure 5 illustrates the difference caused by the missing condition when running Algorithm 3 ‣ On the Worst-Case Complexity of TimSort") on the same input as in Figure 2.

This was discovered by de Gouw et al. when trying to prove the correctness of the Java implementation of TimSort (which is the same as in the earlier versions of Python). And since the Java version of the algorithm uses the (wrong) invariant to compute the maximum size of the stack used to store the runs, the authors were able to build a sequence of runs that causes the Java implementation of TimSort to crash. They proposed two solutions to fix TimSort: reestablish the invariant, which led to the current Python version, or keep the original algorithm and compute correct bounds for the stack size, which is the solution that was chosen in Java 9 (note that this is the second time these values had to be changed). To do the latter, the developers used the claim in that the invariant cannot be violated for two consecutive runs on the stack, which turns out to be false,^33^ 3 This is the consequence of a small error in the proof of their Lemma 1. The constraint $C_{1}>C_{2}$ has no reason to be. Indeed, in our example, we have $C_{1}=25$ and $C_{2}=31$. as illustrated in Figure 6. Thus, it is still possible to cause the Java implementation to fail: it uses a stack of runs of size at most 49 and we were able to compute an example requiring a stack of size 50, causing an error at runtime in Java's sorting method.

Figure 6: Execution of the main loop of the Java version of TimSort (without merge case #5, at line 3 of Algorithm 3), with the lengths of the runs in $\rundecomp$ being. When the algorithm stops, the invariant is violated twice, for consecutive runs (in red).

Even if the bug we highlighted in Java's TimSort is very unlikely to happen, this should be corrected. And, as advocated by de Gouw et al. and Tim Peters himself,^44^ 4 Here is the discussion about the correction in Python: we strongly believe that the best solution would be to correct the algorithm as in the current version of Python, in order to keep it clean and simple. However, since this is the implementation of Java's sort for the moment, there are two questions we would like to tackle: Does the complexity analysis holds without the missing condition? And, can we compute an actual bound for the stack size? We first address the complexity question. It turns out that the missing invariant was a key ingredient for having a simple and elegant proof.

### Proposition 24

^††^margin: Full proof in Section A.1.1.

At any time during the main loop of Java's TimSort, if the stack of runs is $(R_{1},\ldots,R_{h})$ then we have $r_{3}<r_{4}<\ldots<r_{h}$ and, for all $i\geqslant 3$, we have $(2+\sqrt{7})r_{i}\geqslant r_{2}+\ldots+r_{i-1}$.

### Proof ideas

The proof of Proposition 24 is much more technical and difficult than insightful, and therefore we just summarize its main steps. As in previous sections, this proof relies on several inductive arguments, using both inductions on the number of merges performed, on the stack size and on the run sizes. The inequalities $r_{3}<r_{4}<\ldots<r_{h}$ come at once, hence we focus on the second part of Proposition 24.

Since separating starting and ending sequences was useful in Section 4, we first introduce the notion of *stable* stacks: a stack $\mathcal{S}$ is stable if, when operating on the stack $\mathcal{S}=(R_{1},\ldots,R_{h})$, Case #1 is triggered (i.e. Java's TimSort is about to perform a *run push* operation).

We also call *obstruction indices* the integers $i\geqslant 3$ such that $r_{i}\leqslant r_{i-1}+r_{i-2}$: although they do not exist in Python's TimSort, they may exist, and even be consecutive, in Java's TimSort. We prove that, if $i-k,i-k+1,\ldots,i$ are obstruction indices, then the stack sizes $r_{i-k-2},\ldots,r_{i}$ grow "at linear speed". For instance, in the last stack of Figure 6, obstruction indices are $4$ and $5$, and we have $r_{2}=28$, $r_{3}=r_{2}+28$, $r_{4}=r_{3}+27$ and $r_{5}=r_{4}+26$.

Finally, we study so-called *expansion functions*, i.e. functions $f:\mapsto\mathbb{R}$ such that, for every stable stack $\mathcal{S}=(R_{1},\ldots,R_{h})$, we have $r_{2}+\ldots+r_{h-1}\leqslant r_{h}f(r_{h-1}/r_{h})$. We exhibit an explicit function $f$ such that $f(x)\leqslant 2+\sqrt{7}$ for all $x\in$, and we prove by induction on $r_{h}$ that $f$ is an expansion function, from which we deduce Proposition 24. ∎ Once Proposition 24 is proved, we easily recover the following variant of Lemmas 6 ‣ On the Worst-Case Complexity of TimSort") and 10 ‣ On the Worst-Case Complexity of TimSort").

### Lemma 25

At any time during the main loop of Java's TimSort, if the stack is $(R_{1},\ldots,R_{h})$ then we have $r_{2}/(2+\sqrt{7})\leqslant r_{3}<r_{4}<\ldots<r_{h}$ and, for all $i\geqslant j\geqslant 3$, we have $r_{i}\geqslant\delta^{i-j-4}r_{j}$, where $\delta=\left(5/(2+\sqrt{7})\right)^{1/5}>1$. Furthermore, at any time during an ending sequence, including just before it starts and just after it ends, we have $r_{1}\leqslant(2+\sqrt{7})r_{3}$.

### Proof

The inequalities $r_{2}/(2+\sqrt{7})\leqslant r_{3}<r_{4}<\ldots<r_{h}$ are just a (weaker) restatement of Proposition 24. Then, for $j\geqslant 3$, we have $(2+\sqrt{7})r_{j+5}\geqslant r_{j}+\ldots+r_{j+4}\geqslant 5r_{j}$, i.e. $r_{j+5}\geqslant\delta^{5}r_{j}$, from which one gets that $r_{i}\geqslant\delta^{i-j-4}r_{j}$.

Finally, we prove by induction that $r_{1}\leqslant(2+\sqrt{7})r_{3}$ during ending sequences. First, when the ending sequence starts, $r_{1}<r_{3}\leqslant(2+\sqrt{7})r_{3}$. Before any merge during this sequence, if the stack is $\mathcal{S}=(R_{1},\ldots R_{h})$, then we denote by $\overline{\mathcal{S}}=(\overline{R}_{1},\ldots,\overline{R}_{h-1})$ the stack after the merge. If the invariant holds before the merge, in Case #2, we have $\overline{r}_{1}=r_{1}\leqslant(2+\sqrt{7})r_{3}\leqslant(2+\sqrt{7})r_{4}=(2+\sqrt{7})\overline{r}_{3}$; and using Proposition 24 in Cases #3 and #4, we have $\overline{r}_{1}=r_{1}+r_{2}$ and $r_{1}\leqslant r_{3}$, hence $\overline{r}_{1}=r_{1}+r_{2}\leqslant r_{2}+r_{3}\leqslant(2+\sqrt{7})r_{4}=(2+\sqrt{7})\overline{r}_{3}$, concluding the proof. ∎ We can then recover a proof of complexity for the Java version of TimSort, by following the same proof as in Sections 3 ‣ On the Worst-Case Complexity of TimSort") and 4, but using Lemma 25 instead of Lemmas 6 ‣ On the Worst-Case Complexity of TimSort") and 10 ‣ On the Worst-Case Complexity of TimSort").

### Theorem 26

The complexity of Java's TimSort on inputs of size $n$ with $\rho$ runs is $\mathcal{O}(n+n\log\rho)$.

Another question is that of the stack size requirements of Java's TimSort, i.e. computing $h_{\max}$. A first result is the following immediate corollary of Lemma 25.

### Corollary 27

On an input of size $n$, Java's TimSort will create a stack of runs of maximal size $h_{\max}\leqslant 7+\log_{\delta}(n)$, where $\delta=\left(5/(2+\sqrt{7})\right)^{1/5}$.

### Proof

At any time during the main loop of Java's TimSort on an input of size $n$, if the stack is $(R_{1},\ldots,R_{h})$ and $h\geqslant 3$, it follows from Lemma 25 that $n\geqslant r_{h}\geqslant\delta^{h-7}r_{3}\geqslant\delta^{h-7}$. ∎ Unfortunately, for integers smaller than $2^{31}$, Corollary 27 only proves that the stack size will never exceed $347$. However, in the comments of Java's implementation of TimSort,^55^ 5 Comment at line 168: there is a remark that keeping a short stack is of some importance, for practical reasons, and that the value chosen in Python -- $85$ -- is "too expensive". Thus, in the following, we go to the extent of computing the optimal bound. It turns out that this bound cannot exceed $86$ for such integers. This bound could possibly be refined slightly, but definitely not to the point of competing with the bound that would be obtained if the invariant of Equation were correct. Once more, this suggests that implementing the new version of TimSort in Java would be a good idea, as the maximum stack height is smaller in this case.

### Theorem 28

^††^margin: Full proof inxx Sections A.1.2xx and A.1.3.xx On an input of size $n$, Java's TimSort will create a stack of runs of maximal size $h_{\max}\leqslant 3+\log_{\Delta}(n)$, where $\Delta=(1+\sqrt{7})^{1/5}$. Furthermore, if we replace $\Delta$ by any real number $\Delta^{\prime}>\Delta$, the inequality fails for all large enough $n$.

### Proof ideas

The first part of Theorem 28 is proved as follows. Ideally, we would like to show that $r_{i+j}\geqslant\Delta^{j}r_{i}$ for all $i\geqslant 3$ and some fixed integer $j$. However, these inequalities do not hold for all $i$. Yet, we prove that they hold if $i+2$ and $i+j+2$ are not obstruction indices, and $i+j+1$ is an obstruction index, and it follows quickly that $r_{h}\geqslant\Delta^{h-3}$.

The optimality of $\Delta$ is much more difficult to prove. It turns out that the constants $2+\sqrt{7}$, $(1+\sqrt{7})^{1/5}$, and the expansion function referred to in the proof of Proposition 24 were constructed as least fixed points of non-decreasing operators, although this construction needed not be explicit for using these constants and function. Hence, we prove that $\Delta$ is optimal by inductively constructing sequences of run sizes that show that $\limsup\{\log(r_{h})/h\}\geqslant\Delta$; much care is required for proving that our constructions are indeed feasible. ∎

## Conclusion

At first, when we learned that Java's QuickSort had been replaced by a variant of MergeSort, we thought that this new algorithm -- TimSort -- should be really fast and efficient in practice, and that we should look into its average complexity to confirm this from a theoretical point of view. Then, we realized that its worst-case complexity had not been formally established yet and we first focused on giving a proof that it runs in $\mathcal{O}(n\log n)$, which we wrote in a preprint. In the present article, we simplify this preliminary work and provide a short, simple and self-contained proof of TimSort's complexity, which sheds some light on the behavior of the algorithm. Based on this description, we were also able to answer positively a natural question, which was left open so far: does TimSort runs in $\mathcal{O}(n+n\log\rho)$, where $\rho$ is the number of runs? We hope our theoretical work highlights that TimSort is actually a very good sorting algorithm. Even if all its fine-tuned heuristics are removed, the dynamics of its merges, induced by a small number of local rules, results in a very efficient global behavior, particularly well suited for *almost sorted* inputs.

Besides, we want to stress the need for a thorough algorithm analysis, in order to prevent errors and misunderstandings. As obvious as it may sound, the three consecutive mistakes on the stack height in Java illustrate perfectly how the best ideas can be spoiled by the lack of a proper complexity analysis.

Finally, following, we would like to emphasize that there seems to be no reason not to use the recent version of TimSort, which is efficient in practice, formally certified and whose optimal complexity is easy to understand.
