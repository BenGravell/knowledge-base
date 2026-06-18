<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Pattern-defeating Quicksort

Topics include Defeating quicksort.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A new solution for the Dutch national flag problem is proposed, requiring no three-way comparisons, which gives quicksort a proper worst-case runtime of O(nk) for inputs with k distinct elements. This is used together with other known and novel techniques to construct a hybrid sort that is never significantly slower than regular quicksort while speeding up drastically for many input distributions.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Arguably the most used hybrid sorting algorithm at the time of writing is introsort. A combination of insertion sort, heapsort and quicksort, it is very fast and can be seen as a truly hybrid algorithm. The algorithm performs introspection and decides when to change strategy using some very simple heuristics. If the recursion depth becomes too deep, it switches to heapsort, and if the partition size becomes too small it switches to insertion sort.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The goal of pattern-defeating quicksort (or pdqsort) is to improve on introsort's heuristics to create a hybrid sorting algorithm with several desirable properties. It maintains quicksort's logarithmic memory usage and fast real-world average case, effectively recognizes and combats worst case behavior (deterministically), and runs in linear time for a few common patterns. It also unavoidably inherits in-place quicksort's instability, so pdqsort can not be used in situations where stability is needed.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 2 we will explore a quick overview of pattern-defeating quicksort and related work, in Section 3 we propose our new solution for the Dutch national flag problem and prove its $O{({nk})}$ worst-case time for inputs with $k$ distinct elements, Section 4 describes other novel techniques used in pdqsort while Section 5 describes various previously known ones. Our final section consists of an empirical performance evaluation of pdqsort.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper comes with an open source state of the art C++ implementation. The implementation is fully compatible with std::sort and is released under a permissive license. Standard library writers are invited to evaluate and adopt the implementation as their generic unstable sorting algorithm. At the time of writing the Rust programming language has adopted pdqsort for sort_unstable in their standard library thanks to a porting effort by Stjepan Glavina. The implementation is also available in the C++ Boost.Sort library.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Overview and related work", "weight": 1.0} -->

Pattern-defeating quicksort is a hybrid sort consisting of quicksort, insertion sort and a fallback sort. In this paper we use heapsort as our fallback sort, but really any $O{({n{\log n}})}$ worst case sort can be used - it's exceptionally rare that the heuristics end up switching to the fallback. Each recursive call of pdqsort chooses either to fall back, use insertion sort or partition and recurse.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Overview and related work", "weight": 1.0} -->

Insertion sort is used for small recursive calls as despite its $O{(n^{2})}$ worst case it has great constant factors and outperforms quicksort for small $n$. We later discuss (not novel but nevertheless important) techniques to properly implement insertion sort for usage in a hybrid algorithm. We have tried to use small sorting networks akin to Codish's approach as an alternative base case but were unable to beat insertion sort. We conjecture that the small code size of insertion sort has sufficient positive cache effects to offset the slower algorithm when used in a hybrid sort.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Overview and related work", "weight": 1.0} -->

For partitioning we use a novel scheme that indirectly ends up performing tripartite partitioning. This is used in conjunction with the very important technique from BlockQuicksort that greatly speeds up partitioning with branchless comparison functions. In a sense our partitioning scheme is similar to Yaroslavskiy's dual-pivot quicksort from the perspective of equal elements. We did consider dual- and multi-pivot variants of quicksort but chose to stick to traditional partitioning for simplicity, applicability of the techniques described here, and due to the massive speedup from BlockQuicksort, which does not trivially extend to multiple pivots (see IPS^4^o for that).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Overview and related work", "weight": 1.0} -->

We use the well-known median-of-3 pivot selection scheme, with John Tukey's ninther for sufficiently large inputs, which Kurosawa finds has a near-identical number of comparisons to selecting the true median, but is significantly simpler.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Overview and related work", "weight": 1.0} -->

Finally, we beat patterns with two novel additions. We diverge from introsort by no longer simply using the call depth to switch to a fallback. Instead we define a concept of a bad partition, and track those instead. This results in a more precise heuristic on bad sorting behavior, and consequently fallback usage. Whenever we detect a bad partition we also swap a couple well-selected elements, which not only breaks up common patterns and introduces 'noise' similar to how a random quicksort would behave, it introduces new pivot candidates in the selection pool. We also use a technique (not known to us in previous literature) due to Howard Hinnant to optimistically handle ascending/descending sequences with very little overhead.

