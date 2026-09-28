<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Mathematical Table Turning Revisited

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We investigate under which conditions a rectangular table can be placed with all four feet touching a continuous ground by turning it on the spot.

<!-- chunk {"id": "body-0003", "role": "body", "section": "%&\\$#!!!", "weight": 1.0} -->

You sit down at a table and notice that it is wobbling, because it is standing on a surface that is not quite even. What to do? Curse, yes, of course. Apart from that, it seems that the only quick fix to this problem is to wedge something under one of the feet of the table to stabilise it. However, there is another simple approach to solving this annoying problem. Just turn the table on the spot! More often than not, you will find a position in which all four legs of the table are touching the ground. This may seem somewhat counterintuitive. So, why and under what conditions does this trick work?

<!-- chunk {"id": "body-0004", "role": "body", "section": "Balancing Mathematical Tables---a Matter of Existence", "weight": 1.0} -->

In the mathematical analysis of the problem, we will first assume that the ground is the graph of a function $g:\mathbb{R}^{2}\to\mathbb{R}$, and that a mathematical table consists of the four vertices of a rectangle of diameter 2 whose center is on the $z$-axis. What we are then interested in is determining for which choices of the function $g$ can a mathematical table be balanced locally: that is, when can a table be moved such that its center remains on the $z$-axis, and all its vertices end up on the ground.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Balancing Mathematical Tables---a Matter of Existence", "weight": 1.0} -->

We first observe that it is not always possible to balance a mathematical table locally. Consider, for example, the reflectively symmetric function of the angle $\theta$ about the $z$-axis with Figure 1: On this discontinuous ground a square mathematical table cannot be balanced locally.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Balancing Mathematical Tables---a Matter of Existence", "weight": 1.0} -->

So, the ground consists of four quadrants, two at height 1 and two at height 2; see Figure 1. It is not hard to see that a square mathematical table cannot be balanced locally on such a clifflike piece of ground.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Balancing Real Tables...by Turning the Tables", "weight": 1.0} -->

So, one of our highly idealized tables can be balanced locally on any continuous ground. However, being an existence result, Theorem 1 is less applicable to our real-life balancing act than it appears at first glance. Here are two problems that seem worth pondering: Mathematical vs. Real Tables. A real table consists of four legs and a table top; our theorem only tells us that we can balance the four endpoints of the legs of this real table. However, balancing the whole real table in this position may be physically impossible, since the table top or other parts of the legs may run into the ground.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Balancing Real Tables...by Turning the Tables", "weight": 1.0} -->

To deal with this complication, we define a real table to consist of a solid rectangle with diameters of length 2 as top, and four line segments of equal length as legs. These legs are attached to the top at right angles, as shown in Figure 2. The end points of the legs of a real table form its associated mathematical table. We say that a real table is balanced locally if its associated mathematical table is balanced locally, and if no point of the real table is below the ground.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Balancing Real Tables...by Turning the Tables", "weight": 1.0} -->

Balancing by Turning. A second problem with our analysis so far is that Theorem 1, while guaranteeing a balancing position, provides no practical method for finding it. After all, although we restrict the center of the table to the $z$-axis, there are still four degrees of freedom to play with when we are actually trying to find a balancing position.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Balancing Real Tables...by Turning the Tables", "weight": 1.0} -->

The following rough argument indicates how, by turning a table on the spot in a certain way, we should be able to locate a balancing position, as long as we are dealing with a square table and a ground that is not "too crazy".

<!-- chunk {"id": "body-0011", "role": "body", "section": "Balancing Real Tables...by Turning the Tables", "weight": 1.0} -->

