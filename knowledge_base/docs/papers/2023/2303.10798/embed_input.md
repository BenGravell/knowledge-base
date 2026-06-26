<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Aperiodic Monotile

Topics include Aperiodic monotile.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A longstanding open problem asks for an aperiodic monotile, also known as an "einstein": a shape that admits tilings of the plane, but never periodic tilings. We answer this problem for topological disk tiles by exhibiting a continuum of combinatorially equivalent aperiodic polygons. We first show that a representative example, the "hat" polykite, can form clusters called "metatiles", for which substitution rules can be defined. Because the metatiles admit tilings of the plane, so too does the hat. We then prove that generic members of our continuum of polygons are aperiodic, through a new kind of geometric incommensurability argument. Separately, we give a combinatorial, computer-assisted proof that the hat must form hierarchical - and hence aperiodic - tilings.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given a set of two-dimensional tiles, the nature of the planar tilings that they admit arises from a deep interaction between the local and the global. Constraints on the ways that two neighbouring tiles interlock can reverberate through the global structure of a tiling at every scale. Local constraints encoded in a set of tiles determine the larger space of tilings they admit in subtle ways.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Aperiodic sets of tiles walk a fine line between order and disorder, admitting tilings, but only those without the simple repetition of translational symmetry. Their study dates to Wang's work on the then remaining open cases of Hilbert's Entscheidungsproblem. Wang encoded logical fragments by what are now known as Wangtiles -congruent squares with coloured edges-to be tiled by translation only with colours matching on adjoining edges. He conjectured that every set of Wang tiles that admits a tiling (possibly using only a subset of the tiles) must also admit a periodic tiling, and showed that this would imply the decidability of the tiling problem (or domino problem ): the question of whether a given set of Wang tiles admits any tilings at all. The algorithm would consist of enumerating, for each positive integer n, the finite set of all legal n × n blocks of tiles. If there is no tiling by the tiles, there must be some n for which no such block exists (by the Extension Theorem [, Theorem 3.8.1], which ultimately depends on the compactness of spaces of patches), and we will eventually encounter the smallest such n.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, if there is a fundamental domain for a periodic tiling, we will eventually discover it in a block. If Wang's conjecture held and aperiodic sets of tiles did not exist, this algorithm would always terminate.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

∗ Development of software used in this work was supported in part by a Senior Rouse Ball Studentship for 2002-3 from Trinity College, Cambridge.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Subsequent decades have spawned a rich literature on aperiodic tiling, touching many different mathematical and scientific settings; we do not attempt a broad survey here. Yet there remain remarkably few really distinct methods of proving aperiodicity in the plane, despite or due to the underlying undecidability of the tiling problem.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Berger then showed that it was undecidable whether a set of Wang tiles admits a tiling of the plane. He constructed the first aperiodic set of 20426 Wang tiles, which he used as a kind of scaffolding for encoding finite but unbounded runs of arbitrary computation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Berger's initial set comprised thousands of tiles, naturally prompting the question of how small a set of tiles could be while still forcing aperiodicity. Professional and amateur mathematicians produced successively smaller aperiodic sets, culminating in discoveries by Penrose and others of several consisting of just two tiles. Surveys of these sets appear in Chapters 10 and 11 of Gr¨ unbaum and Shephard and in an account of the Trilobite and Cross tiles. A recent table appears in the work of Greenfeld and Tao, counting tiles by translation classes (tiles in different orientations are counted as distinct).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The obvious conclusion of this reduction in size would be to arrive at an aperiodic monotile, a single shape that can form tilings (is a monotile) but can only form non-periodic ones (is aperiodic). Such a shape is also sometimes referred to as an 'einstein' (a pun from the German 'ein stein', roughly 'one shape', popularized by Danzer). In the present article we reserve these terms for two-dimensional closed topological disks that tile aperiodically purely by virtue of their geometry, without the need for any kind of non-geometric matching rules that further constrain tile adjacencies. It has long been an open question whether such a tile exists. Can one tile embody enough complexity to forcibly disrupt periodic order at all scales?

<!-- chunk {"id": "body-0011", "role": "body", "section": "The search for an einstein", "weight": 1.0} -->

Several candidate tiles have been proposed as einsteins, but they all challenge in some way the concepts of 'tile', 'tiling', or 'aperiodic'.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The search for an einstein", "weight": 1.0} -->

Tiles are often endowed with matching rules that constrain their placement. Matching rules have taken a variety of different forms in the literature. They sometimes act as a symbolic proxy for neighbour relationships that could easily be encoded geometrically, but they can also determine more complex relationships between tiles. The Taylor-Socolar tile is a regular hexagon with matching rules in the form of markings in the interiors of tiles. The matching rules force aperiodicity, but they require non-adjacent tiles to exchange information. As a result, it is impossible to reduce the behaviour of the tile to the shape of a closed two-dimensional topological disk. The matching rules can be expressed purely geometrically, but doing so requires either a disconnected tile, a tile with cutpoints, or a three-dimensional shape that aperiodically tiles a thickened plane R 2 ×.

<!-- chunk {"id": "body-0013", "role": "body", "section": "The search for an einstein", "weight": 1.0} -->

Gummelt and Jeong and Steinhardt describe a single regular decagon that can cover the plane with copies that are allowed to overlap by prescribed rules, but only non-periodically, in a manner tightly coupled to the Penrose tiling. Senechal [Sen] similarly describes simple rules that allow copies of the Penrose dart to overlap and cover the plane, but never periodically. The result is an ingenious route to aperiodicity, but not a tiling in the usual sense.

<!-- chunk {"id": "body-0014", "role": "body", "section": "The search for an einstein", "weight": 1.0} -->

The structure of the Taylor-Socolar tiling is closely related to Penrose's 1 + ϵ + ϵ 2 tiling. Like the Trilobite and Crab tiles, these can be adjusted so that an arbitrarily high fraction of the area lies in copies of just one kind of tile. But no matter how thin or small they become, the other tiles remain necessary.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The search for an einstein", "weight": 1.0} -->

Loosely speaking, it is often possible to shift the complexity in a construction from the tiles to the matching rules or vice versa. For example, if we use a finite atlas of finite configurations as our allowed matching rules, even the lowly 2 × 1 rectangle is an aperiodic monotile! 1 Walton and Whittaker recently described a hexagonal tile that, like the Taylor-Socolar tile, achieves aperiodicity via a system of markings. These 'orientational' rules are edge-to-edge, in that they only constrain a tile's relationships to its immediate neighbours. However, this tile's behaviour also cannot be expressed as pure geometry.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The search for an einstein", "weight": 1.0} -->

Following Mozes, we say a set of tiles is strongly aperiodic if it admits tilings but none with any infinite cyclic symmetry. In the Euclidean plane, a set of 'normal' tiles is weakly aperiodic if and only if it is strongly aperiodic [, Theorem 3.7.1], leaving us with a single notion of aperiodicity there.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The search for an einstein", "weight": 1.0} -->

