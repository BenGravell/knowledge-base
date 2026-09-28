<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Worst-Case Complexity of TimSort

Topics include Sorting algorithms, Algorithm analysis.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes the worst-case complexity of Python and Java TimSort, proves an adaptive bound for Python, and identifies a Java implementation bug.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

TimSort is an intriguing sorting algorithm designed in 2002 for Python, whose worst-case complexity was announced, but not proved until our recent preprint. In fact, there are two slightly different versions of TimSort that are currently implemented in Python and in Java respectively. We propose a pedagogical and insightful proof that the Python version runs in O(nlog n). The approach we use in the analysis also applies to the Java version, although not without very involved technical details. As a byproduct of our study, we uncover a bug in the Java implementation that can cause the sorting method to fail during the execution. We also give a proof that Python's TimSort running time is in O(n + nlog rho), where rho is the number of runs (i.e. maximal monotonic sequences), which is quite a natural parameter here and part of the explanation for the good behavior of TimSort on partially sorted inputs.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

TimSort is a sorting algorithm designed in 2002 by Tim Peters, for use in the Python programming language. It was thereafter implemented in other well-known programming languages such as Java. The algorithm includes many implementation optimizations, a few heuristics and some refined tuning, but its high-level principle is rather simple: The sequence $S$ to be sorted is first decomposed greedily into monotonic runs (i.e. nonincreasing or nondecreasing subsequences of $S$ as depicted on Figure 1), which are then merged pairwise according to some specific rules.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

$S=(~\underbrace{12,10,7,5}_{\text{first run}},~\underbrace{7,10,14,25,36}_{\text{second run}},~\underbrace{3,5,11,14,15,21,22}_{\text{third run}},~\underbrace{20,15,10,8,5,1}_{\text{fourth run}}~)$ Figure 1: A sequence and its run decomposition computed by TimSort: for each run, the first two elements determine if it is increasing or decreasing, then it continues with the maximum number of consecutive elements that preserves the monotonicity.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The idea of starting with a decomposition into runs is not new, and already appears in Knuth's NaturalMergeSort, where increasing runs are sorted using the same mechanism as in MergeSort. Other merging strategies combined with decomposition into runs appear in the literature, such as the MinimalSort of (see also for other considerations on the same topic). All of them have nice properties: they run in $\mathcal{O}(n\log n)$ and even $\mathcal{O}(n+n\log\rho)$, where $\rho$ is the number of runs, which is optimal in the model of sorting by comparisons, using the classical counting argument for lower bounds. And yet, among all these merge-based algorithms, TimSort was favored in several very popular programming languages, which suggests that it performs quite well in practice.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

TimSort running time was implicitly assumed to be $\mathcal{O}(n\log n)$, but our unpublished preprint contains, to our knowledge, the first proof of it. This was more than ten years after TimSort started being used instead of QuickSort in several major programming languages. The growing popularity of this algorithm invites for a careful theoretical investigation. In the present paper, we make a thorough analysis which provides a better understanding of the inherent qualities of the merging strategy of TimSort. Indeed, it reveals that, even without its refined heuristics,^11^ 1 These heuristics are useful in practice, but do not improve the worst-case complexity of the algorithm. this is an effective sorting algorithm, computing and merging runs on the fly, using only local properties to make its decisions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We first propose in Section 3 ‣ On the Worst-Case Complexity of TimSort") a new pedagogical and self-contained exposition that TimSort runs in time $\mathcal{O}(n+n\log n)$, which we want both clear and insightful.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In fact, we prove a stronger statement: on an input consisting of $\rho$ runs of respective lengths $r_{1},\ldots,r_{\rho}$, we establish that TimSort runs in $\mathcal{O}(n+n\mathcal{H})\subseteq\mathcal{O}(n+n\log\rho)\subseteq\mathcal{O}(n+n\log n)$, where $\mathcal{H}=H(r_{1}/n,\ldots,r_{\rho}/n)$ and $H(p_{1},\ldots,p_{\rho})=-\sum_{i=1}^{\rho}p_{i}\log_{2}(p_{i})$ is the binary Shannon entropy.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We then refine this approach, in Section 4, to derive precise bounds on the worst-case running time of TimSort, and we prove that it is equal to $1.5n\mathcal{H}+\mathcal{O}(n)$. This answers positively a conjecture of. Of course, the first result follows from the second, but since we believe that each one is interesting on its own, we devote one section to each of them.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

