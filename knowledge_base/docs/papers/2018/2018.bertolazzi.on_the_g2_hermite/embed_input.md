<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the G2 Hermite Interpolation Problem with Clothoids

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The G2 Hermite Interpolation Problem with clothoid curves requires to find the interpolating clothoid that matches initial and final positions, tangents and curvatures, also known as G2 Hermite data. In the paper we prove that this problem does not always admit solution with only one clothoid segment, nor with two, as some counterexamples show. The general fitting scheme herein proposed requires three arcs determined via the solution of a nonlinear system of 8 equations in 10 unknowns. We discuss how it is possible to recast this system to 2 equations and how to efficiently solve it by means of the Newton method. The choice of the clothoid is crucial because it exhibits the curvature which is linear with the arc length, an important property in many applications ranging from path planning for autonomous vehicles, road design, manufacturing and graphics. The algorithm is tested on a fine hypercube of all possible configurations of angles and curvatures. It always converges and in the worst case it requires 5 standard Newton iterations.