<!-- chunk {"id": "body-0012", "role": "body", "section": "A faster solution for the Dutch national flag problem", "weight": 1.0} -->

A naive quicksort implementation might trigger the $\Theta{(n^{2})}$ worst case on the all-equal input distribution by placing equal comparing elements in the same partition. A smarter implementation either always or never swaps equal elements, resulting in average case performance as equal elements will be distributed evenly across the partitions. However, an input with many equal comparing elements is rather common^11^1It is a common technique to define a custom comparison function that only uses a subset of the available data to sort, e.g. sorting cars by their color. Then you have many elements that aren't fundamentally equal, but do compare equal in the context of a sorting operation., and we can do better. Handling equal elements efficiently requires tripartite partitioning, which is equivalent to Dijkstra's Dutch national flag problem.

<!-- chunk {"id": "body-0013", "role": "body", "section": "A faster solution for the Dutch national flag problem", "weight": 1.0} -->

Pattern-defeating quicksort uses the fast 'approaching pointers' method for partitioning. Two indices are initialized, $i$ at the start and $j$ at the end of the sequence. $i$ is incremented and $j$ is decremented while maintaining an invariant, and when both invariants are invalidated the elements at the pointers are swapped, restoring the invariant. The algorithm ends when the pointers cross. Implementers must take great care, as this algorithm is conceptually simple, but is very easy to get wrong.

<!-- chunk {"id": "body-0014", "role": "body", "section": "A faster solution for the Dutch national flag problem", "weight": 1.0} -->

Bentley and McIlroy describe an invariant for partitioning that swaps equal elements to the edges of the partition, and swaps them back into the middle after partitioning. This is efficient when there are many equal elements, but has a significant drawback. Every element needs to be explicitly checked for equality to the pivot before swapping, costing another comparison. This happens regardless of whether there are many equal elements, costing performance in the average case.

<!-- chunk {"id": "body-0015", "role": "body", "section": "A faster solution for the Dutch national flag problem", "weight": 1.0} -->

Unlike previous algorithms, pdqsort's partitioning scheme is not self contained. It uses two separate partition functions, one that groups elements equal to the pivot in the left partition (partition_left), and one that groups elements equal to the pivot in the right partition (partition_right). Note that both partition functions can always be implemented using a single comparison per element as ${a < b}\Leftrightarrow{a \ngeq b}$ and ${a \nless b}\Leftrightarrow{a \geq b}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "A faster solution for the Dutch national flag problem", "weight": 1.0} -->

For brevity we will be using a simplified, incomplete C++ implementation to illustrate pdqsort. It only supports int and compares using comparison operators. It is however trivial to extend this to arbitrary types and custom comparator functions. To pass subsequences^22^2Without exception, in this paper subsequences are assumed to be contiguous. around, the C++ convention is used of one pointer at the start, and one pointer at one-past-the-end. For the exact details refer to the full implementation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "A faster solution for the Dutch national flag problem", "weight": 1.0} -->

Both partition functions assume the pivot is the first element, and that it has been selected as a median of at least three elements in the subsequence. This saves a bound check in the first iteration.

<!-- chunk {"id": "body-0018", "role": "body", "section": "A faster solution for the Dutch national flag problem", "weight": 1.0} -->