Moving to higher dimensional space permits richer forms of aperiodicity to arise. The Schmitt-Conway-Danzer tile [, Section 7.2] tiles R 3, with tilings that never have translations as symmetries; none of its tilings have compact fundamental domains. However, the tile does admit a tiling whose symmetry group contains a screw motion, and hence an infinite cyclic subgroup of screw motions. We refer to such a tile as weakly aperiodic. The 'weak' label is appropriate, as such tiles appear readily in the hyperbolic plane and other non-amenable spaces. As early as 1974, B¨ or¨ oczky exhibited a weakly aperiodic monotile in the hyperbolic plane [B¨ or74], the elegantly simple basis of the 'binary tilings'.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The search for an einstein", "weight": 1.0} -->

Recently, Greenfeld and Tao showed that for a sufficiently high number n of dimensions, a single tile, tiling only by translation, can be aperiodic in Z n (and thus in R n ); Greenfeld and Kolountzakis strengthened this result by showing that the tile can be connected. Greenfeld and Tao also showed that it is undecidable whether a single tile, again tiling by translation, admits a tiling of a periodic subset of Z 2 × G for some nonabelian group G, and subsequently proved this for tiling a periodic subset of Z n (where n is one of the inputs to the decision problem and not fixed). Translational aperiodicity is known to be impossible in R 2. Kenyon, building on the work of Girault-Beauquier and Nivat, showed that any topological disk that admits a tiling by translation also admits a periodic tiling. Bhattacharya showed the same for any finite set in Z 2.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The search for an einstein", "weight": 1.0} -->

Even when a single tile admits periodic tilings, that periodicity may be more or less abstruse, in a way that offers tantalizing hints about aperiodicity. The isohedral number of a tile is the minimumnumberoftransitivity classes in any tiling it admits; a tile is anisohedral if its isohedral number is greater than one. The second part of Hilbert's 18th problem asked whether there exist anisohedral polyhedra in R 3. Gr¨ unbaum and Shephard suggest [, Section 9.6] that this question was asked in R 3 because Hilbert assumed that no such tiles exist in the plane. But Reinhardt found an example of such a polyhedron, and Heesch then gave an Little is known about limits on what sorts of shapes could potentially be aperiodic monotiles. Rao showed through a computer search that the list of 15 known families of convex pentagons that tile the plane is complete, thereby eliminating any remaining possibility that a convex polygon could be an einstein. Jeandel and Rao showed that the smallest aperiodic set of Wang tiles is of size 11.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The search for an einstein", "weight": 1.0} -->

1 Beginning with an aperiodic set of tiles, say, geometric matching rules, pixelate pictures of the tiles and how they fit together, in some black and white bit-map. Take an atlas of these pictures, splitting black pixels vertically and white ones horizontally into identical rectangles. The rectangle is an aperiodic monotile with this atlas of matching rules. example of such a tile in the plane. Many anisohedral prototiles are known today. The computer enumeration by Myers furnished numerous anisohedral polyominoes, polyhexes, and polyiamonds, including a record-holding 16 -hex that tiles with a minimum of ten transitivity classes. It is unknown whether there is an upper bound on isohedral numbers of monotiles. 2 Related insights can be gleaned from the study of shapes that do not tile the plane. A tile's Heesch number is the largest possible combinatorial radius of any patch formed by copies of the shape (or equivalently, the maximum number of complete concentric rings that can be constructed around it). A shape that tiles the plane is said to have a Heesch number of ∞.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The search for an einstein", "weight": 1.0} -->

Heesch first exhibited a shape with Heesch number 1, and a few isolated examples with Heesch numbers up to 3 were discovered thereafter. Mann and Thomas discovered marked polyforms with Heesch numbers up to 5 through a brute-force computer search. Kaplan conducted a search on unmarked polyforms, yielding examples with Heesch numbers up to 4. Baˇ si´ c discovered the current record holder, a shape with Heesch number 6 [Baˇ s21]. Heesch's problem asks which positive integers can be Heesch numbers; beyond specific examples with Heesch numbers up to 6, nothing is known about the solution. An upper bound on finite Heesch numbers would imply the decidability of the tiling problem for a single shape. The algorithm would simply consist of generating all possible concentric rings around a central tile; eventually one will either fail (in which case the shape does not tile the plane) or exceed the upper bound on Heesch numbers (in which case it must tile the plane).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Main result", "weight": 1.0} -->

In this paper, we prove the following: Theorem 1.1. The shape shown shaded in Figure 1.1, a polykite that we call the 'hat', is an aperiodic monotile.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Main result", "weight": 1.0} -->

The shape is almost mundane in its simplicity. It is a polykite: the union of eight kites in the Laves tiling [3. 4. 6. 4] (drawn in thin lines in Figure 1.1), the dual to the (3. 4. 6. 4) Archimedean tiling. No special qualifications or additional matching rules are required: as shown, this shape tiles the plane, but never with any translational symmetries.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Main result", "weight": 1.0} -->

We provide two different proofs of aperiodicity, both with novel aspects. The first proof follows the structure shown in Figure 1.2, centred on a new approach in Section 3 for proving aperiodicity in the plane. We observe that any tiling by the hat corresponds to tilings by two different polyiamonds, one with two thirds the area of the other. If there were a strongly periodic tiling by the hat, the other two tilings would also be strongly periodic. We prove that if so, the lattices of translations in the polyiamond tilings would necessarily be related by a similarity; but no similarity between lattices of translations on the regular triangular tiling can have the scale factor √ 2 required by the ratio of the areas. This argument does not show that a tiling exists, and must be combined with an explicit construction of a tiling (outlined in Section 2 and given in detail in Sections 4 and 5) to complete the proof of aperiodicity.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Main result", "weight": 1.0} -->

2 The problem of determining whether or not a given set of tiles admits a periodic tiling is also undecidable, at least for larger sets of tiles. If we enumerate sets of tiles, and define I ( n ) to be the isohedral number of the n th set if it admits a periodic tiling, and -1 otherwise, then I ( n ) cannot be bounded by any computable function. This defies our imagination.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Main result", "weight": 1.0} -->

In Section 4 we learn that every tiling by hats necessarily contains a mixture of reflected and unreflected tiles. Thus the hat's status as a monotile depends on whether one considers a shape and its reflection to be congruent. By longstanding tradition in the tiling literature (indeed, Because of the combinatorial complexity of the hat polykite, a significant fraction of our second proof relies on exhaustive enumeration of cases, which we carried out and cross-checked with two independent software implementations developed by two of the authors in isolation. These calculations are necessarily ad hoc, and are essentially unenlightening. This case analysis is only needed to show that all tilings follow the substitution structure; it is not needed for showing that a tiling exists, and thus is not needed to show that the tile is aperiodic, given the proof in Section 3 that no periodic tiling exists.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Main result", "weight": 1.0} -->

3 In particular, if a tiling had a translational symmetry, then for sufficiently large k there would exist a levelk supertile that overlaps its image under this translation. Any metatile in the intersection of these two supertiles would then lie within both of their infinite hierarchies, contradicting the supposed uniqueness of those hierarchies [, Theorem 10.1.1]. going back to Euclid's Elements), shapes are considered congruent if they are equivalent under any Euclidean isometry, including those that reverse orientation. The hat is therefore rightly considered a monotile. Still, this potential caveat emphasizes the importance of considering the setting in which a tiling problem is defined: the geometric space in which we are working, conditions on the tiles and their matching rules, and the specific families of isometries that we are allowed to use. The diversity of ideas discussed in Section 1.1 illustrates how context can colour the problem of aperiodicity. We revisit the question of tiling aperiodically without reflections in Section 7.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Main result", "weight": 1.0} -->

