<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Maps of Random Walks on Complex Networks Reveal Community Structure

Topics include Community detection, Infomap, Map equation, Random walk, Information theory, Flow-based clustering, Directed networks, Weighted networks, Network science.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the map equation and Infomap, framing community detection as compression of random-walk flows on a network. This shifted part of the field from purely density- or modularity-based partitions toward flow-based communities, especially useful for directed and weighted networks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To comprehend the multipartite organization of large-scale biological and social systems, we introduce a new information theoretic approach that reveals community structure in weighted and directed networks. The method decomposes a network into modules by optimally compressing a description of information flows on the network. The result is a map that both simplifies and highlights the regularities in the structure and their relationships. We illustrate the method by making a map of scientific communication as captured in the citation patterns of more than 6000 journals. We discover a multicentric organization with fields that vary dramatically in size and degree of integration into the network of science. Along the backbone of the network - including physics, chemistry, molecular biology, and medicine - information flows bidirectionally, but the map reveals a directional pattern of citation from the applied fields to the basic sciences.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Abstract", "weight": 1.5} -->

To comprehend the multipartite organization of large-scale biological and social systems, we introduce a new information theoretic approach that reveals community structure in weighted and directed networks. The method decomposes a network into modules by optimally compressing a description of information flows on the network. The result is a map that both simplifies and highlights the regularities in the structure and their relationships. We illustrate the method by making a map of scientific communication as captured in the citation patterns of more than 6000 journals. We discover a multicentric organization with fields that vary dramatically in size and degree of integration into the network of science. Along the backbone of the network --- including physics, chemistry, molecular biology, and medicine --- information flows bidirectionally, but the map reveals a directional pattern of citation from the applied fields to the basic sciences.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Abstract", "weight": 1.5} -->

complex networks \| clustering \| information theory \| compression

<!-- chunk {"id": "body-0006", "role": "body", "section": "Abstract", "weight": 1.5} -->

Biological and social systems are differentiated, multipartite, integrated, and dynamic. Data about these systems, now available on unprecedented scales, are often schematized as networks. Such abstractions are powerful, but even as abstractions they remain highly complex. It is therefore helpful to decompose the myriad nodes and links into modules that represent the network. A cogent representation will retain the important information about the network and reflect the fact that interactions between the elements in complex systems are weighted, directional, interdependent, and conductive. Good representations both simplify and highlight the underlying structures and the relationships which they depict; they are maps.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Abstract", "weight": 1.5} -->

To create a good map, the cartographer must attain a fine balance between omitting important structures by oversimplification, and obscuring significant relationships in a barrage of superfluous detail. The best maps convey a great deal of information, but require minimal bandwidth: the best maps are also good compressions. By adopting an information-theoretic approach, we can measure how efficiently a map represents the underlying geography --- and we can measure how much detail is lost in the process of simplification. This allows us to quantify and resolve the cartographer's tradeoff.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Network maps and coding theory", "weight": 1.0} -->

In this paper, we use maps to describe the dynamics across the links and nodes in directed, weighted networks that represent the local interactions among the subunits of a system. These local interactions induce a system-wide flow of information that characterizes the behavior of the full system. Consequently, if we want to understand how network structure relates to system behavior, we need to understand the flow of information on the network. We therefore identify the modules which compose the network by finding an optimally compressed description of how information flows on the network. A group of nodes among which information flows quickly and easily can be aggregated and described as a single well-connected module; the links between modules capture the avenues of information flow between those modules.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Network maps and coding theory", "weight": 1.0} -->

Succinctly describing information flow is a coding or compression problem. The key idea in coding theory is that a data stream can be compressed by a code that exploits regularities in the process that generates the stream. We use a random walk as a proxy for the information flow, because a random walk uses all of the information in the network representation and nothing more. Thus it provides a default mechanism for generating a dynamics from a network diagram alone.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Network maps and coding theory", "weight": 1.0} -->

