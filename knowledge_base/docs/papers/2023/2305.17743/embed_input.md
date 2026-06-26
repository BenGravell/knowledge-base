<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Chiral Aperiodic Monotile

Topics include Chiral aperiodic monotile.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The recently discovered "hat" aperiodic monotile mixes unreflected and reflected tiles in every tiling it admits, leaving open the question of whether a single shape can tile aperiodically using translations and rotations alone. We show that a close relative of the hat - the equilateral member of the continuum to which it belongs - is a weakly chiral aperiodic monotile: it admits only non-periodic tilings if we forbid reflections by fiat. Furthermore, by modifying this polygon's edges we obtain a family of shapes called Spectres that are strictly chiral aperiodic monotiles: they admit only chiral non-periodic tilings based on a hierarchical substitution system.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The recently discovered "hat" aperiodic monotile admits tilings of the plane, but none that are periodic. This polygon settles the question of whether a single shape---a closed topological disk in the plane---can tile aperiodically without any additional matching conditions or other constraints on tile placement.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The hat is asymmetric: it is not equal to its image under any non-trivial isometry of the plane. In particular, a hat cannot be brought into perfect correspondence with its own mirror reflections. Moreover all tilings formed by copies of the hat must use both unreflected and reflected tiles. Some people have wondered whether the hat and its reflection ought to be considered two distinct shapes, thereby invalidating its status as a monotile. To some extent, this question is about tiles as physical objects rather than mathematical abstractions. A hat cut from paper or plastic can easily be turned over in three dimensions to obtain its reflection, but a glazed ceramic tile cannot. More broadly, a wide range of three-dimensional objects, from organic molecules to shoes, behave very differently in their left- and right-handed forms.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since Felix Klein introduced the Erlangen program, each metric geometry has been defined by first choosing a set of isometries, the rigid motions of the geometric space in which we are working. Isometries may be classified as *orientation-preserving*, which map left-handed shapes to left-handed shapes (and right-handed to right-handed), or *orientation-reversing*, which exchange left- and right-handedness. In the plane, the orientation-preserving isometries comprise translations and rotations. We will refer to all orientation-reversing isometries generically as "reflections", and the image of a shape under a reflection as a "reflected" copy of that shape.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

From that point of view, the question of whether a single tile admits monohedral tilings of the plane depends upon the set of isometries that may be used to transform tiles. If this set is not specified, one may reasonably assume that the full set of planar isometries is intended. Grünbaum and Shephard explicitly permit reflections in their definition of monohedral tilings \[, Section 1.2\], so that when they later ask for a tile that "only admits monohedral non-periodic tilings" \[, Section 10.7\], we can be confident that they considered reflected tiles to be in play. Ammann's aperiodic pairs of tiles were considered congruent under reflections, and the disconnected aperiodic Taylor-Socolar tile also requires reflections to tile the plane. Likewise, we regard the hat as an aperiodic monotile. Still, the aperiodicity of the hat leaves open the question of whether there might exist a monotile that achieves aperiodicity without the use of reflections.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A *tile* $T$ is a closed topological disk in the plane, and a *monohedral* *tiling* admitted by it is a countable collection $\mathcal{T} = \left\{ T_{1},T_{2},\ldots \right\}$ of congruent copies of $T$ with disjoint interiors, whose union is the entire plane. Each $T_{i}$ is of the form $g_{i}T$ for some planar isometry $g_{i}$. We say that a monohedral tiling $\mathcal{T}$ is a *chiral tiling* if for every pair ${T_{i},T_{j}} \in \mathcal{T}$, there is an orientation-preserving isometry mapping $T_{i}$ to $T_{j}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We then define a *weakly chiral aperiodic monotile* to be a tile whose chiral tilings are all non-periodic (and that admits at least one such tiling), and a *strictly chiral aperiodic monotile* to be a tile that admits *only* chiral non-periodic tilings. Following Klein, the weak case is aperiodic if we decree reflections to be off limits, even if the tile admits periodic tilings when reflections are allowed. The strict case remains both chiral and aperiodic in the presence of reflections. With these definitions in hand, we ask: *Do there exist any weakly or strictly chiral aperiodic monotiles?*^11^1We might call this the "vampire einstein" problem, as we are seeking a shape that is not accompanied by its reflection.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The discovery of the hat is an effective reminder of how little we understand about the possibilities and subtleties of monohedral tilings. Certainly there is no evidence to suggest that the hat (and the continuum of shapes to which it belongs) is somehow unique, and we might therefore hope that a zoo of interesting new monotiles will emerge in its wake. In this context, a chiral aperiodic monotile does not seem particularly unlikely. Nonetheless, we did not expect to find one so close at hand: a solution follows in short order from the hat.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Smith et al. discuss the discovery of two separate aperiodic polykites---the hat, and a $10$-kite known as the "turtle"---and then show that these two shapes are members of a continuum parameterized by choices of two non-negative edge lengths $a$ and $b$. Each member of that continuum is a $14$-sided polygon (with two collinear sides) denoted ${Tile}(a,b)$; the hat is ${Tile}\left( 1,\sqrt{3} \right)$ and the turtle is ${Tile}\left( \sqrt{3},1 \right)$. All members of this continuum are aperiodic monotiles, with three exceptions: ${Tile}$ (the "chevron"), ${Tile}$ (the "comet"), and the equilateral polygon ${Tile}$ (Figure 1.1, left).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Because ${Tile}$ is equilateral, copies of the tile may fit together in more ways than generic members of the continuum, and in fact it admits a simple periodic tiling using equal numbers of left- and right-handed tiles \[, Figure 6.2\]. But what happens if we rein in that freedom slightly? In this paper we prove that ${Tile}$ is a weakly chiral aperiodic monotile: if by fiat we restrict ourselves to tilings using only translations and rotations, then ${Tile}$ admits only non-periodic tilings. More importantly, by modifying the edges of this polygon (Figure 1.1, centre and right), we define a family of strictly chiral aperiodic monotiles that we call "Spectres", which admit only tilings of a single handedness, even when reflections are permitted (Theorem 2.2). Figure 1.2 shows non-periodic tilings by ${Tile}$ (left) and a Spectre (right).

