<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Interaction Aware Trajectory Planning for Merge Scenarios in Congested Traffic Situations

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In many traffic situations there are times where interaction with other drivers is necessary and unavoidable in order to safely progress towards an intended destination. This is especially true for merge manoeuvres into dense traffic, where drivers sometimes must be somewhat aggressive and show the intention of merging in order to interact with the other driver and make the driver open the gap needed to execute the manoeuvre safely. Many motion planning frameworks for autonomous vehicles adopt a reactive approach where simple models of other traffic participants are used and therefore need to adhere to large margins in order to behave safely. However, the large margins needed can sometimes get the system stuck in congested traffic where time gaps between vehicles are too small. In other situations, such as a highway merge, it can be significantly more dangerous to stop on the entrance ramp if the gaps are found to be too small than to make a slightly more aggressive manoeuvre and let the driver behind open the gap needed.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To remedy this problem, this work uses the Intelligent Driver Model (IDM) to explicitly model the interaction of other drivers and evaluates the risk by their required deceleration in a similar manner as the Minimum Overall Breaking Induced by Lane change (MOBIL) model that has been used in large scale traffic simulations before. This allows the algorithm to evaluate the effect on other drivers depending on our own trajectory plans by simulating the nearby traffic situation. Finding a globally optimal solution is often intractable in these situations so instead a large set of candidate trajectories are generated that are evaluated against the traffic scene by forward simulations of other traffic participants. By discretization and using an efficient trajectory generator together with efficient modelling of the traffic scene real-time demands can be met.