Taking this approach, we develop an efficient code to describe a random walk on a network. We thereby show that finding community structure in networks is equivalent to solving a coding problem. We exemplify this by making a map of science, based on how information flows among scientific journals by means of citations.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Describing a path on a network", "weight": 1.0} -->

To illustrate what coding has to do with map-making, consider the following communication game. Suppose that you and I both know the structure of a weighted directed network. We aim to choose a code that will allow us to efficiently describe paths on the network that arise from a random walk process, in a language that reflects the underlying structure of the network. How should we design our code?

<!-- chunk {"id": "body-0012", "role": "body", "section": "Describing a path on a network", "weight": 1.0} -->

If maximal compression were our only objective, we could encode the path at or near the entropy rate of the corresponding Markov process. Shannon showed that one can achieve this rate by assigning to each node a unique dictionary over the outgoing transitions. But compression is not our only objective; here want our language to reflect the network structure, we want the words we use to refer to things in the world. Shannon's approach does not do this for us, because every codeword would have a different meaning depending on where it is used. Compare maps: useful maps assign unique names to important structures. Thus we seek a way of describing or encoding the random walk in which important structures indeed retain unique names.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Describing a path on a network", "weight": 1.0} -->

Let us look at a concrete example. Figure 1A shows a weighted network with $n = 25$ nodes. The link thickness indicates the relative probability that a random walk will traverse any particular link. Overlaid upon the network is a specific 71-step realization of a random walk that we will use to illustrate our communication game. In panels 1B--D, we describe this walk with increasing levels of compression, exploiting more and more of the regularities in the network.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Huffman coding", "weight": 1.0} -->

A straightforward method of giving names to nodes is to use a Huffman code. Huffman codes save space by assigning short codewords to common events or objects, and long codewords to rare ones, much as common words are short in spoken languages. Figure 1B shows a prefix-free Huffman coding for our sample network. Each codeword specifies a particular node, and the codeword lengths are derived from the ergodic node visit frequencies of an infinitely long random walk. With the Huffman code pictured in Fig. 1B, we are able to describe the specific 71-step walk in 314 bits. If we instead had chosen a uniform code, in which all codewords are of equal length, each codeword would be ${\lceil{\log 25}\rceil} = 5$ bits long and ${71 \cdot 5} = 355$ bits would have been required to describe the walk.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Huffman coding", "weight": 1.0} -->

Though in this example we assign actual codewords to the nodes for illustrative purposes, in general we will not be interested in the codewords themselves, but rather in the theoretical limit of how concisely we can specify the path. Here we invoke Shannon's source coding theorem which implies that when you use $n$ codewords to describe the $n$ states of a random variable $X$ that occur with frequencies $p_{i}$, the average length of a codeword can be no less than the entropy of the random variable $X$ itself: ${H{(X)}} = {- {\sum_{1}^{n}{p_{i}{\log{(p_{i})}}}}}$. This theorem provides us with the necessary apparatus to see that in our Huffman illustration, the average number of bits needed to describe a single step in the random walk is bounded below by the entropy $H{(P)}$, where $P$ is the distribution of visit frequencies to the nodes on the network. We define this lower bound on code length to be $L$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Huffman coding", "weight": 1.0} -->

For example, $L = 4.50$ bits/step in Fig. 1B.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Highlighting important objects", "weight": 1.0} -->

Matching the length of codewords to the frequencies of their use gives us efficient codewords for the nodes, but no map. Merely assigning appropriate-length names to the nodes does little to simplify or highlight aspects of the underlying structure. To make a map, we need to separate the important structures from the insignificant details. We therefore divide the network into two levels of description. We retain unique names for large-scale objects, the clusters or modules to be identified within our network, but we reuse the names associated with fine-grain details, the individual nodes within each module. This is a familiar approach for assigning names to objects on maps: most US cities have unique names, but street names are reused from one city to the next, such that each city has a Main Street and a Broadway and a Washington Avenue and so forth. The reuse of street names rarely causes confusion, because most routes remain within the bounds of a single city.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Highlighting important objects", "weight": 1.0} -->