Balancing a Square Table by Turning--the Intermediate Value Theorem in Action\Consider a wobbling square table. We wobble the table until two opposite vertices of the associated mathematical table are on the ground, and the other two vertices are the same vertical distance above the ground; see the left diagram in Figure 2. Let's call this position of the table its initial position. By pushing down on the table, we can make the hovering vertices touch the ground and, in doing so, we have shoved the "touching" vertices that same vertical distance into the ground. We call this new position of the table its end position; see the right diagram in Figure 2. Starting in the initial position, we now rotate the table around the $z$-axis; in doing so, we ensure that at all times the center of the mathematical table is on the $z$-axis, that the same pair of vertices as in the initial position are touching the ground, and that the other two vertices are an equal vertical distance from the ground. Eventually, we will arrive at the end position. So, we started out with two vertices hovering above the ground, and we finished with the same vertices shoved below the ground.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Balancing Real Tables...by Turning the Tables", "weight": 1.0} -->

Furthermore, the vertical distance of the hovering vertices depends continuously on the rotation angle. Hence, by the Intermediate Value Theorem, somewhere during the rotation these vertices are also touching the ground: that is, the table has been balanced locally.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Balancing Real Tables...by Turning the Tables", "weight": 1.0} -->

Unlike most other real-world applications of the Intermediate Value Theorem, it seems that this neat argument is not as well-known as it deserves. We have not been able to pinpoint its origin, but from personal experience we know that the argument has been around for at least thirty five years and that people keep rediscovering it. In terms of proper references in which variations of the argument explicitly appear, we are only aware of (Chapter 6, Problem 6) and; the earliest reference in this list is Martin Gardner's Mathematical Games column in the May 1973 issue of Scientific American. Note that an essential ingredient of the argument is the simple fact that a quarter-turn around its centre takes a square into itself---to move the table from the initial position to the end position takes roughly a quarter-turn around the $z$-axis. Closely related well-documented quarter-turn arguments date back almost a century; see, for example, Emch's proof that any oval contains the vertices of a square in or, Section 4. At any rate, we definitely do not claim to have invented this argument.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Balancing Real Tables...by Turning the Tables", "weight": 1.0} -->

At first glance, the above argument appears reasonable and, if true, would provide a foolproof method for balancing a square table locally by turning. However, for arbitrary continuous ground functions, it appears just about impossible to turn this intuitive argument into a rigorous proof. In particular, it seems very difficult to suitably model the rotating action, so that the vertical distance of the hovering vertices depends continuously upon the rotation angle, and such that we can always be sure to finish in the end position.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Balancing Real Tables...by Turning the Tables", "weight": 1.0} -->

As a second problem, it is easy to construct continuous grounds on which real tables cannot be balanced locally. For example, consider a real square table with short legs, together with a wedge-shaped ground made up of two steep half-planes meeting in a ridge along the $x$-axis. Then it is clear that the solid table top hitting the ground will prevent the table from being balanced locally on this ridge.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Balancing Real Tables...by Turning the Tables", "weight": 1.0} -->

By restricting ourselves to grounds that are not too wild, we can prove that balancing locally by turning really works.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Horizontal balancing", "weight": 1.0} -->

When we balance a table locally, the table will usually not end up horizontal, and a beer mug placed on the table may still be in danger of sliding off. It would be great if we could arrange it so that the table is not only balanced but also horizontal, maybe by moving the center of the table off the $z$-axis and balancing it somewhere else on the ground. Just imagine the ground to be a tilted plane, and you can see that this will not be possible in general. However, Fenn proved the following result: If a continuous ground coincides with the $xy$-plane outside a compact convex disc and if the ground never dips below the $xy$-plane inside the disk, then a given square table can be balanced horizontally such that the center of the table lies above the disk. Let's call the special kind of ground described here a Fenn ground and the part of this ground inside the distinguished compact disk its hill.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Horizontal balancing", "weight": 1.0} -->

The problem of horizontally balancing tables consisting of plane shapes other than squares on Fenn grounds has also been considered. Here 'horizontal balancing on a Fenn ground' means that in the balancing position some interior points of the shape are situated above the hill. It has been shown by Zaks that a triangular table can be balanced on any Fenn ground. In fact, he showed that if we start out with a horizontal triangle somewhere in space and mark a point inside the triangle, then we can balance this triangle on any Fenn ground, with the marked point above the hill, by just translating the triangle. Fenn also showed that tables with four legs that are not concircular and those forming regular polygons with more than four legs cannot always be balanced horizontally on Fenn grounds. Zaks mentions an unpublished proof by L.M. Sonneborn that any polygon table with more than four legs cannot always be balanced horizontally on Fenn grounds. It is not known whether any concircular quadrilateral tables other than squares can always be balanced horizontally on Fenn grounds. See and for further results relating to this line of research.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Local Balancing of Exotic Mathematical Tables", "weight": 1.0} -->