int* part_left(int* l, int* r) { int* part_right(int* l, int* r) {
int* i = l; int* j = r; int* i = l; int* j = r;
while (i &lt; j &amp;&amp; *++i &lt;= p); while (i &lt; j &amp;&amp; *--j &gt;= p);
std::swap(*i, *j); std::swap(*i, *j);
std::swap(*l, *j); std::swap(*l, *(i - 1));
Figure 3: An efficient implementation of partition_left and partition_right (named part_left and part_right here due to limited page width). Note the (almost) lack of bound checks, we assume that p was selected as the median of at least three elements, and in later iterations previous elements are used as sentinels to prevent going out of bounds.

<!-- chunk {"id": "body-0019", "role": "body", "section": "A faster solution for the Dutch national flag problem", "weight": 1.0} -->

Also note that a pre-partitioned subsequence will perform no swaps and that it is possible to detect this with a single comparison of pointers, no_swaps. This is used for a heuristic later.

<!-- chunk {"id": "body-0020", "role": "body", "section": "A faster solution for the Dutch national flag problem", "weight": 1.0} -->

Given a subsequence $\alpha$ let us partition it using partition_right using pivot $p$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "A faster solution for the Dutch national flag problem", "weight": 1.0} -->

If $p \neq q$ we have $q > p$, and apply partition_right on $q,\beta$. Rename $q,\beta$ to be the left partition of this operation (marked as $q^{\prime},\beta^{\prime}$ in the diagram to emphasize renaming). The right partition is marked as '$>$', because in this process we have the perspective of pivot $p$, but it's definitely possible for elements equal to $q$ to be in the partition marked '$>$'.

<!-- chunk {"id": "body-0022", "role": "body", "section": "A faster solution for the Dutch national flag problem", "weight": 1.0} -->

We apply the above step recursively as long as $p \neq q$. If at some point $q,\beta$ becomes empty, we can conclude there were no elements equal to $p$ and the tripartite partitioning was done when we initially partitioned $\alpha$. Otherwise, consider $p = q$. We know that ${{\forall x} \in \beta}:{x \geq p}$, thus ${{\nexistsx} \in \beta}:{x < q}$. If we were to partition $q,\beta$ using partition_left, any element smaller than or equal to $q$ would be partitioned left. However, we just concluded that $\beta$ can not contain elements smaller than $q$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "A faster solution for the Dutch national flag problem", "weight": 1.0} -->

This leads to the partitioning algorithm used by pdqsort. The predecessor of a subsequence is the element directly preceding it in the original sequence. A subsequence that is leftmost has no predecessor. If a subsequence has a predecessor $p$ that compares equal to the chosen pivot $q$, apply partition_left, otherwise apply partition_right. No recursion on the left partition of partition_left is needed, as it contains only equivalent elements.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Preventing quicksort's $O{(n^{2})}$ worst case", "weight": 1.0} -->

Pattern-defeating quicksort calls any partition operation which is more unbalanced than $p$ (where $p$ is the percentile of the pivot, e.g. $\frac{1}{2}$ for a perfect partition) a bad partition. Initially, it sets a counter to $\log n$. Every time it encounters a bad partition, it decrements the counter before recursing^55^5This counter is maintained separately in every subtree of the call graph - it is not a global to the sort process. Thus, if after the first partition the left partition degenerates in the worst case it does not imply the right partition also does.. If at the start of a recursive call the counter is 0 it uses heapsort to sort this subsequence, rather than quicksort.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Introducing fresh pivot candidates on bad partitions", "weight": 1.0} -->

Some input patterns form some self-similar structure after partitioning. This can cause a similar pivot to be repeatedly chosen. We want to eliminate this. The reason for this can be found in Figure 4 worst case ‣ 4 Other novel techniques ‣ Pattern-defeating Quicksort") as well. The difference between a good and mediocre pivot is small, so repeatedly choosing a good pivot has a relatively small payoff. The difference between a mediocre and bad pivot is massive. An extreme example is the traditional $O{(n^{2})}$ worst case: repeatedly partitioning without real progress.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Introducing fresh pivot candidates on bad partitions", "weight": 1.0} -->

The classical way to deal with this is by randomizing pivot selection (also known as randomized quicksort). However, this has multiple disadvantages. Sorting is not deterministic, the access patterns are unpredictable and extra runtime is required to generate random numbers. We also destroy beneficial patterns, e.g. the technique in section 5.2 would no longer work for descending patterns and performance on 'mostly sorted' input patterns would also degrade.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Introducing fresh pivot candidates on bad partitions", "weight": 1.0} -->

