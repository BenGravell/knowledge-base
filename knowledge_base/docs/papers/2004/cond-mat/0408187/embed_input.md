<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Finding Community Structure in Very Large Networks

Topics include Community detection, CNM algorithm, Fast greedy modularity, Modularity optimization, Hierarchical clustering, Agglomerative clustering, Large-scale graphs, Network science.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the CNM fast greedy algorithm, an agglomerative method that efficiently optimizes modularity and produces a community dendrogram. The paper was important because it moved modularity-based community detection toward networks with hundreds of thousands of nodes.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The discovery and analysis of community structure in networks is a topic of considerable recent interest within the physics community, but most methods proposed so far are unsuitable for very large networks because of their computational cost. Here we present a hierarchical agglomeration algorithm for detecting community structure which is faster than many competing algorithms: its running time on a network with n vertices and m edges is O(m d log n) where d is the depth of the dendrogram describing the community structure. Many real-world networks are sparse and hierarchical, with m ~ n and d ~ log n, in which case our algorithm runs in essentially linear time, O(n log^2 n). As an example of the application of this algorithm we use it to analyze a network of items for sale on the web-site of a large online retailer, items in the network being linked if they are frequently purchased by the same buyer. The network has more than 400,000 vertices and 2 million edges. We show that our algorithm can extract meaningful communities from this network, revealing large-scale patterns present in the purchasing habits of customers.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many systems of current interest to the scientific community can usefully be represented as networks. Examples include the Internet and the world-wide web social networks, citation networks food webs, and biochemical networks;. Each of these networks consists of a set of nodes or vertices representing, for instance, computers or routers on the Internet or people in a social network, connected together by links or edges, representing data connections between computers, friendships between people, and so forth.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One network feature that has been emphasized in recent work is community structure, the gathering of vertices into groups such that there is a higher density of edges within groups than between them note. The problem of detecting such communities within networks has been well studied. Early approaches such as the Kernighan--Lin algorithm, spectral partitioning or hierarchical clustering work well for specific types of problems (particularly graph bisection or problems with well defined vertex similarity measures), but perform poorly in more general cases.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To combat this problem a number of new algorithms have been proposed in recent years. Girvan and Newman; proposed a divisive algorithm that uses edge betweenness as a metric to identify the boundaries of communities. This algorithm has been applied successfully to a variety of networks, including networks of email messages, human and animal social networks, networks of collaborations between scientists and musicians, metabolic networks and gene networks. However, as noted, the algorithm makes heavy demands on computational resources, running in $O{({m^{2}n})}$ time on an arbitrary network with $m$ edges and $n$ vertices, or $O{(n^{3})}$ time on a sparse graph (one in which $m \sim n$, which covers most real-world networks of interest). This restricts the algorithm's use to networks of at most a few thousand vertices with current hardware.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

More recently a number of faster algorithms have been proposed. In, one of us proposed an algorithm based on the greedy optimization of the quantity known as modularity. This method appears to work well both in contrived test cases and in real-world situations, and is substantially faster than the algorithm of Girvan and Newman. A naive implementation runs in time $O{({{({m + n})}n})}$, or $O{(n^{2})}$ on a sparse graph.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here we propose a new algorithm that performs the same greedy optimization as the algorithm of and therefore gives identical results for the communities found. However, by exploiting some shortcuts in the optimization problem and using more sophisticated data structures, it runs far more quickly, in time $O{({md{\log n}})}$ where $d$ is the depth of the "dendrogram" describing the network's community structure. Many real-world networks are sparse, so that $m \sim n$; and moreover, for networks that have a hierarchical structure with communities at many scales, $d \sim {\log n}$. For such networks our algorithm has essentially linear running time, $O{({n{\log^{2}n}})}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

This is not merely a technical advance but has substantial practical implications, bringing within reach the analysis of extremely large networks. Networks of ten million vertices or more should be possible in reasonable run times. As an example, we give results from the application of the algorithm to a recommender network of books from the online bookseller Amazon.com, which has more than $400\, 000$ vertices and two million edges.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The algorithm", "weight": 1.0} -->

