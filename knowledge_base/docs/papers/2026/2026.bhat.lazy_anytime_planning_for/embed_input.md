<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Lazy Anytime Planning for the Dubins Moving Target Traveling Salesman Problem with Obstacles

Topics include Moving-target traveling salesman problem, Dubins paths, Lazy collision checking, Anytime planning, Generalized traveling salesman problem, Rapidly-exploring random tree connect.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Alternates optimistic generalized-TSP solutions with obstacle-aware Dubins RRT-Connect checks, lazily evaluating only edges needed by promising target-interception sequences. Repeated space-time sampling makes the method anytime and improves solution costs within a one-minute budget.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The Dubins Moving Target Traveling Salesman Problem with Obstacles (Dubins MT-TSP-O) seeks an obstacle-free trajectory for an agent with a fixed speed and minimum turning radius that intercepts several moving targets. To tackle this NP-hard problem, we introduce the Lazy Iterated Random Generalized TSP (Lazy IRG) algorithm. Each iteration of Lazy IRG samples a set of possible interception points in space-time along the trajectories of the targets. Lazy IRG then manages the high computational cost of motion planning by alternating between two steps: first, it optimistically selects a sequence of interception points by solving a Generalized TSP (GTSP) assuming an obstacle-free world; second, it searches for obstacle-free trajectories between consecutive points in the sequence using an obstacle-aware RRT-Connect planner. If a trajectory is not found, Lazy IRG solves the GTSP again; otherwise, Lazy IRG enters its next iteration and samples new interception points. By deferring expensive collision-checking, our method efficiently focuses computational effort on the most promising solutions.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Numerical results show that Lazy IRG finds significantly lower-cost solutions within a 1-minute time budget compared to the existing IRG-PGLNS algorithm.