We close this introduction with definitions of the essential terminology we will need for the rest of the article. In Section 2, we then present a compendium of provisional observations about this polykite, including an explicit construction of a tiling and aspects of its structure that deserve further study. Our two proofs of aperiodicity follow: we show that there are no periodic tilings (Section 3), then that tiles must group into clusters that define metatiles equipped with matching rules (Section 4), and finally that metatiles must compose into supertiles with combinatorially equivalent matching rules (Section 5). In Section 6, we offer additional remarks about the continuum of tiles that contains the hat polykite. As noted there, computer search shows that the hat is the smallest aperiodic polykite.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Terminology", "weight": 1.0} -->

Terminology used for tilings generally follows that of Gr¨ unbaum and Shephard.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Terminology", "weight": 1.0} -->

In any locally finite tiling of the plane by closed topological disks, the connected components of the intersection of two or more tiles are isolated points, which are called vertices of the tiling, and Jordan arcs, which are called edges of the tiling, and the boundary of any tile is divided into finitely many edges, alternating with vertices. Each edge lies on the boundary of exactly two tiles, which we refer to as lying on opposite sides of the edge. Two distinct tiles are neighbours if they share any point of their boundaries, and adjacents if they share an edge.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Terminology", "weight": 1.0} -->

A tile in a metric space is a closed set of points from that space. A tiling by a set of tiles is a collection of images of tiles from that set under isometries, the interiors of which are pairwise disjoint and the union of which is the whole space; we say a set of tiles admits the tiling, or in the case of a single tile that it admits the tiling. For most purposes, it is convenient for tiles to be nonempty compact sets that are the closures of their interiors; the tiles considered here are polygons, or more generally closed topological disks. A tiling is monohedral if all its tiles are congruent (where congruences can incorporate mirror reflections). All tilings considered here are also locally finite: every circular disk meets only finitely many tiles. Every monohedral plane tiling by closed topological disks is locally finite.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Terminology", "weight": 1.0} -->

When a (closed topological disk) tile has a polygonal boundary, we refer to it as having sides (maximal straight line segments lying on that boundary) and corners (between two sides), to distinguish these features from the edges and vertices of a tiling. We rely on context to distinguish the meanings of 'side' as referring to sides of a polygon or the two sides of an edge of a tiling. A tiling by polygons is edge-to-edge if the corners and sides of the polygons coincide with the vertices and edges of the tiling.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Terminology", "weight": 1.0} -->

A patch of tiles is a collection of non-overlapping tiles whose union is a topological disk.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Terminology", "weight": 1.0} -->

More specifically, a 0 -patch is a patch containing a single tile, and an ( n +1) -patch is a patch formed from the union of an n -patch P and a set S of additional tiles, so that P lies in the interior of the patch and no proper subset of S yields a patch with P in its interior. (In other words, an n -patch is a tile surrounded by n concentric rings of tiles.) Every tile in a fixed tiling generates an n -patch for all finite n, by recursively constructing an ( n -1) -patch and adjoining all its neighbours in the tiling, along with any other tiles required to fill in holes left by adding neighbours.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Terminology", "weight": 1.0} -->

The symmetry group of a tiling is the group of those isometries that act as a permutation on the tiles of the tiling. A tiling is weakly periodic if its symmetry group has an element of infinite order; in the plane, this means it includes a nonzero translation. 4 A tiling is strongly periodic if the symmetry group has a discrete subgroup with cocompact action on the space tiled. In Euclidean space, all strongly periodic tilings are also weakly periodic. A set of tiles (or a single tile) is weakly aperiodic if it admits a tiling but does not admit a strongly periodic tiling, and strongly aperiodic if it admits a tiling but does not admit a weakly periodic tiling.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Terminology", "weight": 1.0} -->

Given a tiling T, a polyT -tile is a closed topological disk that is the union of finitely many tiles from T; in other words, it is the union of the tiles in a patch within T. PolyT -tiles are also referred to generically as polyforms. PolyT -tiles may also be defined so that they are permitted to have holes. Because we are mainly concerned with tiles that admit monohedral tilings, it is not generally significant for the purposes of this paper whether shapes with holes are allowed or not.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Terminology", "weight": 1.0} -->

Any finite set of polygons in the plane that admits a weakly periodic edge-to-edge tiling also admits a strongly periodic tiling [, Theorem 3.7.1]. A similar but simpler argument shows the same to be the case for a finite set of polyT -tiles where T is itself a strongly periodic tiling and the weakly periodic tiling consists of copies of the tiles all aligned to the same underlying copy of T, instead of being edge-to-edge. Thus in such contexts it is not necessary to distinguish weak and strong aperiodicity and we refer to tiles and sets of tiles simply as aperiodic.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Terminology", "weight": 1.0} -->

A uniform tiling [, Section 2.1] is an edge-to-edge tiling by regular polygons with a vertex-transitive symmetry group. In the Euclidean plane, a uniform tiling can be described by listing the sequence of regular polygons around each vertex, yielding notation such as (3. 4. 6. 4). A Laves tiling [, Section 2.7] is an edge-to-edge monohedral tiling by convex polygons with regular vertices (all angles between consecutive edges at a vertex equal) and a tile-transitive symmetry group. Analogous notation such as [3. 4. 6. 4] is used for Laves tilings, listing the sequence of vertex degrees round each tile, and in an appropriate sense Laves tilings are dual to uniform tilings.

<!-- chunk {"id": "body-0039", "role": "body", "section": "The hat polykite and its tilings", "weight": 1.0} -->

Before proceeding to the full proof of aperiodicity, we first offer a less formal presentation of the hat, including an explicit construction of a tiling. This section fulfills three goals. First, it offers an abundance of visual intuition, which provides context for the technical machinery that will follow. Second, it gives some sense of our process of discovery and analysis, though it should not be interpreted as an ordered timeline. Third, it includes a few observations that will not be considered further in this article, but which might provide opportunities for future work by others.

<!-- chunk {"id": "body-0040", "role": "body", "section": "The hat polykite and its tilings", "weight": 1.0} -->

4 Some authors such as Greenfeld and Tao have used the term 'weakly periodic' to refer to a tiling that is a finite union of sets of tiles, each of which is weakly periodic in the sense used here.

<!-- chunk {"id": "body-0041", "role": "body", "section": "The hat polykite and its tilings", "weight": 1.0} -->

Because the hat is a polyform, it was natural at this point to obtain an initial diagnosis of its tiling properties computationally. We modified Kaplan's SAT-based Heesch number software to determine that if the hat does not tile the plane, then its Heesch number must be at least 16. Similarly, we modified Myers' polyform tiling software to determine that if the hat admits periodic tilings, then its isohedral number must be at least 64. These two computations already establish that the hat is of extreme interest-if it had turned out not to be an einstein, then it would have shattered either the record for Heesch numbers or the record for isohedral numbers, in both cases by a wide margin.