Modularity is a property of a network and a specific proposed division of that network into communities. It measures when the division is a good one, in the sense that there are many edges within communities and only a few between them. Let $A_{vw}$ be an element of the adjacency matrix of the network thus: and suppose the vertices are divided into communities such that vertex $v$ belongs to community $c_{v}$. Then the fraction of edges that fall within communities, i.e., that connect vertices that both lie in the same community, is where the $\delta$-function $\delta{(i,j)}$ is 1 if $i = j$ and 0 otherwise, and $m = {\frac{1}{2}{\sum_{vw}A_{vw}}}$ is the number of edges in the graph. This quantity will be large for good divisions of the network, in the sense of having many within-community edges, but it is not, on its own, a good measure of community structure since it takes its largest value of 1 in the trivial case where all vertices belong to a single community.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The algorithm", "weight": 1.0} -->

However, if we subtract from it the expected value of the same quantity in the case of a randomized network, we do get a useful measure.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The algorithm", "weight": 1.0} -->

The degree $k_{v}$ of a vertex $v$ is defined to be the number of edges incident upon it: The probability of an edge existing between vertices $v$ and $w$ if connections are made at random but respecting vertex degrees is ${{k_{v}k_{w}}/2}m$. We define the modularity $Q$ to be If the fraction of within-community edges is no different from what we would expect for the randomized network, then this quantity will be zero. Nonzero values represent deviations from randomness, and in practice it is found that a value above about 0.3 is a good indicator of significant community structure in a network.

<!-- chunk {"id": "body-0013", "role": "body", "section": "The algorithm", "weight": 1.0} -->

If high values of the modularity correspond to good divisions of a network into communities, then one should be able to find such good divisions by searching through the possible candidates for ones with high modularity. While finding the global maximum modularity over all possible divisions seems hard in general, reasonably good solutions can be found with approximate optimization techniques. The algorithm proposed in uses a greedy optimization in which, starting with each vertex being the sole member of a community of one, we repeatedly join together the two communities whose amalgamation produces the largest increase in $Q$. For a network of $n$ vertices, after $n - 1$ such joins we are left with a single community and the algorithm stops. The entire process can be represented as a tree whose leaves are the vertices of the original network and whose internal nodes correspond to the joins. This dendrogram represents a hierarchical decomposition of the network into communities at all levels.

<!-- chunk {"id": "body-0014", "role": "body", "section": "The algorithm", "weight": 1.0} -->

The most straightforward implementation of this idea (and the only one considered in ) involves storing the adjacency matrix of the graph as an array of integers and repeatedly merging pairs of rows and columns as the corresponding communities are merged. For the case of the sparse graphs that are of primary interest in the field, however, this approach wastes a good deal of time and memory space on the storage and merging of matrix elements with value 0, which is the vast majority of the adjacency matrix. The algorithm proposed in this paper achieves speed (and memory efficiency) by eliminating these needless operations.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The algorithm", "weight": 1.0} -->

To simplify the description of our algorithm let us define the following two quantities: which is the fraction of edges that join vertices in community $i$ to vertices in community $j$, and which is the fraction of ends of edges that are attached to vertices in community $i$. Then, writing ${\delta{(c_{v},c_{w})}} = {\sum_{i}{\delta{(c_{v},i)}\delta{(c_{w},i)}}}$, we have, from Eq.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The algorithm", "weight": 1.0} -->

- \frac{1}{2m}\sum\limits_{v}k_{v}\delta{(c_{v},i)}\frac{1}{2m}\sum\limits_{w}k_{w}\delta{(c_{w},i)} \right\rbrack$ | | | The operation of the algorithm involves finding the changes in $Q$ that would result from the amalgamation of each pair of communities, choosing the largest of them, and performing the corresponding amalgamation. One way to envisage (and implement) this process is to think of network as a multigraph, in which a whole community is represented by a vertex, bundles of edges connect one vertex to another, and edges internal to communities are represented by self-edges. The adjacency matrix of this multigraph has elements$A_{ij}' = {2me_{ij}}$, and the joining of two communities $i$ and $j$ corresponds to replacing the $i$th and $j$th rows and columns by their sum.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The algorithm", "weight": 1.0} -->