To introduce our last contribution, we need to look into the evolution of the algorithm: there are actually not one, but two main versions of TimSort. The first version of the algorithm contained a flaw, which was spotted: while the input was correctly sorted, the algorithm did not behave as announced (because of a broken invariant). This was discovered by De Gouw and his co-authors while trying to prove formally the correctness of TimSort. They proposed a simple way to patch the algorithm, which was quickly adopted in Python, leading to what we consider to be the real TimSort. This is the one we analyze in Sections 3 ‣ On the Worst-Case Complexity of TimSort") and 4. On the contrary, Java developers chose to stick with the first version of TimSort, and adjusted some tuning values (which depend on the broken invariant; this is explained in Sections 2 and 5) to prevent the bug exposed. Motivated by its use in Java, we explain in Section 5 how, at the expense of very complicated technical details, the elegant proofs of the Python version can be twisted to prove the same results for this older version.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

While working on this analysis, we discovered yet another error in the correction made in Java. Thus, we compute yet another patch, even if we strongly agree that the algorithm proposed and formally proved in (the one currently implemented in Python) is a better option.

<!-- chunk {"id": "body-0013", "role": "body", "section": "TimSort core algorithm", "weight": 1.0} -->

Input: A sequence S to sort Result: The sequence S is sorted into a single run, which remains on the stack. Note: The function merge_force_collapse repeatedly pops the last two runs on the stack $\runstack$, merges them and pushes the resulting run back on the stack.

<!-- chunk {"id": "body-0014", "role": "body", "section": "TimSort core algorithm", "weight": 1.0} -->

1 $\rundecomp\leftarrow$ a run decomposition of S 2 $\runstack\leftarrow$ an empty stack 3 while $\rundecomp\neq\emptyset$ do // main loop of TimSort 4 remove a run r from $\rundecomp$ and push r onto $\runstack$ 5 merge_collapse($\runstack$) 6 if $\height(\runstack)\neq 1$ then // the height of $\runstack$ is its number of runs 7 merge_force_collapse($\runstack$) Algorithm 1 TimSort (Python 3.6.5) The idea of TimSort is to design a merge sort that can exploit the possible "non randomness" of the data, without having to detect it beforehand and without damaging the performances on random-looking data. This follows the ideas of adaptive sorting (see for a survey on taking presortedness into account when designing and analyzing sorting algorithms).

<!-- chunk {"id": "body-0015", "role": "body", "section": "TimSort core algorithm", "weight": 1.0} -->

The first feature of TimSort is to work on the natural decomposition of the input sequence into maximal runs. In order to get larger subsequences, TimSort allows both nondecreasing and decreasing runs, unlike most merge sort algorithms.

<!-- chunk {"id": "body-0016", "role": "body", "section": "TimSort core algorithm", "weight": 1.0} -->

Then, the merging strategy of TimSort (Algorithm 1) is quite simple yet very efficient. The runs are considered in the order given by the run decomposition and successively pushed onto a stack. If some conditions on the size of the topmost runs of the stack are not satisfied after a new run has been pushed, this can trigger a series of merges between pairs of runs at the top or right under. And at the end, when all the runs in the initial decomposition have been pushed, the last operation is to merge the remaining runs two by two, starting at the top of the stack, to get a sorted sequence. The conditions on the stack and the merging rules are implemented in the subroutine called merge_collapse detailed in Algorithm 2. This is what we consider to be TimSort core mechanism and this is the main focus of our analysis.

<!-- chunk {"id": "body-0017", "role": "body", "section": "TimSort core algorithm", "weight": 1.0} -->

Input: A stack of runs $\runstack$ Result: The invariant of Equations and is established. Note: The runs on the stack are denoted by $\runstack\dots\runstack[\height(\runstack)]$, from top to bottom. The length of run $\runstack$[i] is denoted by ri. The blue highlight indicates that the condition was not present in the original version of TimSort (this will be discussed in section 5).

<!-- chunk {"id": "body-0018", "role": "body", "section": "TimSort core algorithm", "weight": 1.0} -->

