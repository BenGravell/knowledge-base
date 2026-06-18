<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimal Control of LTI Systems over Unreliable Communication Links

Topics include Networked control, Packet drops, Linear quadratic Gaussian control, Mean-square stability, TCP protocols, UDP protocols.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Studies optimal control of LTI systems when actuation commands or observations traverse unreliable links. By separating TCP-like acknowledged drops from UDP-like unacknowledged drops, it clarifies when certainty-equivalence style controllers survive and when packet-loss information changes the optimal policy.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, optimal control of linear time-invariant (LTI) systems over unreliable communication links is studied. The motivation of the problem comes from growing applications that demand remote control of objects over Internet-type or wireless networks where links are prone to failure. Depending on the availability of acknowledgment (ACK) signals, two different types of networking protocols are considered. Under a TCP structure, existence of ACK signals is assumed, unlike the UDP structure where no ACK packets are present. The objective here is to mean-square (m.s.) stabilize the system while minimizing a quadratic performance criterion when the information flow between the controller and the plant is disrupted due to link failures, or packet losses. Sufficient conditions for the existence of stabilizing optimal controllers are derived.
