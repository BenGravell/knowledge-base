<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Real-Time Motion Planning with Applications to Autonomous Urban Driving

Topics include Urban driving, Motion planning, Closed-loop planning, Rapidly-exploring trees, Autonomous vehicles, Real-time planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents closed-loop RRT for real-time autonomous-driving motion planning, simulating a tracking controller during tree expansion rather than planning only in open-loop state space. This makes sampled trajectories more dynamically realistic for urban driving maneuvers.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper describes a real-time motion planning algorithm, based on the rapidly-exploring random tree (RRT) approach, applicable to autonomous vehicles operating in an urban environment. Extensions to the standard RRT are predominantly motivated : 1) the need to generate dynamically feasible plans in real-time; 2) safety requirements; 3) the constraints dictated by the uncertain operating (urban) environment. The primary novelty is in the use of closed-loop prediction in the framework of RRT. The proposed algorithm was at the core of the planning and control software for Team MIT's entry for the 2007 DARPA Urban Challenge, where the vehicle demonstrated the ability to complete a 60 mile simulated military supply mission, while safely interacting with other autonomous and human driven vehicles.