Pattern-defeating quicksort takes a different approach. After partitioning we check if the partition was bad. If it was, we swap our pivot candidates for others. In our implementation pdqsort chooses the median of the first, middle and last element in a subsequence as the pivot, and swaps the first and last candidate for ones found at the 25% and 75% percentile after encountering a bad partition. When our partition is big enough that we would be using Tukey's ninther for pivot selection we also swap the ninther candidates for ones at roughly the 25% and 75% percentile of the partition.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Introducing fresh pivot candidates on bad partitions", "weight": 1.0} -->

With this scheme pattern-defeating quicksort is still fully deterministic, and with minimal overhead breaks up many of the patterns that regular quicksort struggles. If the downsides of non-determinism do not scare you and you like the guarantees that randomized quicksort provides (e.g. protection against DoS attacks) you can also swap out the pivot candidates with random candidates. It's still a good idea to only do this after a bad partition to prevent breaking up beneficial patterns.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Insertion sort", "weight": 1.0} -->

Essentially all optimized quicksort implementations switch to a different algorithm when recursing on a small ($\leq 16$--$32$ elements) subsequence, most often insertion sort. But even the simple insertion sort is subject to optimization, as a significant amount of time is spent in this phase.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Insertion sort", "weight": 1.0} -->

It's important to use a series of moves instead of swaps, as this eliminates a lot of unnecessary shuffling. Another big^66^65-15% from our benchmarks, for sorting small integers. improvement can be made by eliminating bounds checking in the inner insertion sort loop. This can be done for any subsequence that is not leftmost, as there must exist some element before the subsequence you're sorting that acts as a sentinel breaking the loop. Although this change is tiny, for optimal performance this requires an entirely new function as switching behavior based on a condition defeats the purpose of this micro-optimization. This variant is traditionally called unguarded_insertion_sort. This is a prime example where introducing more element comparisons can still result in faster code.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Optimistic insertion sorting on a swapless partition", "weight": 1.0} -->

This technique is not novel, and is due to Howard Hinnants std::sort implementation, but has to our knowledge not been described in literature before. After partitioning we can check whether the partition was swapless. This means we didn't have to swap any element (other than putting the pivot in its proper place). Checking for this condition can be done with a single comparison as shown in Figure 3 with the variable no_swaps.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Optimistic insertion sorting on a swapless partition", "weight": 1.0} -->

If this is the case and the partition wasn't bad we do a partial insertion sort over both partitions that aborts if it has to do more than a tiny number of corrections (to minimize overhead in the case of a misdiagnosed best case). However, if little to no corrections were necessary, we are instantly done and do not have to recurse.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Optimistic insertion sorting on a swapless partition", "weight": 1.0} -->

If you properly choose your pivots^77^7Frankly, this can be a bit fragile. Check the pdqsort source code for the exact procedure used to select pivots, and you notice we actually sort the pivot candidates and put the median one at the start position, which gets swapped back to the middle in the event of a swapless partition. A small deviation from the reference implementation here might lose you the linear time guarantee. then this small optimistic heuristic will sort inputs that are ascending, descending or ascending with an arbitrary element appended all in linear time. We argue that these input distributions are vastly overrepresented in the domain of inputs to sorting functions, and are well worth the miniscule overhead caused by false positives.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Optimistic insertion sorting on a swapless partition", "weight": 1.0} -->

This overhead really is miniscule, as swapless partitions become exceedingly unlikely for large arrays to happen by chance. A hostile attacker crafting worst-case inputs is also no better off. The maximum overhead per partition is $\approx n$ operations, so it doubles performance at worst, but this can already be done to pdqsort by crafting a worst case that degenerates to heapsort. Additionally, the partial insertion sort is only triggered when the partition wasn't bad, forcing an attacker to generate good quicksort progress if she intends to trigger repeated misdiagnosed partial insertion sorts.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Block partitioning", "weight": 1.0} -->

One of the most important optimizations for a modern quicksort is Edelkamp and Weiß' recent work on BlockQuicksort. Their technique gives a huge^88^850-80% from our benchmarks, for sorting small integers. speedup by eliminating branch predictions during partitioning. In pdqsort it is only applied for partition_right, as the code size is significant and partition_left is rarely called.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Block partitioning", "weight": 1.0} -->

