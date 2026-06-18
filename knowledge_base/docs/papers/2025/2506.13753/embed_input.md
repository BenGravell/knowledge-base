Edge Nearest Neighbor: Neighbor-Finding Revisited in Sampling-Based Motion Planning

Neighborhood finders and nearest neighbor queries are fundamental parts of sampling based motion planning algorithms. Using different distance metrics or otherwise changing the definition of a neighborhood produces different algorithms with unique empiric and theoretical properties. LaValle suggests a neighborhood finder for the Rapidly-exploring Random Tree RRT algorithm which finds the nearest neighbor of the sampled point on the swath of the tree, that is on the set of all of the points on the tree edges, using a hierarchical data structure. In this paper we implement such a neighborhood finder and show, theoretically and experimentally, that this results in more efficient algorithms, and suggest a variant of the Rapidly-exploring Random Graph RRG algorithm that better exploits the exploration properties of the newly described subroutine for finding narrow passages.

## Introduction

In the motion planning problem we are given a robot $r$, an environment $E$, and two configurations of $r$ in $E$, denoted $s$ and $t$, and are tasked with finding a *valid* set of motions of $r$ that would take it from configuration $s$ to $t$. A motion is valid (or collision-free) if it does not result in $r$ colliding with itself or any object in the environment.

The problem's intractability \[\] lead to the development of randomized sampling based approaches. These sampling based motion planning (SBMP) algorithms reduce the problem to finding an $(s,t)$-curve in the implicit *configuration space* (c-space) \[\] defined by $r$ and $E$ that does not contain any point representing an invalid configuration. These methods create a geometric graph in c-space, also known as a *roadmap*, by sampling random points (configurations) and using them to expand the graph. The problem is then reduced further to that of finding a $(s,t)$-path in the graph.

The experiments included RRT 200 runs (with each neighborhood finder) on the simple passage and z-passage tasks, and 500 runs (with each neighborhood finder) on the clutter and 7DOF manipulator tasks.
VI-D System and implementation details
All of the experiment code relies on the C++ Parasol Planning Library (PPL) RRT and PRM implementations....

—c—c—c—c—c—c—c—c—c—c—c— \CodeBefore\rectanglecolorlightgray2-23-2 \rectanglecolorlightergray2-32-8 \rectanglecolorlightgray3-23-8 \rectanglecolorlightblue4-25-2 \rectanglecolorlighterblue4-34-8 \rectanglecolorlightblue5-25-8 \rectanglecolortan6-27-2 \rectanglecolorlighttan6-36-8 \rectanglecolortan7-27-8 \rectanglecolorlightgray8-29-2 \rectanglecolorlightergray8-38-8 \rectanglecolorlightgray9-29-8 \rectanglecolorlightblue10-211-2 \rectanglecolorlighterblue10-310-8 \rectanglecolorlightblue11-211-8 \rectanglecolortan12-213-2 \rectanglecolorlighttan12-312-8 \rectanglecolortan13-213-8 \rectanglecolorlightgray14-215-2...

Figure 4: An illustration of a point-to-segment distance calculation between p and s in a 2D c-space 𝒞space = 𝕋2. The two rotational DOFs are marked by θ1 and θ2, and V± is a set of 9 copies of 𝒞space. Marked in orange are the points in p± that give rise to the bisectors required for the point-to-segment distance, and the bisectors forming the Voronoi diagram 𝒱𝒟ℤ(p)....