<!-- chunk {"id": "body-0042", "role": "body", "section": "The hat polykite and its tilings", "weight": 1.0} -->

The first author (Smith) began investigating the hat polykite as part of his open-ended visual exploration of shapes and their tiling properties. Working largely by hand, with the assistance of Scherphuis's PolyForm Puzzle Solver software ( www.jaapsch.net/puzzles/polysolver. htm ), he could find no obvious barriers to the construction of large patches, and yet no clear cluster of tiles that filled the plane periodically.

<!-- chunk {"id": "body-0043", "role": "body", "section": "The hat polykite and its tilings", "weight": 1.0} -->

The most important colouring for the purposes of this article is the one shown on the right in Figure 2.1. A single hat is asymmetric, and so in any patch we can distinguish between 'unreflected' and 'reflected' orientations of tiles. In the patches we computed, reflected tiles (shown in dark blue) are always distributed sparsely and evenly within a field of unreflected tiles. Furthermore, every reflected tile is contained within a congruent cluster of nine tiles, where the other eight tiles in the cluster are unreflected. One such cluster is outlined in bold in the illustration. The interior of the patch can be covered completely by overlapping copies of that cluster. Within the cluster, we are particularly interested in the 'shell' of three light blue tiles adjacent to each reflected tile. Every reflected tile resides in a congruent, non-overlapping copy of this shell.

<!-- chunk {"id": "body-0044", "role": "body", "section": "The hat polykite and its tilings", "weight": 1.0} -->

We have also observed that unreflected tiles tend to form long 'chains' of like orientation, occasionally interrupted by reflected tiles. The chains contained in the example patch are shown coloured on the left in Figure 2.2. Because the hats are aligned with the underlying kite grid, unreflected tiles come in six orientations, all of which also appear as chain directions. Chains may end at reflected tiles or pass through them, but each reflected tile is a hub for at least two, and at most five spokes. Long segments of these chains have boundaries with halfturn symmetry. It is tempting to seek parallels between these chains and linear features in other aperiodic tilings, such as Ammann bars [, Section 10.6] and Conway worms [, Section 10.5]. Finally, we have noticed that these chains seem to impart a rough hexagonal arrangement to the hats, which is particularly clear in the triangular and parallelogram-shaped structures that are surrounded by chains.

<!-- chunk {"id": "body-0045", "role": "body", "section": "The hat polykite and its tilings", "weight": 1.0} -->

We have found that if we merge each reflected tile with its immediate neighbour as shown in Figure 2.2 (centre), then the tiles in any patch can be put into one-to-one correspondence with a patch of hexagons, as in Figure 2.2 (right). The hexagonal grid may provide a convenient domain in which to perform computations on the combinatorial structure of tilings by hats.

<!-- chunk {"id": "body-0046", "role": "body", "section": "The hat polykite and its tilings", "weight": 1.0} -->

In the course of his explorations, the first author discovered a second polykite that did not seem to have a finite isohedral number or a finite Heesch number, this one a union of ten kites that we call the 'turtle'. The idea of identifying two einsteins back-to-back seemed too good to be true! It was both a relief and a revelation when we determined that not only were the hat and the turtle related, they were in fact two points from a continuum of shapes that all tile the plane the same way. The hat is derived from the grid, and therefore its edges come in two lengths, which we can take to be 1 and √ 3 (where we regard an edge of length 2 as two consecutive edges of length 1 ). Furthermore, these edges come in parallel pairs, allowing us to set the two lengths independently to any non-negative values. We use the notation Tile( a, b ) with a and b not both zero to refer to the shape produced when edge lengths a and b are used in place of 1 and √ 3, respectively. Note that Tile( a, b ) is similar to Tile( ka, kb ) for any k = 0.

<!-- chunk {"id": "body-0047", "role": "body", "section": "The hat polykite and its tilings", "weight": 1.0} -->

Given the colouring in Figure 2.2 showing non-overlapping clusters of reflected tiles and their shells, it is natural to wonder whether the remaining unaffiliated tiles in the patch reliably form clusters of other kinds. Figure 2.4 illustrates that we can account for all remaining tiles using two additional cluster types (shown separately on the right). First, where three shells meet they enclose a single isolated tile, which must be included as a cluster of size one. Then the remaining tiles group into copies of a parallelogram-shaped cluster of size two. These appear in two varieties, depending on the local arrangement of clusters around them. In the first case, coloured white in the drawing, the parallelogram is adjacent to two shells along its long edges. In the second case, coloured grey, one end of the parallelogram is plugged into a local centre of threefold rotation, joining six hats into a three-armed propeller shape called a triskelion. A triskelion is shown in isolation on the bottom right of Figure 2.4.

<!-- chunk {"id": "body-0048", "role": "body", "section": "The hat polykite and its tilings", "weight": 1.0} -->

The H, T, and P metatiles have rotational symmetries. In the bottom row of Figure 2.5, we mark tiles with arrows showing their intended orientations. In each case, the arrow points to the (unique) side of the metatile from which two adjacent kites protrude. The arrows suffice to distinguish symmetric rotations and our construction will not use reflections. (We will not need these arrows in later sections, as metatile orientations will be implied by labels on their edges.)

<!-- chunk {"id": "body-0049", "role": "body", "section": "The hat polykite and its tilings", "weight": 1.0} -->

We can now define a family of supertiles that are analogous to the metatiles, following the procedure illustrated in Figure 2.6. We first assemble the patch of oriented metatiles shown on the left. It can easily be checked that the elided hats borne by these tiles fit together with no gaps and no overlaps. This patch is large enough to pick out one or more copies of each supertile, drawn in red in the central diagram. The supertile shapes are fully determined by two constraints: the red dots coincide with the centres of triskelions, and all interior angles of the hexagonal outlines are 120 ◦. The diagram on the right shows the supercluster outlines in isolation, with their inherited orientation markings. Here, each arrow points to the unique supertile edge that passes through an outward-pointing P tile from the previous generation.

<!-- chunk {"id": "body-0050", "role": "body", "section": "The hat polykite and its tilings", "weight": 1.0} -->

At first glance, these supertiles appear to be scaled-up copies of the metatiles. If that were so, we could perhaps proceed to define a typical substitution tiling, where each scaled-up supertile is associated with a set of rigidly transformed tiles. However, with the obvious exception of the T, none of the supertiles is similar to its corresponding metatile. Despite that discrepancy, the supertiles are fully compatible with the construction in Figure 2.6-they can be arranged in the same configuration shown on the left, and used as a scaffolding for deriving outlines of level2 supertiles (implicitly yielding a much larger patch of hats along the way). Indeed, the construction can be iterated any number of times, with slightly different outlines in every generation. Substitution systems like this one, where successive generations are combinatorially but not geometrically compatible, are uncommon in the world of aperiodic tilings. Here we are forced to work with the properties of a shape discovered in the wild, instead of engineering a tile set to conform to our wishes.

