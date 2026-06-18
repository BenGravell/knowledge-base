<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Spoof Resilient Coordination for Distributed Multi-robot Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

As cyber-physical networks become increasingly equipped with embedded sensing, communication, computation, and actuation capabilities, they are made vulnerable to malicious attacks by increasing the number of access points which are available for attackers. A particularly pernicious attack is spoofing, in which a malicious agent spawns multiple identities or impersonates legitimate agents to gain a disproportionate advantage. Spoofing attacks can easily compromise otherwise attack-resilient algorithms and network structures that assume an upper bound on the number of malicious agents in the network. We generalize a class of resilient consensus strategies, known as Weighted Mean-Subsequence-Reduced (W-MSR) consensus, to further provide spoof resilience by incorporating a physical fingerprint analysis of signals received from neighboring agents. By comparing the physical fingerprints of received signals, legitimate agents can identify and isolate malicious agents that attempt spoofing attacks. We quantify the effects of delays in detecting spoofing and inexact detection due to noise in the received signals. Numerical simulations illustrate the effectiveness of the proposed methods. Our framework is applicable to a variety of problems involving multi-robot systems coordinating via wireless communication, including coverage, distributed estimation, and formation control.