A two-level description allows us to describe the path in fewer bits than we could do with a one-level description. We capitalize on the network's structure --- and in particular, on the fact that a random walker is statistically likely to spend long periods of time within certain clusters of nodes. Figure 1C illustratess this approach. We give each cluster a unique name, but use a different Huffman code to name the nodes within each cluster. A special codeword, the exit code, is chosen as part of the within-cluster Huffman coding and indicates that the walk is leaving the current cluster. The exit code is always followed by the "name" or module code of the new module into which the walk is moving (see supporting online material for more details). Thus we assign unique names to coarse-grain structures, the cities in the city metaphor, but reuse the names associated with fine-grain details, the streets in the city metaphor. The savings are considerable; in the two-level description of Fig 1C the limit $L$ is $3.05$ bits/step compared to 4.50 for the one-level description.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Highlighting important objects", "weight": 1.0} -->

Herein lies the duality between finding community structure in networks and the coding problem: to find an optimal code, we look for a module partition $\mathsf{M}$ of $n$ nodes into $m$ modules so as to minimize the expected description length of a random walk. Using the module partition $\mathsf{M}$, the average description length of a single step is given by

<!-- chunk {"id": "body-0020", "role": "body", "section": "Highlighting important objects", "weight": 1.0} -->

This equation comprises two terms: first is the entropy of the movement between modules, and second is the entropy of movements within modules (where exiting the module is also considered a movement). Each is weighted by the frequency with which it occurs in the particular partitioning. Here $q_{\curvearrowright}$ is the probability that the random walk switches modules on any given step. $H{(\mathcal{Q})}$ is the entropy of the module names, i.e., the entropy of the underlined codewords in Fig. 1D. $H{(\mathcal{P}^{i})}$ is the entropy of the within-module movements --- including the exit code for module $i$. The weight $p_{\circlearrowright}^{i}$ is the fraction of within module movements that occur in module $i$, plus the probability of exiting module $i$ such that ${\sum_{i = 1}^{m}p_{\circlearrowright}^{i}} = {1 + q_{\curvearrowright}}$ (see supporting online material for more details).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Highlighting important objects", "weight": 1.0} -->

For all but the smallest networks, it is infeasible to check all possible partitions to find the one that minimizes the description length in the map equation (Eq. 1). Instead we use computational search. We first compute the fraction of time each node is visited by a random walker using the power method, and using these visit frequencies we explore the space of possible partitions using a deterministic greedy search algorithm. We refine the results with a simulated annealing approach using the heat-bath algorithm (see supporting online material for more details).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Highlighting important objects", "weight": 1.0} -->

In the interest of visual simplicity, the illustrative network in Fig. 1 has weighted but undirected links. Our method is developed more generally, so that we can extract information from networks with links that are directed in addition to being weighted. The map equation remains the same, only the path that we aim to describe must be slightly modified to achieve ergodicity. We introduce a small "teleportation probability" $\tau$ in the random walk: with probability $\tau$ the process jumps to a random node anywhere in the network. This converts our random walker into the sort of "random surfer" that drives Google's PageRank algorithm. Our clustering results are highly robust to the particular choice of the small fraction $\tau$. For example, so long as $\tau < 0.45$ the optimal partitioning of the network in Fig. 1 remains exactly the same. In general, the more significant the regularities, the higher $\tau$ can be before frequent teleportation swamps the network structure. We choose $\tau = 0.15$ corresponding to the well known damping factor $d = 0.85$ in the PageRank algorithm.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Mapping flow compared to maximizing modularity", "weight": 1.0} -->

The traditional way of identifing community structure in directed and weighted networks has been to simply disregard the directions and the weights of the links. But such approaches discard valuable information about the network structure. By mapping the system-wide flow induced by local interactions between nodes, we retain the information about the directions and the weights of the links. We also acknowledge their interdependence in networks inherently characterized by flows. This makes it interesting to compare our flow-based approach with recent topological approaches based on modularity optimization that also makes use of information about weight and direction. In its most general form, the modularity for a given partitioning of the network into $m$ modules is the sum of the total weight of all links in each module minus the expected weight