In the algorithm of this operation is done explicitly on the entire matrix, but if the adjacency matrix is sparse (which we expect in the early stages of the process) the operation can be carried out more efficiently using data structures for sparse matrices. Unfortunately, calculating $\DeltaQ_{ij}$ and finding the pair $i,j$ with the largest $\DeltaQ_{ij}$ then becomes time-consuming.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The algorithm", "weight": 1.0} -->

In our new algorithm, rather than maintaining the adjacency matrix and calculating $\DeltaQ_{ij}$, we instead maintain and update a matrix of value of $\DeltaQ_{ij}$. Since joining two communities with no edge between them can never produce an increase in $Q$, we need only store $\DeltaQ_{ij}$ for those pairs $i,j$ that are joined by one or more edges. Since this matrix has the same support as the adjacency matrix, it will be similarly sparse, so we can again represent it with efficient data structures. In addition, we make use of an efficient data structure to keep track of the largest $\DeltaQ_{ij}$. These improvements result in a considerable saving of both memory and time.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The algorithm", "weight": 1.0} -->

In total, we maintain three data structures: A sparse matrix containing $\DeltaQ_{ij}$ for each pair $i,j$ of communities with at least one edge between them. We store each row of the matrix both as a balanced binary tree (so that elements can be found or inserted in $O{({\log n})}$ time) and as a max-heap (so that the largest element can be found in constant time).

<!-- chunk {"id": "body-0020", "role": "body", "section": "The algorithm", "weight": 1.0} -->

A max-heap $H$ containing the largest element of each row of the matrix $\DeltaQ_{ij}$ along with the labels $i,j$ of the corresponding pair of communities.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The algorithm", "weight": 1.0} -->

An ordinary vector array with elements $a_{i}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The algorithm", "weight": 1.0} -->

As described above we start off with each vertex being the sole member of a community of one, in which case $e_{ij} = {{1/2}m}$ if $i$ and $j$ are connected and zero otherwise, and $a_{i} = {{k_{i}/2}m}$. Thus we initially set for each $i$. (This assumes the graph is unweighted; weighted graphs are a simple generalization.)

<!-- chunk {"id": "body-0023", "role": "body", "section": "The algorithm", "weight": 1.0} -->

Our algorithm can now be defined as follows.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The algorithm", "weight": 1.0} -->

Calculate the initial values of $\DeltaQ_{ij}$ and $a_{i}$ according to and, and populate the max-heap with the largest element of each row of the matrix $\DeltaQ$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The algorithm", "weight": 1.0} -->

Select the largest $\DeltaQ_{ij}$ from $H$, join the corresponding communities, update the matrix $\DeltaQ$, the heap $H$ and $a_{i}$ (as described below) and increment $Q$ by $\DeltaQ_{ij}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The algorithm", "weight": 1.0} -->

Repeat step 2 until only one community remains.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The algorithm", "weight": 1.0} -->

Our data structures allow us to carry out the updates in step 2 quickly. First, note that we need only adjust a few of the elements of $\DeltaQ$. If we join communities $i$ and $j$, labeling the combined community $j$, say, we need only update the $j$th row and column, and remove the $i$th row and column altogether. The update rules are as follows.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The algorithm", "weight": 1.0} -->