Branch predictions are eliminated by replacing them with data-dependent moves. First some static block size is determined^99^9In our implementation we settled on a static 64 elements, but the optimal number depends on your CPU and cache architecture as well as the data you're sorting.. Then, until there are fewer than 2\*bsize elements remaining, we repeat the following process.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Block partitioning", "weight": 1.0} -->

We look at the first bsize elements on the left hand side. If an element in this block is bigger or equal to the pivot, it belongs on the right hand side. If not, it should keep its current position. For each element that needs to be moved we store its offset in offsets_l.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Block partitioning", "weight": 1.0} -->

[⬇](data:text/plain;base64,aW50IG51bV9sID0gMDsgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGludCBudW1fciA9IDA7CmZvciAoaW50IGkgPSAwOyBpIDwgYnNpemU7ICsraSkgeyAgICAgICAgICBmb3IgKGludCBpID0gMDsgaSA8IGJzaXplOyArK2kpIHsKICAgIGlmICgqKGwgKyBpKSA+PSBwaXZvdCkgeyAgICAgICAgICAgICAgICAgICBpZiAoKihyIC0gMSAtIGkpIDwgcGl2b3QpIHsKICAgICAgICBvZmZzZXRzX2xbbnVtX2xdID0gaTsgICAgICAgICAgICAgICAgICAgICAgb2Zmc2V0c19yW251bV9yXSA9IGkgKyAxOwogICAgICAgIG51bV9sKys7ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBudW1fcisrOwogICAgfSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0KfSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0=){download=""}

<!-- chunk {"id": "body-0039", "role": "body", "section": "Block partitioning", "weight": 1.0} -->

But this still contains branches.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Block partitioning", "weight": 1.0} -->

[⬇](data:text/plain;base64,aW50IG51bV9sID0gMDsgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGludCBudW1fciA9IDA7CmZvciAoaW50IGkgPSAwOyBpIDwgYnNpemU7ICsraSkgeyAgICAgICAgICBmb3IgKGludCBpID0gMDsgaSA8IGJzaXplOyArK2kpIHsKICAgIG9mZnNldHNfbFtudW1fbF0gPSBpOyAgICAgICAgICAgICAgICAgICAgICBvZmZzZXRzX3JbbnVtX3JdID0gaSArIDE7CiAgICBudW1fbCArPSAqKGwgKyBpKSA+PSBwaXZvdDsgICAgICAgICAgICAgICAgbnVtX3IgKz0gKihyIC0gMSAtIGkpIDwgcGl2b3Q7Cn0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB9){download=""}

<!-- chunk {"id": "body-0041", "role": "body", "section": "Block partitioning", "weight": 1.0} -->

[⬇](data:text/plain;base64,Zm9yIChpbnQgaSA9IDA7IGkgPCBzdGQ6Om1pbihudW1fbCwgbnVtX3IpOyArK2kpIHsKICAgIHN0ZDo6aXRlcl9zd2FwKGwgKyBvZmZzZXRzX2xbaV0sIHIgLSBvZmZzZXRzX3JbaV0pOwp9){download=""}

<!-- chunk {"id": "body-0042", "role": "body", "section": "Block partitioning", "weight": 1.0} -->