<!-- chunk {"id": "body-0051", "role": "body", "section": "The hat polykite and its tilings", "weight": 1.0} -->

To see this construction in action, please try our interactive browser-based visualization tool at cs.uwaterloo.ca/ ~ csk/hat/.

<!-- chunk {"id": "body-0052", "role": "body", "section": "The hat polykite and its tilings", "weight": 1.0} -->

We know from Figure 2.5 that each of the four metatiles can be associated with a cluster of hats. The construction in Figure 2.6 can then be iterated any number of times to form ever-larger patches of metatiles, and hence of hats. We can, for example, consider the H supertiles formed through this process of iteration, and the patch of hats each one contains. The first few generations of H supertiles are illustrated in Figure 2.7. These patches form a sequence that grows in radius without bound, each patch a subset of its successor. The Extension Theorem [, Section 3.8] allows us to continue this iteration process 'to infinity', yielding the following result.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Aperiodicity via coupling of polyiamond tilings", "weight": 1.0} -->

In Theorem 2.1, we proved that the hat polykite is a monotile: it admits tilings of the plane. Our proof used the metatile substitution system of Section 2, described in detail in Sections 4 and 5.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Aperiodicity via coupling of polyiamond tilings", "weight": 1.0} -->

In this section we give a more direct proof of aperiodicity that exploits the hat's membership in the Tile(a, b) continuum introduced in Section 2. As noted in Section 1.3, a planar tile that In those sections we also use a computer-assisted case analysis to show that every tiling by the hat polykite arises from the substitution rules. For that reason the hat polykite does not admit periodic tilings, completing a proof of Theorem 1.1 using a standard approach going back to Berger.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Clustering of tiles", "weight": 1.0} -->

As discussed in Section 2, tilings by the hat polykite are composed of certain clusters of tiles. These clusters can be used to define simplified tile shapes that we call metatiles. The metatiles inherit matching rules from the boundaries of the hats that they contain. Furthermore, through a set of substitution rules they form larger, combinatorially equivalent supertiles that fit together following the same matching rules. In this section, we give a precise definition of how tiles are assigned to clusters, and a computer-assisted proof by case analysis that this assignment does result in the clusters claimed, fitting together in accordance with the matching rules given.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Clustering of tiles", "weight": 1.0} -->

The boundaries of the four metatiles are divided into labelled segments by marked points. The labels represent matching rules to be obeyed in tilings by the metatiles. To satisfy the matching rules, the four metatiles must form a tiling using copies that are only rotated and not reflected; edge segments marked A + and A -must adjoin on adjacent tiles of the tiling; likewise, edge segments B + and B -, X + and X -, F + and F -, and L and L must adjoin. We will show in Section 5 that any tiling by the metatiles has a substitution structure: the tiles may be grouped (after bisecting some tiles) into supertiles that satisfy combinatorially equivalent matching rules.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Clustering of tiles", "weight": 1.0} -->

This grouping process implies that that no tiling by the metatiles is periodic. Furthermore, the substitution structure allows the metatiles to tile arbitrarily large regions of the plane, and hence the whole plane, implying that they form an aperiodic set.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Clustering of tiles", "weight": 1.0} -->

In this section we establish the following result: Theorem 4.1. Any tiling by the hat polykite can be divided into the clusters shown in Figure 4.1 (or reflections thereof, but not mixing reflected and non-reflected clusters), satisfying the given matching rules, with the resulting tiling by metatiles having the same symmetries as the original tiling by polykites.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Clustering of tiles", "weight": 1.0} -->

Since inspection of the cluster shapes shows that, conversely, any tiling by metatiles induces one by the hat polykite (for example, A + and A -are equal and opposite modifications to the shape of an edge and are consistent wherever they appear in the clusters), the division into clusters suffices as part of showing that the hat polykite is an aperiodic monotile.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Clustering of tiles", "weight": 1.0} -->

Both (a) and (b) may be demonstrated by a case analysis of 2 -patches of hats. Ideally, we would restrict our analysis to precisely those 2 -patches that appear in tilings by the hat. Such an approach is unrealistic, however, as it requires foreknowledge of the space of tilings we are attempting to understand. In practice the list of 2 -patches can include false positives that do not occur in any tilings, as long as our analysis produces valid results for them as well (and as long as the list contains every 2 -patch that can occur in a tiling).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Clustering of tiles", "weight": 1.0} -->

The proof of Theorem 4.1 is computer-assisted. We define rules (Section 4.1) for assigning the labels from Figure 4.1 to tiles in any tiling by the hat polykite. Those rules assign a label to a tile based only on its immediate neighbours. Because no arbitrary choices are involved in the rules, they preserve all symmetries of the tiling. It then remains to show that (a) the labels assigned do induce a division into the clusters shown, and (b) the clusters adjoin other clusters in accordance with the matching rules. Because the matching rules do not permit a reflected cluster to adjoin a non-reflected cluster, it then follows that either no clusters are reflected or all clusters are reflected. Without loss of generality we assume in Section 5 that no clusters are reflected.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Clustering of tiles", "weight": 1.0} -->

For the purposes of our proof we worked with the 188 'surroundable 2 -patches': 2 -patches that can be surrounded at least once more to form a 3 -patch. We generated this set of 188 patches computationally. Specifically, we modified Kaplan's SAT-based software to enumerate all distinct 3 -patches of hats, and extracted the unique 2 -patches in their centres. We validated this list by creating an independent implementation based on brute-force search with backtracking; the source code for this implementation is available with our article. This list certainly includes false positives-a more sophisticated case analysis shows that at most 63 of the 188 surroundable 2 -patches can actually appear in a tiling by hats. However, all 188 of them satisfy the conditions given in this section, allowing us to obtain the results we need with simpler and more transparent algorithms.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Clustering of tiles", "weight": 1.0} -->

It is also possible to demonstrate both (a) and (b) by a shorter case analysis using only 1 -patches. However, an analysis based on 1 -patches is more complicated because the classification rules in Section 4.1 assume that all the neighbours of a tile are known. Those rules can therefore not be applied directly to the outer tiles in a 1 -patch, making it necessary to work with partial information about which labels are consistent with such a tile. For more details of this alternative case analysis, see Appendix B.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Clustering of tiles", "weight": 1.0} -->

For each of the 188 surroundable 2 -patches, the classification rules of Section 4.1 determine labels for the tiles in the patch's interior (comprising the central tile and its neighbours). We may then demonstrate (a) by verifying that when the central tile of a patch has a given label from one of the clusters shown in Figure 4.1, its neighbours in that cluster appear with the correct labels in the expected positions and orientations within the patch. This 'within-cluster' verification process is explained in detail in Section 4.2. Similarly, in Section 4.3 we describe a 'betweencluster' verification process that demonstrates (b). In particular, we show that when a patch's central tile is adjacent to a tile with a label from a different cluster, their adajcency relationship is consistent with the labelled edge segments that define the matching rules for the clusters. The reference software mentioned above performs all of these checks on the 188 surroundable 2 -patches.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Clustering of tiles", "weight": 1.0} -->

