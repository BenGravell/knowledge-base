<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sample Complexity of Episodic Fixed-Horizon Reinforcement Learning

Topics include Reinforcement learning, Sample complexity, Learning, Markov decision process, Time horizon.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recently, there has been significant progress in understanding reinforcement learning in discounted infinite-horizon Markov decision processes (MDPs) by deriving tight sample complexity bounds. However, in many real-world applications, an interactive learning agent operates for a fixed or bounded period of time, for example tutoring students for exams or handling customer service requests. Such scenarios can often be better treated as episodic fixed-horizon MDPs, for which only looser bounds on the sample complexity exist. A natural notion of sample complexity in this setting is the number of episodes required to guarantee a certain performance with high probability (PAC guarantee). In this paper, we derive an upper PAC bound tilde O(|mathcal S|^ |mathcal A| H^/epsilon^ lnfrac 1 delta) and a lower PAC bound tilde Omega(|mathcal S| |mathcal A| H^/epsilon^ ln frac 1 delta+ c) that match up to log-terms and an additional linear dependency on the number of states |mathcal S|. The lower bound is the first of its kind for this setting.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our upper bound leverages Bernstein's inequality to improve on previous bounds for episodic finite-horizon MDPs which have a time-horizon dependency of at least H^.