<!-- chunk {"id": "body-0024", "role": "body", "section": "Mapping flow compared to maximizing modularity", "weight": 1.0} -->

Here $w_{ii}$ is the total weight of links starting and ending in module $i$, $w_{i}^{in}$ and $w_{i}^{out}$ the total in- and out-weight of links in module $i$, and $w$ the total weight of all links in the network. To estimate the community structure in a network, Eq. 2 is maximized over all possible assignments of nodes into any number $m$ of modules.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Mapping flow compared to maximizing modularity", "weight": 1.0} -->

The two equations and reflect two different senses of what it means to have a network. The former, which we pursue here, finds the essence of a network in the patterns of flow that its structure induces. The latter effectively situates the essence of network in the combinatoric properties of its links (as we did in ref. ).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Mapping flow compared to maximizing modularity", "weight": 1.0} -->

Does this conceptual distinction make any practical difference? Figure 2 illustrates two simple networks for which the map equation and modularity give different partitionings. The weighted, directed links shown in the network in panel A induce a structured pattern of flow with long persistence times, and limited flow between, the four clusters as highlighted on the left. The map equation picks up on these structural regularities and thus the description length is much shorter for the partitioning in the left-hand figure (2.67 bits/step) than for the right-hand one (4.13 bits/step). Modularity is blind to the interdependence in networks characterized by flows, and thus cannot pick up on this type of structural regularity. It only counts weights of links, in-degree, and out-degree in the modules, and thus prefers to partition the network as shown on the right with the heavily weighted links inside of the modules.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Mapping flow compared to maximizing modularity", "weight": 1.0} -->

In panel B, by contrast, there is no pattern of extended flow at all. Every node is either a source or a sink, and no movement along the links on the network can exceed more than one step in length. As a result, random teleportation will dominate (irrespective of teleportation rate) and any partition into multiple modules will lead to a high flow between the modules. For a network such as in panel B, where the links do not induce a pattern of flow, the map equation will always partition the network into one single module. Modularity, because it looks at pattern in the links and in- and out-degree, separates the network into the clusters shown at right.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Mapping flow compared to maximizing modularity", "weight": 1.0} -->

Which method should a researcher use? It depends on which of the two senses of network, described above, that one is studying. For analyzing network data where links represented patterns of movement among nodes, flow-based approaches such as the map equation are likely to identify the most important aspects of structure. For analyzing network data where links represent not flows but rather pairwise relationships, it may be useful to detect structure even where no flow exists. For these systems, combinatoric methods such as modularity or cluster-based compression may be preferable.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Mapping scientific communication", "weight": 1.0} -->

Science is a highly organized and parallel human endeavor to find patterns in nature; the process of communicating research findings is as essential to progress as is the act of conducting the research in the first place. Thus science is not merely a set of ideas, but also the flow of these ideas through a multipartite and highly differentiated social system. Citation patterns among journals allow us to glimpse this flow, and provide the trace of communication between scientists. To highlight important fields and their relationships, to uncover differences and changes, to simplify and make the system comprehensible --- we need a good map of science.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Mapping scientific communication", "weight": 1.0} -->

Using the information theoretic approach presented above, we map the flow of citations among 6,128 journals in the sciences (Fig. 3) and social sciences (Fig. 4). The 6,434,916 citations in this cross-citation network represent a trace of the scientific activity during 2004. Our data tally on a journal-by-journal basis the citations from articles published in 2004 to articles published in the previous five years. We exclude journals that that publish fewer than 12 articles per year, and those which do not cite other journals within the data set. We also exclude the only three major journals that span a broad range of scientific disciplines: *Science*, *Nature*, and *Proceedings of the National Academy of Sciences*; the broad scope of these journals otherwise creates an illusion of tighter connections among disciplines, when in fact few readers of the physics articles in *Science* are also close readers of the biomedical articles therein. Because we are interested in relationships between journals, we also exclude journal self-citations.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Mapping scientific communication", "weight": 1.0} -->