Taking things to different mathematical extreme, we can consider a table consisting of $n\geq 3$ leg points in 3-space together with an additional center point. We then ask whether, given any continuous ground, it is possible to always balance this table locally, that is, move this configuration of $n+1$ points into a position in which the $n$ leg points are on the ground, and the center is on the $z$-axis.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Local Balancing of Exotic Mathematical Tables", "weight": 1.0} -->

The example of a plane ground shows that the leg points of an always locally balancing table have to be coplanar. Let's consider the example of a ground that contains part of a sphere that is large enough to ensure that all legs of our table end up on this part of the sphere whenever the table is locally balanced on this ground. Then intersecting this sphere with the plane that the leg points are contained in gives a circle that all leg points are contained. Hence the leg points of the table are concircular. Now, let's consider a ground that includes part of an ellipsoid which does not contain a copy of the circumcircle of the leg points of the table; moreover, we choose the ellipsoid large enough so that all leg points of our table end up on the ellipsoid whenever the table is locally balanced on this ground. Then intersecting the ellipsoid with the plane containing the leg points gives an ellipse that is different from the circumcircle of the leg points. However, this is impossible if the table contains more than four leg points because five points on an ellipse determine this ellipse uniquely.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Local Balancing of Exotic Mathematical Tables", "weight": 1.0} -->

We conclude that an always locally balancing table must have three or four leg points and that these points are concircular. Note that requiring concircularity in the case of three points is not superfluous since we need to exclude the case of three collinear points.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Local Balancing of Exotic Mathematical Tables", "weight": 1.0} -->

Livesay's theorem, which made the proof of Theorem 1 so easy, has a counterpart for triangles, due to Floyd.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Balance Everywhere", "weight": 1.0} -->

Imagine a square table with diameter of length 2 suspended horizontally high above some ground, with its center on the $z$-axis. Rotate it a certain angle about the $z$-axis, release it, and let it drop to the ground. It is easy to identify continuous grounds such that all four leg of the table will hit the ground simultaneously, no matter what release angle you choose. Of course, any horizontal plane will do, and so will any ground that contains a vertical translate of the unit circle. We leave it as an exercise for the reader to construct a ground that is not of this type but admits horizontal balancing for any angle. Also, the reader may wish to convince themselves that the following is true: we are dealing with a ground as in Theorem 2. If the center of the table has the same $z$-coordinate in all its equal hovering positions (positions in which $A$ and $C$ touch the ground and $B$ and $D$ are at equal vertical distance from the ground), then in fact the table is balanced in all these positions.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Short Legs and Tiled Floors", "weight": 1.0} -->

Note that if you shorten one of the legs of a real-life square table, this table will wobble if you set it down on the plane, and no turning or tilting will fix this problem. In real life rectangular tables the ends of whose legs do not form a perfect rectangle are not uncommon and, as our simple example shows, those uneven legs may conspire to make our anti-wobble tactics fail.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Short Legs and Tiled Floors", "weight": 1.0} -->

Considering our example of a discontinuous ground at the beginning of this article, it should be clear that a wobbling table on a tiled floor may also defy our table turning efforts.

<!-- chunk {"id": "body-0026", "role": "body", "section": "How to Turn Tables in Practice", "weight": 1.0} -->

In practice, it does not seem to matter how exactly you turn your table on the spot, as long as you turn roughly around the center of the table. Notice that you needn't actually establish the equal hovering: as you rotate towards the correct balancing position, there will be less and less wobble-room until, at the correct rotation, the balancing position is forced. With a square table, you can even go for a little bit of a journey, sliding the table around in your (continuous) backyard. As long as you aim to get back to your starting position, incorporating a quarter turn in your overall movement, you can expect to find a balancing position.