1 while $\height(\runstack)>1$ do 2 $n\leftarrow\height(\runstack)-2$ 3 if (n > 0 and r3 ≤ r2 + r1) or (n > 1 and r4 ≤ r3 + r2) then 5 merge runs $\runstack$ and $\runstack$ on the stack 6 else merge runs $\runstack$ and $\runstack$ on the stack 8 merge runs $\runstack$ and $\runstack$ on the stack Algorithm 2 The merge_collapse procedure (Python 3.6.5) Another strength of TimSort is the use of many effective heuristics to save time, such as ensuring that the initial runs are not to small thanks to an insertion sort or using a special technique called "galloping" to optimize the merges. However, this does not interfere with our analysis and we will not discuss this matter any further.

<!-- chunk {"id": "body-0019", "role": "body", "section": "TimSort core algorithm", "weight": 1.0} -->

Let us have a closer look at Algorithm 2 which is a pseudo-code transcription of the merge_collapse procedure found in the latest version of Python (3.6.5). To illustrate its mechanism, an example of execution of the main loop of TimSort (lines 1-1 of Algorithm 1) is given in Figure 2. As stated in its note, Tim Peter's idea was that: > "The thrust of these rules when they trigger merging is to balance the run lengths as closely as possible, while keeping a low bound on the number of runs we have to remember."

<!-- chunk {"id": "body-0020", "role": "body", "section": "TimSort core algorithm", "weight": 1.0} -->

To achieve this, the merging conditions of merge_collapse are designed to ensure that the following invariant^22^ 2 Actually the invariant is only stated for the 3 topmost runs of the stack. is true at the end of the procedure: This means that the runs lengths $\mathsf{r}_{i}$ on the stack grow at least as fast as the Fibonacci numbers and, therefore, that the height of the stack stays logarithmic (see Lemma 10 ‣ On the Worst-Case Complexity of TimSort"), section 3 ‣ On the Worst-Case Complexity of TimSort")).

<!-- chunk {"id": "body-0021", "role": "body", "section": "TimSort core algorithm", "weight": 1.0} -->

Note that the bound on the height of the stack is not enough to justify the $\mathcal{O}(n\log n)$ running time of TimSort. Indeed, without the smart strategy used to merge the runs "on the fly", it is easy to build an example using a stack containing at most two runs and that gives a $\Theta(n^{2})$ complexity: just assume that all runs have size two, push them one by one onto a stack and perform a merge each time there are two runs in the stack.

<!-- chunk {"id": "body-0022", "role": "body", "section": "TimSort core algorithm", "weight": 1.0} -->

We are now ready to proceed with the analysis of TimSort complexity. As mentioned earlier, Algorithm 2 does not correspond to the first implementation of TimSort in Python, nor to the current one in Java, but to the latest Python version. The original version will be discussed in details later, in Section 5.

<!-- chunk {"id": "body-0023", "role": "body", "section": "TimSort runs in $\\mathcal{O}(n\\log n)$", "weight": 1.0} -->

At the first release of TimSort, a time complexity of $\mathcal{O}(n\log n)$ was announced with no element of proof given. It seemed to remain unproved until our recent preprint, where we provide a confirmation of this fact, using a proof which is not difficult but a bit tedious. This result was refined later, where the authors provide lower and upper bounds, including explicit multiplicative constants, for different merge sort algorithms.

<!-- chunk {"id": "body-0024", "role": "body", "section": "TimSort runs in $\\mathcal{O}(n\\log n)$", "weight": 1.0} -->

Our main concern is to provide an insightful proof of the complexity of TimSort, in order to highlight how well designed is the strategy used to choose the order in which the merges are performed. The present section is more detailed than the following ones as we want it to be self-contained once TimSort has been translated into Algorithm 3 ‣ On the Worst-Case Complexity of TimSort") (see below).

<!-- chunk {"id": "body-0025", "role": "body", "section": "TimSort runs in $\\mathcal{O}(n\\log n)$", "weight": 1.0} -->

Input: A sequence to S to sort Result: The sequence S is sorted into a single run, which remains on the stack. Note: At any time, we denote the height of the stack $\runstack$ by h and its ith top-most run (for 1 ≤ i ≤ h) by Ri. The size of this run is denoted by ri.

<!-- chunk {"id": "body-0026", "role": "body", "section": "TimSort runs in $\\mathcal{O}(n\\log n)$", "weight": 1.0} -->