Through the operation of our algorithm, the fields and the boundaries between them emerge directly from the citation data, rather than from our preconceived notions of scientific taxonomy (see Figs. 3 and 4). Our only subjective contribution has been to suggest reasonable names for each cluster of journals that the algorithm identifies: economics, mathematics, geosciences, and so forth.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Mapping scientific communication", "weight": 1.0} -->

The physical size of each module or "field" on the map reflects the fraction of time that a random surfer spends following citations within that module. Field sizes vary dramatically. Molecular biology includes 723 journals that span the areas of genetics, cell biology, biochemistry, immunology, and developmental biology; a random surfer spends 26% of her time in this field, indicated by the size of the module. Tribology (the study of friction) includes only 7 journals, in which a random surfer spends 0.064% of her time.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Mapping scientific communication", "weight": 1.0} -->

The weighted and directed links between fields represent citation flow, with the color and width of the arrows indicating flow volume. The heavy arrows between medicine and molecular biology indicate a massive traffic of citations between these disciplines. The arrows point in the direction of citation: $A\rightarrow B$ means "$A$ cites $B$" as shown in the legend. These directed links reveal the relationship between applied and basic sciences. We find that the former cite the latter extensively, but the reverse is not true, as we see e.g. with geotechnology citing geosciences, plastic surgery citing general medicine, and power systems citing general physics. The thickness of the module borders reflect the probability that a random surfer within the module will follow a citation to a journal outside of the module. These outflows show a large variation; for example the outflow is 30% in general medicine but only 12% in economics.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Mapping scientific communication", "weight": 1.0} -->

The map reveals a ring-like structure in which all major disciplines are connected to one another by chains of citations --- but these connections are not always direct, because fields on opposite sides of the ring are linked only through intermediate fields. For example, while psychology rarely cites general physics or visa versa, psychology and general physics are connected via the strong links to and between the intermediaries molecular biology and chemistry. Once we consider the weights of the links among fields, however, it becomes clear that the structure of science is more like the letter $\mathbf{U}$ than like a ring, with the social sciences at one terminal and engineering at other, joined mainly by a backbone of medicine, molecular biology, chemistry, and physics. Because our map shows the pattern of citations to research articles published within five years, it represents what de Sola Price called the "research frontier," rather than the long-term interdependencies among fields. For example, while mathematics are essential to all natural sciences, the field of mathematics is not central in our map because only certain subfields (e.g. areas of physics and statistics) rely heavily on the most recent developments in pure mathematics and contribute in return to the research agenda in that field.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Mapping scientific communication", "weight": 1.0} -->

When a cartographer designs a map, the scale or scope of the map influences the choice of which objects are represented. A regional map omits many of the details that appear on a city map. Similarly, in the approach that we have developed here, the appropriate size or resolution of the modules depends on the universe of nodes that are included in the network. If we compare the map of a network to a map of a subset of the same network, we would expect to see the map of the subset to reveal finer divisions, with modules composed of fewer nodes. Figure 4 illustrates this by partitioning a subset of the journals included in the map of science: the 1,431 journals in the the social sciences. The basic structure of the fields and their relations remains unchanged, with psychiatry and psychology linked via sociology and management to economics and political science, but the map also reveals further details. Anthropology fractures along the physical / cultural divide. Sociology divides into behavioral and institutional clusters. Marketing secedes from management. Psychology and psychiatry reveal a set of applied subdisciplines.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Mapping scientific communication", "weight": 1.0} -->

The additional level of detail in the more narrowly focused map would have been clutter on the full map of science. When we design maps to help us comprehend the world, we must find that balance where we eliminate extraneous detail but highlight the relationships among important structures. Here we have shown how to formalize this cartographer's precept using the mathematical apparatus of information theory.
