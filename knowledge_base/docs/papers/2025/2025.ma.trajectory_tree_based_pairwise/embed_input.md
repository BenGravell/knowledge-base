<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Trajectory Tree-Based Pairwise Game for Interactive Decision-Making and Motion Planning in Autonomous Driving

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Interactive decision-making and motion planning is essential for ensuring the safety and driving efficiency of autonomous vehicles. Game-based methods have demonstrated impressive performances in addressing these challenges due to their capability to explicitly model interactive behaviors. However, existing game-based approaches suffer from low computational efficiency owing to the numerical optimization required in continuous action spaces and the high dimensionality inherently present in multi-vehicle interaction scenarios. Also, accurately identifying the utility functions of opponent vehicles (OVs) from limited state observations remains a formidable challenge, which could result in conservative or even unsafe decisions by autonomous vehicles. To tackle these issues, a novel game-theoretic decision-making and motion planning framework is proposed. Specifically, the multi-vehicle interaction is transformed to a pairwise leader-follower game and further modelled by trajectory trees constructed with discrete action sets. To accurately compute the action values of these trajectory trees, we identify the utility functions of OVs from state observations by solving the elaborated restored optimal control problem. The optimal strategy for the trajectory trees is derived using dynamic programming framed within the context of a sequential game, which ensures that the varying behaviors of OVs are effectively considered.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The proposed method is comprehensively validated in two challenging interactive scenarios, and the results show that the trajectory tree-based interaction modeling approach significantly enhances the computational efficiency of game-based methods. Additionally, the identified utility functions of OVs provide a better interpretation of their observed behaviors and ensure safer decision-making and motion planning for autonomous vehicles.