An analysis of tilings based on the enumeration of patches depends on the assumption that it is only necessary to consider tilings where all polykites are aligned to the same underlying [3. 4. 6. 4] Laves tiling. This assumption is not in fact obvious for tilings by polykites or other polyforms in general; it is justified in Appendix A.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Classification rules for the hat polykite", "weight": 1.0} -->

These rules do not distinguish between the labels P 1 and F 1: the last rule assigns all such tiles the common label FP 1. The within-cluster and between-cluster checks that follow are all expressed in terms of this composite label. An FP 1 tile can always be relabelled as either P 1 or F 1 later, depending on whether it has a neighbour labelled P 2 or F 2 in the correct position and orientation.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Within-cluster matching checks for the hat polykite", "weight": 1.0} -->

Let L 1 and L 2 be the labels of neighbouring tiles in one of the clusters shown in Figure 4.1. To verify that tiles can be grouped uniquely into copies of these clusters, we must show that when the central tile of a surroundable 2 -patch has the label L 1, it has a neighbour labelled L 2 in the expected position and orientation shown in the cluster. In practice, we do not need to check all such pairs of labels-it suffices to choose a subset of labels that define spanning trees of the neighbour relationships within each cluster. For H, we choose the spanning tree that connects H 1 to its three neighbours.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Between-cluster matching checks for the hat polykite", "weight": 1.0} -->

Let C be one of the four clusters in Figure 4.1, and let E be any of its marked edge segments. We can enumerate all combinations of an edge segment E ′, belonging to a cluster C ′, which are permitted to adjoin E according to the matching rules. If any one tile in C ′ that adjoins E ′ is in the correct position and orientation relative to any one tile in C that adjoins E, it follows as a result of the within-cluster checks that the entire edge segment properly matches between the two clusters. Furthermore, because the matching rules on the boundaries of F 1 and P 1 are identical, it suffices to handle both using the single label FP 1. So for each E we pick one tile in C, and for each choice of E ′, we pick one tile in C ′ that would be a neighbour of the tile picked in C. We then check that, in each surroundable 2 -patch whose central tile has the label of the tile picked in C, there is a neighbour in a position and orientation and with a label that matches one of the possibilities for a tile picked in C ′ for one choice of E ′.

<!-- chunk {"id": "body-0069", "role": "body", "section": "A four-tile substitution system", "weight": 1.0} -->

Consider the four metatiles, with matching rules as in Figure 4.1, which are depicted in this section in the form shown in Figure 5.1. Edges A are red, B are blue, X are green, F are pink, and L are grey. Edges are marked with small geometrical decorations to indicate the signs (outward on the + side, inward on the -side): equilateral triangles for A, semicircles for B, orthogonal line segments for X, short slanted line segments for F. Note that the A and B on H are the opposite signs to those on T, P, and F. Also note that the tiles in this substitution system may not be reflected, only rotated.

<!-- chunk {"id": "body-0070", "role": "body", "section": "A four-tile substitution system", "weight": 1.0} -->

The configuration of two P metatiles shown in Figure 5.3, denoted PP, often appears in the case analysis. The two adjoining copies of P in the same orientation force a contradiction because after adding the two forced H metatiles, nothing fits at the marked point. Subsequently, when identifying forced tiles, as well as considering a tile as forced when it is the only one that would fit in a given place consistent with the matching rules, we also consider a tile as forced when the only alternative consistent with the matching rules would be to place a P tile in a way that yields this PP configuration.

<!-- chunk {"id": "body-0071", "role": "body", "section": "A four-tile substitution system", "weight": 1.0} -->

Sections 5.1 and 5.2 present a branching network of cases in diagrammatic form, building up to patches that can be found in tilings by metatiles. The diagrams should be interpreted as follows. There are some unnumbered tiles that define the case being considered, then some numbered tiles that are forced in the sequence given by their numbers. If it is then necessary to split into multiple next steps, the position at which multiple choices of tile must be considered is marked on the diagram with a filled circle, and there are then separate diagrams for each choice (in which the previous forced tiles are now unnumbered, but newly forced tiles are numbered).

<!-- chunk {"id": "body-0072", "role": "body", "section": "Cases involving T", "weight": 1.0} -->

The two A -edges of T must be adjacent to the A + edge of H, while the B + edge of T may be adjacent to either of the B -edges of H. Thus we have two cases for the configuration around a T tile, which we refer to as T 1 and T 2 (Figure 5.4). As explained in the captions to this and subsequent figures, a sequence of deductions shows that any T in a tiling must occur in case T 1 PF (Figure 5.9).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Cases with H not adjacent to T", "weight": 1.0} -->

Any H not adjacent to a T tile must have a P tile adjacent to its A + edge, while the B -edges may each be adjacent to P or F. This results in four cases, which we call HPP (Figure 5.11), HPF (Figure 5.12), HFP (Figure 5.13), and HFF (Figure 5.14), and we proceed to draw further forced tiles in each of those cases, with consequences explained in the captions to those figures.

<!-- chunk {"id": "body-0074", "role": "body", "section": "The supertiles", "weight": 1.0} -->

We use the following allocation rules to build groupings of metatiles.

<!-- chunk {"id": "body-0075", "role": "body", "section": "The supertiles", "weight": 1.0} -->

- Each T tile is allocated to an H ′ supertile, along with all the H tiles adjacent to that T. - Each H tile in case HPP is allocated to a T ′ supertile.

<!-- chunk {"id": "body-0076", "role": "body", "section": "The supertiles", "weight": 1.0} -->

- Each H tile in case HFP is allocated to a P ′ supertile, along with the H tile in case HPF shown in Figure 5.13. - Each H tile in case HFF is allocated to an F ′ supertile, along with the H tile in case HPF shown in Figure 5.14. - Each H tile in case HPF was allocated to a supertile by exactly one of the previous two rules. - Each half of a P tile, and the upper half of each F tile, is adjacent to exactly one H tile along its A -or B + edge, and is allocated to the same supertile as that H tile. (We simplify Figures 5.17 and 5.18 by eliding the bisection in the central P tile.) - It remains to allocate the lower halves of F tiles. Each such lower half has an X -edge between an L edge and an F + edge; it is allocated to the same supertile as the H tile adjacent to that X -edge. For this allocation rule to be well defined, we need to show that this X -edge is indeed adjacent to a H tile.

<!-- chunk {"id": "body-0077", "role": "body", "section": "The supertiles", "weight": 1.0} -->

The only other possibility not violating the metatile matching rules would be the configuration shown in Figure 5.19. This configuration cannot arise in a tiling by metatiles, because no tile can be adjoined at the marked point.

<!-- chunk {"id": "body-0078", "role": "body", "section": "The supertiles", "weight": 1.0} -->

The X -edge referenced in the last allocation rule cannot be adjacent to any of the exposed X + edges of H tiles in supertiles T ′, P ′ or F ′ without violating the matching rules. Thus all lower halves of F tiles are the ones that appear on the diagrams of the supertiles, and we have shown that the tiling is partitioned into the supertiles.

<!-- chunk {"id": "body-0079", "role": "body", "section": "The supertiles", "weight": 1.0} -->