1 $\rundecomp\leftarrow$ the run decomposition of S 2 $\runstack\leftarrow$ an empty stack 3 while $\rundecomp\neq\emptyset$ do // main loop of TimSort 4 remove a run r from $\rundecomp$ and push r onto $\runstack$ // #1 6 if h ≥ 3 and r1 > r3 then merge the runs R2 and R3 // #2 7 else if h ≥ 2 and r1 ≥ r2 then merge the runs R1 and R2 // #3 8 else if h ≥ 3 and r1 + r2 ≥ r3 then merge the runs R1 and R2 // #4 9 else if h ≥ 4 and r2 + r3 ≥ r4 then merge the runs R1 and R2 // #5 11 while h ≠ 1 do merge the runs R1 and R2 Algorithm 3 TimSort: translation of Algorithm 1 and Algorithm 2 As our analysis is about to demonstrate, in terms of worst-case complexity, the good performances of TimSort do not rely on the way merges are performed.

<!-- chunk {"id": "body-0027", "role": "body", "section": "TimSort runs in $\\mathcal{O}(n\\log n)$", "weight": 1.0} -->

Thus we choose to ignore their many optimizations and consider that merging two runs of lengths $r$ and $r^{\prime}$ requires both $r+r^{\prime}$ element moves and $r+r^{\prime}$ element comparisons. Therefore, to quantify the running time of TimSort, we only take into account the number of comparisons performed.

<!-- chunk {"id": "body-0028", "role": "body", "section": "TimSort runs in $\\mathcal{O}(n\\log n)$", "weight": 1.0} -->

In particular, aiming at computing precise bounds on the running time of TimSort, we follow and define the *merge cost* for merging two runs of lengths $r$ and $r^{\prime}$ as $r+r^{\prime}$, i.e., the length of the resulting run. Henceforth, we will identify the time spent for merging two runs with the merge cost of this merge.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Claim 4", "weight": 1.0} -->

For any input, Algorithms 1 and 3 ‣ On the Worst-Case Complexity of TimSort") perform the same comparisons.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Proving Theorem 2 ‣ On the Worst-Case Complexity of TimSort") only requires analyzing the *main loop* of the algorithm (lines 3 to 10). Indeed, computing the run decomposition (line 1) can be done on the fly, by a greedy algorithm, in time linear in $n$, and the *final loop* (line 11) might be performed in the main loop by adding a fictitious run of length $n+1$ at the end of the decomposition.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 5", "weight": 1.0} -->

In the sequel, for the sake of readability, we also omit checking that $h$ is large enough to trigger the cases #2 to #5. Once again, such omissions are benign, since adding fictitious runs of respective lengths $8n$, $4n$, $2n$ and $n$ (in this order) at the beginning of the decomposition would ensure that $h\geqslant 4$ during the whole loop.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 5", "weight": 1.0} -->

We sketch now the main steps of our proof, i.e., the amortized analysis of the main loop. A first step is to establish the invariant and, ensuring an exponential growth of the run lengths within the stack.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Elements of the input array are easily identified by their starting position in the array, so we consider them as well-defined and distinct entities (even if they have the same value). The *height* of an element in the stack of runs is the number of runs that are below it in the stack: the elements belonging to the run $R_{i}$ in the stack $\mathcal{S}=(R_{1},\ldots,R_{h})$ have height $h-i$, and we recall that the length of the run $R_{i}$ is denoted by $r_{i}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Refined analysis and precise worst-case complexity", "weight": 1.0} -->

The analysis performed in Section 3 ‣ On the Worst-Case Complexity of TimSort") proves that TimSort sorts arrays in time $\mathcal{O}(n+n\mathcal{H})$. Looking more closely at the constants hidden in the $\mathcal{O}$ notation, we may in fact prove that the cost of merges performed during an execution of TimSort is never greater than $6n\mathcal{H}+\mathcal{O}(n)$. However, the lower bound provided by Proposition 3 ‣ On the Worst-Case Complexity of TimSort") only proves that the cost of these merges must be at least $n\mathcal{H}+\mathcal{O}(n)$. In addition, there exist sorting algorithms whose merge cost is exactly $n\mathcal{H}+\mathcal{O}(n)$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Refined analysis and precise worst-case complexity", "weight": 1.0} -->

Hence, TimSort is optimal only up to a multiplicative constant. We focus now on finding the least real constant $\kappa$ such that the merge cost of TimSort is at most $\kappa n\mathcal{H}+\mathcal{O}(n)$, thereby proving a conjecture of.