| If community $k$ is connected to both $i$ and $j$, then | | | $${\DeltaQ_{jk}'} = {{\DeltaQ_{ik}} + {\DeltaQ_{jk}}}$$ | | (10a) | | If $k$ is connected to $i$ but not to $j$, then | | If $k$ is connected to $j$ but not to $i$, then | Note that these equations imply that $Q$ has a single peak over the course of the algorithm, since after the largest $\DeltaQ$ becomes negative all the $\DeltaQ$ can only decrease.

<!-- chunk {"id": "body-0029", "role": "body", "section": "The algorithm", "weight": 1.0} -->

To analyze how long the algorithm takes using our data structures, let us denote the degrees of $i$ and $j$ in the reduced graph---i.e., the numbers of neighboring communities---as $|i|$ and $|j|$ respectively. The first operation in a step of the algorithm is to update the $j$th row. To implement Eq. (10a), we insert the elements of the $i$th row into the $j$th row, summing them wherever an element exists in both columns. Since we store the rows as balanced binary trees, each of these $|i|$ insertions takes ${O{({\log{|j|}})}} \leq {O{({\log n})}}$ time. We then update the other elements of the $j$th row, of which there are at most ${|i|} + {|j|}$, according to Eqs. (10b) and (10c).

<!-- chunk {"id": "body-0030", "role": "body", "section": "The algorithm", "weight": 1.0} -->

We also have to update the max-heaps for each row and the overall max-heap $H$. Reforming the max-heap corresponding to the $j$th row can be done in $O{({|j|})}$ time. Updating the max-heap for the $k$th row by inserting, raising, or lowering $\DeltaQ_{kj}$ takes ${O{({\log{|k|}})}} \leq {O{({\log n})}}$ time. Since we have changed the maximum element on at most ${|i|} + {|j|}$ rows, we need to do at most ${|i|} + {|j|}$ updates of $H$, each of which takes $O{({\log n})}$ time, for a total of $O{({{({{|i|} + {|j|}})}{\log n}})}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The algorithm", "weight": 1.0} -->

Finally, the update $a_{j}' = {a_{j} + a_{i}}$ (and $a_{i} = 0$) is trivial and can be done in constant time.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The algorithm", "weight": 1.0} -->

Since each join takes $O{({{({{|i|} + {|j|}})}{\log n}})}$ time, the total running time is at most $O{({\log n})}$ times the sum over all nodes of the dendrogram of the degrees of the corresponding communities. Let us make the worst-case assumption that the degree of a community is the sum of the degrees of all the vertices in the original network comprising it. In that case, each vertex of the original network contributes its degree to all of the communities it is a part of, along the path in the dendrogram from it to the root. If the dendrogram has depth $d$, there are at most $d$ nodes in this path, and since the total degree of all the vertices is $2m$, we have a running time of $O{({md{\log n}})}$ as stated.

<!-- chunk {"id": "body-0033", "role": "body", "section": "The algorithm", "weight": 1.0} -->

We note that, if the dendrogram is unbalanced, some time savings can be gained by inserting the sparser row into the less sparse one. In addition, we have found that in practical situations it is usually unnecessary to maintain the separate max-heaps for each row. These heaps are used to find the largest element in a row quickly, but their maintenance takes a moderate amount of effort and this effort is wasted if the largest element in a row does not change when two rows are amalgamated, which turns out often to be the case. Thus we find that the following simpler implementation works quite well in realistic situations: if the largest element of the $k$th row was $\DeltaQ_{ki}$ or $\DeltaQ_{kj}$ and is now reduced by Eq. (10b) or (10c), we simply scan the $k$th row to find the new largest element. Although the worst-case running time of this approach has an additional factor of $n$, the average-case running time is often better than that of the more sophisticated algorithm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "The algorithm", "weight": 1.0} -->

It should be noted that the hierarchies generated by these two versions of our algorithm will differ slightly as a result of the differences in how ties are broken for the maximum element in a row. However, we find that in practice these differences do not cause significant deviations in the modularity, the community size distribution, or the composition of the largest communities.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Amazon.com purchasing network", "weight": 1.0} -->

The output of the algorithm described above is precisely the same as that of the slower hierarchical algorithm of. The much improved speed of our algorithm however makes possible studies of very large networks for which previous methods were too slow to produce useful results. Here we give one example, the analysis of a co-purchasing or "recommender" network from the online vendor Amazon.com. Amazon sells a variety of products, particularly books and music, and as part of their web sales operation they list for each item A the ten other items most frequently purchased by buyers of A. This information can be represented as a directed network in which vertices represent items and there is a edge from item A to another item B if B was frequently purchased by buyers of A. In our study we have ignored the directed nature of the network (as is common in community structure calculations), assuming any link between two items, regardless of direction, to be an indication of their similarity. The network we study consists of items listed on the Amazon web site in August 2003. We concentrate on the largest component of the network, which has $409\, 687$ items and $2\, 464\, 630$ edges.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Amazon.com purchasing network", "weight": 1.0} -->