Next we show that the converse holds: A -2 can only join to A + 2 and B + 2 can only join to B -2. For a contradiction, suppose that the P + and P -edges in some A -2 and B + 2 are joined. If the B + 2 comes from a P ′ supertile, then that P -edge bisects tile 5 in case HFP. Adjacent tiles 5 and 1 in that configuration both have B + edges, which must both be adjacent to H tiles. Those H tiles are adjacent to each other, placing this configuration within an H ′ supertile, which does not have an A -2 edge. The same argument applies in the case of an F ′ supertile, considering tiles 6 and 2 in case HFF. If the P + in an A -2 from P ′ is joined to a B + 2, a similar argument applies (considering tile 2 and an adjacent unnumbered tile in case HFP). So the only remaining case would be if both edges come from supertile T ′, but that possibility is inconsistent with the F tiles forced in case HPP.

<!-- chunk {"id": "body-0080", "role": "body", "section": "The supertiles", "weight": 1.0} -->

To show that the supertiles are fully combinatorially equivalent to the original tiles, one more thing must be checked: that the same combinations of supertiles fit together at vertices as combinations of tiles fit together at vertices. Each supertile has been drawn with a copy of the corresponding tile alongside it, in a corresponding orientation. By inspection, if we take any class of edges of the metatiles, including both sides of the edge (for example, A + and A -), and take any line segment in the corresponding edges of the supertiles, the (directed) angle between the (directed) edges in the tile and in the supertile is consistent across all the diagrams.

<!-- chunk {"id": "body-0081", "role": "body", "section": "The supertiles", "weight": 1.0} -->

Keeping in mind that A + 2, A -2, B + 2, and B -2 must obey the matching rules for the supertiles, note next that the only X + and X -metatile edges on the boundaries of the supertiles that are not part of A + 2, A -2, B + 2 or B -2 are those forming part of F + 2 and F -2. Thus it follows that F + 2 and F -2 must also adjoin each other. The only G + and G -metatile edges still unaccounted for are those that form X -2 and X + 2 edges of the supertiles, meaning that those also match. Finally, the remaining L edges form L 2, which must also match.

<!-- chunk {"id": "body-0082", "role": "body", "section": "The supertiles", "weight": 1.0} -->

This consistency of angles between edges of metatiles and of supertiles means that the angles at vertices of supertiles around a point, each consecutive pair having matching edges, add up to the same amount as the corresponding angles for the corresponding metatiles (an angle at a vertex of a supertile equals the angle at the corresponding vertex of the corresponding metatile, plus the difference between the metatile-supertile angles for the two edges, and those differences cancel when adding up around the point).

<!-- chunk {"id": "body-0083", "role": "body", "section": "The supertiles", "weight": 1.0} -->

Because of the symmetry-preserving correspondence between tilings by metatiles and tilings by hat polykites, we have completed a proof of Theorem 2.1.

<!-- chunk {"id": "body-0084", "role": "body", "section": "The supertiles", "weight": 1.0} -->

The supertiles are therefore combinatorially equivalent to the metatiles, and so the above arguments apply inductively to ensure that the composition of tiles into supertiles may be applied n times for all n. Since the radius of a ball contained in the supertiles goes to infinity with n (a fact that does not depend on the geometry used to bisect P and F metatiles, but that may be easier to show with alternative supertiles that avoid bisection), and the tilings by supertiles have all the symmetries of the original tiling, it follows that the original tiling cannot have a translation as a symmetry. Furthermore, the substitution structure implies that the metatiles tile arbitrarily large finite regions of the plane, and hence the whole plane.

<!-- chunk {"id": "body-0085", "role": "body", "section": "A family of aperiodic monotiles", "weight": 1.0} -->

In the previous sections, we showed that the hat polykite is an aperiodic monotile. This polykite is formed of eight kites from the [3. 4. 6. 4] Laves tiling. Likewise the turtle polykite, formed of ten kites and shown in Figure 6.1, is also aperiodic. We have verified via a computer search that there are no other aperiodic n -kites for n ⩽ 24.

<!-- chunk {"id": "body-0086", "role": "body", "section": "A family of aperiodic monotiles", "weight": 1.0} -->

These two aperiodic polykites are two examples of a family of aperiodic monotiles, all of which have combinatorially equivalent sets of tilings, and which are determined by the choice of two side lengths.

<!-- chunk {"id": "body-0087", "role": "body", "section": "A family of aperiodic monotiles", "weight": 1.0} -->

For nonzero a, the value of r determines the tile up to similarity. In acknowledgment of these similarity classes, we write Tile( r ) as a shorthand for Tile(1, r ). We will show this tile is aperiodic for any positive r = 1. In fact, Tile(1, k √ 3) and Tile( k √ 3, 1) are polykites for all odd positive integers k, implying that this continuum of aperiodic monotiles contains a countably infinite family of aperiodic polykites.

<!-- chunk {"id": "body-0088", "role": "body", "section": "A family of aperiodic monotiles", "weight": 1.0} -->

Let a and b be nonnegative reals, not both zero, and if a = 0 let r = b/a. Define Tile( a, b ) to be the polygon resulting from replacing the sides of length 1 in the hat polykite with sides of length a (we refer to the resulting sides as 1 -sides ) and replacing the sides of length √ 3 in the hat polykite with sides of length b (we refer to the resulting sides as r -sides ). Thus the hat is Tile(1, √ 3) and the turtle is Tile( √ 3, 1). This process results in a closed curve (because the vectors of the 1 -sides add up to 0, as do those of the r -sides) that can easily be shown to be free of self-intersections. It is a 13 -gon (or one with a smaller number of sides if a or b is zero), but considered as a 14 -gon for the purposes of this section. Tile( a, b ) has area √ 3(2 a 2 + √ 3 ab + b 2 ).

<!-- chunk {"id": "body-0089", "role": "body", "section": "A family of aperiodic monotiles", "weight": 1.0} -->

We now prove the following result: Theorem 6.1. Suppose r = 1 and r ′ = 1 are positive. Then there is a bijection between combinatorially equivalent tilings for Tile(r) and Tile(r ′), given by changing the lengths of all r -sides from r to r ′, while preserving angles, orientations, and adjacencies to maximal line segments.

<!-- chunk {"id": "body-0090", "role": "body", "section": "A family of aperiodic monotiles", "weight": 1.0} -->

Suppose first that r is irrational. If a maximal line segment in the union of the boundaries of the tiles has p 1 -sides and q r -sides on one side of the line segment, it also has p 1 -sides and q r -sides on the other side of the line segment. Because a maximal line segment has at most two sides of tiles on each side of the segment, the same argument also applies for any rational r except possibly 1 2, 1, and 2.

<!-- chunk {"id": "body-0091", "role": "body", "section": "A family of aperiodic monotiles", "weight": 1.0} -->

Similarly, in the case r = 1 2, the only additional possibility is that two r -sides align with one 1 -side. The outer corners of the two r -sides have angles 120 ◦ or 240 ◦, one corner of every 1 -side has angle 90 ◦, 180 ◦ or 270 ◦, and those cannot appear at the same vertex.

<!-- chunk {"id": "body-0092", "role": "body", "section": "A family of aperiodic monotiles", "weight": 1.0} -->