<!-- chunk {"id": "body-0036", "role": "body", "section": "About the Java version of TimSort", "weight": 1.0} -->

Algorithm 2 (and therefore Algorithm 3 ‣ On the Worst-Case Complexity of TimSort")) does not correspond to the original TimSort. Before release 3.4.4 of Python, the second part of the condition (in blue) in the test at line 2 of merge_collapse (and therefore merge case #5 of Algorithm 3 ‣ On the Worst-Case Complexity of TimSort")) was missing. This version of the algorithm worked fine, meaning that it did actually sort arrays, but the invariant given by Equation did not hold. Figure 5 illustrates the difference caused by the missing condition when running Algorithm 3 ‣ On the Worst-Case Complexity of TimSort") on the same input as in Figure 2.

<!-- chunk {"id": "body-0037", "role": "body", "section": "About the Java version of TimSort", "weight": 1.0} -->

This was discovered by de Gouw et al. when trying to prove the correctness of the Java implementation of TimSort (which is the same as in the earlier versions of Python). And since the Java version of the algorithm uses the (wrong) invariant to compute the maximum size of the stack used to store the runs, the authors were able to build a sequence of runs that causes the Java implementation of TimSort to crash. They proposed two solutions to fix TimSort: reestablish the invariant, which led to the current Python version, or keep the original algorithm and compute correct bounds for the stack size, which is the solution that was chosen in Java 9 (note that this is the second time these values had to be changed). To do the latter, the developers used the claim in that the invariant cannot be violated for two consecutive runs on the stack, which turns out to be false,^33^ 3 This is the consequence of a small error in the proof of their Lemma 1. The constraint $C_{1}>C_{2}$ has no reason to be.

<!-- chunk {"id": "body-0038", "role": "body", "section": "About the Java version of TimSort", "weight": 1.0} -->

Indeed, in our example, we have $C_{1}=25$ and $C_{2}=31$. as illustrated in Figure 6. Thus, it is still possible to cause the Java implementation to fail: it uses a stack of runs of size at most 49 and we were able to compute an example requiring a stack of size 50, causing an error at runtime in Java's sorting method.

<!-- chunk {"id": "body-0039", "role": "body", "section": "About the Java version of TimSort", "weight": 1.0} -->

Even if the bug we highlighted in Java's TimSort is very unlikely to happen, this should be corrected. And, as advocated by de Gouw et al. and Tim Peters himself,^44^ 4 Here is the discussion about the correction in Python: we strongly believe that the best solution would be to correct the algorithm as in the current version of Python, in order to keep it clean and simple. However, since this is the implementation of Java's sort for the moment, there are two questions we would like to tackle: Does the complexity analysis holds without the missing condition? And, can we compute an actual bound for the stack size? We first address the complexity question. It turns out that the missing invariant was a key ingredient for having a simple and elegant proof.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusion", "weight": 1.5} -->

At first, when we learned that Java's QuickSort had been replaced by a variant of MergeSort, we thought that this new algorithm -- TimSort -- should be really fast and efficient in practice, and that we should look into its average complexity to confirm this from a theoretical point of view. Then, we realized that its worst-case complexity had not been formally established yet and we first focused on giving a proof that it runs in $\mathcal{O}(n\log n)$, which we wrote in a preprint. In the present article, we simplify this preliminary work and provide a short, simple and self-contained proof of TimSort's complexity, which sheds some light on the behavior of the algorithm. Based on this description, we were also able to answer positively a natural question, which was left open so far: does TimSort runs in $\mathcal{O}(n+n\log\rho)$, where $\rho$ is the number of runs? We hope our theoretical work highlights that TimSort is actually a very good sorting algorithm.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Even if all its fine-tuned heuristics are removed, the dynamics of its merges, induced by a small number of local rules, results in a very efficient global behavior, particularly well suited for *almost sorted* inputs.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Besides, we want to stress the need for a thorough algorithm analysis, in order to prevent errors and misunderstandings. As obvious as it may sound, the three consecutive mistakes on the stack height in Java illustrate perfectly how the best ideas can be spoiled by the lack of a proper complexity analysis.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Finally, following, we would like to emphasize that there seems to be no reason not to use the recent version of TimSort, which is efficient in practice, formally certified and whose optimal complexity is easy to understand.
