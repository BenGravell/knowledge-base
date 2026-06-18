<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On-Line Q-Learning Using Connectionist Systems

Topics include Reinforcement learning, Q-learning, Function approximation, Neural networks, Online learning, Robot navigation, Temporal difference learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends Q-learning to continuous-state problems using neural-network function approximation and online temporal-difference updates during trials. The report introduces Modified Connectionist Q-Learning and compares it with Q(lambda) and replay-style updates on a simulated robot-navigation task, emphasizing robustness when trials do not have clean endpoints.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reinforcement learning algorithms are a powerful machine learning technique. However, much of the work on these algorithms has been developed with regard to discrete finite-state Markovian problems, which is too restrictive for many real-world environments. Therefore, it is desirable to extend these methods to high dimensional continuous state-spaces, which requires the use of function approximation to gener-alise the information learnt by the system. In this report, the use of back-propagation neural networks is considered in this context. We consider a number of different algorithms based around Q-Learning combined with the Temporal Difference algorithm, including a new algorithm (Modified Connectionist Q-Learning), and Q(lambda). In addition, we present algorithms for applying these updates on-line during trials, unlike backward replay used by Lin that requires waiting until the end of each trial before updating can occur. On-line updating is found to be more robust to the choice of training parameters than backward replay, and also enables the algorithms to be used in continuously operating systems where no end of trial conditions occur. We compare the performance of these algorithms on a realistic robot navigation problem, where a simulated mobile robot is trained to guide itself to a goal position in the presence of obstacles.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The robot must rely on limited sensory feedback from its surroundings, and make decisions that can be generalised to arbitrary layouts of obstacles. These simulations show that on-line learning algorithms are less sensitive to the choice of training parameters than backward replay, and that the alternative update rules of MCQ-L and Q(lambda) are more robust than standard Q-learning updates.