The dendrogram for this calculation is of course too big to draw, but Fig. 1 illustrates the modularity over the course of the algorithm as vertices are joined into larger and larger groups. The maximum value is $Q = 0.745$, which is high as calculations of this type go; and indicates strong community structure in the network. The maximum occurs when there are $1684$ communities with a mean size of $243$ items each. Fig. 2 gives a visualization of the community structure, including the major communities, smaller "satellite" communities connected to them, and "bridge" communities that connect two major communities with each other.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Amazon.com purchasing network", "weight": 1.0} -->

General interest: politics; art/literature; general fiction; human nature; technical books; how things, people, computers, societies work, etc.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Amazon.com purchasing network", "weight": 1.0} -->

The arts: videos, books, DVDs about the creative and performing arts Hobbies and interests I: self-help; self-education; popular science fiction, popular fantasy; leisure; etc.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Amazon.com purchasing network", "weight": 1.0} -->

Hobbies and interests II: adventure books; video games/comics; some sports; some humor; some classic fiction; some western religious material; etc. classical music and related items children’s videos, movies, music and books church/religious music; African-descent cultural books; homoerotic imagery pop horror; mystery/adventure fiction jazz; orchestral music; easy listening engineering; practical fashion Table 1: The 10 largest communities in the Amazon.com network, which account for 87% of the vertices in the network.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Amazon.com purchasing network", "weight": 1.0} -->

Looking at the largest communities in the network, we find that they tend to consist of items (books, music) in similar genres or on similar topics. In Table 1, we give informal descriptions of the ten largest communities, which account for about 87% of the entire network. The remainder is generally divided into small, densely connected communities that represent highly specific co-purchasing habits, e.g., major works of science fiction ($162$ items), music by John Cougar Mellencamp ($17$ items), and books about (mostly female) spies in the American Civil War ($13$ items). It is worth noting that because few real-world networks have community metadata associated with them to which we may compare the inferred communities, this type of manual check of the veracity and coherence of the algorithm's output is often necessary.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Amazon.com purchasing network", "weight": 1.0} -->

One interesting property recently noted in some networks; is that when partitioned at the point of maximum modularity, the distribution of community sizes $s$ appears to have a power-law form ${P{(s)}} \sim s^{- \alpha}$ for some constant $\alpha$, at least over some significant range. The Amazon co-purchasing network also seems to exhibit this property, as we show in Fig. 3, with an exponent $\alpha \simeq 2$. It is unclear why such a distribution should arise, but we speculate that it could be a result either of the sociology of the network (a power-law distribution in the number of people interested in various topics) or of the dynamics of the community structure algorithm. We propose this as a direction for further research.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have described a new algorithm for inferring community structure from network topology which works by greedily optimizing the modularity. Our algorithm runs in time $O{({md{\log n}})}$ for a network with $n$ vertices and $m$ edges where $d$ is the depth of the dendrogram. For networks that are hierarchical, in the sense that there are communities at many scales and the dendrogram is roughly balanced, we have $d \sim {\log n}$. If the network is also sparse, $m \sim n$, then the running time is essentially linear, $O{({n{\log^{2}n}})}$. This is considerably faster than most previous general algorithms, and allows us to extend community structure analysis to networks that had been considered too large to be tractable. We have demonstrated our algorithm with an application to a large network of co-purchasing data from the online retailer Amazon.com. Our algorithm discovers clear communities within this network that correspond to specific topics or genres of books or music, indicating that the co-purchasing tendencies of Amazon customers are strongly correlated with subject matter.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Our algorithm should allow researchers to analyze even larger networks with millions of vertices and tens of millions of edges using current computing resources, and we look forward to seeing such applications.