for (int i = 0; i \< std::min(num_l, num_r); ++i) {

<!-- chunk {"id": "body-0043", "role": "body", "section": "Block partitioning", "weight": 1.0} -->

std::iter_swap(l + offsets_l\[i\], r - offsets_r\[i\]);

<!-- chunk {"id": "body-0044", "role": "body", "section": "Block partitioning", "weight": 1.0} -->

Notice that we only swap std::min(num_l, num_r) elements, because we need to pair each element that belongs on the left with an element that belongs on the right. Any leftover elements are re-used in the next iteration^1010^10After each iteration at least one offsets buffer is empty. We fill any buffer that is empty., however it takes a bit of extra code to do so. It is also possible to re-use the last remaining buffer for the final elements to prevent any wasted comparisons, again at the cost of a bit of extra code. For the full implementation^1111^11We skip over many important details and optimizations here as they are more relevant to BlockQuicksort than to pattern-defeating quicksort. The full implementation has loop unrolling, swaps elements using only two moves per element rather than three and uses all comparison information gained while filling blocks. and more explanation we invite the reader to check the Github repository, and read Edelkamp and Weiß' original paper.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Block partitioning", "weight": 1.0} -->

The concept is important here: replacing branches with data-dependent moves followed by unconditional swaps. This eliminates virtually all branches in the sorting code, as long as the comparison function used is branchless. This means in practice that the speedup is limited to integers, floats, small tuples of those or similar. However, it's still a comparison sort. You can give it arbitrarily complicated branchless comparison functions (e.g. a\*c \> b-c) and it will work.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Block partitioning", "weight": 1.0} -->

When the comparison function isn't branchless this method of partitioning can be slower. The C++ implementation is conservative, and by default only uses block based partitioning if the comparison function is std::less or similar, and the elements being sorted are native numeric types. If a user wishes to get block based partitioning otherwise it needs to be specifically requested.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Methodology", "weight": 1.0} -->

We present a performance evaluation of pattern-defeating quicksort with (bpdq) and without (pdq) block partitioning, introsort from libstdc++'s implementation of std::sort (std), Timothy van Slyke's C++ Timsort implementation (tim), BlockQuicksort (bq) and the sequential version of In-Place Super Scalar Samplesort (is^4^o). The latter algorithm represents to our knowledge the state of the art in sequential in-place comparison sorting for large amounts of data.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Methodology", "weight": 1.0} -->

In particular the comparison with BlockQuicksort is important as it is a benchmark for the novel methods introduced here. The code repository for BlockQuicksort defines many different versions of BlockQuicksort, one of which also uses Hoare-style crossing pointers partitioning and Tukey's ninther pivot selection. This version is chosen for the closest comparison as it most resembles our algorithm. The authors of BlockQuicksort also proposed their own duplicate handling scheme. To compare the efficacy of their and our approach we also chose the version of BlockQuicksort with it enabled.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Methodology", "weight": 1.0} -->

We evaluate the algorithms for three different data types. The simplest is int, which is a simple 64-bit integer. However, not all data types have a branchless comparison function. For that reason we also have str, which is a std::string representation of int (padded with zeroes such that lexicographic order matches the numeric order). Finally to simulate an input with an expensive comparison function we evaluate bigstr which is similar to str but is prepended with $1000$ zeroes to artificially inflate compare time. An algorithm that is more efficient with the number of comparisons it performs should gain an edge there.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Methodology", "weight": 1.0} -->

The algorithms are evaluated on a variety of input distributions.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Methodology", "weight": 1.0} -->

Shuffled uniformly distributed values (uniform: ${A{\lbrack i\rbrack}} = i$), shuffled distributions with many duplicates (dupsq: ${A{\lbrack i\rbrack}} = {i\operatorname{mod}{\lfloor\sqrt{n}\rfloor}}$, dup8: ${A{\lbrack i\rbrack}} = {{i^{8} + {n/2}}\operatorname{mod}n}$, mod8: ${A{\lbrack i\rbrack}} = {i\operatorname{mod}8}$, and ones: ${A{\lbrack i\rbrack}} = 1$), partially shuffled uniform distributions (sort50, sort90, sort99 which respectively have the first 50%, 90% and 99% of the elements already in ascending order) and some traditionally notoriously bad cases for median-of-3 pivot selection (organ: first half of the input ascending and the second half descending, merge: two equally sized ascending arrays

<!-- chunk {"id": "body-0052", "role": "body", "section": "Methodology", "weight": 1.0} -->

concatenated). Finally we also have the inputs asc, desc which are inputs that are already sorted.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Methodology", "weight": 1.0} -->

The evaluation was performed on an AMD Ryzen Threadripper 2950x clocked at 4.2GHz with 32GB of RAM. All code was compiled with GCC 8.2.0 with flags -march=native -m64 -O2. To preserve the integrity of the experiment no two instances were tested simultaneously and no other resource intensive processes were run at the same time. For all random shuffling a seed was deterministically chosen for each size and input distribution, so all algorithms received the exact same input for the same experiment. Each benchmark was re-run until at least 10 seconds had passed and for at least 10 iterations. The former condition reduces timing noise by repeating small instances many times whereas the latter condition reduces the influence of a particular random shuffle. The mean number of cycles spent is reported, divided by $n{\log_{2}n}$ to normalize across sizes. In total the evaluation program spent 9 hours sorting (with more time spent to prepare input distributions).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Methodology", "weight": 1.0} -->

As the full results are quite large (${{{12\text{~distributions}} \times 3}\text{~data types}} = 36$ plots), they are included in Appendix A.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Results and observations", "weight": 1.0} -->

First we'd like to note that across all benchmarks pdq and bpdq are never significantly slower than their non-pattern defeating counterparts std and bq. In fact, the only regression at all is $\approx {4.5\%}$ for pdq v.s. std for large instances of uniform-int (while being faster for smaller sizes and bpdq being roughly twice as fast).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Results and observations", "weight": 1.0} -->

There is one exception, with bq beating bpdq for the organ and merge distributions (and very slightly for sort99) with the bigstr data type. It is unclear why exactly this happens here. Especially curious is that the former two distributions were very clearly bad cases for bq with the int data type when we compare the performance against uniform. But in bigstr the roles have been reversed, bq is significantly faster on organ and merge than it is on uniform. So it's not that bpdq is slow here, bq is just mysteriously fast. Regardless, we see that both pdq and bpdq maintain good performance (similar to uniform) on these cases, effectively defeating the pattern.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Results and observations", "weight": 1.0} -->

With these observations it's safe to say that the heuristics used in pattern-defeating quicksort come with minimal to no overhead.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Results and observations", "weight": 1.0} -->

Interesting to note is the behavior regarding cache. On this system with sizeof(std::string) being $32$ we see a drastic change of slope for all quicksort based algorithms in the str benchmark around $n = 2^{16}$, which is right when the $1.5$MB L1 cache has filled up. It's odd to see that this shift in slope never happens for int, even when the input size well exceeds any CPU cache. For bigstr the change of slope occurs slightly earlier, at around $n = 2^{12}$. Timsort is seemingly barely affected by this, but the clear winner in this regard is is^4^o, which appears to be basically cache-oblivious.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Results and observations", "weight": 1.0} -->

We already knew this, but block partitioning isn't always beneficial. However even for types where the comparison can be done without branches, it still isn't always faster. In cases where the branch predictor would get it right nearly every time because the data has such a strong pattern (e.g. for pdq in merge-int), the traditional partitioning can still be significantly faster.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Results and observations", "weight": 1.0} -->

It should come at no surprise that for every input with long ascending or descending runs Timsort is in the lead. Timsort is based on mergesort, so it can fully exploit any runs in the data. We note that while pdqsort defeats the patterns, meaning it doesn't heavily slow down on unfavorable patterns, it can't exploit these runs either.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Results and observations", "weight": 1.0} -->

In previous benchmarks however Timsort's constant factor was very high, making it significantly slower for anything that does not have a pattern to exploit. Looking at the results now, we congratulate Timothy van Slyke on his performant implementation, which is significantly more competitive. Especially for bigger or harder to compare types Timsort is now an excellent choice.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Results and observations", "weight": 1.0} -->

Our scheme for handling equal elements is very effective. Especially when the number of equivalence classes approaches $1$ (such as in mod8 and ones) the runtime goes down drastically, but even in milder cases such as dupsq we see that the pattern-defeating sorts build a sizable lead over their counterparts when compared to their performance in uniform.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Results and observations", "weight": 1.0} -->

Finally we note that due to the optimistic insertion sort on swapless partitions pdqsort achieves an incredible speedup for the the ascending and descending input case, rivalling Timsort.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusion and further research", "weight": 1.5} -->

We conclude that the heuristics and techniques presented in this paper have little overhead, and effectively handle various input patterns. Pattern-defeating quicksort is often the best choice of algorithm overall for small to medium input sizes or data type sizes. It and other quicksort variants suffer from datasets that are too large to fit in cache, where is^4^o shines. The latter algorithm however suffers from bad performance on smaller sizes, future research could perhaps combine the best of these two algorithms.