<!-- chunk {"id": "body-0012", "role": "body", "section": "The Spectre and its tilings", "weight": 1.0} -->

Our main results concern Spectres, the set of shapes whose tilings correspond exactly to the *chiral* tilings admitted by ${Tile}$, thereby boosting us from weakly chiral to strictly chiral aperiodicity. It is helpful to begin by giving a precise definition of this set.

<!-- chunk {"id": "body-0013", "role": "body", "section": "The Spectre and its tilings", "weight": 1.0} -->

We regard ${Tile}$ as an equilateral polygon with $14$ unit-length edges and $14$ vertices, where one of those vertices lies between two collinear edges.

<!-- chunk {"id": "body-0014", "role": "body", "section": "The Spectre and its tilings", "weight": 1.0} -->

A tile $X$ is a *Spectre* if and only if $X$ admits only chiral tilings; Every tiling admitted by $X$ corresponds to one by ${Tile}$: if $\left\{ {g_{i}X} \right\}$ is a tiling for a set of isometries $\left\{ g_{i} \right\}$, then $\left\{ {g_{i}{Tile}} \right\}$ is also a tiling; Every chiral tiling admitted by ${Tile}$ corresponds to one by $X$: if $\left\{ {g_{i}{Tile}} \right\}$ is a chiral tiling, then $\left\{ {g_{i}X} \right\}$ is also a tiling; and If $\left\{ {g_{i}X} \right\}$ is a tiling, then that tiling and $\left\{ {g_{i}{Tile}} \right\}$ have the same tiling vertices (points shared by three or more

<!-- chunk {"id": "body-0015", "role": "body", "section": "The Spectre and its tilings", "weight": 1.0} -->

We do not attempt to characterize the space of all Spectres, but we can assert that the space is non-empty.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Main result", "weight": 1.0} -->

When a substitution tiling is aperiodic, the proof of aperiodicity usually relies in some way on showing that the tiles are nested within an infinite hierarchical superstructure in every tiling they admit. We say that a set of tiles is *hierarchical* if, in every tiling admitted by those tiles, every tile is nested within an infinite hierarchy of ever-larger supertiles. If these hierarchies are uniquely determined, then the tilings that contain them must be non-periodic. This approach to aperiodicity informs our main result.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Combinatorial equivalence of tilings", "weight": 1.0} -->

At many points in this paper, we deduce information about a tiling by noting its combinatorial equivalence to some other tiling. Before proceeding we consider the notion of combinatorial equivalence in detail. Two patches, or two tilings, are *combinatorially equivalent* if and only if they are homeomorphic as topological complexes. Two sets of tiles are *combinatorially equivalent* if each tiling admitted by one is combinatorially equivalent to a tiling admitted by the other.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Combinatorial equivalence of tilings", "weight": 1.0} -->

The following lemma gives a test for establishing combinatorial equivalence. An *edge patch* is a collection of tiles with disjoint interiors, such that there exists a closed arc $e$ that is a connected component of the intersection of two of the tiles, all the other tiles contain an endpoint of $e$, and $e$ lies in the interior of the union of the tiles. A *vertex* of an edge patch is a point in the interior of the union of the tiles that is shared by at least three tiles of the patch.

<!-- chunk {"id": "body-0019", "role": "body", "section": "From Spectres to hats and turtles", "weight": 1.0} -->

In the work of Smith et al., computational analysis of the hat was simplified by the fact that it a polyform, specifically a union of eight kites from the Laves tiling $\lbrack 3.4.6.4\rbrack$. Furthermore, the tiles in every tiling by hats must be aligned with the kites of the Laves tiling \[, Lemma A.6\]. Consequently, patches of hats can be manipulated discretely by associating information with the cells of the underlying kite grid. The aperiodic $10$-kite known as the turtle is also compatible with grid-based computations. ${Tile}$ is not a polyform, which at the outset appears to rule out such an approach. However, we can regain the ability to perform discrete computations by exploiting a connection between tilings by ${Tile}$ and tilings by combinations of hats and turtles. We prove the following result.

<!-- chunk {"id": "body-0020", "role": "body", "section": "From hats and turtles to marked hexagons", "weight": 1.0} -->

We have not yet shown that the Spectre admits any tilings of the plane. However, we can still prove that any such tilings, if they exist, must be non-periodic. This section and the one that follows furnish such a proof. As a by-product we also obtain a substitution system that can produce patches of Spectres of any size.

<!-- chunk {"id": "body-0021", "role": "body", "section": "From hats and turtles to marked hexagons", "weight": 1.0} -->

Any tiling by Spectres is combinatorially equivalent to a chiral tiling by ${Tile}$. In turn, that tiling is equivalent to a chiral tiling by hats and turtles (i.e., all tiles are unreflected, or all tiles are reflected). These equivalences extend to any translational symmetries of the tilings, meaning that the Spectre tiling is periodic if and only if the hat-turtle tiling is. As with the analysis of hat tilings \[, Section 4\], we show here that in any chiral tiling by hats and turtles, we can group tiles into non-overlapping clusters. The resulting tiling by the clusters satisfies certain matching conditions and has the same symmetries as the original tiling by hats and turtles. We arrive at the following result.

<!-- chunk {"id": "body-0022", "role": "body", "section": "A substitution system for marked hexagons", "weight": 1.0} -->

In this section, we prove that any tiling admitted by the marked hexagons of Figure 4.2 can be uniquely composed into the supertiles of Figure 5.1. This composition yields a unique hierarchy of level-$n$ supertiles for all $n$, which forces any tiling by these hexagons to be non-periodic. We also observe that the supertiles imply a substitution system that produces patches of hexagons of any size, thus confirming that the hexagons tile the plane.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Many problems in tiling theory depend implicitly or explicitly on an initial decision of when to consider two tiles in a tiling "the same". In the Euclidean plane, if this decision is not otherwise articulated then we assume two tiles are the same if they can be brought into coincidence through any planar isometry. In this paper we first answer the einstein problem in a world where sameness is restricted to orientation-preserving isometries. The polygon ${Tile}$ is a *weakly chiral aperiodic monotile*: a shape that tiles aperiodically if only translations and rotations are permitted. Then, by modifying the edges of that polygon, we obtain a class of shapes called Spectres, which are *strictly chiral aperiodic monotiles*: they tile aperiodically using tiles of a single handedness, even when reflections are allowed.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Other variations of the einstein problem can be posed in which tiles are restricted to images under any given group of isometries. Each such problem comes in weak and strict forms, as above. In the weak case, we ask whether a shape's tilings are non-periodic if tilings are restricted by fiat to the given isometries, even if it would tile periodically when all isometries are allowed. In the strict case we require that by design, a shape does not admit any tilings that use isometries outside the group.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Conclusion", "weight": 1.5} -->

If we restrict our attention to translations alone, then the work of Girault-Beauquier and Nivat and Kenyon shows that a topological disk with a tiling by translation cannot be an aperiodic monotile. However, Greenfeld and Tao and Greenfeld and Kolountzakis showed that translational aperiodic monotiles do exist in sufficiently high dimensions. The next simplest case is where $180^{\circ}$ rotations are allowed along with translations. Schattschneider \[, Problem 18.E1\] posed the question of whether any tile admitting such a tiling of the plane also satisfies the Conway criterion, implying that it must be isohedral.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our work presents a single family of strictly chiral aperiodic monotiles, which are all essentially the same up to trivial modifications of tiling edges. It would be interesting to search for other weakly chiral or strictly chiral einsteins. It would be particularly worthwhile to find (or disprove the existence of) an aperiodic monotile with bilateral reflection symmetry, a shape for which chirality becomes moot.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We showed in Lemma 2.1 that we can replace the $14$ edges of ${Tile}$ by suitably oriented copies of any smooth curve to construct a Spectre, provided the replacement results in a tile with a non-self-intersecting boundary. In fact, the construction works generally for $C^{1}$ curves, which suffice to force the vertices of the original polygon to meet each other in tilings. However, we leave open the question of whether some other curves (e.g., piecewise-linear paths) might permit different tilings, or whether all choices of curve produce valid Spectres.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Conclusion", "weight": 1.5} -->

As part of our proof of aperiodicity, we derived the chiral marked hexagons of Figure 4.2. These hexagons are meant to encode the combinatorics of clusters of Spectres, but they display interesting properties of their own that may be worthy of further study. Figure 5.2 hints at emergent patterns in tilings by marked hexagons.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Some of the hexagons of Figure 4.2 have very similar arrangements of markings; removing the distinctions between some of the edge labels can produce a smaller set of marked hexagons without reducing the set to a single trivially marked tile. In particular, combining $\Theta$, $\Xi$, $\Phi$ and $\Psi$ into a single marked hexagon, and combining $\Lambda$ and $\Pi$ into another marked hexagon, yields a smaller set of five marked hexagons, which preliminary computations suggest might also be aperiodic. It would be of interest to understand what small aperiodic sets of chiral marked hexagons are possible with this style of edge markings, similar to the work of Jeandel and Rao on small aperiodic sets of Wang tiles.