If r = 2, there is the additional possibility that two 1 -sides align with one r -side. When there are two consecutive 1 -sides on one side of a line, with 90 ◦ corners of the two tiles between those two sides (or the 180 ◦ corner of a single tile), the other ends of those sides have corners with angles 120 ◦ or 240 ◦. But for every r -side, one corner has angle 90 ◦ or 270 ◦, and the angles of the tile do not permit 120 ◦ or 240 ◦ at the same vertex of a tiling as 90 ◦ or 270 ◦.

<!-- chunk {"id": "body-0093", "role": "body", "section": "A family of aperiodic monotiles", "weight": 1.0} -->

(This argument relies on the fact that the plane is simply connected. A tiling by Tile(r) of a region with a hole that cannot be filled with tiles might not convert to a tiling by Tile(r ′) of a region with a combinatorially equivalent hole. Indeed, for some vectors defining the sides of the hole, there might not exist any combinatorially equivalent hole if the vectors of the 1 -sides among the sides of the hole do not add up to 0.) √ Thus for any positive r = 1, we have shown that if a maximal line segment in the union of the boundaries of the tiles has p 1 -sides and q r -sides on one side of the line segment, it also has p 1 -sides and q r -sides on the other side of the line segment. We can now construct the required bijection. Because side vectors around any tile add up to zero, and the sides of tiles on both sides of a maximal line segment add up to the same length, the specified process converts a tiling by Tile(r) into one by Tile(r ′) that is combinatorially equivalent [, Lemma 1.1].

<!-- chunk {"id": "body-0094", "role": "body", "section": "A family of aperiodic monotiles", "weight": 1.0} -->

As shown in Lemma A.6, all tilings by Tile are aligned to an underlying [3. 4. 6. 4] Laves tiling, so in fact each maximal line segment is made up only of 1 -sides or only of r -sides.

<!-- chunk {"id": "body-0095", "role": "body", "section": "A family of aperiodic monotiles", "weight": 1.0} -->

Finally, Tile -or more generally Tile(a, a) -is not aperiodic, as shown by the periodic tiling in Figure 6.2. The polyiamonds Tile(a, 0) and Tile(0, b) are also not aperiodic. A tiling by Tile(r) for positive r = 1 can still be mapped to a corresponding tiling by Tile(a, a), Tile(a, 0), or Tile(0, b) following the process described above, but the map is not a bijection.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Wehave exhibited an einstein, the first topological disk that tiles aperiodically with no additional constraints or matching rules. The hat polykite is in fact a member of a continuous family of aperiodic monotiles that admit combinatorially equivalent tilings. The hat forces tilings with hierarchical structure, as is the case for many aperiodic sets of tiles in the plane, but a new method introduced in Section 3 also suffices to show the lack of periodic tilings without needing that hierarchical structure, beyond demonstrating the existence of a tiling.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The hat is a 13 -sided non-convex polygon. A convex polygon cannot be an aperiodic monotile, and all non-convex quadrilaterals can easily be seen to tile periodically. Therefore, in terms of number of sides, the 'simplest' aperiodic n -gon must have 5 ⩽ n ⩽ 13. Subsequent research could chip away at this range, by finding aperiodic n -gons for n < 13 or ruling them out for n ⩾ 5.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our substitution system satisfies the relatively mild conditions needed to guarantee an uncountable infinity of combinatorially distinct tilings, all of which are hierarchical [, Section 7.6.2]. But not every tiling by hats is necessarily produced purely through substitution. As with Robinson's aperiodic set of six shapes, it is conceivable that hats could tile infinite sectors of the plane, which could then be combined into tilings with infinite 'fault lines' that lie on the boundaries of supertiles at all levels. Future work should examine the possibility of tilings with fault lines, as part of characterizing the full space of hat tilings. In particular, it should be determined whether every finite patch that appears in some hat tiling must appear infinitely often in all hat tilings, or whether there are patches that only appear on fault lines and not in the interior of a supertile.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Tilings by the hat necessarily include both reflected and unreflected tiles. We might therefore ask whether there exists an aperiodic monotile for which reflections are not needed, either because the tile has bilateral symmetry or because it covers the plane using only translations and rotations. 5 Finding such a monotile pushes the boundaries of complexity known to be achievable by the tiling behaviour of a single closed topological disk. It does not, however, settle various other unresolved questions about that complexity. For example, all of the following questions remain open.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Conclusion", "weight": 1.5} -->

- Are Heesch numbers unbounded? That is, does there exist, for every positive integer n, a topological disk that does not tile the plane and has Heesch number at least n ? We conjecture that there is no bound on Heesch numbers. - Are isohedral numbers unbounded? That is, does there exist, for every positive integer n, a topological disk that tiles the plane periodically but only admits tilings with at least n 5 In subsequent work, we show that Tile is such a tile if its boundary is modified to prevent the use of reflections. transitivity classes? Again, we conjecture that no bound exists. If the requirement of periodicity is omitted here, then the hat polykite requires infinitely many transitivity classes in any tiling. Socolar showed that if the tile is not required to be a closed topological disk, then tiles exist with every positive isohedral number.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Conclusion", "weight": 1.5} -->

- Is it computationally undecidable whether a polygon (or indeed a more general single tile in the plane) admits a tiling? It would again be reasonable to conjecture yes, which would also imply unbounded Heesch numbers. Greenfeld and Tao demonstrated undecidability in a more general context. For sets of tiles in the plane, Ollinger proved undecidability for sets of five polyominoes. - Is it computationally undecidable whether a polygon (or indeed a more general single tile in the plane) admits a periodic tiling? It would again be reasonable to conjecture yes. Such an answer would imply unbounded isohedral numbers.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Although we have provided a description of tilings by the hat polykite and related tiles described here (all such tilings are given by the substitution system of Section 5, as applied to the clusters of tiles from Section 4, subject to the possibility mentioned above of tilings with fault lines, where each sector is produced by the substitution system), there are various informal observations in Section 2 that have not been fully explored or given precise statements. Those observations could provide starting points for possible future investigation of the tiles described here and their tilings, the metatiles used in classifying tilings by the hat polykite, and other related substitution tilings. It is not clear which ideas from this work will be most promising for future work, so we have generally erred on the side of including observations that might be of use, rather than making the paper focus more narrowly on a single proof of a single main result.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Webelieve that the approach presented in Section 3, of coupling two separate tilings to show that a third tiling cannot be periodic, is a new way to prove that a set of tiles is aperiodic. It would be worth investigating whether it can be applied in other contexts. In particular, polykites (and more generally poly[4. 6. 12] -tiles, a subset of the shapes known as polydrafters ) may be unusually well-suited to this method of proof, because their edges lie on lines belonging to two regular triangle tilings. It might also be applicable to some poly[4. 8. 8] -tiles (a subset of the polyaboloes ). 6 This style of proof might help explain how small polykites proved to be aperiodic when polyominoes, polyiamonds and polyhexes up to high orders yielded no einsteins. However, as noted in Section 6, searches of polykites have not found other aperiodic examples outside the family described in this paper.
